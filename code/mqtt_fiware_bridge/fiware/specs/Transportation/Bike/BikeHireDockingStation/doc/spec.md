# Bike Hire Docking Station

**Note: The latest version of this Data Model can be found at
[https://github.com/smart-data-models/dataModel.Transportation](https://github.com/smart-data-models/dataModel.Transportation)**

## Description

Many cities provide a bike hiring system for citizens. These can hire a bike
base on different types of subscriptions. A bike hire docking station where
subscribed users can hire and return a bike. It provides data about its main
features and availability of bikes and free slots.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://fiware.github.io/data-models/specs/Transportation/Bike/BikeHireDockingStation/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `BikeHireDockingStation`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Normative References:
        [http://schema.org/DateTime](http://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Normative References:
        [http://schema.org/DateTime](http://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Geolocation of the station represented by a GeoJSON
    (Multi)Polygon or Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not defined.

-   `address` : Registered docking station site civic address.

    -   Attribute type: Property. [Address](https://schema.org/address)
    -   Normative References:
        [https://schema.org/address](https://schema.org/address)
    -   Mandatory if `location` is not defined.

-   `name` : Name given to the docking station.

    -   Attribute type: Property. [Text](https://schema.org/Text).
    -   Normative References: `https://uri.etsi.org/ngsi-ld/name` equivalent to
        [name](https://schema.org/name)
    -   Mandatory

-   `description` : Description about the bike hire docking station.

    -   Attribute type: Property. [Text](http://schema.org/Number)
    -   Normative References:
        [https://schema.org/description](https://schema.org/description)
    -   Optional

-   `image` : A URL containing a photo of this docking station.

    -   Attribute type: Property. [image (URL)](http://schema.org/Number)
    -   Normative References:
        [https://schema.org/image](https://schema.org/image)
    -   Optional

-   `totalSlotNumber` : The total number of slots offered by this bike docking
    station.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: Any positive integer number or 0.
    -   Optional

-   `freeSlotNumber` : The number of slots available for returning and parking
    bikes. It must lower or equal than `totalSlotNumber`.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: A positive integer number, including 0. It must lower or
        equal than `totalSlotNumber`.
    -   Metadata:
        -   `timestamp` : Timestamp of the last attribute update.
            -   Type: [DateTime](https://schema.org/DateTime)
    -   Optional

-   `outOfServiceSlotNumber` : The number of slots that are out of order and
    cannot be used to hire or park a bike. It must lower or equal than
    `totalSlotNumber`.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: A positive integer number, including 0.
    -   Metadata:
        -   `timestamp` : Timestamp of the last attribute update
            -   Type: [DateTime](https://schema.org/DateTime)
        -   Optional

-   `availableBikeNumber` : The number of bikes available in the bike hire
    docking station to be hired by users.

    -   Attribute type: Property. [Number](http://schema.org/Number)
    -   Allowed values: A positive integer number, including 0.
    -   Metadata:
        -   `timestamp` : Timestamp of the last attribute update.
            -   Type: [DateTime](https://schema.org/DateTime)
    -   Optional

-   `openingHours` : Opening hours of the docking station.

    -   Normative references:
        [http://schema.org/openingHours](http://schema.org/openingHours)
    -   Optional

-   `status` : Status of the bike hire docking station.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Metadata:
        -   `timestamp` : Timestamp of the last attribute update.
            -   Type: [DateTime](https://schema.org/DateTime)
    -   Allowed values:
        -   (`working`, `outOfService`, `withIncidence`, `full`, `almostFull`,
            `empty`, `almostEmpty`)
        -   Or any other application+specific.
    -   Optional

-   `areaServed` : Area served by this docking station. Precise semantics can
    depend on the application or target city. For instance, it can be a
    neighbourhood, burough or district.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `owner` : Bike hire docking station's owner.

    -   Attribute type: Property. List of [Text](http://schema.org/Text) or List
        of URIs
    -   Optional

-   `provider` : Bike hire service provider.

    -   Attribute Type: Property. [Provider](http://schema.org/provider)
    -   Normative references:
        [https://schema.org/provider](https://schema.org/provider)
    -   Optional

-   `contactPoint` : Bike hire service contact point.
    -   Normative references:
        [https://schema.org/contactPoint](https://schema.org/contactPoint)
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "Bcn-BikeHireDockingStation-1",
    "type": "BikeHireDockingStation",
    "status": {
        "value": "working"
    },
    "availableBikeNumber": {
        "value": 20,
        "metadata": {
            "timestamp": {
                "type": "DateTime",
                "value": "2018-09-25T12:00:00"
            }
        }
    },
    "freeSlotNumber": {
        "value": 10
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [2.180042, 41.397952]
        }
    },
    "address": {
        "type": "PostalAddress",
        "value": {
            "addressCountry": "ES",
            "addressLocality": "Barcelona",
            "streetAddress": "Gran Via Corts Catalanes,760"
        }
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

Bike hire docking station real time data in Malaga

```json
{
    "id": "malaga-bici-7",
    "type": "BikeHireDockingStation",
    "name": "07-Diputacion",
    "location": {
        "coordinates": [-4.43573, 36.699694],
        "type": "Point"
    },
    "availableBikeNumber": 18,
    "freeSlotNumber": 10,
    "address": {
        "streetAddress": "Paseo Antonio Banderas (Diputación)",
        "addressLocality": "Malaga",
        "addressCountry": "España"
    },
    "description": "Punto de alquiler de bicicletas próximo a Diputación",
    "dateModified": "2017-05-09T09:25:55.00Z"
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",
    "type": "BikeHireDockingStation",
    "status": {
        "type": "Property",
        "value": "working"
    },
    "availableBikeNumber": {
        "type": "Property",
        "value": 20,
        "observedAt": "2018-09-25T12:00:00Z"
    },
    "freeSlotNumber": {
        "type": "Property",
        "value": 10
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [2.180042, 41.397952]
        }
    },
    "address": {
        "type": "Property",
        "value": {
            "addressCountry": "ES",
            "addressLocality": "Barcelona",
            "streetAddress": "Gran Via Corts Catalanes,760",
            "type": "PostalAddress"
        }
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Use it with a real service

T.B.D.

## Open Issues

Municipalities do not have a specific tariff or access requirements per station.
Therefore, this information has not been specified in this model so far.
