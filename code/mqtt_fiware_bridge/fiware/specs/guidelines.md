# Data models guidelines

This is a set of guidelines for defining new data models. Further information
and a guideline update can be found at
[D2.2 Synhronicity IoT LSP](http://synchronicity-iot.eu/wp-content/uploads/2018/05/synchronicity_d2_2_guidelines_for_the_definition_of_oasc_shared_data_models.pdf)

Before creating a new data model, explore the existing ones to be sure there is
already a data model that covers your use case. The search box in the
ReadTheDocs page can help you to search for specification connected to your
needs. Recall to use synonyms in your search. E.g. what you might call Public
Transport already exists under UrbanMobility.

If you are looking for guidelines on adoption of existing data models, please
refer to [How to use FIWARE Harmonised Data Models in your projects](howto.md)
section.

## Syntax

-   Use English terms, preferably American English.
-   Use camel case syntax for attribute names (`camelCase`).
-   Entity Type names must start with a Capital letter, for instance,
    `WasteContainer`.
-   Use names and not verbs for Attributes of type Property, ex. `name`,
    qualifying it when necessary, ex. `totalSpotNumber` or `dateCreated`.
-   Avoid plurals in Attribute names, but state clearly when a list of items
    fits. Ex. `category`.

## Reuse

-   Check for the existence of the same Attribute on any of the other models and
    reuse it, if pertinent.
-   Have a look at [schema.org](http://schema.org) trying to find a similar term
    with the same semantics.
-   Try to find common used ontologies or existing standards well accepted by
    the Community, or by goverments, agencies, etc. For instance,
    [Open311](http://www.open311.org/) for civic issue tracking or
    [Datex II](http://www.datex2.eu/) for transport systems.

## Data types

-   When possible reuse schema.org data types (`Text`, `Number`, `DateTime`,
    `StructuredValue`, etc.).
-   Remember that `null` is not allowed in NGSI-LD and therefore should be
    avoided as a value.

## Attribute definition

-   Enumerate the allowed values for each attribute. Generally speaking it is a
    good idea to leave it open for applications to extend the list, provided the
    new value is not semantically covered by any of the existing ones.

-   State clearly what attributes are mandatory and what are optional. Remember
    that `null` value should be avoided as it is prohibited in NGSI-LD.

## Units

-   Define a default unit for magnitudes. Normally it will be the unit as stated
    by the International System of Units.

-   If a quantity is expressed in a different unit than the default one, use the
    [unitCode](http://schema.org/unitCode) metadata attribute in NGSI v2.

-   In NGSI-LD the Property `unitCode` is already defined and available to be
    used.

## Relative values

-   Use values between `0` and `1` for relative quantities, which represent
    attribute values such as `relativeHumidity`, `precipitationProbability`,
    etc.

## Modelling location

-   Use `address` attribute for civic locations as per
    [schema.org](http://schema.org/address)

-   Use the `location` Attribute for geographical coordinates. GeoJSON must be
    used for encoding geospatial properties.

## Modelling linked data

-   When an Entity Attribute is used as a link (relationship) to other entities
    two modelling options are possible:

    1.  Name the attribute with the prefix `ref` plus the name of the target
        (linked) entity type. For instance `refStreetlightModel`, represents an
        attribute which contains a reference to an entity of type
        `StreetlightModel`. This option has been extensively used by data models
        initially intended to be used with NGSI v2 .

    2.  Name the attribute using a verb (plus optionally an object) such as
        `hasStop`, `operatedBy`, `hasTrip`, etc. This option is the one
        advocated by NGSI-LD, as in NGSI-LD URNs are used to identify entities,
        and NGSI-LD URNs already convey the type of the target entity, for
        instance `urn:ngsi-ld:gtfs:Stop:S123`.

As the current trend is to align with NGSI-LD as much as possible, 2. option can
be considered as the recommended one and 1. option is to some extent
"deprecated".

## Date Attributes

-   In NGSI v2 the Attribute type must be `DateTime`.

-   In NGSI-LD, please check the date and time encoding at the
    [NGSI-LD FAQ](https://github.com/FIWARE/data-models/blob/master/specs/ngsi-ld_howto.md#airquality-in-ngsi-ld-format).

-   Use the `date` prefix for naming entity attributes representing dates (or
    complete timestamps). Ex. `dateLastEmptying`.

-   `dateCreated` (`createdAt` in NGSI-LD) must be used to denote the (digital)
    Entity's creation date.

-   `dateModified` (`modifiedAt` in NGSI-LD) must be used to denote the
    (digital) Entity's last update date.

-   `dateCreated` and `dateModified` are special Entity Attributes provided
    off-the-shelf by NGSI implementations. Be careful because they can be
    different than the actual creation or update date of the real world entity
    represented by its corresponding digital entity.

-   When necessary define additional Attributes to capture precisely all the
    details about dates. For instance, to denote the date at which a weather
    forecast was delivered an attribute named `dateIssued` can be used. In that
    particular case just reusing `dateCreated` would be incorrect because the
    latter would be the creation date of the (digital) entity representing the
    weather forecast which typically might have a delay.

## Dynamic attributes

-   In NGSI v2 use a metadata attribute named `timestamp` for capturing the last
    update timestamp of a dynamic attribute. Please note that this is the actual
    date at which the measured value was obtained (from a sensor, by visual
    observation, etc.), and that date might be different than the date (metadata
    attribute named `dateModified` as per NGSI v2) at which the attribute of the
    digital entity was updated, as typically there might be delay, specially on
    IoT networks which deliver data only at specific timeslots.

-   In NGSI-LD use the `observedAt` Property to convey timestamps.

## Internationalization (i18N)

There can be certain entity attributes which content is subject to be
internationalized. For instance, the description of a Point of Interest. The
internationalization (i18N) guidelines for the FIWARE Data Models are defined as
follows:

-   By default, the value of an attribute subject to be internationalized
    _should_ be expressed in **American English** (`en-US`). However there can
    be situations where an English term is not the most common one, for
    instance, the English exonym for the city of Livorno (Italy) is a very
    obscure term, `Leghorn`. In such situations, the common international name
    (`Livorno` in our example) in latin script should be used.

-   There shall always be a term for the original attribute, i.e. it is not
    allowed to have Entity representations which only contain terms associated
    to language variants.

-   For each language variant of an internationalized attribute, there shall be
    an additional Entity Attribute which name shall be in the form:

`<AttributeName>_<LanguageTag>` where `AttributeName` is the original attribute
name and `LanguageTag` shall be a language tag as mandated by
[RFC 5646](https://www.rfc-editor.org/rfc/rfc5646.txt). W3C provides guidelines
on
[how to use language tags](https://www.w3.org/International/articles/language-tags/).

[JSON-LD](https://www.w3.org/TR/json-ld/#string-internationalization) can
facilitate developers to parse internationalized Entity representations, thus
Context Data Producers are encouraged to use JSON-LD (provided that the backing
implementations support it).

When parsing plain JSON content, developers should validate that the
corresponding JSON terms are actually conveying a language variant of an
attribute. For instance, by validating that the term's suffix actually
corresponds to a valid language tag and by checking that the corresponding
original attribute is contained in the entity.

Example:

An entity may contain an attribute named `description`. The value of such
attribute shall be expressed in American English. Additionally it might exist an
attribute named `description_es` used to convey the value of such a
`description` attribute in Spanish.

## Some of the most used attributes

In case of doubt check the existing data models!

-   `name`
-   `alternateName`
-   `description`
-   `serialNumber`
-   `category`
-   `features`
-   `source`
-   `relativeHumidity`
-   `temperature`

## Versioning

FIWARE Data Models Project aim to maintain backwards compatibility, however some
incompatibilities will inevitably occur over time. Data providers may choose to
tag Entities with an additional `schemaVersion` Attribute so that Data Consumers
can behave accordingly. This aligns with the
[https://schema.org/schemaVersion](https://schema.org/schemaVersion) Property
definition.

## How to contribute

Contributions should come in the form of pull requests.
[Fork](https://help.github.com/articles/fork-a-repo/) the repository,
[Create a branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/)
containing your changes, and proceed with a
[Pull Request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

Pull Request should be easy to review, so if the model, or the changes you are
proposing are wide, please create different pull requests.

New data models should be added under a folder structured as follows:

-   `specs/`
    -   `NewModel/`
        -   `doc/`
            -   `spec.md`: A data model description based on the
                [data model template](https://github.com/FIWARE/data-models/blob/master/datamodel_template.md),
                e.g.
                [spec.md of WeatherObserved](./Weather/WeatherObserved/doc/spec.md).
        -   `README.md`: A summary file (as an extract from the spec file), e.g.
            [README.md of WeatherObserved](https://github.com/FIWARE/data-models/tree/master/specs/Weather/WeatherObserved)
        -   `schema.json`: The JSON Schema definition, e.g.
            [schema.json of WeatherObserved](./Weather/WeatherObserved/schema.json)
        -   `example.json`: One or more JSON example file, e.g.
            [example.json of WeatherObserved](./Weather/WeatherObserved/example.json)
        -   `example-normalized.json`: One or more JSON example file in NGSI v2
            normalized format, e.g.
            [example-normalized.json of WeatherObserved](./Weather/WeatherObserved/example-normalized.json)
        -   `example-normalized-ld.jsonld`: One or more JSON example file in
            **NGSI-LD** normalized format, e.g.
            [example-normalized-ld.jsonld of WeatherObserved](./Weather/WeatherObserved/example-normalized-ld.jsonld)

The name of the folder should match the Entity Type used in the JSON Schema
(e.g. `NewModel`). For data models including more entities, a hierarchical
folder should be used. The father folder can include common JSON schemas shared
among the entities. e.g.:

-   `specs/`
    -   `NewModel/`
        -   `doc/`
            -   `spec.md`
        -   `README.md`
        -   `newmodel-schema.json`: the common schema for the different
            entities.
        -   `NewModelEntityOne/`
            -   `doc/`
                -   `spec.md`
            -   `README.md`
            -   `schema.json`
            -   `example.json`
            -   `example-normalized.json`
            -   `example-normalized-ld.jsonld`
        -   `NewModelEntityTwo/`
            -   `doc/`
                -   `spec.md`
            -   `README.md`
            -   `schema.json`
            -   `example.json`
            -   `example-normalized.json`
            -   `example-normalized-ld.jsonld`
