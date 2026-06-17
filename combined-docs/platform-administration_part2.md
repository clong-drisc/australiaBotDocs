

### File: platform-administration\upgrade-management\um-pre-upgrade-activities.md

```text
---
title: Implement pre-upgrade activities on a non-prod instance
description: Complete the pre-upgrade tasks for a successful upgrade experience on your instance.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 13
breadcrumb: [Access guided upgrade on a non-production instance, Configure, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Implement pre-upgrade activities on a non-prod instance

Complete the pre-upgrade tasks for a successful upgrade experience on your instance.

## Before you begin

**Note:** For each step, you will have the option to either skip the step or mark complete and only then move to the next guided upgrade step.

Role required: admin

## Procedure

1.  Select **View release notes** if you want to review the release notes of the selected Guided upgrade version.

    **Note:** This step is visible only if you are in a non-production instance.

2.  Request a clone.

    **Note:** This step is visible only if you are in a non-production instance. It is recommended to clone the production instance to non-production instance. Select **Request clone** to configure the source and target instances.

    **Note:** For data integrity and recovery purposes, it is recommended that the update sets should be either closed out or backed up. It is crucial for preserving all system modifications and enabling restoration when required.

    You can also see the cloning summary information that tells you the instance you have cloned and other relevant information. You can see the start and end time of the cloning process. By default, you are in the America/Los Angeles timezone. You can modify the timezone preference by navigating to **User Menu** &gt; **Preferences** &gt; **Language &amp; Region**. You can then select the required timezone from the drop down menu.

    There are four different scenario for the cloning process.

    -   No clone has been scheduled for this instance

        ![](../image/um-clone-not-scheduled.png)

    -   Scheduled
    -   Running

        ![](../image/um-clone-running.png)

    -   Complete

        ![](../image/um-clone-completed.png)

    **Note:** If the cloning process is in progress, the **Skip** and **Mark as complete** options are disabled.

    A list of production instances shows up and you can select the instance you want to clone.

    **Note:** If you are in a production instance, the list of instances for cloning doesn’t show up.

    You can expect the following in this pre-upgrade activity once you select the instance to be cloned.

    -   You will be redirected to the Cloning tool to initiate the cloning process.
    -   The Cloning tool guides you through the cloning process of your production instance.
    -   You will be reminded to ensure to back up the update sets before starting the cloning process to save any changes and configurations.
3.  Choose an upgrade plan.

    There are two options to choose your upgrade plan.

    -   Select an existing one: You can import update sets to apply or merge upgrade plans for your upgrades. This option is selected by default.

        In order to apply an existing upgrade plan, you have the following options:

        -   Import update sets: You must first import update sets before selecting an existing upgrade plan.
            1.  Select **Import update sets** to import an update set. The Retrieve Update Sets list shows up.
            2.  Select the Import Update Set from XML related link to select the update set to be imported. The Import XML page shows up.
            3.  Select an already existing update set using **Choose file** and then select **Upload**.

                The selected update set gets uploaded in the current upgrade plan. The current upgrade plan shows up on the Retrieve Update Sets list.

            4.  Select the plan from the Retrieve Update Sets list. The Retrieve Update Set form shows up with all its associated customer updates.
            5.  Select **Preview Update Set**. The Update Set Preview modal shows up.
            6.  Once the previewing of the update set is completed successfully, select **Commit Update Set**. The Update Set Commit modal shows up.

                **Note:** This option is visible only after the successful completion of update set preview.

        -   Select an existing upgrade plan: You can view the imported plans to choose or can select multiple plans or merge them into one plan.

            **Note:** This option considerably reduces rework with an upgrade plan, maintains accuracy and makes your upgrade process seamless.

            You will see the following modal when you select Select upgrade plan. You can then select either one upgrade plan or multiple plans to be merged and applied to the current upgrade.

            ![](../image/um-upgrade-plans-merge.jpeg)

            **Note:** The **Apply** option is visible only when you select one upgrade plan to be applied to the current upgrade.

            ![](../image/um-upgrade-plans-apply.jpeg)

            **Note:** The **Merge and apply** option is visible only if you have selected multiple upgrade plans. The upgrade plan name changes as per the selection of upgrade plans.

            When merging multiple upgrade plans, upgrade plan items that appear in more than one plan are used in the merged plan by their highest version. This ensures consistency and avoids version conflicts in the resulting merged plan.

    -   Create a new one: You can get started with creating a new plan for your instance upgrade.
        -   Create an upgrade plan: Select **Create a plan** to start creating the new upgrade plan. Select the Upgrade Plan link from the success message banner to view the created upgrade plan.

            **Note:** The success message banner is generated immediately after the upgrade plan is created by selecting **Create a plan** and stays visible until the page is reloaded.

            If you select the **Create a plan** option again after creating a plan, you will see the following message.

            ![](../image/um-override-upgrade-plan.png)

            **Note:** Only the most recent upgrade plan without any upgrade plan items is retained. For example, if the most recent upgrade plan is created without upgrade plan items, it automatically overrides any earlier upgrade plan that also doesn't have upgrade plan items. There can be more than one upgrade plan with upgrade plan items.

            In the Upgrade Plans list, there can be several upgrade plans with upgrade plan items and only the recent upgrade plan with no upgrade plan items.

            **Note:** An instance can have only one active upgrade plan at a time, regardless of whether the plan includes upgrade plan items. Only the most recent upgrade plan is in active state as it automatically gets applied to the current upgrade.

        -   View generated upgrade plan: This is an alternate way to view the recently created upgrade plan. This option is helpful when you reload the page and the success message banner disappears.

            **Note:** This option is visible only after the upgrade plan is created.

    Once the upgrade plan is finally selected, the **Select upgrade plan** and **Create a new one** options are disabled.

4.  Automate upgrade tasks.

    There are two different kinds of upgrade tasks in this step.

    -   Default automated tasks: These tasks are completed automatically.
        -   Generate upgrade preview: It helps you understand how your instance will be impacted after the upgrade even without having it really upgraded.
        -   Create upgrade update sets: The automatic creation of the upgrade update sets capture changes and helps during review of the skipped records.
    -   Optional automated tasks: You have the option of completing these tasks automatically.
        -   Generate the ATF tests: Automatic generation of the ATF tests using the ATF test generator and cloud runner store application.

            **Note:** These ATF tests run automatically post-upgrade.

        -   Upgrade store applications to the latest version: By default, all the applications are being upgraded to the latest version. If you don’t want them to be upgraded to the latest version, you can disable the toggle and manually select a compatible version during the store application upgrade step.
5.  Conduct pre-testing.

    This step captures all the tests required to be executed after the upgrade.

    -   Generate tests: Auto-generates regression tests with the use of ATF Test generator tool. You can review the start time and the total time to complete the test generation.

        **Note:** The auto-generated ATF test suites are added to the Upgrade Test Suites table and are executed automatically post-upgrade.

        Select **Status** to check the status of the generated tests. You can also cancel the test generation process by selecting **Cancel**.

    -   Create additional tests: Review the existing tests or create additional tests to complete upgrade faster.
    -   Upgrade test suites: The auto-generated regression tests in the Generate tests section are added here automatically when they are generated. You can also add more tests by selecting it from the Available test suites table section.
    -   Available test suites: Review the list of available test suites. You can also select the tests you want to add to the Upgrade test suites section. Only the selected tests are executed automatically after the upgrade.

        ![Screenshot showing the available test suites](../image/um-available-test-suites.png)

        **Note:** The available test suites are already successfully passed test suites.

6.  Preview application upgrades.

    You can preview all the store applications with their updates for your instance. If the upgrade preview generation is in progress, you can track it using the Execution tracker link.

    -   Selected Apps: You can review the following information:
        -   Customized apps: Number of apps that have been customized
        -   New apps to be installed: Total number of new apps to be installed for the upgrade
        -   Apps to be upgraded: Total number of existing apps whose version need to be upgraded

            **Note:** If you have disabled Upgrade store applications to the latest version previously, the value for Apps to be upgraded depends on the manual selection of the Upgrade store applications section.

    -   Update Now Assist Suite: Use the Update Now Assist Suite section to manage application version compatibility. When you upgrade an application in the compatibility matrix, the system automatically updates all related applications to compatible versions.

        Select **Suite Version** to select a suite version from the dropdown menu. The dropdown menu shows the suite versions available in the selected version. For example, if you want to upgrade your instance to Australia, only the suite versions available in Australia are shown in the dropdown menu options.

        **Note:** Select None as the Suite Version option if you don’t want to update Now Assist Suite.

        Select Execution tracker link to track the progress of the list. The Execution tracker form shows up. Select Show status related link to see the current status.

        **Note:** Only the applications whose upgraded versions are available to be upgraded in the selected suite version are shown in the list. No new applications can be installed here.

        -   Application: Name of the application within the selected suite version
        -   Status: Status of the application
        -   Current Version: Current version of the application
        -   Latest Version: Latest available version of the application
        -   Selected Version: Configured version of the application in the selected suite version
        **Note:** Downgrading of application versions is not allowed.

        Select **Dependent apps and plugins** to see the calculated list of all dependent applications and plugins for the Now Assist Suite applications list.

        ![](../image/uc-dependent-apps.png)

        For example, if you have 5 applications in the selected version of Now Assist Suite, the Now assist suite dependencies modal lists only the dependencies of these 5 applications.

    -   Upgrade store applications

        ![Screenshot showing upgrade store apps](../image/um-upgrade-store-apps.png)

        -   Application: Name of the application
        -   Current version: Current version of the application on the instance
        -   Latest version: Latest available version of the application
        -   Upgrade Version: Selected version of the application to which you want to upgrade
        -   State: State of the application based on the selected version for the upgrade. It displays either **Compatible** or **Check compatibility** based on the selected version if its compatible or not.
        -   Status message: Provides you more information about app compatibility if there are any failures after running **Check app compatibility**.
        **Note:** If you have previously selected the automatic upgrade option, the applications are upgraded to the latest version by default.

        If you haven't selected the automatic upgrade option previously, you get an option to select the version of the application to which you want to upgrade.

    The number of Apps to be upgraded gets updated depending on the manual selection of the apps for the selected versions. For example, if you select **Set all to minimum version** for all the applications, the number of Apps to be upgraded remains unchanged. Select **Set all to latest** if you want to update all the applications to the latest version available. Ensure to check the compatibility of the apps after selecting its versions by selecting **Check app compatibility**. If an application is not compatible, modify the version to make it compatible before moving on to the next step.

    **Note:** You can proceed to the next step of the upgrade process only after checking the compatibility of the applications.

    Select **View upgrade plan** in the Selected Apps section to see all the items along with their selected versions being added to the upgrade plan at the end of this step.

    You can now edit this step by selecting **Edit step** even after marking it complete.

    **Note:** The **Edit step** option is available only when you mark this step as complete and before scheduling or starting any upgrade. Once you select **Edit step**, the next step in the Pre-upgrade process resets. You can again proceed to the next step of the upgrade process only after checking the compatibility of the applications.

7.  Review predicted skipped records.

    Skipped records occur when customizations on your instance prevent certain files from being automatically updated during an upgrade.

    Select **Regenerate Preview** to regenerate a preview either for all the applications or for only the modified applications in the previous step.

    **Note:** Set the glide.upgrade\_center.regenerate\_upgrade\_preview property to `true` to regenerate the preview for all the apps.

    -   Upgrade preview: You can view the current version and the previewing version of the upgrade in this section. You can also see if there is any upgrade been scheduled.
    -   Skipped record summary: You can view the following information.

        ![Screenshot showing the skipped record summary](../image/um-skipped-record-summary.png)

        -   Total records changed: Gives the total number of records that have changed since last upgrade. Select the Review changes link to see the list of records that have changed.
        -   Total skipped records: Shows the numbers of skipped records that have been resolved, total skipped records that need to be reviewed and the number of skipped records that have already been reviewed.
        -   Skipped records without tests: States the total number of skipped records that have tests. The Test linked link in the Skipped records section points to the list of tests of the skipped records that have associated tests.
    -   Predicted skipped records: Shows the total number of predicted skipped records

        ![Screenshot showing the predicted skipped records list](../image/um-predicted-skipped-test-link.png)

        -   Name: Name of the skipped record
        -   Product: Name of the record that the skipped record belongs to
        -   Status: Status of the skipped record if it has been resolved, reviewed or needs to be reviewed
        -   Test linked: Links to the list of test associated with the skipped record. It helps you know the reason why a certain record has been skipped by viewing all the tests associated with the skipped record.
        -   Prediction disposition: Action predicted to be performed on the skipped record during the selected upgrade.
            -   Predicted Insert: The system is predicted to insert a new record.
            -   Predicted Update: The system is predicted to update this record.
            -   Reverted: This record was reverted to the base version, and won’t be skipped on the next upgrade.
            -   Predicted Skip: The system won't change this record in order to preserve customizations.
            -   Predicted Skip \(Manual Merge\): The system won't change this record because updating it requires manual intervention.
            -   Predicted Skip \(Apply Once\): The system is predicted to skip this record because it had already applied an update from an xml file in the apply once folder.
    -   Skipped record rules editor: Use the skipped record rules editor to create skipped record rules based on the set conditions to define customizations after an upgrade.

        **Note:** This step is completed within the Review predicted skipped records step.

        The skipped records matching the set conditions in the skipped record rules editor, perform the previously selected actions. Select **View latest upgrade history** to determine the actions and conditions to be set depending on the previous upgrades.

        ![Screenshot showing the skipped record rules editor](../image/um-record-rule-editor.png)

        The skipped record rules shows the list of skipped record rules on the instance.

        -   Name: Name of the rule
        -   Active: States if the rule is active or not
        -   Conditions: Conditions set by the rule to filter the skipped records
        -   Action: Previously chosen action for the specific rule
        -   Order: The order in which the rules are sorted
        Select **Create rule** if you want to create any additional skipped record rules.

    You can do the following in this pre-upgrade activity.

    -   Review the list of predicted skipped records in the Preview module and decide which versions of the files to be retained.
    -   You can choose some customizations to be reverted to the base version, allowing them to go through the entire upgrade process without being skipped.
    -   Ensure to review and update the list of skipped records after the upgrade.
    -   Once done with the reviewing of the skipped records, complete the next activities required in the pre-upgrade process.

**Parent Topic:**[Access guided upgrade on a non-production instance](um-guided-tour-implement.md)

**Related topics**  


[Implement instance upgrade activities on a sub-prod instance](um-implement-instance-upgrade.md)

[Implement post-upgrade activities on a non-prod instance](um-post-upgrade-activities.md)


```


### File: platform-administration\upgrade-management\um-pre-upgrade-prod.md

```text
---
title: Implement pre-upgrade activities on a prod instance
description: Complete the pre-upgrade tasks for a successful upgrade experience on your production instance.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 9
breadcrumb: [Access guided upgrade on a production instance, Configure, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Implement pre-upgrade activities on a prod instance

Complete the pre-upgrade tasks for a successful upgrade experience on your production instance.

## Before you begin

**Note:** For each step, you will have the option to either skip the step or mark complete and only then move to the next guided upgrade step.

Role required: admin

## Procedure

1.  Choose an upgrade plan.

    There are two options to choose your upgrade plan.

    -   Select an existing one: You can import update sets to apply or merge upgrade plans for your upgrades. This option is selected by default.

        In order to apply an existing upgrade plan, you have the following options:

        -   Import update sets: You must first import update sets before selecting an existing upgrade plan.
            1.  Select **Import update sets** to import an update set. The Retrieve Update Sets list shows up.
            2.  Select the Import Update Set from XML related link to select the update set to be imported. The Import XML page shows up.
            3.  Select an already existing update set using **Choose file** and then select **Upload**.

                The selected update set gets uploaded in the current upgrade plan. The current upgrade plan shows up on the Retrieve Update Sets list.

            4.  Select the plan from the Retrieve Update Sets list. The Retrieve Update Set form shows up with all its associated customer updates.
            5.  Select **Preview Update Set**. The Update Set Preview modal shows up.
            6.  Once the previewing of the update set is completed successfully, select **Commit Update Set**. The Update Set Commit modal shows up.

                **Note:** This option is visible only after the successful completion of update set preview.

        -   Select an existing upgrade plan: You can view the imported plans to choose or can select multiple plans or merge them into one plan.

            **Note:** This option considerably reduces rework with an upgrade plan, maintains accuracy and makes your upgrade process seamless.

            You will see the following modal when you select Select upgrade plan. You can then select either one upgrade plan or multiple plans to be merged and applied to the current upgrade.

            ![](../image/um-upgrade-plans-merge.jpeg)

            **Note:** The **Apply** option is visible only when you select one upgrade plan to be applied to the current upgrade.

            ![](../image/um-upgrade-plans-apply.jpeg)

            **Note:** The **Merge and apply** option is visible only if you have selected multiple upgrade plans. The upgrade plan name changes as per the selection of upgrade plans.

            When merging multiple upgrade plans, upgrade plan items that appear in more than one plan are used in the merged plan by their highest version. This ensures consistency and avoids version conflicts in the resulting merged plan.

    -   Create a new one: You can get started with creating a new plan for your instance upgrade.
        -   Create an upgrade plan: Select **Create a plan** to start creating the new upgrade plan. Select the Upgrade Plan link from the success message banner to view the created upgrade plan.

            **Note:** The success message banner is generated immediately after the upgrade plan is created by selecting **Create a plan** and stays visible until the page is reloaded.

            If you select the **Create a plan** option again after creating a plan, you will see the following message.

            ![](../image/um-override-upgrade-plan.png)

            **Note:** Only the most recent upgrade plan without any upgrade plan items is retained. For example, if the most recent upgrade plan is created without upgrade plan items, it automatically overrides any earlier upgrade plan that also doesn't have upgrade plan items. There can be more than one upgrade plan with upgrade plan items.

            In the Upgrade Plans list, there can be several upgrade plans with upgrade plan items and only the recent upgrade plan with no upgrade plan items.

            **Note:** An instance can have only one active upgrade plan at a time, regardless of whether the plan includes upgrade plan items. Only the most recent upgrade plan is in active state as it automatically gets applied to the current upgrade.

        -   View generated upgrade plan: This is an alternate way to view the recently created upgrade plan. This option is helpful when you reload the page and the success message banner disappears.

            **Note:** This option is visible only after the upgrade plan is created.

    Once the upgrade plan is finally selected, the **Select upgrade plan** and **Create a new one** options are disabled.

2.  Preview application upgrades.

    You can preview all the store applications with their updates for your instance. If the upgrade preview generation is in progress, you can track it using the Execution tracker link.

    -   Selected Apps: You can review the following info
        -   Customized apps: Number of apps that have been customized
        -   New apps to be installed: Total number of new apps to be installed for the upgrade
        -   Apps to be upgraded: Total number of existing apps whose version need to be upgraded

            **Note:** If you have disabled Upgrade store applications to the latest version previously, the value for Apps to be upgraded depends on the manual selection of the Upgrade store applications section.

    -   Upgrade store applications

        -   Application: Name of the application
        -   Current version: Current version of the application on the instance
        -   Latest version: Latest available version of the application
        -   Upgrade Version: Selected version of the application to which you want to upgrade
        -   State: State of the application based on the selected version for the upgrade. It displays either **Compatible** or **Check compatibility** based on the selected version if its compatible or not.
        -   Status message: Provides you more information about app compatibility if there are any failures after running **Check app compatibility**.

            **Note:** If you have previously selected the automatic upgrade option, the applications are upgraded to the latest version by default.

            If you haven't selected the automatic upgrade option previously, you get an option to select the version of the application to which you want to upgrade.

        The number of Apps to be upgraded gets updated depending on the manual selection of the apps for the selected versions. For example, if you select **Set all to minimum version** for all the applications, the number of Apps to be upgraded remains unchanged. Select **Set all to latest** if you want to update all the applications to the latest version available. Ensure to check the compatibility of the apps after selecting its versions by selecting **Check app compatibility**. If an application is not compatible, modify the version to make it compatible before moving on to the next step.

        **Note:** You can proceed to the next step of the upgrade process only after checking the compatibility of the applications.

        Select **View upgrade plan** in the Selected Apps section to see all the items along with their selected versions being added to the upgrade plan at the end of this step.

        You can now edit this step by selecting **Edit step** even after marking it complete.

        **Note:** The **Edit step** option is available only when you mark this step as complete and before scheduling or starting any upgrade. Once you select **Edit step**, the next step in the Pre-upgrade process resets. You can again proceed to the next step of the upgrade process only after checking the compatibility of the applications.

    If automatic upgrade has not been opted in, you can manually select the versions of the applications to be upgraded. Select **Set all to latest** if you want to update all the applications to the latest version available. Ensure to check the compatibility of the apps after selecting its versions by selecting **Check app compatibility**. If an application is not compatible, modify the version to make it compatible before moving on to the next step.

3.  Review predicted skipped records.

    Skipped records occur when customizations on your instance prevent certain files from being automatically updated during an upgrade.

    -   Upgrade preview: You can view the current version and the previewing version of the upgrade in this section. You can also see if there is any upgrade been scheduled.
    -   Skipped record summary: You can view the following information.

        ![](../image/um-skipped-without-tests.png)

        -   Total records changed: Gives the total number of records that have changed since last upgrade. Select the Review changes link to see the list of records that have changed.
        -   Total skipped records: Shows the numbers of skipped records that have been resolved, total skipped records that need to be reviewed and the number of skipped records that have already been reviewed.
        -   Skipped records without tests: States the total number of skipped records that have tests. The Test linked link in the Skipped records section points to the list of tests of the skipped records that have associated tests.
    -   Predicted skipped records: Shows the total number of predicted skipped records
        -   Name: Name of the skipped record
        -   Product: Name of the record that the skipped record belongs to
        -   Priority:
        -   Status: Status of the skipped record if it has been resolved, reviewed or needs to be reviewed
        -   Prediction disposition: Action predicted to be performed on the skipped record during the selected upgrade.
            -   Predicted Insert: The system is predicted to insert a new record.
            -   Predicted Update: The system is predicted to update this record.
            -   Reverted: This record was reverted to the base version, and won’t be skipped on the next upgrade.
            -   Predicted Skip: The system won't change this record in order to preserve customizations.
            -   Predicted Skip \(Manual Merge\): The system won't change this record because updating it requires manual intervention.
            -   Predicted Skip \(Apply Once\): The system is predicted to skip this record because it had already applied an update from an xml file in the apply once folder.
        -   Plugin: The app id where the skipped record is found
    -   Skipped record rules editor: Use the skipped record rules editor to create skipped record rules based on the set conditions to define customizations after an upgrade.

        **Note:** This step is completed within the Review predicted skipped records step.

        ![Screenshot showing skipped record rules editor in a prod instance](../image/um-skipped-record-rules-prod.png)

        The skipped records matching the set conditions in the skipped record rules editor, perform the previously selected actions. Select **View latest upgrade history** to determine the actions and conditions to be set depending on the previous upgrades.

        The skipped record rules shows the list of skipped record rules on the instance.

        -   Name: Name of the rule
        -   Active: States if the rule is active or not
        -   Conditions: Conditions set by the rule to filter the skipped records
        -   Action: Previously chosen action for the specific rule
        -   Order: The order in which the rules are sorted
        Select **Create rule** if you want to create any additional skipped record rules.

    You can do the following in this pre-upgrade activity.

    -   Review the list of predicted skipped records in the Preview module and decide which versions of the files to be retained.
    -   You can choose some customizations to be reverted to the base version, allowing them to go through the entire upgrade process without being skipped.
    -   Ensure to review and update the list of skipped records after the upgrade.
    -   Once done with the reviewing of the skipped records, complete the next activities required in the pre-upgrade process.

**Parent Topic:**[Access guided upgrade on a production instance](um-guided-tour-implement-prod.md)


```


### File: platform-administration\upgrade-management\um-prepare-upgrade-plan.md

```text
---
title: Prepare to upgrade with Upgrade Plan
description: Prepare your instance upgrade with Upgrade Plan by determining all the applications and plugins are ready to be implemented in the upgrade.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Upgrade Plans tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Prepare to upgrade with Upgrade Plan

Prepare your instance upgrade with Upgrade Plan by determining all the applications and plugins are ready to be implemented in the upgrade.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to Upgrade Plan using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade Plan**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade Plan**.|

    The upgrade plan that is installed shows up on the list.

2.  Select the upgrade plan.

    The upgrade plan form view shows up with all its configurations.

3.  To ensure that all the applications and plugins are ready to be implemented in the upgrade, select **Refresh** in the context menu of the Upgrade Plan.

    If there are errors for any of the items, then fix them and follow the Reprocess step.

    **Note:** All the applications and plugins under the Upgrade Plan Items related list must be in the **Ready** state to proceed with the upgrade. The application or plugin in the **Already Installed** state, error or its latest version won't be considered during the upgrade process.

    The upgrade plan is now ready to be implemented.

4.  Apply an existing upgrade plan to an instance anytime, without being limited to during upgrades only.

    You can now also export the upgrade plan in a batch install format by using the **Export** button. See [CI/CD - POST /sn\_cicd/app/batch/install](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/rest-apis/cicd-api.md) for more information.

5.  Select **Reinstall** to reinstall the failed items in an upgrade plan, after the upgrade completes.

    You can also review the upgrade plan history to know the reasons of failure.

    **Note:** You are required to use this option only if you have failed items in an upgrade plan.

6.  Click **Reprocess** to reprocess the upgrade plan after the upgrade plan item errors have been resolved.

    **Note:** This step is applicable only if you have any error items in the upgrade plan.


-   **[Preview Upgrade Plan](um-preview-upgrade-plan.md)**  
Preview your upgrade plan before being implemented in the upgrades. Once the upgrade plan is installed, it auto generates the preview of the upgrade plan.

**Parent Topic:**[Upgrade Plans tool in Upgrade Console](../concept/um-upgrade-plans-tool.md)

**Related topics**  


[Building your Upgrade Plan](um-building-upgrade-plan.md)

[Refreshing your Upgrade Plan](um-refreshing-upgrade-plan.md)

[Installing your Upgrade Plan](um-installing-upgrade-plan.md)

[Apply Upgrade Plan on your upgrade](um-apply-upgrade-plan.md)


```


### File: platform-administration\upgrade-management\um-preview-upgrade-plan.md

```text
---
title: Preview Upgrade Plan
description: Preview your upgrade plan before being implemented in the upgrades. Once the upgrade plan is installed, it auto generates the preview of the upgrade plan.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Prepare to upgrade with Upgrade Plan, Upgrade Plans tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Preview Upgrade Plan

Preview your upgrade plan before being implemented in the upgrades. Once the upgrade plan is installed, it auto generates the preview of the upgrade plan.

## Before you begin

Role required: admin

## Procedure

1.  Go to the Upgrade Preview page to preview the Upgrade Plan.

2.  Check the Upgrade Plan mentioned on the Previewing version card.![Image showing previewing version card](../../upgrade-center/image/uc-previewing-version-card.png)

3.  Check the Predicted skipped records with upgrade plan card to preview the skipped records.![Image showing predicted skipped records with upgrade plan card](../../upgrade-center/image/uc-predicted-skipped-records-up.png)

    -   Total: total number of skipped records
    -   Resolved: skipped records included in the upgrade plan
    -   Reviewed: skipped records that have been reviewed
    **Note:** This step is applicable only if you have enabled the GLIDE\_UPGRADE\_PLAN\_INCLUDE\_SKIPS property.


**Parent Topic:**[Prepare to upgrade with Upgrade Plan](um-prepare-upgrade-plan.md)


```


### File: platform-administration\upgrade-management\um-previewed-changes.md

```text
---
title: Preview predicted changes
description: Use the previewed changes table to view the list of total records that are predicted to change when the upgrade occurs.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Upgrade Preview tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Preview predicted changes

Use the previewed changes table to view the list of total records that are predicted to change when the upgrade occurs.

## Preview skipped list prediction

The **Total record changes** also includes records that are predicted to be skipped due to various reasons. The most common reason is due to customization. The reason an upgrade skips customizations is to avoid overwriting your customizations. Upgrade Preview attempts to predict which records will be skipped when the actual upgrade occurs. It predicts skips due to customizations, and some of the other more complex scenarios as well. It is possible to use Upgrade Preview to address these predicted customization skips before the upgrade occurs, which can prevent that skip from happening.

Click **View preview details** link on the **Previewing version** card. The Upgrade Preview form appears along with the following related lists details.

<table id="table_ycy_np2_clb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

File name

</td><td>

Record that has been flagged for reconciliation.

</td></tr><tr><td>

Predicted Disposition

</td><td>

Action predicted to be performed on this file during the selected upgrade:-   Predicted Insert: The system is predicted to insert a new record.
-   Predicted Update: The system is predicted to update this record.
-   Reverted: This record was reverted to the base version, and won’t be skipped on the next upgrade.
-   Predicted Skip: The system won't change this record in order to preserve customizations.
-   Predicted Skip \(Manual Merge\): The system won't change this record because updating it requires manual intervention.
-   Predicted Skip \(Apply Once\): The system is predicted to skip this record because it had already applied an update from an xml file in the apply once folder.

</td></tr><tr><td>

Priority

</td><td>

Priority that has been assigned to resolve the conflict. Values range from one to five, with one representing the highest priority.**Note:** ServiceNow prioritizes the skipped records based on the importance of the file types. The prioritization is done as follows:

-   Priority 1 \(highest priority\): UI pages, UI macros, and more
-   Priority 2: Business Rules, Security ACLs, and more
-   Priority 3: Reports and more
-   Priority 4: Form Sections, Choice Sets, and more
-   Priority 5 \(lowest priority\): other

</td></tr><tr><td>

Resolution

</td><td>

Ways to resolve a conflict.-   **Not reviewed**: Conflicted files that have not been reviewed yet
-   **Reviewed**: Reviewed but no action has been taken yet
-   **Review not needed**: Review of the skipped files are not required
-   **Reviewed and Retained**: Left customizations in place without update from upgrade
-   **Reviewed and Reverted**: Customizations discarded, record updated according to the upgrade version

</td></tr><tr><td>

Plugin

</td><td>

Plugin containing the record

</td></tr><tr><td>

Related record

</td><td>

Record that the changelist entry applies to

</td></tr></tbody>
</table>**Parent Topic:**[Upgrade Preview tool in Upgrade Console](../concept/um-upgrade-preview-tool.md)


```


### File: platform-administration\upgrade-management\um-previous-resolutions-rl.md

```text
---
title: Previous Resolutions related list
description: The Previous Resolutions related list shows the history of the selected skipped record. You can see what resolutions have been done with the selected skipped record in the previous upgrades.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Skipped Records visual task board \(VTB\), Reviewing upgrade history, Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Previous Resolutions related list

The Previous Resolutions related list shows the history of the selected skipped record. You can see what resolutions have been done with the selected skipped record in the previous upgrades.

<table id="table_tht_fp2_clb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

File name

</td><td>

Name of the skipped record.

</td></tr><tr><td>

Disposition

</td><td>

Disposition is skipped since the related list is only for skipped records.

</td></tr><tr><td>

Priority

</td><td>

Prioritization of the skipped records based on the importance of the file types. The prioritization is done as follows:-   Priority 1 \(highest priority\): UI pages, UI macros, and more
-   Priority 2: Business Rules, Security ACLs, and more
-   Priority 3: Reports and more
-   Priority 4: Form Sections, Choice Sets, and more
-   Priority 5 \(lowest priority\): other

</td></tr><tr><td>

Resolution

</td><td>

The resolution made in the previous upgrades

</td></tr><tr><td>

Target name

</td><td>

Name of the record that you see on UI, as opposed to the sys\_update\_name which is the underlying name that has the table and sys\_id

</td></tr><tr><td>

Type

</td><td>

Type of file which determines the priority level.

</td></tr><tr><td>

Table

</td><td>

The table where the skipped record belongs.

</td></tr></tbody>
</table>**Parent Topic:**[Skipped Records visual task board \(VTB\)](../concept/um-vtb-history.md)


```


### File: platform-administration\upgrade-management\um-process-skipped-records.md

```text
---
title: Process the skipped records list
description: Process the skipped records list to resolve the differences between the upgraded and customized versions of a record. If you have customized or altered a record affected by this upgrade, such as a business rule or script, the upgrade generates a skip log record.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Process the skipped records list

Process the skipped records list to resolve the differences between the upgraded and customized versions of a record. If you have customized or altered a record affected by this upgrade, such as a business rule or script, the upgrade generates a skip log record.

## Before you begin

Role required: admin

## About this task

Review the changes you made to baseline records, such as business rules and scripts, that appear on the skipped records list and revert to the baseline version if appropriate. Post-upgrade, thoroughly test all changes you made to these records.

## Procedure

1.  Navigate to Upgrade Monitor using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade Monitor**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade Monitor**.|

    **Note:** If the upgrade is still in progress, the system displays the [Upgrade Progress](../reference/um-monitor-progress.md) screen. When the upgrade finishes, the system displays the [Upgrade Summary Report](../reference/um-complete-summary.md).

    A list of upgrades is displayed.

2.  After the system displays the Upgrade Summary Report, click the Review changes link in the Skipped box.

    The system displays the [System Upgrades form](../reference/um-system-upgrades-form.md).

3.  Navigate to Review Skipped Records section and – if necessary – scroll to the Skipped Changes to Review related list.

    See [Review skipped records using related lists](um-access-rl.md#) for more information.

4.  Click the row for the first record you want to reconcile.

    The system displays the [Upgrade details form](../reference/um-upgrade-details-form.md) for that record.

5.  Evaluate how you want to resolve the conflict for this record and take the appropriate action:

<table id="table_znb_ggg_rlb"><thead><tr><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Retain the customized record as is and do not update it

</td><td>

After reviewing the changes, set **Resolution Status** to **Reviewed and Retained**.The record moves from the Skipped Changes to Review to Skipped Changes Reviewed related list. See [Review skipped records using related lists](um-access-rl.md#).

</td></tr><tr><td>

Retain the customization by merging changes from the updated object

</td><td>

1.  Click **Resolve Conflicts** to navigate to the [Resolve Conflicts form](../reference/um-resolve-conflicts-form.md).
2.  Review the differences.
3.  To merge a field:
    -   Click the right-arrow button for the field.
    -   Click a text box to view and edit the detailed differences.
    -   When you have merged all appropriate fields, click **Merge**.
 After merging the customization changes:

-   The **Disposition** changes from **Skipped** to **Merged**.
-   The **Resolution Status** changes to **Reviewed and Merged**.
-   The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.


</td></tr><tr><td>

Discard the customization and update the record to match the base system for this upgrade

</td><td>

After reviewing the changes, click **Revert to Base System**.-   The **Disposition** changes from **Skipped** to **Reverted**.
-   The **Resolution Status** changes to **Reviewed and Reverted**.
-   The system creates a Customer Update record.
-   The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.

**Note:** At any time after you revert a customization, you can click **Reapply Changes** to reapply the customization \(undo the revert\).

</td></tr><tr><td>

Review the skip and perform no action on the object

</td><td>

After reviewing the changes, set **Resolution Status** to **Reviewed**. The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.

</td></tr><tr><td>

Leave on the skipped list for a later decision, and note that you have not reviewed the record

</td><td>

From the **Resolution** list, choose **Not Reviewed** to defer the decision on how to handle this conflict. The record stays on the Skipped Changes to Review related list.

</td></tr></tbody>
</table>    **Note:** The system tracks changes to records in an update set so you can apply these changes to another instance later. However, the system does not migrate the upgrade details records from one instance to the next. These records apply to a specific upgrade of a specific instance. If you want to preserve the Comments, Resolutions, or other information from the skipped list, export it from this instance.

6.  In the **Comment** field, write the reasons for making your decision and other information you want to document.

7.  Click **Update**.

    Post-upgrade, thoroughly test all changes you made to the records on the skipped record list.


-   **[System Upgrade form](../reference/um-system-upgrades-form.md)**  
When an upgrade is complete, the System Upgrades form displays key statistics about the upgrade and a related list of skipped records \(the skipped list\).

**Parent Topic:**[Upgrade Monitor tool in Upgrade Console](../concept/um-upgrade-monitor-tool.md)


```


### File: platform-administration\upgrade-management\um-quick-access1.md

```text
---
title: Quick access to plugins and history records
description: Reduce the navigating time by directly accessing plugins, application installation history records, and update set commits history records. The filters for the plugins and history records are automatically implemented in the plugins and history records views.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reviewing upgrade history, Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Quick access to plugins and history records

Reduce the navigating time by directly accessing plugins, application installation history records, and update set commits history records. The filters for the plugins and history records are automatically implemented in the plugins and history records views.

## Before you begin

Role required: admin

## About this task

-   **Plugins and application installation history records**
    1.  Navigate to **System Definition** &gt; **Plugin Installation History**.
    2.  Select any of the plugins or history records to access them directly.
-   **Update set commit history records**
    1.  Navigate to **System Update Sets** &gt; **Update Sets to Commit**.
    2.  Select any of the update sets to directly view the commit history of that update set.

**Parent Topic:**[Reviewing upgrade history](../concept/um-review-history.md)


```


### File: platform-administration\upgrade-management\um-references.md

```text
---
title: Upgrade Console references
description: Find all the miscellaneous information about Upgrade Console in this section.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Console references

Find all the miscellaneous information about Upgrade Console in this section.

-   **[Upgrade Console roles](um-roles.md)**  
Upgrade Console is installed with these roles.

**Parent Topic:**[Upgrade Console](../concept/um-landing-page.md)


```


### File: platform-administration\upgrade-management\um-refreshing-upgrade-plan.md

```text
---
title: Refreshing your Upgrade Plan
description: Refresh your upgrade plan to package all the recently installed plugins and applications into your upgrade plan.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Plans tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Refreshing your Upgrade Plan

Refresh your upgrade plan to package all the recently installed plugins and applications into your upgrade plan.

## Before you begin

Role required: admin

## Procedure

1.  Go to the applications and plugins you need and select **Activate** to install them.

    **Note:** This can be done even after the Upgrade Plan is published.

    The plugin activation starts and installs successfully.

2.  Go to the upgrade plan and refresh it by selecting **Refresh**.![Upgrade plan screen.](../../upgrade-center/image/uc-plan-refresh.png)

    The Refresh Upgrade Plan confirmation message shows up.

3.  After the upgrade plan refreshes, select **Go to Upgrade Plan**.

    **Note:** The **Publish** button is still visible because the updated Upgrade Plan needs to be published.

    The recently installed plugins and applications show up under Upgrade Plan Items related list.


**Parent Topic:**[Upgrade Plans tool in Upgrade Console](../concept/um-upgrade-plans-tool.md)

**Related topics**  


[Building your Upgrade Plan](um-building-upgrade-plan.md)

[Installing your Upgrade Plan](um-installing-upgrade-plan.md)

[Prepare to upgrade with Upgrade Plan](um-prepare-upgrade-plan.md)

[Apply Upgrade Plan on your upgrade](um-apply-upgrade-plan.md)


```


### File: platform-administration\upgrade-management\um-resolve-conflict.md

```text
---
title: Resolve conflicts for an individual record
description: Reconcile differences between your customized record and the changes associated with the upgrade.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Resolve conflicts for an individual record

Reconcile differences between your customized record and the changes associated with the upgrade.

## Before you begin

Role required: admin

## Procedure

1.  From the [Upgrade Details form](../reference/um-upgrade-details-form.md) for the record you are reconciling, click **Resolve Conflicts**.

    The system displays the [Resolve Conflicts form](../reference/um-resolve-conflicts-form.md), which highlights differences between the two versions of the record. The form displays information about the base system record on the left and the customized record on the right.

    **Note:** The system creates a new customer update record when you click **Resolve Conflicts**.

2.  Compare the base system with the customized record for each field on this form.

    For non-script fields, edit the customized record on the right-hand side to include what you want from the base system and the customization.

3.  If this record contains a script, check it for conflicts and resolve.

    1.  Click inside the Script field.

        The system displays the Resolve Conflicts - Script form highlighting areas where the two versions of the script differ.

    2.  Edit the right-hand side so that the script contains whichever content you want. To move a block of code from the left to right side, click the small arrows corresponding to that block in the middle column.
    3.  Click **OK**.

        The system returns to the Resolve Conflicts form.

4.  To save your changes to the record, click **Save Merge**.

    The system sets the **Resolution** for this record to **Reviewed and Merged**.


-   **[Upgrade details form](../reference/um-upgrade-details-form.md)**  
From the Upgrade Details form, you can review an individual record affected by the upgrade and reconcile conflicts between the upgrade and customizations.
-   **[Resolve Conflicts form](../reference/um-resolve-conflicts-form.md)**  
The Resolve Conflicts form you compare to the base system version with the customized version of a record and reconcile the differences.

**Parent Topic:**[Upgrade Monitor tool in Upgrade Console](../concept/um-upgrade-monitor-tool.md)


```


### File: platform-administration\upgrade-management\um-resolve-conflicts-form.md

```text
---
title: Resolve Conflicts form
description: The Resolve Conflicts form you compare to the base system version with the customized version of a record and reconcile the differences.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Resolve conflicts for an individual record, Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Resolve Conflicts form

The Resolve Conflicts form you compare to the base system version with the customized version of a record and reconcile the differences.

![Image showing Resolve Conflicts form](../../upgrade-center/image/uc-resolve-conflict-form.png)

## Fields

The fields this form displays depend on the type of record you are reconciling. The left column shows the records fields in the base system, including the proposed changes that are part of the upgrade. The right column shows the fields for your customized record.

**Parent Topic:**[Resolve conflicts for an individual record](../task/um-resolve-conflict.md)


```


### File: platform-administration\upgrade-management\um-resolve-skipped-update.md

```text
---
title: Resolve a skipped update and set a resolution status
description: Review the reason for each skipped record to resolve each skipped update after an upgrade.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Reviewing upgrade history, Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Resolve a skipped update and set a resolution status

Review the reason for each skipped record to resolve each skipped update after an upgrade.

## Before you begin

Role required: admin

## About this task

You resolve an update by either retaining the customization or by merging or overwriting the customization with the base system update.

**Note:** Objects that are customized and that did not change in the base system since the last upgrade require no action on your part.

When an object is customized, the system adds a corresponding record to the Customer Updates \[sys\_update\_xml\] table and then maintains current version information for all customized objects. The upgrade process skips changes to objects that have a current version in the Customer Updates table. When you follow the procedure, you perform one of the following actions:

-   Retain a customization with no changes
-   Retain a customization by merging changes from the updated object
-   Revert a customized object to the updated version \(that is, overwrite the customization\)
-   Review the skip and perform no action on the object

## Procedure

1.  Navigate to Upgrade History using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade History**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade History**.|

    A list of upgrades is displayed.

2.  Select the desired software version.

3.  In the Skipped Changes to Review related list, select the update record to resolve.

    See [Review skipped records using related lists](um-access-rl.md#).

4.  Review the list of changes.

    For text fields, you can click in the field to open the Diff/Merge tool.

    To review the differences, Click a text box to view and edit the detailed differences.

5.  Perform one of the following actions.

    You have the option to add a **Comment** to any record, for example, to explain the action to future reviewers.

<table id="table_cqj_4jv_dlb"><thead><tr><th>

Field

</th><th>

Input Value

</th></tr></thead><tbody><tr><td>

Retain the customized record as is and do not update it.

</td><td>

After reviewing the changes, set **Resolution Status** to **Reviewed and Retained**.The record moves from the Skipped Changes to Review to Skipped Changes Reviewed related list.

</td></tr><tr><td>

Retain the customization by merging changes from the updated object.

</td><td>

1.  Click**Resolve Conflicts** to navigate to the Resolve Conflicts form.
2.  Review the differences.
3.  To merge a field:
    -   Click the right-arrow button for the field.
    -   Click a text box to view and edit the detailed differences.
    -   When you have merged all appropriate fields, click **Merge**.
 After merging the customization changes:

-   The Resolution Status changes to Reviewed and Merged.
-   The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.


</td></tr><tr><td>

Discard the customization and update the record to match the base system for this upgrade.

</td><td>

After reviewing the changes, click **Revert to Base System**.-   **Disposition** changes from **Skipped** to **Reverted**.
-   **Resolution Status** changes to **Reviewed and Reverted**.
-   The system creates a Customer Update record.
-   The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.
 **Note:** At any time after you revert a customization, you can click **Reapply Changes** to reapply the customization.

</td></tr><tr><td>

Review the skip and perform no action on the object.

</td><td>

After reviewing the changes, set **Resolution Status** to **Reviewed**. The record moves from the Skipped Changes to Review to the Skipped Changes Reviewed related list.

</td></tr><tr><td>

Leave on the skipped list for a later decision, and note that you have not reviewed the record.

</td><td>

From the **Resolution** list, choose **Not Reviewed** to defer the decision on how to handle this conflict. The record stays on the Skipped Changes to Review related list.

</td></tr></tbody>
</table>6.  Click **Update**.

7.  Repeat the process to resolve each update record in the list.


## Result

Only skipped updates with a **Resolution Status** of **Not Reviewed** or without a resolution set appear in the Skipped Changes to Review related list. Any action you take that changes the **Resolution Status** to a value other than **Not Reviewed** or **--None--** removes the skipped update from list and moves it to the Skipped Changes Reviewed related list.

**Parent Topic:**[Reviewing upgrade history](../concept/um-review-history.md)


```


### File: platform-administration\upgrade-management\um-revert-customization.md

```text
---
title: Revert a customization
description: To prevent customizations from being overwritten by system upgrades, the upgrade process automatically skips changes to objects that have been customized. You may want to overwrite your customizations when a software upgrade contains a feature that you would like to implement.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reviewing upgrade history, Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Revert a customization

To prevent customizations from being overwritten by system upgrades, the upgrade process automatically skips changes to objects that have been customized. You may want to overwrite your customizations when a software upgrade contains a feature that you would like to implement.

## Before you begin

Role required: admin

## About this task

To identify customized objects, the system adds a corresponding record in the Customer Updates \[sys\_update\_xml\] table. The table maintains the current version information for all objects that have been customized. The upgrade process skips changes to objects that have entries in the table. The upgrade process does not skip objects if only excluded fields have changed.

## Procedure

1.  Navigate to Upgrade History using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade History**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade History**.|

    A list of upgrades is displayed.

2.  Select the desired software version.

3.  Filter the Upgrade Details related list by **Disposition is Skipped**.

4.  Add another filter condition for **Changed is True** to return only the objects that have changed since the last upgrade.

5.  Select the update record to implement.

    The **File differences** field displays a side-by-side comparison of the customization and the default version. Deletions are highlighted in red, additions in green, and modifications in yellow.

6.  Click **Revert to base system** to overwrite your customized object with the system default version.

    -   The **Disposition** changes from **Skipped** to **Reverted**.
    -   After you revert a customization, you have the option to click **Reapply Changes** to reapply your customizations \(undo the revert\).

**Parent Topic:**[Reviewing upgrade history](../concept/um-review-history.md)


```


### File: platform-administration\upgrade-management\um-review-history.md

```text
---
title: Reviewing upgrade history
description: The Upgrade History module tracks every upgrade made to an instance. You can also view the complete report of an old upgrade or a recently completed upgrade version using this module.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Reviewing upgrade history

The Upgrade History module tracks every upgrade made to an instance. You can also view the complete report of an old upgrade or a recently completed upgrade version using this module.

-   [Upgrade History related lists](../task/um-access-rl.md#): Use the related lists to resolve, track and review the skipped records in an upgrade
-   [Visual task board \(VTB\) view of skipped records](um-vtb-history.md): Use the VTB view to see the resolution status of any previous upgrade with skipped records

-   **[Review skipped records using related lists](../task/um-access-rl.md#)**  
Use different related lists to resolve, track and review the skipped records in an upgrade.
-   **[Revert a customization](../task/um-revert-customization.md)**  
To prevent customizations from being overwritten by system upgrades, the upgrade process automatically skips changes to objects that have been customized. You may want to overwrite your customizations when a software upgrade contains a feature that you would like to implement.
-   **[Resolve a skipped update and set a resolution status](../task/um-resolve-skipped-update.md)**  
Review the reason for each skipped record to resolve each skipped update after an upgrade.
-   **[Skipped Records visual task board \(VTB\)](um-vtb-history.md)**  
View the resolution status of any previous upgrade with skipped records using the visual task board \(VTB\) view. An upgrade history record is created for each upgrade that is run.
-   **[View import history](../task/um-import-history.md)**  
View your import history by accessing the **My Application Import History** module.
-   **[Quick access to plugins and history records](../task/um-quick-access1.md)**  
Reduce the navigating time by directly accessing plugins, application installation history records, and update set commits history records. The filters for the plugins and history records are automatically implemented in the plugins and history records views.
-   **[Explore upgrade history log](../task/um-explore-history-log.md)**  
Reduce processing time by extracting all upgrade related logs into a separate file named database-upgrade\_&lt;timestamp&gt;.log. You can also zip the file and attach it to upgrade history.

**Parent Topic:**[Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md)


```


### File: platform-administration\upgrade-management\um-review-skipped-records-upgrade-plan.md

```text
---
title: Review skipped records with upgrade plan
description: Review the skipped records after the completion of the upgrade.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Apply Upgrade Plan on your upgrade, Upgrade Plans tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Review skipped records with upgrade plan

Review the skipped records after the completion of the upgrade.

## Before you begin

**Note:** This process is applicable only if you have enabled the GLIDE\_UPGRADE\_PLAN\_INCLUDE\_SKIPS property.

Role required: admin

## Procedure

1.  Once the upgrade completes, scroll down to see the skipped records with upgrade plan.

    -   Total: Total number of skipped records
    -   Resolved: Total records from the upgrade plan that have been auto-resolved
    -   To review: Total records left to be reviewed manually
    **Note:** After using the upgrade plan, the Global Application is created and all the records move to the Global Application. As soon as you create the Global Application, the new update sets show up.

    You won’t be allowed to choose the skipped records that are captured by the upgrade plan, regardless of whether they are being reviewed. If the customizations are coming from different instances, then the skipped records are required to be reviewed.

2.  Select the To review link to look at the records that need to be reviewed manually.


**Parent Topic:**[Apply Upgrade Plan on your upgrade](um-apply-upgrade-plan.md)


```


### File: platform-administration\upgrade-management\um-roles.md

```text
---
title: Upgrade Console roles
description: Upgrade Console is installed with these roles.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Console roles

Upgrade Console is installed with these roles.

To learn more about managing subscriptions, see [Managing per-user subscriptions in Subscription Management](../../subscription-management/concept/managing-user-subscriptions-v2.md) and contact your account representative.

## System administrator \[admin\]

Access all tables, tools and information within Upgrade Console on your instance.

-   **Contains Roles**

    List of roles contained within the role.

    -   sn\_templated\_snip.template\_snippet\_admin
    -   sn\_employee.admin
    -   taxonomy\_admin
    -   sn\_ace.ace\_user
    -   sn\_hr\_sp.esc\_admin
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevate to a privileged role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/t_ElevateToAPrivilegedRole.md).

    No.

-   **Special considerations**

    None.


**Parent Topic:**[Upgrade Console references](um-references.md)


```


### File: platform-administration\upgrade-management\um-skipped-rules-explore.md

```text
---
title: Explore Upgrade Skipped Record Rules Editor in Upgrade Console
description: Configure skipped record rules with the use of Upgrade Skipped Record Rules Editor to automate or facilitate the resolution of data inconsistencies arising from the upgrade process.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console summary, Explore, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Explore Upgrade Skipped Record Rules Editor in Upgrade Console

Configure skipped record rules with the use of Upgrade Skipped Record Rules Editor to automate or facilitate the resolution of data inconsistencies arising from the upgrade process.

Formulate automated resolution rules to mitigate potential customization conflicts following an upgrade. These rules can be configured to execute autonomously during the upgrade process or manually initiated post-upgrade.

Starting Xanadu release, new skipped rules have been introduced by default to help you auto-retain certain customizations during the upgrade process. This eliminates the need for manual review of the skipped records generated during the upgrade process.

The following is the list of tables from which if any skipped record is being generated as a metadata file, the customizations are retained by default with the new skipped rules:

-   sys\_ui\_section
-   sys\_ui\_form
-   sys\_ui\_form\_section
-   sysevent\_email\_action
-   sys\_ui\_related\_list
-   sys\_ui\_list
-   sys\_choice
-   sys\_choice\_set
-   sys\_report
-   pa\_dashboards
-   wf\_workflow

**Note:** For wf\_workflow\_version table, the new skipped rules automatically sets the generated skipped records to **Keep My Modifications \(Always Retain\)**. This table is generally used for configuration changes and doesn’t need to be reviewed.

The skipped records that are retained automatically by the default skipped rules are found in the Skipped Changes Reviewed related list.

![Image showing retained skipped rules in the Skipped Changes Reviewed related list](../../upgrade-center/image/uc-default-skipped-rules.png)

**Note:** You can also find a comment for each retained skipped record to show the related table it was generated from during the upgrade process.

See [Upgrade Skipped Record Rules Editor tool in Upgrade Console](um-skipped-rules-tool.md) for more information.


```


### File: platform-administration\upgrade-management\um-skipped-rules-tool.md

```text
---
title: Upgrade Skipped Record Rules Editor tool in Upgrade Console
description: Create skipped record rules, based on your specified conditions, to define customizations post-upgrade. Subsequently, execute these rules to resolve skipped records during or after the upgrade process, either automatically or on demand.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Skipped Record Rules Editor tool in Upgrade Console

Create skipped record rules, based on your specified conditions, to define customizations post-upgrade. Subsequently, execute these rules to resolve skipped records during or after the upgrade process, either automatically or on demand.

-   **[Create a skipped record rule](../task/um-create-skipped-record-rule.md)**  
Create skipped record rules based on your set conditions to define your customizations after an upgrade.
-   **[Execute a skipped record rule](../task/um-execute-skipped-record-rule.md#)**  
Run skipped record rules based on your set conditions to resolve skipped records in an upgrade. The rules either execute automatically during an upgrade or can run on demand after an upgrade.

**Parent Topic:**[Upgrade Console tools](../reference/um-tools.md)

**Related topics**  


[ATF Test Generator and Cloud Runner tool in Upgrade Console](um-atf-tool.md)

[Cloning tool in Upgrade Console](um-cloning-tool.md)

[Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md)

[Upgrade Monitor tool in Upgrade Console](um-upgrade-monitor-tool.md)

[Now Support in Upgrade Console](um-now-support.md)

[Upgrade Preview tool in Upgrade Console](um-upgrade-preview-tool.md)

[Upgrade Plans tool in Upgrade Console](um-upgrade-plans-tool.md)


```


### File: platform-administration\upgrade-management\um-system-upgrades-form.md

```text
---
title: System Upgrade form
description: When an upgrade is complete, the System Upgrades form displays key statistics about the upgrade and a related list of skipped records \(the skipped list\).
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Process the skipped records list, Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# System Upgrade form

When an upgrade is complete, the System Upgrades form displays key statistics about the upgrade and a related list of skipped records \(the skipped list\).

![Image showing the System Upgrades form](../../upgrade-center/image/uc-system-upgrade-form.png)

<table id="table_b5b_p14_dlb"><thead><tr><th>

Field

</th><th>

Input Value

</th></tr></thead><tbody><tr><td>

From

</td><td>

Version of the instance before upgrading.

</td></tr><tr><td>

To

</td><td>

Version of the instance after upgrading.

</td></tr><tr><td>

Upgrade started

</td><td>

Time of the start of the upgrade.

</td></tr><tr><td>

Upgrade finished

</td><td>

Time at which the upgrade completed.

</td></tr><tr><td>

Changes skipped

</td><td>

Total number of records that are different from the previous upgrade and the upgrade component was not applied, mostly due to customization.

</td></tr><tr><td>

Changes applied

</td><td>

Total number of changes that are applied as a part of this upgrade**Changes applied** is sum of updated, different records, deleted records \(where the value of changed is true\) and inserted records \(where the value of changed is true\).

</td></tr><tr><td>

Changes processed

</td><td>

Total number of records that were processed as a part of this upgrade. Changes processed is the sum of **Changes skipped** and **Changes applied**.

</td></tr><tr><td>

Copies to review

</td><td>

Total number of copied records to review whose base records have been upgraded

</td></tr></tbody>
</table>**Parent Topic:**[Process the skipped records list](../task/um-process-skipped-records.md)


```


### File: platform-administration\upgrade-management\um-tools.md

```text
---
title: Upgrade Console tools
description: Access all the necessary tools you might require for a seamless upgrade experience on your instance.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Console tools

Access all the necessary tools you might require for a seamless upgrade experience on your instance.

You can access the following tools from the Upgrade Console experience.

**Note:** The tools available in Upgrade Console are same for both sub-production and production instances.

-   **[ATF Test Generator and Cloud Runner tool in Upgrade Console](../concept/um-atf-tool.md)**  
Leverage the power of ServiceNow's ATF Test Generator and Cloud Runner to create intelligent, comprehensive regression tests.
-   **[Cloning tool in Upgrade Console](../concept/um-cloning-tool.md)**  
Utilize the System Clone application to duplicate an entire database from one instance to another. This cloning process, commonly employed to replicate a production instance for pre-production testing, leverages the latest nightly backup as the data source.
-   **[Upgrade History tool in Upgrade Console](../concept/um-upgrade-history-tool.md)**  
Utilize the Upgrade History module to maintain a comprehensive record of all upgrades performed on an instance. Access detailed reports for both historical and recent upgrade versions to facilitate analysis and troubleshooting.
-   **[Upgrade Monitor tool in Upgrade Console](../concept/um-upgrade-monitor-tool.md)**  
Leverage Upgrade Monitor to schedule upgrades, monitor their progress, and analyze post-upgrade results, including conflict resolution.
-   **[Now Support in Upgrade Console](../concept/um-now-support.md)**  
Try contacting Now Support if you need any assistance regarding Upgrade Console.
-   **[Upgrade Preview tool in Upgrade Console](../concept/um-upgrade-preview-tool.md)**  
Use the Upgrade Preview module to have an insight about the experience of an upgrade prior to the actual upgrade. You can explore and preview upgrades to different ServiceNow release versions and see how your instance might be impacted with your current configurations.
-   **[Upgrade Skipped Record Rules Editor tool in Upgrade Console](../concept/um-skipped-rules-tool.md)**  
Create skipped record rules, based on your specified conditions, to define customizations post-upgrade. Subsequently, execute these rules to resolve skipped records during or after the upgrade process, either automatically or on demand.
-   **[Upgrade Plans tool in Upgrade Console](../concept/um-upgrade-plans-tool.md)**  
Accelerate your upgrades using the Upgrade Plan that automates the installation of applications during upgrades, giving you a seamless upgrade experience. It helps you define applications and target versions to be installed in your instance.

**Parent Topic:**[Using Upgrade Console](../concept/um-using.md)


```


### File: platform-administration\upgrade-management\um-upgrade-details-form.md

```text
---
title: Upgrade details form
description: From the Upgrade Details form, you can review an individual record affected by the upgrade and reconcile conflicts between the upgrade and customizations.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Resolve conflicts for an individual record, Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade details form

From the Upgrade Details form, you can review an individual record affected by the upgrade and reconcile conflicts between the upgrade and customizations.

![Image showing the Upgrade Details form](../../upgrade-center/image/uc-upgrade-details-form.png)

<table id="table_znb_ggg_rlb"><thead><tr><th>

Field

</th><th>

Input value

</th></tr></thead><tbody><tr><td>

File name

</td><td>

The record the system has flagged as needing to be reconciled.

</td></tr><tr><td>

Priority

</td><td>

The priority the system has assigned to resolving this conflict. Values range from one to five, with one representing the highest priority.

</td></tr><tr><td>

Comment

</td><td>

Comments to document your decisions about reconciling this record.

</td></tr><tr><td>

Resolution

</td><td>

How you elected to resolve this conflict:-   **Not reviewed**: Not yet reviewed
-   **Reviewed**: Reviewed but no action yet taken
-   **Reviewed and Merged**: Made changes to the record to reconcile the customized and upgraded versions
-   **Reviewed and Retained**: Left customizations in place without update from upgrade
-   **Reviewed and Reverted**: Customizations discarded, record updated according to upgrade

For more information, see [Process the skipped records list](../task/um-process-skipped-records.md).

</td></tr><tr><td>

Disposition

</td><td>

Action performed on this file during the selected upgrade:-   Inserted: The system inserted a new record
-   Updated: The system updated the record
-   Deleted: The system deleted the record
-   Skipped: The system did not change this record in order to preserve customizations
-   Reverted: This record was reverted to the base version
-   Table not found: The system could not find the table that contains this record
-   Unchanged: The system did not change this record because the baseline component has not changed since the last release
-   Skipped Manual Merge: The system did not change this record because updating it requires manual intervention
-   Skipped Apply Once: The system skipped this record because it had already applied an update from an xml file in the apply once folder
-   Not Latest: The system applied a change, but this change was overwritten later during the same upgrade.

</td></tr><tr><td>

Type

</td><td>

Type of the record, for example, Script include.

</td></tr><tr><td>

Target name

</td><td>

Name of the skipped record, if applicable.

</td></tr><tr><td>

Update set

</td><td>

Unused.

</td></tr><tr><td>

Plugin

</td><td>

The plugin containing this record.

</td></tr><tr><td>

Table

</td><td>

The table containing this record.

</td></tr></tbody>
</table>**Parent Topic:**[Resolve conflicts for an individual record](../task/um-resolve-conflict.md)


```


### File: platform-administration\upgrade-management\um-upgrade-history-explore.md

```text
---
title: Explore Upgrade History in Upgrade Console
description: The Upgrade History module maintains a comprehensive record of all upgrades performed on an instance. This module allows you to access detailed reports for both historical and recent upgrade versions.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console summary, Explore, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Explore Upgrade History in Upgrade Console

The Upgrade History module maintains a comprehensive record of all upgrades performed on an instance. This module allows you to access detailed reports for both historical and recent upgrade versions.

To view an upgrade history record, navigate to Upgrade Console in one of the ways.

<table id="table_oqw_5jr_hdc"><thead><tr><th>

Option

</th><th>

Steps

</th></tr></thead><tbody><tr><td>

Using left navigation

</td><td>

1.  Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Console** &gt; **Upgrade History**.
2.  Select an upgrade from the list. On selecting an upgrade from the list, the System Upgrades form appears.

</td></tr><tr><td>

Using Admin tab option

</td><td>

1.  Navigate to **Admin** &gt; **Upgrade Console** &gt; **Upgrade History**.
2.  Select an upgrade from the list. On selecting an upgrade from the list, the System Upgrades form appears.

</td></tr></tbody>
</table>|Field|Description|
|-----|-----------|
|From|Name of the previous .war file \(version\).|
|To|Name of the applied .war file \(version\).|
|Upgrade started|Time stamp when the upgrade process began.|
|Upgrade finished|Time stamp when the upgrade process was completed.|

<table id="table_mc5_sql_hdc"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Changes skipped

</td><td>

Total number of records that are different from the previous upgrade and the upgrade component was not applied, mostly due to customization.

</td></tr><tr><td>

Changes applied

</td><td>

Total number of changes that are applied as a part of this upgrade**Changes applied** is sum of updated and different records, added to the number of deleted records \(where the value of changed is true\) added to the number of inserted records \(where the value of changed is true\).

</td></tr><tr><td>

Changes processed

</td><td>

Total number of records that were processed as a part of this upgrade. Changes processed is the sum of **Changes skipped** and **Changes applied**.

</td></tr><tr><td>

Copies to review

</td><td>

Total number of copied records to review whose base records have been upgraded.

</td></tr></tbody>
</table>See [Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md) for more information.


```


### File: platform-administration\upgrade-management\um-upgrade-history-tool.md

```text
---
title: Upgrade History tool in Upgrade Console
description: Utilize the Upgrade History module to maintain a comprehensive record of all upgrades performed on an instance. Access detailed reports for both historical and recent upgrade versions to facilitate analysis and troubleshooting.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade History tool in Upgrade Console

Utilize the Upgrade History module to maintain a comprehensive record of all upgrades performed on an instance. Access detailed reports for both historical and recent upgrade versions to facilitate analysis and troubleshooting.

See [Reviewing upgrade history](um-review-history.md) for more information.

-   **[Reviewing upgrade history](um-review-history.md)**  
The Upgrade History module tracks every upgrade made to an instance. You can also view the complete report of an old upgrade or a recently completed upgrade version using this module.

**Parent Topic:**[Upgrade Console tools](../reference/um-tools.md)

**Related topics**  


[ATF Test Generator and Cloud Runner tool in Upgrade Console](um-atf-tool.md)

[Cloning tool in Upgrade Console](um-cloning-tool.md)

[Upgrade Monitor tool in Upgrade Console](um-upgrade-monitor-tool.md)

[Now Support in Upgrade Console](um-now-support.md)

[Upgrade Preview tool in Upgrade Console](um-upgrade-preview-tool.md)

[Upgrade Skipped Record Rules Editor tool in Upgrade Console](um-skipped-rules-tool.md)

[Upgrade Plans tool in Upgrade Console](um-upgrade-plans-tool.md)


```


### File: platform-administration\upgrade-management\um-upgrade-monitor-explore.md

```text
---
title: Explore Upgrade Monitor in Upgrade Console
description: The Upgrade Monitor module is a powerful tool for scheduling upgrades, monitoring their progress, and analyzing post-upgrade results, including conflict resolution.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Upgrade Console summary, Explore, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Explore Upgrade Monitor in Upgrade Console

The Upgrade Monitor module is a powerful tool for scheduling upgrades, monitoring their progress, and analyzing post-upgrade results, including conflict resolution.

## Access Upgrade Monitor

If you log in with the admin role while an upgrade is underway, the system automatically displays the Upgrade Progress screen. If no upgrade is in progress, you can follow one of the following ways.

|Option|Navigation|
|------|----------|
|Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Console** &gt; **Upgrade Monitor**.|
|Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Console** &gt; **Upgrade Monitor**.|

## How the Upgrade Monitor fits into the upgrade process

**Note:** For detailed information about the upgrade process, see [Upgrade your instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/release-notes/upgrades-overview.md).

The Upgrade Monitor concerns only part of the larger upgrade process:

1.  Clone the production instance to a test instance and a non-production instance.
2.  Apply the upgrade to the non-production instance.
3.  On the upgraded non-production instance, [Process the skipped records list](../task/um-process-skipped-records.md).
4.  Test the non-production instance to confirm that the instance still works and performs adequately. Compare to benchmark data from pre-upgrade production instance.
5.  Apply the upgrade to the test instance. Import the update sets created on the non-production instance when you processed the skipped list. Repeat the testing to make sure that the process is working.
6.  Apply the upgrade to the production instance. Import the update sets created on the non-production instance when you processed the skipped list. Test to confirm that the instance works and performs adequately.

Within this larger process, the Upgrade Monitor helps you upgrade individual instances:

-   During the upgrade, it shows where in the process the system is
-   After the upgrade, it reports what the upgrade did and for how long
-   As you upgrade the first non-production instance, it helps you resolve conflicts between customizations and changes that are part of the upgrade
-   On non-production instances, it provides information that can help you estimate how long the upgrade might take on the production instance

## Monitoring an individual instance as it upgrades

While the upgrade is in progress the Upgrade Progress shows what the upgrade process has done, what it is doing, and what remains to be done.

When the upgrade completes, the system displays the Upgrade Summary Report. The Upgrade Summary Report provides information about conflicts between customizations versus changes in the upgrade and provides a link to reconcile these conflicts. For information about understanding and resolving these conflicts, see [Process the skipped records list](../task/um-process-skipped-records.md) list.

When you upgrade a non-production instance, the Upgrade Summary Report can help you estimate how long the same upgrade might take on a production instance. For details about the elements on this report and how to use this information, see [Upgrade details form](../reference/um-upgrade-details-form.md).

## Resolving conflicts

To prevent losing customizations, the system skips upgrading records you have customized and provides you with a list of these skipped records.

As you upgrade your first non-production instance, go through the Skipped Changes to Review related list and resolve these conflicts. The system records the changes you make during this process in update sets. See [Review skipped records using related lists](../task/um-access-rl.md#), for more information.

You do not need to reconcile the skipped list on any instances you later upgrade. Instead, you can apply the upgrade then import the update sets containing your changes.

For details on reconciling conflicts, see [Process the skipped records list](../task/um-process-skipped-records.md).

See [Upgrade Monitor tool in Upgrade Console](um-upgrade-monitor-tool.md) for more information.


```


### File: platform-administration\upgrade-management\um-upgrade-monitor-tool.md

```text
---
title: Upgrade Monitor tool in Upgrade Console
description: Leverage Upgrade Monitor to schedule upgrades, monitor their progress, and analyze post-upgrade results, including conflict resolution.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Monitor tool in Upgrade Console

Leverage Upgrade Monitor to schedule upgrades, monitor their progress, and analyze post-upgrade results, including conflict resolution.

## Scheduling and monitoring an upgrade

Use the Upgrade Monitor module to schedule and monitor the status of an ongoing upgrade in your instance. You can also view the upgrade summary and the list of records causing conflicts in your instance once the upgrade is complete.

-   [Monitoring an upgrade](../task/um-monitor-instance-upgrade.md): Monitor the progress of an ongoing upgrade in your instance
-   [Process the skipped records list](../task/um-process-skipped-records.md): Resolve the differences between the upgraded and customized versions of a record by processing the skipped records list
-   [Resolve conflicts of a record](../task/um-resolve-conflict.md): Resolve conflicts between your customized record and the changes associated with the upgrade

-   **[Monitor an upgrade to an instance](../task/um-monitor-instance-upgrade.md)**  
Monitor the progress of an ongoing upgrade in an instance with the Upgrade Monitor. When the upgrade is done, you can view a summary of the results on the Upgrade Summary Report.
-   **[Process the skipped records list](../task/um-process-skipped-records.md)**  
Process the skipped records list to resolve the differences between the upgraded and customized versions of a record. If you have customized or altered a record affected by this upgrade, such as a business rule or script, the upgrade generates a skip log record.
-   **[Resolve conflicts for an individual record](../task/um-resolve-conflict.md)**  
Reconcile differences between your customized record and the changes associated with the upgrade.

**Parent Topic:**[Upgrade Console tools](../reference/um-tools.md)

**Related topics**  


[ATF Test Generator and Cloud Runner tool in Upgrade Console](um-atf-tool.md)

[Cloning tool in Upgrade Console](um-cloning-tool.md)

[Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md)

[Now Support in Upgrade Console](um-now-support.md)

[Upgrade Preview tool in Upgrade Console](um-upgrade-preview-tool.md)

[Upgrade Skipped Record Rules Editor tool in Upgrade Console](um-skipped-rules-tool.md)

[Upgrade Plans tool in Upgrade Console](um-upgrade-plans-tool.md)


```


### File: platform-administration\upgrade-management\um-upgrade-plan-explore.md

```text
---
title: Explore Upgrade Plan in Upgrade Console
description: The Upgrade Plan automates the installation of applications during upgrades, providing a seamless upgrade experience. Define applications and target versions to be installed in your instance and accelerate your upgrade process.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Upgrade Console summary, Explore, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Explore Upgrade Plan in Upgrade Console

The Upgrade Plan automates the installation of applications during upgrades, providing a seamless upgrade experience. Define applications and target versions to be installed in your instance and accelerate your upgrade process.

Navigate to Upgrade Plan using one of the following ways.

|Option|Navigation|
|------|----------|
|Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Console** &gt; **Upgrade Plan**.|
|Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Console** &gt; **Upgrade Plan**.|

You will need the following instances to use Upgrade Plan.

-   Builder instance: Build your upgrade plan
-   Consumer instance: Implement your created upgrade plan

**Note:** Ensure that you have upgraded your instance to the latest available version to build the upgrade plan. It is recommended to configure your dev instance as your builder instance. You are required to install the upgrade plan before upgrading your consumer instance. See [Upgrade Plan Properties](../../upgrade-center/reference/uc-properties.md#table_h4b_wq2_5tb) for more details.

When you upgrade an instance, resolutions are skipped, and customizations are often loaded post upgrade. This causes temporary breakdown of features until fully loaded. Tasks like committing update sets, installing new plugins and applications, and multiple updates are also time consuming. Use the Upgrade Plan feature to automate these post-upgrade tasks by tracking your actions and replaying the steps on all the required instances. You don’t have to manually apply post-upgrade tasks which helps in reducing downtime.

**Note:** After upgrading to the latest version, you will see some skipped records. Some of those records will already be marked as reviewed and some of them will need to be reviewed.

Starting in the Yokohama release, customizations and skipped records are not a part of the Upgrade Plan, by default. You can choose to include the customizations and skipped records along with the app installations within the Upgrade Plan by enabling theglide.upgrade.plan.include.skips property. This property controls about when skips and customizations are included when you build or refresh an Upgrade Plan.

-   When glide.upgrade.plan.include.skips property is **TRUE**, skips and customizations are included when an Upgrade Plan is built or refreshed
-   When glide.upgrade.plan.include.skips property is **FALSE**, skips and customizations aren't included when an Upgrade Plan is built or refreshed. This property has been set to False by default.

You will see one of the following modal messages depending on the scenario:

-   First time user: When you are building your Upgrade Plan for the first time \(the property is disabled by default\)

    ![Screenshot showing first time user for Upgrade Plan](../../upgrade-center/image/uc_up_first_time_user.png)

-   Building the upgrade plan with the property enabled

    ![Screenshot showing building of Upgrade Plan with property enabled](../image/uc_build_up_property_enabled.png)

-   Refreshing the Upgrade Plan with the property disabled \(default\)

    ![Screenshot showing refreshing of the Upgrade Plan with property disabled](../image/uc_refresh_up_property_disabled.png)

-   Refreshing the Upgrade Plan with the property enabled

    ![Screenshot showing refreshing of the Upgrade Plan with property enabled](../image/uc_refresh_up_property_enabled.png)


## Advantages of Upgrade Plan over Update Sets

You can achieve the following using Upgrade Plans:

-   Along with the skipped record resolution, you can also track app and plugin installation.

    **Note:** You won’t be allowed to choose the skipped records that are captured by the upgrade plan. Upgrade plan captures all the skipped records regardless of whether they are reviewed or not and modified or not. If the customizations are coming from different instances, then the skipped records are required to be reviewed.

-   Optimizing the table alters using batch bootstrapping.
-   Manage your customizations using the App Repository.

**Note:** It is recommended to build an Upgrade Plan for each instance upgrade. When you build an upgrade plan on a builder instance, it gets created to the exact same version as the builder instance version \(including patches and hot fixes\). You can’t use the previously created Upgrade Plan for the new instance upgrade. In case of consumer instances, when you install the upgrade plan, its version should match exactly the consumer instance version.

## Persona

If you are using the app repository for active application development, use Upgrade Plan to accelerate your upgrades.

**Note:** If you are currently using the Update Sets and want to catapult your upgrade process, use the Upgrade Plan feature.

## Design considerations

The following are the important considerations while working with Upgrade Plan:

-   Each new instance upgrade requires its own upgrade plan. It can't be shared across upgrades.
-   Only one builder instance is supported to build the Upgrade Plan.
-   Upgrade Plan can’t be uninstalled on a consumer instance. You can roll back the entire upgrade but not partially.
-   The scope of the files moved to **Global Customizations - Upgrade Plan** application by upgrade plan is still global.
-   During an upgrade, only the upgrade plan items with **State=Ready** and **Active=true** are installed on the consumer instances. The rest of the items are skipped.
-   Upgrade sets can’t be included in the Upgrade Plan.
-   Maint only plugins are not allowed in Upgrade Plan.
-   Configure your instance as a builder instance before installing new applications and plugins or during skip resolutions. Otherwise, the actions are not captured by the Upgrade Plan.
-   You can’t view the list of customizations in the Upgrade Plan items view. You can navigate to the respective tables to ensure if the customization has been captured.

See [KB1271313](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1271313) for more information.

## Upgrade Plan background operations

During the building of the upgrade plan, the following operations are done in the background:

-   Skipped records are packaged and uploaded to the App Repository in the form of Global Application and App customization. The following are the 3 types of apps created by Upgrade Plan on your instance and App Repo.

    **Note:** After the packaging is done, you can choose the items from the Upgrade Plan. An Upgrade Plan works at the scope level, so it captures everything and publishes it to the repository.

    -   The global records are packaged into the global customization upgrade plan app and published to the app repo.
    -   The scoped skipped records are packaged into the respective app customization packages.
    -   When the upgrade plan is published, a global application is created, for example, **Upgrade Plan - release name**.
-   Existing ServiceNow features like Global Application and App customization are used as application containers that can be installed in all the required instances. See [Legacy - Global application file management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/servicenow-studio-classic/manage_global_application_files.md) and [Application scope](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/c_ApplicationScope.md) for more information.
-   If you install any applications or plugins, they are also captured in the Upgrade plan. But, since they are application life cycle items, they are never pushed to the App Repository.

During the consumption of the upgrade plan, the following operations are done in the background:

-   At first the upgrade plan is validated and then the source from the app repo is downloaded.
-   Once the source is downloaded, the app is moved to the ready state.

    **Note:** Only the upgrade plan items with **State=Ready** and **Active=true** are installed on the consumer instances. The rest of the items are skipped.

-   Auto-generation of the preview for the upgrade plan.

See [Upgrade Plans tool in Upgrade Console](um-upgrade-plans-tool.md) for more information.


```


### File: platform-administration\upgrade-management\um-upgrade-plans-tool.md

```text
---
title: Upgrade Plans tool in Upgrade Console
description: Accelerate your upgrades using the Upgrade Plan that automates the installation of applications during upgrades, giving you a seamless upgrade experience. It helps you define applications and target versions to be installed in your instance.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Plans tool in Upgrade Console

Accelerate your upgrades using the Upgrade Plan that automates the installation of applications during upgrades, giving you a seamless upgrade experience. It helps you define applications and target versions to be installed in your instance.

Follow the following task to build and apply an upgrade plan to your upgrade.

-   **[Building your Upgrade Plan](../task/um-building-upgrade-plan.md)**  
Build your upgrade plan to experience a seamless and an accelerated upgrade by packaging the applications in an upgrade plan.
-   **[Refreshing your Upgrade Plan](../task/um-refreshing-upgrade-plan.md)**  
Refresh your upgrade plan to package all the recently installed plugins and applications into your upgrade plan.
-   **[Installing your Upgrade Plan](../task/um-installing-upgrade-plan.md)**  
Install your upgrade plan in the consumer instance to implement it in your upgrades.
-   **[Prepare to upgrade with Upgrade Plan](../task/um-prepare-upgrade-plan.md)**  
Prepare your instance upgrade with Upgrade Plan by determining all the applications and plugins are ready to be implemented in the upgrade.
-   **[Apply Upgrade Plan on your upgrade](../task/um-apply-upgrade-plan.md)**  
Apply the selected upgrade plan to your instance upgrade.

**Parent Topic:**[Upgrade Console tools](../reference/um-tools.md)

**Related topics**  


[ATF Test Generator and Cloud Runner tool in Upgrade Console](um-atf-tool.md)

[Cloning tool in Upgrade Console](um-cloning-tool.md)

[Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md)

[Upgrade Monitor tool in Upgrade Console](um-upgrade-monitor-tool.md)

[Now Support in Upgrade Console](um-now-support.md)

[Upgrade Preview tool in Upgrade Console](um-upgrade-preview-tool.md)

[Upgrade Skipped Record Rules Editor tool in Upgrade Console](um-skipped-rules-tool.md)


```


### File: platform-administration\upgrade-management\um-upgrade-preview-explore.md

```text
---
title: Explore Upgrade Preview in Upgrade Console
description: Leverage the Upgrade Preview module to conduct in-depth assessments of your ServiceNow instance prior to an upgrade. Explore how different release versions may affect your current configurations and fine-tune your upgrade plan accordingly.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Upgrade Console summary, Explore, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Explore Upgrade Preview in Upgrade Console

Leverage the Upgrade Preview module to conduct in-depth assessments of your ServiceNow instance prior to an upgrade. Explore how different release versions may affect your current configurations and fine-tune your upgrade plan accordingly.

The preview status info and link in the message displayed on top of the Upgrade Preview page states the current status of the ongoing preview process. Since you can get an accurate prediction on the new and existing applications and their skipped records, the preview execution time has increased considerably. Click on the link in the message to see the status of the preview process.

![Image showing the status message and link](../../upgrade-center/image/uc-status-message-link.png)

The Execution Tracker record shows up on clicking the progress link in the message. Click Show status related list to show the current status of the executed preview process.

![Image showing the preview screen](../../upgrade-center/image/uc-preview-screen.png)

**Note:** Depending on the eligibility of your instance, the list of available target versions for preview varies. Only versions that are allowed for a particular instance to be upgraded to, show up on the list. If your instance is not eligible to be upgraded to any version, the drop-down menu is empty.

The following cards show up with more information.

<table id="table_tht_fp2_clb"><thead><tr><th>

Card names

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Current version

</td><td>

Name of the current version.-   Upgraded on: Date on which the instance got upgraded to the current version
-   End of life: Link to [KB0610454](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610454) for more information about end of life

</td></tr><tr><td>

Previewing version

</td><td>

Information about the previewing version shows up. If you haven't previewed any version, you are expected to select a version for preview and click **Go**. If you have already previewed a version, the following information shows up.-   Preview created: Date on which the preview was created
-   View preview details: Link to the Upgrade Preview form

 **Note:** Click **Refresh preview** if you want to regenerate a new preview of the same target version. Although clicking **Refresh preview** regenerates the skipped list, the reverted records won't get skipped. If you have reviewed and retained some records, they get replaced as soon as you click **Refresh preview**.

</td></tr><tr><td>

Scheduled upgrade

</td><td>

Name of the next upgrade that has been scheduled to start. If there is no currently scheduled upgrade, the card shows No upgrade scheduled.**Note:** This card can have different messages depending on the schedule of the upgrade.

 If there is an upgrade scheduled, the following information shows up.

 -   Estimated upgrade duration: Estimated duration needed to complete the scheduled upgrade

**Note:** If this is your first upgrade, there will be no information about estimated upgrade duration.

-   Next scheduled upgrade: Date and time on which the next upgrade has been scheduled to start.

</td></tr><tr><td>

Find out what's new and changed

</td><td>

Links to view the new and changed features in the current upgrade version. The following three links show up when you click **Go** to preview the upgrade version.-   Problem fixes: Fixes that have been made since the last upgrade version
-   Personalized release notes: Release notes summary for the previewed version
-   Known error articles: Errors that have been identified but not yet resolved

 **Note:** These links don't show up if you haven't previewed any upgrades.

</td></tr><tr><td>

Skipped list prediction**Note:** If you are using Upgrade Plan, the card name changes to Skipped list prediction with plans.

</td><td>

Information about the predicted skipped records. See [Preview predicted changes](../reference/um-previewed-changes.md) for more details.-   Total record changes: Total number of records that are predicted to change when the upgrade occurs. Total record changes also include possible predicted skipped files known as Predicted skipped records.

Review changes: Link to the list of records that have changed and can be reviewed

-   Predicted skipped records: Total number of records that have been predicted to be skipped.

    -   Total: Total predicted skipped records
    -   To review: Predicted skipped records to be reviewed
    -   Reviewed: Predicted skipped records that have been reviewed
    -   Resolved: Predicted skipped records that have been resolved by implementing the rules

**Note:** This entry shows up on the card only when rules are executed on the skipped records. You will also see a link to create a skipped record rule if either there are no existing rules or the existing rules aren't executed.

**Note:** Skipped record rules and upgrade plans can't be implemented together. See [Execute a skipped record rule automatically](../task/um-execute-skipped-record-rule.md#) for more information.

-   Predicted skipped records by priority: Pie chart to represent the predicted skipped records by priority.

**Note:** Click the pie chart to see the list of predicted skipped records.

ServiceNow prioritizes the skipped records based on the importance of the file types. The prioritization is done as follows:

    -   Priority 1 \(highest priority\): UI pages, UI macros, and more
    -   Priority 2: Business Rules, Security ACLs, and more
    -   Priority 3: Reports and more
    -   Priority 4: Form Sections, Choice Sets, and more
    -   Priority 5 \(lowest priority\): everything else

</td></tr><tr><td>

Predicted skipped records by product

</td><td>

Records that have been predicted to be skipped and are sorted as per their product families.![](../../upgrade-center/image/uc-skipped_records_product.png)

 **Note:** The products sorted under the Other category don't have any specific product family.

</td></tr><tr><td>

Application Upgrade Preview

</td><td>

Accurate prediction on the installs and upgrades for new and existing applications and for their specific skipped records. It states the total number of applications that have been either upgraded or installed.**Note:** The skipped records prediction is reflected on the Predicted skipped records by product card.

![Image showing Application Upgrade Preview card](../../upgrade-center/image/uc-upgrade-preview-apps.png)

By default, 10 applications preview details show up. Click View all applications preview details link to view the entire list. It states the name of the application and the following information:

-   Action: The action taken on the specific application. It can either be upgraded for the existing applications or installed for the new applications.
-   From version: States the previous version of the upgraded application \(existing application\).

**Note:** This field is empty if the application is a newly installed application.

-   To version: States the current version to which the existing application has been upgraded.

**Note:** This field shows the current version of the newly installed application.


</td></tr><tr><td>

Predicted Schema Changes

</td><td>

Prediction about the kind of changes in the database based on the upgrade on your instance.![Image showing the Predicted Schema Changes list](../../upgrade-center/image/uc-predicted-schema.png)

By default, 10 predicted schema changes show up. Click View all predicted schema changes link to view the entire list. Changes like new columns, new tables, and new indexes are captured in this section.

</td></tr><tr><td>

Automated Test Framework \(ATF\) results

</td><td>

Percentage of passing ATF tests that ran in the last 30 days.-   Most recent ATF run: Date and time on which the recent ATF tests ran
-   View ATF results: Link to show more information about the recent ATF results

 **Note:** Only the tests which are finished and have passed are considered for the ATF results. If one test runs more than once, only the recent execution is considered in the results.

</td></tr></tbody>
</table>See [Upgrade Preview tool in Upgrade Console](um-upgrade-preview-tool.md) for more information.


```


### File: platform-administration\upgrade-management\um-upgrade-preview-form1.md

```text
---
title: View previewed upgrade
description: Use the Upgrade Preview form to have an alternate view of a previewed upgrade.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Preview tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# View previewed upgrade

Use the Upgrade Preview form to have an alternate view of a previewed upgrade.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to Upgrade Preview using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade Preview**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade Preview**.|

2.  Select the target version to be previewed.

3.  Click **Go** or **Refresh Preview** to run the selected preview.

4.  Click **View preview details** on the **Previewing version** card to view the following related lists.

    -   **Predicted Skips to Review related list**: The Upgrade Preview process informs you about the customizations that are predicted to be skipped during an upgrade. The upgrade preview process the skip files that have been customized. Predicted Skips to Review lists all the skipped files that haven't been reviewed yet.
    -   **Predicted Skips Reviewed related list**: Predicted Skips Reviewed related list displays the records which have previously appeared on the Predicted Skips to Review related list and have been reviewed. When you select a skipped record to review and the **Resolution Status** has been set to a value other than **Not Reviewed**, the updated record moves to the Predicted Skips Reviewed related list.
    -   **Previewed Changes related list**: Previewed Changes related list gives the total number of records that are predicted to change when the upgrade occurs. Total record changes also includes possible predicted skip files known as Predicted skipped records.
    See [Previewed changes](../../upgrade-center/reference/uc-previewed-changes.md) for more details about the related lists.

    ![Image showing Upgrade Preview form](../../upgrade-center/image/uc-upgrade-preview-form.png)

<table id="table_b5b_p14_dlb"><thead><tr><th>

Field

</th><th>

Input Value

</th></tr></thead><tbody><tr><td>

Source version

</td><td>

Current version of the instance

</td></tr><tr><td>

Target version

</td><td>

Target version to which the instance is upgraded to be previewed

</td></tr><tr><td>

Preview status

</td><td>

Status of the preview.-   Pending
-   In Progress
-   Complete
-   Cancelled
-   Failed


</td></tr><tr><td>

Preview Started

</td><td>

Date and time on which the preview started

</td></tr><tr><td>

Preview Finished

</td><td>

Date and time on which the preview completed

</td></tr></tbody>
</table>
**Parent Topic:**[Upgrade Preview tool in Upgrade Console](../concept/um-upgrade-preview-tool.md)


```


### File: platform-administration\upgrade-management\um-upgrade-preview-tool.md

```text
---
title: Upgrade Preview tool in Upgrade Console
description: Use the Upgrade Preview module to have an insight about the experience of an upgrade prior to the actual upgrade. You can explore and preview upgrades to different ServiceNow release versions and see how your instance might be impacted with your current configurations.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Upgrade Preview tool in Upgrade Console

Use the Upgrade Preview module to have an insight about the experience of an upgrade prior to the actual upgrade. You can explore and preview upgrades to different ServiceNow release versions and see how your instance might be impacted with your current configurations.

-   [Preview predicted changes](../reference/um-previewed-changes.md): Preview the changes that have been predicted to occur after an upgrade.
-   [Upgrade Preview form](../task/um-upgrade-preview-form1.md): Alternate view of a previewed upgrade.

-   **[View previewed upgrade](../task/um-upgrade-preview-form1.md)**  
Use the Upgrade Preview form to have an alternate view of a previewed upgrade.
-   **[Preview predicted changes](../reference/um-previewed-changes.md)**  
Use the previewed changes table to view the list of total records that are predicted to change when the upgrade occurs.

**Parent Topic:**[Upgrade Console tools](../reference/um-tools.md)

**Related topics**  


[ATF Test Generator and Cloud Runner tool in Upgrade Console](um-atf-tool.md)

[Cloning tool in Upgrade Console](um-cloning-tool.md)

[Upgrade History tool in Upgrade Console](um-upgrade-history-tool.md)

[Upgrade Monitor tool in Upgrade Console](um-upgrade-monitor-tool.md)

[Now Support in Upgrade Console](um-now-support.md)

[Upgrade Skipped Record Rules Editor tool in Upgrade Console](um-skipped-rules-tool.md)

[Upgrade Plans tool in Upgrade Console](um-upgrade-plans-tool.md)


```


### File: platform-administration\upgrade-management\um-using.md

```text
---
title: Using Upgrade Console
description: Use the Upgrade Console experience to access all the tools, information, and guided setup for a smooth upgrade on your instance.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Using Upgrade Console

Use the Upgrade Console experience to access all the tools, information, and guided setup for a smooth upgrade on your instance.

Review the following for a seamless upgrade experience.

-   **[Upgrade Console tools](../reference/um-tools.md)**  
Access all the necessary tools you might require for a seamless upgrade experience on your instance.

**Parent Topic:**[Upgrade Console](um-landing-page.md)


```


### File: platform-administration\upgrade-management\um-view-loaded-files-plugin.md

```text
---
title: View loaded files for a plugin
description: Get a related list view of all the files loaded for a plugin by clicking View all plugin duration.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Upgrade Summary Report, Monitor an upgrade to an instance, Upgrade Monitor tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# View loaded files for a plugin

Get a related list view of all the files loaded for a plugin by clicking **View all plugin duration**.

## Before you begin

Role required: admin.

## Procedure

1.  Navigate to Upgrade Monitor using one of the following ways.

    |Option|Navigation|
    |------|----------|
    |Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade Monitor**.|
    |Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade Monitor**.|

    **Note:** When the system finishes the upgrade, it displays the Upgrade Summary Report.

2.  Scroll down to **Top 10 Plugins by Duration**.

3.  Click **View all plugin duration**.

    The **System Upgrade Metrics** list of all the plugins and their durations shows up.

4.  Click one of the plugins from the list to open the **System Upgrade Metrics** form view of that plugin.

    The Plugin Files related list of all the loaded files for that plugin is displayed. ![Image showing the System Upgrade Metric form with the duration message and all loaded files](../../upgrade-center/image/uc-plugin-form-view.png)

    **Note:** The total plugin load duration is not the sum of the load duration of all the loaded files for that plugin.


**Parent Topic:**[Upgrade Summary Report](../reference/um-complete-summary.md)


```


### File: platform-administration\upgrade-management\um-vtb-history.md

```text
---
title: Skipped Records visual task board \(VTB\)
description: View the resolution status of any previous upgrade with skipped records using the visual task board \(VTB\) view. An upgrade history record is created for each upgrade that is run.
locale: en-US
release: australia
product: Upgrade Management
classification: upgrade-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reviewing upgrade history, Upgrade History tool in Upgrade Console, Upgrade Console tools, Use, Upgrade Console, Upgrade, Administer the ServiceNow AI Platform]
---

# Skipped Records visual task board \(VTB\)

View the resolution status of any previous upgrade with skipped records using the visual task board \(VTB\) view. An upgrade history record is created for each upgrade that is run.

To view the history report navigate to Upgrade History using one of the following ways.

|Option|Navigation|
|------|----------|
|Using left navigation|Navigate to **All** &gt; **Admin Center** &gt; **Upgrade Management** &gt; **Upgrade History**.|
|Using Admin tab option|Navigate to **Admin** &gt; **Upgrade Management** &gt; **Upgrade History**.|

You can then select an upgrade from the list to view the upgrade history details. Click the **Skipped Record VTB** related link to view and manage the skipped records over VTB.

**Note:** The **Skipped Record VTB** related link shows up only when there are skipped records for the version upgrade.

|Field|Description|
|-----|-----------|
|Not Reviewed|Tasks which have not been reviewed|
|Reviewed|Tasks which have been reviewed|
|Merged|Tasks which have both the old and new changes|
|Retained|Tasks which have retained the updates from the latest upgrade|
|Reverted|Tasks which have reverted its changes to the base system|

The skipped records are prioritized based on the importance of the file types. The prioritization is done as follows:

-   Priority 1 \(highest priority\): UI pages, UI macros, and more
-   Priority 2: Business Rules, Security ACLs, and more
-   Priority 3: Reports and more
-   Priority 4: Form Sections, Choice Sets, and more
-   Priority 5 \(lowest priority\): other

![Image showing the VTB view of skipped records resolution status](../../upgrade-center/image/uc-vtb.png)

-   **[Upgrade History Task form](../reference/um-history-task-form.md)**  
You can update information about a skipped record task using the Upgrade History Task form.
-   **[Previous Resolutions related list](../reference/um-previous-resolutions-rl.md)**  
The Previous Resolutions related list shows the history of the selected skipped record. You can see what resolutions have been done with the selected skipped record in the previous upgrades.
-   **[Update default labels in VTB view](../task/um-label-vtb.md)**  
Filter skipped records in the task board of the VTB with the implementation of color-coded labels. You can filter the skipped records by assigning a color to each of the products.

**Parent Topic:**[Reviewing upgrade history](um-review-history.md)


```


---

## Folder: platform-administration\user-administration



### File: platform-administration\user-administration\application-specific-roles.md

```text
---
title: Application specific roles
description: Applications you install on your instance may include additional roles. Follow the links in this section to see roles installed along with applications.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Base system roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Application specific roles

Applications you install on your instance may include additional roles. Follow the links in this section to see roles installed along with applications.

<table id="table_v41_hxt_bzb" class="custom-rows"><thead><tr><th class="filter">

Workflow

</th><th class="filter">

Product

</th><th>

Roles Documentation Links

</th></tr></thead><tbody><tr><td>

Customer Service Management

</td><td>

Customer Access Management

</td><td>

[Roles installed with customer access management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/r_rolesinstalledwithcustaccessmgmt.md)

</td></tr><tr><td>

Customer Service Management

</td><td>

Customer Service Management

</td><td>

[Roles installed with Customer Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/r_RolesInstalledWithCustomerService.md)

</td></tr><tr><td>

Customer Service Management

</td><td>

Major Issue Management

</td><td>

[Components installed with Major Issue Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/installed-with-major-issue-mgmt.md)

</td></tr><tr><td>

Customer Service Management

</td><td>

OpenFrame

</td><td>

[Components installed with OpenFrame](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/r_InstalledWithOpenFrame.md)

</td></tr><tr><td>

Customer Service Management

</td><td>

Public Sector Digital Services

</td><td>



</td></tr><tr><td>

Customer Service Management

</td><td>

Special Handling Notes

</td><td>

[Components installed with Special Handling Notes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/r_InstalledWithSpecHandNotes.md)

</td></tr><tr><td>

Customer Service Management

</td><td>

Targeted Communications

</td><td>

[Components installed with Targeted Communications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/r_TargetCommInstalledComponents.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Case and Knowledge Management

</td><td>

[Components installed with Case and Knowledge Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/components-installed-with-case-and-knowledge-management.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

HR Service Delivery

</td><td>

[Setting up your Alumni Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/alumni-center/asc-configure.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

HR Service Delivery

</td><td>

[Reference for Document Templates](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/reference-doc-templates.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

HR Service Delivery

</td><td>

v

</td></tr><tr><td>

Employee Service Management

</td><td>

Journey Designer

</td><td>



</td></tr><tr><td>

Employee Service Management

</td><td>

Journey Designer

</td><td>

[Components installed with Journey Accelerator](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/journey-accelerator/components-installed-with-journey-accelerator.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Manager Hub

</td><td>

[Components installed with Manager Hub](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/installed-with-managerhub.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Case Management

</td><td>

[Components installed with Workplace Case Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/components-installed-with-workplace-case-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Calendar Synchronization](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-calendar-synchronization/components-installed-with-workplace-calendar-syncn.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Case Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/components-installed-with-workplace-case-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/safe-workplace/components-installed-with-workplace-safety-mgmt-hr.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/components-installed-with-workplace-move-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Reservations for Microsoft Outlook Add-in](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-service-delivery/components-installed-with-wsd-reservations-outlookaddin.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Reservation Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/components-installed-with-wsd-reservation-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Space Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-space-management/components-installed-with-wsd-space-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Space Mapping](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/wsm-mappedin-components.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Workplace Service Delivery

</td><td>

[Components installed with Workplace Visitor Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-visitor-management/components-installed-with-workplace-visitor-mgmt.md)

</td></tr><tr><td>

Employee Service Management

</td><td>

Vendor Management Workspace

</td><td>



</td></tr><tr><td>

Environmental, Social, and Governance Management

</td><td>

Environmental, Social, and Governance Management

</td><td>

[Components installed with Operational Sustainability Management \(formerly ESG Management\)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/environmental-social-governance/components-installed-with-esg.md)

</td></tr><tr><td>

Governance, Risk, and Compliance

</td><td>

Audit Management

</td><td>

[Components installed with Audit Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/audit-management/r_InstallWAudit.md)

</td></tr><tr><td>

Governance, Risk, and Compliance

</td><td>

GRC: Metrics

</td><td>

[Components installed with the GRC: Metrics application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/environmental-social-governance/tables-installed-with-metrics.md)

</td></tr><tr><td>

Governance, Risk, and Compliance

</td><td>

Operational Resilience

</td><td>



</td></tr><tr><td>

Governance, Risk, and Compliance

</td><td>

Privacy Management

</td><td>

[Roles installed with Privacy Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/privacy-workspace/roles-installed-prm.md)

</td></tr><tr><td>

Governance, Risk, and Compliance

</td><td>

Risk Management

</td><td>

[Components installed with Risk Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/governance-risk-compliance/grc-risk-management-workspace/r_InstallWRisk.md)

</td></tr><tr><td>

Healthcare and Life Sciences

</td><td>

Healthcare and Life Sciences Service Management Core

</td><td>

[Components installed with Healthcare and Life Sciences Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/healthcare-and-life-sciences-service-management-core/hcls-components-installed-serv-mgmt.md)

</td></tr><tr><td>

Healthcare and Life Sciences

</td><td>

Patient Support Services

</td><td>

[Components installed with Patient Support Services](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/pss-components-installed.md)

</td></tr><tr><td>

Healthcare and Life Sciences

</td><td>

Pre-Visit Management

</td><td>

[Components installed with Pre-Visit Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/pre-visit-components-installed.md)

</td></tr><tr><td>

IT Asset Management

</td><td>

Model Management

</td><td>

[Installed with Model Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-asset-management/asset-management/installed-with-model-management.md)

</td></tr><tr><td>

IT Asset Management

</td><td>

Product Catalog

</td><td>

[Roles installed with Product Catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/product-catalog/r_RolesProductCatalog.md)

</td></tr><tr><td>

IT Operations Management

</td><td>

Automation Discovery

</td><td>

[Components installed with Automation Discovery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/installed-with-automation-discovery.md)

</td></tr><tr><td>

IT Operations Management

</td><td>

Event Management

</td><td>

[Components installed with Event Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/event-management/r_InstalledWithEventManagement.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Advanced Work Assignment

</td><td>

[Components installed with Advanced Work Assignment](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/conversational-interfaces/advanced-work-assignment/installed-with-awa.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

AI Search

</td><td>

[Components installed with AI Search](../../ai-search/reference/components-installed-ais.md#)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Application Portfolio Management

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Automation Center

</td><td>

[Components installed with Automation Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/automation-center/components-installed-with-automation-center.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Client Software Distribution 2.0

</td><td>

[Components installed with](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/integration-hub/csd2-installed.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Conversational Analytics

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Document Intelligence

</td><td>

[Document Intelligence roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/document-intelligence-user-roles.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Interaction Management

</td><td>

[Components installed with Interaction Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/interaction-management/components-installed-with-interaction-management.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Live Feed

</td><td>

[User roles installed with Live Feed](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/live-feed/r_UserRolesInstalledWithLiveFeed.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Notify

</td><td>

[Roles installed with Notify](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/notify/r_NotifyRoles.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Orchestration \(Legacy\)

</td><td>

[Installed with Orchestration ROI](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/orchestration/r_InstalledWithOrchestrationROI.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Build Workflows

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Build Workflows

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Build Workflows

</td><td>

[User access to Workflow Studio flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/user-access-flow-designer.md)

</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Build Workflows

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Service Bridge

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

Service Bridge

</td><td>



</td></tr><tr><td>

ServiceNow AI Platform capabilities

</td><td>

State Model

</td><td>

[Installed with State Model](../../state-model/reference/installed-state-model.md#)

</td></tr><tr><td>

Platform Analytics

</td><td>

Automation Discovery

</td><td>

[Components installed with Automation Discovery](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/installed-with-automation-discovery.md)

</td></tr><tr><td>

Platform Analytics

</td><td>

Performance Analytics

</td><td>

[Performance Analytics roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/r_PARoles.md)

</td></tr><tr><td>

Platform Analytics

</td><td>

Process Mining

</td><td>

[Components installed with Process Mining](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/process-mining/components-installed.md)

</td></tr><tr><td>

Platform Analytics

</td><td>

Reporting

</td><td>

[Reporting roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/reporting/reporting-roles.md)

</td></tr><tr><td>

Platform Analytics

</td><td>

Usage Insights

</td><td>

[Roles installed with Usage Insights](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/usage-insights/components-installed-user-exp-analytics.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Asset Management

</td><td>



</td></tr><tr><td>

IT Service Management

</td><td>

Change Management

</td><td>

[Components installed with ITSM Roles - Change Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/change-management/installed-with-cm-itsm-roles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Continual Improvement Management

</td><td>

[Continual Improvement Management roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/continual-improvement-management/cim-roles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Contract Management

</td><td>

[User roles installed with Contract Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/contract-management/r_UserRolesIWContractMgmt.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Digital Portfolio Management

</td><td>

[Roles for Digital Portfolio Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/digital-portfolio-management/dpm-roles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Employee Center

</td><td>

[Employee Center roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/emp-center-personas.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Expense Line

</td><td>

[Components installed with Expense Line](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/expense-line/r_InstalledWithExpenseLine.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Facilities Move Management

</td><td>

[Roles installed with Facilities Move Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_RolesInstallWFacMoveMgmt.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Facilities Service Management

</td><td>

[Roles installed with Facilities Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_RolesInstallWFacServMgmnt.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Incident Management

</td><td>

[Components installed with ITSM Roles — Incident Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/incident-management/inci-roles-instld-itsm-roles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

ITSM Predictive Intelligence Workbench

</td><td>



</td></tr><tr><td>

IT Service Management

</td><td>

Knowledge Management

</td><td>

[Knowledge Management roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/knowledge-management/r_KnowledgeRoles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Performance Analytics

</td><td>

[Performance Analytics roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/r_PARoles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Planned Maintenance

</td><td>

[Installed with SM Planned Maintenance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/planned-maintenance-family/r_InstallWServMgmtPlanMaint.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Problem Management

</td><td>

[Components installed with Problem Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/problem-management/installed-with-madrid-best-prac.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Procurement

</td><td>

[User roles installed with Procurement](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/procurement/r_UserRolesProcurement.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Request Management

</td><td>

[Request ITSM Roles - Request Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/request-management/request-itsm-roles-rm.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Builder

</td><td>

[Roles installed with Service Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-builder/service-builder-roles.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Operations Workspace

</td><td>

[Components installed with Service Operations Workspace ITSM Applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-operations-workspace/components-installed-with-sow.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Operations Workspace

</td><td>

[Components installed with Agent Client Collector for Investigation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-operations-workspace/components-installed-investigate.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Operations Workspace

</td><td>

[Components installed with Microsoft Endpoint Configuration Manager for Investigation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-operations-workspace/components-installed-mecm-adapter.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Operations Workspace

</td><td>

[Components installed with Remedial Actions Framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-operations-workspace/components-installed-with-remediation-fw.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Operations Workspace

</td><td>

[Components installed with Metrics and CI Actions Framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-operations-workspace/components-installed-metrics-ci-action-fw.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Level Management

</td><td>

[Installed with Service Level Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/service-level-management/r_InstalledWithServiceLevelMgmt.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Management Core

</td><td>

[Installed with Service Management Core](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-management-for-the-enterprise/r_InstallWServMgmtCore.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Service Portfolio Management

</td><td>



</td></tr><tr><td>

IT Service Management

</td><td>

Vendor Management Workspace

</td><td>



</td></tr><tr><td>

IT Service Management

</td><td>

Walk-up Experience

</td><td>

[Components installed with Walk-up Experience](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/walk-up-experience/installed-with-walkup-experience.md)

</td></tr><tr><td>

IT Service Management

</td><td>

Workforce Optimization

</td><td>

[Components installed with Process Mining](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/process-mining/components-installed.md)

</td></tr><tr><td>

Security Operations

</td><td>

Security Incident Response

</td><td>

[Components installed with Security Incident Response](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/security-incident-response/installed-with-sir.md)

</td></tr><tr><td>

Security Operations

</td><td>

Threat Intelligence Sharing

</td><td>



</td></tr><tr><td>

Security Operations

</td><td>

Vulnerability Response

</td><td>

[Components installed with Vulnerability Response](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/vulnerability-response/installed-with-vr.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Data Separation

</td><td>



</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Enterprise Release Management

</td><td>



</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Field Service Management

</td><td>

[Components installed with Field Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/field-service-management/r_InstalledWithFSM.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Field Service Management

</td><td>

[Field Service with Service Locations Support components](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/field-service-management/service-locations-components.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Financial Management

</td><td>



</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Investment Funding

</td><td>

[Components installed with Investment Funding](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/investment-funding/installed-with-investment-funding.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Project Portfolio Management

</td><td>

[Components installed with Project Portfolio Management \(PPM\) Standard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/ppm-collaboration/r_InstalledWithProjectPortfolioSuiteWithFinancials.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Scrum Programs

</td><td>

[Components installed with Scrum Programs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/agile-development/installed-with-scrum-programs.md)

</td></tr><tr><td>

Strategic Portfolio Management

</td><td>

Teamspaces

</td><td>

[Installed with teamspaces](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/project-management/r_InstalledWithTeamspaces.md)

</td></tr></tbody>
</table>**Parent Topic:**[Base system roles](r_BaseSystemRoles.md)


```


### File: platform-administration\user-administration\audit-user-roles.md

```text
---
title: Audit user roles
description: Changes to user roles are automatically tracked in the Audit Roles \[sys\_audit\_role\] table.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Audit user roles

Changes to user roles are automatically tracked in the Audit Roles \[sys\_audit\_role\] table.

## Before you begin

Role required: admin

**Note:** If the [Prevent duplicate entries with Contextual Security: Role Management V2](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/access-control/Role-Mgmt-V2.md) plugin is installed, you must [Enable role auditing with Contextual Security: Role Management V2](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/access-control/enable-audit-roles.md).

## Procedure

1.  Navigate to **All**, and then enter `sys_audit_role.list` in the filter.

    The Audit Roles \[sys\_audit\_role\] table displays changes to user roles.

<table id="table_wr1_tsh_4z"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Changed by

</td><td>

The user who made the change.

</td></tr><tr><td>

Count after change

</td><td>

Direct role added as a result of the change \(if any\), plus the number of inherited roles added.

</td></tr><tr><td>

Granted by group

</td><td>

If the role was inherited, the group that the role was inherited from.

</td></tr><tr><td>

Operation

</td><td>

The type of change. Values include:

 -   Added
-   Removed


</td></tr><tr><td>

Role

</td><td>

The affected role.

</td></tr><tr><td>

User

</td><td>

The affected user.

</td></tr></tbody>
</table>
**Parent Topic:**[Managing roles](../concept/ua-creating-roles.md)


```


### File: platform-administration\user-administration\c_ConfigGroupTypesForAssignGroups.md

```text
---
title: Configure assignment group types
description: Use the Type field to define categories of groups. Once defined, you can use these categories to filter assignment groups based on the group type using a reference qualifier.You can add additional group types to filter assignment groups for tasks.You can assign group types to filter assignment groups for tasks.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Creating groups, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Configure assignment group types

Use the **Type** field to define categories of groups. Once defined, you can use these categories to filter assignment groups based on the group type using a reference qualifier.

For example, when selecting an assignment group from the Incident form, **Type** can be used to filter groups based on whether they’re typically involved in the Incident management process. Groups such as Network or Help Desk are displayed as they’re typically involved. Groups such as HR or New York are omitted.

The following items are provided in the base system.

-   The types **catalog**, **itil**, and **survey**.
-   The reference qualifier on \[task.assignment\_group\] filters on **\[Type\] \[equals\] \[itil\]**.
-   A reference qualifier named **GetGroupFilter** is available to filter for group types using [Create a dynamic filter option](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_DynamicFilterOptions.md).

**Note:** Dictionary overrides enable administrators to filter a group type on an extended table using a simple [reference qualifier](../../../script/server-scripting/concept/c_ReferenceQualifiers.md) override.

**Parent Topic:**[Creating groups](../../roles/concept/ua-creating-groups.md)

## Add a group type

You can add additional group types to filter assignment groups for tasks.

### Before you begin

Role required: admin

### About this task

You may need to configure the form to display the **Type** field. For more information see: [Personalize a form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md)

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Select a group record.

3.  Select the lock icon beside **Type**.

4.  Select the lookup icon beside the selection field.

    The Group Types dialog opens.

5.  Complete the following steps.

    1.  Select **New**.

    2.  Enter the group type name and description.

        For example, to define a type for a group as **incident** and **problem**, enter: **incident,problem**.

        Select **Submit**.

    The Group form reopens with the new type listed.

6.  Add additional group types if needed.

7.  Select **Update**.


## Assign a group type

You can assign group types to filter assignment groups for tasks.

### Before you begin

Role required: admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups** and select the desired group.

2.  Select the lock icon beside **Type**.

3.  Select the lookup icon beside the selection field and select one or more group types.

    **Note:** Because the default behavior of task.assignment\_group is to filter out groups with group types defined, adding a type to a group filters it out of the **Assignment Group** field on tasks. To change the behavior, set up the reference qualifier.

4.  Select **Update**.



```


### File: platform-administration\user-administration\c_DelegateRoles.md

```text
---
title: Delegating roles
description: Administrators can grant users the ability to assign roles within groups. However, these users can only assign roles that they already have.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Delegating roles

Administrators can grant users the ability to assign roles within groups. However, these users can only assign roles that they already have.

Role delegators are users responsible for assigning roles to other users within a group. This role can be assigned manually by granting the role\_delegator role to the user, or through the **Group Manager Change** business rule.

The **Group Manager Change** business rule, which is disabled by default, automatically grants the role\_delegator role to a user who is designated manager of a group in the **Manager** field on the **Group** form. The role is removed when the user is no longer the manager of the group.

Activate the business rule to take advantage of it. For more information on **Business rules**, see [Classic Business rules](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/business-rules-classic/c_BusinessRules.md).

## Reviewing Roles and Role Changes

To view roles and role changes:

-   Individual users: Navigate to **User administration** &gt; **Users** select a user, and review the **Roles** related list.
-   Role delegators: Review who can give roles in which groups by navigating to **User administration** &gt; **Role delegators**.
-   For all role changes: To see a history of role changes, navigate to **System security** &gt; **Reports** &gt; **Role audit**. See [Audit user roles](../task/audit-user-roles.md) for more information.

-   **[Designate role delegators](../task/t_RoleDelegation.md)**  
Designate role delegators to assign roles to users who are in a particular group.
-   **[Assign roles as a role delegator](../task/delegate-roles.md)**  
If you're a role delegator, you can delegate roles that are assigned to you for groups that you manage.
-   **[Prevent a role from being delegated](../task/t_PreventARoleFromBeingDelegated.md)**  
You can prevent roles from being delegated to users.

**Parent Topic:**[Managing roles](ua-creating-roles.md)


```


### File: platform-administration\user-administration\c_ImpersonateAUser.md

```text
---
title: Impersonating users
description: Administrators are able to impersonate other authenticated users, a feature primarily used for testing.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Impersonating users

Administrators are able to impersonate other authenticated users, a feature primarily used for testing.

This function enables the administrator to access the system exactly as the impersonated user, including identical menus and modules. All actions performed by the administrator during impersonation are recorded as if they were executed by the impersonated user.

![Impersonation example](../image/imperson_general.png)

## Impersonation limitations

When you impersonate a user, all scope-protected roles and encryption module roles are supported if the **Impersonation** option is configured in the module access policy. See [Create a module access policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/create-module-access-policy.md) for details.

Impersonating a user enables access to scope-protected and encryption roles, as defined in the access policy. However, if impersonating a user with an admin role, access to certain features and modules is limited unless the impersonator already possesses those roles.

Impersonating a user with an application-specific admin role, like Human Resources admin or Security Incident Response, limits access to certain features such as security incidents and profile information, unless these roles are already assigned to the impersonating admin. This restriction extends to certain modules and applications in the navigation bar, and admins can’t change the password of users with application admin roles.

The following actions or conditions cause a user impersonation to end:

-   The user impersonates a different user
-   The user session ends, for example after a user logs out of their instance

    **Note:** When an administrator starts impersonating a user, the 'Impersonate Begin' event is logged in the system log. Similarly, the 'Impersonate End' event is recorded when impersonation concludes under one of the two conditions listed above.


## Impersonation requirements

The user account to be impersonated must have a user ID. You can find this ID in the User \[sys\_user\] record for the account. If this value is missing, the message `The user you selected could not be impersonated` appears.

You need several different accounts to test the system.

-   An admin account to do work
-   An information technology infrastructure library \(ITIL\), or similar, account to test as a technician
-   An ESS account to test as an end user

More logins may be required to adequately test the system.

**Note:** If you try to impersonate a user who is either locked out or inactive, the system will automatically log you out if you initiate an action or select a link. Remember that all changes made during impersonation only apply to that session. To help ensure accuracy, log out and then log back in after completing the impersonation.

## Mobile impersonation

Mobile impersonation is available on ServiceNow mobile apps. For information on mobile impersonations, see [Mobile impersonation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/mobile/mobile-impersonation.md).

-   **[Manage the visibility of the impersonation feature](manage-the-visibility-of-the-impersonation-feature.md)**  
Before users can impersonate another user, an administrator must make the feature visible.
-   **[Impersonate a user](../task/t_ImpersonateAUserInUI16.md)**  
You can select a user or enter a different user name to perform an impersonation.
-   **[Impersonation logs](c_LogImpersonations.md)**  
Impersonations are logged in the system log.
-   **[User impersonation auditing](impersonation-audits.md)**  
User impersonation auditing creates a structured, dedicated audit trail for every impersonation session.

**Parent Topic:**[Monitoring user activity](../../roles/concept/user-admin-tools-landing.md)


```


### File: platform-administration\user-administration\c_LogImpersonations.md

```text
---
title: Impersonation logs
description: Impersonations are logged in the system log.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Impersonating users, Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Impersonation logs

Impersonations are logged in the system log.

Log impersonations for either interactive \(UI\) or non-interactive sessions.

## Impersonation logging for interactive sessions

Interactive sessions are performed through the user interface \(UI\). Enable or disable impersonation logging for interactive sessions using the **glide.sys.log\_impersonation** property.

If you enable impersonation logging for interactive sessions by setting **glide.sys.log\_impersonation** to **true**, all interactive sessions are recorded in the log.

|Property|Description|
|--------|-----------|
|**glide.sys.log\_impersonation**|Enables \(**true**\) or disables \(**false**\) impersonation logging for interactive sessions.|

## Impersonation logging for non-interactive sessions

Non-interactive sessions are performed by applications and scripts, not through the UI.

Impersonation logging of non-interactive sessions is turned off by default. If you enable impersonation logging by setting the **glide.sys.log\_impersonation.non\_interactive** property to **true**, impersonations of non-interactive sessions are recorded in the impersonate log.

Even with **glide.sys.log\_impersonation.non\_interactive** set to **true**, the system doesn’t log certain common impersonation tasks performed on behalf of the default users \(**system**, **soap.guest**, and **guest**\) because the application impersonates those default users to perform a variety of tasks.

Use the **glide.sys.log\_impersonation.non\_interactive.exclusion** property to exclude impersonations by other users in addition to the default users.

<table id="table_hjb_ntk_kbb"><thead><tr><th>

Property

</th><th>

Description

</th></tr></thead><tbody><tr><td>

**glide.sys.log\_impersonation.non\_interactive**

</td><td>

Enables \(**true**\) or disables \(**false**\) impersonation logging for non-interactive sessions.

</td></tr><tr><td>

**glide.sys.log\_impersonation.non\_interactive.exclusion**

</td><td>

Excludes impersonation logging of non-interactive sessions for specified users.Enter user names as a comma-separated list. Default users \(**system**, **soap.guest**, and **guest**\) don’t need to be included in the list.

</td></tr></tbody>
</table>**Parent Topic:**[Impersonating users](c_ImpersonateAUser.md)


```


### File: platform-administration\user-administration\c_ManageUserSessions.md

```text
---
title: Managing user sessions
description: The ServiceNow AI Platform provides the ability to view and terminate individual user sessions, lock out users from the system, and make users inactive.Secure your instance by enforcing a maximum time for sessions regardless of user activity.Specify when to time out user sessions after a period of inactivity.Configure how much time users have to extend a session before it times out due to inactivity.Lock out a user when you don’t want the user to access the instance.You can mark a user inactive so the user doesn't show up in any fields that reference active users on the User table.You can terminate a user session, for example, if you’re going to perform system maintenance and users are still logged in.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Managing user sessions

The ServiceNow AI Platform provides the ability to view and terminate individual user sessions, lock out users from the system, and make users inactive.

Regardless of the number of windows you have open in a browser, it’s considered to be one session. However, if you have two separate browsers open \(such as Google Chrome and Safari\), it’s considered to be two separate sessions.

-   Terminating a user session effectively logs that user out of the next transaction, which is usually the next browser select. Use the terminate sessions feature when you want to perform system maintenance.
-   Locking a user out of the system means they can no longer log in or generate any actions from any email messages that they send to the instance. Locking users out also terminates their sessions.
-   Making a user inactive means they don't show up in any fields that reference active users on the **User** table.

**Parent Topic:**[Monitoring user activity](../../roles/concept/user-admin-tools-landing.md)

## Configure a maximum active time for user sessions

Secure your instance by enforcing a maximum time for sessions regardless of user activity.

### Before you begin

Role required: admin

### About this task

By default, sessions expire only after a period of inactivity. Enforcing a maximum active session time ends sessions regardless of whether a user has been active recently, including whether they recently selected to extend a session. The active session timeout should be greater than the value configured for the inactive session timeout. For example, if sessions are configured to time out after 30 minutes of inactivity, the active session timeout should be greater than 30 minutes.

### Procedure

1.  In the navigation filter, enter `sys_properties.list`.

2.  Filter the System Properties \[sys\_properties\] list for the following properties and then select a property to open its record.

    -   **glide.ui.active.session.life\_span**: Sets the maximum session time for authenticated user sessions regardless of user activity. Authenticated users are logged out of the instance after the time specified and must enter their credentials again to access the instance.
    -   **glide.guest.active.session.life\_span**: Sets the maximum session time for guest user sessions regardless of user activity. This setting helps secure an instance using applications that involve guest user sessions, such as Agent Chat.
3.  In the **Value** field, enter the number of minutes before the session times out regardless of user activity.

    The value should be greater than the value of the corresponding properties for an inactive session timeout: **glide.ui.session\_timeout** for authenticated users or **glide.guest.session\_timeout** for guest users. By default, the inactive session timeout for both authenticated and guest users is 30 minutes.

4.  Select **Update**.


**Related topics**  


[Configure a maximum active time for integration sessions](../../../integrate/concept/managing-integration-sessions.md#)

## Modify user session timeout after inactivity

Specify when to time out user sessions after a period of inactivity.

### Before you begin

Role required: admin

### About this task

By default, after 30 minutes of inactivity in the application, the platform logs the user out automatically, unless the **Remember Me** check box in the login screen is selected. Making the interval longer can lead to the unnecessary maintenance of inactive sessions in memory. Adjust this timeout setting to no more than a few hours, although up to 24 hours is workable.

**Note:**

-   Ajax calls to the server keep the session alive \(such as Labels and Refreshing dashboards\).
-   Polling keeps the session alive when the chat desktop is open \(requires the Chat plugin\).

### Procedure

1.  Clear the **Remember Me** check box in the login screen.

2.  In the navigation filter, enter `sys_properties.list`.

3.  From the System Property \[sys\_properties\] list, search for **glide.ui.session\_timeout**.

4.  If **glide.ui.session\_timeout** doesn’t exist, select **New** to add a new property using the following values:

    -   **Name**: **glide.ui.session\_timeout**
    -   **Description**: Type a brief description. In this case, enter something like `Override the default session timeout (30). This value is in minutes`.
    -   **Type**: Select the appropriate data type. In this case, select **Integer**.
    -   **Value**: Change the default value from 30 minutes to a value of your choice.
    **Note:** The session timeout can also be set through installation exit customizations.


### What to do next

Administrators may also want to add the following properties to the System Properties table.

-   **glide.security.csrf.handle.ajax.timeout**: Handles errors for timed out Ajax requests when set to **true**.
-   **glide.security.auto.resubmit.ajax**: Automatically resubmits timed-out Ajax requests when set to **true** and the [Log in to an instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_LoggingIn.md) check box is selected or [Change the default value of the Remember me check box](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/authentication/c_ChSetRemMeChkbxCookie.md). A pop-up appears to users asking them to continue.
-   **glide.ui.auto\_req.extend.session**: When set to **true**, the system automatically extends a user's session by the value they select for the homepage refresh time. If there’s no homepage refresh time, the standard timeout value applies. Tablet and mobile devices don’t support this property. When set to **false**, user sessions time out when the **Remember me** check box is clear. The timeout is based on whether there’s a homepage refresh time. When there’s no homepage refresh time, the standard timeout value applies. When there’s a homepage refresh time, the user session times out after the timeout value plus one interval of the homepage refresh time. For example, if a user selects a refresh interval of five minutes, then that session expires after the timeout value plus five minutes.

    **Note:** Users who select the **Remember me** check box are unaffected by session timeout properties.


Administrators can also add the following properties to configure additional timeout settings for user sessions. These additional settings help to conserve system resources:

-   **glide.session.unauthorized.timeout.enabled**: Enables an alternate session timeout for unauthenticated, guest sessions. Guest sessions are created for HTTP requests to the instance that don’t contain authentication information. By default this property is set to **true**.
-   **glide.unauthorized.session\_timeout**: Specifies the time, in minutes, after an authenticated user logs out of an instance before the session ends. Set the property to a value greater than **0** and less than the value in the **glide.ui.session\_timeout** property.

**Related topics**  


[Modify integration session timeout after inactivity](../../../integrate/concept/managing-integration-sessions.md#)

## Prompting users to extend a session

Configure how much time users have to extend a session before it times out due to inactivity.

### Before you begin

Role required: admin

### About this task

By default, users are prompted to extend their session two minutes before it expires with an "Extend your session" dialog box. This procedure explains how to adjust the timing of when users are presented with this prompt.

### Procedure

1.  Navigate to **All**, and then enter `sys_properties.list` in the navigation filter.

2.  Open the **glide.ui.session\_timeleft** property.

3.  In the **Value** field, enter the number of minutes before the session timeout to prompt users to extend their session.

    Setting the value to zero turns off prompting users to extend their sessions.

4.  Select **Update**.


## Lock out a user

Lock out a user when you don’t want the user to access the instance.

### Before you begin

Role required: user\_admin or admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users** and select the user from the list.

2.  Select the **Locked Out** check box, and update the record.


## Mark a user inactive

You can mark a user inactive so the user doesn't show up in any fields that reference active users on the **User** table.

### Before you begin

Role required: admin

### About this task

**Note:** By default, when you mark a user inactive, you lock out that user. The **Lock Out Inactive Users** business rule governs this behavior.

If you clear the **Active** checkbox, the user is locked out and cannot access the instance. This functionality is controlled through a Glide property **glide.authenticate.only.allow.active.user.login** which will only allow the active users to access the instance.

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users** and select the user from the list.

2.  Clear the **Active** check box, and update the record.


## Terminate a user session

You can terminate a user session, for example, if you’re going to perform system maintenance and users are still logged in.

### Before you begin

Role required: admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Logged in users**.

    You can only see users who are logged in to the same application node as you. If the Active field on a user record value is false, the user is logged in but not currently running a transaction. Most users appear as inactive at any given time.

2.  Select the session that you want to end.

3.  Select **Lock Out Session**.

    The session is terminated, and the user is redirected to the login page at the next attempted transaction. The user isn’t locked out. Multiple user sessions may be associated with one user. Terminating a user session only affects the specific session.

    **Note:** Mobile user sessions can’t be terminated using this process.



```


### File: platform-administration\user-administration\c_NonInteractiveSessions.md

```text
---
title: Non-interactive sessions
description: The Non-Interactive Sessions plugin creates a distinction between interactive and non-interactive users.Non-interactive users can only connect to a ServiceNow instance from an API protocol. Use this feature to set up user accounts for web service authentication purposes.Manually switch a non-interactive user to an interactive user.If your instance requires strict security, add the soap role to any user accounts used for web services.You can specify whether non-interactive sessions require authentication from the High Security Settings module.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Non-interactive sessions

The Non-Interactive Sessions plugin creates a distinction between interactive and non-interactive users.

-   **Interactive users**

    New users added to the instance automatically become interactive users. Interactive users can perform the following actions:

    -   Use their user name and password to log in to the UI or a service portal.
    -   Connect to an instance from a URL that calls a UI page, form, or list, for example, https://&lt;instance name&gt;.service-now.com/incident.do.
    -   Connect with single sign-on, for example, digest authentication or a Security assertion markup language \(SAML\).
    -   Use their credentials to authorize SOAP connections if allowed by strict security.
    -   Use their credentials for other API connections such as WSDL, JSON, XML, or XSD without restriction.
-   **Non-interactive users**

    Non-interactive users can only use their credentials to authorize API connections such as JSON, SOAP, and WSDL. They can’t log in to the ServiceNow UI. The strict security high security setting determines if non-interactive users are subject to [Contextual Security Manager](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/access-control/r_ContextualSecurity.md) requirements.


Distinguishing between interactive and non-interactive users increases instance security by helping to ensure that users abide by the principle of least privilege.

## Installed with Non-Interactive Sessions

**Note:** Non-Interactive Sessions is enabled for all new instances since the Calgary release. If you don’t see it in the list of plugins, request it using the Activate Plugin service catalog item in Now Support.

-   Adds a column titled **Web Service Access Only** \[web\_service\_access\_only\] to the **User** \[sys\_user\] table.
-   Changes all existing users to be interactive users \(web\_service\_access\_only=false\).
-   Updates the User form to display the **Web Service Access Only** \[web\_service\_access\_only\] field by default.

**Parent Topic:**[Monitoring user activity](../../roles/concept/user-admin-tools-landing.md)

## Create a non-interactive user for web services

Non-interactive users can only connect to a ServiceNow instance from an API protocol. Use this feature to set up user accounts for web service authentication purposes.

### Before you begin

Role required: user\_admin or admin

### About this task

Non-interactive users can't log in to an instance or a service portal or connect through single-sign-on. They can be used as a MID Server user if they’re flagged as an Internal Integration User.

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users**.

2.  Search for the user to be updated.

    For example, SOAP user.

3.  Select the **Web Service Access Only** check box.

4.  Select **Update**.

    **Note:**

    The ServiceNow platform uses any user name and password credentials supplied with a request even if the [High Security Settings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_HighSecuritySettings.md) don’t require authorization for a given API protocol. For example, if a SOAP request supplies a user name and password, the instance verifies those credentials even if SOAP requests don’t require authorization. To avoid verifying user credentials, the request must not include them.


## Make a non-interactive user record interactive

Manually switch a non-interactive user to an interactive user.

### Before you begin

Role required: user\_admin or admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users**.

2.  Search for the user you want to update.

    For example, **System Administrator**.

3.  Clear the **Web Service Access Only** check box.

4.  Select **Update**.


## Update web service user accounts for strict security

If your instance requires strict security, add the soap role to any user accounts used for web services.

### Before you begin

Role required: user\_admin or admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users**.

2.  Select a web service user from the list.

3.  From the **Roles** related list, select **Edit**.

4.  Add soap to the **Roles List**.

5.  Select **Save**.

6.  Select **Update**.


## Require authentication

You can specify whether non-interactive sessions require authentication from the **High Security Settings** module.

### Before you begin

Role required: admin with elevated privileges

### About this task

A non-interactive session bypasses the UI to connect to the instance at an API level. Typically, non-interactive sessions use set protocols such as JSON, SOAP, XSD, or WSDL. By default, all non-interactive sessions require authentication.

### Procedure

1.  Log in with an administrator user with the security\_admin role.

2.  Elevate your privileges to use security\_admin.

3.  Navigate to **All** &gt; **System Security** &gt; **High Security Settings**.

4.  Select the matching **Requires authorization...** option for the protocol you want to set.

    For example, **Requires authorization for incoming SOAP requests**.

5.  Select the check box to require authentication for the non-interactive session method.

    Clear the check box to enable the non-interactive session method to connect without providing any credentials.

    **Note:**

    Activating the Non-Interactive Sessions plugin might restrict existing users who manage SOAP and WSDL-based integrations from logging in, unless they already possess the SOAP role.



```


### File: platform-administration\user-administration\c_NormalChangingNames.md

```text
---
title: Changing normalized company names
description: You can change a normalized company name several different ways. In all cases, that change affects all normalized fields referring to that company.You can change normalized company names by editing records in the Normalized Company Name table.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Changing normalized company names

You can change a normalized company name several different ways. In all cases, that change affects all normalized fields referring to that company.

You have several options for changing a normalized company name:

-   Edit the Normalized Name field in the Normalized Mappings table. This method is preferred.
-   Edit the Normalized Company name table.
-   Edit the Company Name field on any table that refers to the Company \[core\_company\] table.

**Warning:** If you edit a field whose value is a normalized name, you change the normalized name for ALL discovered names that map to it.

**Parent Topic:**[Normalization data services](c_NormalizationOverview.md)

## Change a normalized company name

You can change normalized company names by editing records in the Normalized Company Name table.

### Before you begin

Role required: nds\_admin

### About this task

You can add and edit records in the Normalized Company Names table.

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Normalization Data Services** &gt; **Normalized Mappings**.

2.  Find the record with the name that you want to replace and edit the Normalized name field.

    The system changes the Normalized Company name for every discovered name that maps to that normalized name.



```


### File: platform-administration\user-administration\c_NormalizationOverview.md

```text
---
title: Normalization data services
description: The Normalization Data Services plugin helps maintain consistency for table fields that refer to a company name.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [search optimization, data]
breadcrumb: [Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Normalization data services

The Normalization Data Services plugin helps maintain consistency for table fields that refer to a company name.

Tables related to configuration items and assets usually contain columns referring to a company name, such as a vendor or manufacturer. Often, these tables refer to the same company by several different names. This situation can happen for many reasons. For example, vendors sometimes use different company names depending on the device. This inconsistency creates problems, especially for reports that rely on these company names.

The Normalization Data Services plugin helps alleviate this problem.

When you enable and configure the Normalization Data Services plugin, the system downloads a list of standard company names that ServiceNow has compiled. It also downloads a list of common variants of that name. Anytime the plugin finds a company-name field with one of those variants, it substitutes the standard name in its place.

**Note:** The Normalization Data Services plugin refers to a standard name as a normalized name and to a variant name as a discovered name.

While the Normalization Data Services plugin provides services similar to the field normalization feature, this plugin doesn’t require you to manually set up the mappings from one name to another. If you like, you can add your own mappings to the set. However, you automatically start with extensive lists of common company names \(normalized names\) and their variants \(discovered names\).

The Normalization Data Services plugin stores data in two tables. The Normalized Company Names table contains the list of normalized company names. The Normalized Mappings table contains the mappings between each discovered name and its normalized name.

**Important:** If you edit a field whose value is a normalized name, you change the normalized name for ALL discovered names that map to it. These types of updates occur regardless of the table in which you edit the field.

The Normalization Data Services plugin adds a unique index or hash on the \[core\_company\] table. You can store only one company record for a company name. The unique hash is the same for two companies with the same name. The uniqueness is required for many features to work correctly. For example, **Discovery**, which creates customer management database \(CMDB\) models and CIs. On a domain separated instance, the unique index is expanded to hash,sys\_scope. This enables each domain to have its own version of a company with the same name.

-   **[Implementing normalization data services using guided setup](implementing-normalization-data-services-using-guided-setup.md)**  
You can implement Normalization Data Services using a guided setup.
-   **[Normalized company names table](../reference/r_NormalizedCompanyNames.md)**  
The Normalization Data Services plugin stores the normalized company names in the Normalized Company Names table.
-   **[Normalized Mappings table](../reference/r_NormalizedMappings.md)**  
The Normalized Mappings table lists all the discovered names and the normalized name to which each maps.
-   **[Normalization properties](../reference/r_NormalizedProperties.md)**  
On the normalization properties form, you can see and change the configurable properties for the Normalization Data Services plugin.
-   **[Changing normalized company names](c_NormalChangingNames.md#)**  
You can change a normalized company name several different ways. In all cases, that change affects all normalized fields referring to that company.
-   **[Enabling duplicate company names in extension tables](enhanced-nds-for-duplicate-records.md#)**  
You can create records with duplicate company names in extension tables, such as Customer Account \[customer\_account\] table, without causing normalization conflicts in Normalization Data Services.

**Parent Topic:**[Creating users, companies, and departments](../../roles/concept/using-user-administration.md)


```


### File: platform-administration\user-administration\c_ReadOnlyRole.md

```text
---
title: Read-only role
description: The read-only role \(snc\_read\_only\) restricts a user or a group of users to read-only access on the tables to which the user already has access.If it isn’t already active, an administrator can activate the Read-Only User Role \(com.snc.read\_only.role\) plugin.These system properties control the snc\_read\_only role. The following default values are used for the properties.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Base system roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Read-only role

The read-only role \(snc\_read\_only\) restricts a user or a group of users to read-only access on the tables to which the user already has access.

This role is designed to complement other roles a user possesses. Its purpose is to restrict actions like the insert, update, or delete operations on the tables accessible through their existing roles.

After you assign this role to a user, they can no longer create, update, or delete records on ANY tables.

**Note:** Assign this role only to users. Don’t assign this role to other resources in the system, including applications, access control levels \(ACLs\), and so on.

The snc\_read\_only role can be assigned to any user to limit access to data without having to create ACLs for system tables, custom tables, and fields. This practice is useful for performing internal or external audits without enabling a user to have insert or update access to data.

Users with the snc\_read\_only role have the following restrictions regardless of other roles and privileges that they have.

-   Can’t insert, update, or delete records from the UI or when using the GlideRecord API.
-   Can’t activate or upgrade plugins.
-   Can’t directly run SQL.
-   Can’t upload XML files.
-   Can only run background scripts when on an instance in the public sandbox environment.

**Note:** These role restrictions are in place even if impersonating another user with write access such as an admin.

**Parent Topic:**[Base system roles](../../roles/reference/r_BaseSystemRoles.md)

## Activate the read-only role

If it isn’t already active, an administrator can activate the Read-Only User Role \(com.snc.read\_only.role\) plugin.

### Before you begin

Role required: admin

### Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Read-Only User Role \(com.snc.read\_only.role\) plugin using the filter criteria and search bar.

    You can search for the plugin by its name or ID. If you cannot find a plugin, you might have to request it from ServiceNow personnel.

3.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).


## Read-only role properties

These system properties control the snc\_read\_only role. The following default values are used for the properties.

<table id="simpletable_tqr_1hx_4zb"><thead><tr><th>

Name

</th><th>

Description

</th></tr></thead><tbody><tr><td>

**glide.security.snc\_read\_only\_role.tables.exempt\_create**

</td><td>

Specifies which tables are exempt from the read-only role enforcement and enable the creation of new records.

 -   Type: string
-   Default value: sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth
-   Location: System Properties \[sys\_properties\] table

</td></tr><tr><td>

**glide.security.snc\_read\_only\_role.tables.exempt\_write**

</td><td>

Specifies which tables are exempt from the read-only role enforcement and enable the updating of existing records.

 -   Type: string
-   Default value: sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth
-   Location: System Properties \[sys\_properties\] table

</td></tr><tr><td>

**glide.security.snc\_read\_only\_role.tables.exempt\_delete**

</td><td>

Specifies which tables are exempt from the read-only role enforcement and enable the deletion of existing records.

 -   Type: string
-   Default value: sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth
-   Location: System Properties \[sys\_properties\] table

</td></tr></tbody>
</table>After you configure these properties, assign the read-only role as needed. When you log in, you’re restricted from creating, updating, or deleting records on ANY tables unless you modified these properties.

**Note:** Test the read-only role by assigning it to a user and then impersonating that user.


```


### File: platform-administration\user-administration\c_UserAdministration.md

```text
---
title: User administration
description: Manage the individuals who can access your instance by defining them as users in the system. Create user groups and assign users to them. Use roles to specify what different users and user groups can see and do.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure core features, Administer the ServiceNow AI Platform]
---

# User administration

Manage the individuals who can access your instance by defining them as users in the system. Create user groups and assign users to them. Use roles to specify what different users and user groups can see and do.

## Get started

<table id="table_myk_l1d_kxb" class="nav-card"><tbody><tr><td>

[Explore![](../../../reuse/icons/brand-icons/bus-explore.svg)Learn about User administration.](exploring-user-administration.md)

</td><td>

[Create users, companies, and departments![](../../../reuse/icons/brand-icons/bus-2-person.svg)Create records for users or enable self-registration. Optionally create companies and departments to further categorize users.](using-user-administration.md)

</td><td>

[Create groups![](../../../reuse/icons/brand-icons/bus-3-person.svg)Create and manage groups that you can grant roles to and assign users to for efficiency.](ua-creating-groups.md)

</td></tr><tr><td>

[Manage roles![](../../../reuse/icons/brand-icons/bus-profile.svg)Manage roles that govern what users and groups with that role can do.](ua-creating-roles.md)

</td><td>

[Monitor user activity![](../../../reuse/icons/brand-icons/bus-infographic.svg)Monitor user activity and troubleshoot issues by impersonating users and managing sessions.](user-admin-tools-landing.md)

</td><td>

[Monitor instance usage![](../../../reuse/icons/brand-icons/bus-management-console.svg)Track application usage on your instance.](../../subscription-management/concept/usage-analytics-module-subscription.md)

</td></tr></tbody>
</table>## Troubleshoot and get help

-   [ServiceNow Community forums](https://www.servicenow.com/community/)
-   [Search the Known Error Portal for known error articles](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597477)
-   [Contact Customer Service and Support](https://support.servicenow.com/now?draw=case)


```


### File: platform-administration\user-administration\c_UserRegistration.md

```text
---
title: User self-registration
description: The User Registration Request \[com.snc.user\_registration\] plugin provides the ability for unregistered users to request access to a ServiceNow instance. An administrator can activate the plugin.When a user submits a self-registration form, an admin can review and approve it.Admins can enable users to self-register. Enable automatic approval of such accounts to streamline user registration.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Creating users, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# User self-registration

The User Registration Request \[com.snc.user\_registration\] plugin provides the ability for unregistered users to request access to a ServiceNow instance. An administrator can activate the plugin.

A user can request an account by navigating to the instance. If the plugin is installed, the following section is added to the welcome screen.

![Welcome screen](../image/WelcomeScreen.png)

The user can complete and submit the self-registration form, and see a confirmation that it was submitted. The user receives an email when the account is registered.

**Note:** If the email address entered in the self-registration form is already in the system, the request is not submitted.

**Parent Topic:**[Creating users](../../roles/concept/ua-creating-users.md)

## Approve a self-registered user account

When a user submits a self-registration form, an admin can review and approve it.

### Before you begin

Role required: admin

### Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Pending User Registrations** and open the request.

2.  Use the **Create User** and **Reject** related links on the registration request form to approve or deny the request.

    -   If **Create User** is selected, a new user is created using the email address as the **User ID**.
    -   If **Reject** is selected, the request is marked **Rejected**.
    If the request was accepted, the user is sent an email notification with the login information. If it was denied, the user is sent an email with the rejection information.


## Enable automatic self-registered user account approval

Admins can enable users to self-register. Enable automatic approval of such accounts to streamline user registration.

### Before you begin

Role required: admin

### Procedure

1.  Navigate to **System Properties** &gt; **System**.

2.  Select **Enable auto processing of user registration request**

3.  Select **save**

    If enabled, registration requests do not require approval. Instead, the business rule **Auto-Process User Registration** creates the user record from the information provided.


### What to do next

Request activation of the [Explicit Roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/explicit-roles.md) \(`com.glide.explicit_roles`\) plugin. The Explicit Roles plugin creates two roles to differentiate between internal and external users.


```


### File: platform-administration\user-administration\delegate-roles.md

```text
---
title: Assign roles as a role delegator
description: If you're a role delegator, you can delegate roles that are assigned to you for groups that you manage.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Delegating roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Assign roles as a role delegator

If you're a role delegator, you can delegate roles that are assigned to you for groups that you manage.

## Before you begin

Role required: role\_delegator

## Procedure

1.  Navigate to **User Administration** &gt; **Delegate Roles in Group**.

2.  Fill out the form.

    |Field|Description|
    |-----|-----------|
    |Group|Select the group in which to delegate a role or roles to a member. Any group can be selected, including groups that the role\_delegator doesn’t belong to or groups that the role\_delegator doesn’t manage.|
    |User|Select the group member to delegate a role or roles.|
    |Roles to delegate|Select the roles to delegate to the group member. The roles available for delegating are only the roles that the role\_delegator has.|

    \(Optional\) To remove a delegated role from a user, open the delegation record and remove the unwanted role or roles.


**Parent Topic:**[Delegating roles](../concept/c_DelegateRoles.md)


```


### File: platform-administration\user-administration\enhanced-nds-for-duplicate-records.md

```text
---
title: Enabling duplicate company names in extension tables
description: You can create records with duplicate company names in extension tables, such as Customer Account \[customer\_account\] table, without causing normalization conflicts in Normalization Data Services.Configure the Normalization Data Services feature to enable records with duplicate company names across core company's extension tables, such as Customer Account \[customer\_account\] table.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Enabling duplicate company names in extension tables

You can create records with duplicate company names in extension tables, such as Customer Account \[customer\_account\] table, without causing normalization conflicts in Normalization Data Services.

If your ServiceNow instance has company records in the Company \[core\_company\] table from IT Service Management \(ITSM\) or IT Operations Management \(ITOM\), and you are adopting Customer Service Management \(CSM\), you may encounter errors when creating Customer Account records for the same companies.

Normalization Data Services manages company name normalization across the Company \[core\_company\] table and its extension tables, such as Customer Account \[customer\_account\] table. By default, Normalization Data Services enforces unique company name across all company-related tables. This causes conflicts when a vendor in the Company table and a customer account share the same name.

The **glide.cmdb.canonical.use\_base\_core\_company\_only** property introduces support for creating duplicate company names in extension tables. When you enable this property, Normalization Data Services restricts unique company name validation to the base, Company \[core\_company\] table only. Each duplicate record in an extension table still links to the correct normalized record in the base table.

Enable this property if you are upgrading from Zurich or an earlier release. You must use Customer Service Management with one or more of the following applications that extend the Company \[core\_company\] table:

-   ITSM Software Asset Management
-   Hardware Asset Management

**Parent Topic:**[Normalization data services](c_NormalizationOverview.md)

## Configure Normalization Data Services to create duplicate company name in extension table

Configure the Normalization Data Services feature to enable records with duplicate company names across core company's extension tables, such as Customer Account \[customer\_account\] table.

### Before you begin

Role required: nds\_admin

### About this task

**Note:** This procedure applies only if you are upgrading from Zurich or an earlier release. If you are on the Australia release or later, this feature is enabled by default and no action is required.

### Procedure

1.  Navigate to **All** &gt; **System Definitions** &gt; **Script includes**.

2.  Search for and open the **ClearNonCoreCompanyExtensionsFix** script.

3.  Select **Run Script**.

    The script clears the hash values and sets the Normalized flag to false for all duplicate company name records in the Company \[core\_company\] extension tables.

4.  Verify that the script ran successfully.

    1.  Navigate to **All** &gt; **System Log** &gt; **All**.

    2.  Search for the following log entries in the Log \[syslog\_list.do\] table.

        -   \[ClearNonCoreCompanyExtensionsFix\] Cleared hash
        -   \[ClearNonCoreCompanyExtensionsFix\] Set canonical=false
    The log entries confirm that the hash values are cleared and the normalized flag is set to false.

5.  Add the **glide.cmdb.canonical.use\_base\_core\_company\_only** system property and set its value to **True**.

    For more information, see [Add a system property](../../reference-pages/reference/r_AvailableSystemProperties.md#).

6.  Normalize data in the CMDB table.

    1.  Navigate to **All** &gt; **Normalization Data Services** &gt; **Guided Setup**.

    2.  In the Normalize Configuration Items \(CMDB\) Model step, select **Configure**.

    3.  Select **Start Update**.

    4.  Select **Close** after the update completes.

7.  Verify if you can create records with duplicate company names in extension tables.

    1.  Navigate to **All**, and then enter `customer_account.list` in the filter to go to the Customer Account table.

    2.  Select **New**.

    3.  On the form, fill in the fields.

        For a description of the field values, see [Account form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/customer-service-management/customer-service-account-form.md).

    4.  Select **Submit**.

8.  If you’re using Hardware Asset Management \(HAM\), run the following one-time script.

    1.  Navigate to **All** &gt; **System Definitions** &gt; **Script includes**.

    2.  Select **New**.

    3.  Enter a **Name** for the script include.

    4.  Enter the script include code in the **Script** field.

        ```
        var worker = new CanonicalUpdaterWorker(); 
                   var tables = { 
                   'sn_hamp_hw_manufacturer': ['company'],
                   'cmdb_hardware_product_model': ['normalized_company'], 
                   'cmdb_consumable_product_model': ['normalized_company'], 
            }; 
            for (var table in tables) {
                 if (tables.hasOwnProperty(table)) {
                 var fields = tables[table]; 
                 for (var i = 0; i < fields.length; i++) {
                     worker.addNormalization(table, fields[i]); 
                 } 
               } 
            } 
            worker.setProgressName(gs.getMessage("Normalization Data Service")); 
            worker.setBackground(true); 
            worker.start();
        ```

    5.  Select **Submit**.

    6.  Select **Run Script**.



```


### File: platform-administration\user-administration\exploring-user-administration.md

```text
---
title: Exploring user administration
description: Learn more about user administration for your instance.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Exploring user administration

Learn more about user administration for your instance.

## Overview

Creating users, groups, and roles provide a flexible and scalable way to manage access to features on the ServiceNow AI Platform. By creating user accounts, assigning users to groups, and defining roles and permissions, administrators can ensure that users have the appropriate level of access to applications and data. This enables organizations to control access to sensitive data, maintain conformance with regulatory requirements, and improve overall security. Additionally, users, groups, and roles can be easily managed and modified over time as organizational needs change.

## Work flow

Subscriptions, users, groups, and roles work together to help you define who can access features on your instance.

1.  [Subscription Management](../../subscription-management/reference/subscription-management-landing-page-v2.md)

    Understand your subscriptions. Subscription management enables you to manage your subscriptions proactively and monitor subscription usage on your instances.

    Subscriptions may include per-user subscriptions. For more information, see [Managing per-user subscriptions in Subscription Management](../../subscription-management/concept/managing-user-subscriptions-v2.md).

2.  [Creating users, companies, and departments](using-user-administration.md)

    Create an account record for the individuals who have access to your instance. Each user account has a unique login ID, password, and set of permissions \(roles\) that define what they can do and access within the platform.

3.  [Creating groups](ua-creating-groups.md)

    Define groups that have similar roles or permissions. Groups enable you to apply permissions \(roles\) to multiple users at the same time. When a user is a member of a group, that user has the same permissions that have been defined for the group.

    You can view group members by navigating to **All** &gt; **User Administration** &gt; **Groups**. Select a group name and view the members in the Group Members related list.

4.  [Managing roles](ua-creating-roles.md)

    Roles describe the types of activities that a user can perform on the instance. Each role has a set of permissions that can govern what the users and groups can do, such as read, write, create, or delete records. Roles can be assigned to users and groups. Users can have multiple roles.

    For a complete list of the roles included with the ServiceNow AI Platform, see [Base system roles](../reference/r_BaseSystemRoles.md).

    Role records are stored in the Roles \[sys\_user\_role\] table.

5.  [Monitoring instance usage](../../subscription-management/concept/usage-analytics-module-subscription.md)

    Users with the admin or usage\_admin role can view the **Application usage overview** and ServiceNow Store **usage overview** dashboards to track instance usage.

6.  [Monitoring user activity](user-admin-tools-landing.md)

    Users with the admin role can impersonate users, manage user sessions, and leverage non-interactive sessions.


![Create users and add them to groups. Create and assign roles to both users and groups.](../image/users-groups-roles.png "User administration workflow")

## User preferences

Users can configure many UI features. Some examples include the number of rows per page in a list or whether the response time displays at the bottom of a list or form. Administrators can modify or delete these preferences as needed. For more information, see [User preferences](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UserPreferences.md).

## User groups

A group is a set of users who share a common purpose. Groups may perform tasks such as approving change requests, resolving incidents, receiving email notifications, or performing work order tasks. Any business rules, assignment rules, system roles, or attributes that refer to the group apply to all group members automatically. Users with the user\_admin role can create and edit groups.

When possible, simplify user administration by assigning roles to groups. Create groups that contain all the roles necessary for specific personas, and then assign users to those groups.

**Note:** You can view group members by navigating to **All** &gt; **User Administration** &gt; **Groups**. Select a group name and view the members in the **Group Members** related list.

Group records are stored in the Groups \[sys\_user\_group\] table.

## User roles

Roles control access to features and capabilities in applications and modules. The admin role provides access to all features and capabilities.

After access has been granted to a role, all the groups or users assigned to the role are granted the access. Roles can contain other roles, and any access granted to a role is granted to any role that contains it.

For a complete list of the roles included with the ServiceNow platform, see [Base system roles](../reference/r_BaseSystemRoles.md).

**Note:**

When possible, simplify user administration by assigning roles to groups. Create groups that contain all the roles necessary for specific personas, and then assign users to those groups.

Role records are stored in the Roles \[sys\_user\_role\] table.


```


### File: platform-administration\user-administration\impersonation-audits.md

```text
---
title: User impersonation auditing
description: User impersonation auditing creates a structured, dedicated audit trail for every impersonation session.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-25"
reading_time_minutes: 1
keywords: [user impersonation, auditing, audit trail, security, administrator, session lifecycle, system logs, impersonation session, audit records, transaction logs]
audience: administrator
breadcrumb: [Impersonating users, Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# User impersonation auditing

User impersonation auditing creates a structured, dedicated audit trail for every impersonation session.

Impersonation activity is indistinguishable from regular user activity in a standard audit trail, you can't reliably attribute changes to the administrator who made them rather than the user they were impersonating. With the user impersonation auditing you can capture every impersonation session as a self-contained audit set, clearly separated from ordinary session data and accessible to administrators through system logs.

## Plugin and feature property

-   Plugin required for user impersonation auditing \(`com.glide.security.audit`\).
-   Property to control the feature user impersonation auditing \(`glide.audit.user.impersonation.enabled`\).

## Accessing impersonation audit records

Impersonation audit records are available to security administrators through **System Logs** &gt; **User Impersonation**. The list view displays a summary of all impersonation sessions recorded on the instance, including the identities of both parties and the session duration. Selecting any session record opens the detail view, which presents the complete audit set — the start entry, all actions in chronological order, and the closing entry — in a single place. This allows a security administrator to verify that the actions taken during a session were appropriate and within the expected scope of the impersonation.

## Audit record fields

Each entry in an impersonation audit set, whether a session-level record or an action-level entry, captures the following information.

|Field|Description|Example value|
|-----|-----------|-------------|
|Impersonated by|User who initiated the impersonation session.|`john.smith`|
|Impersonated to|User whose identity is being assumed.|`jane.doe`|
|Impersonation Start Time|Timestamp when the impersonation session began.|`2024-06-10 09:15:32 UTC`|
|Impersonation End Time|Timestamp when the session was terminated.|`2024-06-10 09:47:11 UTC`|

Select the **Impersonation Start Time** to know more about the impersonation activity. Following details are displayed:

-   Created
-   Type
-   Origin Application
-   Created by
-   Response time
-   Output length
-   SQL count
-   SQL time
-   Business rule count
-   ACL Time
-   URL

You can use the **Personailze List Columns** options to add more columns to the log.

**Note:** Impersonation audit records follow the same retention policy as transaction logs. The default retention period is `seven` days, but this is configurable by a system administrator. Any change to the transaction log retention setting applies equally to impersonation audit records.

**Parent Topic:**[Impersonating users](c_ImpersonateAUser.md)


```


### File: platform-administration\user-administration\implementing-normalization-data-services-using-guided-setup.md

```text
---
title: Implementing normalization data services using guided setup
description: You can implement Normalization Data Services using a guided setup.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Implementing normalization data services using guided setup

You can implement Normalization Data Services using a guided setup.

Normalization Data Services guided setup provides a sequence of tasks that help you configure the Normalization Data Services plugin on your instance. To open Normalization Data Services guided setup, navigate to **Normalization Data Services** &gt; **Guided Setup**. For more information about using the guided setup interface, see [Using guided setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/adoption-services/guided-setup.md).

**Note:** Because the Normalization Data Services feature requires an internet connection to download mapping information, this feature isn’t supported for on-premise instances.

## Activating the plugin

In the first task of the guided setup, you activate the Normalization Data Services plugin \(com.glide.data\_services\_canonicalization.client\). Activating the plugin installs all the necessary schema to support normalizing references to Company records in the customer management database \(CMDB\) and Asset Management.

## Downloading normalized data

In this task, you download the repository of all enterprise vendor names and the mappings to their normalized counterparts. After the download finishes, you can view the downloaded data in the Normalized Company Names \[cds\_client\_name\] table. You can verify mappings in the Normalized Mappings \[cds\_client\_mapping\] table. For example, you can verify that “Dell”, “DELL”, “Dell \(UK\)” are mapped to “Dell Inc.”.

## Updating reference qualifiers

This task modifies the reference qualifiers in reference fields linked to the Companies \[core\_company\] table, helping to ensure that users can only select from a list of normalized company names. For example, when creating a Computer \(cmdb\_ci\_computer\) record, users can only select “Dell Inc.” and not “Dell” or “Dell Incorporated”.

Some reference qualifiers may not get updated. To normalize these reference qualifiers manually, see [KB0784201](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784201).

## Activating normalization properties

In this task, select the properties you want to activate. See [Normalization properties](../reference/r_NormalizedProperties.md).

Enable the **Normalize existing canonical core\_company records** property if the Companies \[core\_company\] table has two or more records that were both set to Normalized \("canonical=true"\) before any mapping. This option ensures only one \[core\_company\] record is set to Normalized. When you normalize the CMDB tables later in guided setup, the normalization job reassigns the proper normalized value.

For example, prior to mapping, both “DELL Inc” and “Dell Inc.” are set to Normalized \("canonical=true"\). You define a new mapping for “DELL Inc” to “Dell Inc.”. If this property is true, guided setup denormalizes "DELL Inc", and updates the manufacturer field in the CMDB records to “Dell Inc." when the CMDB tables are normalized.

## Normalizing data

To finish the guided setup, complete the remaining tasks by normalizing data in the following tables:

-   Configuration Items \(CMDB\)
-   Configuration Items \(CMDB\) Model
-   Software Asset Management tables

**Parent Topic:**[Normalization data services](c_NormalizationOverview.md)


```


### File: platform-administration\user-administration\manage-the-visibility-of-the-impersonation-feature.md

```text
---
title: Manage the visibility of the impersonation feature
description: Before users can impersonate another user, an administrator must make the feature visible.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Impersonating users, Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Manage the visibility of the impersonation feature

Before users can impersonate another user, an administrator must make the feature visible.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System properties** &gt; **UI properties**.

2.  Select a check box under **Enable impersonation button in the banner line** to display or conceal the button.

3.  Select **save** at the top of the page.

    Admins can still impersonate users via the **impersonate\_dialog** UI page.


**Parent Topic:**[Impersonating users](c_ImpersonateAUser.md)


```


### File: platform-administration\user-administration\r_BaseSystemRoles.md

```text
---
title: Base system roles
description: Administrators can assign one or more base system user roles to grant access to base system platform features and applications.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 43
breadcrumb: [Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Base system roles

Administrators can assign one or more base system user roles to grant access to base system platform features and applications.

To learn more about managing per-user subscriptions, see [Managing per-user subscriptions in Subscription Management](../../subscription-management/concept/managing-user-subscriptions-v2.md) and contact your account representative.

**Important:** Avoid granting an admin role when more specialized roles are available.

## Administrator \[admin\]

The administrator role. This role has access to all system features, functions, and data because administrators can override access control list \(ACL\) rules and pass all role checks. Avoid assigning this role to your users when more targeted roles are available.

-   **Contains Roles**

    List of roles contained within the role.

    -   ais\_admin
    -   announcement\_admin
    -   catalog
    -   catalog\_admin
    -   catalog\_builder\_editor
    -   catalog\_lookup\_admin
    -   catalog\_template\_editor
    -   chat\_admin
    -   evam\_admin
    -   image\_admin
    -   import\_admin
    -   import\_scheduler
    -   import\_set\_loader
    -   import\_transformer
    -   live\_feed\_admin
    -   ml\_admin
    -   ml\_labeler
    -   nlu\_admin
    -   nlu\_editor
    -   nlu\_user
    -   pa\_data\_collector
    -   pa\_viewer
    -   personalize\_dictionary
    -   platform\_ml\_create
    -   platform\_ml\_read
    -   platform\_ml\_write
    -   search\_application\_admin
    -   search\_relevancy\_model\_admin
    -   sn\_ace.ace\_user
    -   sn\_employee.admin
    -   sn\_hr\_sp.admin
    -   sn\_hr\_sp.esc\_admin
    -   sn\_nlu\_workbench.nlu\_feedback\_admin
    -   sn\_templated\_snip.template\_snippet\_admin
    -   sn\_templated\_snip.template\_snippet\_reader
    -   sn\_templated\_snip.template\_snippet\_writer
    -   sp\_admin
    -   taxonomy\_admin
    -   user\_criteria\_admin
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    Grant this privilege carefully. If you have sensitive information, such as HR records, that you must protect, create a custom admin role for that area. Train any users authorized to see those records to act as the administrator. Also note the [Special Administrative Roles](r_SpecialAdministrativeRoles.md#).

    **Note:** Users with roles related to the Key Management Framework can only be modified by admins with the kmf\_admin role. For details on KMF roles, see [Roles installed with Key Management Framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/kmf-roles.md).


## Agent administrator \[agent\_admin\]

Agent administrators can download and administer the built-in system agent. They can manage MID Server-related scripts.

-   **Contains Roles**

    List of roles contained within the role.

    -   agent\_security\_admin
    -   view\_changer
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## AI search administrator \[ais\_admin\]

AI search administrators can query, create, update, and delete indexing and search settings and log messages through the [AI Search](../../ai-search/concept/overview-ais.md) application.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Application client company installer \[app\_client\_company\_installer\]

Users assigned the app\_client\_company\_installer role can install applications containing the same company as the currently logged in instance. Assigning this role enables first-time installation of applications for the company associated with the current instance. Users with this role can’t install an application for another company.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Application client user \[app\_client\_user\]

Application client users can install applications containing the same company as the currently logged in instance.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Approval administrator \[approval\_admin\]

Approval administrators can view or modify approval requests not directly assigned to them. Use the approver\_user role to enable approvers to view or modify only requests directly assigned to them.

Fulfillers may approve within the product to which they are subscribed \(ITSM Fulfiller approving within ITSM\). This approval may be in the platform or via email. No additional entitlement is required.

Fulfillers may not approve beyond the product to which they are subscribed \(ITSM Fulfiller approving within Procurement, GRC, etc.\). This approval would need an additional approval entitlement for the user.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Approver users \[approver\_user\]

Approver users can modify requests for approval routed to them. They also have all the capabilities of requesters.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    There’s a fee associated with this role. Don’t assign it to users without confirming your organization has the appropriate entitlement.


## Asset user \[asset\]

Asset users can manage hardware and software assets.

-   **Contains Roles**

    List of roles contained within the role.

    -   inventory\_user
    -   cmdb\_query\_builder
    -   canvas\_user
    -   financial\_mgmt\_user
    -   cmdb\_read
    -   contract\_manager
    -   category\_manager
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Assignment rule administrator \[assignment\_rule\_admin\]

Assignment rule administrators can manage assignment rules.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Business process administrator \[business\_process\_admin\]

Business process admins can create, read, update, and delete all records and their relationships in the business process.

In the context of Governance, Risk, and Compliance \(GRC\), users with the sn\_grc.admin role who manage GRC applications and their setup automatically gain access to this role. This access enables the GRC administrators to administer a business process and its records similar to other GRC tables.

-   **Contains Roles**

    List of roles contained within the role: business\_process\_manager.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    This role is assigned to users who are administrators and have thorough information and training on business processes. None.


## Business process manager \[business\_process\_manager\]

Business process managers can create, read, and update any business process and manage the relationship of business processes with other records. This role is assigned to business process managers who are usually specialists and manage multiple business processes in the organization. Assign this role to users who generally work with other employees and are experts around business processes.

In the context of GRC, users with the sn\_grc.manager role automatically inherit this role that enables them to manage the business processes for the entire organization.

-   **Contains Roles**

    List of roles contained within the role - business\_process\_user.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Business process user \[business\_process\_user\]

Business process users can update the business processes that a user owns and can also read any business process. This role must be assigned to the respective process owners. This role can also be provided to users who are required to view the business processes in the organization and understand them better.

In the context of GRC, users with the sn\_risk.user role are automatically assigned this role. This role enables users to manage the business processes that they own as well as read all business processes.

-   **Contains Roles**

    List of roles contained within the role- cmdb\_read.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Catalog administrator \[catalog\_admin\]

Catalog administrators can manage the Service Catalog application, including catalog categories and items.

-   **Contains Roles**

    List of roles contained within the role.

    -   user\_criteria\_admin
    -   catalog\_builder\_editor
    -   catalog\_template\_editor
    -   catalog
    -   catalog\_lookup\_admin
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Catalog editor \[catalog\_editor\]

Catalog editors can create, modify, and publish items within categories that they’re assigned to.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Catalog item designer \[catalog\_item\_designer\]

Catalog item designers can view the status of their category requests. This role is granted automatically to users when they make a request for an item designer category.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Catalog manager \[catalog\_manager\]

Catalog managers can view and assign catalog editors to their categories. They can also create, modify, and publish items within their categories.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Catalog user \[catalog\]

Catalog users have read and some write access to all Service Catalog Requests, Tasks, and Items.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    -   Catalog Request Approvers &gt; $1000
    -   Catalog Request Approvers for Sales
    -   Field Services
-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Category manager \[category\_manager\]

Category managers can create, edit, and delete model categories.

-   **Contains Roles**

    List of roles contained within the role - model\_manager.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CMDB administrator \[sn\_cmdb\_admin\]

The configuration management data base \(CMDB\) administrator is a key role required for interacting with the CMDB Workspaceand the Service Graph Workspace. CMDB administrators can access all CMDB data, tools, and UIs within the CMDB Workspaceand Service Graph Workspace. Users with this role can set policies that an editor can't, such as class manager and app service requirements.

As you drill down in the CMDB Workspaceor the Service Graph Workspace, there are some dashboards and list views that require specific roles in addition to the CMDB Admin, CMDB Editor, or CMDB User roles.

-   **Contains Roles**

    List of roles contained within the role.

    -   canvas\_admin
    -   cmdb\_ms\_admin
    -   data\_manager\_admin
    -   sn\_cmdb\_editor
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## CMDB de-duplication administrator \[cmdb\_dedup\_admin\]

CMDB de-duplication admins can review and remediate CMDB de-duplication tasks.

-   **Contains Roles**

    List of roles contained within the role - cmdb\_read.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## CMDB editor \[sn\_cmdb\_editor\]

A key role required for interacting with CMDB Workspaceand the Service Graph Workspace. CMDB editors can create, edit, and delete CMDB records but can't change policies such as data manager, class manager within CMDB Workspaceor Service Graph Workspace.

As you drill down in the CMDB Workspaceor Service Graph Workspace, there are some dashboards and list views that require specific roles in addition to the key CMDB Admin, CMDB Editor, or CMDB User roles.

-   **Contains Roles**

    List of roles contained within the role.

    -   cmdb\_ms\_editor
    -   sn\_cmdb\_user
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CMDB multi-source administrator \[cmdb\_ms\_admin\]

The CMDB multi-source administrator can create and run a query and can modify CMDB 360 properties. Contains the cmdb\_ms\_write role.

-   **Contains Roles**

    List of roles contained within the role - cmdb\_ms\_editor.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## CMDB multi-source editor \[cmdb\_ms\_editor\]

CMDB multi-source editors can create and query, read, and write CMDB records, but can't perform recomputing actions.

-   **Contains Roles**

    List of roles contained within the role - cmdb\_ms\_user.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CMDB multi-source user \[cmdb\_ms\_user\]

CMDB multi-source users have read and execute access to the multi-source queries.

-   **Contains Roles**

    List of roles contained within the role - cmdb\_read.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CMDB reader \[cmdb\_read\]

CMDB reader users can read data from the CMDB hierarchy.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CMDB user \[sn\_cmdb\_user\]

A key role required for interacting with CMDB Workspaceand the Service Graph Workspace. CMDB users have read-only access to CMDB data and basic UI within CMDB Workspaceand Service Graph Workspace.

As you drill down in the CMDB Workspaceor in Service Graph Workspace, there are some dashboards and list views that require specific roles in addition to the key CMDB Admin, CMDB Editor, or CMDB User roles.

-   **Contains Roles**

    List of roles contained within the role.

    -   app\_service\_user
    -   canvas\_user
    -   cmdb\_ms\_user
    -   cmdb\_query\_builder
    -   data\_manager\_user
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Contract manager \[contract\_manager\]

Contract managers can create, edit, and delete contracts through the Contract Management application.

-   **Contains Roles**

    List of roles contained within the role.

    -   canvas\_user
    -   financial\_mgmt\_user
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## CreateNow unlimited \[unlimited\_createnow\]

Role for CreateNow unlimited licensed users.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Data classification administrator \[data\_classification\_admin\]

Data classification administrators manage all aspects of the Data Classification application, data classification code setup, and assignment.

-   **Contains Roles**

    List of roles contained within the role - data\_classification\_auditor.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Data classification auditor \[data\_classification\_auditor\]

Data classification auditors audit Data Classification code assignments.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Enterprise CMDB administrator \[ecmdb\_admin\]

Enterprise CMDB administrators can perform administrative tasks and access tables and records in Enterprise CMDB.

-   **Contains Roles**

    List of roles contained within the role - cmdb\_read.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Filter administrator \[filter\_admin\]

Filter administrators can create, edit, and delete filter \[sys\_filter\] records.

-   **Contains Roles**

    List of roles contained within the role.

    -   filter\_global
    -   filter\_group
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Filter group user \[filter\_group\]

Filter group users can create filters that belong to groups of which the user is a member.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Gauge maker \[gauge\_maker\]

Gauge makers can create gauges from reports. Starting with Helsinki, reports are no longer made into gauges.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Global filter user \[filter\_global\]

Global filter users can create global filter \[sys\_filter\] records.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Global template editor \[template\_editor\_global\]

Users with the template\_editor\_global role can create templates for global use.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Group template editor \[template\_editor\_group\]

Users with the template\_editor\_group role can create templates for groups. \(Users must also be assigned the template\_read\_global role\)

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Guided tour administrator \[guided\_tour\_admin\]

Guided tour administrators can create, modify, and delete guided tour \[sys\_embedded\_tour\_guide\] records.

-   **Contains Roles**

    List of roles contained within the role - sn\_tourbuilder.tour\_admin.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Image administrator \[image\_admin\]

Image administrators can create, modify, and delete image \[db\_image\] records.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Impersonator \[impersonator\]

Impersonators can impersonate users.

**Warning:** This role doesn’t enable the impersonation of admin users.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    For details on impersonation, see [Base system roles](r_BaseSystemRoles.md).


## Import administrator \[import\_admin\]

Import administrators can manage all aspects of import set \[sys\_import\_set\] records and imports.

-   **Contains Roles**

    List of roles contained within the role.

    -   import\_set\_loader
    -   import\_transformer
    -   import\_scheduler
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Import scheduler \[import\_scheduler\]

Import schedulers can schedule imports.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    **Warning:** Grant this role carefully. The import\_scheduler can execute scripts with administrator level privileges.


## Import set loader \[import\_set\_loader\]

Import set loader users can load import set \[sys\_import\_set\] records.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Import transformer \[import\_transformer\]

Import transformer users can manage import set transform map \[sys\_transform\_map\] records and run transforms.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Inventory administrator \[inventory\_admin\]

Inventory administrators administer stockrooms, stock models, stock rules.

-   **Contains Roles**

    List of roles contained within the role.

    -   inventory\_user
    -   canvas\_user
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Inventory user \[inventory\_user\]

Inventory users have access to stock information.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## ITIL

Information Technology Infrastructure Library \(ITIL\) users can open, update, close incidents, problems, changes, and read some rules, definitions, and CIs related to CMDB features. This role is the base system technician role. Users with the ITIL role can have tasks assigned to them.

-   **Contains Roles**

    List of roles contained within the role.

    -   agent\_workspace\_user
    -   app\_service\_user
    -   cmdb\_query\_builder
    -   cmdb\_read
    -   dependency\_views
    -   email\_composer
    -   snc\_platform\_rest\_api\_access
    -   sn\_change\_write
    -   sn\_comm\_management.comm\_plan\_viewer
    -   sn\_gd\_guidance.guidance\_user
    -   sn\_incident\_write
    -   sn\_nb\_action.next\_best\_action\_user
    -   sn\_problem\_write
    -   sn\_request\_write
    -   sn\_sow.sow\_list
    -   sn\_sow.sow\_user
    -   sn\_sttrm\_condition\_read
    -   survey\_reader
    -   template\_editor
    -   tracked\_file\_reader
    -   view\_changer
    -   viz\_creator
-   **Groups**

    List of groups this role is assigned to by default.

    -   Field Services
    -   Catalog Request Approvers &gt; $1000
    -   Catalog Request Approvers for Sales
-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## ITIL administrator \[itil\_admin\]

ITIL administrators can delete incidents, problems, changes, and other related records. This role is intended for team leads.

-   **Contains Roles**

    List of roles contained within the role.

    -   assessment\_admin
    -   sn\_bm\_client.benchmark\_data\_viewer
    -   cmdb\_read
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    Avoid granting admin roles when more specialized roles are available.


## Knowledge \[knowledge\]

Knowledge users can write, edit, and review knowledge management articles.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Knowledge administrator \[knowledge\_admin\]

Knowledge administrators can manage knowledge bases.

-   **Contains Roles**

    List of roles contained within the role - knowledge.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## List updater \[list\_updater\]

List updater users can select the **Update Entire List** and **Update Selected** menu options on a list.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Maintenance

This role is reserved for ServiceNow use.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    This role can’t be assigned or impersonated, and is reserved for ServiceNow use.


## MID server \[mid\_server\]

MID server users can access to the tables that MID servers ordinarily use. This role should be granted to your MID servers.

-   **Contains Roles**

    List of roles contained within the role - soap.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    This role should be assigned to user accounts created for MID servers to interact with your instance. For details, see [Create the MID Server user and grant the role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/t_SetupMIDServerRole.md).


## Model manager \[model\_manager\]

Model managers can create, modify, and delete base model \[cmdb\_model\] records.

-   **Contains Roles**

    List of roles contained within the role - catalog\_editor.

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None.


## Personalize \[personalize\]

Users with the personalize role can personalize forms, lists, rules, controls, and scripts.

-   **Contains Roles**

    List of roles contained within the role.

    -   personalize\_control
    -   personalize\_rules
    -   personalize\_dictionary
    -   personalize\_choices
    -   personalize\_styles
    -   personalize\_responses
    -   personalize\_list
    -   personalize\_form
-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize choices \[personalize\_choices\]

Users assigned to the personalize\_choices role can personalize the choices for a list field.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize control \[personalize\_control\]

Personalize control users can personalize controls on lists, such as filters, links, and buttons.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize dictionary \[personalize\_dictionary\]

Users with the personalize\_dictionary role can personalize dictionary entries and labels.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize form \[personalize\_form\]

Users with the personalize\_form role can personalize forms.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize list \[personalize\_list\]

Users with the personalize\_list role can personalize lists.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize responses \[personalize\_responses\]

Users with the personalize\_form role can personalize predefined responses for suggestion fields, such as the additional comments field.

-   **Contains Roles**

    List of roles contained within the role.

    None

-   **Groups**

    List of groups this role is assigned to by default.

    None

-   **Elevated**

    Whether the role is an elevated role. Elevated roles aren’t assigned to users or groups, and must be used by elevation. For details, see [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md).

    No

-   **Special considerations**

    None


## Personalize rules \[personalize\_rules\]

Personalize rules users can personalize business rules and scripts. This role contains additional roles for granting selective, administrative access to rules and scripts.

-   **Contains Roles**

    List of roles contained within the role.

    -   ui\_action\_admin
    -   business\_rule\_admin
    -   client\_script\_admin
    -   ui\_policy\_admin
-   **Groups**

    List of
```


### File: platform-administration\user-administration\r_NormalizedCompanyNames.md

```text
---
title: Normalized company names table
description: The Normalization Data Services plugin stores the normalized company names in the Normalized Company Names table.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [data]
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Normalized company names table

The Normalization Data Services plugin stores the normalized company names in the Normalized Company Names table.

|Field|Description|
|-----|-----------|
|Name|The normalized name for this company.|
|Table|The table in which this name is stored.|
|Description|\[optional\] A description with further information about this company or record.|
|Field|The field in which this name is stored.|
|Customer override|**True**, if the customer has an override in place for this name. Otherwise, **false**.|

|List|Description|
|----|-----------|
|Normalized mappings|A list of all the discovered names that map to this normalized name.|

See [KB0819618](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819618) for more information.

**Parent Topic:**[Normalization data services](../concept/c_NormalizationOverview.md)


```


### File: platform-administration\user-administration\r_NormalizedMappings.md

```text
---
title: Normalized Mappings table
description: The Normalized Mappings table lists all the discovered names and the normalized name to which each maps.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [data]
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Normalized Mappings table

The Normalized Mappings table lists all the discovered names and the normalized name to which each maps.

|Field|Description|
|-----|-----------|
|Discovered name|A variant of a normalized name in the database.|
|Normalized name|The normalized name to which the discovered name maps.|
|Table|The table in which this name is stored.|
|Field|The field in which this name is stored.|

|List|Description|
|----|-----------|
|Related mappings|A list of all the discovered names that map to the same normalized name as the selected record.|

|List|Description|
|----|-----------|
|Promote discovered name|Replaces the normalized name with the discovered name for the selected record and for all the records in its related mappings list.|

**Parent Topic:**[Normalization data services](../concept/c_NormalizationOverview.md)


```


### File: platform-administration\user-administration\r_NormalizedProperties.md

```text
---
title: Normalization properties
description: On the normalization properties form, you can see and change the configurable properties for the Normalization Data Services plugin.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Normalization data services, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Normalization properties

On the normalization properties form, you can see and change the configurable properties for the Normalization Data Services plugin.

|Field|Description|
|-----|-----------|
|Reference qualifiers on all tables that reference the company will be updated to use the Normalized field.|If **Yes**, any reference field for the company – for any table across the platform – uses the Normalized name. This service only works if you have run the Update Reference Qualifiers task in the Guided Setup.|
|Enable a business rule that automatically normalizes manufacturer names for configuration items.|If **Yes**, the system normalizes company names when you add or update configuration items by a mechanism other than Discovery \(such as by manual import sets\).|
|Enable Discovery to use the normalization service for the manufacturer name.|To have Discovery use the normalized company name for the manufacturer name, select **Yes**.|
|This property is to enable or disable the Normalization process.|To enable the Normalization Data Service process, select **Yes**. To disable, select **No**. For details, see [Normalization data services](../concept/c_NormalizationOverview.md).|
|Normalize existing canonical core\_company records.|Select **Yes** to update an existing normalized \(canonical=true\) Companies record to not-normalized \(canonical=false\) if a mapping is present. For details, see [KB0957144](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0957144).|

**Parent Topic:**[Normalization data services](../concept/c_NormalizationOverview.md)


```


### File: platform-administration\user-administration\r_SpecialAdministrativeRoles.md

```text
---
title: Special administrative roles
description: Certain roles grant specific administrative rights without the full privileges of the admin role. For example, an administrator can grant a user the right to change UI policy but not client scripts.Create, modify, and delete assignment rulesThe instance can automatically assign a task to a user or group based on pre-defined conditions by using data lookup rules and assignment rules..Create, modify, and delete Business rules./&gt;.Create, modify, and delete client scripts.Create, modify, and delete forms, and form sections and section elements.Manage, share, publish, and schedule all reports. Users assigned this role can access the Reports Administration module and manage all report-related objects. The report\_admin role inherits all other report roles.Create, modify, and delete Script Includes.Create, modify, and delete UI actions.Create, modify, and delete UI macros.Create, modify, and delete UI pages.Create, modify, and delete using UI policies.Create, modify, and delete UI scripts.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Base system roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Special administrative roles

Certain roles grant specific administrative rights without the full privileges of the admin role. For example, an administrator can grant a user the right to change UI policy but not client scripts.

To learn more about managing per-user subscriptions, see [Managing per-user subscriptions in Subscription Management](../../subscription-management/concept/managing-user-subscriptions-v2.md) and contact your account representative.

These roles don’t change the behavior of the admin role, which grants full administrative privileges.

**Important:** You can’t rename roles of any kind in the ServiceNow AI Platform

**Parent Topic:**[Base system roles](r_BaseSystemRoles.md)

## Assignment rule administrator \[assignment\_rule\_admin\]

Create, modify, and delete [assignment rules](../../task-table/concept/c_DefineAssignmentRules.md).

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## Business rule administrator \[business\_rule\_admin\]

Create, modify, and delete Business rules./&gt;.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## Client script administrator \[client\_script\_admin\]

Create, modify, and delete client scripts.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## Form administrator \[form\_admin\]

Create, modify, and delete forms, and form sections and section elements.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## Report administrator \[report\_admin\]

Manage, share, publish, and schedule all reports. Users assigned this role can access the **Reports** &gt; **Administration** module and manage all report-related objects. The report\_admin role inherits all other report roles.

### Contains Roles

List of roles contained within the role.

-   gauge\_maker
-   report\_alias\_admin
-   report\_global
-   report\_group
-   report\_publisher
-   report\_scheduler
-   viz\_admin

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## Script include administrator \[script\_include\_admin\]

Create, modify, and delete Script Includes.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## UI action administrator \[ui\_action\_admin\]

Create, modify, and delete UI actions.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## UI macro administrator \[ui\_macro\_admin\]

Create, modify, and delete UI macros.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## UI page administrator \[ui\_page\_admin\]

Create, modify, and delete UI pages.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## UI policy administrator \[ui\_policy\_admin\]

Create, modify, and delete using UI policies.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.

## UI script administrator \[ui\_script\_admin\]

Create, modify, and delete UI scripts.

### Contains Roles

List of roles contained within the role.

None.

### Groups

List of groups this role is assigned to by default.

None.

### Special considerations

**Note:** Avoid granting an admin role when more specialized roles are available.


```


### File: platform-administration\user-administration\t_AddANewCompany.md

```text
---
title: Add a new company
description: You can add companies that represent vendors, manufacturers, or customers with whom you do business. These companies provide a way to categorize users, groups, and assets.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Add a new company

You can add companies that represent vendors, manufacturers, or customers with whom you do business. These companies provide a way to categorize users, groups, and assets.

## Before you begin

Role required: user\_admin or admin

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Companies**.

2.  Click **New**.

3.  Complete the form with the company details.

<table id="table_x3s_msg_m4"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the company.

</td></tr><tr><td>

Phone

</td><td>

Company phone number.

</td></tr><tr><td>

Fax phone

</td><td>

Company fax number.

</td></tr><tr><td>

Manufacturer

</td><td>

Whether the company is a manufacturer.

</td></tr><tr><td>

Vendor

</td><td>

Whether the company is a vendor.

</td></tr><tr><td>

Stock symbol

</td><td>

Three or four letter stock symbol for the company.

</td></tr><tr><td>

Stock price

</td><td>

Current price at which company stock is sold.

</td></tr><tr><td>

Street

</td><td>

Mailing street address of the company.

</td></tr><tr><td>

City

</td><td>

City in which the company is located.

</td></tr><tr><td>

State

</td><td>

State or province in which the company is located.

</td></tr><tr><td>

Zip/Postal code

</td><td>

Zip or postal code for the company.

</td></tr><tr><td>

Notes

</td><td>

Any information about the company that would be helpful for others to know.

</td></tr><tr><td class="sub-head" colspan="2">

Fields that can be added by [Personalize a form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md):

</td></tr><tr><td>

Latitude

</td><td>

The latitude of the company, if applicable. This field is populated by a business rule called **get\_lat\_long**. Deactivate this business rule to prevent the system from overwriting any values populated in the field manually. Latitude is expressed as a floating point data type. Latitude from upgraded versions of ServiceNow expressed in any format other than floating point appears in a column called **Old Latitude**. The system attempts to convert all latitude values from previous versions to the floating point notation, where possible.**Note:** This field doesn't display by default. You can add it by [personalizing the form.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md)

</td></tr><tr><td>

Longitude

</td><td>

The longitude of the company, if applicable. This field is populated by a business rule called **get\_lat\_long**. Deactivate this business rule to prevent the system from overwriting any values populated in the field manually. Longitude is expressed as a floating point data type. Longitude from upgraded versions of ServiceNow expressed in any format other than floating point appears in a column called **Old Longitude**. The system attempts to convert all longitude values from previous versions to the floating point notation, where possible.**Note:** This field doesn't display by default. You can add it by [personalizing the form.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md)

</td></tr></tbody>
</table>    **Note:** The IT Finance application adds a Finance view to the Company form. The Finance view adds a chart that shows expenses that were allocated to the company.


## What to do next

Normalize company data to create consistency when referring to a company name, such as a vendor or manufacturer. For more information see, [Normalization data services](../../normalization/concept/c_NormalizationOverview.md).

**Parent Topic:**[Creating users, companies, and departments](../../roles/concept/using-user-administration.md)


```


### File: platform-administration\user-administration\t_AddANewDepartment.md

```text
---
title: Add a department
description: Departments provide another way to categorize users, groups, and assets. You can add departments and assign them to users.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Add a department

Departments provide another way to categorize users, groups, and assets. You can add departments and assign them to users.

## Before you begin

Role required: user\_admin or admin

## About this task

An administrator may need to configure the form to show all the fields listed in the steps. For more information see [Personalize a form.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md)

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Departments** &gt; **Create a new record**.

2.  Enter or modify the department name, ID, and description.

3.  Select the company that the department is associated with.

4.  Add a department head, primary contact, or both from your list of users.

5.  Select **Submit**.


**Parent Topic:**[Creating users, companies, and departments](../../roles/concept/using-user-administration.md)


```


### File: platform-administration\user-administration\t_AddARoleToAnExistingRole.md

```text
---
title: Add a role to an existing role
description: When you add a new role to an existing role for a user, the user inherits the access that is granted by the new role.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Add a role to an existing role

When you add a new role to an existing role for a user, the user inherits the access that is granted by the new role.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Roles** and open the existing role.

2.  Click **Edit** in the Contains Roles related list.

3.  Use the slushbucket to add one or more roles to the existing role.

4.  Click **Save**.

    The users with the existing role inherit the access that is granted by the new role.


**Parent Topic:**[Create a role](t_CreateARole.md)


```


### File: platform-administration\user-administration\t_AddAUserToAGroup.md

```text
---
title: Add a user to a group
description: Add a user to a group so that the user inherits all the roles assigned to the group.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Creating groups, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Add a user to a group

Add a user to a group so that the user inherits all the roles assigned to the group.

## Before you begin

Role required: user\_admin

## About this task

If you’re a non-admin user, you can’t add a user to a group that contains the admin role. Likewise, if you don’t have a security\_admin role, you can’t add a user to a group that contains the security\_admin role.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Select a group **Name**.

3.  In the **Group Members** related list, select **Edit**.

4.  Select one or more names in the **Collection** list.

5.  Select **Add** and **Save**.

6.  Remove a user from a group when they change roles.

    1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

    2.  Select a group **Name**.

    3.  In the **Group Members** related list, select the check box next to each group member name you want to remove.

    4.  From the **Actions on selected rows** menu, select **Delete**.

        **Note:** Before selecting **Delete**, first make sure you have properly selected the rows containing the users you want to remove from the group.


**Parent Topic:**[Creating groups](../../roles/concept/ua-creating-groups.md)


```


### File: platform-administration\user-administration\t_AssignARoleToAUser.md

```text
---
title: Assign a role to a user
description: A user inherits roles from all groups to which they belong. You can also assign roles directly to a user. Whenever a user is assigned a new role, it only takes effect after logging in with a new session.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Assign a role to a user

A user inherits roles from all groups to which they belong. You can also assign roles directly to a user. Whenever a user is assigned a new role, it only takes effect after logging in with a new session.

## Before you begin

Role required: user\_admin or admin

When possible, simplify user administration by assigning roles to groups. Create groups that contain all the roles necessary for specific personas, and then assign users to those groups.

## About this task

To grant the admin role to a user, you must also have the admin role. To grant the security\_admin role to a user, you must also have the security\_admin role. You must elevate to the security\_admin role before granting the security\_admin role to other users. See [Elevate to a privileged role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/t_ElevateToAPrivilegedRole.md).

**Note:**

The System administrator\(admin\) role provides access to all system features, functions, and data, regardless of security constraints. Avoid assigning this role to your users when more targeted roles are available.

You can’t delete roles that are assigned to the group from the user record. You must remove the user from the group record.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users** and then open a user record.

2.  In the **Roles** related list, select **Edit**.

3.  In the **Collection** list, select the desired roles, and then select **Add**.

4.  Select **Save**.


## What to do next

**Note:** If the user is logged in when you update their roles and they’re unable to access records enabled by the new role, they may need to log out and back in again.

**Parent Topic:**[Create a role](../../roles/task/t_CreateARole.md)


```


### File: platform-administration\user-administration\t_AssignRoleToGroup.md

```text
---
title: Assign a role to a group
description: You can assign a role to a group to grant access to applications and modules to group members.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Assign a role to a group

You can assign a role to a group to grant access to applications and modules to group members.

## Before you begin

Role required: user\_admin or admin

## About this task

When you assign roles to groups rather than to individual users, members of the group inherit the role. When a user switches groups, the new group role is assigned automatically. For information about the Service Mapping roles, see [Control user access to application services](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/service-mapping/control-user-access-to-business-services.md).

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Select the group to assign a role.

3.  In the **Roles** related list, select **Edit**.

4.  Add the desired roles to the group.

5.  Select **Save**.


**Parent Topic:**[Create a role](t_CreateARole.md)


```


### File: platform-administration\user-administration\t_CreateAGroup.md

```text
---
title: Create a user group
description: Create groups and assign roles to them. Users assigned to the group inherit the roles.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Creating groups, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Create a user group

Create groups and assign roles to them. Users assigned to the group inherit the roles.

## Before you begin

Role required: user\_admin

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Select **New**.

3.  On the form, fill in the fields.

    Some fields appear after personalizing the form. [Personalize a form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md).

<table id="table_flh_qwv_sbb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the group.

</td></tr><tr><td>

Manager

</td><td>

Group manager or lead.

</td></tr><tr><td>

Type

</td><td>

Category for this group. For example, a group designated as type **catalog** is a service catalog group and can also be accessed under the **Service Catalog** &gt; **Catalog Policy** &gt; **Fulfillment Groups** module. See [Configure assignment group types](../concept/c_ConfigGroupTypesForAssignGroups.md#) for more information.You may need to [Personalize a form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/t_PersonalizeAForm.md) to add the **Type** field. Activating the Work Management plugin adds the **Type** field automatically.

**Note:** ITIL is added for groups with an empty group type. Also, the default reference qualifier for tasks enables these groups to assign tasks and other task types to the group.

</td></tr><tr><td>

Group email

</td><td>

Group email distribution list or the email address of the point of contact, such as the group manager.

</td></tr><tr><td>

Parent

</td><td>

Other group of which this group is a member. If a group has a parent, the child group inherits the roles of the parent group. The members of the child group aren’t members of the parent group. For example, if an incident is assigned to the parent group and you select the **Assigned to** lookup icon, only the members in the parent group are available. The members of the child group aren’t available.

</td></tr><tr><td>

Active

</td><td>

Check box that indicates whether the group is active or inactive. Inactive groups still appear in any reference field that already references the group, but aren’t visible by non-admin users in:-   lists of groups
-   the reference lookup list for reference fields
-   the auto-complete list of groups displayed when you type into a reference field


</td></tr><tr><td>

Exclude manager

</td><td>

Check box that controls whether the group manager receives email notifications.

</td></tr><tr><td>

Include members

</td><td>

Check box that controls whether the group members receive individual emails when someone sends an email to the **Group Email** address. The only exception to this functionality is for approval notifications, whereby all members of a group receive an approval notification, regardless of the **Include members** selection. See [Receive notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/approvals/c_ReceiveNotifications.md) for more information.

</td></tr><tr><td>

Description

</td><td>

Helpful information about the group.

</td></tr></tbody>
</table>4.  Remove or hide a group.

    1.  **Note:** Only users in the hidden group are able to see the hidden group when selecting a group in a reference field.

        Create a true/false field labeled `Hidden` on the Group form.

        For more information on creating fields, see [Add and customize a field in a table](../../field-administration/task/t_CreatingNewFields.md)

        The system creates a field called **u\_hidden** on the **Users \[sys\_user\_group\]** table and enables use of the **Hidden** check box to designate a hidden group.

    2.  Create a new before query business rule on the \[sys\_user\_group\] \(Group\) table with the following script:

        ```
        if (!gs.hasRole("admin") && !gs.hasRole("groups_admin") && gs.getSession().isInteractive()) { 
          var qc = current.addQuery("u_hidden", "!=", "true"); //cannot see hidden groups... 
          qc.addOrCondition("sys_id", "javascript:getMyGroups()"); //...unless in the hidden group 
        }
        ```

        **Note:** For more information, see [Before Query business rules](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/bp-before-query-business-rules.md).


## Result

The user group is created based on the configuration that you've provided.

**Note:**

When `glide.ui.schedule_job_for_group_parent_change` is set to true, removing a parent group results in the roles of the parent group being added to the child group asynchronously. If `glide.ui.schedule_job_for_group_parent_change` is set to false, the roles of the parent group are added to the child group synchronously when the parent group is removed.

**Parent Topic:**[Creating groups](../../roles/concept/ua-creating-groups.md)


```


### File: platform-administration\user-administration\t_CreateAGroupRole.md

```text
---
title: Create a group role
description: Create a group role to control access to features and capabilities in applications for all members in a group.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Create a group role

Create a group role to control access to features and capabilities in applications for all members in a group.

## Before you begin

Role required: admin.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Group Roles**.

2.  Select **New**.

3.  Fill in the fields on the form and then select **Submit**.

    |Field|Description|
    |-----|-----------|
    |Group|Select a group.|
    |Role|Select the role to apply to the group.|
    |Inherits|Select this option to have all members of the group inherit the role. This option is selected by default.|

    **Note:** To move this action to the background so you aren’t waiting when adding a number of group members, add the system property **glide.ui.schedule\_slushbucket\_save\_for\_group\_roles** and set it to true.


**Parent Topic:**[Create a role](t_CreateARole.md)


```


### File: platform-administration\user-administration\t_CreateARole.md

```text
---
title: Create a role
description: Create a role to control access to features and capabilities in applications and modules. The new role doesn’t have access to any application or module until you add other roles to it, or add it to the appropriate applications and modules.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Create a role

Create a role to control access to features and capabilities in applications and modules. The new role doesn’t have access to any application or module until you add other roles to it, or add it to the appropriate applications and modules.

## Before you begin

Role required: admin

## About this task

After access has been granted to a role, all groups or users assigned to the role are granted the access. Roles can contain other roles, and any access granted to a role is granted to any role that contains it.

For a complete list of the roles included with the base instance, see [Base system roles](../reference/r_BaseSystemRoles.md)

**Note:**

You can’t rename roles of any kind in the ServiceNow AI Platform. If you manually create a role, you can’t rename it after you save it.

Move this action to the background so you aren’t waiting when adding a number of group members by adding the system property **glide.ui.schedule\_slushbucket\_save\_for\_group\_roles**. Set the system property to **true**. The system user is used to create records or update existing ones since the action is running in the background.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Roles** and create a record.

2.  Complete the form.

<table id="table_cgz_hzf_xq"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Enter a name for the role.

</td></tr><tr><td>

Requires Subscription

</td><td>

Indicates whether users with this role require a subscription to stay in compliance. -   **Yes**

Measured-role that requires a subscription. You can allocate subscriptions to users with this role by adding one or more groups to a product subscription. To learn more, see [Managing per-user subscriptions in Subscription Management](../../subscription-management/concept/managing-user-subscriptions-v2.md).

-   **No**

Not a measured-role.

-   **Unspecified**

Neither

</td></tr><tr><td>

Application

</td><td>

Select the application that contains this record.

</td></tr><tr><td>

Elevated privilege

</td><td>

A role that requires elevated privilege can’t be assigned to a user at login by the system. Instead, a user must manually elevate privileges to receive the elevated role. Select this option to mark this role as required to elevate it to high security. See [Elevated privilege roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_ElevatedPrivilege.md) for more information.

</td></tr><tr><td>

Description

</td><td>

Select the roles to delegate to the group member.

</td></tr></tbody>
</table>
-   **[Grant a role access to applications and modules](t_GrantARoleAccessToAppsAndModules.md)**  
Roles control access to features and capabilities in applications and modules. You add a role to an application or module to enable the role to grant access to the application or module for all users with the role.
-   **[Assign a role to a group](t_AssignRoleToGroup.md)**  
You can assign a role to a group to grant access to applications and modules to group members.
-   **[Assign a role to a user](../../users-and-groups/task/t_AssignARoleToAUser.md)**  
A user inherits roles from all groups to which they belong. You can also assign roles directly to a user. Whenever a user is assigned a new role, it only takes effect after logging in with a new session.
-   **[Add a role to an existing role](t_AddARoleToAnExistingRole.md)**  
When you add a new role to an existing role for a user, the user inherits the access that is granted by the new role.
-   **[Create a group role](t_CreateAGroupRole.md)**  
Create a group role to control access to features and capabilities in applications for all members in a group.

**Parent Topic:**[Managing roles](../concept/ua-creating-roles.md)


```


### File: platform-administration\user-administration\t_CreateAUser.md

```text
---
title: Create a user
description: You can add a user to your instance to enable them to log in and use designated application features.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Creating users, Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Create a user

You can add a user to your instance to enable them to log in and use designated application features.

## Before you begin

Role required: user\_admin

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users**.

2.  Select **New**.

3.  On the form, fill in the fields.

<table id="t_CreateUserFields"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

User ID

</td><td>

Create a unique identifier for this user's ServiceNow login user name. Typical examples of user IDs are `cwitherspoon` and `charlie.witherspoon`. You can’t create a user whose User ID duplicates an existing user. If you do import duplicates from an update set, the more recently created name takes the duplicate User ID.

</td></tr><tr><td>

Given name

</td><td>

Enter the user's given \(often their first\) name.

</td></tr><tr><td>

Family name

</td><td>

Enter the user's family name \(often their last name\). **Note:** You can clear the **First Name** field, or the **Last Name** field in an existing user record, but you can’t clear both at the same time.

</td></tr><tr><td>

Title

</td><td>

Enter a title or job description, or select one from the list.

</td></tr><tr><td>

Department

</td><td>

Select the user's department from the list.

</td></tr><tr><td>

Password

</td><td>

Assign a password to the user. To set up the user's password, fill in the fields on the form and **save** the record. Then, select **Set Password**. This password can be permanent or temporary.

</td></tr><tr><td>

Password needs reset

</td><td>

Select this check box to require the user to change the password during the first login.

</td></tr><tr><td>

Locked out

</td><td>

Select this check box to lock the user out of the instance and terminate all their active sessions. The system helps prevent users with the admin role from locking themselves out.

</td></tr><tr><td>

Active

</td><td>

Select this check box to make this user active. Only the administrator sees an inactive user in: -   Lists of users
-   The selection list on reference fields \(magnifying glass icon\)
-   The auto-complete list that appears when you type into a reference field


</td></tr><tr><td>

Web service access only

</td><td>

It designates a user as a non-interactive user. This field is available with [Non-Interactive Sessions](../concept/c_NonInteractiveSessions.md#).**Note:** The Web service access only check box is automatically enabled when you select **Machine** in the Identity type field. The Web service access only check box is automatically disabled when you select **Human** or **AI**.

</td></tr><tr><td>

Internal Integration User

</td><td>

Select this check box to [Mark service accounts as internal integration users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/web-services/t_MarkSvcAcctsAsInternalIntegUsers.md).

</td></tr><tr><td>

Email

</td><td>

Enter the user's email address. To enter a non-standard email address that doesn’t pass field validation, you must deactivate the validation script first:

1.  Navigate to **System Definition** &gt; **Validation Scripts**.
2.  Select the **email** record.
3.  Clear the **Active** check box and save the change.
4.  Complete the user profile, including the email address, and update or submit the record.
5.  Reactivate the email validation script.


</td></tr><tr><td>

Identity type

</td><td>

Select the user identity type based on the user:-   Human - Select this for a real person, such as an employee, customer, or admin.
-   Machine - Select this for a non-human system or device, such as a server, application, or service account that makes automated requests.
-   AI - Select this for an autonomous AI-driven system. AI users should be used when an AI agent or agentic workflow needs permissions greater than that of the invoking user.

See [Security for AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/aia-security-implementation.md) for more information on using AI type users.

**Note:** The Web service access only check box is automatically enabled when you select **Machine** in the Identity type field. The Web service access only check box is automatically disabled when you select **Human** or **AI**.

</td></tr><tr><td>

Identity Subtype

</td><td>

Displays the identity type subtype based on the user login. For example:-   External
-   Internal
-   Guest


</td></tr><tr><td>

Language

</td><td>

Select your preferred language from the list.

</td></tr><tr><td>

Calendar integration

</td><td>

Select **Outlook** to have this user receive meeting notifications via email directly to the calendar. Otherwise, select **None**.

</td></tr><tr><td>

Time zone

</td><td>

Select the user's time zone.

</td></tr><tr><td>

Date format

</td><td>

Select the user's preferred format for dates. The following date formats are supported:-   08/19/26
-   19/08/26
-   08-19-2026
-   08/19/2026
-   19-08-2026
-   19/08/2026
-   19.08.2026
-   2026/08/19
-   2026.08.19
-   2026-08-19
For more information, see [GlideDateTime - Global](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideDateTimeAPI.md).

</td></tr><tr><td>

Time format

</td><td>

Select the user's preferred format for time. The following time formats are supported:-   16:30:45
-   16.30.45
-   04:30:45 PM
-   04.30.45 PM
-   16:30
-   16.30
-   04:30 PM
-   04.30 PM
For more information, see [GlideDateTime - Global](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/c_GlideDateTimeAPI.md).

</td></tr><tr><td>

Business phone

</td><td>

Enter the user's business phone number.

</td></tr><tr><td>

Mobile phone

</td><td>

Enter the user's mobile phone number.

</td></tr><tr><td>

Photo

</td><td>

Attach a photo of the user, if appropriate.

</td></tr></tbody>
</table>    The minimum fields required to create a user record are: **User ID** and either **First name** or **Last name**.

    You can select the **Personalize Form** icon to remove fields.

4.  Add **Roles**, **Groups**, **Delegates**, **Skills**, and **Subscriptions** to the user.

    For more information, see [Managing roles](../../roles/concept/ua-creating-roles.md), [Creating groups](../../roles/concept/ua-creating-groups.md), and [Delegating roles](../../roles/concept/c_DelegateRoles.md).

5.  Select **Submit**.

    The new user record appears in the list.


**Parent Topic:**[Creating users](../../roles/concept/ua-creating-users.md)


```


### File: platform-administration\user-administration\t_GrantARoleAccessToAppsAndModules.md

```text
---
title: Grant a role access to applications and modules
description: Roles control access to features and capabilities in applications and modules. You add a role to an application or module to enable the role to grant access to the application or module for all users with the role.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Grant a role access to applications and modules

Roles control access to features and capabilities in applications and modules. You add a role to an application or module to enable the role to grant access to the application or module for all users with the role.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Applications** or **System Definition** &gt; **Modules**.

2.  Select the appropriate application or module to open it in form view.

3.  Select the lock to open the **Roles** field.

4.  Add the desired roles to the application or module.

5.  Select the lock to close the **Roles** field, and then save your changes.


**Parent Topic:**[Create a role](t_CreateARole.md)


```


### File: platform-administration\user-administration\t_ImpersonateAUserInUI16.md

```text
---
title: Impersonate a user
description: You can select a user or enter a different user name to perform an impersonation.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Impersonating users, Monitoring user activity, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Impersonate a user

You can select a user or enter a different user name to perform an impersonation.

## Before you begin

Role required: impersonator

## Procedure

1.  In the banner frame, select your user profile picture to open the user menu.

2.  Select **Impersonate User**.

    -   In Next Experience:

        ![Impersonate user dialog box in Next Experience.](../image/impersonation-3.png)

    -   In Core UI:

        ![Impersonate User in Core UI](../image/imperson-CoreUI.png)

    The Impersonate user dialog box displays.

3.  Select a user from the **Recent Impersonations** list or enter a different user's name in the user selection field.

    -   In Next Experience:

        ![Impersonate user dialog box in Next Experience.](../image/impersonation-4.png)

    -   In Core UI:

        ![Impersonate User dialog box in Core UI](../image/impersonate-user-CoreUI.png)

4.  Select **Impersonate User**.

5.  To impersonate another user while impersonating a user, open the user menu and select **Impersonate another user**.

6.  To return to your original login, open the user menu and select **End Impersonation**.

    **Note:** In some cases, impersonating a user might cause an issue that makes it difficult to switch back. If you’re presented with a broken page while impersonating a user in a test environment, you may need to force a logout. To do so, navigate to http://&lt;instance name&gt;.service-now.com/logout.do and log back in.


**Parent Topic:**[Impersonating users](../concept/c_ImpersonateAUser.md)


```


### File: platform-administration\user-administration\t_PreventARoleFromBeingDelegated.md

```text
---
title: Prevent a role from being delegated
description: You can prevent roles from being delegated to users.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Delegating roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Prevent a role from being delegated

You can prevent roles from being delegated to users.

## Before you begin

Role required: admin

## About this task

By default, the following roles can’t be delegated.

-   admin
-   public
-   role\_delegator

    **Note:** A user with the role\_delegator role can’t delegate this role to other group members.


## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Roles**.

2.  Open the role.

3.  Configure the form to add the **Grantable** or **Can delegate** fields.

4.  Clear the check box for one or both of these fields.

5.  Select **Update**.


**Parent Topic:**[Delegating roles](../concept/c_DelegateRoles.md)


```


### File: platform-administration\user-administration\t_RoleDelegation.md

```text
---
title: Designate role delegators
description: Designate role delegators to assign roles to users who are in a particular group.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Delegating roles, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Designate role delegators

Designate role delegators to assign roles to users who are in a particular group.

## Before you begin

Role required: admin

## About this task

Delegators can assign roles that they inherit from a group. They can also assign roles that an administrator assigned to them.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Designate Role Delegator**.

2.  Select the group that includes the user who you want to be the role delegator.

3.  Select the user.

4.  Select **Submit**.

    A change request for the role delegator request is created and automatically approved.


**Parent Topic:**[Delegating roles](../concept/c_DelegateRoles.md)


```


### File: platform-administration\user-administration\time-limited-role-overview.md

```text
---
title: Time-limited role
description: Time-limited roles give users the defined role during the defined time period.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Time-limited role

Time-limited roles give users the defined role during the defined time period.

Assigning the time-limited roles ensures users have elevated access only when needed, without requiring manual revocation. When you assign a time-limited role to a user, you specify a start and end date. The system automatically activates the role at the start date and removes it when the end date passes, eliminating the need for manual access cleanup.

## Supported roles and limits

Time-limited roles enhance security by automatically reducing privileges when no longer needed, support compliance through time-bound access policies, and improve efficiency by eliminating manual tracking and revocation. The following table provides information about the available time-limited roles and limits:

<table id="table_db5_z3t_k3c"><thead><tr><th>

Supported Roles

</th><th>

Assignment Rules

</th></tr></thead><tbody><tr><td>

-   `admin`
-   `snc_read_only`
-   `impersonator`
-   `snc_required_script_writer_permission`

</td><td>

-   Maximum of four concurrent time-limited roles per user can be assigned
-   Time-limited role can be maximum of 5 days per user.
-   Time-limited assignments can handle more than one role assignment to a user, even if the total duration across assignments is less than five days.

</td></tr></tbody>
</table>-   **[Grant a time-limited user role](time-limited-roles.md#)**  
Learn how to assign a role to a user temporarily. Use this feature if you have a user who needs to perform a one-time action that is normally outside their roles.

**Parent Topic:**[Managing roles](ua-creating-roles.md)


```


### File: platform-administration\user-administration\time-limited-roles.md

```text
---
title: Grant a time-limited user role
description: Learn how to assign a role to a user temporarily. Use this feature if you have a user who needs to perform a one-time action that is normally outside their roles.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Time-limited role, Managing roles, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Grant a time-limited user role

Learn how to assign a role to a user temporarily. Use this feature if you have a user who needs to perform a one-time action that is normally outside their roles.

## Before you begin

Role required: user\_admin

**Note:**

-   Time-limited user roles can be assigned to a user for a maximum of 5 days.
-   For a user, you can assign only `admin`, `snc_read_only`, `impersonator`, and \(or\) `snc_required_script_writer_permission` role as time-limited role.
-   Time-limited user roles are not displayed to the assigned users under the **Roles** tab of the user \(sys\_user\) record.
-   When the time-limited role assigned users log in, they see a notification regarding the role assignment.
-   Time-limited assignments can handle more than one role assignment to a user, even if the total duration across assignments is less than five days.

## About this task

**Warning:** Usage of Time-limited User Roles may consume access and use rights procured by customer and could result in additional subscription fees.

## Procedure

1.  Navigate to **All** &gt; **** &gt; **User Administration** &gt; **Time-limited user roles**.

2.  Select **New**.

3.  Fill in the fields on the form.

    All fields except Comments are mandatory.

<table id="table_dxg_2qw_m1c"><thead><tr><th>

Fields

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Active

</td><td>

Determines if the time limited role assignment is active.

</td></tr><tr><td>

Role

</td><td>

The role assigned to the user. Only admin, impersonate, and snc\_readonly are allowed

</td></tr><tr><td>

User

</td><td>

The user to be assigned the time limited role

</td></tr><tr><td>

Start Time

</td><td>

The start time and date for the time limited role

</td></tr><tr><td>

End Time

</td><td>

The end time and date for the time limited role**Note:** **End Time** cannot be more than 5 days from the **Start Time**.

</td></tr><tr><td>

Comments \(Optional\)

</td><td>

Additional comments or information for the limited role assignment

</td></tr></tbody>
</table>4.  Select **Submit**.


## Result

The specified user now has the role. They must complete their restricted task between the start time and the end time.

**Parent Topic:**[Time-limited role](time-limited-role-overview.md)


```


### File: platform-administration\user-administration\ua-creating-groups.md

```text
---
title: Creating groups
description: Admins can add users to one or more groups.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Creating groups

Admins can add users to one or more groups.

-   **[Create a user group](../../users-and-groups/task/t_CreateAGroup.md#)**  
Create groups and assign roles to them. Users assigned to the group inherit the roles.
-   **[Add a user to a group](../../users-and-groups/task/t_AddAUserToAGroup.md)**  
Add a user to a group so that the user inherits all the roles assigned to the group.
-   **[Configure assignment group types](../../users-and-groups/concept/c_ConfigGroupTypesForAssignGroups.md#)**  
Use the **Type** field to define categories of groups. Once defined, you can use these categories to filter assignment groups based on the group type using a reference qualifier.

**Parent Topic:**[Configure ServiceNow AI Platform core features](../../general/concept/config-now-platform-core-features.md)


```


### File: platform-administration\user-administration\ua-creating-roles.md

```text
---
title: Managing roles
description: Administrators can create and configure roles that grant specific permissions, which govern what users and groups with that role can do.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Managing roles

Administrators can create and configure roles that grant specific permissions, which govern what users and groups with that role can do.

-   **[Base system roles](../reference/r_BaseSystemRoles.md)**  
Administrators can assign one or more base system user roles to grant access to base system platform features and applications.
-   **[Create a role](../task/t_CreateARole.md)**  
Create a role to control access to features and capabilities in applications and modules. The new role doesn’t have access to any application or module until you add other roles to it, or add it to the appropriate applications and modules.
-   **[Audit user roles](../task/audit-user-roles.md)**  
Changes to user roles are automatically tracked in the Audit Roles \[sys\_audit\_role\] table.
-   **[Delegating roles](c_DelegateRoles.md)**  
Administrators can grant users the ability to assign roles within groups. However, these users can only assign roles that they already have.
-   **[Time-limited role](time-limited-role-overview.md)**  
Time-limited roles give users the defined role during the defined time period.

**Parent Topic:**[Configure ServiceNow AI Platform core features](../../general/concept/config-now-platform-core-features.md)


```


### File: platform-administration\user-administration\ua-creating-users.md

```text
---
title: Creating users
description: Users are typically added through Lightweight Directory Access Protocol \(LDAP\) directory integrations. Admins can also manually add users to the instance, enable self-registration for new users, and impersonate users to ensure that they have the proper access privileges.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Creating users, companies, departments, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Creating users

Users are typically added through Lightweight Directory Access Protocol \(LDAP\) directory integrations. Admins can also manually add users to the instance, enable self-registration for new users, and impersonate users to ensure that they have the proper access privileges.

For more information on LDAP integrations, see [Lightweight Directory Access Protocol integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/ldap-integration/c_LDAPIntegration.md).

-   **[Create a user](../../users-and-groups/task/t_CreateAUser.md)**  
You can add a user to your instance to enable them to log in and use designated application features.
-   **[User self-registration](../../users-and-groups/concept/c_UserRegistration.md#)**  
The User Registration Request \[com.snc.user\_registration\] plugin provides the ability for unregistered users to request access to a ServiceNow instance. An administrator can activate the plugin.

**Parent Topic:**[Creating users, companies, and departments](using-user-administration.md)


```


### File: platform-administration\user-administration\user-admin-tools-landing.md

```text
---
title: Monitoring user activity
description: Learn about the tools available to administrators for monitoring users on their instance.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Monitoring user activity

Learn about the tools available to administrators for monitoring users on their instance.

## User administration tools

In addition to storing information on a user, user accounts are also associated to groups and roles. Your instance uses groups and roles to determine which records and features an individual may access.

-   **Impersonation**

    Administrators can select user records for impersonation. Use this feature to experience the instance as another user, with that user's preferences and permissions. User impersonation can be a valuable tool for testing and troubleshooting. For more information on impersonation, see [Impersonating users](../../users-and-groups/concept/c_ImpersonateAUser.md).

-   **Investigating user account activity**

    At any time there is a need to review specific user behavior, below are the recommended steps on how to review the transaction logs and event logs:

    -   Locate the IP address of successful/failed login for a particular ServiceNow user for their instance
    -   Modify the time frame of the search
    -   Limiting the scope of the search by user name
    -   View successful/failed login attempts
    For more information about investigating user activity, see the [How to investigate user account activity \[KB0564981\]](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564981) article in the Now Support Knowledge Base.

-   **User sessions**

    With user session management, and administrator can view and terminate individual user sessions, lock out users from the instance, and make users inactive. For details on managing user sessions, see [Managing user sessions](../../user-sessions/concept/c_ManageUserSessions.md#).

    User records are also associated with transaction logs. Administrators can use these logs to track all browser activity for an instance.


-   **[Impersonating users](../../users-and-groups/concept/c_ImpersonateAUser.md)**  
Administrators are able to impersonate other authenticated users, a feature primarily used for testing.
-   **[Managing user sessions](../../user-sessions/concept/c_ManageUserSessions.md#)**  
The ServiceNow AI Platform provides the ability to view and terminate individual user sessions, lock out users from the system, and make users inactive.
-   **[Non-interactive sessions](../../users-and-groups/concept/c_NonInteractiveSessions.md#)**  
The Non-Interactive Sessions plugin creates a distinction between interactive and non-interactive users.

**Parent Topic:**[Configure ServiceNow AI Platform core features](../../general/concept/config-now-platform-core-features.md)


```


### File: platform-administration\user-administration\user.md

```text
---
title: The User record
description: Learn about user records and their use within the ServiceNow AI Platform.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Exploring user admin, User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# The User record

Learn about user records and their use within the ServiceNow AI Platform.

## User account records

User records establish a relationship between an individual and your ServiceNow instance. User records consist of a user name, a password, and information relating to the individual, such as contact information, location, and job title.

![A sample user record.](../image/user-record.png "User record")

User records are stored in the Users \[sys\_user\] table.

## Related records

User records are associated with records on several other tables to control permissions, preferences, and other features.

-   **Roles**

    Roles control access to features and capabilities in applications and modules. For more information on roles, see [Managing roles](ua-creating-roles.md).

    **Note:**

    When possible, simplify user administration by assigning roles to groups. Create groups that contain all the roles necessary for specific personas, and then assign users to those groups.

-   **Groups**

    A group is a set of users who share a common purpose. Users assigned to groups are automatically assigned to all roles associated with that group. For more details, see [Creating groups](ua-creating-groups.md) and [Managing roles](ua-creating-roles.md).

-   **Delegates**

    In addition to role and group assignments, users can be assigned as delegates, giving them permission to act with the same permissions as a delegator user. See [Delegating roles](c_DelegateRoles.md) for more information on delegation.

-   **Skills**

    Use skill management to associate users with their areas of training and expertise. For more information on skill management, see [Skill Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/skills-management/skills-management.md).

-   **Subscriptions**

    Administrators use subscriptions to control which users have access to purchased subscriptions on their instances. Details on subscription management can be found at [Subscription Management](../../subscription-management/reference/subscription-management-landing-page-v2.md).

-   **User preferences**

    User accounts are also connected with user preferences. Users can save personalized preferences to configure many UI features, as well as preferences regarding the notifications they receive. Details on administering user preferences are found at [User preferences](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UserPreferences.md).


## Date and time formatting

You can set your preferred date and time formatting through the User record. If you don't specify a preference in these fields, the system applies default formatting.

The Date format field appears in the User record by default and can be modified without specific permissions. However, the Time format field must be added to the User record by revealing additional form fields. For instructions on showing or hiding form fields, see [Configuring the form layout](../../form-administration/concept/configure-form-layout.md#). If you can't modify form fields, contact your organization's user administrator to update your time format preferences.

The Date and time format field in **User Menu** &gt; **Preferences** &gt; **Language &amp; Region** extends the options you select in the Date format and Time format fields of your User record. For more information, see [User preferences](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_UserPreferences.md). Timezone settings automatically sync between the User record and your preferences.

## System and guest users

Some automated processes use the system or guest user to apply and track changes to records. As a result, some records may show that they were last updated by system or guest.

For example, when a user logs in for the first time in a day, some fields on that user's record are updated by the system user, such as **Last login** and **Last login time**. If a user has a failed login attempt or is locked out, some fields on that user's record are updated by the guest user, such as **Failed Login Attempts** or **Locked Out**.

If a record was last updated by the system or by guest users, identify the fields that were updated by enabling auditing for the table and viewing the audit history set. For more information, see [Configuring auditing for a table](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/t_EnableAuditingForATable.md) and [Knowing about History sets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/c_HistorySets.md).


```


### File: platform-administration\user-administration\using-user-administration.md

```text
---
title: Creating users, companies, and departments
description: Create user records for the individuals who access your instance. Users can be assigned to groups with defined roles to determine what records and actions they can access.
locale: en-US
release: australia
product: User Administration
classification: user-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Creating users, companies, and departments

Create user records for the individuals who access your instance. Users can be assigned to groups with defined roles to determine what records and actions they can access.

-   **[Creating users](ua-creating-users.md)**  
Users are typically added through Lightweight Directory Access Protocol \(LDAP\) directory integrations. Admins can also manually add users to the instance, enable self-registration for new users, and impersonate users to ensure that they have the proper access privileges.
-   **[Add a new company](../../users-and-groups/task/t_AddANewCompany.md)**  
You can add companies that represent vendors, manufacturers, or customers with whom you do business. These companies provide a way to categorize users, groups, and assets.
-   **[Normalization data services](../../normalization/concept/c_NormalizationOverview.md)**  
The Normalization Data Services plugin helps maintain consistency for table fields that refer to a company name.
-   **[Add a department](../../user-administration/task/t_AddANewDepartment.md)**  
Departments provide another way to categorize users, groups, and assets. You can add departments and assign them to users.

**Parent Topic:**[Configure ServiceNow AI Platform core features](../../general/concept/config-now-platform-core-features.md)


```
