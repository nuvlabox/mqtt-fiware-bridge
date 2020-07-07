# GtfsCalendarRule

## Description

See
[https://developers.google.com/transit/gtfs/reference/#calendartxt](https://developers.google.com/transit/gtfs/reference/#calendartxt)

## Data Model

The data model is defined as shown below:

-   `id`: Entity ID

    -   It shall be `urn:ngsi-ld:GtfsCalendarRule:<calendar_rule_identifier>`.

-   `type`: Entity Type

    -   It shall be equal to `GtfsCalendarRule`

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
    -   Read-Only. Automatically generated.

-   `dateModified` : Last update timestamp of this Entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `hasService` : Service to which this rule applies to. Derived from
    `service_id`.

    -   Attribute type: Relationship. It shall point to an entity of Type
        [GtfsService](../../GtfsService/doc/spec.md)
    -   Mandatory

-   `name` : Name of this rule

    -   Attribute type: Property. [Text](https://schema.org/Text).
    -   Normative References: `https://uri.etsi.org/ngsi-ld/name` equivalent to
        [name](https://schema.org/name)
    -   Optional

-   `description`: Description of this rule

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References: `https://uri.etsi.org/ngsi-ld/description`
        equivalent to [description](https://schema.org/description)
    -   Optional

-   `monday`: Same as GTFS `monday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `tuesday`: Same as GTFS `tuesday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `wednesday`: Same as GTFS `wednesday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `thursday`: Same as GTFS `thursday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `friday`: Same as GTFS `friday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `saturday`: Same as GTFS `saturday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `sunday`: Same as GTFS `sunday`

    -   Attribute type: Property.
        [https://schema.org/Boolean](https://schema.org/Boolean)
    -   Mandatory

-   `startDate`: Start date of this rule in `YYYY-MM-DD` format. It can be
    obtained from the field `start_date` of
    [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt).

    -   Attribute type: Property.
        [https://schema.org/Date](https://schema.org/Date).
    -   Mandatory

-   `endDate`: End date of this rule in `YYYY-MM-DD` format. It can be obtained
    from the field `end_date` of
    [calendar.txt](https://developers.google.com/transit/gtfs/reference/#calendartxt).
    -   Attribute type: Property.
        [https://schema.org/Date](https://schema.org/Date).
    -   Mandatory

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",
    "type": "GtfsCalendarRule",
    "startDate": {
        "type": "Date",
        "value": "2018-01-01"
    },
    "endDate": {
        "type": "Date",
        "value": "2019-01-01"
    },
    "name": {
        "value": "Rule Hospital Service 1"
    },
    "monday": {
        "value": true
    },
    "tuesday": {
        "value": true
    },
    "friday": {
        "value": true
    },
    "wednesday": {
        "value": true
    },
    "thursday": {
        "value": true
    },
    "sunday": {
        "value": false
    },
    "hasService": {
        "type": "Relationship",
        "value": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"
    },
    "saturday": {
        "value": false
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "urn:ngsi-ld:GtfsCalendarRule:Madrid:Rule1267",
    "type": "GtfsCalendarRule",
    "name": "Rule Hospital Service 1",
    "hasService": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1",
    "monday": true,
    "tuesday": true,
    "wednesday": true,
    "thursday": true,
    "friday": true,
    "saturday": false,
    "sunday": false,
    "startDate": "2018-01-01",
    "endDate": "2019-01-01"
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:CalendarRule:Madrid:Rule1267",
    "type": "GtfsCalendarRule",
    "startDate": {
        "type": "Property",
        "value": {
            "@type": "Date",
            "@value": "2018-01-01"
        }
    },
    "endDate": {
        "type": "Property",
        "value": {
            "@type": "Date",
            "@value": "2019-01-01"
        }
    },
    "name": {
        "type": "Property",
        "value": "Rule Hospital Service 1"
    },
    "monday": {
        "type": "Property",
        "value": true
    },
    "tuesday": {
        "type": "Property",
        "value": true
    },
    "friday": {
        "type": "Property",
        "value": true
    },
    "wednesday": {
        "type": "Property",
        "value": true
    },
    "thursday": {
        "type": "Property",
        "value": true
    },
    "sunday": {
        "type": "Property",
        "value": false
    },
    "hasService": {
        "type": "Relationship",
        "object": "urn:ngsi-ld:GtfsService:Madrid:Hospital_1"
    },
    "saturday": {
        "type": "Property",
        "value": false
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Summary of mappings to GTFS

| GTFS Field   | NGSI Attribute | LinkedGTFS           | Comment |
| :----------- | :------------- | :------------------- | :------ |
|              | `name`         | `schema:name`        |         |
|              | `description`  | `schema:description` |         |
| `monday`     | `monday`       | `gtfs:monday`        |         |
| `tuesday`    | `tuesday`      | `gtfs:tuesday`       |         |
| `wednesday`  | `wednesday`    | `gtfs:wednesday`     |         |
| `thursday`   | `thursday`     | `gtfs:thursday`      |         |
| `friday`     | `friday`       | `gtfs:friday`        |         |
| `saturday`   | `saturday`     | `gtfs:saturday`      |         |
| `sunday`     | `sunday`       | `gtfs:sunday`        |         |
| `start_date` | `startDate`    | `schema:startDate`   |         |
| `end_date`   | `endDate`      | `schema:endDate`     |         |

### Relationships

| GTFS Field | NGSI Attribute | LinkedGTFS     | Comment                                             |
| :--------- | :------------- | :------------- | :-------------------------------------------------- |
|            | `hasService`   | `gtfs:service` | Shall point to another Entity of Type `GtfsService` |

## Open issues
