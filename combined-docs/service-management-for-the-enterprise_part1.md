# service-management-for-the-enterprise



---

## Folder: service-management-for-the-enterprise



### File: service-management-for-the-enterprise\FacilitiesLandingPage.md

```text
---
title: Facilities Service Management
description: With the ServiceNow Facilities Service Management application, you can request changes to the operation and maintenance of your facilities, track these requests, and make the necessary changes.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service Management]
---

# Facilities Service Management

With the ServiceNow® Facilities Service Management application, you can request changes to the operation and maintenance of your facilities, track these requests, and make the necessary changes.

## Deprecation announcement

Facilities Service Management is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported until deprecation. Workplace Service Delivery provides the latest experience for this functionality. For details, see the [KB0867184 Deprecation Process](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867184) article in the Now Support knowledge base.

<table id="simpletable_g33_wwg_vt" class="simpletableBody"><tbody><tr><td>

**Explore**

 -   [Facilities Service Management overview](../concept/c_FacilitiesServiceManagement.md)
-   [Domain separation and Facilities Service Management](../concept/domain-separation-facilities-service-mgt.md)

</td><td>

**Set up**

 -   [Activate Facilities Visualization Workbench](../../facilities-interactive-facility-maps/task/t_ActivateFacVisWorkbench.md)

</td><td>

**Administer**

 -   [Facilities service management process](../concept/c_FacilitiesSMProcess.md)
-   [Configure Facilities Service Management](../task/t_ConfigureFacilities.md)
-   [Configure Enterprise Move](../../facilities-move-management/task/t_ConfigureEnterpriseMove.md)
-   [Properties installed with Facilities Service Management](r_PropInstallWFacServMgmnt.md)
-   [Properties installed with Facilities Move Management](../../facilities-move-management/reference/r_PropsInstallWFacMoveMgmt.md)

</td></tr><tr><td>

**Use**

 -   [Facilities requests](../concept/c_FacilitiesRequests.md)
-   [Facilities request tasks](../../planning-and-policy/concept/c_FacRequestTasks.md)
-   [Space management](r_SpaceManagement.md)
-   [Facilities move management](../../facilities-move-management/concept/c_FacMoveMgmt.md)

</td><td>

**Develop**

 -   [Developer training](https://developer.servicenow.com/app.do#!/training/landing)
-   [Developer documentation](https://developer.servicenow.com/app.do#!/documentation)
-   [Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)

</td><td>

**Troubleshoot and get help**

 -   [Ask or answer questions in the community](https://community.servicenow.com/community)
-   [Search the Known Error Portal for known error articles](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597477)
-   [Contact Customer Service and Support](https://support.servicenow.com/now?draw=case)

</td></tr><tr><td>

 

</td><td>

 

</td><td>

 

</td></tr></tbody>
</table>
```


### File: service-management-for-the-enterprise\SpaceMgmntProperties.md

```text
---
title: Space Management properties
description: Space Management Properties are available to configure floor plan, parsing, and space management defaults settings. You can control default settings like the color for selected space, compass on a floor plan, and logos and titles to appear.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Space Management properties

Space Management Properties are available to configure floor plan, parsing, and space management defaults settings. You can control default settings like the color for selected space, compass on a floor plan, and logos and titles to appear.

Space Management organizes properties into these sections:

-   Floor Plan
-   Parsing
-   Space Management

Navigate to **Space Management** &gt; **Map Configuration** &gt; **Properties**.

## Floor Plan

<table id="table_b4f_jcp_yq"><thead><tr><th>

Property

</th><th>

Description

</th></tr></thead><tbody><tr><td>

The logo to use for the header of the interactive floor plan \[facilities.management.fvw.workbench.logo\]

</td><td>

Click to select a logo that appears in the top, left corner of an interactive floor plan.

</td></tr><tr><td>

The title to show on the workbench \[facilities.management.fvw.workbench.title\]

</td><td>

The title to show on the workbench.-   Type: string
-   Default value: Workbench

</td></tr><tr><td>

Use user's location as the default campus when available \[facilities.management.fvw.default.campus\]

</td><td>

The location of the user is used as the default campus when available.-   Yes: Use the location of the user.
-   No: Do not use the location of the user.

</td></tr><tr><td>

Allow copying a URL link when available on the workbench \[facilities.management.fvw.allow.copy.url\]

</td><td>

Allow copying a URL link when available on the workbench.-   Yes: Allow copying of a URL.
-   No: Do not allow copying of a URL.

</td></tr><tr><td>

Default to showing the compass on the floor plan \[facilities.management.fvw.show.compass\]

</td><td>

Determines if a compass appears in the top, right corner of a floor plan to provide directional orientation.

</td></tr><tr><td>

The maximum length allowed for a label before using ellipses \[facilities.management.fvw.max.label.length\]

</td><td>

The maximum number of characters allowed for a label before using ellipses.-   Type: integer
-   Default value: 30

</td></tr><tr><td>

The color to use for highlighting the selected space on the floor plan map \[facilities.management.fvw.highlight.color\]

</td><td>

The color that can be used for highlighting a specific space on the floor plan map.-   Type: string
-   Default value: \#F5F500

</td></tr><tr><td>

The colors for applying filters to the workbench \[facilities.management.fvw.filter.colors\]

</td><td>

The colors available for applying filters to the workbench.-   Type: string
-   Default value: \#278ECF; \#4BD762; \#FFCA1F; \#FF9416; \#D42AE8; \#535AD7; \#FF402C; \#83BFFF; \#6EDB8F; \#FFE366; \#FFC266; \#D284BD; \#8784DB; \#FF7B65; \#CAEEFC; \#9ADBAD; \#FFF1B2; \#FFE0B2; \#FFBEB2; \#B1AFDB

</td></tr><tr><td>

The colors for availability filtering on the workbench \[facilities.management.fvw.availability.colors\]

</td><td>

The colors for availability filtering on the workbench.-   Type: string
-   Default value: \#71e279; \#fcc742; \#278efc; \#f95050; \#00A0A6; \#fc8a3d; \#00FFFF; \#b1afdb

</td></tr><tr><td>

Maximum number of search results to return per level on spaces tab in workbench \[facilities.management.fvw.max.results.per.level\]

</td><td>

Maximum number of search results to return per level on spaces tab in workbench.-   Type: integer
-   Default value: 20

</td></tr><tr><td>

Maximum number of search results to return per campuses on spaces tab in workbench \[facilities.management.fvw.max.results.per.campus\]

</td><td>

Maximum number of search results to return for campuses on spaces tab in workbench.-   Type: integer
-   Default value: 20

</td></tr><tr><td>

Maximum number of search results to return for other campus on spaces tab in workbench \[facilities.management.fvw.max.results.per.other.campus\]

</td><td>

Maximum number of search results to return for other campuses on spaces tab in workbench. -   Type: integer
-   Default value: 20

</td></tr><tr><td>

Maximum number of search results to return when searching for tasks in workbench \[facilities.management.fvw.max.requests.per.search\]

</td><td>

Maximum number of search results to return when searching for facilities/move requests tabs in workbench. -   Type: integer
-   Default value: 200

</td></tr><tr><td>

Maximum number of spaces per zone to render for the zone edit tab \[facilities.management.fvw.max.spaces.per.zone\]

</td><td>

Maximum number of spaces per zone to render for the zone edit tab. -   Type: integer
-   Default value: 50

</td></tr><tr><td>

Maximum number of tasks to return per level on workbench \[facilities.management.fvw.max.requests.per.level\]

</td><td>

Maximum number of search results to return per level on spaces tab in workbench.-   Type: integer
-   Default value: 20

</td></tr></tbody>
</table>## Parsing

<table id="table_ubt_fdx_lcb"><thead><tr><th>

Property

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Specifies whether we should preserve the field values of records when parsing geoJSON files if the record already exists \[facilities.management.fvw.geojson.parsing.preserve.fields\]

</td><td>

Determines how to save the field values of existing records when parsing geoJSON files or to delete them.-   Yes: Do not change when parsing new map.
    -   The building name.
    -   The level name, level abbreviation, and the main level flag.
    -   The space name and internal name.
-   No: Use values from latest geoJSON file.

</td></tr><tr><td>

Specifies whether we should preserve the field values of records when parsing geoJSON files if the record already exists \[facilities.management.fvw.geojson.parsing.preserve.fields\]

</td><td>

If the space exists, specifies whether the sys\_class\_name of a space is preserved when parsing geoJSON files.-   Yes: Save
-   No: Update

**Note:** The sys\_class\_name \(fm\_bathroom, fm\_cubicle, and so on\) are only updated if both parsing properties are set to **No**.


</td></tr><tr><td>

Specifies whether we should preserve the sys\_class\_name of a space when parsing geoJSON files if the space already exists \[facilities.management.fvw.geojson.parsing.preserve.sys\_class\_name\]

</td><td>

Specifies how to handle area parsing. -   Preserve Existing Area: Saves the area space when the current value is greater than 0.0001 in the **Area** field in the **Space** form.
-   Overwrite Area: Always updates the area of a space from an area file.
-   Ignore Area Files: Does not parse any existing area files within the map set.

**Note:** Regardless of the flags, area roll ups are calculated after parsing.


</td></tr></tbody>
</table>## Space Management

<table id="table_mlq_pz1_qy"><thead><tr><th>

Properties

</th><th>

Description

</th></tr></thead><tbody><tr><td>

The system base area unit for facilities space tables. Set to true to use meters squared, or false to use feet squared \[facilities.management.fvw.area.unit\]

</td><td>

The system base area unit for facilities space tables. Set to true to use meters squared, or false to use feet squared.-   Type: true \| false
-   Default value: false

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Visualization Workbench](../../facilities-interactive-facility-maps/reference/r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\c_AgAtAssgmtMlt.md

```text
---
title: Agent auto assignment using multiple selection criteria
description: At its simplest, auto assignment involves identifying a set of selection criteria and automatically assigning the task to the agent who most closely meets the criteria. You can, however, select multiple sets of criteria, including both rating-based and time-based criteria.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using multiple selection criteria

At its simplest, auto assignment involves identifying a set of selection criteria and automatically assigning the task to the agent who most closely meets the criteria. You can, however, select multiple sets of criteria, including both rating-based and time-based criteria.

When a task is qualified or marked as **Ready for Work**, the following evaluations are performed:

1.  The ratings of an agent are calculated. If the **Auto-selection of agents will consider agent or task schedules** configuration option is disabled for the application, the ratings of an agent are used exclusively for auto-assigning an agent.

    For more information on how the ratings are calculated, see:

    -   [Agent auto assignment using location](c_AgentAutoAssignmentUsingLocation.md)
    -   [Agent auto assignment using skills](c_AgentAutoAssignmentUsingSkills.md)
    -   [Agent auto assignment using time zones](c_AgAtAssgnZones.md)
2.  If the **Auto-selection of agents will consider agent or task schedules** configuration option is enabled, the schedules of the agents whose ratings are acceptable for auto-assignment are compared to the schedule for the task, and the agent with the best match is auto-assigned. For more information on time-based methods for auto-assigning agents, see:
    -   [Agent auto assignment using schedules](c_AgAtAssgnSchd.md)
    -   [Agent auto assignment using priority assignment](c_AgentAutoAssignUsePrioAssign.md)

Auto assignment is based on the following calculation:

`(Criteria_1 rating x Criteria_1 weight) + (Criteria_2 rating x Criteria_2 weight) + (Criteria_3 rating x Criteria_3 weight) / Number of criteria types used`

Where:

-   Number of criteria types used = 1, 2, or 3 depending on the location, skill, and time zone settings used.

This example calculates agent auto-assignment based on location and skills. The example is based on the following assumptions.

-   The **Auto-selection of agents will consider location of agents** configuration option is enabled for the application.
-   The **Auto-selection of agents requires them to have some of the required skills for the task** configuration option is enabled for the application.
-   The **Skills Weight** property is set to 10 for the application.
-   The **Location Weight** property is set to 5 for the application.
-   Agents A and B are available to perform a task, and the task requires four specific skills.
-   The location of Agent A is 5 miles from the site of the task. Agent A possesses three of the four required skills.
-   The location of Agent B is one-quarter mile from the site. Agent B possesses two of the required skills.

Auto assignment for the agents uses this calculation:

`[(Location rating x Location weight) + (Skills rating x Skills weight)]/ 2`

-   The auto assignment calculation for Agent A is: `[(0.7 x 0.5) + (0.75 x 1)]/ 2 = 0.55`
-   The auto assignment calculation for Agent B is: `[(0.9 x 0.5) + (0.5 x 1)]/ 2 = 0.475`

In this example, Agent A is auto assigned the task.

**Parent Topic:**[Agent auto assignment](../../service-management-core/concept/c_AgentAutoAssignment.md)


```


### File: service-management-for-the-enterprise\c_AgAtAssgnSchd.md

```text
---
title: Agent auto assignment using schedules
description: Agents can be auto assigned based on the agent or the task schedule.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Agent auto assignment using time-based criteria, Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using schedules

Agents can be auto assigned based on the agent or the task schedule.

Auto assignment by schedule can be performed only in a [task-driven processing](c_TaskVsRequestDrivenProcessing.md) environment, and the **Auto-selection of agents will consider agent or task schedules** configuration option must be enabled for the application. If this option is turned off, only the [agent ratings](c_AgentAutoAssignUseRatBaseCrit.md) are used for auto-assignment.

When a task is qualified or marked as **Ready for Work**, agents ratings are evaluated, and the schedules of qualified agents are compared against the schedule of the task to determine the agent with the best matching schedule.

**Note:** If the task includes specific time entries in the **Window start** and **Window end** fields, and no schedule of an agent falls within that task window, no agents are assigned. Also if the customer wants a task to be performed at or near a specific time, the **Window start** time should be set as close to that time as possible. For example, the **Window start** and **Window end** fields are set to 1:00 pm and 8:00 pm respectively. The customer prefers the job to be started at 4:00 pm. It is possible that an agent is dispatched at 13:00. So, setting the **Window start** closer to 4:00 can help ensure that the work is performed when the customer prefers it to be done.

If the application is configured to use other selection criteria, such as skills or time zone, the ratings of all selection criteria are averaged, and the agent with the highest overall rating is auto-selected for the task. See [Agent auto assignment using multiple selection criteria](c_AgAtAssgmtMlt.md) for details.

**Parent Topic:**[Agent auto assignment using time-based criteria](c_AgAtAssgnTime.md)


```


### File: service-management-for-the-enterprise\c_AgAtAssgnTime.md

```text
---
title: Agent auto assignment using time-based criteria
description: Time-based methods, such as schedules and priority assignment, help you auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using time-based criteria

Time-based methods, such as schedules and priority assignment, help you auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.

Any combination of time-based methods can be enabled in the application configuration screen.

When a task is created, the schedule of the agent and the task to be performed are combined with rating-based criteria to auto-assign an agent.

-   **[Agent auto assignment using schedules](c_AgAtAssgnSchd.md)**  
Agents can be auto assigned based on the agent or the task schedule.
-   **[Agent auto assignment using priority assignment](c_AgentAutoAssignUsePrioAssign.md)**  
The priority assignment feature enables you to configure auto assignment so that agents can be assigned to perform tasks or provide services on a continual, 24x7x365 basis. Priority assignment is triggered when the priority of a task matches the priority set in the application configuration page.

**Parent Topic:**[Agent auto assignment](../../service-management-core/concept/c_AgentAutoAssignment.md)


```


### File: service-management-for-the-enterprise\c_AgAtAssgnZones.md

```text
---
title: Agent auto assignment using time zones
description: Agents can be auto assigned based on the time zone defined in their user records and the time zone of the tasks.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Agent auto assignment using rating-based criteria, Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using time zones

Agents can be auto assigned based on the time zone defined in their user records and the time zone of the tasks.

Auto assignment by time zone can be performed in either a [task- or request-driven processing](c_TaskVsRequestDrivenProcessing.md) environment when the **Auto-selection of agents will consider time zone for the task** configuration option must be enabled for the application.

When a task is qualified or marked as **Ready for Work**, agents in the time zone closest to the task time zone are considered for the task. If the application is configured so that only time zone is considered, an agent in the same time zone is auto-assigned the task.

**Note:** It is important that the time zones for the agent and the task are set correctly.

When a task is created, agents are rated based on the time zones of both task and agent using the following formula:

`1 - [abs(Task_tz – Agent_tz) ÷ 12]`

Where:

-   `abs` is the mathematical function to compute the absolute value.
-   `Task_tz` is the offset between the time zone of the task and GMT.
-   `Agent_tz` is the offset between the time zone of the agent and GMT.

For example, a task is created in New York City \(GMT-4\), and two agents are available to perform the task, one in Los Angeles \(GMT-7\) and one in Paris, France \(GMT+1\).

The rating of the agent in Los Angeles is calculated as:

`1 - abs((-4) - (-7)) ÷ 12 or 0.75`

The rating of the agent in Paris is calculated as:

`1 - abs((-4) - (+1)) ÷ 12 or 0.58`

So if the auto assignment of the task is based on the time zone alone, it is assigned to the agent from Los Angeles.

If the application is configured to use other selection criteria, such as skills or location, the ratings of all selection criteria are averaged, and the agent with the highest overall rating is auto-selected for the task. See [Agent auto assignment using multiple selection criteria](c_AgAtAssgmtMlt.md) for details.

**Parent Topic:**[Agent auto assignment using rating-based criteria](c_AgentAutoAssignUseRatBaseCrit.md)


```


### File: service-management-for-the-enterprise\c_AgentAssignment.md

```text
---
title: Agent assignment methods
description: Depending on your settings in the SM application's configuration screen, you can assign agents manually or using auto-assignment.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Agent assignment methods

Depending on your settings in the SM application's configuration screen, you can assign agents manually or using auto-assignment.

-   **[Manually assign agents to active requests](../../planning-and-policy/task/t_ManAssignAgtToActSMReq.md)**  
Use this procedure to assign agents to active requests in service management \(SM\) applications.
-   **[Agent auto assignment](c_AgentAutoAssignment.md)**  
When auto assignment is enabled and a task is qualified or marked as **Ready for Work**, an appropriate agent is automatically assigned to the task and it is moved to the **Assigned** state. If the task cannot be auto-assigned, a user with the dispatcher role must adjust the values in the request or task form and then save the record.

**Parent Topic:**[Request Management in a Service Management application](../../planning-and-policy/concept/rm-sm-application.md)


```


### File: service-management-for-the-enterprise\c_AgentAutoAssignUsePrioAssign.md

```text
---
title: Agent auto assignment using priority assignment
description: The priority assignment feature enables you to configure auto assignment so that agents can be assigned to perform tasks or provide services on a continual, 24x7x365 basis. Priority assignment is triggered when the priority of a task matches the priority set in the application configuration page.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent auto assignment using time-based criteria, Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using priority assignment

The priority assignment feature enables you to configure auto assignment so that agents can be assigned to perform tasks or provide services on a continual, 24x7x365 basis. Priority assignment is triggered when the priority of a task matches the priority set in the application configuration page.

Priority assignment can be used with location and skills settings. However, it can also operate independently.

To use priority assignment, you must set the following configuration options for the application.

|Field|Description|
|-----|-----------|
|Process life cycle|Set to **task driven \(subtasks are required\)**.|
|Assignment method for tasks|Set to **auto-assignment**.|
|Auto-selection of agents considers agent or task schedules|Enabled.|
|Enable priority assignment|Enabled.|
|Select priorities for assignment|Select one or more priorities.|

Only tasks of the selected priority or priorities trigger auto-assignment based on priority assignment.

When a task is qualified or marked as **Ready for Work**, and the priority of the task matches a priority selected for the application, the agent that best matches the schedule of the task is auto-assigned. If the location and skills options are enabled, agents are first evaluated on their physical proximity to the location of the task, and then on how their skills match the skills required to perform the task. The agent whose location, availability, and skills best match the requirements of the task is auto-assigned.

When a task has a priority that matches a priority in the priority assignment list, the Location Rating and Timezone Rating are ignored, even if they have been enabled.

If the priority of a task matches a priority selected in the **Select priorities for assignment** option, and no agents in the assignment group are available to be auto-assigned, the task is assigned to the group manager, regardless of whether the manager is available. It is the responsibility of the manager to locate an agent to perform the task.

**Note:** If no agent is located in the same time zone as the task, priority assignment fails.

**Parent Topic:**[Agent auto assignment using time-based criteria](c_AgAtAssgnTime.md)


```


### File: service-management-for-the-enterprise\c_AgentAutoAssignUseRatBaseCrit.md

```text
---
title: Agent auto assignment using rating-based criteria
description: Rating-based methods, such as location, skills, and time zones, help to auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using rating-based criteria

Rating-based methods, such as location, skills, and time zones, help to auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.

Any combination of rating-based methods can be enabled in configuration screen of the application.

When a task is created, a rating for each type of enabled selection criteria is calculated for each available agent. The agent whose average rating is highest is considered for auto-assignment. The settings for the auto-assignment weighting properties, found in **\[SM application\]** &gt; **Administration** &gt; **Properties**, are included in the rating calculations.

These values help you prioritize which auto-assignment selection criteria is more important to your organization. The priority values should be \[1, 10\] and they are factored between 1 and 0. That is, 10 is a factor of 1, 5 is a factor of 0.5, and so on. For an example of how the weighting properties affect agent ratings, see [Agent auto assignment using multiple selection criteria](c_AgAtAssgmtMlt.md).

-   **[Agent auto assignment using location](c_AgentAutoAssignmentUsingLocation.md)**  
Agents can be auto assigned based on the location defined in their user record and the location of the tasks.
-   **[Agent auto assignment using skills](c_AgentAutoAssignmentUsingSkills.md)**  
Agents can be auto assigned based on the skills of an agent, and the skills required to perform the task. Assign skills to an agent user records using **Skills** &gt; **Users**.
-   **[Agent auto assignment using time zones](c_AgAtAssgnZones.md)**  
Agents can be auto assigned based on the time zone defined in their user records and the time zone of the tasks.

**Parent Topic:**[Agent auto assignment](../../service-management-core/concept/c_AgentAutoAssignment.md)


```


### File: service-management-for-the-enterprise\c_AgentAutoAssignment.md

```text
---
title: Agent auto assignment
description: When auto assignment is enabled and a task is qualified or marked as Ready for Work, an appropriate agent is automatically assigned to the task and it is moved to the Assigned state. If the task cannot be auto-assigned, a user with the dispatcher role must adjust the values in the request or task form and then save the record.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment

When auto assignment is enabled and a task is qualified or marked as **Ready for Work**, an appropriate agent is automatically assigned to the task and it is moved to the **Assigned** state. If the task cannot be auto-assigned, a user with the dispatcher role must adjust the values in the request or task form and then save the record.

The Auto-Assignment feature can be enabled for requests or tasks, depending on the configuration settings of Service Management \(SM\) application:

-   If the Requests are assigned via auto-assignment option is enabled, requests are automatically assigned.
-   If the Tasks are assigned via auto-assignment option is enabled, the tasks in a request are automatically assigned.

-   **[Agent auto assignment using rating-based criteria](../../planning-and-policy/concept/c_AgentAutoAssignUseRatBaseCrit.md)**  
Rating-based methods, such as location, skills, and time zones, help to auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.
-   **[Agent auto assignment using time-based criteria](../../planning-and-policy/concept/c_AgAtAssgnTime.md)**  
Time-based methods, such as schedules and priority assignment, help you auto assign agents based on configuration settings and optional properties. The calculated ratings are used to determine the best agent to perform the task.
-   **[Agent auto assignment using multiple selection criteria](../../planning-and-policy/concept/c_AgAtAssgmtMlt.md)**  
At its simplest, auto assignment involves identifying a set of selection criteria and automatically assigning the task to the agent who most closely meets the criteria. You can, however, select multiple sets of criteria, including both rating-based and time-based criteria.

**Parent Topic:**[Agent assignment methods](c_AgentAssignment.md)


```


### File: service-management-for-the-enterprise\c_AgentAutoAssignmentUsingLocation.md

```text
---
title: Agent auto assignment using location
description: Agents can be auto assigned based on the location defined in their user record and the location of the tasks.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent auto assignment using rating-based criteria, Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using location

Agents can be auto assigned based on the location defined in their user record and the location of the tasks.

Auto assignment by location can be performed in a [task- or request-driven processing](c_TaskVsRequestDrivenProcessing.md) environment when the **Auto-selection of agents will consider location of agents** configuration is enabled.

When a task is created, agent locations are compared to the following ranges to determine a location rating for each agent.

|Distance \(mi.\) from agent to task|Rating|
|-----------------------------------|------|
|0–0.1|1|
|0.11–0.5|0.9|
|0.51–5|0.7|
|5.1–10|0.5|
|10.1–20|0.4|
|20.1–30|0.3|
|30.1–40|0.2|
|40.1–100|0.1|
|&gt;100|0|

When a task is qualified or marked as **Ready for Work**, the agent closest to the task location is considered for the task. If the application is configured so that only location is considered, the closest agent is auto-assigned to the task.

If the application is configured to use other selection criteria—such as skills, time zone, or schedule—the ratings of all selection criteria are averaged, and the agent with the highest overall rating is auto-assigned for the task. See [Agent auto assignment using multiple selection criteria](c_AgAtAssgmtMlt.md) for details.

**Parent Topic:**[Agent auto assignment using rating-based criteria](c_AgentAutoAssignUseRatBaseCrit.md)


```


### File: service-management-for-the-enterprise\c_AgentAutoAssignmentUsingSkills.md

```text
---
title: Agent auto assignment using skills
description: Agents can be auto assigned based on the skills of an agent, and the skills required to perform the task. Assign skills to an agent user records using Skills Users .
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent auto assignment using rating-based criteria, Agent auto assignment, Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Agent auto assignment using skills

Agents can be auto assigned based on the skills of an agent, and the skills required to perform the task. Assign skills to an agent user records using **Skills** &gt; **Users**.

Auto assignment by skills can be performed in either a [task- or request-driven processing](c_TaskVsRequestDrivenProcessing.md) environment when the **Auto-selection of agents for tasks requires them to have skills** configuration option must be set to **all** or **some** for the application.

When a task that includes skills is qualified or marked as **Ready for Work**, skills of each agent are compared with the skills required to perform the task, and a rating is calculated based on the skills configuration option. If the option is set to **some**, the agent with the closest skills match is auto-assigned the task. If the option is set to **all**, only agents who possess all the required skills are considered. If no agents possess all the skills required to perform the task, none are auto-assigned.

Skills rating of an agent is calculated as:

`Skills_agent/Skills_task`

When:

-   `Skills_agent` is the number of skills possessed by the agent that match the skills required for the task.
-   `Skills_task` is the total number of skills required for the task.

For example, if a task requires four skills, and Agent A possesses three of them and Agent B possesses two of them:

-   Skill rating of Agent A = 3/4 or 0.75
-   Skill rating of Agent B = 2/4 or 0.5

If the application is configured to use other selection criteria, such as location or time zone, the ratings of all selection criteria are averaged, and the agent with the highest overall rating is auto-selected for the task. See [Agent auto assignment using multiple selection criteria](c_AgAtAssgmtMlt.md) for details.

**Parent Topic:**[Agent auto assignment using rating-based criteria](c_AgentAutoAssignUseRatBaseCrit.md)


```


### File: service-management-for-the-enterprise\c_ClosedAndCompletedRequests.md

```text
---
title: Closed and completed requests
description: When the Request lifecycle option is set to request-driven, the assigned agent can complete and close the request once all the tasks in the request are complete.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Close a request, Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Closed and completed requests

When the **Request lifecycle** option is set to **request-driven**, the assigned agent can complete and close the request once all the tasks in the request are complete.

A **Close Complete** button is visible to the agent assigned to the request. The agent enters work notes before clicking **Close Complete**. When the button is clicked, the open task is automatically completed \(if applicable\) and the request transitions to the **Complete** state.

**Note:** To view all closed tasks, navigate to **All** &gt; **Field Service** &gt; **All Work Orders** and enter **Close Complete** in the **State** field.

**Parent Topic:**[Close a request](../task/t_CloseARequest.md)


```


### File: service-management-for-the-enterprise\c_EnhancedLabels.md

```text
---
title: Enhanced labels
description: Enhanced labels allow the end user to show any information on any mappable space \(fm\_space\), as the space label. Users choose to display the occupant name, the department name, or other custom field as the default label.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enhanced labels

Enhanced labels allow the end user to show any information on any mappable space \(fm\_space\), as the space label. Users choose to display the occupant name, the department name, or other custom field as the default label.

![In this figure, the enhanced label filtering feature is presented.](../image/EnhancedLabels.png "Enhanced Labels")

The label selector on the interactive map gives the user all fields on fm\_space including custom, user-defined fields, allowing any piece of information to be a label. In addition to fm\_space two special pieces of information are shown:

-   Sys\_users assigned to space based on the fm\_m2m\_user\_to\_space table
-   Departments assigned to the space based on the fm\_m2m\_department\_to\_space table

**Parent Topic:**[Interactive facility maps](c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\c_EnterpriseMove.md

```text
---
title: Enterprise move
description: Facility teams use Enterprise Move to plan and execute move scenarios in support of large or complex employee move requests.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enterprise move

Facility teams use Enterprise Move to plan and execute move scenarios in support of large or complex employee move requests.

The Facilities enterprise move process is as follows:

1.  A facilities administrator uses the Move Planning Tool to create scenarios of potential moves.
    -   A facilities administrator assigns delegators and move groups to each scenario.
    -   A facilities administrator reviews the scenarios and chooses the one to execute.
2.  Delegators access their assigned move scenarios and assign users to seats.
3.  Facilities staff members execute and facilitate the move through the Enterprise Move workflow.
    -   State changes are handled by UI actions and a workflow, which contains a required approval from facilities\_admin or move\_admin.

**Note:** The Service management workflow can be edited to meet customer-specific processes.

-   **[Move planning tool](c_MovePlanningTool.md)**  
The Move Planning tool displays occupancy totals by campus and floor. Facilities and move administrators can add or remove users to and from scenarios while planning a move. Groups of people are selected and moved by department \(department on sys\_user record\) or by direct manager \(manager on sys\_user record\).

**Parent Topic:**[Facilities move management](c_FacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\c_EnterpriseMoveDelegators.md

```text
---
title: Move delegators
description: Facilities administrators assign move delegators to assign users to locations.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate a delegator, Enterprise move scenarios, Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Move delegators

Facilities administrators assign move delegators to assign users to locations.

Move delegators are usually managers or someone assigned by the manager, to determine which locations users are moving into. Delegators assign locations on the floor plan, which are added to the move scenario and carried over to the move request and subsequent move tasks.

**Parent Topic:**[Activate a delegator](../task/t_ActivateADelegator.md)


```


### File: service-management-for-the-enterprise\c_FacMoveMgmt.md

```text
---
title: Facilities move management
description: Employees and managers can request single user moves. Members of the facilities staff can use the enterprise move tool to plan and execute large move scenarios involving multiple people, assets/CIs, and departments.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities move management

Employees and managers can request single user moves. Members of the facilities staff can use the enterprise move tool to plan and execute large move scenarios involving multiple people, assets/CIs, and departments.

The Facilities Move Management application benefits your organization in the following ways:

-   Streamlines the move process from request through execution
-   Reduces costs by avoiding unnecessary moves
-   Simplifies move planning through increased visibility of space resources
-   Provides reporting and insight into in-progress moves
-   Improves service delivery through better communication and coordination throughout a move process

**Note:** This feature is no longer available for new customers.

-   **[Facilities move requests](c_FacMoveRequests.md)**  
Both employees and managers can request a move, which initiates the workflow of tasks to complete that move. Any user can submit a move request through the Facilities catalog. Users with the Facilities staff role can also create and update facilities requests using the move request form directly.
-   **[Facilities move request templates](c_FacMoveReqTemplates.md)**  
The facilities staff adds templates to the facilities catalog, so users can select from subcategories for their request type.
-   **[Enterprise move](c_EnterpriseMove.md)**  
Facility teams use Enterprise Move to plan and execute move scenarios in support of large or complex employee move requests.

**Parent Topic:**[Facilities Service Management overview](../../facilities-service-management/concept/c_FacilitiesServiceManagement.md)


```


### File: service-management-for-the-enterprise\c_FacMoveReqTemplates.md

```text
---
title: Facilities move request templates
description: The facilities staff adds templates to the facilities catalog, so users can select from subcategories for their request type.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities move request templates

The facilities staff adds templates to the facilities catalog, so users can select from subcategories for their request type.

**Parent Topic:**[Facilities move management](c_FacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\c_FacMoveRequests.md

```text
---
title: Facilities move requests
description: Both employees and managers can request a move, which initiates the workflow of tasks to complete that move. Any user can submit a move request through the Facilities catalog. Users with the Facilities staff role can also create and update facilities requests using the move request form directly.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities move requests

Both employees and managers can request a move, which initiates the workflow of tasks to complete that move. Any user can submit a move request through the Facilities catalog. Users with the Facilities staff role can also create and update facilities requests using the move request form directly.

Facilities move management works in the following manner:

1.  A ServiceNow administrator activates and configures the Facilities Move Management application according to your organization's needs and requirements.
2.  A facilities administrator creates your organization's campus and configures the spaces and assets contained within.
3.  Users submit facilities move requests, including the name of user to be moved, the move from location, and the move to location.
4.  The move workflow creates tasks and updates the state of the move request.
5.  Facilities staff members perform the tasks necessary to fulfill the move request.
6.  The end of workflow script runs to update the user location and the location of all the asserts that were requested to be moved.

-   **[Create a move request through the facilities catalog](../task/t_CreateAMoveReqThruFacCatalog.md)**  
Users can submit move requests by selecting from the categories of the Facilities catalog.
-   **[Create a move request with the move request form](../task/t_CreateMoveReqWFacReqForm.md)**  
Facilities staff members can create move requests using the move request form.

**Parent Topic:**[Facilities move management](c_FacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\c_FacRequestTasks.md

```text
---
title: Facilities request tasks
description: A facilities request contains one or more tasks. These tasks allow qualifiers to define separate activities that must be done to complete a facilities request.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities request tasks

A facilities request contains one or more tasks. These tasks allow qualifiers to define separate activities that must be done to complete a facilities request.

Administrators can create multiple tasks under a single request. Splitting a request into separate tasks, when necessary, enables qualifiers to:

-   Assign different aspects of a request to different staff members.
-   Assign tasks to staff members with different skill sets.
-   Assign tasks to staff members in different locations.
-   Schedule parts of the work at different times.
-   Schedule tasks so they are done one after another.
-   Schedule tasks so they are done at the same time by different staff members.
-   Schedule more tasks, if necessary, to complete the request.

Users with these roles can edit schedule times, including windows and planned durations. The Estimated end time is calculated from the expected start time and the work duration and is read-only.

-   &lt;sm application&gt;\_qualifier: Tasks in the Draft state.
-   &lt;sm application&gt;\_dispatcher: Tasks in the Pending Dispatch state.
-   &lt;sm application&gt;\_admin: Tasks in Draft or Pending Dispatch state.

-   **[Create a facilities request task](../task/t_CreateAFacilitiesRequestTask.md)**  
Facilities request tasks are created from facilities requests.
-   **[Clone a request task](../task/t_CloneARequestTask.md)**  
Existing tasks can be cloned to create tasks with the same populated fields.
-   **[Create a task template for common task requests](../task/t_UseTaskTempForMultReqTemp.md)**  
If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.
-   **[Auto-dispatch a task](../../work-management/task/t_AutoDispatchATask.md)**  
When a task is auto-dispatched, the application matches the task with a nearby agent having the necessary skills and schedule that can accommodate the task.

**Parent Topic:**[Facilities service management process](../../facilities-service-management/concept/c_FacilitiesSMProcess.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesFloorPlan.md

```text
---
title: Facilities Floor Plan
description: Users use the floor plan find other users, spaces, and assets. Users can also create facilities requests from any space on the floor plan.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities Floor Plan

Users use the floor plan find other users, spaces, and assets. Users can also create facilities requests from any space on the floor plan.

Use the floor plan as follows:

1.  A ServiceNow administrator activates and configures the Facilities Floor Plan according to your organization's needs and requirements.
2.  A facilities administrator creates your organization's campus and configures the spaces and assets contained within.
3.  Users submit facilities and move requests and those request locations are tagged on the floor plan.
4.  Users can set filters to see particular spaces, users, and assets.
5.  From the workbench, administrators qualify facilities requests. This is the process of checking that the information in the request is complete, so facilities tasks can be assigned.
6.  Administrators organize requests into tasks that must be done before the request is complete, and dispatch those tasks.
7.  Facilities staff members perform the tasks necessary to fulfill the request.
8.  The assigned facilities staff members close their tasks, allowing the request to be closed.

-   **[Create a facility request from the floor plan](../task/t_CreateFacReqWorkbench.md)**  
All users in your organization can create any facility requests that your facilities admin \[facilities\_admin\] has enabled on the floor plan view.

**Parent Topic:**[Interactive facility maps](c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesRequestApprovals.md

```text
---
title: Facilities request approvals
description: Approving a facilities request means that the request has been reviewed and is ready to be qualified for facilities task creation and assignment. When a request is sent to a user with the facilities\_approver\_user role, the approver has several choices.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities request approvals

Approving a facilities request means that the request has been reviewed and is ready to be qualified for facilities task creation and assignment. When a request is sent to a user with the facilities\_approver\_user role, the approver has several choices.

If a facilities request is created from a template with a workflow in **Draft** state, and the **Ready to Work** button is clicked, the request goes to a **Submitted** state. The template workflow turns the **Submitted** state to **Ready** state. Users can include approvals in that workflow, if desired.

**Parent Topic:**[Facilities requests](c_FacilitiesRequests.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesRequests.md

```text
---
title: Facilities requests
description: A facilities request is a record in the system that tracks a proposed change to the physical facility of the organization. Typical facilities requests include the reporting of something bring broken or an issue like a beeping smoke alarm.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities requests

A facilities request is a record in the system that tracks a proposed change to the physical facility of the organization. Typical facilities requests include the reporting of something bring broken or an issue like a beeping smoke alarm.

-   **[Facilities request creation](../reference/r_FacilitiesRequestCreation.md)**  
Facilities service management uses the common service management request management process. Any user can submit a facilities request through the Facilities catalog. Users with the facilities\_staff role can also create and update facilities requests from the Facilities Request form.
-   **[Facilities request approvals](c_FacilitiesRequestApprovals.md)**  
Approving a facilities request means that the request has been reviewed and is ready to be qualified for facilities task creation and assignment. When a request is sent to a user with the facilities\_approver\_user role, the approver has several choices.
-   **[Facilities agent assignment](../reference/r_FacilitiesAgentAssignment.md)**  
Depending on your settings in the facilities configuration screen, you can assign agents manually or using auto-assignment.
-   **[Schedule blackout periods](c_ScheduleBlackout.md)**  
A blackout period prevents work from being performed in a defined area for a scheduled time period. Blackout periods can be defined for spaces, levels, buildings, campuses, and zones.
-   **[Collaborate on a request](../../planning-and-policy/task/t_CollaborateOnARequest.md)**  
Within a request, you can enter comments that are visible to the submitter, allowing for collaboration between the two of you. For collaboration with other agents, you can enter comments that are not visible to the submitter.
-   **[Change the location of a request](../../planning-and-policy/task/t_ChangeTheLocationOfARequest.md)**  
After opening a request, you can modify the details and update it.
-   **[Close a request](../../planning-and-policy/task/t_CloseARequest.md)**  
When you close a request, you can add details that you want the submitter to be aware of.

**Parent Topic:**[Facilities service management process](c_FacilitiesSMProcess.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesSMProcess.md

```text
---
title: Facilities service management process
description: The facilities administrator creates the campus and configures the application with workflow, agent assignment, and other considerations. Employees make facilities and move requests that are tracked to specific locations anywhere on the campus.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities service management process

The facilities administrator creates the campus and configures the application with workflow, agent assignment, and other considerations. Employees make facilities and move requests that are tracked to specific locations anywhere on the campus.

The Facilities Service Management process is as follows:

1.  A ServiceNow administrator activates and configures the Facilities Service Management application according to the needs and requirements for your organization.
2.  A facilities administrator creates the campus and configures the spaces and assets contained within.
3.  Users submit facilities requests.
4.  Facilities staff qualify facilities requests. Which is the process of checking that the information in the request is complete, so facilities tasks can be assigned.
5.  Administrators organize requests into tasks and dispatch those tasks.
6.  Facilities staff members perform the tasks necessary to fulfill the request.
7.  The assigned facilities staff members close their tasks, allowing the request to be closed.

Be sure to identify people within your organization that can be assigned the following facilities roles:

-   **facilities administrator**

    Creates and modifies all campuses, building, floors, rooms, and floor plans. They can also qualify and dispatch requests.

-   **facilities staff**

    Performs the work necessary to answer facilities requests.

-   **facilities dispatcher**

    Schedules and assigns the tasks to facilities staff.


-   **[Facilities requests](c_FacilitiesRequests.md)**  
A facilities request is a record in the system that tracks a proposed change to the physical facility of the organization. Typical facilities requests include the reporting of something bring broken or an issue like a beeping smoke alarm.
-   **[Facilities request tasks](../../planning-and-policy/concept/c_FacRequestTasks.md)**  
A facilities request contains one or more tasks. These tasks allow qualifiers to define separate activities that must be done to complete a facilities request.

**Parent Topic:**[Facilities Service Management overview](c_FacilitiesServiceManagement.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesServiceManagement.md

```text
---
title: Facilities Service Management overview
description: The Facilities Service Management application lets users request changes to the operation and maintenance of your facilities. The facilities staff can then track these requests and make the necessary changes.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Facilities Service Management, Service Management]
---

# Facilities Service Management overview

The Facilities Service Management application lets users request changes to the operation and maintenance of your facilities. The facilities staff can then track these requests and make the necessary changes.

The Facilities Service Management application offers the following benefits:

-   Indicates the location of a facility request so the facilities team knows exactly where users encountered the issue.
-   Identifies configuration items \(CIs\) for each facility request so you know which items in your infrastructure are also impacted.
-   Allows any user in the system to view all open facilities requests. Users can see the facilities issues that have already been reported before they submit a new request.

-   **[Activate Facilities Service Management](../task/t_ActivateFacilitiesSM.md)**  
The Facilities Service Management plugin \(com.snc.facilities\_service\_automation\) is now deprecated and no longer supported or available for new activation.
-   **[Activate Facilities Move Management](../../facilities-move-management/task/t_ActivateFacMoveMgmt.md)**  
The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.move\) plugins are now deprecated and no longer supported or available for new activation.
-   **[Activate Facilities Visualization Workbench](../../facilities-interactive-facility-maps/task/t_ActivateFacVisWorkbench.md)**  
The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.fvw\) plugins are now deprecated and no longer supported or available for new activation.
-   **[Facilities service management process](c_FacilitiesSMProcess.md)**  
The facilities administrator creates the campus and configures the application with workflow, agent assignment, and other considerations. Employees make facilities and move requests that are tracked to specific locations anywhere on the campus.
-   **[Domain separation and Facilities Service Management](domain-separation-facilities-service-mgt.md)**  
Domain separation is supported in Facilities Service Management. Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation, including which users can see and access data.
-   **[Space management](../reference/r_SpaceManagement.md)**  
The concept of space is part of the Facilities Service Management application. Space provides a definition at all levels with the same unit measure, and presents metrics that are readily available for analysis. These metrics include occupancy percentage, total space available, and so on.
-   **[Facilities move management](../../facilities-move-management/concept/c_FacMoveMgmt.md)**  
Employees and managers can request single user moves. Members of the facilities staff can use the enterprise move tool to plan and execute large move scenarios involving multiple people, assets/CIs, and departments.
-   **[Interactive facility maps](../../facilities-interactive-facility-maps/concept/c_InteractiveFacilityMaps.md)**  
The interactive facility maps, including the Workbench and the Floor Plan, provide a campus-level hierarchy, improving your facilities request tracking and space management. Decision makers in your organization can track, manage, and analyze spaces in support of organizational needs and users can find other users and assets.

**Parent Topic:**[Facilities Service Management](../reference/FacilitiesLandingPage.md)


```


### File: service-management-for-the-enterprise\c_FacilitiesWorkbench.md

```text
---
title: Facilities Workbench
description: Members of the facilities staff use the workbench to interact dynamically with the floor plan. Users have access to the floor plan \(but not the workbench\), from which they can find other users and spaces.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities Workbench

Members of the facilities staff use the workbench to interact dynamically with the floor plan. Users have access to the floor plan \(but not the workbench\), from which they can find other users and spaces.

Use the workbench as follows:

1.  A ServiceNow administrator activates and configures the Facilities Visualization Workbench application according to your needs and requirements.
2.  A facilities administrator creates your campus and configures the spaces and assets contained within.
3.  Users submit facilities and move requests and those request locations are tagged on the workbench.
4.  From the workbench, administrators qualify facilities requests. This process checks that the information in the request is complete, so facilities tasks can be assigned.
5.  Administrators organize requests into tasks that must be done before the request is complete, and dispatch those tasks.
6.  Facilities staff members perform the tasks necessary to fulfill the request.
7.  The assigned facilities staff members close their tasks, allowing the request to be closed.

    **Note:** Facilities Workbench is available on a mobile device, but with limited capabilities.


-   **[Find a move request](../task/t_FindMoveRequest.md)**  
Facilities and move staff can locate and manage move requests from the Moves tab within the workbench.
-   **[Find a facilities request](../task/t_FindFacilitesRequest.md)**  
Facilities administrators can locate and manage requests from the Requests tab within the workbench.
-   **[Edit a zone](../task/t_EditAZone.md)**  
Facilities administrators and staff can edit existing zones from the Zones tab within the workbench.

**Parent Topic:**[Interactive facility maps](c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\c_FieldControlsInStateFlows.md

```text
---
title: Field controls in state flows
description: You can define controls for individual fields that are enforced when a record transitions between states.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# Field controls in state flows

You can define controls for individual fields that are enforced when a record transitions between states.

Settings in the Field Controls section of the State Flow form enable you to apply field controls when the system detects a specified state transition or when the end state is the current state when the form is opened. The control is applied only to existing fields on the form. State flows cannot add fields to the form.

For example, you might want the **Problem** field to be visible when an incident moves to the **Awaiting Problem** state. If the incident state changes to **Awaiting User Info**, you hide the **Problem** field and make the **Caller** field mandatory.

Configure state flow records with an ending state only and create the correct behavior for every ending state you want to control. This ensures that the field controls are set properly when the user selects a new state, and also when the user returns a record's **State** field to the original state. Only specify a full state transition, with both a starting and ending state, when you want a particular behavior for that precise state transition.

**Note:** State flows use client scripts to enforce field controls. It is possible that your settings can be changed by existing UI policies, which execute after client scripts.

**Parent Topic:**[State flow customization](c_StateFlowCustomization.md)

**Related topics**  


[Request states](../../planning-and-policy/reference/r_SMRequestStates.md)

[Request task states](../../planning-and-policy/reference/r_SMRequestTaskStates.md)


```


### File: service-management-for-the-enterprise\c_ImpDsblStFl.md

```text
---
title: Implications of disabling SM state flows
description: State flows are used by SM applications to control how a work order or request automatically transitions from one state to the next. When state flows are disabled, various aspects of the ServiceNow system are also changed, as described here.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service management states, Service Management]
---

# Implications of disabling SM state flows

State flows are used by SM applications to control how a work order or request automatically transitions from one state to the next. When state flows are disabled, various aspects of the ServiceNow system are also changed, as described here.

Review the following implications before setting the **Enable state flows** configuration option to **Off**. After the configuration is saved, state flows cannot be re-enabled from the user interface.

When state flows are disabled, the state transition-related behavior of the following business rules, UI actions, and security rules are affected.

-   **Business rules on requests:**
    -   Group change validation
    -   Move tasks to pending assignment
    -   Request-driven dispatch
    -   Unassigned
    -   Verify work notes
-   **Business rules on tasks:**
    -   Apply dispatch method
    -   Populate schedule
    -   Populate schedule - new SOT \(service order task\)
    -   Transitions
    -   Unassigned
-   **The following business rules run partially:**
    -   The part of **Build scratchpad and display info messages** that shows an error message if a task is pending dispatch and auto-assignment fails is disabled.
    -   For the **Validate changes** business rule, the only part that runs is when the system checks for work notes and rolls them up.
-   **UI actions on requests:**
    -   When the **Spam** button on the request form is clicked, the state is not changed, but the work notes indicate that the request was closed as spam.
-   **UI actions on tasks:**
    -   Assign to me
    -   View task on map
    -   New
-   **Security rules:**
    -   State-based aspects of security rules no longer apply. For example, when state flows are enabled, the **Short description** field is not editable when a request or task is closed complete, incomplete, or canceled. When state flows are disabled, the **Short description** is always editable.
    -   Role-based aspects of security rules continue to apply when state flows are disabled.
-   **Additional changes when state flows are disabled:**
    -   The process flow formatter is removed from request and task forms.
    -   The **State** field can be edited on request and task forms.
    -   The following configuration fields are changed:
        -   **Process lifecycle** is set to **request-driven**.
        -   **Assignment method for requests** is set to **manual**.
        -   **Assignment method for tasks** is set to **manual**.
        -   **Approval for new request required** is disabled.
        -   **Qualification is required for new requests** is disabled.
        -   **Agent must accept or reject the assigned task** is disabled.
        -   **Use dispatch queue** is disabled.

-   **[Re-enable state flows](../task/t_ReEnableStateFlows.md)**  
When service management state flows have been disabled, they cannot be re-enabled from the user interface.

**Parent Topic:**[Service management states](../../it-services/concept/c_ServiceManagementStates.md)


```


### File: service-management-for-the-enterprise\c_InteractiveFacilityMaps.md

```text
---
title: Interactive facility maps
description: The interactive facility maps, including the Workbench and the Floor Plan, provide a campus-level hierarchy, improving your facilities request tracking and space management. Decision makers in your organization can track, manage, and analyze spaces in support of organizational needs and users can find other users and assets.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Interactive facility maps

The interactive facility maps, including the Workbench and the Floor Plan, provide a campus-level hierarchy, improving your facilities request tracking and space management. Decision makers in your organization can track, manage, and analyze spaces in support of organizational needs and users can find other users and assets.

**Note:** This feature is no longer available for new customers.

The interactive facility maps offer the following benefits:

-   The workbench provides the exact location of a facilities request on a campus map, so the facilities team knows exactly where users encountered the issue.
-   Maps are available to anyone in the organization, so users can search for people or spaces on the map.
-   Configuration items \(CIs\) on each request identifies the impacted items in your infrastructure.
-   You can see affected spaces with zone creation by particular actions, like construction or maintenance of equipment that services those zones.
-   Define spaces with capacity metrics \(gross space, usable space, assignable space, occupiable space\) for reporting and financials.

-   **[Map filters](../reference/r_MapFilters.md)**  
Users can filter the map to determine how various spaces are colored.
-   **[Enhanced labels](c_EnhancedLabels.md)**  
Enhanced labels allow the end user to show any information on any mappable space \(fm\_space\), as the space label. Users choose to display the occupant name, the department name, or other custom field as the default label.
-   **[Map settings](../reference/r_MapSettings.md)**  
Map settings allow the facilities staff or users to choose the appearance of their floor plan.
-   **[Find a space or user on a mobile interface](../task/t_FindSpaceUserMobile.md)**  
Quickly find a conference room, office, cubicle, or another employee in your organization on a mobile interface.
-   **[Find a space or user](../task/t_FindASpaceOrUser.md)**  
All users in your organization, regardless of their role, can search for other users and spaces. The results are ordered by current level or floor, current campus, and other campuses.
-   **[Find an asset or CI](../task/t_FindAssetorCI.md)**  
All users in your organization, regardless of their role, can search for assets and CIs. The results are ordered by current level or floor, current campus, and other campuses.
-   **[Show any task on a map](../task/t_ShowAnyTaskOnMap.md)**  
Custom tables that are extended from task can be created, shown, and managed on the interactive map. The location field on the task, must be a mappable space \(fm\_space\). There are some location fields on task that may have a reference qualifier that does not allow fm\_space be used.
-   **[Facilities Floor Plan](c_FacilitiesFloorPlan.md)**  
Users use the floor plan find other users, spaces, and assets. Users can also create facilities requests from any space on the floor plan.
-   **[Facilities Workbench](c_FacilitiesWorkbench.md)**  
Members of the facilities staff use the workbench to interact dynamically with the floor plan. Users have access to the floor plan \(but not the workbench\), from which they can find other users and spaces.

**Parent Topic:**[Facilities Service Management overview](../../facilities-service-management/concept/c_FacilitiesServiceManagement.md)


```


### File: service-management-for-the-enterprise\c_Lounge.md

```text
---
title: Lounge
description: When a facilities administrator sets up a move scenario without specifying the destination building or floor, the users are moved to the lounge.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Plan a move scenario, Enterprise move scenarios, Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Lounge

When a facilities administrator sets up a move scenario without specifying the destination building or floor, the users are moved to the lounge.

![In this figure, the Lounge shows four users needing a destination on the campus.](../image/Lounge.png "Move Planning Tool Lounge")

**Parent Topic:**[Plan a move scenario](../task/t_PlanScenarioMPT.md)


```


### File: service-management-for-the-enterprise\c_MovePlanningTool.md

```text
---
title: Move planning tool
description: The Move Planning tool displays occupancy totals by campus and floor. Facilities and move administrators can add or remove users to and from scenarios while planning a move. Groups of people are selected and moved by department \(department on sys\_user record\) or by direct manager \(manager on sys\_user record\).
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Move planning tool

The Move Planning tool displays occupancy totals by campus and floor. Facilities and move administrators can add or remove users to and from scenarios while planning a move. Groups of people are selected and moved by department \(department on sys\_user record\) or by direct manager \(manager on sys\_user record\).

The move planning tool also contains three tabs to help in enterprise move planning.

<table id="table_qjv_hvd_dv"><thead><tr><th>

Tab

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Scenarios

</td><td>

-   Create or change scenarios
-   Change the campus you are viewing
-   See current seating capacity

</td></tr><tr><td>

Planning

</td><td>

-   Choose how you want to select groups to move: by department or manager
-   Select a group and color that group on the map

</td></tr><tr><td>

Display

</td><td>

-   Select how segments are displayed
-   Hide buildings and floors

</td></tr></tbody>
</table>![In this figure, the Move Planning Tool is displayed with different colors representing categories per floors in a building.](../image/MPTPlanningTab.png "Move Planning Tool")

-   **[Enterprise move scenarios](../reference/r_EnterMoveScenarios.md)**  
Move scenarios are used by the Facilities team to see the implications of a move in relation to other moves. Multiple scenarios can be created.
-   **[Enterprise move details](../reference/r_EnterMoveDetails.md)**  
Enterprise move details are created when people are added to the scenario. Move details contain information about the move for a specific person, such the destination floor, destination building, need for moving boxes, or a security badge update.
-   **[Enterprise move requests](../reference/r_EnterMoveRequests.md)**  
Enterprise move requests are managed by a workflow, which contains required approvals from facilities\_admin or move\_admin. State changes are handled by UI actions.
-   **[Enterprise move tasks](../reference/r_EnterMoveTasks.md)**  
Before a move can be executed, destination locations for all users must be complete. Move tasks are based on check boxes on the request form.

**Parent Topic:**[Enterprise move](c_EnterpriseMove.md)


```


### File: service-management-for-the-enterprise\c_RebuildStateFlows.md

```text
---
title: Rebuild state flows
description: You can rebuild state flows when a mismatch between existing and new sys\_ids occurs.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# Rebuild state flows

You can rebuild state flows when a mismatch between existing and new sys\_ids occurs.

When you use an XML file to import a state flow record into an instance, the system attempts to match the incoming states with existing states by comparing sys\_ids. Because the sys\_ids of items in a choice list can vary between instances, the system can fail to match the states, even though they are otherwise identical.

When matching fails, the start and end states of affected records are left blank or contain numeric values. To repair these records navigate to **State Flows** &gt; **Admin** &gt; **Rebuild State Flows**. This module runs a script that compares the numerical value of each item in the **State** field choice list until it finds a match in the imported state flow record.

**Parent Topic:**[State flow customization](c_StateFlowCustomization.md)


```


### File: service-management-for-the-enterprise\c_RequestApprovals.md

```text
---
title: Request approvals
description: Approving a request in an SM application means that the request is ready for task creation and assignment.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Request approvals

Approving a request in an SM application means that the request is ready for task creation and assignment.

When a request is sent to a user with the \[SM application\]\_approver\_user role, the approver has several choices. If you select **Approval is required for new requests** in the applications Configuration screen, a newly created request automatically moves to the **Awaiting Approval** state. Otherwise, the request moves to the next configured state.

<table id="table_syj_r13_yq"><thead><tr><th>

Approval Choice

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Approved

</td><td>

The request is approved.

</td></tr><tr><td>

Rejected

</td><td>

The request is not qualified and it is moved to the canceled state. Also, the following work note is added to the request:

 **The \[SM application\] request is rejected.**

</td></tr><tr><td>

More information required

</td><td>

The request does not contain enough information. It reverts to the **Draft** state and the following work note is added to the request:

 **The \[SM application\] request needs more information for further approval.**

</td></tr><tr><td>

Duplicate

</td><td>

The request is no longer required, because another request has already performed the work. The request is moved to the **Cancelled** state and the following work note is added to the request:

 **This is a duplicate \[SM application\] request.**

</td></tr></tbody>
</table>**Parent Topic:**[Request Management in a Service Management application](rm-sm-application.md)


```


### File: service-management-for-the-enterprise\c_RequestTasksMgmt.md

```text
---
title: Request task management
description: A request contains one or more tasks. These tasks allow qualifiers to define activities that must be done to complete a request.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Request task management

A request contains one or more tasks. These tasks allow qualifiers to define activities that must be done to complete a request.

Administrators can create multiple tasks under a single request.

Splitting a request into separate tasks, when necessary, enables qualifiers to do the following:

-   Assign different aspects of a request to different staff members.
-   Assign tasks to staff members who have different set of skills, or are in different locations.
-   Schedule tasks so they are either done one after another, or at the same time by different staff members.
-   Schedule additional tasks, if necessary, to complete the request.

**Note:** If you have the Request life cycle is request driven configuration option activated, you can manually add tasks as needed. If you have Request life cycle is task driven activated, an initial task is automatically created when the request record is created.

## Configuration Overview

Optionally, set up one or more additional request task management configurations:

-   [Task windows](../reference/r_TaskWindows.md)

    Set a task window to define the time period for performing the task by specifying the start and end dates.

-   [Create a task template for common task requests](../task/t_UseTaskTempForMultReqTemp.md)

    Create task templates to efficiently manage frequently repeated tasks across multiple jobs. By reusing these templates in various request templates, you save time and ensure consistency. Task templates can also be used in Work Order requests to automatically include common information, streamlining the process and minimizing errors.

-   [Clone a request task](../task/t_CloneARequestTask.md)

    Clone an existing task to save time and ensures consistency by allowing administrators to quickly replicate tasks while reducing errors and enabling easy customization.


-   **[Create request tasks](../task/t_CreateRequestTasks.md)**  
Tasks are created in support of requests.
-   **[Request task states](../reference/r_SMRequestTaskStates.md)**  
Like requests, the associated request tasks follow a specific life cycle and move through a series of states, which are displayed in the **State** field on the task record.
-   **[Task windows](../reference/r_TaskWindows.md)**  
A task window is the time period, bordered by start and end times, in which a task is performed.
-   **[Create a task template for common task requests](../task/t_UseTaskTempForMultReqTemp.md)**  
If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.
-   **[Clone a request task](../task/t_CloneARequestTask.md)**  
Existing tasks can be cloned to create tasks with the same populated fields.

**Parent Topic:**[Request Management in a Service Management application](rm-sm-application.md)

**Related topics**  


[Change the location of a request](../task/t_ChangeTheLocationOfARequest.md)

[Request approvals](c_RequestApprovals.md)

[Collaborate on a request](../task/t_CollaborateOnARequest.md)

[Close a request](../task/t_CloseARequest.md)


```


### File: service-management-for-the-enterprise\c_ScheduleBlackout.md

```text
---
title: Schedule blackout periods
description: A blackout period prevents work from being performed in a defined area for a scheduled time period. Blackout periods can be defined for spaces, levels, buildings, campuses, and zones.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Schedule blackout periods

A blackout period prevents work from being performed in a defined area for a scheduled time period. Blackout periods can be defined for spaces, levels, buildings, campuses, and zones.

Blackout business rules check the **Schedules** field of the **Location** field on a request or task to assess if there are any schedule conflicts with the time span of current.expected\_start to current.estimated\_end.

|Business rule|Action|
|-------------|------|
|Display Space Schedule Conflicts \(facilities\_request business rule\)|If the current.expected\_start and current.estimated\_end are populated and the location is a facilities space, informs the user of any possible schedule conflicts.|
|Display Space Schedule Conflicts \(facilities\_request\_task business rule\)|If the current.expected\_start and current.estimated\_end are populated and the location is a facilities space, informs the user of any possible schedule conflicts.|
|Prevent Space Schedule Conflicts \(facilities\_request\_task business rule\)|If there are any possible schedule conflicts between `now` and `now + estimated_work_duration`, prevent the user from starting work. To override, a facilities\_admin can use a field override\_schedule\_conflict|

-   **[Create a facilities schedule blackout](../task/t_CreateFacScheduleBlackout.md)**  
Blackout periods can be defined for spaces, levels, buildings, campuses, and zones. The Facilities\_admin can override blackout period requests.

**Parent Topic:**[Facilities requests](c_FacilitiesRequests.md)


```


### File: service-management-for-the-enterprise\c_ServiceManagement.md

```text
---
title: Service Management
description: Service Management \(SM\) refers to the ServiceNow service management applications you install, such as Facilities Service Management. Each of these applications allow you to manage business functions that require a request-type workflow where requests are approved, qualified, assigned, and completed.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
---

# Service Management

Service Management \(SM\) refers to the ServiceNow service management applications you install, such as Facilities Service Management. Each of these applications allow you to manage business functions that require a request-type workflow where requests are approved, qualified, assigned, and completed.

-   **[Activate Service Management](../task/t_ActivateServiceManagement.md)**  
The Service Management Core plugin is activated automatically when you activate any service management application.
-   **[Service management states](c_ServiceManagementStates.md)**  
From creation until closure, SM application requests for work \(for example, work orders and facilities requests\), and their respective tasks follow a life cycle tracked by the **State** field in Field Service Management and Facilities Service Management.
-   **[Service Management Core installation reference](../../service-management-core/reference/r_ServMgmtCoreInstallRef.md)**  
Service Management Core includes several feature plugins. Each of these plugins installs several types of components in support of the service management process.
-   **[Planned Maintenance](../../service-management-planned-maintenance/concept/c_SMPlanMaint.md)**  
The Planned Maintenance application is not a Service Management application, but it works with Service Management applications to help organizations manage regular preventive maintenance of assets.
-   **[Facilities Service Management](../../facilities-service-management/reference/FacilitiesLandingPage.md)**  
With the ServiceNow® Facilities Service Management application, you can request changes to the operation and maintenance of your facilities, track these requests, and make the necessary changes.
-   **[Request Management in a Service Management application](../../planning-and-policy/concept/rm-sm-application.md)**  
Agents regularly access request records as they resolve requests and correspond with the submitters. They can also access built-in reports to see information like the number of active or unassigned requests for an SM application.


```


### File: service-management-for-the-enterprise\c_ServiceManagementStates.md

```text
---
title: Service management states
description: From creation until closure, SM application requests for work \(for example, work orders and facilities requests\), and their respective tasks follow a life cycle tracked by the State field in Field Service Management and Facilities Service Management.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Service management states

From creation until closure, SM application requests for work \(for example, work orders and facilities requests\), and their respective tasks follow a life cycle tracked by the **State** field in Field Service Management and Facilities Service Management.

The life cycle is controlled through business rules and UI actions that are updated by the system automatically.

**Note:** The **State** field on the record is always read-only.

-   **[State flow customization](c_StateFlowCustomization.md)**  
State flows control the sequence in which records transition between states in Service Management applications.
-   **[State flow example](../task/t_StateFlowExample.md)**  
Your business processes might require work order tasks to be accepted automatically when dispatched to an agent.
-   **[Implications of disabling SM state flows](../../planning-and-policy/concept/c_ImpDsblStFl.md)**  
State flows are used by SM applications to control how a work order or request automatically transitions from one state to the next. When state flows are disabled, various aspects of the ServiceNow system are also changed, as described here.

**Parent Topic:**[Service Management](c_ServiceManagement.md)

**Related topics**  


[bundle-fsm.t_CustomizeAStateFlow]


```


### File: service-management-for-the-enterprise\c_SpaceRollupCalculations.md

```text
---
title: Space roll up calculations
description: The Facilities Service Management application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups apply to spaces that are designated as 'occupiable'. The occupancy values from that space are rolled up to the level above them.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Space roll up calculations

The Facilities Service Management application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups apply to spaces that are designated as 'occupiable'. The occupancy values from that space are rolled up to the level above them.

An occupiable space is designated by selecting the check box on the facility space record. The **Current occupancy** and **Percent occupied** fields rely on the **Occupiable** option. Roll up calculations are modified in a script include.

![image is a screen shot showing the Occupiable check box and dependant fields](../image/Occupiable.png "Occupiable selected and dependent fields")

The values that roll up are:

-   occupancy
-   max occupancy
-   assignable area

The percent occupied calculation takes place based on the current and max occupancy values.

**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\c_StateFlowCustomization.md

```text
---
title: State flow customization
description: State flows control the sequence in which records transition between states in Service Management applications.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Service management states, Service Management]
---

# State flow customization

State flows control the sequence in which records transition between states in Service Management applications.

An administrator can perform the following tasks:

-   Add or delete states.
-   Trigger events on particular state transitions.
-   Transition to another state automatically when data in a request or its task changes, or change states manually when the user clicks a button.
-   Limit the choice list for the State field to those end states that are valid transitions from the given start state.
-   Control the visibility and behavior of selected fields on a target table when records in that table change states.
-   Create custom state flows. Turn off the **State flows are enabled** option on the configuration screen. Creating custom state flows requires scripting knowledge.

**Note:** Users with the wm\_admin role can create, read, update, and delete only work order flows and work task flows. Users with the facilities\_admin role can create, read, update, and delete only facilities request flows and request task flows. Users with the wm\_admin role cannot manipulate facilities records, and users with the facilities\_admin role cannot manipulate work order records.

## How SM request and task state flows work

State flows replace the standard process that controls how requests and their associated tasks move between states. The ServiceNow system creates business rules, client scripts, and UI actions that perform the transitions and field controls you specify. These programming elements remain in use while the state flow records that use them are present. When state flows on an SM application table are deleted, the system attempts to delete any unnecessary programming elements that were created on that table. You can limit the selections for the State field to valid states for the transition, based on the starting state.

State flows provide the following controls:

-   **Manual transitions:**A UI action, created automatically by the system when you provide a condition or a script, initiates a transition.
-   **Automatic transitions:**A business rule, created automatically by the system when you provide a condition and a script, initiates a transition when changes are made to a request or task.

## Features available with state flows

-   **Custom transitions:** Customize the order in which states can change for requests and task records.
-   **Field controls:** Control the behavior and visibility of specific fields when a task changes states or reaches a specified end state.
-   **State choice list:**Limit the values offered in a task record State field to valid states for that transition. This is the same client script that the system creates to manage field controls for state transitions.
-   **Events:**Trigger events when a state transition occurs or when a record reaches a specific end state.

## Start and end states

You can create a custom state flow for processing that must occur when a task record makes a specific transition from one state to another. These records require a starting state and an ending state, and processing occurs during the transition between states. To perform some processing when a task record reaches a particular end state, you only need to define the end state. In some cases a state flow can have a starting state only, such as when you need to perform some type of cleanup after a task is canceled. A state flow might have no starting or ending state if the processing in the record applies to more than one state transition.

The solution is to store the business rule or client script in a state flow record and create a condition to trigger processing for any state change that requires it. An example of this in field service management is the Roll Up Changes business rule on the Work Order Task \[wm\_task\] table. This business rule rolls up state changes that occur in tasks to the parent work order.

-   **[State flow dictionary overrides](../task/t_StateFlowDictionaryOverrides.md)**  
A dictionary override in a state flow defines the starting state for all new records in a specific table. You set an override in tables that extend a base table only, so that your customizations are applied only to the extended table.
-   **[Work notes in state flows](c_WorkNotesInStateFlows.md)**  
Work notes are an important part of the state flow process and are used to communicate information about state transitions.
-   **[Field controls in state flows](c_FieldControlsInStateFlows.md)**  
You can define controls for individual fields that are enforced when a record transitions between states.
-   **[Trigger events on state changes](../task/t_TriggerEventsOnStateChanges.md)**  
You can configure a state flow to trigger a registered system event when a task transitions from a starting state to a specified end state. For example, you can use events to trigger email notifications and create script actions.
-   **[Rebuild state flows](c_RebuildStateFlows.md)**  
You can rebuild state flows when a mismatch between existing and new sys\_ids occurs.
-   **[State flow cleanup](../reference/r_StateFlowCleanup.md)**  
The business rules, client scripts, and UI actions that the system creates automatically to perform custom transitions exist only while the state flow records that use them are present.

**Parent Topic:**[Service management states](c_ServiceManagementStates.md)


```


### File: service-management-for-the-enterprise\c_TaskVsRequestDrivenProcessing.md

```text
---
title: Task vs. request driven processing
description: All applications use either task-driven or request-driven processes for handling tasks.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Task vs. request driven processing

All applications use either task-driven or request-driven processes for handling tasks.

Each application defaults to one or the other of these processing types, but you can switch between them as needed.

Task-driven processing means that the work order or request simply contains a list of tasks necessary for completing the overall work. When a work order record is created, an associated task record is automatically created. A request must have at least one task, and more tasks can be defined to handle all aspects of the request. As tasks are performed and completed, the request transitions through a series of states. After the last task is closed, the request automatically transitions to closed.

Request-driven processing means that tasks are assigned to a request, but closing all the tasks does not automatically close the request. A request does not require any tasks and can be opened and closed independently. Any tasks can be transitioned and assigned independently and to different agents than specified on the request. Even if all tasks are closed, the request can remain open and continue to be worked on. However, the request cannot be closed until all tasks are also closed. In request-driven processing, state transitions are based solely on the request.

**Parent Topic:**[Configure Facilities Service Management](../../facilities-service-management/task/t_ConfigureFacilities.md)


```


### File: service-management-for-the-enterprise\c_TransformMap.md

```text
---
title: Transform map
description: A transform map is an .xls file that allows you to add spaces or details about spaces from other sources into the space management application.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Run transform to update data, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Transform map

A transform map is an .xls file that allows you to add spaces or details about spaces from other sources into the space management application.

Transform maps must be run separately for floors and spaces. Unique spaces are identified based on a combination of the building name, floor, and space name and must be included in the transform map.

For your convenience, ServiceNow provides two transform maps for your use:

-   imp\_facilities\_data
-   imp\_facilities\_level\_data

For instructions, see [Run transform to update data](../task/t_RunTransform.md).

**Parent Topic:**[Run transform to update data](../task/t_RunTransform.md)


```


### File: service-management-for-the-enterprise\c_WorkNotesInStateFlows.md

```text
---
title: Work notes in state flows
description: Work notes are an important part of the state flow process and are used to communicate information about state transitions.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# Work notes in state flows

Work notes are an important part of the state flow process and are used to communicate information about state transitions.

The state flow adds work notes into the **Work notes** field of any task making this transition. For example, you might include the note, "Task rejected by agent" in the **Reject** state flow, which occurs when the task moves from **Assigned** to **Pending Dispatch**. If an agent rejects the task and fails to enter a work note, this note tells the dispatcher why the task reappeared in the dispatch queue. Work notes added by an agent rejecting the task are appended to the work notes that are inherited from the state flow.

These rules apply to state flow work notes:

-   For a state flow with no **Starting state**, the work note is added every time the task transitions to the **Ending state**.
-   For a state flow with a **Starting state** and an **Ending state**, the work note is added only when the task transitions from that starting state to that ending state.
-   If two state flows with work notes have the same **Ending state**, but only one has a **Starting state**, the system adds the work notes from the state flow with the starting state. This better matches the state flow work note to the more important transition between specific starting and ending states. In the example here, the work note information is more pertinent to a task moving from **Assigned** to **Pending Dispatch** than to a task that reaches the Pending Dispatch state from an undetermined beginning state.

**Parent Topic:**[State flow customization](c_StateFlowCustomization.md)

**Related topics**  


[State flow customization](c_StateFlowCustomization.md)

[Request states](../../planning-and-policy/reference/r_SMRequestStates.md)

[Request task states](../../planning-and-policy/reference/r_SMRequestTaskStates.md)


```


### File: service-management-for-the-enterprise\domain-separation-facilities-service-mgt.md

```text
---
title: Domain separation and Facilities Service Management
description: Domain separation is supported in Facilities Service Management. Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation, including which users can see and access data.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Domain separation and Facilities Service Management

Domain separation is supported in Facilities Service Management. Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation, including which users can see and access data.

## Support level: Basic



-   Business logic: Ensure that data goes into the proper domain for the application’s service provider use cases.
-   The application supports domain separation at run time. The domain separation includes separation from the user interface, cache keys, reporting, rollups, and aggregations.
-   The owner of the instance must set up the application to function across multiple tenants.

Sample use case: When a service provider \(SP\) uses chat to respond to a tenant-customer’s message, the customer must be able to see the SP's response.

For more information on support levels, see [Application support for domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-separated-apps.md).

**Parent Topic:**[Facilities Service Management overview](c_FacilitiesServiceManagement.md)

**Related topics**  


[Domain separation for service providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-sep-landing-page.md)


```


### File: service-management-for-the-enterprise\index.md

```text
---
title: Australia Service Management
locale: en-US
release: australia
bundle: sm4e
doc_type: toc
---

# Australia Service Management

- [Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_ServiceManagement.md) -- Service Management (SM) refers to the ServiceNow service management applications you install, such as Facilities Service Management. Each of these applications allow you to manage business functions that require a request-type workflow where requests are approved, qualified, assigned, and completed.
  - [Activate Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ActivateServiceManagement.md) -- The Service Management Core plugin is activated automatically when you activate any service management application.
    - [Activate other Service Management applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ActivateOtherSMApplications.md) -- After the Service Management Core plugin has been activated, you can activate other SM applications, such as Field Service management and facilities service management. You can also activate CMS portals for each of these SM applications to add them to the Service Management Portal.
  - [Service management states](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_ServiceManagementStates.md) -- From creation until closure, SM application requests for work (for example, work orders and facilities requests), and their respective tasks follow a life cycle tracked by the State field in Field Service Management and Facilities Service Management.
    - [State flow customization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_StateFlowCustomization.md) -- State flows control the sequence in which records transition between states in Service Management applications.
      - [State flow dictionary overrides](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_StateFlowDictionaryOverrides.md) -- A dictionary override in a state flow defines the starting state for all new records in a specific table. You set an override in tables that extend a base table only, so that your customizations are applied only to the extended table.
      - [Work notes in state flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_WorkNotesInStateFlows.md) -- Work notes are an important part of the state flow process and are used to communicate information about state transitions.
      - [Field controls in state flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FieldControlsInStateFlows.md) -- You can define controls for individual fields that are enforced when a record transitions between states.
      - [Trigger events on state changes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_TriggerEventsOnStateChanges.md) -- You can configure a state flow to trigger a registered system event when a task transitions from a starting state to a specified end state. For example, you can use events to trigger email notifications and create script actions.
      - [Rebuild state flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_RebuildStateFlows.md) -- You can rebuild state flows when a mismatch between existing and new sys_ids occurs.
      - [State flow cleanup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_StateFlowCleanup.md) -- The business rules, client scripts, and UI actions that the system creates automatically to perform custom transitions exist only while the state flow records that use them are present.
    - [State flow example](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_StateFlowExample.md) -- Your business processes might require work order tasks to be accepted automatically when dispatched to an agent.
    - [Implications of disabling SM state flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_ImpDsblStFl.md) -- State flows are used by SM applications to control how a work order or request automatically transitions from one state to the next. When state flows are disabled, various aspects of the ServiceNow system are also changed, as described here.
      - [Re-enable state flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ReEnableStateFlows.md) -- When service management state flows have been disabled, they cannot be re-enabled from the user interface.
  - [Service Management Core installation reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ServMgmtCoreInstallRef.md) -- Service Management Core includes several feature plugins. Each of these plugins installs several types of components in support of the service management process.
    - [Installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Tables installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Properties installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Roles installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Script includes installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Client script includes installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Business rules installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
      - [Email notifications installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md) -- Several types of components are installed with the Service Management Core plugin.
  - [Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/c_SMPlanMaint.md) -- The Planned Maintenance application is not a Service Management application, but it works with Service Management applications to help organizations manage regular preventive maintenance of assets.
    - [Activate Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_ActivatePlanMaint.md) -- The SM Planned Maintenance plugin is available as a separate subscription.
      - [Installed with SM Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_InstallWServMgmtPlanMaint.md) -- The SM Planned Maintenance core plugin also includes demo data.
    - [Managing maintenance plans](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/c_MaintPlanMgmt.md) -- Planned Maintenance allows you to create, maintain, and schedule maintenance for equipment that requires regular maintenance.
      - [Create a maintenance plan](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_CreateAMaintPlan.md) -- When creating a maintenance plan, options on the form help to determine how and when maintenance should be performed.
      - [Property settings for Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/planned-maint-properties.md) -- You configure Planned Maintenance properties at Planned Maintenance Properties .
      - [Configure a maintenance schedule](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_DefineAMaintSched.md) -- After creating a maintenance plan, define specific criteria for determining when the plan should be executed.
        - [Changes to maintenance schedules](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/c_ChangesToMaintSched.md) -- If you make and save changes to an existing maintenance schedule, any previously associated records are updated accordingly.
      - [Associate a maintenance plan to filtered records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_AssocMaintPlanToFilterRec.md) -- You can configure a maintenance plan with filtering criteria. For example, you can apply a maintenance plan to all records containing computers that start with "apple".
      - [Associate a schedule template to matching records](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_AssocSchedTempToMatchRec.md) -- The instance adds templates to a maintenance schedule so the appropriate requests and tasks, such as work orders and facilities requests, can be auto-generated when a maintenance schedule runs.
      - [Run a scheduled job to execute a maintenance schedule](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_RunSchedJobToExecMaintSched.md) -- Maintenance schedules are executed whenever the meter, duration, script, or condition criteria is met. You can also use the Schedule ad-hoc feature to run a maintenance schedule manually.
      - [Run a maintenance schedule on demand](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_RunAMaintSchedOnDemand.md) -- Maintenance schedules are typically run using the scheduled job named Planned Maintenance Nightly Run. However, you may want to run the schedule immediately or change the date when a schedule runs.
      - [View a maintenance log](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/t_ViewAMaintLog.md) -- You can view all maintenance performed on a particular CI, the next scheduled maintenance, and the last time maintenance was performed.
    - [Maintenance plan examples](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_MaintPlanExamples.md) -- You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.
      - [Define a maintenance schedule for a computer reboot](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_MaintPlanExamples.md) -- You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.
      - [Define a maintenance schedule for an ink cartridge replacement](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_MaintPlanExamples.md) -- You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.
      - [Define a maintenance schedule to run antivirus software](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_MaintPlanExamples.md) -- You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.
    - [Domain separation and Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/domain-separation-planned-maintenance.md) -- Domain separation is supported in Planned Maintenance. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
  - [Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/FacilitiesLandingPage.md) -- With the ServiceNow Facilities Service Management application, you can request changes to the operation and maintenance of your facilities, track these requests, and make the necessary changes.
    - [Facilities Service Management overview](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacilitiesServiceManagement.md) -- The Facilities Service Management application lets users request changes to the operation and maintenance of your facilities. The facilities staff can then track these requests and make the necessary changes.
      - [Activate Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ActivateFacilitiesSM.md) -- The Facilities Service Management plugin (com.snc.facilities_service_automation) is now deprecated and no longer supported or available for new activation.
        - [Create a group](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateAGroup.md) -- Set up groups and assign the necessary roles and users. The users in the group inherit the roles of the group, so you do not have to assign roles to each user separately.
        - [Configure Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ConfigureFacilities.md) -- Facilities administrators can set facilities configurations to determine how the system handles daily operations.
          - [Task vs. request driven processing](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_TaskVsRequestDrivenProcessing.md) -- All applications use either task-driven or request-driven processes for handling tasks.
        - [Installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWFacServMgmnt.md) -- Several types of components are installed with the Facilities Service Management plugin.
          - [Tables installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TableInsWFacServMgmnt.md) -- Facilities Service Management adds the following tables.
          - [Properties installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_PropInstallWFacServMgmnt.md) -- Facilities Service Management Properties controls the behavior of the Facilities Service Management application.
          - [Roles installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_RolesInstallWFacServMgmnt.md) -- Roles control access to features and capabilities in Facilities Service Management.
          - [Script includes installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ScriptInclnstallWFacServMgmnt.md) -- Script includes are used to store JavaScript that runs on the server.
          - [Business rules installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_BRIWFacilitiesServiceManagement.md) -- A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
          - [Email notifications installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EmailNotsInstWithFacServMgmt.md) -- Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Service Management.
          - [Catalogs installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_CatInstallWFacServMgmnt.md) -- Catalogs provide customers with self-service opportunities within Facilities Service Management.
          - [Table transform maps installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TableTransMapInstWFacServMgmnt.md) -- Table transform maps allows you to add spaces or details about spaces from other sources.
      - [Activate Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ActivateFacMoveMgmt.md) -- The (com.snc.facilities_service_automation) and the (com.snc.facilities_service_automation.move) plugins are now deprecated and no longer supported or available for new activation.
        - [Configure Enterprise Move](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ConfigureEnterpriseMove.md) -- Facilities or Move administrators can set configurations to determine how the system displays colors on the move planning tool.
        - [Installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWFacMoveMgmt.md) -- Several types of components are installed with the Facilities Move Management plugin.
          - [Tables installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TblsInstallWFacMoveMgmt.md) -- Facilities Move Management adds the following tables.
          - [Properties installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_PropsInstallWFacMoveMgmt.md) -- Properties control the behavior of the Facilities Move Management application.
          - [Roles installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_RolesInstallWFacMoveMgmt.md) -- Roles control access to features and capabilities in Facilities Move Management.
          - [Email templates installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EmailTemplInstallWFacMoveMgmt.md) -- Email templates allow you to create reusable content for the subject line and message body of email notifications.
          - [Script includes installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ScrptIncludeInstallWFacMoveMgmt.md) -- Script includes are used to store JavaScript that runs on the server.
          - [Client scripts installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_CScriptsInstallWFacMoveMgmt.md) -- Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
          - [Notification email scripts installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_NotifyEmailScriptsInstallWFacMoveMgmt.md) -- Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Move Management.
          - [Business rules installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_BRulesInstallWFacMoveMgmt.md) -- A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
          - [Workflows installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_WrkflwsInstallWFacMoveMgmt.md) -- Workflows provide a drag-and-drop interface for automating multi-step processes.
      - [Activate Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ActivateFacVisWorkbench.md) -- The (com.snc.facilities_service_automation) and the (com.snc.facilities_service_automation.fvw) plugins are now deprecated and no longer supported or available for new activation.
        - [Facilities visualization workbench configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_WorkbenchConfiguration.md) -- Space administrators configure properties on the workbench. In the application navigator, Facilities Workbench Configuration contains the configuration settings divided into sections.
        - [Migrate facilities data to new space definition tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_MigFacDataToNewSpaceDefTable.md) -- To continue using the image-based floor plans with the new space definition, migrate your data from the old tables to the new space definition tables.
        - [Installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWFacVisWorkbench.md) -- Several types of components are installed with the Facilities Visualization Workbench plugin.
          - [Tables installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TableInstallWFacVisWorkbench.md) -- Facilities visualization workbench adds the following tables.
          - [Space Management properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/SpaceMgmntProperties.md) -- Space Management Properties are available to configure floor plan, parsing, and space management defaults settings. You can control default settings like the color for selected space, compass on a floor plan, and logos and titles to appear.
          - [System property categories installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_SysPropCatInstallWFacVisWorkbench.md) -- Facilities visualization workbench adds the following system property categories.
          - [Script includes installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ScriptIncInstallWFacVisWorkbench.md) -- Script includes are used to store JavaScript that runs on the server.
          - [Client scripts installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ClientScrptInstWFac.md) -- Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
          - [Business rules installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_BRIWFaciiltiesVizWorkbench.md) -- A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
          - [Macros installed with Facilities Visualization Workbench](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_MacrosInstallWFacVisWorkbench.md) -- Facilities visualization workbench adds the following macros.
      - [Facilities service management process](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacilitiesSMProcess.md) -- The facilities administrator creates the campus and configures the application with workflow, agent assignment, and other considerations. Employees make facilities and move requests that are tracked to specific locations anywhere on the campus.
        - [Facilities requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacilitiesRequests.md) -- A facilities request is a record in the system that tracks a proposed change to the physical facility of the organization. Typical facilities requests include the reporting of something bring broken or an issue like a beeping smoke alarm.
          - [Facilities request creation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_FacilitiesRequestCreation.md) -- Facilities service management uses the common service management request management process. Any user can submit a facilities request through the Facilities catalog. Users with the facilities_staff role can also create and update facilities requests from the Facilities Request form.
            - [Create a request through the facilities catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateAReqThroughFacCatalog.md) -- Employees use the Facilities catalog to submit requests. The catalog provides several different categories so users can choose the one that closely relates to their request.
            - [Create a request with the facilities request form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateReqWFacRequestForm.md) -- Facilities staff members create requests using the Facilities Request form, allowing them to associate the request with a configuration item (CI), like printers or projectors.
          - [Facilities request approvals](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacilitiesRequestApprovals.md) -- Approving a facilities request means that the request has been reviewed and is ready to be qualified for facilities task creation and assignment. When a request is sent to a user with the facilities_approver_user role, the approver has several choices.
          - [Facilities agent assignment](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_FacilitiesAgentAssignment.md) -- Depending on your settings in the facilities configuration screen, you can assign agents manually or using auto-assignment.
          - [Schedule blackout periods](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_ScheduleBlackout.md) -- A blackout period prevents work from being performed in a defined area for a scheduled time period. Blackout periods can be defined for spaces, levels, buildings, campuses, and zones.
            - [Create a facilities schedule blackout](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateFacScheduleBlackout.md) -- Blackout periods can be defined for spaces, levels, buildings, campuses, and zones. The Facilities_admin can override blackout period requests.
          - [Collaborate on a request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CollaborateOnARequest.md) -- Within a request, you can enter comments that are visible to the submitter, allowing for collaboration between the two of you. For collaboration with other agents, you can enter comments that are not visible to the submitter.
          - [Change the location of a request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ChangeTheLocationOfARequest.md) -- After opening a request, you can modify the details and update it.
          - [Close a request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CloseARequest.md) -- When you close a request, you can add details that you want the submitter to be aware of.
            - [Closed and completed requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_ClosedAndCompletedRequests.md) -- When the Request lifecycle option is set to request-driven, the assigned agent can complete and close the request once all the tasks in the request are complete.
        - [Facilities request tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacRequestTasks.md) -- A facilities request contains one or more tasks. These tasks allow qualifiers to define separate activities that must be done to complete a facilities request.
          - [Create a facilities request task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateAFacilitiesRequestTask.md) -- Facilities request tasks are created from facilities requests.
            - [Task windows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_TaskWindows.md) -- A task window is the time period, bordered by start and end times, in which a task is performed.
          - [Clone a request task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CloneARequestTask.md) -- Existing tasks can be cloned to create tasks with the same populated fields.
          - [Task template for common tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_UseTaskTempForMultReqTemp.md) -- If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.
          - [Auto-dispatch a task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AutoDispatchATask.md) -- When a task is auto-dispatched, the application matches the task with a nearby agent having the necessary skills and schedule that can accommodate the task.
      - [Domain separation and Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/domain-separation-facilities-service-mgt.md) -- Domain separation is supported in Facilities Service Management. Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation, including which users can see and access data.
      - [Space management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_SpaceManagement.md) -- The concept of space is part of the Facilities Service Management application. Space provides a definition at all levels with the same unit measure, and presents metrics that are readily available for analysis. These metrics include occupancy percentage, total space available, and so on.
        - [GeoJSON map files](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_GeoJSONMapFiles.md) -- The floor plan visualization feature uses files in the GeoJSON format, an open standard for representing geographical features.
          - [Community file](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_CommunityFile.md) -- The community file contains information about the campus, including the number of buildings and the number of floors for each building.
            - [Campus information](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_CampusInfo.md) -- Sample code for campus and map set properties.
            - [Building information](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_BuildingInfo.md) -- Each drawing in the campus map file represents a building or campus overview. The campus overview is a map that shows the entire campus, and is included for multi-building campuses only.
            - [Level information](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_LevelInfo.md) -- Each building (drawing) has a list of levels. Each level is a map and represents one floor, though that is not a rule.
          - [Level geometry file](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_LevelFile.md) -- The level geometry file contains all the geometry for a given level. Each file is one map that can be rendered in the ServiceNow platform.
            - [Valid classes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_ValidClasses.md) -- There are certain classes and class types that are valid for the level geometry file.
          - [Process GeoJSON map files](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ProcessMapFiles.md) -- Processing GeoJSON map files includes parsing data from a map and importing that information to the campus space management tables. Use this process to set up your spaces or update bulk changes to your campus without having to enter each change manually.
        - [Customer-created maps](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_Manually-builtMaps.md) -- Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.
          - [Space roll up calculations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_SpaceRollupCalculations.md) -- The Facilities Service Management application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups apply to spaces that are designated as 'occupiable'. The occupancy values from that space are rolled up to the level above them.
          - [Add or edit a campus](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AddOrEditACampus.md) -- A campus represents the top level in the organization space, and contains buildings and map sets. Details include its location, manager, gross area, and usable area. Occupancy and utilization metrics are calculated using these details.
          - [Add or edit a building](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AddOrEditABuilding.md) -- Buildings are assigned to campuses with a unique name, and contain floors or levels, a location, and utilization thresholds.
          - [Add or edit a floor or level](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AddOrEditAFloorOrLevel.md) -- A floor is a level in a structure that contains spaces. It can be a floor of a building, the basement, levels in a parking lot, or outdoor areas.
          - [Add or edit a space](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AddOrEditASpace.md) -- Spaces are assigned to floors or levels, and can be cubicles, conference rooms, restrooms, gymnasiums, elevators, parking spaces, and so on. Spaces are assigned users and assets, and have the most data defined.
          - [Add or edit a zone](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AddOrEditAZone.md) -- Zones are a logical collection of spaces that can be shared across campuses, floors, or buildings. Examples of zones are: Chiller 4 Zone, Guest Wi-Fi Zone, AC 1 Zone, Power Circuit 3 Zone, and so on.
          - [Delete a campus](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_DeleteACampus.md) -- Delete all buildings assigned to a campus, before deleting the campus itself.
          - [Delete a building](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_DeleteABuilding.md) -- Before deleting a building, delete any floors or levels defined for it.
          - [Delete a floor or level](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_DeleteAFloorOrLevel.md) -- Before you can delete a floor, you must first delete any spaces defined for it.
          - [Delete a space](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_DeleteASpace.md) -- Spaces can be deleted from any floor or from another space as long as the space you want to remove does not have other spaces associated with it. For example, if you want to delete a space that contains several offices, those spaces must be deleted before the parent space can be deleted.
          - [Delete a zone](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_DeleteAZone.md) -- When deleting a zone, any associated assets or spaces is also deleted.
        - [Run transform to update data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_RunTransform.md) -- Running a transform exports information from your records into an .xls file. That data can be imported into the ServiceNow space management application.
          - [Transform map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_TransformMap.md) -- A transform map is an .xls file that allows you to add spaces or details about spaces from other sources into the space management application.
      - [Facilities move management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacMoveMgmt.md) -- Employees and managers can request single user moves. Members of the facilities staff can use the enterprise move tool to plan and execute large move scenarios involving multiple people, assets/CIs, and departments.
        - [Facilities move requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacMoveRequests.md) -- Both employees and managers can request a move, which initiates the workflow of tasks to complete that move. Any user can submit a move request through the Facilities catalog. Users with the Facilities staff role can also create and update facilities requests using the move request form directly.
          - [Create a move request through the facilities catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateAMoveReqThruFacCatalog.md) -- Users can submit move requests by selecting from the categories of the Facilities catalog.
          - [Create a move request with the move request form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateMoveReqWFacReqForm.md) -- Facilities staff members can create move requests using the move request form.
        - [Facilities move request templates](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_FacMoveReqTemplates.md) -- The facilities staff adds templates to the facilities catalog, so users can select from subcategories for their request type.
        - [Enterprise move](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_EnterpriseMove.md) -- Facility teams use Enterprise Move to plan and execute move scenarios in support of large or complex employee move requests.
          - [Move planning tool](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_MovePlanningTool.md) -- The Move Planning tool displays occupancy totals by campus and floor. Facilities and move administrators can add or remove users to and from scenarios while planning a move. Groups of people are selected and moved by department (department on sys_user record) or by direct manager (manager on sys_user record).
            - [Enterprise move scenarios](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EnterMoveScenarios.md) -- Move scenarios are used by the Facilities team to see the implications of a move in relation to other moves. Multiple scenarios can be created.
              - [Plan a move scenario](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_PlanScenarioMPT.md) -- Facilities administrators create move scenarios when planning and executing large-scale moves. When people are added to the scenario, move_detail records are created. These records contain all the information about the potential move for a specific person, such as the reference to the sys_user, destination floor, and destination building.
                - [Lounge](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_Lounge.md) -- When a facilities administrator sets up a move scenario without specifying the destination building or floor, the users are moved to the lounge.
              - [Activate a delegator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_ActivateADelegator.md) -- Delegators assign users to seats in a scenario. Activating the delegator sends an email notification request that they assign seats using Move Details.
                - [Move delegators](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_EnterpriseMoveDelegators.md) -- Facilities administrators assign move delegators to assign users to locations.
              - [Assign users to seats](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_AssignSeatsAsADelegator.md) -- Delegators receive an email notification requesting that they assign seats using Move Details.
            - [Enterprise move details](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EnterMoveDetails.md) -- Enterprise move details are created when people are added to the scenario. Move details contain information about the move for a specific person, such the destination floor, destination building, need for moving boxes, or a security badge update.
            - [Enterprise move requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EnterMoveRequests.md) -- Enterprise move requests are managed by a workflow, which contains required approvals from facilities_admin or move_admin. State changes are handled by UI actions.
            - [Enterprise move tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_EnterMoveTasks.md) -- Before a move can be executed, destination locations for all users must be complete. Move tasks are based on check boxes on the request form.
      - [Interactive facility maps](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_InteractiveFacilityMaps.md) -- The interactive facility maps, including the Workbench and the Floor Plan, provide a campus-level hierarchy, improving your facilities request tracking and space management. Decision makers in your organization can track, manage, and analyze spaces in support of organizational needs and users can find other users and assets.
        - [Map filters](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_MapFilters.md) -- Users can filter the map to determine how various spaces are colored.
          - [Simple filters](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_SimpleFilters.md) -- Simple filters are available for the Workbench and the floor plan.
          - [Saved filters](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_SavedFilters.md) -- A saved filter allows advanced filtering when you want to highlight spaces, based on conditions not supported by a simple filter.
          - [Create a map filter in Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/t_CreateAMapFilter.md) -- Create a custom filter to highlight spaces on a map for fast and easy recognition. You can create custom filters for any mappable space (fm_space), asset, associated user, CI, or task with a location defined.
        - [Enhanced labels](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/c_EnhancedLabels.md) -- Enhanced labels allow the end user to show any information on any mappable space (fm_space), as the space label. Users choose to display the occupant name, the department name, or other custom field as the default label.
        - [Map settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_MapSettings.md) -- Map settings allow the facilities staff or users to choose the appearance of thei
```


### File: service-management-for-the-enterprise\open-req-item-age-dashboard.md

```text
---
title: Open Requested Item Age Monitor dashboard
description: Use this dashboard when you wish to dive into open requests for items divided by Age.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Requested Item Age Monitor dashboard

Use this dashboard when you wish to dive into open requests for items divided by Age.

![Open Requested Item Age Monitor dashboard](../image/open-incidents-age-monitor.png)

## Indicators

-   **Number of open requested items**

    Records on the Requested Item \[sc\_req\_item\] table opened on or before today and not closed.

-   **Average age of updated since of open requested items**

    Result of the formula `[[Summed age of updated since of open requested item]] / [[Number of open requested items]] / 24`

-   **Average age of open requested item**

    The result in days of the formula `[[Summed age of open requested item]] / [[Number of open requested items]] / 24`

-   **Average re-assignment of open requested items**

    Result of the formula `[[Summed re-assignment of open requested item]] / [[Number of open requested items]] / 24`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open requested item**

    The aggregate sum of the RequestedItem.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed re-assignment of open requested item**

    The aggregate sum of reassignment counts for open requested items

-   **Summed age of updated since of open requested item**

    The aggregate sum of the results of the script RequestedItem.UpdatedSince.Hours. This script calculates the difference between the latest time stamp of an open request and the last time stamp of an update to that request.


## Breakdowns

-   Age
-   Assignment Group
-   Stage
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\open-req-item-reports-dashboard.md

```text
---
title: Open Requested Item Reports dashboard
description: To view the current state of open item requests, see the Open Requested Item Reports.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Requested Item Reports dashboard

To view the current state of open item requests, see the Open Requested Item Reports.

![Animated tour of the tabs of the Open Requested Item Reports dashboard](../image/open-req-item-reports.gif)

## Data visualizations

<table id="table_xvt_hl4_2fb"><thead><tr><th>

Title

</th><th>

Type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Open requested items - List

</td><td>

List ![list report icon](../../../reuse/reporting/image/score-list-tile.svg)

</td><td>

List of all requests for items that have not been closed

</td></tr><tr><td>

Open requested items - Pivot table

</td><td>

Pivot ![pivot table report icon](../../../reuse/reporting/image/pivot.svg)

</td><td>

Table letting you explore the number of open item requests by any combination of state, assignment group, and priority, for any age bucket or for all ages.

</td></tr><tr><td>

Open requested items - Heatmap

</td><td>

Heatmap ![Heatmap icon](../../performance-analytics/image/heatmap.png)

</td><td>

Heatmap letting you explore the number of open item requests by any combination of state, assignment group, and priority, for any age bucket or for all ages.

</td></tr></tbody>
</table>**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\open-req-item-state-dashboard.md

```text
---
title: Open Requested Item State Monitor dashboard
description: Use this dashboard when you wish to dive into open requests for items divided by State: Pending, Work in Progress, or all Open requests.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Requested Item State Monitor dashboard

Use this dashboard when you wish to dive into open requests for items divided by State: Pending, Work in Progress, or all Open requests.

![Open Requested Item State Monitor reflecting requests in the Pending state](../image/open-req-item-state-monitor.png "Open Requested Item State Monitor focused on Pending requests")

## Indicators

-   **Number of open requested items**

    Records on the Requested Item \[sc\_req\_item\] table opened on or before today and not closed.

-   **Number of open requested item not updated in last 30 days**

    As Number of open requested items, but the Updated value is either empty or from more than 30 days ago.

-   **Number of open requested item not updated in last 5 days**

    As Number of open requested items, but the Updated value is either empty or from more than five days ago.

-   **% of open requested items not updated in last 30 days**

    Result of the formula `( [[Number of open requested items not updated in last 30 days]] / [[Number of open requested items]] ) * 100`

-   **% of open requested items not updated in last 5 days**

    Result of the formula `( [[Number of open requested items not updated in last 5 days]] / [[Number of open requested items]] ) * 100`

-   **Average age of updated since of open requested items**

    Result of the formula `[[Summed age of updated since of open requested item]] / [[Number of open requested items]] / 24`

-   **Average age of open requested item**

    The result in days of the formula `[[Summed age of open requested item]] / [[Number of open requested items]] / 24`

-   **Average re-assignment of open requested items**

    Result of the formula `[[Summed re-assignment of open requested item]] / [[Number of open requested items]] / 24`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open requested item**

    The aggregate sum of the RequestedItem.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed re-assignment of open requested item**

    The aggregate sum of reassignment counts for open requested items

-   **Summed age of updated since of open requested item**

    The aggregate sum of the results of the script RequestedItem.UpdatedSince.Hours. This script calculates the difference between the latest time stamp of an open request and the last time stamp of an update to that request.


## Breakdowns

-   Age
-   Assignment Group
-   Stage
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\open-request-reports-dashboard.md

```text
---
title: Open Request Reports dashboard
description: To view the current state of open requests, see the Open Request Reports.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Request Reports dashboard

To view the current state of open requests, see the Open Request Reports.

![Animated tour of Open Request Reports](../image/open-request-reports.gif)

## Data visualizations

<table id="table_xvt_hl4_2fb"><thead><tr><th>

Title

</th><th>

Type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Open requests - List

</td><td>

List ![list report icon](../../../reuse/reporting/image/score-list-tile.svg)

</td><td>

List of all requests that have not been closed

</td></tr><tr><td>

Open requests - Pivot table

</td><td>

Pivot ![pivot table report icon](../../../reuse/reporting/image/pivot.svg)

</td><td>

Table letting you explore the number of open requests by any combination of state, assignment group, and priority, for any age bucket or for all ages.

</td></tr><tr><td>

Open requests - Heatmap

</td><td>

Heatmap ![Heatmap icon](../../performance-analytics/image/heatmap.png)

</td><td>

Heatmap letting you explore the number of open requests by any combination of state, assignment group, and priority, for any age bucket or for all ages.

</td></tr></tbody>
</table>**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\open-requests-age-dashboard.md

```text
---
title: Open Requests Age Monitor dashboard
description: Use this dashboard when you wish to dive into open requests divided by Age.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Requests Age Monitor dashboard

Use this dashboard when you wish to dive into open requests divided by Age.

![Open request age monitor showing the 0-1 day bucket](../image/open-req-age-monitor.png)

## Indicators

-   **Number of open requests**

    Records on the Request \[sc\_req\_item\] table opened on or before today and not closed.

-   **Average age of updated since of open requests**

    Result of the formula `[[Summed age of updated since of open request]] / [[Number of open requests]] / 24`

-   **Average age of open request**

    The result in days of the formula `[[Summed age of open request]] / [[Number of open requests]] / 24`

-   **Average re-assignment of open requests**

    Result of the formula `[[Summed re-assignment of open request]] / [[Number of open requests]] / 24`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open request**

    The aggregate sum of the Requests.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed re-assignment of open request**

    The aggregate sum of reassignment counts for open requests

-   **Summed age of updated since of open request**

    The aggregate sum of the results of the script Requests.UpdatedSince.Hours. This script calculates the difference between the last update of an open request \(sys\_updated\_on\) and the last second of yesterday \(score\_end\) and returns negative value if sys\_updated\_on is after score\_end.


## Breakdowns

-   Age
-   Assignment Group
-   Priority
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\open-requests-state-dashboard.md

```text
---
title: Open Requests State Monitor dashboard
description: Use this dashboard when you wish to dive into open requests divided by State: Pending Approval or Approved.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Open Requests State Monitor dashboard

Use this dashboard when you wish to dive into open requests divided by State: Pending Approval or Approved.

![Open Requests State Monitor dashboard](../image/open-req-state-monitor.png)

## Indicators

-   **Number of open requests**

    Records on the Request \[sc\_req\_item\] table opened on or before today and not closed.

-   **Number of open request not updated in last 30 days**

    As Number of open requests, but the Updated value is either empty or from more than 30 days ago.

-   **Number of open request not updated in last 5 days**

    As Number of open requests, but the Updated value is either empty or from more than five days ago.

-   **% of open requests not updated in last 30 days**

    Result of the formula `( [[Number of open requests not updated in last 30 days]] / [[Number of open requests]] ) * 100`

-   **% of open requests not updated in last 5 days**

    Result of the formula `( [[Number of open requests not updated in last 5 days]] / [[Number of open requests]] ) * 100`

-   **Average age of updated since of open requests**

    Result of the formula `[[Summed age of updated since of open request]] / [[Number of open requests]] / 24`

-   **Average age of open requests**

    The result in days of the formula `[[Summed age of open request]] / [[Number of open requests]] / 24`

-   **Average re-assignment of open requests**

    Result of the formula `[[Summed re-assignment of open request]] / [[Number of open requests]] / 24`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open requests**

    The aggregate sum of the Requests.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed re-assignment of open requests**

    The aggregate sum of reassignment counts for open requests

-   **Summed age of updated since of open requests**

    The aggregate sum of the results of the script Requests.UpdatedSince.Hours. This script calculates the difference between the latest time stamp of an open request and the last time stamp of an update to that request.


## Breakdowns

-   Age
-   Assignment Group
-   Priority
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\r_ActivateOtherSMApplications.md

```text
---
title: Activate other Service Management applications
description: After the Service Management Core plugin has been activated, you can activate other SM applications, such as Field Service management and facilities service management. You can also activate CMS portals for each of these SM applications to add them to the Service Management Portal.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Activate Service Management, Service Management]
---

# Activate other Service Management applications

After the Service Management Core plugin has been activated, you can activate other SM applications, such as Field Service management and facilities service management. You can also activate CMS portals for each of these SM applications to add them to the Service Management Portal.

<table id="table_lnh_kp3_br"><thead><tr><th>

Plugin

</th><th>

ID

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Facilities Service Management

</td><td>

com.snc.facilities.core

</td><td>

Manages facilities requests and enables users to report and track requests by their location on a floor plan. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

 Facilities Service Management is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported until deprecation. Workplace Service Delivery provides the latest experience for this functionality. For details, see the [KB0867184 Deprecation Process](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867184) article in the Now Support knowledge base.

</td></tr><tr><td>

Facilities Service Management CMS Portal

</td><td>

com.snc.facilities.core.cms

</td><td>

Displays the Facilities Service Automation SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr><tr><td>

Field Service Management

</td><td>

com.snc.work\_management

</td><td>

Provides support for scheduling and managing on location work.

</td></tr><tr><td>

Field Service Management CMS Portal

</td><td>

com.snc.work\_management.cms

</td><td>

Displays the Work Management SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr><tr><td>

Finance Service Management

</td><td>

com.snc.finance\_service\_automation

</td><td>

Deprecated Feb 1, 2023.

</td></tr><tr><td>

Finance Service Management CMS Portal

</td><td>

com.snc.finance\_service\_automation.cms

</td><td>

Displays the Finance Service Automation SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr><tr><td>

HR Service Delivery: Core

</td><td>

com.snc.hr.core

</td><td>

Provides a basic data and security model for HR systems.

</td></tr><tr><td>

HR Service Delivery: Core CMS Portal

</td><td>

com.snc.hr.core.cms

</td><td>

Displays the Human Resources Service Automation SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr><tr><td>

Legal Service Management

</td><td>

com.snc.legal\_service\_automation

</td><td>

Deprecated Feb 1, 2023.

</td></tr><tr><td>

Legal Service Management CMS Portal

</td><td>

com.snc.legal\_service\_automation.cms

</td><td>

Displays the Legal Service Automation SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr><tr><td>

Marketing Service Management

</td><td>

com.snc.marketing\_service\_automation

</td><td>

Deprecated Feb 1, 2023.

</td></tr><tr><td>

Marketing Service Management CMS Portal

</td><td>

com.snc.marketing\_service\_automation.cms

</td><td>

Displays the Marketing Service Automation SM application on the Service Management portal. Activation of this plugin on production instances may require a separate license. Contact ServiceNow for details.

</td></tr></tbody>
</table>**Parent Topic:**[Activate Service Management](../task/t_ActivateServiceManagement.md)


```


### File: service-management-for-the-enterprise\r_BRIWFaciiltiesVizWorkbench.md

```text
---
title: Business rules installed with Facilities Visualization Workbench
description: A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Business rules installed with Facilities Visualization Workbench

A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.

Facilities visualization workbench adds the following business rules.

<table id="table_ngl_zwx_dt"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Update default campus

</td><td>

Campus\[fm\_campus\]

</td><td>

Ensures one default campus

</td></tr><tr><td>

Prevent duplicates

</td><td>

Facility Map Option\[fm\_map\_option\]

</td><td>

Prevents duplicate map options

</td></tr><tr><td>

Max search results per campus &lt; 50

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the maximum search results to less than 50

</td></tr><tr><td>

Max spaces per zone &lt; 1000

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the number of spaces per zone to 1000

</td></tr><tr><td>

Build Scratchpad

</td><td>

Facilities Map Filter\[fm\_map\_filter\]

</td><td>

Provides a list of tables that are extended from fm\_spaces. Used by the Hide field for space tables client script.

</td></tr><tr><td>

Prevent duplicates

</td><td>

Facility Map Color\[fm\_map\_color\]

</td><td>

Prevents duplicate map colors

</td></tr><tr><td>

Prevent duplicates

</td><td>

Facility Map Task Option\[fm\_map\_task\]

</td><td>

Prevents duplicate map task options

</td></tr><tr><td>

Facility map highlight color validation

</td><td>

System Property\[sys\_properties\]

</td><td>

Validates the highlight colors on the floor plan map

</td></tr><tr><td>

Facility map color validation

</td><td>

Facility Map Color\[fm\_map\_color\]

</td><td>

Validates the colors on the floor plan map

</td></tr><tr><td>

Max facilities/move search results&lt; 5000

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the maximum facilities move search results to less than 5000

</td></tr><tr><td>

Prevent duplicate

</td><td>

Facility Feature\[fm\_facility\_feature\]

</td><td>

Prevents duplicate facility features

</td></tr><tr><td>

Create spaces requires default class

</td><td>

Facility Feature\[fm\_facility\_feature\]

</td><td>

Prevents empty class by default on a space

</td></tr><tr><td>

Facility map outline color validation

</td><td>

System Property\[sys\_properties\]

</td><td>

Validates the outline colors on the floor plan map

</td></tr><tr><td>

Max requests per level should be &lt; 5000

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the number of requests per level to 5000

</td></tr><tr><td>

Prevent duplicate

</td><td>

Facility Icon\[fm\_icon\]

</td><td>

Prevents duplicate facility icons

</td></tr><tr><td>

Max search results for other campuses

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the maximum search results for other campuses

</td></tr><tr><td>

Max search results per level &lt; 50

</td><td>

System Property\[sys\_properties\]

</td><td>

Limits the maximum search results per level to less than 50

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_BRIWFacilitiesServiceManagement.md

```text
---
title: Business rules installed with Facilities Service Management
description: A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Business rules installed with Facilities Service Management

A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.

Facilities Service Management adds the following business rules.

<table id="table_ngl_zwx_dt"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Building Utilization

</td><td>

Building\[alm\_building\]

</td><td>

Ensures that utilization thresholds are set to numbers from 0 through 100.

</td></tr><tr><td>

Update User Primary Location

</td><td>

Associated User\[fm\_m2m\_user\_to\_space\]

</td><td>

Updates the sys user records location to the current primary location for the user in the fm\_m2m\_user\_to\_space table.

</td></tr><tr><td>

Reference Area

</td><td>

Facility Space\[fm\_space\]

</td><td>

Calculates the area in common units for the space.

</td></tr><tr><td>

Prevent ancestry loop

</td><td>

Facility Space\[fm\_space\]

</td><td>

Prevents circular space definitions where a space is both a parent and child at the same time.

</td></tr><tr><td>

Rollup

</td><td>

Facility Space\[fm\_space\]

</td><td>

Rolls up the space information to level as info is changed on the space.

</td></tr><tr><td>

Rollup

</td><td>

Level\[fm\_level\]

</td><td>

Rolls up level information to the building.

</td></tr><tr><td>

Floor Utilization

</td><td>

Level\[fm\_level\]

</td><td>

Ensures that utilization thresholds are set to numbers from 0 through 100.

</td></tr><tr><td>

Rollup

</td><td>

Associated User\[fm\_m2m\_user\_to\_space\]

</td><td>

Updates the space utilization on a space as users are added and removed from spaces.

</td></tr><tr><td>

Reference area

</td><td>

Campus\[fm\_campus\]

</td><td>

Calculates the area in common units for the space.

</td></tr><tr><td>

update space display name

</td><td>

Building\[alm\_building\]

</td><td>

Generates the full display name for the space.

</td></tr><tr><td>

Max Occupancy

</td><td>

Building\[alm\_building\]

</td><td>

Max occupancy cannot be less than 0.

</td></tr><tr><td>

Rollup

</td><td>

Building\[alm\_building\]

</td><td>

Rolls up building data to the campus.

</td></tr><tr><td>

Request Autoclose

</td><td>

Facilities Request\[facilities\_request\]

</td><td>

Automatically closes requests that are resolved and have not been updated in the 1 day. This number is a property in System Properties.

</td></tr><tr><td>

Facilities Primary Location Change

</td><td>

User\[sys\_user\]

</td><td>

Updates the fm\_m2m\_user\_to\_space table when the location on the sys\_user records changes.

</td></tr><tr><td>

Max Occupancy

</td><td>

Facility Space\[fm\_space\]

</td><td>

Max occupancy cannot be less than 0.

</td></tr><tr><td>

Prevent duplicates

</td><td>

Facility Zone \[fm\_zone\]

</td><td>

Do not allow the same space to be added to a single zone more than once.

</td></tr><tr><td>

Prevent duplicates

</td><td>

Associated User\[fm\_m2m\_user\_to\_space\]

</td><td>

Do not allow the same user to be added to the same space more than once.

</td></tr><tr><td>

Prevent multiple main level for building

</td><td>

Level\[fm\_level\]

</td><td>

Do not allow there to be more than one main level set for levels in a building.

</td></tr><tr><td>

Update primary location

</td><td>

Associated User\[fm\_m2m\_user\_to\_space\]

</td><td>

Helps keep the sys user and fm\_m2m\_users\_to\_space tables in synchronization when primary location changes.

</td></tr><tr><td>

Facilities area unit option changed

</td><td>

Facility Space\[fm\_space\]

</td><td>

Converts\` square feet to square meters

</td></tr><tr><td>

update space display name

</td><td>

Level\[fm\_level\]

</td><td>

Updates display name as building and level name changes

</td></tr><tr><td>

Reference Area

</td><td>

Facility Space\[fm\_space\]

</td><td>

Calculates the area in common units for the spaces.

</td></tr><tr><td>

Max Occupancy

</td><td>

Facility Space\[fm\_space\]

</td><td>

Max occupancy cannot be less than 0.

</td></tr><tr><td>

Reference Area

</td><td>

Facility Space\[fm\_space\]

</td><td>

Calculates the area in common units for the space.

</td></tr><tr><td>

Space - generate full name

</td><td>

Facility Space\[fm\_space\]

</td><td>

Generates the full display name for the space.

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_BRulesInstallWFacMoveMgmt.md

```text
---
title: Business rules installed with Facilities Move Management
description: A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Business rules installed with Facilities Move Management

A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.

Facilities Move Management adds the following business rules.

<table id="table_ngl_zwx_dt"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Force Workflow Update

</td><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Forces workflow to trigger on close

</td></tr><tr><td>

Move to/from Facility Spaces only

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Only allows facility space \(fm\_space\) as to or from location

</td></tr><tr><td>

Pending Assignment - Update Task State

</td><td>

Move Task\[move\_task\]

</td><td>

Sets state to pending assignment

</td></tr><tr><td>

Set request to WIP

</td><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Set request to work in progress when a task is started

</td></tr><tr><td>

Keep request scenario reference in synch

</td><td>

Enterprise Move Scenario\[enterprise\_move\_scenario\]

</td><td>

Update scenario on enterprise move request

</td></tr><tr><td>

Move Catalog out of draft

</td><td>

Move Request\[move\_request\]

</td><td>

If the request was created through the facilities catalog, set the state to **Ready**

</td></tr><tr><td>

Move users and assets

</td><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Update user and asset location

</td></tr><tr><td>

Set Requested by user

</td><td>

Move Request\[move\_request\]

</td><td>

Set caller and requested by user

</td></tr><tr><td>

Enforce Building when floor is populated

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Prevent the selection of a building that does not contain a floor

</td></tr><tr><td>

Set Building when floor is populated

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Set the building when one of its floors are selected

</td></tr><tr><td>

Do not remove scenario from move request

</td><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

Maintain the scenario with the move request

</td></tr><tr><td>

Trigger workflow on update

</td><td>

Move Task\[move\_task\]

</td><td>

Force workflow to start

</td></tr><tr><td>

Prevent non-space to\_location

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Ensure the **to location** is a facilities space \(fm\_space\)

</td></tr><tr><td>

Prevent Duplicates

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Do not allow the same move detail record to be added more than once

</td></tr><tr><td>

Set Move Request

</td><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Set the parent request

</td></tr><tr><td>

Check for open tasks

</td><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

Prevent a request from being closed when tasks are still open

</td></tr><tr><td>

Autopopulate Move Delegator

</td><td>

Enterprise Move Delegator\[move\_delegator\]

</td><td>

Set the delegator

</td></tr><tr><td>

Add messaging

</td><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

Add help messaging on the move request

</td></tr><tr><td>

Uncheck task options

</td><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

 

</td></tr><tr><td>

Set Assigned

</td><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Set the state to Assigned when Assigned to is not empty and State is Pending Assignment

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_BuildingInfo.md

```text
---
title: Building information
description: Each drawing in the campus map file represents a building or campus overview. The campus overview is a map that shows the entire campus, and is included for multi-building campuses only.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Community file, GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Building information

Each drawing in the campus map file represents a building or campus overview. The campus overview is a map that shows the entire campus, and is included for multi-building campuses only.

```
{
            "id": 28500,
            "levels": [
 
           . . . . . . . . . . . <See level section>>
 
            ],
            "obj_type": "Drawing",
            "properties": {
                "display_name": "SD Campus Building 1",
                "map_type": "Shopping Mall",
                "name": "San Diego Campus Building 1"
            },
            "ref_frame": {
                "angle_deg": -16.554,
                "height": 782.891,
                "local2m": 0.05893868944676606,
                "transform": [
                    6.043292819573627e-07,
                    1.508500607965198e-07,
                    1.7962840831123188e-07,
                    -5.075094178111973e-07,
                    -117.206364,
                    32.882096
                ],
                "width": 1505.19
            }
        },
```

-   This information is used to create a building in alm\_building.
-   The `id` is mapped to the external building id in alm\_building.
-   The `display_name` is used to name the building.
-   The `ref frame` is used to align the building horizontally and vertically. The GeoJSON data, contains WGS 84 information used to rotate the image so it displays at a natural horizontal orientation.

**Parent Topic:**[Community file](r_CommunityFile.md)


```


### File: service-management-for-the-enterprise\r_CScriptsInstallWFacMoveMgmt.md

```text
---
title: Client scripts installed with Facilities Move Management
description: Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Client scripts installed with Facilities Move Management

Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.

Facilities Move Management adds the following client scripts.

<table id="table_wtf_krf_2t"><thead><tr><th>

Client script

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Remove bad date

</td><td>

Move Request\[move\_request\]

</td><td>

Remove default date

</td></tr><tr><td>

Autopopulate from\_location

</td><td>

Move Request\[move\_request\]

</td><td>

Auto-populate the from\_location based on the selected User to be moved.

</td></tr><tr><td>

Autopopulate From on embedded list

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Populate from location when a user is added

</td></tr><tr><td>

State is read only

</td><td>

Move Request\[move\_request\]

</td><td>

Set state to read only when state is Draft or Submitted

</td></tr><tr><td>

Warn to\_location not a Facility Space

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Warn the user that the **to location** is not a facility space \(fm\_space\)

</td></tr><tr><td>

Asset update

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Update assets for the user in a move

</td></tr><tr><td>

Close Complete Check

</td><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

Check that all tasks are closed complete before setting request state

</td></tr><tr><td>

Autopopulate from location

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Populate from location when a user is added

</td></tr><tr><td>

hide submit

</td><td>

Move Request\[move\_request\]

</td><td>

Hide submit button when needed

</td></tr><tr><td>

Lock down form when request approved

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Prevent changes to the request after tasks are created

</td></tr><tr><td>

Info message

</td><td>

Move Request\[move\_request\]

</td><td>

Add an info message when state is Ready

</td></tr><tr><td>

Remove extra buttons on Workbench

</td><td>

Enterprise Move Scenario\[enterprise\_move\_scenario\]

</td><td>

Remove the extra buttons \(various icons, and so on\) while in a modal

</td></tr><tr><td>

Warn from\_location not a Facility Space

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Warn the user when the selected **from location** is a cmn\_location and not a facility space \(fm\_space\)

</td></tr><tr><td>

Warn from\_location not a Facility Space

</td><td>

Move Request\[move\_request\]

</td><td>

Warn the user when the selected **from location** is a cmn\_location and not a facility space \(fm\_space\)

</td></tr><tr><td>

Remove bad date2

</td><td>

Move Request\[move\_request\]

</td><td>

Remove default date

</td></tr><tr><td>

Set Building and Floor

</td><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Automatically sets the destination building and floor when the **to location** is selected

</td></tr><tr><td>

Warn to\_location not a Facility Space

</td><td>

Move Request\[move\_request\]

</td><td>

Warn the user that the selected **from location** is a \(cmn\_location\)

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_CampusInfo.md

```text
---
title: Campus information
description: Sample code for campus and map set properties.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Community file, GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Campus information

Sample code for campus and map set properties.

```
"entity_version": 1,
    "id": 23641,
    "languages": [
        "en"
    ],
    "location": {
        "coordinates": [
            -117.20527,
            32.882205
        ],
        "type": "Point"
    },
    "map_version": 1,
    "obj_type": "CommunityMap",
    "properties": {
        "city": "San Diego",
        "com_type": "Business Campus",
        "country": "US",
        "default_lang": "en",
        "name": "ServiceNow - San Diego Campus",
        "postal code": "92121",
        "state": "CA",
        "street address": "4810 Eastgate Mall"
    }
```

-   The `id` is a unique id for this campus and is mapped to the database as the **external campus id** field in the campus table.

-   The `entity_version` and `map_version` are the versions of the map sets, helpful when a campus has multiple map sets.
-   The `location` contains WGS 84 coordinates providing the overall latitude and longitude of the campus.

    **Note:** Latitude and Longitude are set at the Campus level only.

-   Other data provides the name and address of the campus and is used to create a location in the location table for the campus.

**Parent Topic:**[Community file](r_CommunityFile.md)


```


### File: service-management-for-the-enterprise\r_CatInstallWFacServMgmnt.md

```text
---
title: Catalogs installed with Facilities Service Management
description: Catalogs provide customers with self-service opportunities within Facilities Service Management.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Catalogs installed with Facilities Service Management

Catalogs provide customers with self-service opportunities within Facilities Service Management.

Facilities Service Management adds the following catalogs.

|Table|Description|
|-----|-----------|
|Facilities Catalog|Contains facilities catalog items|

**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_ClientScrptInstWFac.md

```text
---
title: Client scripts installed with Facilities Visualization Workbench
description: Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Client scripts installed with Facilities Visualization Workbench

Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.

Facilities visualization workbench adds the following client scripts.

|Client script|Description|
|-------------|-----------|
|Reload form on attachment window|Reload the external map data form every time the attachment window closes to hide or display the process map file UI action.|
|Hide field for space tables|Show or hide the "field" field when the "table" field value is an extension of "cmn\_location" or not.|

**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_CommunityFile.md

```text
---
title: Community file
description: The community file contains information about the campus, including the number of buildings and the number of floors for each building.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Community file

The community file contains information about the campus, including the number of buildings and the number of floors for each building.

The file naming standard is:

-   Must begin with `map`
-   Must contain `-geojson-com-map-`

For example, `map-23641-mv-1-ev-1-geojson-com-map-fv-2.json`

-   **[Campus information](r_CampusInfo.md)**  
Sample code for campus and map set properties.
-   **[Building information](r_BuildingInfo.md)**  
Each drawing in the campus map file represents a building or campus overview. The campus overview is a map that shows the entire campus, and is included for multi-building campuses only.
-   **[Level information](r_LevelInfo.md)**  
Each building \(drawing\) has a list of levels. Each level is a map and represents one floor, though that is not a rule.

**Parent Topic:**[GeoJSON map files](r_GeoJSONMapFiles.md)


```


### File: service-management-for-the-enterprise\r_EmailNotsInstWithFacServMgmt.md

```text
---
title: Email notifications installed with Facilities Service Management
description: Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Service Management.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Email notifications installed with Facilities Service Management

Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Service Management.

Facilities Service Management adds the following email notifications.

|Notification|Description|
|------------|-----------|
|Facilities Request is assigned|Sends an email message to the facilities staff member who is assigned to the facilities request.|

**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_EmailTemplInstallWFacMoveMgmt.md

```text
---
title: Email templates installed with Facilities Move Management
description: Email templates allow you to create reusable content for the subject line and message body of email notifications.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Email templates installed with Facilities Move Management

Email templates allow you to create reusable content for the subject line and message body of email notifications.

Facilities Move Management adds the following email templates.

|Email templates|Description|
|---------------|-----------|
|move.del|Notifies delegators to assign seats for an enterprise move.|

**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_EnterMoveDetails.md

```text
---
title: Enterprise move details
description: Enterprise move details are created when people are added to the scenario. Move details contain information about the move for a specific person, such the destination floor, destination building, need for moving boxes, or a security badge update.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enterprise move details

Enterprise move details are created when people are added to the scenario. Move details contain information about the move for a specific person, such the destination floor, destination building, need for moving boxes, or a security badge update.

Duplicate details are not allowed \(same user, scenario, and from\_location\). The same move detail can be in multiple scenarios. Updates can be made to move details from the list or form view.

![In this figure, the Enterprise Move Scenario record is open with the Move Details shown in a related list.](../image/MoveDetailsTab.png "Enterprise Move Scenario with Move Details")

**Parent Topic:**[Move planning tool](../concept/c_MovePlanningTool.md)


```


### File: service-management-for-the-enterprise\r_EnterMoveRequests.md

```text
---
title: Enterprise move requests
description: Enterprise move requests are managed by a workflow, which contains required approvals from facilities\_admin or move\_admin. State changes are handled by UI actions.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enterprise move requests

Enterprise move requests are managed by a workflow, which contains required approvals from facilities\_admin or move\_admin. State changes are handled by UI actions.

**Parent Topic:**[Move planning tool](../concept/c_MovePlanningTool.md)


```


### File: service-management-for-the-enterprise\r_EnterMoveScenarios.md

```text
---
title: Enterprise move scenarios
description: Move scenarios are used by the Facilities team to see the implications of a move in relation to other moves. Multiple scenarios can be created.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enterprise move scenarios

Move scenarios are used by the Facilities team to see the implications of a move in relation to other moves. Multiple scenarios can be created.

Predictive availability considers planned seating changes for the selected scenario \(on or off current level\).

-   **[Plan a move scenario](../task/t_PlanScenarioMPT.md)**  
Facilities administrators create move scenarios when planning and executing large-scale moves. When people are added to the scenario, move\_detail records are created. These records contain all the information about the potential move for a specific person, such as the reference to the sys\_user, destination floor, and destination building.
-   **[Activate a delegator](../task/t_ActivateADelegator.md)**  
Delegators assign users to seats in a scenario. Activating the delegator sends an email notification request that they assign seats using Move Details.
-   **[Assign users to seats](../task/t_AssignSeatsAsADelegator.md)**  
Delegators receive an email notification requesting that they assign seats using Move Details.

**Parent Topic:**[Move planning tool](../concept/c_MovePlanningTool.md)


```


### File: service-management-for-the-enterprise\r_EnterMoveTasks.md

```text
---
title: Enterprise move tasks
description: Before a move can be executed, destination locations for all users must be complete. Move tasks are based on check boxes on the request form.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Enterprise move tasks

Before a move can be executed, destination locations for all users must be complete. Move tasks are based on check boxes on the request form.

-   One task per type:
    -   Move users and assets
    -   Update security badge
-   Groups or waves of users can be moved at a time. Useful if the move will be executed over a period of time with different groups moving at different times.
-   One per user moving. Useful for tracking actual users moves in detail.
-   When the user move task is closed, the location of the users and their assets are updated.

**Parent Topic:**[Move planning tool](../concept/c_MovePlanningTool.md)


```


### File: service-management-for-the-enterprise\r_FacilitiesAgentAssignment.md

```text
---
title: Facilities agent assignment
description: Depending on your settings in the facilities configuration screen, you can assign agents manually or using auto-assignment.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities agent assignment

Depending on your settings in the facilities configuration screen, you can assign agents manually or using auto-assignment.

If you have a limited number of agents for completing requests or you simply do not want to auto-assign agents, you can use manual assignment.

Auto-assignment allows you to define criteria by which agents can be automatically selected to satisfy requests entered in service management applications. Based on the needs of your organization, you can configure the criteria for agent auto-assignment in the following ways.

When auto-assignment is enabled and a task is qualified or marked as **Ready for Work**, the following actions occur:

-   Available agents are evaluated based on the criteria defined in the configuration.
-   An appropriate agent is automatically assigned to the task.
-   The task is moved to the **Assigned** state.

If more than one set of criteria is considered, such as location and skills, the agents are evaluated on the weighting property settings and other criteria.

If the task cannot be auto-assigned, a user with the dispatcher role adjusts the values in the request or task form and saves the record.

**Parent Topic:**[Facilities requests](../concept/c_FacilitiesRequests.md)

**Related topics**  


[Agent assignment methods](../../service-management-core/concept/c_AgentAssignment.md)


```


### File: service-management-for-the-enterprise\r_FacilitiesRequestCreation.md

```text
---
title: Facilities request creation
description: Facilities service management uses the common service management request management process. Any user can submit a facilities request through the Facilities catalog. Users with the facilities\_staff role can also create and update facilities requests from the Facilities Request form.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities request creation

Facilities service management uses the common service management request management process. Any user can submit a facilities request through the Facilities catalog. Users with the facilities\_staff role can also create and update facilities requests from the Facilities Request form.

-   **[Create a request through the facilities catalog](../task/t_CreateAReqThroughFacCatalog.md)**  
Employees use the Facilities catalog to submit requests. The catalog provides several different categories so users can choose the one that closely relates to their request.
-   **[Create a request with the facilities request form](../task/t_CreateReqWFacRequestForm.md)**  
Facilities staff members create requests using the Facilities Request form, allowing them to associate the request with a configuration item \(CI\), like printers or projectors.

**Parent Topic:**[Facilities requests](../concept/c_FacilitiesRequests.md)


```


### File: service-management-for-the-enterprise\r_GeoJSONMapFiles.md

```text
---
title: GeoJSON map files
description: The floor plan visualization feature uses files in the GeoJSON format, an open standard for representing geographical features.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# GeoJSON map files

The floor plan visualization feature uses files in the GeoJSON format, an open standard for representing geographical features.

Due to the complexity of each file, work with Micello, Inc. or some other vendor to create the floor plan for your organization.

**Note:** However, creating a floor plan requires GeoJSON knowledge. Ensure that you are familiar with geospatial data and/or GeoJSON data before attempting this task.

For information about the GeoJSON standard, see [http://geojson.org](http://geojson.org). Object properties in the GeoJSON files are used to create buildings, floors, and spaces.

When cloning an instance, sys\_attachments including GeoJSON maps are not cloned by default. See the **Exclude large attachment data field** in [Request a clone](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_StartAClone.md) .

**Note:** As an option, you can download the GeoJSON maps from the source tables \(fm\_map\_set and fm\_map\_set\_tranformed\) and upload to the destination.

-   **[Community file](r_CommunityFile.md)**  
The community file contains information about the campus, including the number of buildings and the number of floors for each building.
-   **[Level geometry file](r_LevelFile.md)**  
The level geometry file contains all the geometry for a given level. Each file is one map that can be rendered in the ServiceNow platform.
-   **[Process GeoJSON map files](../task/t_ProcessMapFiles.md)**  
Processing GeoJSON map files includes parsing data from a map and importing that information to the campus space management tables. Use this process to set up your spaces or update bulk changes to your campus without having to enter each change manually.

**Parent Topic:**[Space management](r_SpaceManagement.md)


```


### File: service-management-for-the-enterprise\r_InstallWFacMoveMgmt.md

```text
---
title: Installed with Facilities Move Management
description: Several types of components are installed with the Facilities Move Management plugin.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Installed with Facilities Move Management

Several types of components are installed with the Facilities Move Management plugin.

Demo data is available with Facilities Move Management.

-   **[Tables installed with Facilities Move Management](r_TblsInstallWFacMoveMgmt.md)**  
Facilities Move Management adds the following tables.
-   **[Properties installed with Facilities Move Management](r_PropsInstallWFacMoveMgmt.md)**  
Properties control the behavior of the Facilities Move Management application.
-   **[Roles installed with Facilities Move Management](r_RolesInstallWFacMoveMgmt.md)**  
Roles control access to features and capabilities in Facilities Move Management.
-   **[Email templates installed with Facilities Move Management](r_EmailTemplInstallWFacMoveMgmt.md)**  
Email templates allow you to create reusable content for the subject line and message body of email notifications.
-   **[Script includes installed with Facilities Move Management](r_ScrptIncludeInstallWFacMoveMgmt.md)**  
Script includes are used to store JavaScript that runs on the server.
-   **[Client scripts installed with Facilities Move Management](r_CScriptsInstallWFacMoveMgmt.md)**  
Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
-   **[Notification email scripts installed with Facilities Move Management](r_NotifyEmailScriptsInstallWFacMoveMgmt.md)**  
Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Move Management.
-   **[Business rules installed with Facilities Move Management](r_BRulesInstallWFacMoveMgmt.md)**  
A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
-   **[Workflows installed with Facilities Move Management](r_WrkflwsInstallWFacMoveMgmt.md)**  
Workflows provide a drag-and-drop interface for automating multi-step processes.

**Parent Topic:**[Activate Facilities Move Management](../task/t_ActivateFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_InstallWFacServMgmnt.md

```text
---
title: Installed with Facilities Service Management
description: Several types of components are installed with the Facilities Service Management plugin.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Installed with Facilities Service Management

Several types of components are installed with the Facilities Service Management plugin.

Demo data is available with Facilities Service Management.

-   **[Tables installed with Facilities Service Management](r_TableInsWFacServMgmnt.md)**  
Facilities Service Management adds the following tables.
-   **[Properties installed with Facilities Service Management](r_PropInstallWFacServMgmnt.md)**  
Facilities Service Management Properties controls the behavior of the Facilities Service Management application.
-   **[Roles installed with Facilities Service Management](r_RolesInstallWFacServMgmnt.md)**  
Roles control access to features and capabilities in Facilities Service Management.
-   **[Script includes installed with Facilities Service Management](r_ScriptInclnstallWFacServMgmnt.md)**  
Script includes are used to store JavaScript that runs on the server.
-   **[Business rules installed with Facilities Service Management](r_BRIWFacilitiesServiceManagement.md)**  
A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
-   **[Email notifications installed with Facilities Service Management](r_EmailNotsInstWithFacServMgmt.md)**  
Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Service Management.
-   **[Catalogs installed with Facilities Service Management](r_CatInstallWFacServMgmnt.md)**  
Catalogs provide customers with self-service opportunities within Facilities Service Management.
-   **[Table transform maps installed with Facilities Service Management](r_TableTransMapInstWFacServMgmnt.md)**  
Table transform maps allows you to add spaces or details about spaces from other sources.

**Parent Topic:**[Activate Facilities Service Management](../task/t_ActivateFacilitiesSM.md)


```


### File: service-management-for-the-enterprise\r_InstallWFacVisWorkbench.md

```text
---
title: Installed with Facilities Visualization Workbench
description: Several types of components are installed with the Facilities Visualization Workbench plugin.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Installed with Facilities Visualization Workbench

Several types of components are installed with the Facilities Visualization Workbench plugin.

Demo data is available with Facilities Visualization Workbench.

-   **[Tables installed with Facilities Visualization Workbench](r_TableInstallWFacVisWorkbench.md)**  
Facilities visualization workbench adds the following tables.
-   **[Space Management properties](../../facilities-service-management/reference/SpaceMgmntProperties.md)**  
Space Management Properties are available to configure floor plan, parsing, and space management defaults settings. You can control default settings like the color for selected space, compass on a floor plan, and logos and titles to appear.
-   **[System property categories installed with Facilities Visualization Workbench](r_SysPropCatInstallWFacVisWorkbench.md)**  
Facilities visualization workbench adds the following system property categories.
-   **[Script includes installed with Facilities Visualization Workbench](r_ScriptIncInstallWFacVisWorkbench.md)**  
Script includes are used to store JavaScript that runs on the server.
-   **[Client scripts installed with Facilities Visualization Workbench](r_ClientScrptInstWFac.md)**  
Client scripts define custom behaviors that run when events occur like when a form is loaded or submitted, or a cell changes value.
-   **[Business rules installed with Facilities Visualization Workbench](r_BRIWFaciiltiesVizWorkbench.md)**  
A business rule is a server-side script that runs when a record is displayed, inserted, updated, deleted, or when a table is queried.
-   **[Macros installed with Facilities Visualization Workbench](r_MacrosInstallWFacVisWorkbench.md)**  
Facilities visualization workbench adds the following macros.

**Parent Topic:**[Activate Facilities Visualization Workbench](../task/t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_InstallWServMgmtCore.md

```text
---
title: Installed with Service Management Core
description: Several types of components are installed with the Service Management Core plugin.Tables are added with Service Management Core.Properties are added with Service Management Core.Roles are added with Service Management Core.Script includes are added with Service Management Core.Client scripts are added with Service Management Core.Business rules are added with Service Management Core.Email notifications are added with Service Management Core.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 23
breadcrumb: [Service Management Core installation reference, Service Management]
---

# Installed with Service Management Core

Several types of components are installed with the Service Management Core plugin.

Demo data is available with Service Management Core.

**Parent Topic:**[Service Management Core installation reference](r_ServMgmtCoreInstallRef.md)

## Tables installed with Service Management Core

Tables are added with Service Management Core.

<table id="table_u5j_fry_dt"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Part Requirement\[cmdb\_model\_part\_requirement\]

</td><td>

Defines a relationship between a service order task an an asset \(part\) required to complete this task.

</td></tr><tr><td>

Service Order Model\[cmdb\_serviceorder\_product\_model\]

</td><td>

Stores service order templates.

</td></tr><tr><td>

Service Task Model\[cmdb\_servicetask\_product\_model\]

</td><td>

Stores service task templates.

</td></tr><tr><td>

Service Management Flow \[sf\_state\_flow\]

</td><td>

State flows for Service Management.

</td></tr><tr><td>

Service Order Flow \[sf\_sm\_order\]

</td><td>

State flows for service orders.

</td></tr><tr><td>

Service Task Flow \[sf\_sm\_task\]

</td><td>

State flows for service order tasks.

</td></tr><tr><td>

Asset Usage \[sm\_asset\_usage\]

</td><td>

Defines relationship between a service order task and the assets used to complete this task.

</td></tr><tr><td>

SM Category\[sm\_category\]

</td><td>

Links a single service order template to a service order category value.

</td></tr><tr><td>

SM Config Module \[sm\_config\_module\]

</td><td>

Links a configuration to a set of navigation modules that are shown or hidden based on configuration settings.

</td></tr><tr><td>

SM Config\[sm\_config\]

</td><td>

Service management application configuration.

</td></tr><tr><td>

Service Management Incidentals\[sm\_incidentals\]

</td><td>

Incidental items used to complete a service order task.

</td></tr><tr><td>

Service Order Groups Dependency\[sm\_m2m\_group\_dependency\]

</td><td>

Dispatch groups that handle scheduling for assignment groups.

</td></tr><tr><td>

SM Model Application\[sm\_m2m\_model\_application\]

</td><td>

Links SM applications to hardware and consumable models often used in part sourcing.

</td></tr><tr><td>

SM Model Knowledge\[sm\_m2m\_model\_knowledge\]

</td><td>

Relates any knowledge page to any model.

</td></tr><tr><td>

Affected CI \[sm\_m2m\_order\_affected\_ci\]

</td><td>

Configuration items related to a service order.

</td></tr><tr><td>

Service Order Task Models\[sm\_m2m\_somodel\_stmodel\]

</td><td>

Links service task models to service order models.

</td></tr><tr><td>

Task Affected CI \[sm\_m2m\_task\_affected\_ci\]

</td><td>

Configuration items related to a service order task.

</td></tr><tr><td>

Service Order Task Contract\[sm\_m2m\_task\_contract\]

</td><td>

Defines a relationship between a task and contract.

</td></tr><tr><td>

Service Order Task Dependency\[sm\_m2m\_task\_dependency\]

</td><td>

Defines a dependency between two service order tasks: downstream task cannot be started before upstream task gets completed.

</td></tr><tr><td>

Service Order Task Template Dependency\[sm\_m2m\_task\_template\_dependency\]

</td><td>

Defines a dependency between two service order task templates: downstream task cannot be started before upstream task gets completed.

</td></tr><tr><td>

SM Notification Rule \[sm\_notification\_rule\]

</td><td>

Service management notification rules.

</td></tr><tr><td>

Service Order \[sm\_order\]

</td><td>

Defines and manages work that needs to be performed.

</td></tr><tr><td>

Part Requirement \[sm\_part\_requirement\]

</td><td>

Defines a relationship between a service order task and an asset \(part\) required to complete this task.

</td></tr><tr><td>

Service Task \[sm\_task\]

</td><td>

Unit of work performed by one person in one session \(one location, one time\).

</td></tr><tr><td>

SM Template Definition\[sm\_template\_definition\]

</td><td>

Defines a field and value that will be included in a service order template.

</td></tr><tr><td>

Task Asset \[task\_asset\]

</td><td>

Assets related to a task.

</td></tr></tbody>
</table>## Properties installed with Service Management Core

Properties are added with Service Management Core.

|Property|Description|
|--------|-----------|
|Properties for service management core|
|sm.template.minute.step|Default minute step for date time or time fields on service order template page. Can be overridden for a specific application by replacing "sm.template" with the appropriate property prefix. See application configuration record.|
|sm.template.hour.step|Default hour step for date time or time fields on service order template page. Can be overridden for a specific application by replacing "sm.template" with the appropriate property prefix. See application configuration record.|
|glide.autodispatch.debug|Whether auto dispatch engine should output logs when assigning tasks.|

## Roles installed with Service Management Core

Roles are added with Service Management Core.

|Role title \[name\]|Description|
|-------------------|-----------|
|personalize\_read\_dictionary|Role allowing service management application admins the ability to see fields when modifying field controls \(for example, mandatory fields, read-only fields\) on the state flow form.|
|sm\_qualifier|Qualifier role used when creating SM applications. This role is a template only and it does not provide actual access to any navigation modules or records.|
|sm\_agent|Agent role used when creating SM applications. Performs work on a task. This role is a template only and it does not provide actual access to any navigation modules or records.|
|sm\_approver\_user|Approver user role used when creating SM application. Approves requests. This role is a template only and it does not provide actual access to any navigation modules or records|
|sm\_initiator|Initiator user role used when creating SM application. Grants UI access, as well as performing the same functions as Basic. This role is a template only and it does not provide actual access to any navigation modules or records.|
|service\_fulfiller|Role allowing service management users the ability to see the Service Desk modules.|
|sm\_admin|Admin user role used when creating SM application. Controls all data. This role is a template only and it does not provide actual access to any navigation modules or records|
|sm\_basic|Basic user role used when creating SM application. Reads and creates requests, and follows up on those requests. This role is a template only and it does not provide actual access to any navigation modules or records.|
|sm\_dispatcher|Dispatcher user role used when creating SM application. Schedules and assigns tasks to agents. This role is a template only and it does not provide actual access to any navigation modules or record.|
|sm\_read|Read-only user role used when creating SM application. This role is a template only and it does not provide actual access to any navigation modules or records.|
|template\_admin|Grants the ability to create and administer Service Management templates.|

## Script includes installed with Service Management Core

Script includes are added with Service Management Core.

|Script includes|Description|
|---------------|-----------|
|PartRequirementStateHandler|Marks a part requirement Sourced or Delivered based on the transfer orders.|
|SMTemplates|Builds a service order and related tasks from an SM Template.|
|SMAutoAssignment|Javascript wrapper around SNC.SMAutoassignment that automatically determines property prefix needed.|
|SMStockRooms|Retrieves and creates personal stockrooms.|
|BaseSMControls|Provides functions used to control access to service management records like the configuration and notification rules. Modify the SMControls Script Include to make changes rather than modifying this Script Include.|
|SMConfigProcessor|Handles changes that are made to the configuration page. Also handles sending notifications set up on the configuration page.|
|SMTemplateHelper|Backend-code for the SM Template page. Should not be customized.|
|AppCreatorCMSCreation|Creates CMS pages for apps created by Service Management template.|
|SMDateRollup|Rolls up the dates from service order tasks to service orders.|
|SMI18nUtils|Utilities for internationalizing the Service Management and Configuration Pages.|
|SMAJAX|Handles Service management AJAX calls.|
|AJAXMileageCalculator|Calculates mileage costs for incidentals.|
|SMCIControls|Service Management CI controls for adding and removing CI's from Orders and Tasks.|
|SharedServiceUtils|Shared Service Utilities|
|SMSourcingDispatch|Contains methods supporting the Agent Schedule section in the lower portion of the Source popup.|
|SMStateFlowCreator|Methods for creating state flows for ESM-based applications.|
|SMAgentStatusAJAX|AJAX wrapper around the updateStatus function available in SMScheduleStatus.|
|SMDateValidation|Verifies that dates in service order tasks are valid and consistent with one another in terms of scheduling.|
|SMTask|Service Management Task utility functions.|
|AppCreatorKnowledgeCreation|Methods for "app creator" engine to create knowledgebase pages.|
|SMAgentStatus|Code for updating the "on schedule" and status of an agent.|
|SMAppCreator|Methods for creating Service management applications.|
|SMScheduleGrapper|Schedule APIs. Gets schedule times from a work order task in milliseconds. Actual times are given priority, if those are not available, return scheduled times.|
|SMTableCreator|Methods for creating tables for Service management applications|
|SMControls|Extension of BaseSMControls. Modify this script for controlling access to service management records like the configuration and notification rules|
|AssetUsageFilters|Reference qualifier filters for AssetUsage.|
|SMTaskDependency|Collection of methods that control the data integrity of the Service Order Tasks Dependency \[sm\_m2m\_task\_dependency\] table.|
|AppCreatorCatalogCreation|Creates an SM application catalog.|
|SMAssetUsage|Asset Usage APIs|
|SMConstants|List of constants used in the State field of the Service Management \(SM\) flows \(sm\_order and sm\_task\) and extended tables \(for example, wm\_order, wm\_task\).|
|SMNotifRuleTables|Restricts tables that are displayed on the SM Notification Rule form to the request and task table of the application.|
|SMTransferOrders|Collection of methods that create or update service management-related transfer order lines.|
|SMPortalCreator|Methods for creating a portal and reports for SM-based applications.|
|WMSourcingAjax|AJAX calls used in the "Source" popup available from Work Orders and Work Order Tasks. Contains methods for displaying work order tasks and part requirements in the tree-section \(left-hand side\), deleting and copying part requirements using the tree, and retrieving task information and agent information for the lower section.|
|SMFilters|Filters for service management.|
|SMUpgradeManager|Handles finding SM application items that need upgrades, storing information, upgrading.|
|SMTemplateMigration|Handles migrating SM templates from previous version of Geneva.|

## Client script includes installed with Service Management Core

Client scripts are added with Service Management Core.

<table id="table_wtf_krf_2t"><thead><tr><th>

Client script includes

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Hide excluded fields

</td><td>

SM Config\[sm\_config\]

</td><td>

Hide sm\_config fields based on exclusion list.

</td></tr><tr><td>

Start work read-only \(exp. travel chg\)

</td><td>

Service order task \[sm\_task\]

</td><td>

Start work read-only when travel is required and not started.

</td></tr><tr><td>

Start work read-only when travel is required and not started

</td><td>

Service order task \[sm\_task\]

</td><td>

Displays an error after a location change when no dispatch group or assignment group covers the location of the work order task.

</td></tr><tr><td>

Show or hide/clear contract field

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

If type is Vendor cost, then show the contract field. Otherwise, clear and hide the contract field.

</td></tr><tr><td>

check order of start date and end date

</td><td>

Service order task \[sm\_task\]

</td><td>

Verify that the start date happens before the end date.

</td></tr><tr><td>

Update Assigned to \(Assign Group change\)

</td><td>

Service order \[sm\_order\]

</td><td>

Update Assigned to when Assignment group changes: - clear the Assigned to field.

</td></tr><tr><td>

Ci update

</td><td>

Service order \[sm\_order\]

</td><td>

Updates the associated asset and location based on changes to the affected CI.

</td></tr><tr><td>

Populate CI Location

</td><td>

Service order \[sm\_order\]

</td><td>

Populates work order location based on CI location.

</td></tr><tr><td>

check\_work\_duration

</td><td>

Service order task \[sm\_task\]

</td><td>

Verify that the work duration is not 0 or empty.

</td></tr><tr><td>

Calculate total amount - quantity

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Calculates the total mileage costs when the quantity changes.

</td></tr><tr><td>

Validate Estimated Travel Duration

</td><td>

Service order task \[sm\_task\]

</td><td>

Ensure that the estimated travel duration does not carry into the expected start time.

</td></tr><tr><td>

Validate Scheduled Travel Start

</td><td>

Service order task\[sm\_task\]

</td><td>

Ensure that the scheduled travel start \(with its duration\) is before scheduled work start.

</td></tr><tr><td>

Template selected

</td><td>

Service order \[sm\_order\]

</td><td>

Populates form based on template values.

</td></tr><tr><td>

Populate Caller Location

</td><td>

Service order \[sm\_order\]

</td><td>

Sets the location field when the caller is changed.

</td></tr><tr><td>

Check for group errors

</td><td>

Service order \[sm\_order\]

</td><td>

Displays an error on load if no qualification group covers the location of the work order.

</td></tr><tr><td>

Hide unused related lists/fields

</td><td>

Service order \[sm\_order\]

</td><td>

Hides related lists that are not relevant based on application configuration

</td></tr><tr><td>

Ci update

</td><td>

Service order task \[sm\_task\]

</td><td>

Updates the associated asset and location based on changes to the affected CI.

</td></tr><tr><td>

New fields type control

</td><td>

SM Template Definition\[sm\_template\_definition\]

</td><td>

Displays the appropriate field type based on selection of field on template definition page.

</td></tr><tr><td>

Asset update

</td><td>

Service order \[sm\_order\]\[sm\_order\]

</td><td>

Updates the associated configuration item and location based on changes to the affected asset.

</td></tr><tr><td>

Field onload helper

</td><td>

SM Template Definition \[sm\_template\_definition\]

</td><td>

Displays the appropriate field type based on selection of field on template definition page \(onload\).

</td></tr><tr><td>

Read only task templates dependencies

</td><td>

Service Order Task Template Dependency \[sm\_m2m\_task\_template\_dependency\]

</td><td>

Makes the dependent field read only when creating task template dependencies in sm\_m2m\_task\_template\_dependencies table.

</td></tr><tr><td>

Make Location not mandatory

</td><td>

Stockroom \[alm\_stockroom\]

</td><td>

Makes Location not mandatory for stockroom type field\_agent

</td></tr><tr><td>

Calculate End Time \(Duration change\)

</td><td>

Service order task\[sm\_task\]

</td><td>

Calculates Estimated End Time in a Work Order Task based on a change of estimated work duration.

</td></tr><tr><td>

Show error when no application installed

</td><td>

Service Order Model \[cmdb\_serviceorder\_product\_model\]

</td><td>

Show error when no application installed.

</td></tr><tr><td>

Calculate total amount - cost per mile

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Calculates the total mileage costs when the quantity changes.

</td></tr><tr><td>

Priority assignment

</td><td>

SM Config \[sm\_config\]

</td><td>

Set scheduling to true and hide consistent assignment of priority assignment is turned on.

</td></tr><tr><td>

Asset update

</td><td>

Service order task \[sm\_task\]

</td><td>

Updates the associated configuration item and location based on changes to the affected asset.

</td></tr><tr><td>

Read only group dependencies

</td><td>

Service Order Group Dependency \[sm\_m2m\_group\_dependency\]

</td><td>

Once set, fields are read-only.

</td></tr><tr><td>

Add sourcing UI Listeners

</td><td>

Service order task\[sm\_task\]

</td><td>

Sets up event listeners for changes to travel duration, work duration, or expected work start so that they are automatically updated in the sourcing UI \(if the task is opened via the sourcing UI\).

</td></tr><tr><td>

check window\_start

</td><td>

Service order task \[sm\_task\]

</td><td>

Verify that window start is before window end.

</td></tr><tr><td>

Set required quantity read-only

</td><td>

Part Requirement \[sm\_part\_requirement\]

</td><td>

Sets the Required quantity field to read-only when the required number of assets are sourced for the part requirement

</td></tr><tr><td>

Show messages

</td><td>

Service order task \[sm\_task\]

</td><td>

Shows messages if the expected due date for the task is after the requested due date of the request, or if auto-assignment does not work.

</td></tr><tr><td>

Calculate total amount - type

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Calculates the total mileage costs when the type changes.

</td></tr><tr><td>

Update Assigned to \(Assign Group change\)

</td><td>

Service order task \[sm\_task\]

</td><td>

Update Assigned to when Assignment group changes: - clear the Assigned to field.

</td></tr><tr><td>

Hide group field

</td><td>

Service Task Model\[cmdb\_servicetask\_product\_model\]

</td><td>

Hides the dispatch group field when dispatch queue is off

</td></tr><tr><td>

Hide state flow field

</td><td>

SM Config \[sm\_config\]

</td><td>

When state flow is turned off, hide the field from the form.

</td></tr><tr><td>

Check TOs before reassigning

</td><td>

Service order task \[sm\_task\]

</td><td>

When reassigning or unassigning a work order task, prompt user to cancel all transfer orders to personal stock rooms for a task if the task only has cancelable transfer orders.

</td></tr><tr><td>

Verify Group Post Dispatch Group Change

</td><td>

Service order task\[sm\_task\]

</td><td>

Displays an error on load if no assignment group covers the location of the work order task.

</td></tr><tr><td>

Set Tables

</td><td>

SM Notification Rule \[sm\_notification\_rule\]

</td><td>

Limit the tables to the two possible tables, if none is chosen, set the first one as the default.

</td></tr><tr><td>

Calculate End Time \(Start time change\)

</td><td>

Service order task \[sm\_task\]

</td><td>

Calculate the Estimated End Time based on Expected Start Time changing. Also checks for inconsistencies that may have been created with estimated travel start.

</td></tr><tr><td>

Update Model and Quantity based on Asset

</td><td>

Asset Usage\[sm\_asset\_usage\]

</td><td>

Synchronizes model and quantity information of an asset usage record based on the asset it references.

</td></tr><tr><td>

Read Only Order Affected Cis

</td><td>

Affected CI\[sm\_m2m\_order\_affected\_ci\]

</td><td>

Makes a field read only once a value is selected for that field.

</td></tr><tr><td>

Reset quantity

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

When the type changes back to car rental, the Qty is set back to 1.

</td></tr><tr><td>

Read Only Task Affected CIs

</td><td>

Task Affected CI\[sm\_m2m\_task\_affected\_ci\]

</td><td>

Makes a field read only once a value is selected for that field.

</td></tr><tr><td>

Hide group field

</td><td>

Service Order Model \[cmdb\_serviceorder\_product\_model\]

</td><td>

Hide the assignment group field if application is not request driven, hide the qualification group field if qualification is off.

</td></tr><tr><td>

Check TOs before reassigning

</td><td>

Service order task \[sm\_task\]

</td><td>

When reassigning or unassigning a work order task, prompt user to cancel all transfer orders to personal stock rooms for a task if the task only has cancelable transfer orders.

</td></tr><tr><td>

Notify parent on submit

</td><td>

Part Requirement \[sm\_part\_requirement\]

</td><td>

Updates the Source tree whenever a new part requirement is created inside the Source popup window.

</td></tr><tr><td>

Show warning msg of templates upgrade

</td><td>

SM Config \[sm\_config\]

</td><td>

Show warning message when the templates must be migrated.

</td></tr><tr><td>

Verify Group Fields

</td><td>

Service order task\[sm\_task\]

</td><td>

Displays an error on load if no dispatch group or assignment group covers the location of the work order task.

</td></tr><tr><td>

Ensure no negative and decimal quantity

</td><td>

Part Requirement\[sm\_part\_requirement\]

</td><td>

Ensures the quantity required for a part is valid.

</td></tr><tr><td>

Read only task dependencies

</td><td>

Service Order Task Dependency \[sm\_m2m\_task\_dependency\]

</td><td>

Making the dependent field read only on creating task dependencies in sm\_m2m\_task\_order table.

</td></tr><tr><td>

Start work read-only \(actual travel chg\)

</td><td>

Service order task \[sm\_task\]

</td><td>

Start work read-only when travel is required and not started. 'Schedule travel start' and 'Schedule start' are mandatory when 'Agent Track Time' is on.

</td></tr><tr><td>

Show warning message of disable SF

</td><td>

SM Config \[sm\_config\]

</td><td>

Shows a warning message when state flows are disabled.

</td></tr><tr><td>

Populate from stockroom for drop off

</td><td>

Transfer Order \[alm\_transfer\_order\]

</td><td>

Sets the from stock room to the logged in user's personal stockroom when creating a drop off transfer order.

</td></tr><tr><td>

Set value before submit

</td><td>

SM Template Definition\[sm\_template\_definition\]

</td><td>

Sets the value from the various widgets to the appropriate value before submitting the template definition form.

</td></tr><tr><td>

Template selected

</td><td>

Service order task \[sm\_task\]

</td><td>

Populates form based on template values.

</td></tr><tr><td>

Personal Stockroom Name by Type

</td><td>

Stockroom \[alm\_stockroom\]

</td><td>

Sets the name of a stockroom based on its manager when it becomes a personal stockroom.

</td></tr><tr><td>

Update agent status

</td><td>

Service order task \[sm\_task\]

</td><td>

Update the status of assigned agent.

</td></tr><tr><td>

Update UI on load and model change

</td><td>

Asset Usage \[sm\_asset\_usage\]

</td><td>

Update UI on load and model change

</td></tr><tr><td>

Personal Stockroom Name by Manager

</td><td>

Stockroom \[alm\_stockroom\]

</td><td>

Updates the name of a personal stockroom when its manager changes.

</td></tr><tr><td>

Hide unused related lists/fields

</td><td>

Service order task \[sm\_task\]

</td><td>

Hides related lists that are not relevant based on application configuration.

</td></tr><tr><td>

use schedule

</td><td>

SM Config \[sm\_config\]

</td><td>

Turn off priority assignment and show consistent assignment if scheduling is turned off.

</td></tr><tr><td>

Verify Group Post Location Change

</td><td>

Service order \[sm\_order\]\[alm\_stockroom\]

</td><td>

Displays an error after a location change when no qualification group covers the location of the work order.

</td></tr></tbody>
</table>## Business rules installed with Service Management Core

Business rules are added with Service Management Core.

<table id="table_ngl_zwx_dt"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Build scratchpad &amp; display info messages

</td><td>

Service order task \[sm\_task\]

</td><td>

Build scratchpad variables that are used to display initial info messages on page.

</td></tr><tr><td>

Affected CI changed or removed

</td><td>

Service Order \[sm\_order\]

</td><td>

Synchronizes the primary CI field and the Affected CIs related list on the Service Order form.

</td></tr><tr><td>

Verify Work Notes

</td><td>

Service Order \[sm\_order\]

</td><td>

Ensures that the Work notes field is populated in work orders that transition to the Cancel state.

</td></tr><tr><td>

Set default values

</td><td>

SM Template Definition\[sm\_template\_definition\]

</td><td>

Sets the **table** field by default.

</td></tr><tr><td>

Set Personal Stockroom

</td><td>

Transfer Order \[alm\_transfer\_order\]

</td><td>

Automatically sets the stockroom to the personal stockroom of the logged in user for drop-off transfer orders.

</td></tr><tr><td>

Export to update set

</td><td>

Part Requirement \[cmdb\_model\_part\_requirement\]

</td><td>

Exports part requirement templates to the current update set and creates a sys\_metadata\_link record to associate template with current application.

</td></tr><tr><td>

Export to update set

</td><td>

Service Order Task Models \[sm\_m2m\_somodel\_stmodell\]

</td><td>

Exports link between service order template and service task template to the current update set and creates a sys\_metadata\_link record to associate template with current application.

</td></tr><tr><td>

Export to update set

</td><td>

Service Order Task Template\[cmdb\_servicetask\_product\_model\]

</td><td>

Exports service task templates to the current update set and creates a sys\_metadata\_link record to associate template with current application.

</td></tr><tr><td>

Export to update set

</td><td>

Service Order Template\[cmdb\_serviceorder\_product\_model\]

</td><td>

Exports service order templates to the current update set and creates a sys\_metadata\_link record to associate template with current application.

</td></tr><tr><td>

Sync update of associated variables

</td><td>

SM Template Definition \[sm\_template\_definition\]

</td><td>

Synchronizes template definition with associated catalog variable.

</td></tr><tr><td>

Date Checks

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Validates the window, estimated, and actual start and end dates.

</td></tr><tr><td>

Populate Location - New SOT

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Populates the location, if possible, based on parent work order location.

</td></tr><tr><td>

add\_model\_filter

</td><td>

Global \[global\]

</td><td>

Filter for SM Model Application slush bucket, limits available models to hardware and consumable models.

</td></tr><tr><td>

Reset qty to 1

</td><td>

Service Management Incidentals\[sm\_incidentals\]

</td><td>

Sets the quantity field to 1 when the type is Car Rental.

</td></tr><tr><td>

Validate notification

</td><td>

SM Notification Rule\[sm\_notification\_rule\]

</td><td>

Validates that a user or group is selected when inserting or updating a notification rule.

</td></tr><tr><td>

Validate Field Agent Type

</td><td>

Stockroom \[alm\_stockroom\]

</td><td>

Prevents duplicate personal stockrooms.

</td></tr><tr><td>

Calculate cost

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Helps to calculate the **Cost**when the **Type** is **Mileage** \(starting with the Eureka release\).

</td></tr><tr><td>

Check asset and CI

</td><td>

Service order task \[sm\_task\]

</td><td>

Synchronizes affected Cis and affected assets.

</td></tr><tr><td>

Assign the previous agent on task

</td><td>

Service order task \[sm\_task\]

</td><td>

Sets the previous agent whenever the task assigned to changes.

</td></tr><tr><td>

Populate Service Order from Template

</td><td>

Service Order \[sm\_order\]

</td><td>

Populates a new work order from the work order model selected as a template.

</td></tr><tr><td>

Validate quantity requested

</td><td>

Transfer Order Line \[alm\_transfer\_order\_line\]

</td><td>

Checks that the quantity requested on a transfer order line with a part requirement does not exceed the quantity that is required to fulfill the part requirement \(starting with the Eureka release\).

</td></tr><tr><td>

Close service order on workflow complete

</td><td>

Workflow contexts \[wf\_context\]

</td><td>

Prevents rollup of task closures when there are active workflows on service orders.

</td></tr><tr><td>

Create Sub Tasks

</td><td>

Service Order \[sm\_order\]

</td><td>

When service order leaves draft state, creates tasks from template if service order built from template, or creates default task if task-driven.

</td></tr><tr><td>

Validate Field Agent Name

</td><td>

Stockroom \[alm\_stockroom\]

</td><td>

Validates that a personal stockroom has a valid, associated agent.

</td></tr><tr><td>

Create expense line

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Creates or updates an expense line based on the incidental's cost when the incidental is saved and all of the following are true: -   The state is Incurred

 -   The type is not None

 -   The cost is not zero

</td></tr><tr><td>

Validation

</td><td>

Service Order Groups Dependency \[sm\_m2m\_group\_dependency\]

</td><td>

Validates that the dependency is valid.

</td></tr><tr><td>

Verify CI on SM Task

</td><td>

Cis Affected \[task\_ci\]

</td><td>

Verifies that the affected CI for a task is also an affected CI for the order.

</td></tr><tr><td>

Vendor type requires manager

</td><td>

User Group \[sys\_user\_group\]

</td><td>

Vendor is required for vendor groups.

</td></tr><tr><td>

Part Requirements

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Creates part requirements for a service order task from the part requirements configured for a service order task model used as a template. Free up assets when unassigned or reassigned. Update asset usages when tasks are closed.

</td></tr><tr><td>

Apply dispatch method

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Automatically assigns a task once it is marked as ready for assignment when assignment method of the application is workflow or auto.

</td></tr><tr><td>

Group change validation

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Validates changes to assignment and dispatch groups in work order tasks.

</td></tr><tr><td>

Assign the previous agent on order

</td><td>

Service Order \[sm\_order\]

</td><td>

Sets the previous agent whenever the order assigned to changes.

</td></tr><tr><td>

ValidateChanges

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Validates dispatch group and assignment group types match and that worknotes are provided if required.

</td></tr><tr><td>

Transitions

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Sets a task into work in progress when the task is accepted and work start is populated.

</td></tr><tr><td>

Sync catalog

</td><td>

SM Config \[sm\_config\]

</td><td>

Synchronizes the application catalog when the service management configuration changes.

</td></tr><tr><td>

Set required by date on display

</td><td>

Part Requirement\[sm\_part\_requirement\]

</td><td>

Sets part requirement required by to the expected travel start of the associate service order task.

</td></tr><tr><td>

Request driven dispatch

</td><td>

Service Order \[sm\_order\]

</td><td>

Responsible for dispatching service orders based on application configuration.

</td></tr><tr><td>

Build scratchpad &amp; display info messages

</td><td>

Service Order \[sm\_order\]

</td><td>

Build scratchpad variables that are used to display initial info messages on page.

</td></tr><tr><td>

Prevent Loop In TaskTemplateDependencies

</td><td>

Service Order Task Template Dependency \[sm\_m2m\_task\_template\_dependency\]

</td><td>

Prevents loops in task template dependencies

</td></tr><tr><td>

getMainSMModels

</td><td>

Global\[global\]

</td><td>

Slush bucket filter when linking service order task templates to service order templates.

</td></tr><tr><td>

Task contract m2m

</td><td>

Service Management Incidentals \[sm\_incidentals\]

</td><td>

Synchronizes contracts, expense lines, and incidentals

</td></tr><tr><td>

Notification for task

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Sends notifications when task changes if values change for fields specified in the configuration page.

</td></tr><tr><td>

Build scratchpad tables

</td><td>

SM Notification Rule\[sm\_notification\_rule\]

</td><td>

Sets the tables that should be displayed on notification rule page.

</td></tr><tr><td>

Update PR based on TOL

</td><td>

Transfer Order Line\[alm\_transfer\_order\_line\]

</td><td>

Updates the part requirement when the associated transfer order line changes stage.

</td></tr><tr><td>

Add removed asset

</td><td>

Asset Usage \[sm\_asset\_usage\]

</td><td>

Determines validity of asset removal and updates the removed asset accordingly.

</td></tr><tr><td>

Add/remove manager to/from vendor group

</td><td>

Group \[sys\_user\_group\]

</td><td>

When group manager changes for a vendor group, add the new manager as a group member and remove the previous manager as a group member.

</td></tr><tr><td>

Service Management Group Types

</td><td>

Group \[sys\_user\_group\]

</td><td>

Ensures data integrity for dispatch group coverage information.

</td></tr><tr><td>

Deletion of Affected CI

</td><td>

Cis Affected \[task\_ci\]

</td><td>

Part of the synchronization mechanism between the primary CI field and the Affected CIs related list on the Service Order form.

</td></tr><tr><td>

Prevent Loop In Tasks Dependencies

</td><td>

Service Order Task Dependency \[sm\_m2m\_task\_dependency\]

</td><td>

Prevents circular work order task dependencies.

</td></tr><tr><td>

Cascade SO deletion

</td><td>

Service Order \[sm\_order\]

</td><td>

Delete service order tasks and checklists when service order is deleted.

</td></tr><tr><td>

Create Personal Stockroom

</td><td>

User Role \[sys\_user\_has\_role\]

</td><td>

Creates a personal stockroom for users \(if they do not have one already\) when they are assigned an agent role.

</td></tr><tr><td>

Delete Personal Stockroom

</td><td>

User Role\[sys\_user\_has\_role\]

</td><td>

Deletes a user's personal stockroom when all agent roles are removed from the user.

</td></tr><tr><td>

Validate Part Requirement

</td><td>

Part Requirement\[sm\_part\_requirement\]

</td><td>

Validates the part requirement and checks for availability of the part. Validates sourcing information.

</td></tr><tr><td>

Invoke template workflow &amp; move task

</td><td>

Service Order \[sm\_order\]

</td><td>

Start workflow for service order and move subtasks to pending dispatch.

</td></tr><tr><td>

Populate Group - Qualification

</td><td>

Service Order \[sm\_order\]

</td><td>

Populates the qualification group, if possible, based on location.

</td></tr><tr><td>

Create catalog

</td><td>

Service Order Template\[cmdb\_serviceorder\_product\_model\]

</td><td>

Create a corresponding record producer if automatic publishing is on.

</td></tr><tr><td>

Populate schedule

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Populates scheduling fields if they are not already set. They are set, only if the state changes to Pending Dispatch.

</td></tr><tr><td>

Notification for request

</td><td>

Service Order \[sm\_order\]

</td><td>

Sends notifications when task changes if values change for fields specified in the configuration page.

</td></tr><tr><td>

Cascade delete checklist

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Delete checklists when service order task is deleted.

</td></tr><tr><td>

Scratchpad

</td><td>

SM Config\[sm\_config\]

</td><td>

Builds scratchpad for SM config form.

</td></tr><tr><td>

Validate TOL and check availability

</td><td>

Transfer Order Line\[alm\_transfer\_order\_line\]

</td><td>

Validates transfer order line state changes and ensures that the asset is available in the stockroom.

</td></tr><tr><td>

Delete all expense lines

</td><td>

SM Incidentals\[sm\_incidentals\]

</td><td>

Delete expense lines when incidentals are deleted.

</td></tr><tr><td>

Populate Schedule - New SOT

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Populates scheduling fields if they are not already set. They are set only if the state changes to Pending Dispatch.

</td></tr><tr><td>

Populate Location

</td><td>

Service Order \[sm\_order\]

</td><td>

Populates the location, if possible, based on the affected CI identified by the caller.

</td></tr><tr><td>

Add as Primary if none set

</td><td>

Cis Affected \[task\_ci\]

</td><td>

Add configuration item as primary affected CI if no primary CI exists.

</td></tr><tr><td>

Roll Up Changes

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Rollup state changes and estimated work times to service order.

</td></tr><tr><td>

Build scratchpad

</td><td>

Service Order Template\[cmdb\_serviceorder\_product\_model\]

</td><td>

Sets scratchpad for service order template form.

</td></tr><tr><td>

Check asset and CI

</td><td>

Service order \[sm\_order\]

</td><td>

Synchronizes affected Cis and affected assets.

</td></tr><tr><td>

Unassigned

</td><td>

Service order \[sm\_order\]

</td><td>

Sets state of service order back to ready when it becomes unassigned.

</td></tr><tr><td>

Propagate priority

</td><td>

Service order \[sm\_order\]

</td><td>

Propagates priority from service order to service order tasks.

</td></tr><tr><td>

Apply configuration settings

</td><td>

SM Config \[sm\_config\]

</td><td>

Handles changes to SM Config record.

</td></tr><tr><td>

Update agent status

</td><td>

Service Order Task \[sm\_task\]

</td><td>

Updates the status of an agent assigned to a task.

</td></tr><tr><td>

Build scratchpad

</td><td>

Service Order Task Template\[cmdb\_servicetask\_product\_model\]

</td><td>

Sets scratchpad for service order task template form.

</td></tr><tr><td>

Check TOs before reassigning

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Sets scratchpad to prevent reassigning a task when there are transfer orders in transit.

</td></tr><tr><td>

Prevent Duplicate Order Affected CIs

</td><td>

Cis Affected \[task\_ci\]

</td><td>

Prevent duplicated affected Cis

</td></tr><tr><td>

Unassigned

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Prevent reassigning a task if there are transfer orders in transit.

</td></tr><tr><td>

SNC - Run parent workflows \(Approval\)

</td><td>

Approval \[sysapproval\_approver\]

</td><td>

Handles order workflows when approval set to "More info required" or "Duplicate".

</td></tr><tr><td>

getTaskSMModels

</td><td>

Global \[global\]

</td><td>

Slush bucket filter when linking service order templates to service task templates.

</td></tr><tr><td>

Prevent model change after sourced

</td><td>

Part Requirement\[sm\_part\_requirement\]

</td><td>

Prevent changing the model after the part requirement is sourced.

</td></tr><tr><td>

Create AssetUsage when TOL delivered

</td><td>

Transfer Order Line\[alm\_transfer\_order\_line\]

</td><td>

Create asset usage once a transfer order line is delivered.

</td></tr><tr><td>

Release Asset on AssetUsage delete

</td><td>

Asset Usage \[sm\_asset\_usage\]

</td><td>

Make asset available when asset usage is deleted.

</td></tr><tr><td>

Redirect TOL to existing TO under WOT

</td><td>

Transfer Order Line\[alm\_transfer\_order\_line\]

</td><td>

Attempts to group transfer order lines under the same transfer order for a service order if the transfer order lines have the same "from" and "to" locations.

</td></tr><tr><td>

Populate Group - Dispatch/Work

</td><td>

Service Order Task\[sm\_task\]

</td><td>

Populates the dispatch group and assignment groups when only one dispatch group covers the location of a task, and only one assignment group is covered by the dispatch group.

</td></tr></tbody>
</table>## Email notifications installed with Service Management Core

Email notifications are added with Service Management Core.

<table id="table_o2m_2mw_dp"><thead><tr><th>

Notification

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

$\{Request\_Label\} created from email

</td><td>

Service Order\[sm\_order\]

</td><td>

Template that is used to build notifications for new applications created from a Service Management template. This notification should remain inactive and not be used.

</td></tr><tr><td>

$\{Request\_Label\} changed

</td><td>

Service Order\[sm\_order\]

</td><td>

Template that is used to build notifications for new applications created from a Service Management template. This notification should remain inactive and not be used.

</td></tr><tr><td>

$\{Task\_Label\} changed

</td><td>

Service Order\[sm\_order\]

</td><td>

Template that is used to build notifications for new applications created from a Service Management template. This notification should remain inactive and not be used.

</td></tr></tbody>
</table>
```


### File: service-management-for-the-enterprise\r_LevelFile.md

```text
---
title: Level geometry file
description: The level geometry file contains all the geometry for a given level. Each file is one map that can be rendered in the ServiceNow platform.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Level geometry file

The level geometry file contains all the geometry for a given level. Each file is one map that can be rendered in the ServiceNow platform.

The file naming standard is:

-   Name with the `id` of the level found in the community map file
-   Must contain `-geojson-geojson-level-geom-`

For example, level 46475 is found in a file named `map-23641-mv-1-ev-1-geojson-geojson-level-geom-46475-fv-2.json`

The main component of the level file is an array of features, and looks like:

```
{
            "geometry": {
                "coordinates": [
                    [
                        [
                            -117.2057125,
                            32.8818922
                        ],
                        [
                            -117.2057223,
                            32.8819201
                        ],
                        [
                            -117.2057559,
                            32.8819117
                        ],
                        [
                            -117.205746,
                            32.8818838
                        ],
                        [
                            -117.2057125,
                            32.8818922
                        ]
                    ]
                ],
                "type": "Polygon"
            },
            "id": 13960404,
            "label_area": [
                -117.20573465198783,
                32.88190207162559,
                2.9198852018440062,
                2.9198852018440062,
                1.2818771600723267
            ],
            "location": {
                "coordinates": [
                    -117.2057347,
                    32.8819021
                ],
                "type": "Point"
            },
            "obj_type": "Geometry",
            "properties": {
                "display_name": "Reef Shark",
                "entities": [
                    1473100
                ],
                "facility": "room",
                "int_address": "Room B1-132"
            },
            "type": "Feature"
        },
```

-   The `geometry` object is the geoJSON representation of points that make up the object. For more information about the GeoJSON standard, see [http://geojson.org](http://geojson.org).
-   `Geometries` can be turned into fm\_space records.
-   The `id` is mapped to the external space id on the fm\_space record.
-   The `display_name` is the name of the space.
-   The `type` is the most important property. In the example, the class is a `facility` and the type for that class is a `room`. When parsing, these values determine:
    -   If an fm\_space record is created for the geometry
    -   If the fm\_space has a subtype
    -   If any default icons are assigned to a space
    -   If any default colors are assigned to the map

-   **[Valid classes](r_ValidClasses.md)**  
There are certain classes and class types that are valid for the level geometry file.

**Parent Topic:**[GeoJSON map files](r_GeoJSONMapFiles.md)


```


### File: service-management-for-the-enterprise\r_LevelInfo.md

```text
---
title: Level information
description: Each building \(drawing\) has a list of levels. Each level is a map and represents one floor, though that is not a rule.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Community file, GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Level information

Each building \(drawing\) has a list of levels. Each level is a map and represents one floor, though that is not a rule.

```
{
                    "id": 46475,
                    "obj_type": "Level",
                    "properties": {
                        "main": true,
                        "name": "1",
                        "parent_level": 46465,
                        "root_geom": 13958749,
                        "zlevel": 0
                    }
                },
                {
                    "id": 46477,
                    "obj_type": "Level",
                    "properties": {
                        "name": "2",
                        "type": "indoor",
                        "zlevel": 1
                    }
                },
                {
                    "id": 46478,
                    "obj_type": "Level",
                    "properties": {
                        "name": "3",
                        "type": "indoor",
                        "zlevel": 2
                    }
                }
```

-   Each level creates an fm\_level record.
-   The `id` is mapped to the external level id in fm\_level.
-   The `name` is mapped to the name field in fm\_level.
-   The `zlevel` orders the levels \(0 is ground level\).
-   The `main` property assigns the main level of the building and is used as the default map when a building is selected.
-   The `id` is used to find the correct level geometry file.

**Parent Topic:**[Community file](r_CommunityFile.md)


```


### File: service-management-for-the-enterprise\r_MacrosInstallWFacVisWorkbench.md

```text
---
title: Macros installed with Facilities Visualization Workbench
description: Facilities visualization workbench adds the following macros.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Macros installed with Facilities Visualization Workbench

Facilities visualization workbench adds the following macros.

|Macro|Description|
|-----|-----------|
|floor\_plan\_show\_space|If the location is on a map, it adds a map icon next to the location field|
|floor\_plan\_show\_affected\_ci|If the location of the CI is on a map, it adds a map icon next to the CI field|
|floor\_plan\_show\_user|If the location of the user is on a map, it adds a map icon next to the user field|

**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_Manually-builtMaps.md

```text
---
title: Customer-created maps
description: Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Customer-created maps

Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.

-   **[Space roll up calculations](../concept/c_SpaceRollupCalculations.md)**  
The Facilities Service Management application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups apply to spaces that are designated as 'occupiable'. The occupancy values from that space are rolled up to the level above them.
-   **[Add or edit a campus](../task/t_AddOrEditACampus.md)**  
A campus represents the top level in the organization space, and contains buildings and map sets. Details include its location, manager, gross area, and usable area. Occupancy and utilization metrics are calculated using these details.
-   **[Add or edit a building](../task/t_AddOrEditABuilding.md)**  
Buildings are assigned to campuses with a unique name, and contain floors or levels, a location, and utilization thresholds.
-   **[Add or edit a floor or level](../task/t_AddOrEditAFloorOrLevel.md)**  
A floor is a level in a structure that contains spaces. It can be a floor of a building, the basement, levels in a parking lot, or outdoor areas.
-   **[Add or edit a space](../task/t_AddOrEditASpace.md)**  
Spaces are assigned to floors or levels, and can be cubicles, conference rooms, restrooms, gymnasiums, elevators, parking spaces, and so on. Spaces are assigned users and assets, and have the most data defined.
-   **[Add or edit a zone](../task/t_AddOrEditAZone.md)**  
Zones are a logical collection of spaces that can be shared across campuses, floors, or buildings. Examples of zones are: Chiller 4 Zone, Guest Wi-Fi Zone, AC 1 Zone, Power Circuit 3 Zone, and so on.
-   **[Delete a campus](../task/t_DeleteACampus.md)**  
Delete all buildings assigned to a campus, before deleting the campus itself.
-   **[Delete a building](../task/t_DeleteABuilding.md)**  
Before deleting a building, delete any floors or levels defined for it.
-   **[Delete a floor or level](../task/t_DeleteAFloorOrLevel.md)**  
Before you can delete a floor, you must first delete any spaces defined for it.
-   **[Delete a space](../task/t_DeleteASpace.md)**  
Spaces can be deleted from any floor or from another space as long as the space you want to remove does not have other spaces associated with it. For example, if you want to delete a space that contains several offices, those spaces must be deleted before the parent space can be deleted.
-   **[Delete a zone](../task/t_DeleteAZone.md)**  
When deleting a zone, any associated assets or spaces is also deleted.

**Parent Topic:**[Space management](r_SpaceManagement.md)


```


### File: service-management-for-the-enterprise\r_MapFilters.md

```text
---
title: Map filters
description: Users can filter the map to determine how various spaces are colored.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Map filters

Users can filter the map to determine how various spaces are colored.

There are two types of map filters:

-   Simple filter: Allows you to quickly highlight spaces based on conditions.
-   Saved filter: Allows advanced filtering when you want to highlight spaces, based on conditions not supported by a simple filter.

-   **[Simple filters](r_SimpleFilters.md)**  
Simple filters are available for the **Workbench** and the floor plan.
-   **[Saved filters](r_SavedFilters.md)**  
A saved filter allows advanced filtering when you want to highlight spaces, based on conditions not supported by a simple filter.
-   **[Create a map filter in Facilities Service Management](../task/t_CreateAMapFilter.md)**  
Create a custom filter to highlight spaces on a map for fast and easy recognition. You can create custom filters for any mappable space \(fm\_space\), asset, associated user, CI, or task with a location defined.

**Parent Topic:**[Interactive facility maps](../concept/c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\r_MapSettings.md

```text
---
title: Map settings
description: Map settings allow the facilities staff or users to choose the appearance of their floor plan.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Map settings

Map settings allow the facilities staff or users to choose the appearance of their floor plan.

**Parent Topic:**[Interactive facility maps](../concept/c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\r_NotifyEmailScriptsInstallWFacMoveMgmt.md

```text
---
title: Notification email scripts installed with Facilities Move Management
description: Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Move Management.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Notification email scripts installed with Facilities Move Management

Email notifications are a way to send selected users email or SMS notifications about specific activities in Facilities Move Management.

Facilities Move Management adds the following email notifications.

|Notification email script|Description|
|-------------------------|-----------|
|move\_delegator\_link|Generates the link that is provided in the email sent to move delegators|

**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_PropInstallWFacServMgmnt.md

```text
---
title: Properties installed with Facilities Service Management
description: Facilities Service Management Properties controls the behavior of the Facilities Service Management application.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Properties installed with Facilities Service Management

Facilities Service Management Properties controls the behavior of the Facilities Service Management application.

Facilities Service Management adds the following properties.

<table id="table_b4f_jcp_yq"><thead><tr><th>

Property

</th><th>

Description

</th></tr></thead><tbody><tr><td>

facilities.management.autoclose.request.time

</td><td>

Number of days \(integer\) after which Resolved requests are automatically closed. Zero \(0\) disables this feature.-   Type: integer
-   Default value: 1
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.workflow.state

</td><td>

Select the state at which the template workflow starts.-   Type: string
-   Default value: 5
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.default.end.time

</td><td>

Default end time for all work agents when no schedule is set, formatted as 17:00.-   Type: string
-   Default value: 17:00
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.fvw.area.unit

</td><td>

The system base area unit for facilities space tables. Set to true to use meters squared, or false to use feet squared.-   Type: true \| false
-   Default value: false
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.timezone.weight

</td><td>

Time zone weight.-   Type: integer
-   Default value: 10
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.state.value

</td><td>

Select the state that the request goes into after **work in progress**.-   Type: integer
-   Default value: 6
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.work.spacing

</td><td>

Amount of time \(in minutes\) to add between the end of a task and the travel start of the next.-   Type: integer
-   Default value: 0
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.skills.weight

</td><td>

Skills weight.-   Type: integer
-   Default value: 10
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.location.weight

</td><td>

Location weight.-   Type: integer
-   Default value: 10
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.default.start.time

</td><td>

Default start time for all agents when no schedule is set. If there is no scheduled task or if the task is continued from the previous day, the start time is set for a day other than the current day. This property uses a 24-hour clock.-   Type: string
-   Default value: 08:00
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.overwrite.user.location

</td><td>

Overwrite the user location with the primary location set in the fm\_m2m\_user\_to\_space table.-   Type: true \| false
-   Default value: true
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

glide.ui.facilities\_request\_task\_activity.fields

</td><td>

Facilities Request Task activity formatter fields-   Type: string
-   Default value: assigned\_to,cmdb\_ci,state,impact,priority,opened\_by,work\_notes,comments,override\_schedule\_conflict
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities\_management.map.merge.task.agent.markers

</td><td>

Merge the task and agent markers on the geolocation maps with a purple marker.-   Type: true \| false
-   Default value: false
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr><tr><td>

facilities.management.max.agents.processed

</td><td>

Sets the maximum number of agents processed by auto-dispatch at a time. The system has an absolute limit of 300 agents. The system cannot auto-dispatch a task for a dispatch group that contains more agents than the value configured.-   Type: integer
-   Default value: 100
-   Location: **Facilities** &gt; **Administration** &gt; **Properties**

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_PropsInstallWFacMoveMgmt.md

```text
---
title: Properties installed with Facilities Move Management
description: Properties control the behavior of the Facilities Move Management application.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Properties installed with Facilities Move Management

Properties control the behavior of the Facilities Move Management application.

Facilities Move Management adds the following properties.

|Property|Description|
|--------|-----------|
|The colors for segments on the move planning tool \[facilities.enterprise.move.mpt.segment.colors\]|The colors for segments on the move planning tool|
|The color to use for highlighting seats on the move planning tool after the list of segment colors has been exhausted \[facilities.enterprise.move.mpt.overflow.seats.color\]|The color to use for highlighting seats on the move planning tool after the list of segment colors has been exhausted|
|The color to use for non-selected segments \[facilities.enterprise.move.mpt.other.color\]|The color to use for non-selected segments|
|The color to use for highlighting open seats on the move planning tool \[facilities.enterprise.move.mpt.open.seats.color\]|The color to use for highlighting open seats on the move planning tool|

**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_ReqCreateUseInboundEmailAct.md

```text
---
title: Request creation using inbound email actions
description: Requests can be automatically created or updated from the information in inbound emails as long as the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request creation, Request Management in a Service Management application, Service Management]
---

# Request creation using inbound email actions

Requests can be automatically created or updated from the information in inbound emails as long as the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.

After the functionality has been enabled by selecting the **Requests can be created and updated by inbound email** option on the application configuration screen, three inbound email actions are available for the SM applications available in the base system. These inbound email actions are also available for new applications created using the SM application creator.

-   **[Create a request from an inbound email](../task/t_CreateARequestFromAnInboundEmail.md)**  
Requests can be automatically created from the information in inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.
-   **[Create a request from a forwarded inbound email](../task/t_CreateReqFromAForwInbndEmail.md)**  
Requests can be automatically created from the information in forwarded inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.
-   **[Update a request from an inbound email](../task/t_UpdateARequestFromAnInboundEmail.md)**  
Requests can be automatically updated from the information in inbound email replies as long the functionality has been enabled on the SM application's configuration screen. The emails must also be sent to a mailbox defined by criteria in the appropriate inbound email action.

**Parent Topic:**[Request creation](r_RequestCreation.md)

**Related topics**  


[Email and SMS notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_EmailNotifications.md)

[Inbound email actions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/c_InboundEmailActions.md)


```


### File: service-management-for-the-enterprise\r_RequestCreation.md

```text
---
title: Request creation
description: Requests are created differently based on the role that has been granted to the user. Department administrators can create requests differently than an employee can.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Request creation

Requests are created differently based on the role that has been granted to the user. Department administrators can create requests differently than an employee can.

-   **[Create a request through a catalog](../task/t_CreateARequestThroughTheCatalog.md)**  
The catalog provides several different categories so users can choose the one that closely relates to their request.
-   **[Request creation using inbound email actions](r_ReqCreateUseInboundEmailAct.md)**  
Requests can be automatically created or updated from the information in inbound emails as long as the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.

**Parent Topic:**[Request Management in a Service Management application](../concept/rm-sm-application.md)


```


### File: service-management-for-the-enterprise\r_RolesInstallWFacMoveMgmt.md

```text
---
title: Roles installed with Facilities Move Management
description: Roles control access to features and capabilities in Facilities Move Management.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Roles installed with Facilities Move Management

Roles control access to features and capabilities in Facilities Move Management.

Facilities Move Management adds the following roles.

<table id="table_b4f_jcp_yq"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains Roles

</th></tr></thead><tbody><tr><td>

Move Basic\[move\_basic\]

</td><td>

Can read and create service orders and follow up on the orders they created.

</td><td>

-   document\_management\_user
-   move\_read
-   service\_fulfiller
-   task\_activity\_writer
-   skill\_user
-   territory\_user
-   inventory\_user

</td></tr><tr><td>

Move administrator\[move\_admin\]

</td><td>

Has full control over all Service Management data. Also administers Territories and Skills, as needed.

</td><td>

-   territory\_admin
-   skill\_model\_admin
-   move\_approver\_user
-   skill\_admin
-   catalog admin
-   knowledge\_manager
-   move\_agent
-   template\_admin
-   move\_dispatcher

</td></tr><tr><td>

Move dispatcher\[move\_dispatcher\]

</td><td>

Schedules and assigns the tasks to agents. They can be searched \(filtered by\) the group they manage.

</td><td>

-   skill\_model\_user
-   inventory\_user
-   territory\_user
-   move\_basic

</td></tr><tr><td>

Move agent\[move\_agent\]

</td><td>

Can accept or reject a task. It is the one who performs the work on the site.

</td><td>

-   move\_basic

</td></tr><tr><td>

Move initiator\[move\_initiator\]

</td><td>

Similar to sm\_basic \(can read and create service orders and follow up on the orders they created\), but can also grant UI access.

</td><td>

-   move\_basic

</td></tr><tr><td>

Move approver\[move\_approver\_user\]

</td><td>

Approve orders and requests.

</td><td>

-   approver\_user

</td></tr><tr><td>

Move read\[move\_read\]

</td><td>

Can only read and create service orders and follow up on the orders they created.

</td><td>

 

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_RolesInstallWFacServMgmnt.md

```text
---
title: Roles installed with Facilities Service Management
description: Roles control access to features and capabilities in Facilities Service Management.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Roles installed with Facilities Service Management

Roles control access to features and capabilities in Facilities Service Management.

Facilities Service Management adds the following roles.

**Note:** You must add the Notify viewer \(notify\_view\) role to employees you want to view notify \(conference calls and SMS messages\) content. For more information, see [Roles installed with Notify](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/notify/r_NotifyRoles.md).

<table id="table_b4f_jcp_yq"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains Roles

</th></tr></thead><tbody><tr><td>

facilities\_read

</td><td>

Can read facilities requests.

</td><td>

none

</td></tr><tr><td>

facilities\_admin

</td><td>

Can create and modify all facilities requests, modify floor plans, and configure buildings, floors, and rooms. Administrators can also create tasks using the Clone Task feature.

</td><td>

-   knowledge\_manager
-   facilities\_staff
-   facilities\_dispatcher
-   catalog\_admin
-   territory\_admin
-   skill\_admin
-   facilities\_approver\_user
-   template\_admin
-   skill\_model\_admin

</td></tr><tr><td>

facilities\_asset\_admin

</td><td>

Can create and modify all facilities assets.

</td><td>

asset

</td></tr><tr><td>

facilities\_approver\_user

</td><td>

Can approve whether a facilities request can move forward.

</td><td>

approver\_user

</td></tr><tr><td>

facilities\_dispatcher

</td><td>

Can schedule and assign tasks to the facilities staff. They can be searched \(filtered by\) the group they manage.

</td><td>

-   skill\_model\_user
-   facilities\_staff
-   territory\_user
-   inventory\_user

</td></tr><tr><td>

facilities\_staff

</td><td>

Provides full access to the Facilities application and all modules. Can create and modify facilities requests and access facilities reports. Facilities staff are typically the users who are assigned to facilities requests and update the request record accordingly.

</td><td>

-   inventory\_user
-   skill\_user
-   document\_management\_user
-   fc\_request\_reader
-   territory\_user
-   service fulfiller
-   fc\_request\_writer
-   facilities\_read

</td></tr><tr><td colspan="3">

The facilities\_staff and facilities\_admin roles automatically inherit the following roles:

</td></tr><tr><td>

fc\_request\_reader

</td><td>

Can read facilities request records.

</td><td>

none

</td></tr><tr><td>

fc\_request\_writer

</td><td>

Can create, read, write, and delete facilities request records.

</td><td>

fc\_request\_reader

</td></tr><tr><td>

fpv\_floorplan\_writer

</td><td>

Can create, read, write, and delete facilities floor plans.

</td><td>

fpv\_floorplan\_reader

</td></tr><tr><td>

fpv\_element\_reader

</td><td>

Can read room records.

</td><td>

none

</td></tr><tr><td>

fpv\_element\_writer

</td><td>

Can create, read, write, and delete room records.

</td><td>

none

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_SMRequestStates.md

```text
---
title: Request states
description: Service Management requests follow a specific life cycle and move through a series of states, which are displayed in the State field on the request record.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Request states

Service Management requests follow a specific life cycle and move through a series of states, which are displayed in the **State** field on the request record.

The request states displayed depend on the SM application, as indicated in the table.

**Note:** The **State** field on the request record is always read-only.

<table id="table_ds4_hf5_1r"><thead><tr><th>

State

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Draft

</td><td>

Request initiator adds information about the work to be done.

</td></tr><tr><td>

Awaiting Qualification

</td><td>

Initiator fully describes the request, and qualifier can process the request. This state is valid only for the following SM applications:-   Field Service Management

</td></tr><tr><td>

Qualified

</td><td>

Request is fully qualified, meaning that all technical information to complete the request tasks has been added, but work has not started. This state is valid only for the following SM applications:-   Field Service Management

</td></tr><tr><td>

Awaiting Approval

</td><td>

When the information is complete enough for review by an approver, the request is marked ready for approval. This state is valid only for the Facilities Service Management application.

</td></tr><tr><td>

Approved

</td><td>

The appropriate approver approves the request. This state is valid only for the Facilities Service Management application.

</td></tr><tr><td>

Work In Progress

</td><td>

Work has started.

</td></tr><tr><td>

Closed Complete

</td><td>

Request was completed to specification.

</td></tr><tr><td>

Closed Incomplete

</td><td>

Request could not be completed as specified.

</td></tr><tr><td>

Canceled

</td><td>

Request was canceled.

</td></tr></tbody>
</table>In addition to the **State** field, the different request task states are also shown visually at the top of each task record with the process flow formatter.

**Note:** If the **State flows are enabled** option in the configuration screen is not selected, the process flow formatter is removed. If you added states to the request and task tables, those states are visible on the request form.

**Parent Topic:**[Request Management in a Service Management application](../concept/rm-sm-application.md)


```


### File: service-management-for-the-enterprise\r_SMRequestTaskStates.md

```text
---
title: Request task states
description: Like requests, the associated request tasks follow a specific life cycle and move through a series of states, which are displayed in the State field on the task record.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request task management, Request Management in a Service Management application, Service Management]
---

# Request task states

Like requests, the associated request tasks follow a specific life cycle and move through a series of states, which are displayed in the **State** field on the task record.

The request task states displayed depend on the SM application, as indicated in the table.

**Note:** The **State** field on the request task record is always read-only.

<table id="table_ohw_z45_1r"><thead><tr><th>

State

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Draft

</td><td>

Qualifier is not done describing the work.

</td></tr><tr><td>

Pending

</td><td>

Request task is ready to be assigned. Depending on the SM application, this state label may be expanded, for example, **Pending Dispatch** or **Pending Change**.

 The parent request state can change to **Qualified**, for example, if all associated tasks are in **Pending Dispatch** or a later state.

</td></tr><tr><td>

Assigned

</td><td>

Request task is pending acceptance from the assigned agent.

</td></tr><tr><td>

Accepted

</td><td>

Agent accepts the request task and is ready to be done.

</td></tr><tr><td>

Work In Progress

</td><td>

Work on the request task has started. The parent request state changes to **Work In Progress** if no associated tasks are in **Draft** state.

</td></tr><tr><td>

Closed Complete

</td><td>

Request task was completed to specification.

</td></tr><tr><td>

Closed Incomplete

</td><td>

Request task could not be completed as specified.

</td></tr><tr><td>

Canceled

</td><td>

Request task was canceled.

</td></tr></tbody>
</table>In addition to the **State** field, the different request task states are also shown visually at the top of each task record with the process flow formatter.

**Note:** If the **State flows are enabled** option in the configuration screen is not selected, the process flow formatter is removed.

**Parent Topic:**[Request task management](../concept/c_RequestTasksMgmt.md)


```


### File: service-management-for-the-enterprise\r_SavedFilters.md

```text
---
title: Saved filters
description: A saved filter allows advanced filtering when you want to highlight spaces, based on conditions not supported by a simple filter.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Map filters, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Saved filters

A saved filter allows advanced filtering when you want to highlight spaces, based on conditions not supported by a simple filter.

You can set a filter showing all the printers on a map and share that filter with other users. Private filters can be saved without sharing those filters with others.

![Used to filter what you want to see on a facilities map.](../image/SavedFilter.png "Facilities map filter")

**Parent Topic:**[Map filters](r_MapFilters.md)

**Related topics**  


[Simple filters](r_SimpleFilters.md)

[Create a map filter in Facilities Service Management](../task/t_CreateAMapFilter.md)


```


### File: service-management-for-the-enterprise\r_ScriptIncInstallWFacVisWorkbench.md

```text
---
title: Script includes installed with Facilities Visualization Workbench
description: Script includes are used to store JavaScript that runs on the server.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Script includes installed with Facilities Visualization Workbench

Script includes are used to store JavaScript that runs on the server.

Facilities visualization workbench adds the following script includes.

|Script include|Description|
|--------------|-----------|
|FacilitiesViewerUtils|Utility methods|
|FacilitiesViewerAJAX|Utilities used by the UI macros and the map set parsing|
|FacilitiesGeoJsonParser|Configurable parsing support for feature properties|
|FacilitiesCampusMapFileParser|Contains functions that take file attachments and process them to extract facilities spaces for the Facilities Viewer Workbench|
|FacilitiesMapFilterUtils|Utility for map filtering capabilities|
|FacilitiesConstants|List of constants used in Facilities Management and Facilities Visualization Workbench|

**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_ScriptInclnstallWFacServMgmnt.md

```text
---
title: Script includes installed with Facilities Service Management
description: Script includes are used to store JavaScript that runs on the server.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Script includes installed with Facilities Service Management

Script includes are used to store JavaScript that runs on the server.

Facilities Service Management adds the following script includes.

<table id="table_wtf_krf_2t"><thead><tr><th>

Script include

</th><th>

Description

</th></tr></thead><tbody><tr><td>

fc\_AbstractWrapper

</td><td>

Abstract wrapper used to wrap GlideRecord objects related to the Facilities Management application. Customers do not modify this class.

</td></tr><tr><td>

fpv\_ElementSecurityManager

</td><td>

Wrapper class for Floor Plan Viewer security. Customers do not modify this class.

</td></tr><tr><td>

fpv\_Factory

</td><td>

Customizable class providing the correct Facilities Management wrapper type. Customers modify this class when adding their own wrapper implementations.

</td></tr><tr><td>

fc\_AbstractSecurityManager

</td><td>

Abstract security manager providing default denied access. All security managers extend this class.Customers do not modify this class.

</td></tr><tr><td>

fpv\_Floorplan

</td><td>

Wrapper class for Floor Plan Viewer floorplan record.Customers do not modify this class.

</td></tr><tr><td>

fc\_Constants

</td><td>

Facilities ConstantsCustomers do not modify this class.

</td></tr><tr><td>

fc\_BaseFactory

</td><td>

Base class providing wrappers for Facilities Request objects.Customers do not modify this class.

</td></tr><tr><td>

fc\_RequestSecurityManager

</td><td>

Wrapper class for Facilities Management Request security. Customers do not modify this class.

</td></tr><tr><td>

fpv\_BaseFactory

</td><td>

Base class providing wrappers for FloorPlanViewer objects.Customers do not modify this class.

</td></tr><tr><td>

fpv\_AbstractSecurityManager

</td><td>

Abstract security manager providing default denied access. All security managers extend this class.Customers do not modify this class.

</td></tr><tr><td>

fc\_FacilitiesRequest

</td><td>

Facilities Request functions.Customers do not modify this class.

</td></tr><tr><td>

fpv\_AbstractWrapper

</td><td>

Abstract wrapper used to wrap GlideRecord objects related to the Floor Plan Viewer plugin.Customers do not modify this class.

</td></tr><tr><td>

fpv\_Element

</td><td>

Wrapper class for Floor Plan Viewer element records.Customers do not modify this class.

</td></tr><tr><td>

fc\_FacilitiesRequestAjax

</td><td>

Facilities Request AJAX.Customers do not modify this class.

</td></tr><tr><td>

FacilitiesUtils

</td><td>

Contains utility methods for space management, including rollup calculations from spaces to levels and levels to building.

</td></tr><tr><td>

fc\_Factory

</td><td>

Customizable class providing the correct Facilities Management wrapper type.Customers modify this class when adding their own wrapper implementations.

</td></tr><tr><td>

FacilitiesUtilsAJAX

</td><td>

Contains utility methods for facilities, including scheduling and blackouts.

</td></tr><tr><td>

fpv\_Constants

</td><td>

Floor Plan Viewer Constants.Customers do not modify this class.

</td></tr><tr><td>

fpv\_FloorplanSecurityManager

</td><td>

Wrapper class for Facilities Management Case security.Customers do not modify this class.

</td></tr><tr><td>

FacilitiesViewerUtils

</td><td>

Contains utility methods for the floor plan viewer.

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_ScrptIncludeInstallWFacMoveMgmt.md

```text
---
title: Script includes installed with Facilities Move Management
description: Script includes are used to store JavaScript that runs on the server.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Script includes installed with Facilities Move Management

Script includes are used to store JavaScript that runs on the server.

Facilities Move Management adds the following script includes.

|Script include|Description|
|--------------|-----------|
|FacilitiesMoveUtils|Utilities used by move management|

**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_ServMgmtCoreInstallRef.md

```text
---
title: Service Management Core installation reference
description: Service Management Core includes several feature plugins. Each of these plugins installs several types of components in support of the service management process.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Service Management Core installation reference

Service Management Core includes several feature plugins. Each of these plugins installs several types of components in support of the service management process.

-   **[Installed with Service Management Core](r_InstallWServMgmtCore.md#)**  
Several types of components are installed with the Service Management Core plugin.

**Parent Topic:**[Service Management](../../it-services/concept/c_ServiceManagement.md)


```


### File: service-management-for-the-enterprise\r_SimpleFilters.md

```text
---
title: Simple filters
description: Simple filters are available for the Workbench and the floor plan.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Map filters, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Simple filters

Simple filters are available for the **Workbench** and the floor plan.

Simple filters allow you to quickly highlight spaces based on conditions.

From **Workbench**, click the Filter icon ![List filter icon](../../../common/image/List_FilterIcon.png).

<table id="table_xjm_z11_x5"><thead><tr><th>

Category

</th><th>

Options

</th></tr></thead><tbody><tr><td>

Show Spaces

</td><td>

-   Deselect All
-   Lists spaces queried from the tables that extend or include \[fm\_spaces\]

</td></tr><tr><td>

Availability

</td><td>



</td></tr><tr><td>

Show color by

</td><td>

-   None
-   Department
-   Availability

</td></tr><tr><td>

Departments

</td><td>

Lists departments queried from the tables that extend or include \[fm\_m2m\_department\_to\_space\]

</td></tr><tr><td>

Zones

</td><td>

Lists zones queried from the tables that extend or include \[fm\_m2m\_space\_to\_zone\]

</td></tr></tbody>
</table>**Parent Topic:**[Map filters](r_MapFilters.md)

**Related topics**  


[Saved filters](r_SavedFilters.md)

[Create a map filter in Facilities Service Management](../task/t_CreateAMapFilter.md)


```


### File: service-management-for-the-enterprise\r_SpaceManagement.md

```text
---
title: Space management
description: The concept of space is part of the Facilities Service Management application. Space provides a definition at all levels with the same unit measure, and presents metrics that are readily available for analysis. These metrics include occupancy percentage, total space available, and so on.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Space management

The concept of space is part of the Facilities Service Management application. Space provides a definition at all levels with the same unit measure, and presents metrics that are readily available for analysis. These metrics include occupancy percentage, total space available, and so on.

**Note:** This feature is no longer available for new customers.

The additional benefits of space management include:

-   Ability to forecast future space requirements
-   Simplification of the charge back process
-   Space analysis for actual and planned use cases
-   Addition of zones for creating different collections of spaces

## Space hierarchy

A natural hierarchy models all the spaces of your organization. You can use this information to determine how effectively you are using your facilities space. The hierarchy from top to bottom is campus, building, level \(floor\), and space.

You can create types of spaces as needed. New space definition tables extend the \[fm\_space\] table. Be sure to set the proper ACLs. The following graphic depicts how tables are related to one another.

![Picture depicts order of tables as fm_campus, alm_building, fm_level, and fm_space and how they are extended](../image/SpaceHierarchy.png "Space table hierarchy")

## Space roll up calculations

The Facilities Service Management application can roll up occupancy, area, and usage information from lower to higher levels in the space hierarchy. Roll ups are spaces designated as available for occupancy. The occupancy values from that space roll up to the level above them.

When you designate a space as available for occupancy, you can also specify the maximum occupancy. Depending on the actual occupancy, a percentage appears to show how much space is available. A script include modifies the roll-up calculations.

![image is a screenshot showing the available occupancy check box and dependant fields](../image/Occupiable.png "Available for occupancy selected and dependent fields")

The values that roll up are:

-   Occupancy
-   Max occupancy
-   Assignable area

The percent occupied calculation takes place based on the current and max occupancy values.

## Associated users

You can assign users to more than one location, with a primary location.

Assign employees a primary location. A business rule ensures that an employee can have only one primary location. Employees that travel between campuses can have an assigned space on each campus. The \[fm\_m2m\_user\_to\_space\] table stores these records. Adding a user automatically updates the current occupancy and availability status of the space and performs the percent occupied calculation.

**Note:** Space becomes available when a user becomes inactive.

## Associated departments

You can assign spaces to more than one department for cost allocation and reporting purposes.

The Associated Department \[fm\_m2m\_department\_to\_space\] table extends the fm\_space table, containing the relationship of departments and percentage ownership. A percentage automatically calculates after setting the weight for each department. A business rule sets the percentages based on weight so that the sum of percentages equals 100%.

-   **[GeoJSON map files](r_GeoJSONMapFiles.md)**  
The floor plan visualization feature uses files in the GeoJSON format, an open standard for representing geographical features.
-   **[Customer-created maps](r_Manually-builtMaps.md)**  
Creating a map begins with the addition of the campus, then the buildings, floors, and other spaces.
-   **[Run transform to update data](../task/t_RunTransform.md)**  
Running a transform exports information from your records into an .xls file. That data can be imported into the ServiceNow space management application.

**Parent Topic:**[Facilities Service Management overview](../concept/c_FacilitiesServiceManagement.md)


```


### File: service-management-for-the-enterprise\r_StateFlowCleanup.md

```text
---
title: State flow cleanup
description: The business rules, client scripts, and UI actions that the system creates automatically to perform custom transitions exist only while the state flow records that use them are present.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# State flow cleanup

The business rules, client scripts, and UI actions that the system creates automatically to perform custom transitions exist only while the state flow records that use them are present.

When all the state flows on a table are deleted, the system attempts to delete any unnecessary programming elements that were created on that table, using these criteria:

<table id="table_p4b_lnb_br"><thead><tr><th>

Element

</th><th>

Deleted When

</th></tr></thead><tbody><tr><td>

-   UI action
-   Business rule
-   Dictionary override

</td><td>

The state flow that created it is deleted.

</td></tr><tr><td>

Business rule that processes events triggered by a state flow

</td><td>

All state flows for the table specified that have events configured are deleted.

</td></tr><tr><td>

Client script \(onLoad\)

</td><td>

All state flows for the table are deleted.

</td></tr><tr><td>

Client script \(onChange\)

</td><td>

All state flows with field controls are deleted.

</td></tr><tr><td>

Work notes business rule

</td><td>

All state flows with field controls or work notes are deleted

</td></tr></tbody>
</table>**Parent Topic:**[State flow customization](../concept/c_StateFlowCustomization.md)

**Related topics**  


[State flow customization](../concept/c_StateFlowCustomization.md)

[Request states](../../planning-and-policy/reference/r_SMRequestStates.md)

[Request task states](../../planning-and-policy/reference/r_SMRequestTaskStates.md)


```


### File: service-management-for-the-enterprise\r_SysPropCatInstallWFacVisWorkbench.md

```text
---
title: System property categories installed with Facilities Visualization Workbench
description: Facilities visualization workbench adds the following system property categories.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# System property categories installed with Facilities Visualization Workbench

Facilities visualization workbench adds the following system property categories.

|System property category|Description|
|------------------------|-----------|
|Floor Plan Properties|Grouping for interactive floor map properties|

**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_TableInsWFacServMgmnt.md

```text
---
title: Tables installed with Facilities Service Management
description: Facilities Service Management adds the following tables.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Tables installed with Facilities Service Management

Facilities Service Management adds the following tables.

<table id="table_u5j_fry_dt"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Equipment Item\[cmdb\_equipment\_item\]

</td><td>

Stores equipment item records

</td></tr><tr><td>

Facilities Request\[facilities\_request\]

</td><td>

Stores facilities request records

</td></tr><tr><td>

Facilities Request Task\[facilities\_request\_task\]

</td><td>

Stores facilities request task records

</td></tr><tr><td>

Facilities Request Flow\[sf\_facilities\_request\]

</td><td>

Stores request state flow records

</td></tr><tr><td>

Facilities Request Task Flow\[sf\_facilities\_request\_task\]

</td><td>

Stores request task state flow records

</td></tr><tr><td>

Facilities Request Model\[cmdb\_facreq\_product\_model\]

</td><td>

Stores request models

</td></tr><tr><td>

Facilities Request Task Model\[cmdb\_factask\_product\_model\]

</td><td>

Stores request task models

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_TableInstallWFacVisWorkbench.md

```text
---
title: Tables installed with Facilities Visualization Workbench
description: Facilities visualization workbench adds the following tables.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Visualization Workbench, Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Tables installed with Facilities Visualization Workbench

Facilities visualization workbench adds the following tables.

<table id="table_u5j_fry_dt"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Building\[alm\_building\]

</td><td>

Stores building records

</td></tr><tr><td>

Bathroom\[fm\_bathroom\]

</td><td>

Stores bathroom records

</td></tr><tr><td>

Campus\[fm\_campus\]

</td><td>

Stores campus records

</td></tr><tr><td>

Conference Room\[fm\_conference\_room\]

</td><td>

Stores conference room records

</td></tr><tr><td>

Cubicle\[fm\_cubicle\]

</td><td>

Stores cubicle records

</td></tr><tr><td>

Elevator\[fm\_elevator\]

</td><td>

Stores elevator records

</td></tr><tr><td>

Hallway\[fm\_hallway\]

</td><td>

Stores hallway records

</td></tr><tr><td>

Level\[fm\_level\]

</td><td>

Stores level records

</td></tr><tr><td>

Spaces to Zones\[fm\_m2m\_space\_to\_zone\]

</td><td>

Stores space assignment to zone records

</td></tr><tr><td>

Associated User\[fm\_m2m\_user\_to\_space\]

</td><td>

Stores associated user records

</td></tr><tr><td>

Associated Department\[fm\_m2m\_department\_to\_space\]

</td><td>

Stores associated department records

</td></tr><tr><td>

Office\[fm\_office\]

</td><td>

Stores office records

</td></tr><tr><td>

Point\[fm\_point\]

</td><td>

Stores point records

</td></tr><tr><td>

Facility Space\[fm\_space\]

</td><td>

Stores facility space records

</td></tr><tr><td>

Stairs\[fm\_stairs\]

</td><td>

Stores stairs records

</td></tr><tr><td>

Facility Zone\[fm\_zone\]

</td><td>

Stores zones records

</td></tr><tr><td>

Facilities Data\[imp\_facilities\_data\]

</td><td>

Import set table used as the source for transforming facilities space records

</td></tr><tr><td>

Facilities Floor Data\[imp\_facilities\_level\_data\]

</td><td>

Import set table used as the source for transforming facilities floors

</td></tr><tr><td>

Facility Map Option\[fm\_map\_option\]

</td><td>

Specify what space types show labels by default

</td></tr><tr><td>

Facility Map Task Option\[fm\_map\_task\]

</td><td>

Specify what task types can be seen on a map

</td></tr><tr><td>

Facility Feature\[fm\_facility\_feature\]

</td><td>

Specify what features are parsed

</td></tr><tr><td>

Space Icon Mapping\[fm\_m2m\_space\_icon\]

</td><td>

Associate an icon with a space

</td></tr><tr><td>

Facilities Map Menu Item\[fm\_map\_menu\_item\]

</td><td>

Specify what catalog items are available on a map

</td></tr><tr><td>

Fm Map Filter\[fm\_map\_filter\]

</td><td>

Create a custom filter for a map

</td></tr><tr><td>

Facilities Map Set Transformed\[fm\_map\_set\_transformed\]

</td><td>

Holds transformed GeoJSON as attachments, with the transformation showing the map in a "straight up" manner

</td></tr><tr><td>

Facility Icon\[fm\_icon\]

</td><td>

Specify icons that can be added to the map

</td></tr><tr><td>

Facilities Map Set\[fm\_map\_set\]

</td><td>

Holds GeoJSON files as attachments

</td></tr><tr><td>

Facility Map Color\[fm\_map\_color\]

</td><td>

Specifies map colors

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Visualization Workbench](r_InstallWFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_TableTransMapInstWFacServMgmnt.md

```text
---
title: Table transform maps installed with Facilities Service Management
description: Table transform maps allows you to add spaces or details about spaces from other sources.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Service Management, Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Table transform maps installed with Facilities Service Management

Table transform maps allows you to add spaces or details about spaces from other sources.

Facilities Service Management adds the following table transform maps.

|Table transform maps|Description|
|--------------------|-----------|
|Facilities level transform map|Helps the user quickly populate floor \(level\) data.|
|Facilities transform map|Helps the user quickly populate space data, including associated users.|

**Parent Topic:**[Installed with Facilities Service Management](r_InstallWFacServMgmnt.md)


```


### File: service-management-for-the-enterprise\r_TaskWindows.md

```text
---
title: Task windows
description: A task window is the time period, bordered by start and end times, in which a task is performed.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a facilities request task, Facilities request tasks, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Task windows

A task window is the time period, bordered by start and end times, in which a task is performed.

Task windows can be flexible or fixed, and are used by the route optimization and auto-dispatch features when determining the daily schedule of staff members. A flexible window has start and end times that the application attempts to respect when dispatching or routing a task automatically. The system can reschedule a flexible task window if necessary, to make it fit into the schedule of a staff member. A fixed task window cannot be rescheduled. If the auto-router that optimizes task routes or the auto-dispatcher cannot schedule the task for the fixed window time period, that task is not scheduled at all. The time interval configured for a window cannot be less than the time required to perform the task.

For more information on creating work order tasks, see .

For more information on Work order task start and end dates, see .

**Parent Topic:**[Create a facilities request task](../task/t_CreateAFacilitiesRequestTask.md)

**Parent Topic:**[Request task management](../concept/c_RequestTasksMgmt.md)


```


### File: service-management-for-the-enterprise\r_TblsInstallWFacMoveMgmt.md

```text
---
title: Tables installed with Facilities Move Management
description: Facilities Move Management adds the following tables.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Tables installed with Facilities Move Management

Facilities Move Management adds the following tables.

<table id="table_u5j_fry_dt"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Enterprise Move Scenario\[enterprise\_move\_scenario\]

</td><td>

Holds all scenarios

</td></tr><tr><td>

Enterprise Move Request\[enterprise\_move\_request\]

</td><td>

Holds actual move requests

</td></tr><tr><td>

Enterprise Move Request Task\[enterprise\_move\_request\_task\]

</td><td>

Contains tasks for enterprise move request

</td></tr><tr><td>

Enterprise Move Delegator\[move\_delegator\]

</td><td>

Stores delegator to scenario correlations

</td></tr><tr><td>

Enterprise Move Detail\[move\_detail\]

</td><td>

Contains users moved in enterprise move scenario

</td></tr><tr><td>

Move Task Template\[move\_task\_template\]

</td><td>

Contains sm\_core template for single user move tasks

</td></tr><tr><td>

Move Task Flow\[move\_sf\_task\]

</td><td>

Stateflow for single user move task

</td></tr><tr><td>

Move Request\[move\_request\]

</td><td>

Contains single user move requests

</td></tr><tr><td>

Move Request Flow\[move\_sf\_request\]

</td><td>

Stateflow for single user move request

</td></tr><tr><td>

Move Request Template\[move\_request\_template\]

</td><td>

Contains sm\_core template for single user move requests

</td></tr><tr><td>

Move Task\[move\_task\]

</td><td>

Holds single user move tasks

</td></tr></tbody>
</table>**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\r_ValidClasses.md

```text
---
title: Valid classes
description: There are certain classes and class types that are valid for the level geometry file.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Level geometry file, GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Valid classes

There are certain classes and class types that are valid for the level geometry file.

-   Facility
    -   Bathroom
        -   Gender
            -   Female
            -   Male
            -   Family
    -   Elevator
    -   Escalator
    -   Stairs
    -   Room
    -   Door
    -   Wall
    -   Hallway
    -   Inaccessible space
    -   Wall
    -   Window

-   Safety
    -   Defibrillator
    -   Fire extinguisher
    -   First aid

-   Service
    -   Atm
    -   Power
    -   Changing station
    -   Wifi

-   Area
    -   Smoke
    -   Rest area

-   Furnishing
    -   Chair
    -   Table
    -   Shelf
    -   Bin

**Parent Topic:**[Level geometry file](r_LevelFile.md)


```


### File: service-management-for-the-enterprise\r_WorkbenchConfiguration.md

```text
---
title: Facilities visualization workbench configuration
description: Space administrators configure properties on the workbench. In the application navigator, Facilities Workbench Configuration contains the configuration settings divided into sections.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Facilities visualization workbench configuration

Space administrators configure properties on the workbench. In the application navigator, **Facilities** &gt; **Workbench Configuration** contains the configuration settings divided into sections.

## Map properties

Map properties allow some customization on the floor plan. For a full description of each property, see [Space Management properties](../../facilities-service-management/reference/SpaceMgmntProperties.md).

## Parsing configuration

Map features \[fm\_facility\_feature\] define how to handle features during processing map set files and running transforms. A basic set of Map Features are pre-loaded for your use under **Space Management** &gt; **Map Configuration** &gt; **Feature Definitions**.

To create spaces for a feature type during parsing:

-   Set **Create spaces** to true.
-   Set the default space type to specify the class of space that is created.

## Icon definition

A set of Map Icons \[fm\_icon\] is pre-loaded for your use.

-   These icon definitions affect both parsing and runtime configuration.
-   If the geoJSON property of type "point" type is found during parsing and its name matches the **Parsing name** field, then an icon is added to the map.
-   Set **Active** to true to show the icons on the map.
-   Set **Show by default** to true so the icons appear on the initial map load.

## Map colors

A set of Feature Colors \[fm\_map\_color\] is preloaded for your use.

-   The **Color** and **Outline** color fields support hex values, RGB values, and HTML colors.
-   The **Opacity** field supports decimal values from 0 to 1 to set the opacity of the feature on the map.
-   The **Outline thickness** field supports whole numbers to set the outline thickness of a feature on the map.

## Map labels

Specify which space types have labels shown by default on the interactive map. The settings section of the map lets you change the currently selected values.

-   For each facilities space type, set **show label** to true for its label to be visible on the map by default.

## Map tasks

Specify which **Tasks** to show and search on the workbench.

-   For each facilities map task, set **show task** to true for its pin to be visible on the map by default.
-   Showing tasks can be limited to specified roles \(not specifying a role shows tasks to all who can see them based on security settings\).

## Map filters

Specify filters to apply to the map, coloring spaces based on conditions specified.

-   Limit showing map filters to **Roles** or specific users with the **Owner**, **Public**, and **Roles** fields.
-   Example filters are provided as a default.

## Map menu items

Specify which catalog items are displayed in the pop-up menu on the workbench.

<table id="table_mq1_f45_pcb"><thead><tr><th>

 

</th></tr></thead><tbody><tr><td>

-   To view catalog items from **Workbench**, right-click on a space and the catalog items appear. Or, click a space and the catalog items appear under **Related Links**.

</td></tr><tr><td>

-   For each facility map menu item, select the **Roles** for which this catalog item is visible. No defined roles means that the catalog item is available to all users.

</td></tr><tr><td>

-   For each facility map menu item, select the **Order** in which this entry appears.

</td></tr><tr><td>

-   For each facility map menu item, select the **Campuses** for which this catalog item is visible. No defined campuses means that the catalog item is available on all campuses.

</td></tr></tbody>
</table>**Note:** You can show catalog items from any catalog \(Facilities, IT, HR, and others\).

## URL parameters

Workbench supports URL parameters. URL parameters provide configuration information for a form or list.

**Note:** The URL parameters are listed in order of dependency. For example, syspar\_drawingId requires sysparm\_campusSysId in the URL parameter.

The URL parameters supported are:

|URL parameters|Description|
|--------------|-----------|
|sysparm\_campusSysId|Loads the map to a Campus \[fm\_campus\] identified by its sys\_id.|
|sysparm\_drawingId|Loads the map to a Building \[alm\_building\] identified by its external\_building\_id \(requires sysparm\_campusSysId\).|
|sysparm\_levelId|Loads the map to a Level \[fm\_level\] identified by its external\_level\_id \(requires sysparm\_drawingId\).|
|sysparm\_spaceid|Loads the map to a space \[fm\_space\] identified by its external\_space\_id \(requires sysparm\_levelId\).|
|sysparm\_scenarioSysId|Loads the map to a Scenario \[enterprise\_move\_scenario\] identified by its sys\_id \(requires Facilities Move Management plugin\).|
|sysparm\_zoneSysId|Loads the map to a zone \[fm\_zone\] identified by its sys\_id. Multiple spaces make up a zone.|
|sysparm\_filterSysId|Applies a filter \[fm\_map\_filter\] for a loaded map. Filters highlight spaces based on conditions.|
|sysparm\_refreshInterval|Enter a whole number value to specify a rate in minutes to automatically refresh applied filters.|
|sysparm\_labelDisplay|Specify the label to appear for a map \(can be changed under settings on the map\).|
|sysparm\_move|Loads a move query for a map.|
|sysparm\_tab|Specify the number of the tab to default to on the map.|
|sysparm\_fromWidget|Triggers event "space.clicked" on a space click, which returns \{'sys\_id': SPACESYSID, 'displayName': SPACEDISPLAYNAME\}, or hiding space which returns \{'sys\_id':", 'displayName':"\};|

**Parent Topic:**[Activate Facilities Visualization Workbench](../task/t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\r_WrkflwsInstallWFacMoveMgmt.md

```text
---
title: Workflows installed with Facilities Move Management
description: Workflows provide a drag-and-drop interface for automating multi-step processes.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Installed with Facilities Move Management, Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Workflows installed with Facilities Move Management

Workflows provide a drag-and-drop interface for automating multi-step processes.

Facilities Move Management adds the following workflows.

|Workflow|Description|
|--------|-----------|
|Single User Move|Handles single user move requests|
|Enterprise Move|Handles enterprise move requests|

**Parent Topic:**[Installed with Facilities Move Management](r_InstallWFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\request-content-pack.md

```text
---
title: Request Management Platform Analytics Solutions
description: Platform Analytics Solutions contain preconfigured dashboards. These dashboards contain actionable data visualizations that help you improve your business processes and practices.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Request Management in a Service Management application, Service Management]
---

# Request Management Platform Analytics Solutions

Platform Analytics Solutions contain preconfigured dashboards. These dashboards contain actionable data visualizations that help you improve your business processes and practices.

Platform Analytics data visualizations use Performance Analytics [indicator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/glossary/now-platform-glossary.md) data to show you data over time, helping you analyze your business processes and identify areas of improvement. With Platform Analytics Solutions, you can get value from Performance Analytics for your application with minimal setup. You can always create your own objects as well.

Platform Analytics Solutions are available for both Requests and Requested Items Management. To enable a solution for Request Management, an admin can navigate to **Performance Analytics** &gt; **Guided Setup**. Click **Get Started** then scroll to the section for Request Management. Select either the Requests or the Requsted Items guided setup. You can follow both guided setups, in either order. The guided setup takes you through the setup and configuration process.

## Inactive dashboards

Some dashboards in this content pack are inactive when installed. Complete configuration and run [data collection jobs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/glossary/now-platform-glossary.md) before you activate these dashboards. You can activate dashboards in Dashboard Properties, accessible from the context menu. You have to assign an owner to the dashboard to activate it.

-   **[Legacy: Request Management - Requested Item dashboard](requested-item-mgmt-dashboard.md)**  
Track the progress of purchase orders, transfer orders, and software assignments.
-   **[Open Requested Item State Monitor dashboard](open-req-item-state-dashboard.md)**  
Use this dashboard when you wish to dive into open requests for items divided by State: Pending, Work in Progress, or all Open requests.
-   **[Open Requested Item Age Monitor dashboard](open-req-item-age-dashboard.md)**  
Use this dashboard when you wish to dive into open requests for items divided by Age.
-   **[Open Requested Item Reports dashboard](open-req-item-reports-dashboard.md)**  
To view the current state of open item requests, see the Open Requested Item Reports.
-   **[Legacy: Request Management - Request dashboard](request-mgmt-dashboard.md)**  
Track the progress of new requests through the time they are worked on until they are closed.
-   **[Open Requests State Monitor dashboard](open-requests-state-dashboard.md)**  
Use this dashboard when you wish to dive into open requests divided by State: Pending Approval or Approved.
-   **[Open Requests Age Monitor dashboard](open-requests-age-dashboard.md)**  
Use this dashboard when you wish to dive into open requests divided by Age.
-   **[Open Request Reports dashboard](open-request-reports-dashboard.md)**  
To view the current state of open requests, see the Open Request Reports.

**Parent Topic:**[Request Management in a Service Management application](../../../product/planning-and-policy/concept/rm-sm-application.md)

**Related topics**  


[Activate your Performance Analytics subscription](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/c_PremiumPerformanceAnalytics.md)


```


### File: service-management-for-the-enterprise\request-mgmt-dashboard.md

```text
---
title: Legacy: Request Management - Request dashboard
description: Track the progress of new requests through the time they are worked on until they are closed.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Legacy: Request Management - Request dashboard

Track the progress of new requests through the time they are worked on until they are closed.

**Important:**

Starting in Xanadu release, the Request Management Platform Analytics Solutions dashboards are deprecated. Users can use the [Request dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/request.md) to view the actionable data visualizations that help in improving the business processes and practices.

![Animated tour of the tabs of the Request Management - Requests dashboard](../image/request-mgmt-requests.gif)

## End user and roles

<table id="table_ov2_tj4_2fb"><thead><tr><th>

End user and goal

</th><th>

Required role

</th></tr></thead><tbody><tr><td>

Request manager who needs to track the rate of progress of all requests

</td><td>

sn\_request\_read, sn\_request\_writeTo see the 'Basic indicators' widget, the pa\_viewer role is necessary

</td></tr></tbody>
</table>## Indicators

-   **Number of open requests**

    Records on the Request \[sc\_req\_item\] table opened on or before today and not closed.

-   **Number of new requests**

    Records on the Request \[sc\_req\_item\] table opened today and not closed.

-   **Number of closed requests**

    Records on the Request \[sc\_req\_item\] table closed today.

-   **Number of open requests not updated in last 5 days**

    As Number of open requests, but the Updated value is either empty or from more than five days ago.

-   **Number of open requests not updated in last 30 days**

    As Number of open requests, but the Updated value is either empty or from more than 30 days ago.

-   **Average age of open requests**

    The result in days of the formula `[[Summed age of open request]] / [[Number of open requests]] / 24`

-   **Average close time of requests**

    The result in days of the formula `[[Summed duration of closed requests]] / [[Number of closed requests]] / 24`

-   **Requests backlog growth**

    The result of the formula `[[Number of new requests]] - [[Number of closed requests]]`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open requests**

    The aggregate sum of the Request.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed duration of closed requests**

    The aggregate sum of the Request.CloseTime.Hours script. This script calculates the difference between the time stamp when an item request is opened and the time stamp of when it is closed.


## Breakdowns

-   Age
-   Assignment Group
-   Contact Type
-   Priority
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\requested-item-mgmt-dashboard.md

```text
---
title: Legacy: Request Management - Requested Item dashboard
description: Track the progress of purchase orders, transfer orders, and software assignments.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request Management Platform Analytics Solutions, Request Management in a Service Management application, Service Management]
---

# Legacy: Request Management - Requested Item dashboard

Track the progress of purchase orders, transfer orders, and software assignments.

**Important:**

Starting in Xanadu release, the Request Management Platform Analytics Solutions dashboards are deprecated. Users can use the [Request dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/request.md) to view the actionable data visualizations that help in improving the business processes and practices.

![Animated tour through the tabs of the Requested Item Management dashboard](../image/requested-item-mgmt-dashboard.gif "Request Management - Requested Item dashboard")

## End user and roles

<table id="table_ov2_tj4_2fb"><thead><tr><th>

End user and goal

</th><th>

Required role

</th></tr></thead><tbody><tr><td>

Request manager who needs to track the rate of progress of item requests

</td><td>

sn\_request\_read, sn\_request\_writeTo see the 'Basic requested items indicators' widget, the pa\_viewer role is necessary

</td></tr></tbody>
</table>## Indicators

Indicators are displayed in Performance Analytics widgets.

-   **Number of open requested items**

    Records on the Requested Item \[sc\_req\_item\] table opened on or before today and not closed.

-   **Number of new requested items**

    Records on the Requested Item \[sc\_req\_item\] table opened today and not closed.

-   **Number of closed requested items**

    Records on the Requested Item \[sc\_req\_item\] table closed today.

-   **Average age of open requested item**

    The result in days of the formula `[[Summed age of open requested item]] / [[Number of open requested items]] / 24`

-   **Average close time of requested items**

    The result in days of the formula `[[Summed duration of closed requested items]] / [[Number of closed requested items]] / 24`

-   **Requested items backlog growth**

    The result of the formula `[[Number of new requested items]] - [[Number of closed requested items]]`


Indicators not appearing in dashboard widgets but used in formulas:

-   **Summed age of open requested item**

    The aggregate sum of the RequestedItem.Age.Hours script. This script calculates the difference between the latest and the first time stamp for an open item request record.

-   **Summed duration of closed requested items**

    The aggregate sum of the RequestedItem.CloseTime.Hours script. This script calculates the difference between the time stamp when an item request is opened and the time stamp of when it is closed.


## Breakdowns

-   Age
-   Assignment Group
-   Priority
-   Stage
-   State

**Parent Topic:**[Request Management Platform Analytics Solutions](request-content-pack.md)


```


### File: service-management-for-the-enterprise\rm-sm-application.md

```text
---
title: Request Management in a Service Management application
description: Agents regularly access request records as they resolve requests and correspond with the submitters. They can also access built-in reports to see information like the number of active or unassigned requests for an SM application.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Request Management in a Service Management application

Agents regularly access request records as they resolve requests and correspond with the submitters. They can also access built-in reports to see information like the number of active or unassigned requests for an SM application.

-   **[Request creation](../reference/r_RequestCreation.md)**  
Requests are created differently based on the role that has been granted to the user. Department administrators can create requests differently than an employee can.
-   **[Request states](../reference/r_SMRequestStates.md)**  
Service Management requests follow a specific life cycle and move through a series of states, which are displayed in the **State** field on the request record.
-   **[Request approvals](c_RequestApprovals.md)**  
Approving a request in an SM application means that the request is ready for task creation and assignment.
-   **[Agent assignment methods](../../service-management-core/concept/c_AgentAssignment.md)**  
Depending on your settings in the SM application's configuration screen, you can assign agents manually or using auto-assignment.
-   **[Collaborate on a request](../task/t_CollaborateOnARequest.md)**  
Within a request, you can enter comments that are visible to the submitter, allowing for collaboration between the two of you. For collaboration with other agents, you can enter comments that are not visible to the submitter.
-   **[Close a request](../task/t_CloseARequest.md)**  
When you close a request, you can add details that you want the submitter to be aware of.
-   **[Request task management](c_RequestTasksMgmt.md)**  
A request contains one or more tasks. These tasks allow qualifiers to define activities that must be done to complete a request.
-   **[Request Management Platform Analytics Solutions](../../../use/dashboards/application-content-packs/request-content-pack.md)**  
Platform Analytics Solutions contain preconfigured dashboards. These dashboards contain actionable data visualizations that help you improve your business processes and practices.

**Parent Topic:**[Service Management](../../it-services/concept/c_ServiceManagement.md)


```


### File: service-management-for-the-enterprise\t_ActivateADelegator.md

```text
---
title: Activate a delegator
description: Delegators assign users to seats in a scenario. Activating the delegator sends an email notification request that they assign seats using Move Details.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Enterprise move scenarios, Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Activate a delegator

Delegators assign users to seats in a scenario. Activating the delegator sends an email notification request that they assign seats using Move Details.

## Before you begin

Role required: facilities\_staff or move\_basic

## Procedure

1.  Navigate to **All** &gt; **Enterprise Move** &gt; **Enterprise Move Scenarios**.

2.  Select the move scenario.

3.  Click the **Enterprise Move Delegators** tab to review the list of delegators.

4.  Add or delete delegators, as necessary.

5.  Click **Activate Delegators**.


-   **[Move delegators](../concept/c_EnterpriseMoveDelegators.md)**  
Facilities administrators assign move delegators to assign users to locations.

**Parent Topic:**[Enterprise move scenarios](../reference/r_EnterMoveScenarios.md)


```


### File: service-management-for-the-enterprise\t_ActivateFacMoveMgmt.md

```text
---
title: Activate Facilities Move Management
description: The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.move\) plugins are now deprecated and no longer supported or available for new activation.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Activate Facilities Move Management

The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.move\) plugins are now deprecated and no longer supported or available for new activation.

## Before you begin

Role required: admin

For details, see the [Deprecation Process \[KB0867184\]](https://hi.service-now.com/kb_view.do?sysparm_article=KB0867184) article in the Now Support knowledge base.

-   **[Configure Enterprise Move](t_ConfigureEnterpriseMove.md)**  
Facilities or Move administrators can set configurations to determine how the system displays colors on the move planning tool.
-   **[Installed with Facilities Move Management](../reference/r_InstallWFacMoveMgmt.md)**  
Several types of components are installed with the Facilities Move Management plugin.

**Parent Topic:**[Facilities Service Management overview](../../facilities-service-management/concept/c_FacilitiesServiceManagement.md)

**Related topics**  


[List of plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/list-of-plugins.md)

[Activate Facilities Service Management](../../facilities-service-management/task/t_ActivateFacilitiesSM.md)

[Activate Facilities Visualization Workbench](../../facilities-interactive-facility-maps/task/t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\t_ActivateFacVisWorkbench.md

```text
---
title: Activate Facilities Visualization Workbench
description: The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.fvw\) plugins are now deprecated and no longer supported or available for new activation.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Activate Facilities Visualization Workbench

The \(com.snc.facilities\_service\_automation\) and the \(com.snc.facilities\_service\_automation.fvw\) plugins are now deprecated and no longer supported or available for new activation.

## Before you begin

Role required: admin

For details, see the [Deprecation Process \[KB0867184\]](https://hi.service-now.com/kb_view.do?sysparm_article=KB0867184) article in the Now Support knowledge base.

## About this task

**Important:**

This plugin is no longer available for activation.

For more details on the process of deprecation and its effects on your usage of the application, see the [Plugin Deprecation \(End-of-Life\) Policy and Process \[KB0621681\] article in Now Support.](https://support.servicenow.com/kb_view.do?sysparm_article=KB0621681).

If you are an existing user of Facilities Service Management, you can continue to use the application.

-   **[Facilities visualization workbench configuration](../reference/r_WorkbenchConfiguration.md)**  
Space administrators configure properties on the workbench. In the application navigator, **Facilities** &gt; **Workbench Configuration** contains the configuration settings divided into sections.
-   **[Migrate facilities data to new space definition tables](../../facilities-legacy-floor-plan-viewer/task/t_MigFacDataToNewSpaceDefTable.md)**  
To continue using the image-based floor plans with the new space definition, migrate your data from the old tables to the new space definition tables.
-   **[Installed with Facilities Visualization Workbench](../reference/r_InstallWFacVisWorkbench.md)**  
Several types of components are installed with the Facilities Visualization Workbench plugin.

**Parent Topic:**[Facilities Service Management overview](../../facilities-service-management/concept/c_FacilitiesServiceManagement.md)

**Related topics**  


[List of plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/list-of-plugins.md)

[Activate Facilities Service Management](../../facilities-service-management/task/t_ActivateFacilitiesSM.md)

[Activate Facilities Visualization Workbench](t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\t_ActivateFacilitiesSM.md

```text
---
title: Activate Facilities Service Management
description: The Facilities Service Management plugin \(com.snc.facilities\_service\_automation\) is now deprecated and no longer supported or available for new activation.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Activate Facilities Service Management

The Facilities Service Management plugin \(com.snc.facilities\_service\_automation\) is now deprecated and no longer supported or available for new activation.

## Before you begin

Role required: admin

For details, see the [Deprecation Process \[KB0867184\]](https://hi.service-now.com/kb_view.do?sysparm_article=KB0867184) article in the Now Support knowledge base.

-   **[Create a group](../../planning-and-policy/task/t_CreateAGroup.md)**  
Set up groups and assign the necessary roles and users. The users in the group inherit the roles of the group, so you do not have to assign roles to each user separately.
-   **[Configure Facilities Service Management](t_ConfigureFacilities.md)**  
Facilities administrators can set facilities configurations to determine how the system handles daily operations.
-   **[Installed with Facilities Service Management](../reference/r_InstallWFacServMgmnt.md)**  
Several types of components are installed with the Facilities Service Management plugin.

**Parent Topic:**[Facilities Service Management overview](../concept/c_FacilitiesServiceManagement.md)

**Related topics**  


[List of plugins](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/list-of-plugins.md)

[Activate Facilities Move Management](../../facilities-move-management/task/t_ActivateFacMoveMgmt.md)

[Activate Facilities Visualization Workbench](../../facilities-interactive-facility-maps/task/t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\t_ActivateServiceManagement.md

```text
---
title: Activate Service Management
description: The Service Management Core plugin is activated automatically when you activate any service management application.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Activate Service Management

The Service Management Core plugin is activated automatically when you activate any service management application.

## Before you begin

Role required: admin

## About this task

For information on subscribing to a service management application, see [Activate Facilities Service Management](../../facilities-service-management/task/t_ActivateFacilitiesSM.md).

The Service Management Core plugin also activates the following plugins if they are not already active.

-   Automatic Assignment
-   Asset Management
-   Process Flow Formatter
-   State Flows
-   Knowledge Management V3
-   Skills Management
-   Territory Management
-   Managed documents
-   Task Activities
-   Service Management Geolocation
-   Encryption Support
-   Workbench
-   Checklist

-   **[Activate other Service Management applications](../reference/r_ActivateOtherSMApplications.md)**  
After the Service Management Core plugin has been activated, you can activate other SM applications, such as Field Service management and facilities service management. You can also activate CMS portals for each of these SM applications to add them to the Service Management Portal.

**Parent Topic:**[Service Management](../concept/c_ServiceManagement.md)

**Related topics**  


[Process flow formatter](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/r_ProcessFlowFormatter.md)

[State flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/c_StateFlows.md)

[Managed Documents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/c_ManagedDocuments.md)


```


### File: service-management-for-the-enterprise\t_AddOrEditABuilding.md

```text
---
title: Add or edit a building
description: Buildings are assigned to campuses with a unique name, and contain floors or levels, a location, and utilization thresholds.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Add or edit a building

Buildings are assigned to campuses with a unique name, and contain floors or levels, a location, and utilization thresholds.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Building**.

2.  Continue with one of the following options.

<table id="choicetable_b35_kc4_ht"><thead><tr><th align="left" id="d30013e99">

Option

</th><th align="left" id="d30013e102">

Action

</th></tr></thead><tbody><tr><td id="d30013e108">

**To add a building**

</td><td>

-   Click **New**.


</td></tr><tr><td id="d30013e126">

**To edit the details of the building**

</td><td>

-   Click the name of the building you want to edit.


</td></tr></tbody>
</table>3.  Fill in the fields on the form, as appropriate.

<table id="table_BuildingForm"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Provide a descriptive name for this building.

</td></tr><tr><td>

Campus

</td><td>

Select the campus where this building is located.

</td></tr><tr><td>

Floors

</td><td>

Enter the number of floors the building has.

</td></tr><tr><td>

Location

</td><td>

Select the location for this building. Define the locations in Organization Management. A good practice is to select a location that is defined at the address, not at the floor level. Floors are defined separately in Facilities Service Management.

</td></tr><tr><td>

Assignable area

</td><td>

Displays only the area of the building that is assignable to users.

</td></tr><tr><td>

Usable area

</td><td>

Enter only the area of the building that is available for the creation of spaces.

</td></tr><tr><td>

Gross area

</td><td>

Enter the total area of the building, including non-usable and non-assignable spaces.

</td></tr><tr><td>

Area unit

</td><td>

Select the unit used for defining the space size: square feet or square meters.

 **Note:** The **Area unit** assigned to all spaces must be consistent for the roll-up calculations to work properly. See [Space roll up calculations](../concept/c_SpaceRollupCalculations.md).

</td></tr><tr><td>

Current occupancy

</td><td>

Displays the number of users currently associated with the space. Calculation is generated using business rules on the Associated User \[m2m\_fm\_user\_to\_space\] table.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Max occupancy

</td><td>

Displays max occupancy of the building based on rollup calculations from the spaces below it.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Percent occupied

</td><td>

Displays the percentage of total space occupied based on rollup calculations from the spaces below it.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Utilization Min

</td><td>

Enter a number to define the minimum level of utilization for the building.

</td></tr><tr><td>

Utilization Max

</td><td>

Enter a number to define the maximum level of utilization for the building.

</td></tr></tbody>
</table>4.  Click **Save** and the **Related Links** section displays.

    -   Show Floor Plan: Click to display a floor plan of the selected floor.
    -   View Facilities Schedule: Click to create a facilities schedule blackout and prevent work from being performed in a defined area for a scheduled time period.
5.  Three tabs appear:

    -   Levels: List of levels for the building. Click **New** to create a level or on an existing level to edit.
    -   Assets: List of assets associated with the building. Click **New** to create an asset or on an existing asset to edit.
    -   Expense Lines: List of expense lines for the building. Click **New** to create an expense line or on an existing expense line to edit.
6.  Continue with one of the following options.

<table id="choicetable_pbs_zp4_ht"><thead><tr><th align="left" id="d30013e397">

Option

</th><th align="left" id="d30013e400">

Action

</th></tr></thead><tbody><tr><td id="d30013e406">

**To add the building**

</td><td>

-   Click **Submit**.


</td></tr><tr><td id="d30013e424">

**To update the building details**

</td><td>

-   Click **Update**.


</td></tr></tbody>
</table>
**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_AddOrEditACampus.md

```text
---
title: Add or edit a campus
description: A campus represents the top level in the organization space, and contains buildings and map sets. Details include its location, manager, gross area, and usable area. Occupancy and utilization metrics are calculated using these details.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Add or edit a campus

A campus represents the top level in the organization space, and contains buildings and map sets. Details include its location, manager, gross area, and usable area. Occupancy and utilization metrics are calculated using these details.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Campus**.

2.  Continue with one of the following options.

<table id="choicetable_b35_kc4_ht"><thead><tr><th align="left" id="d22599e99">

Option

</th><th align="left" id="d22599e102">

Action

</th></tr></thead><tbody><tr><td id="d22599e108">

**To add a campus manually**

</td><td>

-   Click **New**.


</td></tr><tr><td id="d22599e126">

**To add a campus using a map set**

</td><td>

-   [Process GeoJSON map files](t_ProcessMapFiles.md)


</td></tr><tr><td id="d22599e146">

**To edit the details of the campus**

</td><td>

-   Click the name of the campus you want to edit.


</td></tr></tbody>
</table>3.  Fill in the fields on the form, as appropriate.

    |Field|Description|
    |-----|-----------|
    |Name|Enter a descriptive name for the campus.|
    |Managed by|Select the employee who manages the campus.|
    |Location|Select from the location hierarchy.|
    |Gross area|The total floor space of a campus. Includes unusable space or excluded areas.|
    |Usable area|The total useable area of a campus. Excludes unusable space or excluded areas.|
    |Assignable area|Indicates a space roll-up calculation. See [Space roll up calculations](../concept/c_SpaceRollupCalculations.md).|
    |Area unit|Select the unit used for defining the space size: square feet or square meters.|
    |Current occupancy|Displays the number of users currently associated with the space. The calculation is generated using business rules on the Associated User \[m2m\_fm\_user\_to\_space\] table.|
    |Max occupancy|Enter the maximum capacity of users for this space. This value is intended for reporting purposes.|
    |Percent occupied|The percentage of the total floor space that is occupied.|
    |Default campus|Check to indicate that this campus is the primary location for the company.|
    |Notes|Notes or comments about this campus.|

4.  Continue with one of the following options.

<table id="choicetable_zlc_rp4_ht"><thead><tr><th align="left" id="d22599e330">

Option

</th><th align="left" id="d22599e333">

Action

</th></tr></thead><tbody><tr><td id="d22599e339">

**To add the campus**

</td><td>

-   Click **Submit**.


</td></tr><tr><td id="d22599e357">

**To update the campus details**

</td><td>

-   Click **Update**.


</td></tr></tbody>
</table>
**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)

**Related topics**  


[Space roll up calculations](../concept/c_SpaceRollupCalculations.md)


```


### File: service-management-for-the-enterprise\t_AddOrEditAFloorOrLevel.md

```text
---
title: Add or edit a floor or level
description: A floor is a level in a structure that contains spaces. It can be a floor of a building, the basement, levels in a parking lot, or outdoor areas.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Add or edit a floor or level

A floor is a level in a structure that contains spaces. It can be a floor of a building, the basement, levels in a parking lot, or outdoor areas.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Floor**.

2.  Continue with one of the following options.

<table id="choicetable_b35_kc4_ht"><thead><tr><th align="left" id="d41270e124">

Option

</th><th align="left" id="d41270e127">

Action

</th></tr></thead><tbody><tr><td id="d41270e133">

**To add a floor or level**

</td><td>

-   Click **New**.


</td></tr><tr><td id="d41270e151">

**To edit the details of a floor or level**

</td><td>

-   Click the name of the floor or level you want to edit.


</td></tr></tbody>
</table>3.  Fill in the fields on the form, as appropriate.

<table id="table_FloorForm"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Provide a descriptive name for this floor or level.

</td></tr><tr><td>

Building

</td><td>

Select the building that the floor is in.

</td></tr><tr><td>

Main level

</td><td>

Select this check box if this floor is the main level of the building.

</td></tr><tr><td>

Abbreviation

</td><td>

Enter an alphanumeric string to identify the level the floor is on. For example, enter `G` for garage or `3` for the third floor.

</td></tr><tr><td>

Assignable area

</td><td>

Displays only the area of the floor that is assignable to users.

</td></tr><tr><td>

Usable area

</td><td>

Enter only the area of the floor that is available for the creation of spaces.

</td></tr><tr><td>

Gross area

</td><td>

Enter the total area of the floor, including non-usable and non-assignable spaces.

</td></tr><tr><td>

Area unit

</td><td>

Select the unit used for defining the space size: square feet or square meters.

 **Note:** The **Area unit** assigned to all spaces must be consistent for the rollup calculations to work properly. See [Space roll up calculations](../concept/c_SpaceRollupCalculations.md).

</td></tr><tr><td>

Current occupancy

</td><td>

Displays the number of users currently associated with the space. Calculation is generated using business rules on the Associated User \[m2m\_fm\_user\_to\_space\] table.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Max occupancy

</td><td>

Displays max occupancy of the floor based on rollup calculations from the spaces below it.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Percent occupied

</td><td>

Displays the percentage of total space occupied on this floor based on rollup calculations from the spaces below it.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Utilization min

</td><td>

Enter a number to define the minimum level of utilization for the floor or level.

</td></tr><tr><td>

Utilization max

</td><td>

Enter a number to define the maximum level of utilization for the floor or level.

</td></tr></tbody>
</table>4.  Click **Save** and the **Related Links** section displays.

    -   Show Floor Plan: Click to display a floor plan of the selected floor.
    -   View Facilities Schedule: Click to create a facilities schedule blackout and prevent work from being performed in a defined area for a scheduled time period.
5.  The **Facility Spaces** section displays with a list of spaces that are part of the floor or level. Click **New** to add a facility space or click a facility space to edit.

6.  Continue with one of the following options.

<table id="choicetable_pbs_zp4_ht"><thead><tr><th align="left" id="d41270e410">

Option

</th><th align="left" id="d41270e413">

Action

</th></tr></thead><tbody><tr><td id="d41270e419">

**To add the floor**

</td><td>

-   Click **Submit**.


</td></tr><tr><td id="d41270e437">

**To update the floor details**

</td><td>

-   Click **Update**.


</td></tr></tbody>
</table>

```


### File: service-management-for-the-enterprise\t_AddOrEditASpace.md

```text
---
title: Add or edit a space
description: Spaces are assigned to floors or levels, and can be cubicles, conference rooms, restrooms, gymnasiums, elevators, parking spaces, and so on. Spaces are assigned users and assets, and have the most data defined.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Add or edit a space

Spaces are assigned to floors or levels, and can be cubicles, conference rooms, restrooms, gymnasiums, elevators, parking spaces, and so on. Spaces are assigned users and assets, and have the most data defined.

## Before you begin

Role required: admin

## About this task

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Space**.

2.  Continue with one of the following options.

<table id="choicetable_b35_kc4_ht"><thead><tr><th align="left" id="d28222e101">

Option

</th><th align="left" id="d28222e104">

Action

</th></tr></thead><tbody><tr><td id="d28222e110">

**To add a space**

</td><td>

-   Click **New**. The Facility Space interceptor page displays. Select the type of space you are creating.![Facility Space interceptor page displays list of space types.](../image/SpaceInterceptor.png)


</td></tr><tr><td id="d28222e133">

**To edit the details of a space**

</td><td>

-   Click the name of the floor or level you want to edit.


</td></tr></tbody>
</table>3.  Fill in the fields on the form, as appropriate.

<table id="table_wdh_p14_r4"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Display name

</td><td>

An auto-generated label based on the **Name**, **Building**, and **Floor** entries.

 For example, if the **Name** is 1002, the **Building** is Santa Clara Building 1, and the **Floor** is Floor 1, the **Display name** is Santa Clara Building 1 - Floor 1 – 1002.

</td></tr><tr><td>

Name

</td><td>

Enter a descriptive name for the space.

</td></tr><tr><td>

Building

</td><td>

Select the building for which you are defining the space.

</td></tr><tr><td>

Floor

</td><td>

Select the floor for which you are defining the space.

</td></tr><tr><td>

Area

</td><td>

Enter the value associated with the space size and the **Area unit** field: square feet or square meters.

</td></tr><tr><td>

Area unit

</td><td>

Select the unit used for defining the space size: square feet or square meters.

 **Note:** The **Area unit** assigned to all spaces must be consistent for the rollup calculations to work properly. See [Space roll up calculations](../concept/c_SpaceRollupCalculations.md).

</td></tr><tr><td>

Cost center

</td><td>

Select the cost center for the space. Cost centers are defined in IT Cost Management and require activation of cost management. For more information, see [Activate Cost Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/cost-management/t_ActivatingCostManagement.md). This field is a reference to \[cmn\_cost\_center\] table for charge backs reasons.

</td></tr><tr><td>

Department

</td><td>

Select the department for the space. Departments are defined in User Administration. This field is a reference to the \[cmn\_department\] table.

</td></tr><tr><td>

Status

</td><td>

Select the status of the space \(active, planned, maintenance, retired\).

</td></tr><tr><td>

Availability

</td><td>

Select the availability of the space \(vacant, partially occupied, at capacity, over capacity or reserved\).

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Current occupancy

</td><td>

Displays the number of users currently associated with the space. Calculation is generated using business rules on the Associated User \[m2m\_fm\_user\_to\_space\] table.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Max occupancy

</td><td>

Enter the maximum capacity of users for this space.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Percent occupied

</td><td>

Displays the percentage of total space occupied.

 **Note:** This field depends on the **Occupiable** option being selected.

</td></tr><tr><td>

Occupiable

</td><td>

Select this check box if the space can be occupied. See [Space roll up calculations](../concept/c_SpaceRollupCalculations.md).

</td></tr></tbody>
</table>4.  Use the **Associated Users** and **Assets** related lists to view or add users and assets to the space.

5.  Use the **Associated Departments** related list to view or add which departments are associated with this space.

6.  Continue with one of the following options.

<table id="choicetable_zlc_rp4_ht"><thead><tr><th align="left" id="d28222e433">

Option

</th><th align="left" id="d28222e436">

Action

</th></tr></thead><tbody><tr><td id="d28222e442">

**To add the space**

</td><td>

-   Click **Submit**.


</td></tr><tr><td id="d28222e460">

**To update the space details**

</td><td>

-   Click **Update**.


</td></tr></tbody>
</table>
**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_AddOrEditAZone.md

```text
---
title: Add or edit a zone
description: Zones are a logical collection of spaces that can be shared across campuses, floors, or buildings. Examples of zones are: Chiller 4 Zone, Guest Wi-Fi Zone, AC 1 Zone, Power Circuit 3 Zone, and so on.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Add or edit a zone

Zones are a logical collection of spaces that can be shared across campuses, floors, or buildings. Examples of zones are: Chiller 4 Zone, Guest Wi-Fi Zone, AC 1 Zone, Power Circuit 3 Zone, and so on.

## Before you begin

Role required: admin

## About this task

There are no restrictions on zones. They can cross campuses and buildings. In addition, spaces can belong to one or more zones.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Zone**.

2.  Continue with one of the following options.

    |Option|Action|
    |------|------|
    |**To add a zone**|Click **New**.|
    |**To edit the details of a zone**|Click the name of the zone you want to edit.|

3.  Fill in the fields on the form, as appropriate.

    |Field|Description|
    |-----|-----------|
    |Name|Provide a descriptive name for this zone.|
    |Short description|Provide a more descriptive name for this zone.|

4.  Continue with one of the following options.

    |Option|Action|
    |------|------|
    |**To add the zone**|Click **Submit**.|
    |**To update the zone details**|Click **Update**.|


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_AssignSeatsAsADelegator.md

```text
---
title: Assign users to seats
description: Delegators receive an email notification requesting that they assign seats using Move Details.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Enterprise move scenarios, Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Assign users to seats

Delegators receive an email notification requesting that they assign seats using Move Details.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Self-Service** &gt; **Floor Plan**.

2.  On the right-side pane, on the Moves tab, select the scenario.

3.  Click the destination link for which there are pending assignments.

    The users with pending destinations are listed.

    ![In this figure, the users requiring seats are shown in the Pending Destination section of the Moves tab.](../image/PendingSeats.png "Users pending destinations")

4.  Click the ![chair icon](../image/ChairIcon.png) icon beside a name and click a destination space on the map.

    The user and location are added to the Assigned destination link.

5.  Continue assigning spaces in this manner.

    You are finished assigning spaces when all users in the Pending destination list have been moved into the Assigned destination list.

    ![In this figure, the users have all been moved to the Assigned destination section of the Moves tab.](../image/UsersAssigned.png "Users assigned spaces")


**Parent Topic:**[Enterprise move scenarios](../reference/r_EnterMoveScenarios.md)


```


### File: service-management-for-the-enterprise\t_AutoDispatchATask.md

```text
---
title: Auto-dispatch a task
description: When a task is auto-dispatched, the application matches the task with a nearby agent having the necessary skills and schedule that can accommodate the task.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities request tasks, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Auto-dispatch a task

When a task is auto-dispatched, the application matches the task with a nearby agent having the necessary skills and schedule that can accommodate the task.

## Procedure

1.  To dispatch a task from a task record automatically, click **Auto-Dispatch**.

    If the system cannot find an appropriate agent, it displays a failure message and leaves the task in the **Pending Dispatch** state.


**Parent Topic:**[Facilities request tasks](../../planning-and-policy/concept/c_FacRequestTasks.md)


```


### File: service-management-for-the-enterprise\t_ChangeTheLocationOfARequest.md

```text
---
title: Change the location of a request
description: After opening a request, you can modify the details and update it.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Change the location of a request

After opening a request, you can modify the details and update it.

## Procedure

1.  Perform one of the following actions:

    -   **Facilities** &gt; **Open** and open the request you want to modify.
    -   **Facilities** &gt; **View Floor Plans**, click the request icon \(![Request icon.](../image/FacilitiesRequest.png)\), and click the request number on the list that appears.
2.  On the Facilities Request form, click the reference lookup icon beside **Room**.

    A list of locations defined for your organization appears. A location could be a room or any point on a floor plan.

3.  Select the correct location.

    If you don't see the location, contact the facilities administrator to add the location to the floor plan.


**Parent Topic:**[Facilities requests](../../facilities-service-management/concept/c_FacilitiesRequests.md)


```


### File: service-management-for-the-enterprise\t_CloneARequestTask.md

```text
---
title: Clone a request task
description: Existing tasks can be cloned to create tasks with the same populated fields.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities request tasks, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Clone a request task

Existing tasks can be cloned to create tasks with the same populated fields.

## Before you begin

Role required: admin, ITIL, creator, or catalog admin

## About this task

In the cloning process, the following information is copied from the source task:

-   Parent request reference
-   Short description
-   Description
-   Assignment group
-   Location
-   Required skills

## Procedure

1.  Open the request task and select **Clone Task** under **Related Links**.

    The application creates a task in **Draft** state. The **Work Notes** field contains the original task number and text stating that the task is a clone.


**Parent Topic:**[Facilities request tasks](../concept/c_FacRequestTasks.md)

**Parent Topic:**[Request task management](../concept/c_RequestTasksMgmt.md)


```


### File: service-management-for-the-enterprise\t_CloseARequest.md

```text
---
title: Close a request
description: When you close a request, you can add details that you want the submitter to be aware of.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Close a request

When you close a request, you can add details that you want the submitter to be aware of.

## Procedure

1.  Navigate to **All** &gt; **\[SM application\]** &gt; **Assigned to me**.

2.  Click the request number.

3.  In the **Additional comments** field, enter any final notes or comments.

4.  Change the **State** field to the appropriate closed state.

5.  Click **Update**.


-   **[Closed and completed requests](../concept/c_ClosedAndCompletedRequests.md)**  
When the **Request lifecycle** option is set to **request-driven**, the assigned agent can complete and close the request once all the tasks in the request are complete.

**Parent Topic:**[Facilities requests](../../facilities-service-management/concept/c_FacilitiesRequests.md)

**Parent Topic:**[Request Management in a Service Management application](../concept/rm-sm-application.md)


```


### File: service-management-for-the-enterprise\t_CollaborateOnARequest.md

```text
---
title: Collaborate on a request
description: Within a request, you can enter comments that are visible to the submitter, allowing for collaboration between the two of you. For collaboration with other agents, you can enter comments that are not visible to the submitter.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Collaborate on a request

Within a request, you can enter comments that are visible to the submitter, allowing for collaboration between the two of you. For collaboration with other agents, you can enter comments that are not visible to the submitter.

## Procedure

1.  Navigate to **All** &gt; **\[SM application\]** &gt; **All \[SM application\] Requests**.

2.  Open the request you want to collaborate on.

3.  In the **Additional comments** \(Customer visible\) field, enter the comments that you want the person who submitted the request to see.

    The submitter can see the comments in this field and add more comments as necessary. Update this field as many times as necessary to correspond with the submitter.

4.  To correspond with other agents, enter content that you do not want the submitter to see in the **Work notes** field.


**Parent Topic:**[Facilities requests](../../facilities-service-management/concept/c_FacilitiesRequests.md)

**Parent Topic:**[Request Management in a Service Management application](../concept/rm-sm-application.md)


```


### File: service-management-for-the-enterprise\t_ConfigureEnterpriseMove.md

```text
---
title: Configure Enterprise Move
description: Facilities or Move administrators can set configurations to determine how the system displays colors on the move planning tool.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Move Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Configure Enterprise Move

Facilities or Move administrators can set configurations to determine how the system displays colors on the move planning tool.

## Before you begin

Role required: facilities\_admin or move\_admin

## Procedure

1.  Navigate to **All** &gt; **Enterprise Move** &gt; **Configuration** &gt; **Enterprise Move Properties**.

2.  Fill in the fields on the form, as appropriate.

    |Option|Selection|
    |------|---------|
    |The colors for segments on the move planning tool|Hex values, RGB values, or HTML colors|
    |The color to use for highlighting seats on the move planning tool after the list of segment colors has been exhausted|Hex values, RGB values, or HTML colors|
    |The color to use for non-selected segments|Hex values, RGB values, or HTML colors|
    |The color to use for highlighting open seats on the move planning tool|Hex values, RGB values, or HTML colors|

3.  Click **Save**.


**Parent Topic:**[Activate Facilities Move Management](t_ActivateFacMoveMgmt.md)


```


### File: service-management-for-the-enterprise\t_ConfigureFacilities.md

```text
---
title: Configure Facilities Service Management
description: Facilities administrators can set facilities configurations to determine how the system handles daily operations.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Configure Facilities Service Management

Facilities administrators can set facilities configurations to determine how the system handles daily operations.

## Before you begin

Role required: facilities\_admin

## About this task

Facilities Service Management defaults to the request-driven processing method for handling tasks. For information about both processing methods, see [Task vs. request driven processing](../../planning-and-policy/concept/c_TaskVsRequestDrivenProcessing.md).

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Administration** &gt; **Configuration**.

    **Note:** Administrators in domains lower than the global domain can view the Configurations screen, but cannot modify the settings.

    The options on the configuration screen are arranged in a multiple-tabbed layout, as follows:

    -   The **Business Process** tab contains options for setting up the request life cycle, creating catalogs and requests, and configuring notifications.
    -   The **Assignment** tab contains options for setting up manual and auto-assignment.
    -   The **Add-ons** tab contains options for enabling the knowledge base, managed documents, and task activities.
2.  Fill in the fields on the **Business process** tab.

    **Note:** The Configuration screen contains many configuration options. An option is enabled when the switch appears green and is toggled to the right. All configuration options listed in the **Dependency** must be enabled in order for the option to be displayed.

<table id="table_h44_tnx_5r"><thead><tr><th>

Field

</th><th>

Description

</th><th>

Dependency

</th></tr><tr><th class="sub-head" colspan="2">

Lifecycle

</th><th>

 

</th></tr></thead><tbody><tr><td>

Enable state flows

</td><td>

Enable state flows consistent with all [service management applications](../../it-services/concept/c_ServiceManagement.md). If you prefer to create your own state flows using business rules, client scripts, and UI actions, disable the option. A confirmation box displays and includes a link to a help article that describes the implications of disabling state flows. It is highly recommended that you read the article before proceeding.

 If you disable state flows and save, this configuration option is removed from the screen and state flows cannot be re-enabled from the user interface.

</td><td>

 

</td></tr><tr><td>

Process life cycle

</td><td>

Select **request driven \(subtasks are optional\)** if you do not want to require tasks to fulfill requests. When the request life cycle is request driven, requests can be directly assigned to users in an assignment group. Users can still add tasks to requests. However, closing all tasks does not automatically close the request. **Note:** If the **Enable state flows** option is not selected, the process life cycle becomes**request-driven** and this field is not displayed.

</td><td>

**Enable state flows** is turned on.

</td></tr><tr><td>

Agent must accept or reject the assigned task

</td><td>

Enable to require the assigned agent to accept or reject the task.

</td><td>

**Enable state flows** is turned on.

</td></tr><tr><td>

Work notes are required to close or cancel a request or task

</td><td>

Enable if work notes are required when closing, completing, or canceling requests and tasks. If it is disabled, work notes are not needed when closing, completing, or canceling.

</td><td>

 

</td></tr><tr><td>

Copy task work notes to request

</td><td>

Enable to synchronize task work notes with the work notes on the order or request. When work notes are added in the task, the same work notes appear in the order or request.

</td><td>

**Enable state flows** is turned on.

</td></tr><tr class="sub-head"><td class="sub-head" colspan="3">

**Catalog and Request Creation**

</td></tr><tr><td>

Create or update requests by inbound email.

</td><td>

Enable this option to allow inbound email messages to create or update requests. This option must be enabled to allow requests to be marked as spam.

</td><td>

 

</td></tr><tr><td>

Requests are created using

</td><td>

Select **catalog or regular form** to install the catalog and enable automatic publishing of request templates to the catalog.Select **regular form only** to uninstall the catalog and disable automatic publishing of request templates to the catalog.

</td><td>

 

</td></tr><tr><td>

Templates create a dedicated catalog item

</td><td>

Enable this option to allow automatic publishing of catalog items for the application.

</td><td>

 

</td></tr><tr class="sub-head"><td colspan="3">

**Notifications**

</td></tr><tr><td>

Send a notification when a field changes for a task or request.

</td><td>

Configure notifications to be sent to specific recipients when selected fields in requests and/or tasks change. 1.  From **Table**, select **Request** or **Task**.
2.  From **Field**, select the field to use for generating notifications. When a change is made to the selected field, a notification is sent to the recipients identified.
3.  From **Recipients**, select one or more recipients
4.  If **a specific user** or **a specific group**, is selected, the user is prompted to select a user or group.
5.  To define more notifications using other fields or recipients, repeat the steps on the next line.
6.  To remove a notification, click the ![delete notification symbol](../../planning-and-policy/image/DeleteNotification.png) symbol to the right of the notification.


</td><td>

 

</td></tr></tbody>
</table>3.  Click the **Assignment** tab and fill in the fields.

<table id="table_yl5_vns_5r"><thead><tr><th>

Field

</th><th>

Description

</th><th>

Dependency

</th></tr></thead><tbody><tr class="sub-head"><td class="sub-head" colspan="3">

Assignment method for tasks: Manually

</td></tr><tr><td>

Assign requests or tasks based on assignment group coverage areas

</td><td>

Enable this option to limit the selection of groups from the **Dispatch group** and **Assignment group** fields to groups that cover the location of the task.

</td><td>

 

</td></tr><tr class="sub-head"><td colspan="3">

**Scheduling**

</td></tr><tr><td>

Use agent or task scheduling

</td><td>

Enable this option to allow agent auto-assignment and agent auto-selection.

</td><td>

 

</td></tr><tr><td>

Auto-selection of agents will consider time zone for tasks

</td><td>

Enable this option to consider the time zone of the agent when assigning a task.

</td><td>

**Enable state flows** is turned on.

</td></tr><tr><td>

Enable priority assignment

</td><td>

Enable this option to use priority assignment for auto-assigning agents.

</td><td>

-   **Enable state flows** is turned on.
-   **Process life cycle: Life cycle is task driven**.
-   **Auto-selection of agents will consider agent or task schedules**.
 **Note:** The **Process life cycle** option is not available in all service management applications.

</td></tr><tr><td>

Select priorities for priority assignment

</td><td>

Select priorities for assignment.

</td><td>

-   **Use agent or task scheduling** is turned on.
-   **Enable priority assignment** is turned on.


</td></tr><tr class="sub-head"><td colspan="3">

**Additional Factors**

</td></tr><tr><td>

Auto-selection of agents will consider location of agents

</td><td>

Enable this option to use the agent and location when determining who to assign the task to. Agents closer to the task location receive preference.

</td><td>

-   **Enable state flows** is turned on.
-   If using **Process life cycle: Life cycle is task driven**, then **Assignment method for tasks: using auto-assignment**.
-   If using **Process life cycle: Life cycle is request driven**, then **Assignment method for requests: using auto-assignment**.


</td></tr><tr><td>

Auto-selection of agents for tasks requires them to have skills

</td><td>

This option determines the degree to which skills must be matched to a task when determining auto-assignment. -   Select **all** to require that an assigned agent has all the skills to perform the task. An agent who lacks one skill is eliminated.
-   Select **some** if you want agents who have most of the skills to perform the task.
-   Select **none** if you want to auto-assign agents without considering skills.


</td><td>

-   **Enable state flows** is turned on.
-   If using **Process life cycle: Life cycle is task driven**, then **Assignment method for tasks: using auto-assignment**.
-   If using **Process life cycle: Life cycle is request driven**, then **Assignment method for requests: using auto-assignment**.


</td></tr></tbody>
</table>4.  Click the **Add-ons** tab and fill in the fields.

    |Field|Description|Dependency|
|Part Requirements|
    |-----|-----------|----------|
    |-----------------|
    |Part requirements are needed by agents|Enable this option to require agents to specify parts for the task.| |
    |Edit associated models|Click **add** and select the part model to be used for this task. Click **more** to select more part models.|**Part requirements are needed by agents.**|
    |**Documentation**|
    |Enable a dedicated knowledge base|Enable this option to install the knowledge base for the application.| |
    |Enable managed documents|Enable this option to add a related list to managed documents.| |
    |Enable task activities|Enable this option to log the task interactions and communications, such as phone calls and email messages.| |
    |**Associated Task Tables**|
    |Select associated tables|Click **Add** to select more tables.| |
    |**Maps**|
    |Enable maps|Enable this option to use maps.| |

5.  Click **Save**.

    **Warning:** When the **Enable state flows** option is disabled, a confirmation box with a link to documentation appears, explaining the consequences of disabling state flows. It is highly recommended that you read the documentation before making this change, as the action of disabling service management state flows cannot be reversed.


-   **[Task vs. request driven processing](../../planning-and-policy/concept/c_TaskVsRequestDrivenProcessing.md)**  
All applications use either task-driven or request-driven processes for handling tasks.

**Parent Topic:**[Activate Facilities Service Management](t_ActivateFacilitiesSM.md)


```


### File: service-management-for-the-enterprise\t_CreateAFacilitiesRequestTask.md

```text
---
title: Create a facilities request task
description: Facilities request tasks are created from facilities requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Facilities request tasks, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a facilities request task

Facilities request tasks are created from facilities requests.

## Before you begin

Role required: facilities\_admin or facilities\_qualifier

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Requests** &gt; **All Facility Requests**.

2.  Open the desired request.

3.  Click the **Add Task** related link.

4.  Fill in the fields on the form.

<table id="table_ptc_455_cr"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

Auto-generated identification number for the task.

</td></tr><tr><td>

State

</td><td>

Current state of the task, such as **Accepted** or **Closed Complete**. States progress automatically as users complete the work for each successive state and appears on the subway map at the top of the form.

</td></tr><tr><td>

Parent

</td><td>

Facilities request that this task is associated with.

</td></tr><tr><td>

Assignment group

</td><td>

Group from which an individual facilities staff member is selected to complete the task. The lookup list shows only the assignment groups associated with the selected **Location**. If the **Assignment Group** field is empty, the system searches for the group covering the territory that includes the location of the task.

</td></tr><tr><td>

Cloned from

</td><td>

Record number of the task this task was cloned from, if any.

</td></tr><tr><td>

Assigned to

</td><td>

The individual staff member to complete the task, selected from the **Assignment group**. The **Assigned to** field lookup list shows only those staff members in the assignment group who have all the **Skills** required. If no exact match of skills is found, the lookup list shows all assignment group members.

</td></tr><tr><td>

Override schedule conflict

</td><td>

 

</td></tr><tr><td>

Location

</td><td>

The geographical area of the request. The location is critical for determining which staff member is assigned to the task.

</td></tr><tr><td>

Template

</td><td>

 

</td></tr><tr><td>

Skills

</td><td>

Abilities necessary to execute the task. The system automatically completes the **Skills** field based on the selection in the **Affected CI** field on the associated request. If you change the affected CI on the request, the system adds any skills required by the new CI to the skills already listed here.

</td></tr><tr><td>

Short description

</td><td>

Brief explanation of the task.

</td></tr><tr><td>

Description

</td><td>

Exact technical description of the unit of work to be performed. Provide as much detail about the problem as possible to avoid extra communication with the caller in later stages of the request.

</td></tr><tr><td>

Work notes

</td><td>

Information about the task as it progresses through each state. Work notes are not visible to customers.

</td></tr><tr><td colspan="2">

**Schedule**

</td></tr><tr><td>

Scheduled start

</td><td>

Date and time that work on the task is expected to begin. The scheduled start time is set automatically to one hour after the scheduled travel start time. For example, if **Scheduled travel start** is 10:00 AM, the **Scheduled start** time is set to 11:00 AM. When the task reaches the **Pending Dispatch** stage, the default value can be edited. A staff member cannot be scheduled for two tasks at the same time. If a specified time is already allocated to another task, an error message is displayed. This field is required when the task is assigned or when the state is **Assigned**, **Accepted**, **Pending Dispatch**, or **Work In Progress**.

</td></tr><tr><td>

Estimated end

</td><td>

\[Read-only\] Date on which work on the task ends. The date is automatically calculated based on the **Scheduled start** and **Estimated work duration**.

</td></tr><tr><td>

Estimated work duration

</td><td>

Estimated amount of work time. One hour is set by default. The default value can be edited during the **Draft** or **Pending Dispatch** stage. When defining the estimated work duration, it cannot exceed the total time of the window.

</td></tr><tr><td>

Actual work start

</td><td>

Time when work began. This field is not available until **Actual travel start** time is added manually or the **Start Travel** button is clicked.

</td></tr><tr><td>

Actual work end

</td><td>

Time when work on the task was completed.

</td></tr><tr><td>

Actual duration

</td><td>

\[Read-only\] Total amount of time spent traveling to the site and completing the task. This value is automatically calculated based on the **Actual travel start** and **Actual work end** times.

</td></tr></tbody>
</table>5.  Click **Submit**.


-   **[Task windows](../reference/r_TaskWindows.md)**  
A task window is the time period, bordered by start and end times, in which a task is performed.

**Parent Topic:**[Facilities request tasks](../concept/c_FacRequestTasks.md)


```


### File: service-management-for-the-enterprise\t_CreateAGroup.md

```text
---
title: Create a group
description: Set up groups and assign the necessary roles and users. The users in the group inherit the roles of the group, so you do not have to assign roles to each user separately.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Service Management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a group

Set up groups and assign the necessary roles and users. The users in the group inherit the roles of the group, so you do not have to assign roles to each user separately.

## Before you begin

Role required: admin

## About this task

There are a few good practices when creating groups:

-   Create one group for administrators and assign the admin role to this group only.
-   Create as many groups as needed in your organization. For example, create a staff group for each geographic location, function, skills, and product models, such as building maintenance or building security. Assign the necessary users to those groups, and then assign the staff role to those groups.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Click **New**.

3.  Fill in the fields on the form, as appropriate.

    See [Create a user group](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/user-administration/t_CreateAGroup.md) for an explanation of each field.

4.  Click the lock icon beside the **Type** field.

    If the field is not visible, configure the form to add it.

    The **Type** field expands.

5.  Click the lookup icon \(![Lookup icon.](../image/SearchIcon.png)\) and select the **\[application\]** type.

6.  Right-click the form header and select **Save**.

7.  Add the \[application\]\_admin or \[application\]\_staff role to the **Roles** related list.

8.  Add users to the **Group Members** related list.

9.  Click **Update**.


**Parent Topic:**[Activate Facilities Service Management](../../facilities-service-management/task/t_ActivateFacilitiesSM.md)


```


### File: service-management-for-the-enterprise\t_CreateAMapFilter.md

```text
---
title: Create a map filter in Facilities Service Management
description: Create a custom filter to highlight spaces on a map for fast and easy recognition. You can create custom filters for any mappable space \(fm\_space\), asset, associated user, CI, or task with a location defined.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Map filters, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a map filter in Facilities Service Management

Create a custom filter to highlight spaces on a map for fast and easy recognition. You can create custom filters for any mappable space \(fm\_space\), asset, associated user, CI, or task with a location defined.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Space Management** &gt; **Map Configuration** &gt; **Filters**.

2.  Click **New** or an existing map filter.

3.  Complete or edit the form.

    Map Filter form

<table id="table_zvv_lgq_hbb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Unique name for the map filter.

</td></tr><tr><td>

Table

</td><td>

Table that the map filter is accessing information from.

</td></tr><tr><td>

Location field

</td><td>

Fields from the table selected when the table is not associated with a location. **Note:** The table selected determines which fields show. You can dot-walk to any field from the selected table.

</td></tr><tr><td>

Group by

</td><td>

Field that the map filter groups by. You can color each matching space based on this group.For example, you can group by availability status from the Facility Space \[fm\_space\] table.

 **Note:** The table selected determines which fields show. You can dot-walk to any field from the selected table.

</td></tr><tr><td>

Condition

</td><td>

Conditions that define the map filter. The table selected determines what conditions are available.

</td></tr><tr><td>

Public

</td><td>

Filter is available to others.

</td></tr><tr><td>

Roles

</td><td>

Roles required to view this filter on the workbench.

</td></tr><tr><td>

Description

</td><td>

Description of the map filter.

</td></tr></tbody>
</table>4.  Click **Submit** or **Update**.


## What to do next

After you create a filter, click the **Show on Floor Plan** related link to view the map filter on a map.

**Parent Topic:**[Map filters](../reference/r_MapFilters.md)

**Related topics**  


[Simple filters](../reference/r_SimpleFilters.md)

[Saved filters](../reference/r_SavedFilters.md)


```


### File: service-management-for-the-enterprise\t_CreateAMoveReqThruFacCatalog.md

```text
---
title: Create a move request through the facilities catalog
description: Users can submit move requests by selecting from the categories of the Facilities catalog.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities move requests, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a move request through the facilities catalog

Users can submit move requests by selecting from the categories of the Facilities catalog.

## Before you begin

Role required: none

## Procedure

1.  Navigate to **All** &gt; **Self-Service** &gt; **Facilities Catalog**.

2.  Select the **Space Management** category.

3.  Select the subcategory for your move request.

4.  Fill in the fields on the form, as appropriate.

    **Note:** Some request forms do not contain every field described here. For more information, see [Forms](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UsingForms.md).

<table id="table_gj5_llf_xq"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Requested by

</td><td>

The name of the person submitting this request.

</td></tr><tr><td>

User to be moved

</td><td>

Select a name if you are opening this request on behalf of another user.

</td></tr><tr><td>

From location

</td><td>

The current location of the user.

</td></tr><tr><td>

To location

</td><td>

The new location for the user.

</td></tr><tr><td>

Requested move date

</td><td>

Select a date for the move request to be performed.

</td></tr><tr><td>

Additional comments

</td><td>

Enter additional information about the move that you feel is important for the facilities staff to know.

</td></tr><tr><td class="sub-head" colspan="2">

Options

</td></tr><tr><td>

Security badge update

</td><td>

Select this check box if the user being moved requires changes in location access.

</td></tr><tr><td>

Boxes

</td><td>

Select this check box if the user requires that boxes be delivered before their move.

</td></tr><tr><td>

Move assets

</td><td>

Select this check box if the user being moved requires assets to be moved along with them.

</td></tr><tr><td>

Assets to be moved

</td><td>

Provides filtering and condition statements to help narrow your search for assets. Move **assets** to the Selected assets list. **Note:** This field depends on the **Move assets** check box being selected.

</td></tr></tbody>
</table>5.  Click **Submit**.


**Parent Topic:**[Facilities move requests](../concept/c_FacMoveRequests.md)


```


### File: service-management-for-the-enterprise\t_CreateAReqThroughFacCatalog.md

```text
---
title: Create a request through the facilities catalog
description: Employees use the Facilities catalog to submit requests. The catalog provides several different categories so users can choose the one that closely relates to their request.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities request creation, Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a request through the facilities catalog

Employees use the Facilities catalog to submit requests. The catalog provides several different categories so users can choose the one that closely relates to their request.

## Before you begin

Role required: none

## Procedure

1.  Navigate to **All** &gt; **Self-Service** &gt; **Facilities Catalog**.

2.  Select a category.

3.  If necessary, select a subcategory.

4.  Fill in the fields on the form, as appropriate.

    **Note:** Some request forms do not contain every field described here. For more information, see [Forms](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UsingForms.md).

    |Field|Description|
    |-----|-----------|
    |Opened for|The name of the person submitting this request. Select a new name if you are opening this request on behalf of another user.|
    |Location|The location for this request.|
    |Short Description|A brief summary of the request.|
    |Detailed Description|A detailed description of the request.|
    |Priority|The priority that describes the importance of this request.|

5.  Click **Submit**.


**Parent Topic:**[Facilities request creation](../reference/r_FacilitiesRequestCreation.md)


```


### File: service-management-for-the-enterprise\t_CreateARequestFromAnInboundEmail.md

```text
---
title: Create a request from an inbound email
description: Requests can be automatically created from the information in inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request creation using inbound email actions, Request creation, Request Management in a Service Management application, Service Management]
---

# Create a request from an inbound email

Requests can be automatically created from the information in inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.

## Procedure

1.  Navigate to **All** &gt; **System Policy** &gt; **Email** &gt; **Inbound Actions**.

2.  Select the inbound email action.

    For example, **Create Work Order**.

    The inbound email action record opens and displays the default conditions that trigger the inbound email action.

    When an email is sent to the mail list defined by the criteria in **Actions**, a request is created with the following information:

    -   The **Contact type** is set to **Email**.
    -   The email sender \(if found\) populates the **opened\_by** and **Caller** fields for a newly created sm\_order based item.
    -   The email subject populates the **Short description** field.
    -   The email body populates the **Description** field.
    -   The email senders company \(Sender-&gt;Company\) populates the **Company** field.
    -   The email senders location \(Sender-&gt;Location\) populates the **Location** field.
    -   The entire email is copied into the **Work notes** field.
3.  You can use the email action as it is or modify it to meet the needs of your organization.


**Parent Topic:**[Request creation using inbound email actions](../reference/r_ReqCreateUseInboundEmailAct.md)


```


### File: service-management-for-the-enterprise\t_CreateARequestThroughTheCatalog.md

```text
---
title: Create a request through a catalog
description: The catalog provides several different categories so users can choose the one that closely relates to their request.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request creation, Request Management in a Service Management application, Service Management]
---

# Create a request through a catalog

The catalog provides several different categories so users can choose the one that closely relates to their request.

## Procedure

1.  Open **Field Service Catalog**.

2.  Choose from the displayed categories.

3.  Select a subcategory, if necessary.

4.  Fill in the fields on the form.

    **Note:** Each catalog can display different fields. The following is a list of fields displayed when you select Service Management catalog.

    |Field|Description|
    |-----|-----------|
    |Opened for|The name of the person submitting this request. Select a new name if you are opening this request on behalf of another user.|
    |Location|The location for this request.|
    |Priority|The priority that describes the importance of this request.|
    |Short Description|A brief summary of the request.|
    |Detailed Description|A detailed description of the request.|

5.  Click **Submit**.

    **Note:** If the catalog fields do not appear on the request form, you can configure the form and add variables or variable sets.


**Parent Topic:**[Request creation](../reference/r_RequestCreation.md)


```


### File: service-management-for-the-enterprise\t_CreateFacReqWorkbench.md

```text
---
title: Create a facility request from the floor plan
description: All users in your organization can create any facility requests that your facilities admin \[facilities\_admin\] has enabled on the floor plan view.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Floor Plan, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a facility request from the floor plan

All users in your organization can create any facility requests that your facilities admin \[facilities\_admin\] has enabled on the floor plan view.

## Before you begin

Role required: none

## Procedure

1.  Perform one of the following options.

    |Choice|Action|
    |------|------|
    |**To search for a space location**|[Find a space on the floor plan.](t_FindASpaceOrUser.md)|
    |**If you know the space location**|Click the space on the floor plan.|

2.  On the Spaces tab, under the room information details and **Related Links** section, click **Create Facilities Request**.

    **Note:** You can also right-click the space link and select **Create Facilities Request**.

    ![Create a facilities request like trash removal.](../image/CreateFacReq.png)

    |Field|Description|
    |-----|-----------|
    |Location|The specific location from the floor plan.|
    |Short Description|Enter a short description summarizing the facilities request. You can overwrite the default description.|
    |Detailed Description|Enter a detailed description of the facilities request.|
    |Requested buy|The user name of the person making the request displays.|
    |Additional comments|Add additional comments if necessary.|

3.  Click **Submit** and the **Floor Plan** form displays.


**Parent Topic:**[Facilities Floor Plan](../concept/c_FacilitiesFloorPlan.md)


```


### File: service-management-for-the-enterprise\t_CreateFacScheduleBlackout.md

```text
---
title: Create a facilities schedule blackout
description: Blackout periods can be defined for spaces, levels, buildings, campuses, and zones. The Facilities\_admin can override blackout period requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Schedule blackout periods, Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a facilities schedule blackout

Blackout periods can be defined for spaces, levels, buildings, campuses, and zones. The Facilities\_admin can override blackout period requests.

## Before you begin

Role required: Facilities\_admin \(create\), Facilities\_staff \(view\)

## Procedure

1.  Navigate to the list of spaces, levels, buildings, campuses, or zones within the **Space Management** application. For example, **All** &gt; **Space Management** &gt; **Floor**

2.  Select a record for the space you want to add the blackout period.

3.  In the **Related Links**, click **View Facilities Schedule**.

4.  Fill in the fields on the form, as appropriate.

    |Field|Description|
    |-----|-----------|
    |Schedule|The new or existing cmn\_schedule|
    |Schedule name|The name of the cmn\_schedule|
    |Blackout name|The name of the blackout|
    |Start|Date to start the blackout schedule|
    |End|Date to end the blackout schedule|
    |Blackout spans for|Display blackout spans for selected time frame|

5.  Click **Add**.


**Parent Topic:**[Schedule blackout periods](../concept/c_ScheduleBlackout.md)


```


### File: service-management-for-the-enterprise\t_CreateMoveReqWFacReqForm.md

```text
---
title: Create a move request with the move request form
description: Facilities staff members can create move requests using the move request form.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Facilities move requests, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a move request with the move request form

Facilities staff members can create move requests using the move request form.

## Before you begin

Role required: facilities\_read

## About this task

Associating a CI to a move request helps your facilities team understand which services or assets are affected in a move. You can also use this form to include extra comments and work notes for the move request.

## Procedure

1.  Navigate to **All** &gt; **Facilities Move** &gt; **Requests** &gt; **Create New**.

2.  Fill in the fields on the form, as appropriate.

<table id="table_rbb_2xm_xq"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

An auto-generated number that identifies the move request record.

</td></tr><tr><td>

Priority

</td><td>

The priority that describes the importance of this request. By default, all requests are set to **4-Low**.

</td></tr><tr><td>

Move date

</td><td>

Select a date for the move request to be performed.

</td></tr><tr><td>

State

</td><td>

The state that describes what work stage this request is in. By default, all requests are set to **Open**.

</td></tr><tr><td>

Opened

</td><td>

Auto-filled with the date and time the request was opened.

</td></tr><tr><td>

Assignment group

</td><td>

Select the group from which an agent is assigned to the request. You can select only assignment groups associated with the service management application you are using.

**Note:** If you selected the **Use the dispatch queue** option on the Facilities Management Configuration screen, only users with the Dispatcher role can edit this field. If you did not select the **Use the dispatch queue** option, all users except those users with the Basic and Initiator roles can edit this field.

</td></tr><tr><td>

Requested by

</td><td>

The name of the requester.

</td></tr><tr><td>

Assigned to

</td><td>

Select the agent to assign the request to. If you already selected an assignment group, you can only select agents who belong to that group. If email notifications are enabled on your instance, a built-in email notification automatically sends an email to this user when you save the request record.

**Note:**

-   If you selected the **Use the dispatch queue** option on the Facilities Management Configuration screen, only users with the Dispatcher and Agent roles can edit this field. If you did not select the **Use the dispatch queue** option, all users except those users with the Basic and Initiator roles can edit this field.
-   If you selected an assignment group and want to assign the work to a new user, click the reference lookup icon next to **Assigned to**, click **New**, and create a user. Be aware, however, that you must navigate to **User Administration &gt; Groups** and add the user to the assignment group before the request can be assigned.


</td></tr><tr><td>

Template

</td><td>

\[Required\] The workflow template to be used for the fulfillment of this request.

</td></tr><tr><td>

Short description

</td><td>

\[Required\] A brief summary of the request. Optionally, you can click the search knowledge icon to view articles in the knowledge base relating to this product model, plan, or CI. Doing so could provide a solution related to the reason you are submitting this request.

</td></tr><tr><td class="sub-head" colspan="2">

Move Details

</td></tr><tr><td>

User to be moved

</td><td>

Select a name if you are opening this request on behalf of another user.

</td></tr><tr><td>

From location

</td><td>

The location from which the user is moved.

</td></tr><tr><td>

To location

</td><td>

The location to which the user is moved.

</td></tr><tr><td>

Requested move date

</td><td>

Select a date for the move request to be performed.

</td></tr><tr><td>

Boxes

</td><td>

Select this check box if the user requires that boxes be delivered before their move.

</td></tr><tr><td>

Security badge update

</td><td>

Select this check box if the user being moved requires changes in location access.

</td></tr><tr><td>

Move assets

</td><td>

Select this check box if the user being moved requires assets to be moved along with them.

</td></tr><tr><td class="sub-head" colspan="2">

Work Notes

</td></tr><tr><td>

Description

</td><td>

A detailed description of the request. The description is always visible to the submitter. Therefore, if you add or modify the description for a request that another user submitted, the user is able to see the changes.

</td></tr><tr><td>

Work notes

</td><td>

Extra notes that you want to share between users who can access the request form. A user who submits the request through the service catalog cannot see the work notes.

</td></tr></tbody>
</table>    **Note:** To specify an **Assignment group**, and assign the work to a user not in your user table, click the magnifying glass icon in the **Assigned to** field. Then click **New**, and create the user record. Be aware, however, that the new user is not recognized.

3.  Continue with one of the following options.

    |Option|Action|
    |------|------|
    |**To assign the move request to yourself**|Click **Assign to me**.|
    |**To initiate the workflow**|Click **Ready for Work**.|
    |**To save the form without initiating workflow**|Click **Save**.|


**Parent Topic:**[Facilities move requests](../concept/c_FacMoveRequests.md)


```


### File: service-management-for-the-enterprise\t_CreateReqFromAForwInbndEmail.md

```text
---
title: Create a request from a forwarded inbound email
description: Requests can be automatically created from the information in forwarded inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request creation using inbound email actions, Request creation, Request Management in a Service Management application, Service Management]
---

# Create a request from a forwarded inbound email

Requests can be automatically created from the information in forwarded inbound emails as long the functionality has been enabled on the configuration screen of SM application. The emails are also to be sent to a mailbox defined by criteria in the appropriate inbound email action.

## Procedure

1.  Navigate to **All** &gt; **System Policy** &gt; **Email** &gt; **Inbound Actions**.

2.  Select the inbound email action called **Create \[application name\] Request \(Forwarded\)**.

    The forwarded inbound email action record opens and displays the default conditions that trigger the inbound email action.

    When an email is forwarded to the mail list defined by the criteria in **Action**, a request is created with the following information:

    -   The **Contact type** is set to **Email**.
    -   The email sender \(if found\) populates the **opened\_by** and **Caller** fields for a newly created sm\_order based item.
    -   The email subject populates the **Short description** field.
    -   The email body populates the **Description** field.
    -   The email senders company \(Sender-&gt;Company\) populates the **Company** field.
    -   The email senders location \(Sender-&gt;Location\) populates the **Location** field.
    -   The entire email is copied into the **Work notes** field.
3.  You can use the email action as it is or modify it to meet the needs of your organization.


**Parent Topic:**[Request creation using inbound email actions](../reference/r_ReqCreateUseInboundEmailAct.md)


```


### File: service-management-for-the-enterprise\t_CreateReqWFacRequestForm.md

```text
---
title: Create a request with the facilities request form
description: Facilities staff members create requests using the Facilities Request form, allowing them to associate the request with a configuration item \(CI\), like printers or projectors.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Facilities request creation, Facilities requests, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a request with the facilities request form

Facilities staff members create requests using the Facilities Request form, allowing them to associate the request with a configuration item \(CI\), like printers or projectors.

## Before you begin

Role required: facilities\_admin

## About this task

Associating a CI to a request helps your facilities team understand which services have a negative impact by a facilities issue.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Requests** &gt; **Create New**.

2.  Fill in the fields on the form, as appropriate.

<table id="table_rbb_2xm_xq"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

An auto-generated number that identifies the request record.

</td></tr><tr><td>

Opened

</td><td>

Auto-filled with the date and time the request was opened.

</td></tr><tr><td>

Caller

</td><td>

The name of the requester.

</td></tr><tr><td>

Priority

</td><td>

The priority that describes the importance of this request. By default, all requests are set to 4-Low.

</td></tr><tr><td>

Affected CI

</td><td>

A CI affected by this request.

</td></tr><tr><td>

State

</td><td>

The state that describes what work stage this request is in. By default, all requests are set to **Open**.

</td></tr><tr><td>

Location

</td><td>

The location associated with this request. Verify that the location is correct. If it is not, you can select another location record.

</td></tr><tr><td>

Category

</td><td>

A category the request falls under.

</td></tr><tr><td>

Template

</td><td>

The template for creating this request \(optional\). Click the reference lookup icon and select a template. The request is populated with all fields in the selected template including all subtasks and part requirements \(if applicable\).

</td></tr><tr><td>

Initiated from

</td><td>

Indicates that an ITIL task is required.

</td></tr><tr><td>

Short description

</td><td>

\[Required\] A brief summary of the request. Optionally, you can click the search knowledge icon to view articles in the knowledge base relating to this product model, plan, or CI. Doing so could provide a solution related to the reason you are submitting this request.

</td></tr><tr><td>

Description

</td><td>

A detailed description of the request. The description is always visible to the submitter. Therefore, if you add or modify the description for a request that another user submitted, the user is able to see the changes.

</td></tr><tr><td>

Work notes

</td><td>

Extra notes that you want to share between staff members assessing the request form. **Note:** A user who submits the request through the service catalog cannot see the work notes.

</td></tr><tr><td>

Checklist

</td><td>

Provides a checklist of tasks that must be completed before the case is closed.Create a unique checklist for the case or task.

1.  Click the down arrow button and select **Create new**. Or, select from the list of previously created checklist templates.
2.  Add tasks in **Add Item**.
3.  Click the down arrow and select **Save as Template**.
4.  Enter a template name.
5.  Select a user group that can use the template \(optional\).


</td></tr></tbody>
</table>3.  Click **Save** from the **Form Context Menu** icon to save the request and remain on the **Facilities Request** form. The Related Links section appears.

    When an Affected CI has a warranty date in the future, the **Facilities Request Task** tab appears as a task to check the warranty information.

    ![Task form for a facilities request.](../image/WarrantyCheck.png)


**Parent Topic:**[Facilities request creation](../reference/r_FacilitiesRequestCreation.md)


```


### File: service-management-for-the-enterprise\t_CreateRequestTasks.md

```text
---
title: Create request tasks
description: Tasks are created in support of requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Request task management, Request Management in a Service Management application, Service Management]
---

# Create request tasks

Tasks are created in support of requests.

## Before you begin

Role required: \[SM application\]\_admin or \[SM application\]\_qualifier

## Procedure

1.  Navigate to **All** &gt; **\[SM Application\]** &gt; **Requests** &gt; **All \[SM Application\] Requests**.

2.  Open the request for which you want to create tasks.

3.  Click the **Add Task** related link.

    The Task screen for the SM application opens.

4.  Fill in the fields on the form.

    **Note:** Not all fields display for all SM applications.

<table id="table_ptc_455_cr"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

Auto-generated identification number for the task.

</td></tr><tr><td>

Parent

</td><td>

Request that this task is associated with.

</td></tr><tr><td>

Cloned from

</td><td>

Record number of the task this task was cloned from, if any.

</td></tr><tr><td>

Location

</td><td>

Geographical area where the work must be done. The location is critical for determining the staff member who is assigned to the task.

</td></tr><tr><td>

Template

</td><td>

Template for creating this request \(optional\). Click the lookup icon and select a template. The description of the selected template populates the **Description** field.

</td></tr><tr><td>

Skills

</td><td>

Abilities necessary to execute the task. This field is automatically completed based on the selection in the **Affected CI** field on the associated request. If you change the affected CI on the request, the system adds any skills required by the new CI to the skills already listed here.

</td></tr><tr><td>

State

</td><td>

Current state of the task, such as **Accepted** or **Closed Complete**. ServiceNow advances the state automatically as users complete the work for each successive state.

</td></tr><tr><td>

Assignment group

</td><td>

Group from which an individual legal staff member is selected to complete the task. The lookup list shows only the assignment groups associated with the selected **Location**. If the **Assignment Group** field is empty, the system searches for a group covering the territory that includes the location of the task.

</td></tr><tr><td>

Assigned to

</td><td>

Individual staff members who should complete the task, selected from the **Assignment group**. If you defined skills and assigned them to staff members, the **Assigned to** field lookup list shows only those staff members in the assignment group who have all the **Skills** required. If no exact match of skills is found, the lookup list shows all assignment group members. **Note:** If state flows are disabled, this field is not mandatory.

</td></tr><tr><td>

Short description

</td><td>

Brief explanation of the task.

</td></tr><tr><td>

Description

</td><td>

Exact technical description of the unit of work to be performed. Qualifiers should provide as much detail about the problem as possible to avoid extra communication with the caller in later stages of the request.

</td></tr><tr><td>

Work notes

</td><td>

Information about the task as it progresses through each state. Work notes are not visible to customers.

</td></tr></tbody>
</table>    **Note:** The workflow appears at the top of the form, with the completed states shown in green.


**Parent Topic:**[Request task management](../concept/c_RequestTasksMgmt.md)


```


### File: service-management-for-the-enterprise\t_DeleteABuilding.md

```text
---
title: Delete a building
description: Before deleting a building, delete any floors or levels defined for it.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Delete a building

Before deleting a building, delete any floors or levels defined for it.

## Before you begin

You must delete all the floors in a building before deleting the building itself.

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Building**.

2.  Click the name of the building you want to delete.

3.  Click **Delete**.

    If the building has any floors defined for it, a warning box opens and identifies the floors. Delete the floors before deleting the building.


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_DeleteACampus.md

```text
---
title: Delete a campus
description: Delete all buildings assigned to a campus, before deleting the campus itself.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Delete a campus

Delete all buildings assigned to a campus, before deleting the campus itself.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Campus**.

2.  Click the name of the campus you want to delete.

3.  Click **Delete**.

    **Note:** If the campus has any buildings defined for it, a warning box appears identifying those buildings. Delete the buildings before deleting the campus.


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_DeleteAFloorOrLevel.md

```text
---
title: Delete a floor or level
description: Before you can delete a floor, you must first delete any spaces defined for it.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Delete a floor or level

Before you can delete a floor, you must first delete any spaces defined for it.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Floor**.

2.  Click the name of the floor you want to delete.

3.  Click **Delete**.

    If the building has any assets associated with it, a warning box opens. If you click **Delete**, the associated asset is deleted.


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_DeleteASpace.md

```text
---
title: Delete a space
description: Spaces can be deleted from any floor or from another space as long as the space you want to remove does not have other spaces associated with it. For example, if you want to delete a space that contains several offices, those spaces must be deleted before the parent space can be deleted.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Delete a space

Spaces can be deleted from any floor or from another space as long as the space you want to remove does not have other spaces associated with it. For example, if you want to delete a space that contains several offices, those spaces must be deleted before the parent space can be deleted.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Space**.

2.  Click the name of the space you want to delete.

3.  Click **Delete**.

    If the space has any assets associated with it, or if the space is associated with another space, a warning box opens. If you click **Delete**, the associated asset or space is deleted.


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_DeleteAZone.md

```text
---
title: Delete a zone
description: When deleting a zone, any associated assets or spaces is also deleted.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Customer-created maps, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Delete a zone

When deleting a zone, any associated assets or spaces is also deleted.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Space Management** &gt; **Zone**.

2.  Click the name of the zone you want to delete.

3.  Click **Delete**.

    **Note:** If the space has any assets associated with it, or if the space is associated with another space, a warning box opens. If you click **Delete**, the associated asset or space is deleted.


**Parent Topic:**[Customer-created maps](../reference/r_Manually-builtMaps.md)


```


### File: service-management-for-the-enterprise\t_EditAZone.md

```text
---
title: Edit a zone
description: Facilities administrators and staff can edit existing zones from the Zones tab within the workbench.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Workbench, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Edit a zone

Facilities administrators and staff can edit existing zones from the Zones tab within the workbench.

## Before you begin

Role required: facilities\_staff

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Workbench**.

2.  On the Zones tab, click **Edit**.

3.  Select a zone from the choice list.

    The spaces belonging to that zone are shown on the floor plan, highlighted in blue.

4.  Continue with one of the following options.

<table id="choicetable_WorkbenchAccess"><thead><tr><th align="left" id="d37529e96">

Option

</th><th align="left" id="d37529e99">

Action

</th></tr></thead><tbody><tr><td id="d37529e105">

**To remove a space from the zone**

</td><td>

Click a space within the zone. **Note:** The space turns red indicating that it will be removed when the update is applied.

</td></tr><tr><td id="d37529e117">

**To add a space to the zone**

</td><td>

Click a space outside the zone. **Note:** The space turns green indicating that it will be added when the update is applied.

</td></tr></tbody>
</table>5.  You can select other floors, buildings, and campuses while making edits to a zone.

    ![In this figure, a facilities map image displays a building floor and its designated spaces.](../image/CampusFloorSelection.png)

6.  When finished making edits, click **Apply edits**.


**Parent Topic:**[Facilities Workbench](../concept/c_FacilitiesWorkbench.md)


```


### File: service-management-for-the-enterprise\t_FindASpaceOrUser.md

```text
---
title: Find a space or user
description: All users in your organization, regardless of their role, can search for other users and spaces. The results are ordered by current level or floor, current campus, and other campuses.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Find a space or user

All users in your organization, regardless of their role, can search for other users and spaces. The results are ordered by current level or floor, current campus, and other campuses.

## Before you begin

Role required: none

## About this task

## Procedure

1.  Perform one of the following options.

    |Type of user|Action|
    |------------|------|
    |**User**|Navigate to **Self-Service** &gt; **Floor Pan**.|
    |**Facility role**|Navigate to **Facilities** &gt; **Workbench**.|

2.  Select **User/Space** in the search criteria box.

3.  To help narrow your search results, you can select the campus, building, and floor number for your search.

    **Note:** The facilities administrator configures the number of search results returned. See [Facilities visualization workbench configuration](../reference/r_WorkbenchConfiguration.md).

    ![In this figure, a facilities map image displays a building floor and its designated spaces.](../image/CampusFloorSelection.png)

4.  On the Spaces tab, enter the user's name or space name in the search field.

5.  Press the Enter key to submit your search criteria.

    Search results are returned in the following order:

    -   Current Level
    -   Other in Campus
    -   Other Campuses
6.  Perform one of the following options.

<table id="choicetable_dm3_syy_nt"><thead><tr><th align="left" id="d32682e205">

Result

</th><th align="left" id="d32682e208">

Action

</th></tr></thead><tbody><tr><td id="d32682e214">

**To see the space or user details**

</td><td>

Click the link for the space or user. The details for that user or space open in a separate form.

 **Note:** If the location is a space, users and facilities staff can create facilities requests from the room information. See [Create a facility request from the floor plan](t_CreateFacReqWorkbench.md).

</td></tr><tr><td id="d32682e237">

**To see the location of the space or user on the floor plan**

</td><td>

Click the pin ![Pin icon shows location on floor plan.](../image/PinIcon.png) icon, beside the link for the user or space.

</td></tr></tbody>
</table>

```


### File: service-management-for-the-enterprise\t_FindAssetorCI.md

```text
---
title: Find an asset or CI
description: All users in your organization, regardless of their role, can search for assets and CIs. The results are ordered by current level or floor, current campus, and other campuses.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Find an asset or CI

All users in your organization, regardless of their role, can search for assets and CIs. The results are ordered by current level or floor, current campus, and other campuses.

## Before you begin

Role required: none

## About this task

## Procedure

1.  Perform one of the following options.

    |Type of user|Action|
    |------------|------|
    |**User**|Navigate to **Self-Service** &gt; **Floor Pan**.|
    |**Facility role**|Navigate to **Facilities** &gt; **Workbench**.|

2.  Select **Asset/CI** in the search criteria box.

3.  To help narrow your search results, you can select the campus, building, and floor number for your search.

    **Note:** The facilities administrator configures the number of search results returned. See [Facilities visualization workbench configuration](../reference/r_WorkbenchConfiguration.md).

    ![In this figure, a facilities map image displays a building floor and its designated spaces.](../image/CampusFloorSelection.png)

4.  On the Spaces tab, enter the asset or CI in the search field.

5.  Press the Enter key to submit your search criteria.

    Search results are returned in the following order:

    -   Current Level
    -   Other in Campus
    -   Other Campuses
6.  Perform one of the following options.

<table id="choicetable_dm3_syy_nt"><thead><tr><th align="left" id="d25822e180">

Result

</th><th align="left" id="d25822e183">

Action

</th></tr></thead><tbody><tr><td id="d25822e189">

**To see the asset or CI details**

</td><td>

Click the link for the asset or CI. The details for that asset or CI open in a separate form.

</td></tr><tr><td id="d25822e201">

**To see the location of the asset or CI on the floor plan**

</td><td>

Click the pin ![pin icon](../image/PinIcon.png) icon, beside the link for the asset or CI.

</td></tr></tbody>
</table>
**Parent Topic:**[Interactive facility maps](../concept/c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\t_FindFacilitesRequest.md

```text
---
title: Find a facilities request
description: Facilities administrators can locate and manage requests from the Requests tab within the workbench.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Workbench, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Find a facilities request

Facilities administrators can locate and manage requests from the Requests tab within the workbench.

## Before you begin

Role required: facilities admin

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Workbench**.

2.  To help narrow your search results, you can select the campus, building, and floor number for your search.

    **Note:** The facilities administrator configures the number of search results returned. See [Facilities visualization workbench configuration](../reference/r_WorkbenchConfiguration.md).

    ![Campus and floor selection](../image/CampusFloorSelection.png)

    By default, facilities administrators can see all requests for the selected level displayed in the right side pane. Red pins \(![red pin icon shows where facilities requests for floor plan.](../image/RequestPin.png)\) depict those requests on the floor plan.

3.  Continue with one of the following options.

<table id="choicetable_WorkbenchAccess"><thead><tr><th align="left" id="d36525e127">

Option

</th><th align="left" id="d36525e130">

Action

</th></tr></thead><tbody><tr><td id="d36525e136">

**To see all requests assigned to you**

</td><td>

Select **Assigned to me** check box.

</td></tr><tr><td id="d36525e148">

**To search for a request**

</td><td>

1.  On the Requests tab, enter the request number or the name of the user who made the request.
2.  Press the Enter key to submit your search criteria.


</td></tr></tbody>
</table>    Search results are returned in the following order:

    -   Current Level
    -   Other in Campus
    -   Other Campuses
4.  Continue with one of the following options.

    |Option|Action|
    |------|------|
    |**To see request details**|Click the request number.|
    |**To see tasks associated with a request**|Click the task number under the request.|
    |**To see the location on the floor plan**|Click the pin \( ![Pin icon that shows a location on floor plan.](../image/PinIcon.png)\) icon.|


**Parent Topic:**[Facilities Workbench](../concept/c_FacilitiesWorkbench.md)


```


### File: service-management-for-the-enterprise\t_FindMoveRequest.md

```text
---
title: Find a move request
description: Facilities and move staff can locate and manage move requests from the Moves tab within the workbench.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Facilities Workbench, Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Find a move request

Facilities and move staff can locate and manage move requests from the Moves tab within the workbench.

## Before you begin

Role required: move\_basic

## About this task

The Move tab is only visible when the Facilities Move Management plugin \(com.snc.facilities\_service\_automation.move\) has been activated.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Workbench**.

2.  To help narrow your search results, you can select the campus, building, and floor number for your search.

    **Note:** The facilities administrator configures the number of search results returned. See [Facilities visualization workbench configuration](../reference/r_WorkbenchConfiguration.md).

    ![Campus and floor selection](../image/CampusFloorSelection.png)

    By default, facilities administrators can see all move requests for the selected level displayed in the right side pane. Yellow pins \(![move request icon](../image/MoveRequestPin.png)\) depict those request locations on the floor plan.

3.  Continue with one of the following options.

<table id="choicetable_WorkbenchAccess"><thead><tr><th align="left" id="d31100e130">

Option

</th><th align="left" id="d31100e133">

Action

</th></tr></thead><tbody><tr><td id="d31100e139">

**To see all move requests assigned to you**

</td><td>

Select **Assigned to me** check box.

</td></tr><tr><td id="d31100e151">

**To search for a move request**

</td><td>

1.  On the Moves tab, enter the move request number, the name of the user to be moved, or the name of the user who made the request.
2.  Press the Enter key to submit your search criteria.


</td></tr></tbody>
</table>    Search results are returned in the following order:

    -   Current Level
    -   Other in Campus
    -   Other Campuses
4.  Continue with one of the following options.

<table id="choicetable_swj_2jx_mt"><thead><tr><th align="left" id="d31100e193">

Option

</th><th align="left" id="d31100e196">

Action

</th></tr></thead><tbody><tr><td id="d31100e202">

**To see move request details**

</td><td>

Click the move request number.

</td></tr><tr><td id="d31100e211">

**To edit the From or To space**

</td><td>

1.  Click the edit \(![edit icon](../image/EditIcon.png)\) icon beside the **From:** or **To:** field.
2.  Click a space on the floor plan to change its location.
3.  Click the save \(![save icon](../image/SaveIcon.png)\) icon.


</td></tr><tr><td id="d31100e250">

**To see the location on the floor plan**

</td><td>

Click the pin \(![pin icon](../image/PinIcon.png)\) icon.

</td></tr></tbody>
</table>
**Parent Topic:**[Facilities Workbench](../concept/c_FacilitiesWorkbench.md)


```


### File: service-management-for-the-enterprise\t_FindSpaceUserMobile.md

```text
---
title: Find a space or user on a mobile interface
description: Quickly find a conference room, office, cubicle, or another employee in your organization on a mobile interface.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Find a space or user on a mobile interface

Quickly find a conference room, office, cubicle, or another employee in your organization on a mobile interface.

## Before you begin

Role required: none

## Procedure

1.  Tap the ![double chevron icon](../image/ExpandArrows.png) icon to expand the side tab.

2.  In the **User/Space search** field on the Spaces tab, enter the search criteria and tap **return**.

    Matching users and spaces are listed by current level, campus, and other campuses.

    ![In this figure, the user has entered Tiber in the search field. A space named Tiber is located in Building B - Floor 4.](../image/SearchResults.png)

3.  Perform one of the following options.

    |Result|Action|
    |------|------|
    |**To see the space or user details**|Tap the link for the space or user.|
    |**To see the location of the space or user on the floor plan**|Tap the pin ![pin icon](../image/PinIcon.png) icon, beside the link for the user or space.|


**Parent Topic:**[Interactive facility maps](../concept/c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\t_ManAssignAgtToActSMReq.md

```text
---
title: Manually assign agents to active requests
description: Use this procedure to assign agents to active requests in service management \(SM\) applications.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Agent assignment methods, Request Management in a Service Management application, Service Management]
---

# Manually assign agents to active requests

Use this procedure to assign agents to active requests in service management \(SM\) applications.

## Procedure

1.  Navigate to one of the following modules:

    -   **\[SM application\]** &gt; **Open - Unassigned** for a list of requests that no one is assigned to.
    -   **\[SM application\]** &gt; **All \[SM application\] Requests** for a list of all open requests, regardless of their current assignment.
2.  Open the request you want to assign.

3.  In the **Assignment group** field, enter the group that handles this kind of request.

    If no groups are available, leave this field blank. To look up the assignment group, click the reference lookup icon \(![Lookup icon](../image/IconReferenceLookup.png)\) beside the **Assignment group** field.

    **Note:** You do not have to select an assignment group, but doing so limits the users you can assign the request to.

4.  In the **Assigned to** field, enter the agent to handle this request.

    To look up an agent, click the lookup icon \(![Lookup icon.](../image/IconReferenceLookup.png)\) beside the **Assigned to** field.

    **Note:** If one was selected, the users in the search results are limited to the users in the **Assignment group**.

5.  Click **Update**.

    An email notification is automatically sent to the assigned agent when email notifications are set up for the instance.


**Parent Topic:**[Agent assignment methods](../../service-management-core/concept/c_AgentAssignment.md)


```


### File: service-management-for-the-enterprise\t_MigFacDataToNewSpaceDefTable.md

```text
---
title: Migrate facilities data to new space definition tables
description: To continue using the image-based floor plans with the new space definition, migrate your data from the old tables to the new space definition tables.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Activate Facilities Visualization Workbench, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Migrate facilities data to new space definition tables

To continue using the image-based floor plans with the new space definition, migrate your data from the old tables to the new space definition tables.

## Before you begin

Role required: facilities\_admin

## About this task

The migration process only migrates complete data. A space that is not in a level or a level not in a building is not migrated. This behavior can be changed by updating the migration script include. Floors that are not connected to a building are not migrated, nor are spaces that are not part of a floor or building. As part of the migration process, the legacy spaces, floors, and buildings are marked as migrated.

The migration path for the old tables to the new are:

-   \[cmn\_building\] migrates to \[alm\_building\]
-   \[fpv\_floor\] migrates to \[fm\_level\]
-   \[fpv\_element\] migrates to \[fm\_space\]

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Administration** &gt; **Migrate**.

2.  Click **Migrate**.


## Result

The following results can be expected:

-   Data is migrated to the new facilities management tables for buildings, floors, and spaces.
-   After a building, floor, or space is migrated, it is marked as migrated, and is not able to be migrated again.

    **Note:** Any object that is marked as migrated does not get migrated again, so you can safely run through the migration process multiple times without creating duplicated objects in the space tables. This behavior can be modified in the migration script include or by resetting the migration flag on the original objects.


**Parent Topic:**[Activate Facilities Visualization Workbench](../../facilities-interactive-facility-maps/task/t_ActivateFacVisWorkbench.md)


```


### File: service-management-for-the-enterprise\t_PlanScenarioMPT.md

```text
---
title: Plan a move scenario
description: Facilities administrators create move scenarios when planning and executing large-scale moves. When people are added to the scenario, move\_detail records are created. These records contain all the information about the potential move for a specific person, such as the reference to the sys\_user, destination floor, and destination building.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Enterprise move scenarios, Move planning tool, Enterprise move, Facilities move management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Plan a move scenario

Facilities administrators create move scenarios when planning and executing large-scale moves. When people are added to the scenario, move\_detail records are created. These records contain all the information about the potential move for a specific person, such as the reference to the sys\_user, destination floor, and destination building.

## Before you begin

Role required: move\_agent or facilities\_staff

## Procedure

1.  Navigate to **All** &gt; **Enterprise Move** &gt; **Move Planning Tool**.

2.  Click **Create New Scenario**.

3.  Fill in the fields on the form, as appropriate.

    |Field|Description|
    |-----|-----------|
    |Name|Provide a name for the scenario.|
    |Notes|Enter additional information about the move that you feel is important for the facilities staff to know.|

4.  Click **Submit**.

5.  On the right-side pane, on the Scenarios tab, select the campus this move applies to.

    Occupancy totals for the campus you selected are displayed per floor in bar charts, showing how many seats are assigned to a department or manager. The total number of open seats are shown also.

6.  Click the Planning tab, and select the **User Manager** or **User Department** view.

    **Note:** User Department refers to the department of the user \(sys\_user\) that is sitting there. It is not showing the department that is assigned the space.

7.  Select the manager or department on the floor bar chart.

8.  Click a highlighted segment on one of the floors.

9.  Fill in the fields on the form, as appropriate.

<table id="table_kmr_lvg_x5"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Destination building

</td><td>

The building you are moving employees to.**Note:** If no building or floor is specified, the user is moved to the Lounge.

</td></tr><tr><td>

Destination level

</td><td>

The floor you are moving employees to.

</td></tr><tr><td>

Move group

</td><td>

Enter a name for the group you are planning to move.**Note:** Use a unique name to identify a group. After clicking **Submit**, the group name is saved and can be used again.

</td></tr><tr><td>

Move delegator

</td><td>

The person responsible for assigning users to open spaces in a scenario. Refer to [Activate a delegator](t_ActivateADelegator.md).

</td></tr></tbody>
</table>10. To add or delete users in this scenario, click the arrow to expand the **Users** tab.

11. Select users and click **Add Users to Scenario**.

    Users added to the scenario are shown in the pending assignments in the floor details.

    ![In this figure, the users have been added to the move scenario and show as pending on the floor to which they have been assigned.](../image/AddUsersScenarios.png "Pending assignment")


-   **[Lounge](../concept/c_Lounge.md)**  
When a facilities administrator sets up a move scenario without specifying the destination building or floor, the users are moved to the lounge.

**Parent Topic:**[Enterprise move scenarios](../reference/r_EnterMoveScenarios.md)


```


### File: service-management-for-the-enterprise\t_ProcessMapFiles.md

```text
---
title: Process GeoJSON map files
description: Processing GeoJSON map files includes parsing data from a map and importing that information to the campus space management tables. Use this process to set up your spaces or update bulk changes to your campus without having to enter each change manually.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [GeoJSON map files, Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Process GeoJSON map files

Processing GeoJSON map files includes parsing data from a map and importing that information to the campus space management tables. Use this process to set up your spaces or update bulk changes to your campus without having to enter each change manually.

## Before you begin

Role required: facilities\_admin

## About this task

To process the files properly:

-   Include the area file in the map set and follow the proper naming convention \(`-area-geom-`\)
-   Set the **facilities.management.fvw.geojson.space.area.parsing** property to true

## Procedure

1.  Navigate to **All** &gt; **Space Management** &gt; **Campus**.

2.  Click the name of the campus.

3.  Click the **Facilities Map Sets** related list to see all the maps sets associated with this campus.

4.  Click the name of the map set you want to parse.

    All files associated with that map set are shown as attachments.

5.  Click **Process the Map Files** related link.

    All the files that will be read and parsed \(processed\) are shown.

6.  Click **Preview**.

    A summary of all the spaces that will be created are shown.

    |Field|Description|
    |-----|-----------|
    |Summary|The total for each space that will be added or retired: buildings, levels, spaces|
    |Facility space creation|
    |Feature type|All the types of spaces that will be created|
    |Class name| |
    |Creating|The total amount of each space type that will be created.|
    |Existing|The existing amount of each space type.|
    |Ignoring|The amount of each space type that not is created.|
    |Icon Creation|
    |Icon|The names of all icons that will be included within this campus.|
    |Parsing label|The parsing label of all icons that will be included within this campus.|
    |Creating|The total number of that icon type that will be created for this campus.|
    |Existing|The total number of that icon type that already exists within this campus.|

7.  Review the process map set summary carefully, to be sure if the space adds and ignores make sense.

    If the summary does not make sense, refer to the \[fm\_facility\_feature\] table.

8.  Click **Process**.

    A summary of all spaces created is displayed when the map file has been processed.


**Parent Topic:**[GeoJSON map files](../reference/r_GeoJSONMapFiles.md)


```


### File: service-management-for-the-enterprise\t_ReEnableStateFlows.md

```text
---
title: Re-enable state flows
description: When service management state flows have been disabled, they cannot be re-enabled from the user interface.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Implications of disabling SM state flows, Service management states, Service Management]
---

# Re-enable state flows

When service management state flows have been disabled, they cannot be re-enabled from the user interface.

## About this task

State flows can, however, be re-enabled by running a script for each service management application.

## Procedure

1.  For each service management application, run the following script:

    ```
    var now_GR = new GlideRecord(‘sm_config’);
     gr.get(‘name’, ‘{YOUR_APP_NAME}’); //this can be looked up by navigating to 
     the sm_config list
     gr.use_sf = true;
     gr.update();
    ```


**Parent Topic:**[Implications of disabling SM state flows](../concept/c_ImpDsblStFl.md)


```


### File: service-management-for-the-enterprise\t_RunTransform.md

```text
---
title: Run transform to update data
description: Running a transform exports information from your records into an .xls file. That data can be imported into the ServiceNow space management application.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Space management, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Run transform to update data

Running a transform exports information from your records into an .xls file. That data can be imported into the ServiceNow space management application.

## Before you begin

Role required: admin

## About this task

An example transform map is included with the demo data. Load the demo data on a pre-production instance, go to campuses, and select the **Westfield Valley Fair** campus. Open the Westfield**Valley Fair V262-259** map set. Use the **westfield\_transform\_example.xls** file as an example. Process the campus, then run the transform.

## Procedure

1.  Navigate to **All** &gt; **System Import Sets** &gt; **Run Transform**.

2.  Click **Create and load an import set first**.

3.  Fill in the fields on the form, as appropriate.

<table id="table_ing_z2n_lt"><thead><tr><th>

Option

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Import set table

</td><td>

Selections are create table or existing table.

</td></tr><tr><td>

Label

</td><td>

Enter a label for the new table.**Note:** This field depends on the **Create table** option being selected.

</td></tr><tr><td>

Name

</td><td>

The name is automatically generated from the **Label** you enter. **Note:** This field depends on the **Create table** option being selected.

</td></tr><tr><td>

Import set table

</td><td>

All saved import set tables are listed in a list.**Note:** This field depends on the **Existing table** option being selected.

</td></tr><tr><td>

Source of the import

</td><td>

Selections are file or data source.

</td></tr><tr><td>

File

</td><td>

Browse to the location of the file.**Note:** This field depends on the **File** option being selected.

</td></tr><tr><td>

Sheet number

</td><td>

Identifies the sheet number used for the transform.**Note:** This field depends on the **File** option being selected.

</td></tr><tr><td>

Header row

</td><td>

Identifies the row number used as the header row in the transform file.**Note:** This field depends on the **File** option being selected.

</td></tr><tr><td>

Data source

</td><td>

All data sources are listed in a list.

</td></tr></tbody>
</table>4.  Click **Submit**.

5.  Click **Run transform**.

6.  Click **Transform**.

    All the spaces are populated in space management from the space details in the transform map.

7.  Navigate to **Space Management** &gt; **Spaces**

8.  Review all space details to be certain all extra details were imported.


-   **[Transform map](../concept/c_TransformMap.md)**  
A transform map is an .xls file that allows you to add spaces or details about spaces from other sources into the space management application.

**Parent Topic:**[Space management](../reference/r_SpaceManagement.md)


```


### File: service-management-for-the-enterprise\t_ShowAnyTaskOnMap.md

```text
---
title: Show any task on a map
description: Custom tables that are extended from task can be created, shown, and managed on the interactive map. The location field on the task, must be a mappable space \(fm\_space\). There are some location fields on task that may have a reference qualifier that does not allow fm\_space be used.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Interactive facility maps, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Show any task on a map

Custom tables that are extended from task can be created, shown, and managed on the interactive map. The location field on the task, must be a mappable space \(fm\_space\). There are some location fields on task that may have a reference qualifier that does not allow fm\_space be used.

## Before you begin

Role required: facilities\_admin to edit, create, delete records

-   Check that the location of the task is mappable \(fm\_space\).
-   Check that the reference qualifier on the location field allows fm\_space.

## Procedure

1.  Navigate to **All** &gt; **Facilities** &gt; **Workbench Configuration** &gt; **Map Tasks**

2.  Click **New**.

    All the items that extend the task are available.

3.  Do one of the following actions:

<table id="choicetable_lmr_1x2_bv"><tbody><tr><td id="d21679e89">

**To show the task on the map**

</td><td>

Set **Show task** to true

</td></tr><tr><td id="d21679e101">

**To hide the task from the map**

</td><td>

Set **Show task** to false

</td></tr></tbody>
</table>    These tasks display on the Task tab on the map.

    ![In this figure, there is a Task tab, with four requests on the current level.](../image/TaskTab.png "Tasks Tab")


**Parent Topic:**[Interactive facility maps](../concept/c_InteractiveFacilityMaps.md)


```


### File: service-management-for-the-enterprise\t_StateFlowDictionaryOverrides.md

```text
---
title: State flow dictionary overrides
description: A dictionary override in a state flow defines the starting state for all new records in a specific table. You set an override in tables that extend a base table only, so that your customizations are applied only to the extended table.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# State flow dictionary overrides

A dictionary override in a state flow defines the starting state for all new records in a specific table. You set an override in tables that extend a base table only, so that your customizations are applied only to the extended table.

## Before you begin

Role required: admin

## Procedure

1.  In a state flow record, select an **Ending state**.

    This is the override value which becomes the starting state for all new records in the table named.

2.  Click **Create Default Value**.

    The system populates the **Dictionary override** field with a value of state, which is the field in the task table affected by the override. The Dictionary override field is read-only. After the override is created, the system hides the **Create Default Value** button on all subsequent state flow forms for that table.


**Parent Topic:**[State flow customization](../concept/c_StateFlowCustomization.md)


```


### File: service-management-for-the-enterprise\t_StateFlowExample.md

```text
---
title: State flow example
description: Your business processes might require work order tasks to be accepted automatically when dispatched to an agent.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service management states, Service Management]
---

# State flow example

Your business processes might require work order tasks to be accepted automatically when dispatched to an agent.

## Before you begin

Role required: admin

## About this task

Create a new state flow record that automates the transition from Pending Dispatch to Accepted and bypasses the Assigned state in which agents can reject tasks. This prevents the system from running the manual script associated with UI actions. The automatic script performs the jobs that the manual script performed, such as updating the date and time the task was dispatched, or to do additional work such as sending a notification.

## Procedure

1.  Navigate to **All** &gt; **Field Service** &gt; **State Flows** &gt; **Work Task Flows**.

2.  Open the **Assigned** record that defines a task transition from a starting state of **Pending Dispatch** to an ending state of **Assigned**.

    This is an automatic state change that occurs when an agent's name is added to the Assigned to field and the task is updated.

3.  Change the name of the state flow.

    In this example, change the name to **Skip Agent Acceptance**.

4.  Change the value in the **Ending state** field to **Accepted**.

    This transition allows you to bypass the **Accept** state flow record that enables agents to reject tasks.

5.  Set up the condition criteria in the following fields:

    -   **Automatic condition string**: This condition ensures that the current state is at **Pending Dispatch** and the value in the **Assigned to** field changes. For example, `current.state == 10 && current.assigned_to.changes()`.
    -   **Automatic condition**: The condition **\[Assigned to\] \[is not empty\]**ensures that all dispatched tasks are accepted automatically.
    -   **Automatic script**:\] The automatic script sets the time the task was dispatched. For example, use method: `current.dispatched_on = gs.nowDateTime();`.
    **Note:** The previous two condition statements have an **\[and\]** relationship. In this example, the business rule runs when a task in a state of **Pending Dispatch** is assigned to any agent.

6.  Copy the record using the **Insert and Stay** command.

    This action increments the record number and clears the **Business rule** field. The system automatically creates a new business rule, using the name of the new state flow record. The Skip Agent Acceptance business rule moves the task from **Pending Dispatch** to **Accepted** automatically when a dispatcher enters a user name in the **Assigned to** field. Note that any changes you make to this state flow record in the future are executed by this business rule.

7.  Ensure that the **Active** check box is selected.

8.  In the Work Task Flows list, locate the **Accept** state flow record and change the **Active** status to **false**.

    This action deactivates the transition that allows agents to accept tasks and moves the state flow directly from **Pending Dispatch** to **Accepted**.


**Parent Topic:**[Service management states](../concept/c_ServiceManagementStates.md)


```


### File: service-management-for-the-enterprise\t_TriggerEventsOnStateChanges.md

```text
---
title: Trigger events on state changes
description: You can configure a state flow to trigger a registered system event when a task transitions from a starting state to a specified end state. For example, you can use events to trigger email notifications and create script actions.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [State flow customization, Service management states, Service Management]
---

# Trigger events on state changes

You can configure a state flow to trigger a registered system event when a task transitions from a starting state to a specified end state. For example, you can use events to trigger email notifications and create script actions.

## Before you begin

Role required: admin

## About this task

You can configure a state flow to trigger a registered system event when a task transitions from a starting state to a specified end state. For example, you can use events to trigger email notifications and create script actions. When you attach an event to a state flow, the ServiceNow system creates a business rule called **State Flow Events for &lt;table name&gt;** for the table specified in the state flow. If you specify a start and end state, the business rule executes when the record transitions from the start state to the end state. If the state flow only specifies an end state, the business rule executes whenever that end state is reached. The system creates one business rule for all state flows containing events on a single table. When all events or all state flows on a table are deleted, the system deletes the business rule.

To create an event that fires when a work order task moves from a starting state of **Work in Progress** to an end state of **Closed Complete**:

## Procedure

1.  Register a new event on the Work Order Task \[wm\_task\] table called `task.closed`.

2.  Navigate to **State Flows** **Work Task Flows**.

3.  Open the state flow record **Close Complete**.

4.  Select `task.closed` in the **Event** field and save your changes.

    The ServiceNow system automatically creates a business rule called **State Flow Events for wm\_task**.


**Parent Topic:**[State flow customization](../concept/c_StateFlowCustomization.md)


```


### File: service-management-for-the-enterprise\t_UpdateARequestFromAnInboundEmail.md

```text
---
title: Update a request from an inbound email
description: Requests can be automatically updated from the information in inbound email replies as long the functionality has been enabled on the SM application's configuration screen. The emails must also be sent to a mailbox defined by criteria in the appropriate inbound email action.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Request creation using inbound email actions, Request creation, Request Management in a Service Management application, Service Management]
---

# Update a request from an inbound email

Requests can be automatically updated from the information in inbound email replies as long the functionality has been enabled on the SM application's configuration screen. The emails must also be sent to a mailbox defined by criteria in the appropriate inbound email action.

## Procedure

1.  Navigate to **All** &gt; **System Policy** &gt; **Email** &gt; **Inbound Actions**.

2.  Navigate to the inbound email action called **Update \[application name\] Request** and click its **Name**.

    The update inbound email action record opens and displays the default conditions that trigger the inbound email action.

    When an email reply is received in the mail list defined by the criteria in the email action, the associated request is opened and update information is added to the **Work notes** field.

3.  You can use the email action as is or modify it to meet the needs of your organization.


**Parent Topic:**[Request creation using inbound email actions](../reference/r_ReqCreateUseInboundEmailAct.md)


```


### File: service-management-for-the-enterprise\t_UseTaskTempForMultReqTemp.md

```text
---
title: Create a task template for common task requests
description: If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Facilities request tasks, Facilities service management process, Facilities Service Management overview, Facilities Service Management, Service Management]
---

# Create a task template for common task requests

If you have tasks that are often repeated across multiple jobs, you can create and reuse a task template in multiple request templates. You can also use it on a Work order request to pull common and repeatable information into a request.

## Before you begin

Role required: wm\_admin

Create a request template and an associated task template that contains the information you want to reuse.

**Note:** Checklist templates are a way to populate a checklist of tasks to be completed. Checklist templates are created on a Work order request or on a Work order task. After being created, they can be saved as a template and be reused.

When you create subsequent request templates, you can select the task template from the **Task Template** field and save the file.

## About this task

A work order outlines the entire request or process. A work order task are the detailed steps for the parent work order. Every work order needs at least one work order task to get assigned to a specific agent to finish that step. Every work order task must have a parent work order to track the request.

Sometimes work orders are opened with the same purpose, and these work orders should have similar flows and similar work order tasks. A work order template can be used to fill in some fields in the work order, and create work order tasks.

The difference between a work order template and task template is you can’t create a task template alone, it must be part of the work order template. Creating a task template is a step of creating a work order template since you can define tasks and task templates for a work order or work order template.

With request tasks, work order tasks are not required, though they can be used. Request task management gives you the ability to split a request into multiple tasks. This document, Create a task template for common request tasks, describes the ability to use the work order task templates to apply them to common or repeated requests that you might have.

## Procedure

1.  Navigate to **All** &gt; **Field Service** &gt; **Catalog &amp; Knowledges** &gt; **Work Order Templates**.

2.  Select **New** and enter the following information.

    |Field|Description|
    |-----|-----------|
    |Name|A descriptive name for the Work order Template.|
    |Short description|A short description of the template.|
    |Description|A detailed description of the template.|
    |Checklist template|A Checklist template saved from the Work Order Request Form.|

3.  Select **Add Task**.

4.  Select **Copy Task Template** to use a previously created template, or enter the following information.

    |Field|Description|
    |-----|-----------|
    |Task type|The type of task being requested.|
    |Name|Descriptive name of the task.|
    |Description|Detailed description of the task.|
    |Parts and quantities|What parts and how many are needed to complete the task.|
    |Dispatch group|The dispatch group to assign the task to.|
    |Depends on|Indicates if the task depends on another task. For example, if you have two tasks, you can make task 2 dependent on task 1 completing before task 2 can start.|
    |Checklist template|A Checklist template saved from the Work order Request Form.|
    |Work type|The type of work being performed during the task.|

5.  Select **Submit**.


**Parent Topic:**[Facilities request tasks](../concept/c_FacRequestTasks.md)

**Parent Topic:**[Request task management](../concept/c_RequestTasksMgmt.md)


```


---

## Folder: service-management-for-the-enterprise\planned-maintenance-family



### File: service-management-for-the-enterprise\planned-maintenance-family\c_ChangesToMaintSched.md

```text
---
title: Changes to maintenance schedules
description: If you make and save changes to an existing maintenance schedule, any previously associated records are updated accordingly.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure a maintenance schedule, Managing maintenance plans, Planned Maintenance, Service Management]
---

# Changes to maintenance schedules

If you make and save changes to an existing maintenance schedule, any previously associated records are updated accordingly.

The following examples explain the types of behavior you can expect after making changes:

-   If you change a schedule from a duration-based to a meter-based schedule, the next run time is cleared and the associated records are populated with a next run value instead.
-   If the **Every** field is changed on a meter-based schedule, the next run value is updated based on the existing Last Run Value, or from the current value of the asset if no last run value exists.
-   If you change the **Field** value for a meter-based schedule, the records associated with the schedule have their next run values recalculated based on the new **Field** value.
-   For Interval-based schedules, changing from one **Trigger type** to another updates the next run time based on the existing **Last Run Time** value, or from **Now** if no last run time exists.

**Parent Topic:**[Configure a maintenance schedule](../task/t_DefineAMaintSched.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\c_MaintPlanMgmt.md

```text
---
title: Managing maintenance plans
description: Planned Maintenance allows you to create, maintain, and schedule maintenance for equipment that requires regular maintenance.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Planned Maintenance, Service Management]
---

# Managing maintenance plans

Planned Maintenance allows you to create, maintain, and schedule maintenance for equipment that requires regular maintenance.

The maintenance plan specifies the CI class, product model, or other criteria, such as location, and specifies the maintenance to be performed. The maintenance schedule specifies the timing, by specifying how often and when to perform the maintenance.

For example, you can configure a maintenance plan to inspect and clean all air conditioners for a particular product model. The maintenance schedule specifies that the inspection is performed every six months.

Maintenance plans and schedules also take into consideration service management work orders and facilities requests opened against that equipment.

## Timing the first maintenance

By default, the first planned maintenance is scheduled based on the timing entered in the schedule. For example, if you create a schedule to inspect the air conditioners every six months, the first maintenance occurs six months from the time that you created the schedule.

To schedule the date of the first maintenance:

1.  Navigate to the Maintenance Schedule form.
2.  Click the **Run on demand** related link.
3.  De-select the **Run now** field.
4.  In the **Select next run date** field, use the calendar to select the desired date.
5.  Save the date.
6.  Click **Schedule**. This updates the next run time for the maintenance plan records.

You can update any maintenance schedule as needed. For example, if the regular interval is due next month, you can select an earlier or later date to change when the maintenance occurs.

-   **[Create a maintenance plan](../task/t_CreateAMaintPlan.md)**  
When creating a maintenance plan, options on the form help to determine how and when maintenance should be performed.
-   **[Property settings for Planned Maintenance](../reference/planned-maint-properties.md)**  
You configure Planned Maintenance properties at **Planned Maintenance** &gt; **Properties**.
-   **[Configure a maintenance schedule](../task/t_DefineAMaintSched.md)**  
After creating a maintenance plan, define specific criteria for determining when the plan should be executed.
-   **[Associate a maintenance plan to filtered records](../task/t_AssocMaintPlanToFilterRec.md)**  
You can configure a maintenance plan with filtering criteria. For example, you can apply a maintenance plan to all records containing computers that start with "apple".
-   **[Associate a schedule template to matching records](../task/t_AssocSchedTempToMatchRec.md)**  
The instance adds templates to a maintenance schedule so the appropriate requests and tasks, such as work orders and facilities requests, can be auto-generated when a maintenance schedule runs.
-   **[Run a scheduled job to execute a maintenance schedule](../task/t_RunSchedJobToExecMaintSched.md)**  
Maintenance schedules are executed whenever the meter, duration, script, or condition criteria is met. You can also use the Schedule ad-hoc feature to run a maintenance schedule manually.
-   **[Run a maintenance schedule on demand](../task/t_RunAMaintSchedOnDemand.md)**  
Maintenance schedules are typically run using the scheduled job named Planned Maintenance Nightly Run. However, you may want to run the schedule immediately or change the date when a schedule runs.
-   **[View a maintenance log](../task/t_ViewAMaintLog.md)**  
You can view all maintenance performed on a particular CI, the next scheduled maintenance, and the last time maintenance was performed.

**Parent Topic:**[Planned Maintenance](c_SMPlanMaint.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\c_SMPlanMaint.md

```text
---
title: Planned Maintenance
description: The Planned Maintenance application is not a Service Management application, but it works with Service Management applications to help organizations manage regular preventive maintenance of assets.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Planned Maintenance

The Planned Maintenance application is not a Service Management application, but it works with Service Management applications to help organizations manage regular preventive maintenance of assets.

Planned Maintenance uses maintenance plans to trigger the creation of work orders or facilities requests. These work orders and facilities requests specify how to perform maintenance on devices and vehicles, or just about any type of asset that requires maintenance. Work orders and requests can be based on:

-   A specified time interval. For example, after a number of months since the previous maintenance was performed
-   Meters or usage. For example, after a specified number of pages are printed or a specified number of miles are driven.

-   **[Activate Planned Maintenance](../task/t_ActivatePlanMaint.md)**  
The SM **Planned Maintenance** plugin is available as a separate subscription.
-   **[Managing maintenance plans](c_MaintPlanMgmt.md)**  
Planned Maintenance allows you to create, maintain, and schedule maintenance for equipment that requires regular maintenance.
-   **[Maintenance plan examples](../reference/r_MaintPlanExamples.md#)**  
You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.
-   **[Domain separation and Planned Maintenance](domain-separation-planned-maintenance.md)**  
Domain separation is supported in Planned Maintenance. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.

**Parent Topic:**[Service Management](../../it-services/concept/c_ServiceManagement.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\domain-separation-planned-maintenance.md

```text
---
title: Domain separation and Planned Maintenance
description: Domain separation is supported in Planned Maintenance. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Planned Maintenance, Service Management]
---

# Domain separation and Planned Maintenance

Domain separation is supported in Planned Maintenance. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.

## Support level: Standard\*

The support level is Standard but has some exceptions or special conditions.

-   Includes all aspects of **Basic** level support.
-   Business logic: The service provider \(SP\) creates or modifies processes per customer. The use cases reflect proper use of the application by multiple SP customers in a single instance.
-   The instance owner must be able to configure minimum viable product \(MVP\) business logic and data parameters. This configuration is done per tenant, as expected for the specific application.

Sample use case: An admin must be able to make comments required when a record closes for one tenant, but not for another.

For more information on support levels, see [Application support for domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-separated-apps.md).

## How domain separation works in Planned Maintenance

There is no sys\_domain column in the Maintenance Plan \(sm\_maint\_plan\) table. The application cannot be exposed to customer fulfillers; however, the table is condition-based so there is some limited support.

You can set maintenance plans to include or exclude domains or set them globally by design. Support in the Part Requirements \(sm\_part\_requirement\} table is data only.

**Parent Topic:**[Planned Maintenance](c_SMPlanMaint.md)

**Related topics**  


[Domain separation for service providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-sep-landing-page.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\planned-maint-properties.md

```text
---
title: Property settings for Planned Maintenance
description: You configure Planned Maintenance properties at Planned Maintenance Properties .
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Property settings for Planned Maintenance

You configure Planned Maintenance properties at **Planned Maintenance** &gt; **Properties**.

## Trigger properties

<table id="table_aw1_jgm_pbb"><tbody><tr><td>

Use this property to maintain the planned maintenance intervals in fixed meter\[planned\_maintenance.fixed\_meter\]

</td><td>

Preserve the calculated meter trigger. See the illustration.

 -   Select the check box to perform the next planned maintenance at the meter value that was originally calculated even if the most recent work order was completed at a later meter value.
-   Clear the check box to restart the meter calculation using the reading when the work order was completed.

</td></tr><tr><td>

Use this property to maintain the planned maintenance intervals in fixed intervals\[planned\_maintenance.fixed\_interval\]

</td><td>

Preserve the calculated interval trigger. See the illustration.

 -   Select the check box to perform the next planned maintenance at the time/date that was originally calculated based on the configured interval even if the most recent work order was completed late.
-   Clear the check box to restart the interval calculation when the work order is completed.

</td></tr></tbody>
</table>![Properties controlling trigger calculation](../image/property-preserve-calc.png)

**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\r_InstallWServMgmtPlanMaint.md

```text
---
title: Installed with SM Planned Maintenance
description: The SM Planned Maintenance core plugin also includes demo data.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Activate Planned Maintenance, Planned Maintenance, Service Management]
---

# Installed with SM Planned Maintenance

The SM Planned Maintenance core plugin also includes demo data.

## Tables installed with SM Planned Maintenance

<table id="table_u5j_fry_dt"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Maintenance Plan Record\[sm\_m2m\_maint\_plan\_to\_record\]

</td><td>

Relates a maintenance schedule to a record in the system \(from a document ID\). Also contains information about the last time or value the schedule was run for the record and the next time or value when the schedule will run.

</td></tr><tr><td>

Schedule Template\[sm\_m2m\_schedule\_template\]

</td><td>

Relates a maintenance schedule to service management templates.

</td></tr><tr><td>

Maintenance Plan\[sm\_maint\_plan\]

</td><td>

Defines a maintenance plan, including which table and records the plan applies to.

</td></tr><tr><td>

Maintenance Schedule\[sm\_schedule\]

</td><td>

Defines a schedule that is part of a maintenance plan. A schedule can be duration, meter, condition, or script based.

</td></tr></tbody>
</table>## Roles installed with SM Planned Maintenance

|Role title \[name\]|Description|
|-------------------|-----------|
|plan\_maint\_admin|Administrator for planned maintenance.|

## Script includes installed with SM Planned Maintenance

|Script include|Description|
|--------------|-----------|
|PlannedMaintenanceUtils|Utilities for planned maintenance.|
|PlannedMaintenanceAjax|AJAX entry points into PlannedMaintenanceUtils.|

## Client scripts installed with SM Planned Maintenance

<table id="table_wtf_krf_w3"><thead><tr><th>

Client script

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Update field display - trigger type chg

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Updates the fields displayed on the maintenance schedule form based on the trigger type selected.

</td></tr><tr><td>

Update field display - repetition chg

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Updates the fields displayed on the maintenance schedule form based on the repetition selected.

</td></tr><tr><td>

Update table when type changes

</td><td>

Maintenance plan\[sm\_maint\_plan\]

</td><td>

Updates the **table** field based on the selected models \(for model-based plans\).

</td></tr><tr><td>

Validate the every field

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Verifies that the **every** field is a positive number; else it defaults to 1.

</td></tr><tr><td>

Update table when models change

</td><td>

Maintenance plan\[sm\_maint\_plan\]

</td><td>

Updates the **table** field based on the selected models \(for model-based plans\).

</td></tr></tbody>
</table>## Business rules installed with SM Planned Maintenance

<table id="table_ngl_zwx_dt"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Update maintenance plan record

</td><td>

Service Order\[sm\_order\]

</td><td>

Updates the maintenance records \[sm\_m2m\_maint\_plan\_to\_record\] once a service order is closed.

</td></tr><tr><td>

Update m2m schedule records

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Recalculates the next value or next run time when **meter** or **duration** fields change.

</td></tr><tr><td>

Active changes

</td><td>

Maintenance Plan Record\[sm\_m2m\_maint\_plan\_to\_record\]

</td><td>

Handles changes to the active flag for a maintenance plan record.

</td></tr><tr><td>

Active insert

</td><td>

Maintenance Plan Record\[sm\_m2m\_maint\_plan\_to\_record\]

</td><td>

Handles changes to the active flag for a maintenance plan record.

</td></tr><tr><td>

Active changes

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Handles changes to the active flag for a maintenance schedule.

</td></tr><tr><td>

Active changes

</td><td>

Maintenance plan\[sm\_maint\_plan\]

</td><td>

Handles changes to the active flag for a maintenance plan.

</td></tr><tr><td>

Active Insert

</td><td>

Maintenance schedule\[sm\_schedule\]

</td><td>

Handles changes to the active flag for a maintenance schedule.

</td></tr><tr><td>

Apply plan to new records

</td><td>

Maintenance plan\[sm\_maint\_plan\]

</td><td>

Updates the business rule for applying a plan to new records whenever the **Apply to new records** field changes.

</td></tr></tbody>
</table>## Scheduled jobs installed with SM Planned Maintenance

|Scheduled jobs|Description|
|--------------|-----------|
|Planned Maintenance Nightly Run|Builds maintenance requests based on active maintenance plans.|

**Parent Topic:**[Activate Planned Maintenance](../task/t_ActivatePlanMaint.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\r_MaintPlanExamples.md

```text
---
title: Maintenance plan examples
description: You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.To schedule a reboot for certain computer models after a specified number of keystrokes, define a model-based plan with a meter-based maintenance schedule. In the example, a field called keystrokes is added to the Computer \[cmdb\_ci\_computer\] table.To schedule a printer ink cartridge replacement after printing a specified number of pages, define a general plan with a meter-based maintenance schedule. In the example, a table called Printer is added with string fields for printer, model, pages, and the like.To schedule an antivirus scan on certain computers after a specified number of days, define a model-based plan with a duration-based maintenance schedule. In the example, a field called trigger type is added to the Computer \[cmdb\_ci\_computer\] table.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Planned Maintenance, Service Management]
---

# Maintenance plan examples

You can define maintenance plans using model-based, meter-based, or duration-based selection criteria.

-   To schedule a reboot for certain computer models after a specified number of keystrokes, define a model-based plan with a meter-based maintenance schedule.
-   To schedule a printer ink cartridge replacement after printing a specified number of pages, define a general plan with a meter-based maintenance schedule.
-   To schedule an antivirus scan on particular computers after a specified number of days, define a model-based plan with a duration-based maintenance schedule.

**Parent Topic:**[Planned Maintenance](../concept/c_SMPlanMaint.md)

## Define a maintenance schedule for a computer reboot

To schedule a reboot for certain computer models after a specified number of keystrokes, define a model-based plan with a meter-based maintenance schedule. In the example, a field called **keystrokes** is added to the Computer \[cmdb\_ci\_computer\] table.

### Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Click **New** and create a maintenance plan called `Reboot Apple Computers` with the following definitions and then click **Submit**.

    -   **Type**: Model-based
    -   **Model**: Click the lock icon and select **Apple iMac 27** and **Apple MacBook Pro 17**.
3.  Navigate to **Planned Maintenance** &gt; **Maintenance Plans** and then click the number of the maintenance plan you just created.

4.  In the **Maintenance Schedules** related list, click **New**, enter the following settings, and then click **Submit**.

    -   **Name**: Reboot Apple Computers
    -   **Short description**: Scheduled reboot for Apple computers
    -   **Repetition**: Meter
    -   **Every**: 500000
    -   **Field**: keystrokes

### Result

The Reboot Apple Computer maintenance plan schedules all Apple iMac 27 and Apple MacBook Pro 17 computers to reboot after 500,000 keystrokes.

## Define a maintenance schedule for an ink cartridge replacement

To schedule a printer ink cartridge replacement after printing a specified number of pages, define a general plan with a meter-based maintenance schedule. In the example, a table called **Printer** is added with string fields for printer, model, pages, and the like.

### Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Click **New** and create a maintenance plan called `Epson Laser Cartridge Replacement` with the following definitions and then click **Submit**.

    -   **Type**: `General`
    -   **Table**: `Printer`
    -   **Filter condition**: `Model is Epson`
3.  Navigate to **Planned Maintenance** &gt; **Maintenance Plans** and then click the number of the maintenance plan you just created..

4.  In the **Maintenance Schedules** related list, click **New**, enter the following settings, and then click **Submit**.

    -   **Name**: Epson Laser Cartridge Replacement
    -   **Short description**: Scheduled cartridge replacement for Epson laser printers
    -   **Repetition**: Meter
    -   **Every**: 7500
    -   **Field**: Pages

### Result

The Epson Laser Cartridge Replacement maintenance plan schedules all Epson laser printers to replace ink cartridges after printing 7,500 pages.

## Define a maintenance schedule to run antivirus software

To schedule an antivirus scan on certain computers after a specified number of days, define a model-based plan with a duration-based maintenance schedule. In the example, a field called **trigger type** is added to the Computer `[cmdb_ci_computer]` table.

### Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Click **New** and create a maintenance plan called `Update Antivirus` with the following definitions:

    -   **Type**: Model-based
    -   **Model**: Click the lock icon and select **Apple iMac 27** and **Apple MacBook Pro 17**.
3.  Click **Submit**.

4.  Navigate to **Planned Maintenance** &gt; **Maintenance Plans** and then click the number of the maintenance plan you just created.

5.  In the **Maintenance Schedules** related list, click **New**, enter the following settings, and then click **Submit**.

    -   **Name**: Antivirus Update
    -   **Short description**: Scheduled antivirus update for Apple computers
    -   **Repetition**: Duration
    -   **Trigger Type**: Interval
    -   **Days**: 30

### Result

The Update Antivirus maintenance plan schedules all Apple iMac 27 and Apple MacBook Pro 17 computers to run the antivirus software every 30 days.


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_ActivatePlanMaint.md

```text
---
title: Activate Planned Maintenance
description: The SM Planned Maintenance plugin is available as a separate subscription.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Planned Maintenance, Service Management]
---

# Activate Planned Maintenance

The SM **Planned Maintenance** plugin is available as a separate subscription.

## Before you begin

Role required: admin

## About this task

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).


-   **[Installed with SM Planned Maintenance](../reference/r_InstallWServMgmtPlanMaint.md)**  
The SM Planned Maintenance core plugin also includes demo data.

**Parent Topic:**[Planned Maintenance](../concept/c_SMPlanMaint.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_AssocMaintPlanToFilterRec.md

```text
---
title: Associate a maintenance plan to filtered records
description: You can configure a maintenance plan with filtering criteria. For example, you can apply a maintenance plan to all records containing computers that start with "apple".
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Associate a maintenance plan to filtered records

You can configure a maintenance plan with filtering criteria. For example, you can apply a maintenance plan to all records containing computers that start with "apple".

## Before you begin

Role required: SM admin

## Procedure

1.  [Create a maintenance plan](t_CreateAMaintPlan.md).

2.  Set up a **Filter condition** to capture the records that should use the maintenance plan.

    **Note:** You can click **Refresh** \(![picture of the refresh icon, showing two horizontal arrows going opposite directions](../image/RefreshIcon.png)\) to view the number of matching records.

3.  Click **Submit**.

4.  [Configure a maintenance schedule](t_DefineAMaintSched.md).

5.  In the **Related Links** for the maintenance plan, click **Apply schedules to filtered records**.


## Result

The schedule is applied to the records that meet the specified filter conditions.

**Note:** If multiple schedules are defined, they all take effect on the matching records when you click **Apply schedules to filtered records**. See [Configure a maintenance schedule](t_DefineAMaintSched.md) for details. This same functionality exists for maintenance schedules. The **Related Links** for the schedule also contains an **Apply schedule to filtered records** link. If you click this link in the maintenance schedule, only this specific schedule is applied to the records that meet the filter conditions in the associated maintenance plan.

**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_AssocSchedTempToMatchRec.md

```text
---
title: Associate a schedule template to matching records
description: The instance adds templates to a maintenance schedule so the appropriate requests and tasks, such as work orders and facilities requests, can be auto-generated when a maintenance schedule runs.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Associate a schedule template to matching records

The instance adds templates to a maintenance schedule so the appropriate requests and tasks, such as work orders and facilities requests, can be auto-generated when a maintenance schedule runs.

## Before you begin

Role required: SM admin

## About this task

A maintenance schedule runs and the requests or orders are generated, when a scheduled job called Planned Maintenance Nightly Run evaluates the schedule and determines that the meter or interval criteria in the schedule is met or exceeded. You can [run a scheduled job to execute a maintenance schedule](t_RunSchedJobToExecMaintSched.md) that runs at a day or time convenient for your business.

Each auto-generated service order is linked to the record under maintenance in the following ways:

-   Each service order **Record table** and **Record ID** field is always populated with the table name and ID of the record under maintenance.
-   If the record under maintenance is a configuration item, the service orders **Affected CI** field is populated.

## Procedure

1.  [Create a maintenance plan](t_CreateAMaintPlan.md).

2.  Add a **Filter condition** to identify those records for which you want to apply the maintenance plan.

    **Note:** You can click **Refresh** \(![Refresh icon, showing two horizontal arrows going opposite directions](../image/RefreshIcon.png)\) to display the number of matching records.

3.  Click **Submit**.

4.  [Define or select a maintenance schedule.](t_DefineAMaintSched.md)

5.  In the **Maintenance Schedules** related list, click the name of the schedule.

    In the **Maintenance Schedule** form, a **Schedule Templates** related list appears.

6.  In the **Schedule Templates** related list, click **Edit**.

    The **Edit Members** slushbucket displays all the service order, work management, and facilities request templates defined using any of the following applications:

    -   **Product Catalog** &gt; **Templates** &gt; **Work Order Templates**
    -   **Facilities** &gt; **Catalog&amp;Knowledge** &gt; **Facilities Request Templates**
7.  Move the templates you want to apply to the matching record from the **Collection** bucket to the **Model List** bucket and then click **Save**.

8.  In the Maintenance Schedule header, click **Back**.


## Result

Work orders or facilities requests created by the scheduled jobs running on the associated records contain the selected template.

**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_CreateAMaintPlan.md

```text
---
title: Create a maintenance plan
description: When creating a maintenance plan, options on the form help to determine how and when maintenance should be performed.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Create a maintenance plan

When creating a maintenance plan, options on the form help to determine how and when maintenance should be performed.

## Before you begin

Role required: SM admin

## Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Click **New**, specify a meaningful **Name** and **Short description**, fill in the form, and then click **Submit**.

<table id="table_wcf_kbw_mr"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

Auto-generated identification number for the maintenance plan.

</td></tr><tr><td class="sub-head" colspan="2">

Conditions

</td></tr><tr><td>

Type

</td><td>

Type of trigger that determines when maintenance should be performed.

-   **Model based**: Base the maintenance plan on a specified model of a CI, such as a product model.
-   **General**: Base the maintenance plan on a table and filter.
 **Note:** Model-based plans apply only to hardware models, specifically ones that have at least one model category defined.

</td></tr><tr><td>

Model

</td><td>

Select one or more [Product catalog items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/product-catalog/c_ManagingProductCatalogItems.md) to identify the CIs that require preventive maintenance. When you select a model, the associated table appears in the **Table** field. For example, if you select a specific model of PC, the **Table** field displays Computer \[cmdb\_ci\_computer\]. This field appears if you selected the **Model based** type.

 If you select more than one model in the same category, the table does not change. But if you select a CI from a different category, the **Table** field displays the lowest level table that contains all the selected CIs. For example, if you select two PCs and one laser printer, the **Table** field changes to Hardware \[cmdb\_ci\_hardware\], because that table includes computers and printers. If you then add a computer rack, the **Table** field changes to Configuration Item \[cmdb\_ci\], which contains all CIs.

</td></tr><tr><td>

Table

</td><td>

If you selected the **General** type, select the table you want to associate with the maintenance plan. If you selected the **Model based** type, this field displays the lowest level table that contains all the selected CIs.

</td></tr><tr><td>

Filter condition

</td><td>

Filter conditions to locate the specific assets you want to maintain. Only records in the selected table that match the filtering criteria require maintenance.

</td></tr><tr><td>

Apply to new matching records

</td><td>

Select the check box to ensure that the schedules defined for this maintenance plan are applied to all records that have been added to the specified table since the last time the plan was executed, and that meet the conditions entered in the **Filter condition**. For more information, see [Associate a maintenance plan to filtered records](t_AssocMaintPlanToFilterRec.md).

</td></tr><tr><td>

Task creation policy

</td><td>

Specify what to do when a maintenance plan runs on a record that is already under maintenance.-   **Leave alone**: Do not allow the creation of new tasks or the deletion of existing ones.
-   **Cancel existing**: Allow tasks currently associated with the plan to be deleted.
-   **Add to existing**: Allow new tasks, along with existing active tasks, to be added to maintenance plans.


</td></tr></tbody>
</table>    The maintenance plan is now ready for you to [Configure a maintenance schedule](t_DefineAMaintSched.md).

    **Note:** You can [configure the form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-form-layout.md) to add **Asset**, **CI**, and **User** reference fields. These fields are appropriately pre-filled in the associated table and can be useful for generating reports. When a configuration item is selected for the maintenance plan and it is associated with an asset, the **Asset** field is pre-populated with that CI.

    **Note:** After you define a maintenance plan and create maintenance schedules for the plan, you cannot change the **Type**, **Model**, and **Table** fields, or the **Filter conditions**. Changes could potentially cause conflicts. If you need to make changes to those fields, first delete the maintenance schedules, then recreate the schedules with the desired settings.


**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_DefineAMaintSched.md

```text
---
title: Configure a maintenance schedule
description: After creating a maintenance plan, define specific criteria for determining when the plan should be executed.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Configure a maintenance schedule

After creating a maintenance plan, define specific criteria for determining when the plan should be executed.

## Before you begin

Role required: sm\_admin

## About this task

Depending on the asset or CI for which you are setting up maintenance plans, you can create a single plan or multiple plans. For example, you can set up plans for a class of computer to be rebooted on the first and fifteenth of every month.

**Note:** Plan carefully when defining multiple maintenance schedules for the same plan. For example, you set up one schedule to replace a printer cartridge every three months. You set up another schedule to replace the cartridge after every 10,000 pages is printed. This conflict could cause the cartridge to be replaced twice in the same week. Ensure that your schedules do not conflict with one another.

Based on the templates associated with the plan, one or more service management work orders and facilities requests are auto-generated.

Maintenance schedules can be based on either duration or meter and can be triggered by the first occurring related condition. For example, on the Maintenance Schedule form, select **Duration or Meter** as the trigger for an automobile maintenance schedule and then define the duration as three months and the meter as 5,000 miles. The schedule is triggered by whichever comes first. With the **Duration or Meter** trigger selected, the **Next run time** and **Next run value** fields are populated in the **Maintenance Plan Records** related list on the Maintenance Plan form.

**Note:** In a maintenance plan record, the time stamp displayed in the **Next run time** field is not the same as the time set for executing the planned maintenance. The **Next action** field in the **Planned Maintenance Nightly Run** record displays the actual scheduled job execution time for the planned maintenance.

When the scheduled job runs, it will check whether the value in the **Next run time** field is less than the time set of the next planned maintenance nightly run job and if it is, the system will generate a request. A planned nightly maintenance is not executed and a request is not generated based on the next run time.

## Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Click the number of the maintenance plans you want to associate to a maintenance schedule.

3.  In the **Maintenance Schedules** related list, click **New**, specify a meaningful **Name** and **Short description**, fill in the form, and then click **Submit**.

    **Note:** If the form is configured to show the **Next action** field, you can select the date and time for the first maintenance to be performed.

<table id="table_apw_f2w_mr"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Plan

</td><td>

Name of the maintenance plan that this schedule is a part of.

</td></tr><tr><td>

Active

</td><td>

Select the check box to activate the schedule for the maintenance plan.

</td></tr><tr><td>

Trigger

</td><td>

Timing condition that triggers the execution of the plan.

-   **Duration**: Maintenance to be performed based on time. Depending on your selection, additional fields appear to define the duration.
-   **Meter**: Maintenance to be performed based on count. The **Every** and **Field** fields appear.
-   **Condition**: Maintenance to be performed when a certain condition is met. The **Filter condition** field appears
-   **Script**: Apply advanced criteria for running a maintenance plan. The **Script** field appears.
-   **Duration or Meter**: Maintenance to be performed based on both time and count, whichever comes first. You must specify the duration and meter details.


</td></tr><tr><td>

Trigger type

</td><td>

Duration category for the maintenance schedule. For example, if you select **Monthly**, the **Due day of month** field appears so you can specify which day of each month to run maintenance. Different fields appear depending on the trigger type selected. This field appears when **Duration** is selected for **Trigger**.

</td></tr><tr><td>

Repeat

</td><td>

Frequency of the repetition. This field appears when **Interval** is selected for **Trigger type**.

</td></tr><tr><td>

Due day of week

</td><td>

Day of week to repeat on. This field appears when **Weekly** is selected for **Trigger type**.

</td></tr><tr><td>

Due day of month

</td><td>

Day of the month to repeat on. This field appears when **Monthly** or **Annually**is selected for **Trigger type**.

</td></tr><tr><td>

Due month

</td><td>

Month to repeat on. This field appears when **Annually** is selected for **Trigger type**.

</td></tr><tr><td>

Due time

</td><td>

Time of day in hours, minutes, and seconds. This field appears for all trigger types except **Interval**.

</td></tr><tr><td>

Every

</td><td>

Number of occurrences, such as miles or pages, that must be recorded before the maintenance plan is executed. Must be greater than zero \(0\). This field appears when **Meter** is selected for **Trigger**.

</td></tr><tr><td>

Field

</td><td>

Field used to define what the occurrences in the **Every** field apply to. For example, if the **pages** field is entered, the **Every** field can contain the number of pages that are printed before the action defined in the plan is performed. This field appears when **Meter** is selected for **Trigger**.

</td></tr><tr><td>

Table

</td><td>

Lists the table associated with the assets or CIs selected for maintenance. This field appears when **Meter** or **Condition** is selected for **Trigger**.

</td></tr><tr><td>

Lead time

</td><td>

Number of days prior to the **Requested Due by** date to determine the date on which work should begin. That date is pre-filled in the **Scheduled start** field for the task. This field appears when **Duration** is selected for **Trigger**.

</td></tr><tr><td>

Condition

</td><td>

Condition that determines if the maintenance schedule should run. This field appears when Condition is selected for **Trigger**.

</td></tr><tr><td>

Script

</td><td>

Script that determines if the maintenance schedule should run. This field appears when Script is selected for **Trigger**. Maintenance runs if the script returns true. The "current" variable is available and represents the record that is undergoing maintenance, for example, a CI.

</td></tr></tbody>
</table>4.  Specify whether the next planned maintenance should occur at the originally calculated time/meter value or whether to restart the meter/interval calculation from the time that the work order was completed.

    See [Property settings for Planned Maintenance](../reference/planned-maint-properties.md).


-   **[Changes to maintenance schedules](../concept/c_ChangesToMaintSched.md)**  
If you make and save changes to an existing maintenance schedule, any previously associated records are updated accordingly.

**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_RunAMaintSchedOnDemand.md

```text
---
title: Run a maintenance schedule on demand
description: Maintenance schedules are typically run using the scheduled job named Planned Maintenance Nightly Run. However, you may want to run the schedule immediately or change the date when a schedule runs.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Run a maintenance schedule on demand

Maintenance schedules are typically run using the scheduled job named Planned Maintenance Nightly Run. However, you may want to run the schedule immediately or change the date when a schedule runs.

## Before you begin

Role required: admin

## About this task

When you run a maintenance schedule on demand, all of the next run dates for the relevant maintenance plan records are updated to the user-defined time, now or in the future. All the appropriate service orders are created. If the schedule is meter, condition, or script-based, service orders are created for maintenance plan records that meet the schedule criteria.

## Procedure

1.  Navigate to **All** &gt; **Planned Maintenance** &gt; **Maintenance Plans**.

2.  Open the Maintenance Plan that contains the schedule to run.

3.  In the **Maintenance Schedules** related list, select the maintenance schedule you want to run.

4.  Click the **Run on demand** related link and then fill in the form.

<table id="table_upp_ml3_ts"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Run now

</td><td>

Select the check box to run the maintenance for the schedule immediately. Clear the check box to schedule a date for the schedule to run.

</td></tr><tr><td>

Select date

</td><td>

Date in the future for maintenance to run. **Note:** This field appears only when the **Run Now** check box is not selected.

</td></tr></tbody>
</table>
**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_RunSchedJobToExecMaintSched.md

```text
---
title: Run a scheduled job to execute a maintenance schedule
description: Maintenance schedules are executed whenever the meter, duration, script, or condition criteria is met. You can also use the Schedule ad-hoc feature to run a maintenance schedule manually.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# Run a scheduled job to execute a maintenance schedule

Maintenance schedules are executed whenever the meter, duration, script, or condition criteria is met. You can also use the Schedule ad-hoc feature to run a maintenance schedule manually.

## Before you begin

Role required: SM admin

## About this task

Maintenance schedules are run regularly using the Planned Maintenance Nightly Run scheduled job. When the scheduled job is run, the appropriate Service Orders are created for all records that meet the schedule criteria \(including all records for the current day\).

To configure the nightly planned maintenance scheduled job:

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Scheduled Jobs**.

2.  Open **Planned Maintenance Nightly Run**.

3.  In Related Links, click **Configure Job Definition**.

4.  To specify a different schedule for running the job, change the **Run** and **Time** fields.

    A scheduled job does not run based on the value set in the **Next run time** field in the maintenance plan record for this job. For more information, see [Configure a maintenance schedule](t_DefineAMaintSched.md).

5.  Click **Update**.

6.  At any time, to run the scheduled job, click **Execute Now**.

    The scheduled job evaluates all previously defined schedules and executes the ones that are scheduled to run.

    **Note:** If one or more records in the table associated with the maintenance plan are deleted after the matching records were associated with the maintenance plan, the next nightly run removes all the records associated with those removed assets.


**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```


### File: service-management-for-the-enterprise\planned-maintenance-family\t_ViewAMaintLog.md

```text
---
title: View a maintenance log
description: You can view all maintenance performed on a particular CI, the next scheduled maintenance, and the last time maintenance was performed.
locale: en-US
release: australia
product: Planned Maintenance \(Family\)
classification: planned-maintenance-family
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing maintenance plans, Planned Maintenance, Service Management]
---

# View a maintenance log

You can view all maintenance performed on a particular CI, the next scheduled maintenance, and the last time maintenance was performed.

## Before you begin

Role required: SM admin

## Procedure

1.  After the Planned Maintenance Nightly Run scheduled job has executed for a maintenance plan, navigate to the location of the CI for which you ran the plan.

    For example, **Configuration** &gt; **Servers** &gt; **Linux**.

2.  Right-click in the record header and select **View** &gt; **Maintenance**.

3.  Select the CI to view the log.

    Related lists display maintenance plans, maintenance plan records for the CI, and service orders.


**Parent Topic:**[Managing maintenance plans](../concept/c_MaintPlanMgmt.md)


```
