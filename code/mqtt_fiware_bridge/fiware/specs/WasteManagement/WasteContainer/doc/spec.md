# Waste Container

**Note: The latest version of this Data Model can be found at
[https://github.com/smart-data-models/dataModel.WasteManagement](https://github.com/smart-data-models/dataModel.WasteManagement)**

## Description

A waste container.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](http://fiware.github.io/data-models/specs/WasteManagement/WasteContainer/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `WasteContainer`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `location` : Container's location represented by a GeoJSON Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not present.

-   `address`: Civic address where the container is located.

    -   Attribute type: Property. [Address](https://schema.org/address)
    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Mandatory if `location` is not present.

-   `fillingLevel` : Filling level of the container (percentage, expressed in
    parts per one). When the container is full it must be equal to `1.0`. When
    the container is empty it must be equal to `0.0`.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.
    -   Allowed values: Interval \[0,1\].
    -   Optional

-   `fullnessThreshold` : The level at which the container will generate a
    warning (percentage, expressed in parts per one). If the filling level
    passes this threshold, action should be taken to clean the container.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.
    -   Allowed values: Interval \[0,1\].
    -   Optional

-   `cargoWeight` : Weight of the container load.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:

        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type:[DateTime](http://schema.org/DateTime)
        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.

    -   Default Unit: Kilograms.
    -   See also: [https://schema.org/weight](https://schema.org/weight)
    -   Optional

-   `temperature` : Temperature inside the container.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:

        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.

    -   Default unit: Celsius Degrees.
    -   Optional

-   `methaneConcentration` : Methane (CH4) concentration inside the container.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Attribute metadata:

        -   `timestamp`: Timestamp when the last update of the attribute
            happened.

            -   Type: [DateTime](http://schema.org/DateTime)

        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.

    -   Default unit: Micrograms per cubic meter.
    -   Optional

-   `storedWasteOrigin` : Origin of the waste stored.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`household`, `municipal`, `industrial`,
        `construction`, `hostelry`, `agriculture`, `other`) - or any other value
        which does not fit within the former.
    -   Optional

-   `storedWasteKind` : Kind/s of waste stored by the container.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Allowed values: (`organic`, `inorganic`, `glass`, `oil`, `plastic`,
        `metal`, `paper`, `batteries`, `electronics`, `hazardous`, `other`) - Or
        any other value which does not fit within the former.
    -   Optional

-   `storedWasteCode` : As per the regulation, waste codes which precisely
    identifies waste origin and kind.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Allowed values: Depend on the target regulation. For Europe, check
        [Europe's List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm).
    -   Optional

-   `refWasteContainerModel` : Container's model.

    -   Attribute type: Relationship. Reference to a
        [WasteContainerModel](../../WasteContainerModel/doc/spec.md) entity.
    -   Optional

-   `serialNumber` : Serial number of the container.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        [https://schema.org/serialNumber](https://schema.org/serialNumber)
    -   Optional

-   `regulation` : Regulation under which the container is operating.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Optional

-   `responsible` : Responsible for the container, i.e. entity in charge of
    actuating (emptying, collecting etc.).

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `owner` : Container's owner.

    -   Attribute type: Property. List of [Text](http://schema.org/Text) or List
        of URIs
    -   Optional

-   `dateServiceStarted` : Date at which the container started giving service.

    -   Attribute type: Property. [Date](http://schema.org/Date)
    -   Optional

-   `dateLastEmptying` : Timestamp which represents when the container was
    emptied last time.

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Optional

-   `nextActuationDeadline` : Deadline for next actuation to be performed
    (emptying, picking up, etc.).

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Optional

-   `actuationHours` : Hours suitable for performing actuations over the
    container.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Normative References: Value must be compliant with
        [https://schema.org/openingHours](https://schema.org/openingHours)

-   `dateLastCleaning` : When the container was cleaned last time.

    -   Attribute type: Property. [DateTime](http://schema.org/Date)
    -   Optional

-   `nextCleaningDeadline` : Deadline for next cleaning.

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Optional

-   `refWasteContainerIsle` : Isle where the container is placed.

    -   Attribute Type: Reference to a
        [WasteContainerIsle](../../WasteContainerIsle/doc/spec.md) entity.
    -   Optional

-   `isleId` : Identifier (or name) of the isle where the container is placed.
    This attribute should be used when entities of type `WasteContainerIsle` are
    not being modelled specifically. Otherwise, `refWasteContainerIsle` should
    be used.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `category` : Container's category.

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Allowed Values: All values allowed for the `category` property of
        [WasteContainerModel](../../WasteContainerModel/doc/spec.md).
        -   `fixed`. Container is fixed to a wall, support or handle.
        -   `underground`. Container is placed underground.
        -   `ground`. Container is placed at ground level.
        -   `portable`. Container can be moved around a certain extent.
        -   Any other value which captures an aspect not covered by those
            referred above.

-   `status` : Container's status from the point of view of safety.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Allowed Values:
        -   `ok`. Container is where it must be and stands properly.
        -   `lidOpen`. Container's lid has been opened and not closed after a
            certain amount of time.
        -   `dropped`. Container has been dropped for some reason.
        -   `moved`. Container has been moved from its regular position and has
            not come back.
        -   `vandalized`. Container has been damaged or destroyed due to
            vandalism.
        -   `burning`. Container is burning and an immediate action has to be
            taken.
        -   `unknown`. The status of the container is not known to the system.
    -   Attribute metadata:

        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
        -   `TimeInstant` :
            [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
            saved by FIWARE's IoT Agents. Note: This attribute has not been
            harmonized to keep backwards compatibility with current FIWARE
            reference implementations.
            -   Type: [DateTime](https://schema.org/DateTime). There can be
                production environmments where the attribute type is equal to
                the `ISO8601` string. If so, it must be considered as a synonym
                of `DateTime`.

    -   Optional

-   `color` : Container's color

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Allowed Values: - A color keyword as specified by
        [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords) -
        A color value as specified by
        [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)
    -   See also: [https://schema.org/color](https://schema.org/color)
    -   Optional

-   `image` : A URL containing a photo of the container.

    -   Normative References:
        [https://schema.org/image](https://schema.org/image)
    -   Optional

-   `description` : Description about the container.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `annotations` : A field reserved for annotations (incidences, remarks,
    etc.).

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Optional

-   `areaServed` : Higher level area to which the container belongs to. It can
    be used to group containers per responsible, district, neighbourhood, etc.

    -   Normative References:
        [https://pending.schema.org/areaServed](https://pending.schema.org/areaServed)
    -   Optional

-   `dateModified` : Last update timestamp of this entity

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `TimeInstant` :
    [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
    saved by FIWARE's IoT Agent as per dynamic IoT data arrival. Note: This
    attribute has not been harmonized to keep backwards compatibility with
    current FIWARE reference implementations.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime). There
        can be production environmments where the attribute type is equal to the
        `ISO8601` string. If so, it must be considered as a synonym of
        `DateTime`.

    -   Optional

-   `refDevice` : Reference to the device(s) used to monitor this container.
    -   Attribute type: Relationship. List of Reference to entity(ies) of type
        [Device](../../../Device/Device/doc/spec.md)
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "wastecontainer:Fleming:12a",
    "type": "WasteContainer",
    "status": {
        "value": "ok"
    },
    "category": {
        "value": ["underground"]
    },
    "dateLastEmptying": {
        "type": "DateTime",
        "value": "2016-06-21T15:05:59.408Z"
    },
    "serialNumber": {
        "value": "ab56kjl"
    },
    "nextActuationDeadline": {
        "value": "2016-06-28T15:05:59.408Z"
    },
    "refWasteContainerIsle": {
        "type": "Relationship",
        "value": "wastecontainerisle:Fleming:12"
    },
    "refDevice": {
        "type": "Relationship",
        "value": ["device-Fleming:12a:1"]
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [-3.164485591715449, 40.62785133667262]
        }
    },
    "fillingLevel": {
        "value": 0.4
    },
    "refWasteContainerModel": {
        "type": "Relationship",
        "value": "wastecontainermodel:c1"
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "wastecontainer:Fleming:12a",
    "type": "WasteContainer",
    "refWasteContainerModel": "wastecontainermodel:c1",
    "refWasteContainerIsle": "wastecontainerisle:Fleming:12",
    "serialNumber": "ab56kjl",
    "location": {
        "type": "Point",
        "coordinates": [-3.164485591715449, 40.62785133667262]
    },
    "fillingLevel": 0.4,
    "dateLastEmptying": "2016-06-21T15:05:59.408Z",
    "nextActuationDeadline": "2016-06-28T15:05:59.408Z",
    "status": "ok",
    "category": ["underground"],
    "refDevice": ["device-Fleming:12a:1"]
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",
    "type": "WasteContainer",
    "status": {
        "type": "Property",
        "value": "ok"
    },
    "category": {
        "type": "Property",
        "value": ["underground"]
    },
    "dateLastEmptying": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2016-06-21T15:05:59.408Z"
        }
    },
    "serialNumber": {
        "type": "Property",
        "value": "ab56kjl"
    },
    "nextActuationDeadline": {
        "type": "Property",
        "value": "2016-06-28T15:05:59.408Z"
    },
    "refWasteContainerIsle": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12"
    },
    "refDevice": {
        "type": "Relationship",
        "object": ["urn:ngsi-ld:Device:device-Fleming:12a:1"]
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [-3.164485591715449, 40.62785133667262]
        }
    },
    "fillingLevel": {
        "type": "Property",
        "value": 0.4
    },
    "refWasteContainerModel": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1"
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Test it with real services

## Open issues
