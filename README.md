# camtrap-dp

Specifications to standardize camera trap data as a [Data Package](https://frictionlessdata.io/data-package/). A camtrap data package consists of:

file | definition | specs
--- | --- | ---
`datapackage.json` | Metadata regarding the data package and camera trap project. | [camtrap-dp-profile.json](camtrap-dp-profile.json)
`deployments.csv` | Table with camera trap deployments. Includes `deployment_id`, start, end, location and camera setup. | [deployments-table-schema.json](deployments-table-schema.json)
`media.csv` | Table with media files (images/videos) captured by camera traps. Associated with deployments (`deployment_id`) and organized in events (`event_id`). Includes timestamp and file location. | [media-table-schema.json](media-table-schema.json)
`observations.csv` | Table with camera trap observations. Associated with deployments (`deployment_id`) and based on one or more media files (`event_id` and optionally `media_id`), covering an event start/end time interval. Observations can contain species (with multiple observations for groups of certain count, age, sex, behaviour and/or individuals) or not (empty, setup/pickup). | [observations-table-schema.json](observations-table-schema.json)

These specifications build upon existing standards:

- `camtrap-package-profile.json`: an extension of [Tabular Data Package](https://specs.frictionlessdata.io/tabular-data-package/), itself a [Data Package](https://specs.frictionlessdata.io/data-package/).
- `deployments-table-schema.json`, `media-table-schema.json`, `observations-table-schema.json`: [Table Schemas](https://specs.frictionlessdata.io/table-schema/) describing the fields, contraints and requirements for a [Tabular Data Resource](https://specs.frictionlessdata.io/tabular-data-resource/).

## Contribute

You can contribute by watching this repository and participating in the [issue discussions](https://gitlab.com/oscf/camtrap-package-schemas/-/issues).
