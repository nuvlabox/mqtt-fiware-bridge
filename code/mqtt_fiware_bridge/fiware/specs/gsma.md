# FIWARE IoT-BigData Instance

## Table of Contents

-   [Introduction](#introduction)
-   [Public Data sources](#public-data-sources)
-   [Data and IoT Device providers](#data-and-iot-device-providers)
-   [Endpoints](#endpoints)
-   [Harmonized data published](#harmonized-data-published)
-   [Useful links](#useful-links)
-   [Examples](#examples)

### Introduction

This document describes the IoT-BD instance developed under the
[GSMA IoT Big Data Project](https://www.gsma.com/iot/iot-big-data/), part of
GSMA’s Connected Living Programme.

### Public Data sources

Here there is a description of the original public data sources used to perform
data harmonization.

<table border="0">
<thead>
<tr>
<th>Entity Type</th>
<th>Public Data source(s)</th>
<th>URLs</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">AirQualityObserved</td>
<td>Generalidad de Catalu&ntilde;a (only Barcelona&rsquo;s data)</td>
<td>http://mediambient.gencat.cat/ca/05_ambits_dactuacio/atmosfera/qualitat_de_laire/vols-saber-que-respires/visor-de-dades/</td>
</tr>
<tr>
<td>Ayuntamiento de Madridr</td>
<td>http://datos.madrid.es/egob/catalogo/212531-7916318-calidad-aire-tiempo-real.txt</td>
</tr>
<tr>
<td rowspan="2">WeatherObserved WeatherForecast</td>
<td>Agencia Estatal de Meteorolog&iacute;a (AEMET)</td>
<td>http://www.aemet.es</td>
</tr>
<tr>
<td>Instituto portugu&ecirc;s do mar y do atmosfera (IPMA)</td>
<td>https://www.ipma.pt/pt/index.html</td>
</tr>
<tr>
<td>Alert</td>
<td>The Network of European Meteorological Services (EUMETNET)</td>
<td>http://www.meteoalarm.eu/</td>
</tr>
<tr>
<td>PointOfInterest</td>
<td>Ineco</td>
<td>https://www.ineco.com/webineco/</td>
</tr>
<tr>
<td>Vehicle OffStreetParking</td>
<td>Fiware Foundation e.V.</td>
<td>https://fiware.org</td>
</tr>
</tbody>
</table>

The usage of the data offered through this instance is subject to the terms,
conditions and licenses expressed by the original data sources. In the table
below, for each data source you can find a link to them.

<!-- textlint-disable terminology -->

| Data source                                                | Terms and Conditions                                                                                                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Generalidad de Cataluña                                    | [http://web.gencat.cat/ca/menu-ajuda/ajuda/avis_legal/](http://web.gencat.cat/ca/menu-ajuda/ajuda/avis_legal) (Spanish)                                            |
| Madrid                                                     | [http://www.mambiente.munimadrid.es/opencms/opencms/calaire/avisoLegal.html](http://www.mambiente.munimadrid.es/opencms/opencms/calaire/avisoLegal.html) (Spanish) |
| AEMET Agencia Estatal de Meteorología                      | [http://www.aemet.es/en/nota_legal](http://www.aemet.es/en/nota_legal) (English)                                                                                   |
| IPMA Instituto português do mar y do atmosfera             | [https://www.ipma.pt/en/siteinfo/index.html?page=index.xml](https://www.ipma.pt/en/siteinfo/index.html?page=index.xml) (English)                                   |
| The Network of European Meteorological Services (EUMETNET) | [http://www.meteoalarm.eu/terms.php?lang=en_UK](http://www.meteoalarm.eu/terms.php?lang=en_UK) (English)                                                           |
| Ineco                                                      |                                                                                                                                                                    |
| FIWARE Foundation e.V.                                     |                                                                                                                                                                    |

<!-- textlint-enable terminology -->

### Data and IoT Device providers

Below there is a list of data / IoT Device providers who kindly are publishing a
sample of their data to this instance. Such data must not be used for commercial
purposes without the consent of their owners.

| Data Provider  | Data offered                                                          |
| -------------- | --------------------------------------------------------------------- |
| EDP Ingeniería | Air quality data from Málaga (Spain). Sensors mounted on public buses |
| Urban Clouds   | Air quality data from Málaga (Spain). Sensors mounted on bicycles     |
| Kunak          | Air quality data from Pamplona (Spain)                                |
| Turespaña      | A sample of points of interest in Spain                               |

### Endpoints

| Endpoint                          | URL                              |
| --------------------------------- | -------------------------------- |
| Harmonized data endpoint (NGSIv2) | `https://streams.lab.fiware.org` |

### Useful links

<!-- textlint-disable terminology -->

| Information                    | URL                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Harmonized data models by GSMA | [https://github.com/GSMADeveloper/NGSI-LD-Entities](https://github.com/GSMADeveloper/NGSI-LD-Entities) |
| Data model by FIWARE           | [https://www.fiware.org/developers/data-models/](https://www.fiware.org/developers/data-models/)       |

<!-- textlint-enable terminology -->

### Harmonized data published

Below there is a description of the harmonized data currently published

| Entity Type        | FIWARE Service | Comment                                      |
| ------------------ | -------------- | -------------------------------------------- |
| AirQualityObserved | environment    | Air quality observations from Madrid         |
| WeatherObserved    | weather        | Weather observations from Spain and Portugal |
| WeatherForecast    | weather        | Weather forecasts from Spain and Portugal    |
| Alert              | weather        | Weather alerts from Spain                    |
| PointOfInterest    | poi            | Points of interest in Spain and Portugal     |

### Examples

Some Postman recipes prepared, you can read documents
[here](https://documenter.getpostman.com/view/3940441/RznEMKdr). Be aware,
Postman recipes use environment variables, don't forget to change it to "FIWARE
Data Streams"
