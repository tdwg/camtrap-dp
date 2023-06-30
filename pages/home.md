---
title: Camtrap DP
background: /assets/home.jpg
permalink: /
description: Data exchange format for camera trap data
---

{:.alert .alert-warning}
Camtrap DP is [under development](https://github.com/tdwg/camtrap-dp/milestone/1) and not yet recommended for production use.

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data. A Camtrap DP is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{:.d-inline-block style="width:150px;"} | [Metadata](metadata/) about the data package and camera trap project.
`deployments.csv` | Table with camera trap placements ([deployments](data/#deployments)).
`media.csv` | Table with [media](data/#media) files recorded during deployments.
`observations.csv` | Table with [observations](data/#observations) derived from the media files.

Want to learn more about Camtrap DP? Read our [preprint](https://doi.org/10.32942/X2BC8J) or watch the [November 2022 webinar](https://www.gbif.org/event/f68927-b5c1-4ac8-a4ac-7d47645/exploring-camera-trap-data).

## Example

See the [example dataset](example/).

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
- [Integrated Publishing Toolkit (IPT)](https://www.gbif.org/ipt) (upcoming release): Online software tool to publish biodiversity datasets to the Global Biodiversity Information Facility (GBIF).

## Contribute

Questions? Suggestions? Contribute to the development of Camtrap DP by watching the [repository](https://github.com/tdwg/camtrap-dp) and participating in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

To cite Camtrap DP in general, use the preprint ([bibtex](citation.bib)):

> Bubnicki JW, Norton B, Baskauf SJ, Bruce T, Cagnacci F, Casaer J, Churski M, Cromsigt JPGM, Dal Farra S, Fiderer C, Forrester TD, Hendry H, Heurich M, Hofmeester TR, Jansen PA, Kays R, Kuijper DPJ, Liefting Y, Linnell JDC, Luskin MS, Mann C, Milotic T, Newman P, Niedballa J, Oldoni D, Ossi F, Robertson T, Rovero F, Rowcliffe M, Seidenari L, Stachowicz I, Stowell D, Tobler MW, Wieczorek J, Zimmermann F, Desmet P (2023) Camtrap DP: An open standard for the FAIR exchange and archiving of camera trap data. EcoEvoRxiv. preprint <https://doi.org/10.32942/X2BC8J>

To cite a specific version of Camtrap DP, use:

> Camtrap DP Development Team (\<year\>) Camera Trap Data Package (Camtrap DP). Version \<version\>. <https://tdwg.github.io/camtrap-dp> accessed on \<yyyy-mm-dd\>.

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG).
