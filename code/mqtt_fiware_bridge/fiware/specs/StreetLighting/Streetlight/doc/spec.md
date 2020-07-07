# Streetlight

**Note: The latest version of this Data Model can be found at
[https://github.com/smart-data-models/dataModel.Streetlighting](https://github.com/smart-data-models/dataModel.Streetlighting)**

An entity of type `Streetlight` represents a urban streetlight. Actually, there
will be an entity of type `Streetlight` per lamp. Thus, if a particular pole
holds more than one lantern there will be as many streetlight entites as
installed lamps. As a result there might be more than one streetlight entity per
location. A `Streetlight` entity does not contain any attribute corresponding to
structural characteristics. Such data is captured by entities of type
`StreetlightModel`.

## Data Model

The data model is defined as shown below:

-   `id` : Entity's unique identifier.

-   `type` : It must be equal to `Streetlight`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `location` : Streetlight's location represented by a GeoJSON Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    -   Mandatory if `address` is not present.

-   `address` : Civic address where the streetlight is located.

    -   Attribute type: Property. [Address](https://schema.org/address)
    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Mandatory if `location` is not present.

-   `areaServed` : Higher level area to which this streetlight belongs to. It
    can be used to group streetlights per responsible, district, neighbourhood,
    etc.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        [https://schema.org/areaServed](https://schema.org/areaServed)
    -   Optional

-   `circuit` : The circuit to which this streetlight connects to and gets power
    from. Typically it will contain an identifier that will allow to obtain more
    information about such circuit.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `refStreetlightModel` : Streetlight's model.

    -   Attribute type : Reference to a
        [StreetlightModel](../../StreetlightModel/doc/spec.md) entity.
    -   Optional

-   `refStreetlightControlCabinet` : If this streetlight is individually
    controlled, reference to the control cabinet in charge of.

    -   Attribute type : Reference to a
        [StreetlightControlCabinet](../../StreetlightControlCabinet/doc/spec.md)
        entity.
    -   Optional

-   `status` : The overall status of this street light.

    -   Attribute type: Relationship. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`ok`, `defectiveLamp`, `columnIssue`,
        `brokenLantern`)
        -   Or any other value meaningful to the application and not covered by
            the values above.
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Mandatory

-   `powerState` : Streetlight's power state.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Attribute metadata:
        -   `timestamp` : Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Allowed values: one Of (`on`, `off`, `low`, `bootingUp`)
    -   Optional

-   `refDevice` : Reference to the device(s) used to monitor this streetligth.

    -   Attribute type: Relationship. List of Reference to entity(ies) of type
        [Device](../../../Device/Device/doc/spec.md)
    -   Optional

-   `refStreetlightGroup` : Streetlight's group, if this streetlight belongs to
    any group.

    -   Attribute type : Reference to a
        [StreetlightGroup](../../StreetlightGroup/doc/spec.md) entity.
    -   Optional

-   `dateLastLampChange` : Timestamp of the last change of lamp made.

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Attribute metadata:
        -   `timestamp` : Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Optional

-   `dateLastSwitchingOn` : Timestamp of the last switching on.

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Attribute metadata:
        -   `timestamp` : Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Optional

-   `dateLastSwitchingOff` : Timestamp of the last switching off.

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Attribute metadata:
        -   `timestamp` : Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Optional

-   `controllingMethod` : The method used to control this streetlight.

    -   Attribute type: Relationship. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`group`, `individual`)
    -   Optional

-   `dateModified` : Timestamp of the last update made to this entity

    -   Attribute type: Property. [DateTime](http://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateServiceStarted` : Date at which the streetlight started giving service.

    -   Attribute type: Property. [Date](http://schema.org/Date)
    -   Optional

-   `image` : A URL containing a photo of the streetlight.

    -   Normative References:
        [https://schema.org/image](https://schema.org/image)
    -   Optional

-   `description` : Description about the streetlight.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `annotations` : A field reserved for annotations (incidences, remarks,
    etc.).

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Optional

-   `locationCategory` : Category of the location where the streetlight is
    placed.

    -   Attribute type:
    -   Allowed values: oneOf (`façade`, `sidewalk`, `pedestrianPath`, `road`,
        `playground`, `park`, `garden`, `bridge`, `tunnel`, `parking`,
        `centralIsland`)
        -   Or any other value with semantics not covered by the above list.

-   `lanternHeight` : Lantern's height. In columns with many arms this can vary
    between streetlights. Another variation source of this property are
    wall-mounted streetlights.

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Default unit: Meters.
    -   Optional

-   `illuminanceLevel` : Relative illuminance level setting.
    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: A number between 0 and 1.
    -   Attribute metadata:
        -   `timestamp`: Timestamp when the last update of the attribute
            happened.
            -   Type: [DateTime](http://schema.org/DateTime)
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "streetlight:guadalajara:4567",
    "type": "Streetlight",
    "status": {
        "value": "ok"
    },
    "powerState": {
        "value": "off"
    },
    "circuit": {
        "value": "C-456-A467"
    },
    "locationCategory": {
        "value": "centralIsland"
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [-3.164485591715449, 40.62785133667262]
        }
    },
    "areaServed": {
        "value": "Roundabouts city entrance"
    },
    "controllingMethod": {
        "value": "individual"
    },
    "refStreetlightGroup": {
        "type": "Relationship",
        "value": "streetlightgroup:G345"
    },
    "dateLastLampChange": {
        "type": "DateTime",
        "value": "2016-07-08T08:02:21.753Z"
    },
    "lanternHeight": {
        "value": 10
    },
    "refStreetlightModel": {
        "type": "Relationship",
        "value": "streetlightmodel:STEEL_Tubular_10m"
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "streetlight:guadalajara:4567",
    "type": "Streetlight",
    "location": {
        "type": "Point",
        "coordinates": [-3.164485591715449, 40.62785133667262]
    },
    "areaServed": "Roundabouts city entrance",
    "status": "ok",
    "refStreetlightGroup": "streetlightgroup:G345",
    "refStreetlightModel": "streetlightmodel:STEEL_Tubular_10m",
    "circuit": "C-456-A467",
    "lanternHeight": 10,
    "locationCategory": "centralIsland",
    "powerState": "off",
    "controllingMethod": "individual",
    "dateLastLampChange": "2016-07-08T08:02:21.753Z"
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",
    "type": "Streetlight",
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [-3.164485591715449, 40.62785133667262]
        }
    },
    "areaServed": {
        "type": "Property",
        "value": "Roundabouts city entrance"
    },
    "status": {
        "type": "Property",
        "value": "ok"
    },
    "refStreetlightGroup": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345"
    },
    "refStreetlightModel": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m"
    },
    "circuit": {
        "type": "Property",
        "value": "C-456-A467"
    },
    "lanternHeight": {
        "type": "Property",
        "value": 10
    },
    "locationCategory": {
        "type": "Property",
        "value": "centralIsland"
    },
    "powerState": {
        "type": "Property",
        "value": "off"
    },
    "controllingMethod": {
        "type": "Property",
        "value": "individual"
    },
    "dateLastLampChange": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2016-07-08T08:02:21.753Z"
        }
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Test it with a real service

## Open Issues

-   Initially is not considered practical to monitor individual power
    consumptions
