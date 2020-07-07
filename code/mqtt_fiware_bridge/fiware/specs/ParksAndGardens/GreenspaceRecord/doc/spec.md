# GreenspaceRecord

## Description

This entity contains a harmonised description of the conditions recorded on a
particular area or point inside a greenspace (flower bed, garden, etc.). This
entity type has been inspired by the `AgriParcelRecord` entity type defined by
the GSMA Harmonized Data Models.

## Data Model

A JSON Schema corresponding to this data model can be found
{{add link to JSON Schema}}

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `GreenspaceRecord`.

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.
    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.
-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `location` : Location of the area concerned by this record and represented
    by a GeoJSON geometry.
    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory
-   `dateObserved` : The date and time of this observation in ISO8601 UTCformat.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime).
    -   Mandatory

-   `soilTemperature` : The observed soil temperature in Celsius degrees.
    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Default unit: Celsius degrees.
    -   Attribute metadata:
        -   `timestamp` : optional timestamp for the observed value. It can be
            omitted if the observation time is the same as the one captured by
            the `dateObserved` attribute at entity level.
    -   Optional
-   `soilMoistureVwc` : The observed soil moisture measured as Volumetric Water
    Content, VWC (percentage, expressed in parts per one).

    -   Attribute type: Property. [Number](https://schema.org/Number) between 0
        and 1.
    -   Attribute metadata:
        -   `timestamp` : optional timestamp for the observed value. It can be
            omitted if the observation time is the same as the one captured by
            the `dateObserved` attribute at entity level.
    -   Optional

-   `soilMoistureEc` : The observed soild moisture measured as Electrical
    Conductivity, EC in units of Siemens per meter (S/m).

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Default unit: Siemens per meter (S/m).
    -   Attribute metadata:
        -   `timestamp` : optional timestamp for the observed value. It can be
            omitted if the observation time is the same as the one captured by
            the `dateObserved` attribute at entity level.
    -   Optional

-   `refGreenspace` : The garden or flower bed to which this record refers to.

    -   Attribute type: Relationship. Reference to an entity of type `Garden` or
        `FlowerBed`.
    -   Optional

-   `refDevice` : The device or devices used to obtain the data expressed by
    this record.
    -   Attribute type: Relationship. Reference to an entity of type `Device`
    -   Optional

### Representing related weather conditions

There are two options for representing weather conditions (air temperature,
humidity, etc.) observed at the area:

-   A/ Through a linked entity of type `WeatherObserved` (attribute named
    `refWeatherObserved`).
-   B/ Through a group of weather-related properties already defined by
    [WeatherObserved](../../../Weather/WeatherObserved/doc/spec.md).

Below is the description of the attribute to be used for option A/.

-   `refWeatherObserved` : Weather observed associated to the measurements
    described by this entity.
    -   Attribute type: Relationship. Reference to a
        [WeatherObserved](../../../Weather/WeatherObserved/doc/spec.md) entity.
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "Santander-Garden-Piquio-Record-1",
    "type": "GreenspaceRecord",
    "refGreenspace": {
        "type": "Relationship",
        "value": "Santander-Garden-Piquio"
    },
    "temperature": {
        "value": 17
    },
    "soilTemperature": {
        "value": 13
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [-3.7836974, 43.4741091]
        }
    },
    "relativeHumidity": {
        "value": 0.87
    },
    "dateObserved": {
        "type": "DateTime",
        "value": "2019-01-15T12:00:00Z"
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "Santander-Garden-Piquio-Record-1",
    "type": "GreenspaceRecord",
    "location": {
        "type": "Point",
        "coordinates": [-3.7836974, 43.4741091]
    },
    "temperature": 17,
    "relativeHumidity": 0.87,
    "soilTemperature": 13,
    "refGreenspace": "Santander-Garden-Piquio",
    "dateObserved": "2019-01-15T12:00:00Z"
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:GreenspaceRecord:Santander-Garden-Piquio-Record-1",
    "type": "GreenspaceRecord",
    "refGreenspace": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:Greenspace:Santander-Garden-Piquio"
    },
    "temperature": {
        "type": "Property",
        "value": 17
    },
    "soilTemperature": {
        "type": "Property",
        "value": 13
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [-3.7836974, 43.4741091]
        }
    },
    "relativeHumidity": {
        "type": "Property",
        "value": 0.87
    },
    "dateObserved": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2019-01-15T12:00:00Z"
        }
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Use it with a real service

Soon to be available

## Open Issues
