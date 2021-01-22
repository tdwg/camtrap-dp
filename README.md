# Camera Trap Data Package (Camtrap DP)

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange standard for camera trap data. A Camtrap DP is a [Frictionless Data Package](https://frictionlessdata.io/data-package/) that consists of:

file | definition | specification
--- | --- | ---
`datapackage.json` | Metadata regarding the data package and camera trap project. | [camtrap-dp-profile.json](camtrap-dp-profile.json)
`deployments.csv` | Table with camera trap deployments. Includes `deployment_id`, start, end, location and camera setup information. | [deployments-table-schema.json](deployments-table-schema.json)
`multimedia.csv` | Table with multimedia files (images/videos) captured by the camera traps. Associated with deployments (`deployment_id`) and organized in sequences (`sequence_id`). Includes timestamp and file path. | [multimedia-table-schema.json](multimedia-table-schema.json)
`observations.csv` | Table with observations based on the multimedia files. Associated with deployments (`deployment_id`), sequences (`sequence_id`) and optionally individual multimedia files (`multimedia_id`). Observations can mark non-animal events (camera setup, human, empty) or one or more animal observations (`observation_type` = `animal`) of a certain species, count, age, sex, behaviour and/or individual. | [observations-table-schema.json](observations-table-schema.json)

The specifications build upon existing standards:

- `camtrap-package-profile.json`: an extension of [Tabular Data Package](https://specs.frictionlessdata.io/tabular-data-package/), itself a [Data Package](https://specs.frictionlessdata.io/data-package/).
- `deployments-table-schema.json`, `multimedia-table-schema.json`, `observations-table-schema.json`: [Table Schemas](https://specs.frictionlessdata.io/table-schema/) describing the fields, contraints and requirements for a [Tabular Data Resource](https://specs.frictionlessdata.io/tabular-data-resource/).

## Contribute

You can contribute by watching this repository and participating in the [issue discussions](https://gitlab.com/oscf/camtrap-dp/-/issues).
