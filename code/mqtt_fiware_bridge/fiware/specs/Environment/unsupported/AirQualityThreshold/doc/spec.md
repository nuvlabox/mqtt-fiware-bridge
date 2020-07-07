# Air quality threshold

The formal documentation of this model is currently under development. In the
meantime please check the examples of use

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### key-value pairs Example

```json
{
    "id": "EU-AirQualityThreshold-O3-Background-VeryLow",
    "type": "AirQualityThreshold",
    "category": ["Background"],
    "frequency": "Hourly",
    "indexClass": "VeryLow",
    "maxConcentration": 60,
    "minConcentration": "0",
    "pollutant": "O3",
    "source": "http://www.airqualitynow.eu/"
}
```

### LD Example

Sample uses the NGSI-LD representation

```json

```
