---
background: /assets/home.jpg
permalink: /
description: Data exchange format for camera trap data
---

# Camtrap DP

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data.

## Usage

A Camtrap DP is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{: .d-inline-block style="width:150px;"} | [Metadata](https://tdwg.github.io/camtrap-dp/metadata/) regarding the data package and camera trap project.
`deployments.csv` | Table with camera trap [deployments](https://tdwg.github.io/camtrap-dp/data/#deployments).
`media.csv` | Table with [media](https://tdwg.github.io/camtrap-dp/data/#media) files captured by the camera traps.
`observations.csv` | Table with [observations](https://tdwg.github.io/camtrap-dp/data/#observations) based on the media files.

Camtrap DP is endorsed the camera trap data management systems [Agouti](https://www.agouti.eu/), [eMammal](https://emammal.si.edu/), [TRAPPER](https://doi.org/10.1111/2041-210X.12571), [Wildlife Insights](https://www.wildlifeinsights.org/) and already available as an export format in some of these.

## Example

[Example dataset](https://github.com/tdwg/camtrap-dp/tree/main/example) following Camtrap DP specifications.

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

## Contribute

Questions? Suggestions? Contribute to the development of Camtrap DP by watching the [repository](https://github.com/tdwg/camtrap-dp) and participating in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

> Camtrap DP Development Team (2021) Camera Trap Data Package <https://github.com/tdwg/camtrap-dp>

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG). It was originally developed by the [Open Science Conservation Fund](https://os-conservation.org/) and the [Research Institute for Nature and Forest (INBO)](https://inbo.be/en).
