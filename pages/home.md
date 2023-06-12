---
title: Camtrap DP
background: /assets/home.jpg
permalink: /
description: Data exchange format for camera trap data
---

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data.

{:.alert .alert-warning}
Camtrap DP is [under development](https://github.com/tdwg/camtrap-dp/milestone/1) and not yet recommended for production use.

## Usage

A Camtrap DP is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{:.d-inline-block style="width:150px;"} | [Metadata](metadata/) regarding the data package and camera trap project.
`deployments.csv` | Table with camera trap [deployments](data/#deployments).
`media.csv` | Table with [media](data/#media) files captured by the camera traps.
`observations.csv` | Table with [observations](data/#observations) derived from the media files.

## Example

[Example dataset](example/) following Camtrap DP specifications.

## Validation

To allow validation, the `datapackage.json` of your dataset should reference the used version of Camtrap DP, both in `profile` and the resources' `schema`:

```json
{
   "name": "...",
   "profile": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/camtrap-dp-profile.json",
   "resources": [
      {
         "name": "deployments",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/deployments-table-schema.json"
      },
      {
         "name": "media",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/media-table-schema.json"
      },
      {
         "name": "observations",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/observations-table-schema.json"
      }
   ]
}
```

You can validate your dataset against the specifications of Camtrap DP (and Frictionless Data Package) with:

```shell
pip install frictionless
frictionless validate path/to/your/datapackage.json
```

## Implementations

- [camtraptor](https://inbo.github.io/camtraptor): R package to read, explore and visualize Camtrap DP.
- [Agouti](https://agouti.eu): Data management platform, uses Camtrap DP as export format.
- [TRAPPER](https://os-conservation.org/projects/trapper): Data management platform, uses Camtrap DP as export format.

See also the recorded [November 2022 webinar](https://www.gbif.org/event/f68927-b5c1-4ac8-a4ac-7d47645/exploring-camera-trap-data) for an introduction to Camtrap DP and its intended adoption as a publication format by the Global Biodiversity Information Facility (GBIF).

## Contribute

Questions? Suggestions? Contribute to the development of Camtrap DP by watching the [repository](https://github.com/tdwg/camtrap-dp) and participating in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

> Camtrap DP Development Team (2022) Camera Trap Data Package (Camtrap DP). <https://tdwg.github.io/camtrap-dp>

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG). It was originally developed by the [Open Science Conservation Fund](https://os-conservation.org/), the [Mammal Research Institute Polish Academy of Sciences (MRI PAS)](https://ibs.bialowieza.pl/en/) and the [Research Institute for Nature and Forest (INBO)](https://inbo.be/en).

Camtrap DP is endorsed by the camera trap data management systems [Agouti](https://www.agouti.eu/), [eMammal](https://emammal.si.edu/), [TRAPPER](https://doi.org/10.1111/2041-210X.12571), [Wildlife Insights](https://www.wildlifeinsights.org/) and already available as an export format in some of these.
