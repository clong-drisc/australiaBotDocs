# service-exchange



---

## Folder: service-exchange



### File: service-exchange\import-and-export-fds-configuration.md

```text
---
title: Import and export foundation data sync configuration
description: Export ETL configurations for foundation data sync \(FDS\) from one instance to another using update sets.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring inbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Import and export foundation data sync configuration

Export ETL configurations for foundation data sync \(FDS\) from one instance to another using update sets.

## Before you begin

FDS requires the following fields on a subscription to be identical in both the exporting and importing instances to support linking or using imported configurations:

-   Offering definition name
-   List of tables offered as part of the offering
-   Cadence in subscription
-   Provider company name
-   FDS compatibility.

Also, the offering definition and connection company must be identical in both the exporting and importing instances.

Role required: admin

## About this task

You can export ETL configurations from one instance and import them into another. For example, you can configure ETL in a pre-production environment and then export those configurations and import them into a production environment. FDS supports this transfer through update sets, which enable seamless reuse of configurations.

## Procedure

1.  Export the ETL configuration.

    1.  Create a local update sets and mark it as current.

    2.  Request a foundation data sync \(FDS\) offering, complete the configuration, and verify that the data sync is working correctly.

        For more information on how to request a foundation data sync \(FDS\) offering, see [Request foundation data sync offerings](service-bridge-v2-request-fds-offerings.md).

    3.  Complete the update sets and export it.

        For more information on update sets, see [General guidelines for planning the update process](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/system-update-sets/get-started-update-sets.md).

2.  Import the ETL configuration to another instance.

    1.  In the new instance, request a foundation data sync \(FDS\) offering with same cadence as in [Step 1](import-and-export-fds-configuration.md#substeps_dwc_5l1_cgc).

    2.  After a subscription is created for your FDS request, and the request is in awaiting validation state, import the configuration that you have exported in Step 1.

        If you have any errors in the update sets, you can skip those files and commit the remaining files. Your configuration won't be affected. For more information on update sets, see [General guidelines for planning the update process](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/system-update-sets/get-started-update-sets.md).

    3.  Open the subscription and the subscription item.

    4.  Select **ETL Transform Map Assistance**.

        In the guided setup, step 1, step 2, and step 3 are marked as completed. For more information, see [Validate foundation data sync subscription items](service-bridge-v2-validate-fds-subscription.md)

    5.  Verify all the steps in ETL configuration to make sure everything is mapped correctly, and run the integration and perform rollback.

        For details, see [IntegrationHub ETL](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/integration-hub-etl/integrationhub-etl.md).



```


### File: service-exchange\index.md

```text
---
title: Australia Service Exchange
locale: en-US
release: australia
bundle: sebrdg
doc_type: toc
---

# Australia Service Exchange

- [Service Exchange](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/tmt-service-bridge-both-landing-page.md) -- ServiceNow Service Exchange connects multiple ServiceNow instances to provide seamless support and service experiences across the ecosystem, from enterprise customers to suppliers and system integrators. Service Exchange provides a frictionless experience that makes it easy to collaborate and process requests while giving users the convenience of working in their own ServiceNow instance.
  - [Explore](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-exploring-service-bridge.md) -- Service Exchange helps providers, consumers, and partners connect their ServiceNow instances to build secure business workflows across the ServiceNow ecosystem.
    - [Mismatched version support](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-mismatch-version.md) -- Providers and consumers using different versions of the Service Exchange applications can exchange and synchronize data between their ServiceNow instances.
    - [Configuring revisions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-config-revision.md) -- As a provider, you can update the configurations of remote record producers, remote task definitions, foundation data sync offerings, and create new versions that can be entitled to consumers.
    - [Remote catalogs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-apps.md) -- As an application developer for the provider, you can create a remote catalog item containing the services for your consumers. After you create these items, an administrator in the consumer’s instance can assign them to the consumer's catalogs and categories and then activate them, just like any other catalog item.
      - [Remote record producers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-record.md) -- Remote record producers in Service Exchange for Providers are service requests published in consumer instances. They enable your consumer to request provider services through their service catalog.
      - [Remote choice fields](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-choice-fields.md) -- Remote choice fields provide your consumers direct access to your (provider) data in real time while they submit a remote catalog item from their instance.
      - [Authorized users and personas](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-auth-users.md) -- The Authorized Users feature enables a provider to categorize remote catalog items by user personas so that only authorized users with these personas can access the catalog items. It also allows consumer admins to associate these personas to users in their instances to allow access.
    - [Proactive cases](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-proactive-case.md) -- Proactively notifies consumer users of case alerts and enables real-time collaboration with providers without any additional configuration in connected consumer instances.
    - [Provider tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-provider-tasks.md) -- Enable all providers using Service Exchange to be transparent and collaborative with their consumers who use ServiceNow.
    - [Remote tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-task-overview.md) -- Learn how you, as a provider, can resolve and fulfill multiple consumer tasks, such as incidents, cases, and service requests, by using remote tasks. Also as a consumer, you can assign the incidents to multiple providers for resolution.
      - [Transform framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-transform-about.md) -- Use the Transform Framework to integrate tasks between two ServiceNow instances to transform remote task data in the Service Exchange application.
    - [Journal field frameworks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-expolre-journal-field-framework.md) -- The Journal Field Framework (JFF) enables real-time synchronization of journal type fields, such as comments and work notes, between provider and consumer.
    - [Foundation data sync](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-explore-foundation-data-sync.md) -- Foundation data sync (FDS) enables structured, periodic data sharing from provider to consumer and consumer to provider instances. FDS ensures that both providers and consumers can share and receive accurate, up‑to‑date foundational data, supporting better service delivery and operational alignment.
    - [Magic links](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-explore-magic-link.md) -- Magic links enable seamless authentication from a consumer instance to a provider instance in Service Exchange, enabling consumers to access shared resources without manual login. This mechanism supports both per-user and single-user login modes and is particularly useful for HR tasks, catalog submissions, and knowledge base access.
    - [Flow action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-flow-action.md) -- Workflow Studio predefined actions help you preserve mapped variable integrity and maintain flow compatibility across configuration revisions.
    - [Instance scan checks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-scan-checks.md) -- Instance scan checks in Service Exchange proactively identify issues and system inconsistencies, helping administrators maintain system health and reduce downtime. The health dashboard displays findings, errors, and check statuses, helping you quickly identify and resolve problems.
    - [Service Exchange Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-se-center.md) -- Service Exchange center is a unified dashboard that consolidates connection health monitoring, issue resolution, and scan check management into a single interface.
  - [Service Exchange for Providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-providers-landing-page.md) -- Use the Service Exchange for Providers application to create and publish catalogs of services, receive, and fulfill requests generated from consumers, and establish integrations with consumer instances.
    - [Configure for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-configure-provider.md) -- To set up and configure the Service Exchange for Providers application, follow these steps.
      - [Install for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/install-service-bridge-v2-provider.md) -- If you have an admin role, you can install the Service Exchange for Providers (sn_sb_pro) application. The application includes the demo data and installations that are related to ServiceNow Store applications and plugins.
      - [Migrate from Service Exchange (legacy)](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-migrate.md) -- This section describes the process to migrate from the Service Exchange (legacy) version.
      - [Set up a provider record](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-new-provider.md) -- Set up a new provider record to establish a unique identifier for the Service Exchange for Providers (sn_sb_pro) application.
      - [User roles for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-personas.md) -- Learn about the roles, skills, and tasks for the different users in the Service Exchange for Providers application.
        - [Assign roles to groups](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-assign-roles.md) -- Assign roles to control the actions that are available for each user. In ServiceNow, you assign roles by group rather than by individual user. When the job descriptions of users change, their roles are automatically updated.
      - [Create catalog personas](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-catalog-persona.md) -- Create catalog user personas to control the catalog items that consumers can access on their instance.
      - [Create remote choice definitions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-remote-choice-fld-defs.md) -- As a provider, define remote choice fields that allow consumers to retrieve choice data from their instances in real time.
      - [Create remote catalogs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-catalog.md) -- As a provider, you can create remote catalogs to automate the task fulfillment process for your consumers.
        - [Create a remote record producer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-remote-rec-prod.md) -- Create remote record producers as part of creating a Remote Catalog in Service Exchange for Providers.
        - [Create variables for RRPs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-assign-variables-ser-defn.md) -- Create variables for a remote record producer (RRP) in Service Exchange for Providers application.
        - [Creating entitlements](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-entitlements.md) -- Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.
        - [Create a consumer criteria](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-consumer-criteria.md) -- Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.
        - [Using variable sets with RRP](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-variable-sets.md) -- Use single and multi-row variable sets with remote record producers.
        - [Create a variable set](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-variable-sets.md) -- Create variable sets for a remote record producer in Service Exchange for Providers application.
      - [Create a remote task definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-remote-tasks-defs.md) -- As a provider, create remote task definitions (RTD) that trigger the assignment of a remote task.
        - [Create a remote task using Workflow Studio](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-remote-task-flow-desig.md) -- As a provider, proactively create remote tasks for your customers by using Workflow Studio.
      - [Publish catalog items as RRPs](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-copy-catalog-as-rrp.md) -- As a provider, you can copy your local catalog items to Service Exchange as remote record producers (RRP) enabling you to avoid manual re-creation of catalog items as RRPs.
      - [Create catalog client scripts](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-client-script.md) -- As a provider, create catalog client scripts in Service Exchange to control the behavior of the catalog items when presented to your consumers.
      - [Create a transform](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-transform.md) -- As a provider or a consumer, create a transform in Service Exchange to integrate tasks between connected instances.
      - [Create configuration revisions](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-config-rev.md) -- As a provider, you can edit and create revisions of entitlements that contain updated functionality that can be developed and deployed to consumers.
      - [Configuring outbound FDS as providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-using-foundation-data-sync.md) -- As a provider, share foundational data with your consumer using foundation data sync (FDS).
        - [Create a FDS definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-fds-offering-definition.md) -- Create an foundation data sync (FDS) offering definition to inform your consumers about the data you’re ready to share.
        - [Acknowledge FDS offering request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-acknowledge-FDS-request.md) -- Acknowledge a foundation data sync (FDS) offering request and send a sample payload to help your consumer understand the type of data they’ll receive.
        - [Publish a foundation data subscription](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-publish-fds-subscription.md) -- Publish the foundation data sync (FDS) subscription to complete the foundation data sync after the consumer configures and accepts the subscription.
      - [Configure inbound FDS as providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-configure-inboun-fds-providers.md) -- As a provider, receive the foundation data from your provider using foundation data sync (FDS).
        - [Request FDS offerings from a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-request-fds-offering-consumers.md) -- Request a foundation data sync (FDS) offering from your consumer to receive foundational data.
        - [Validate a subscription item as a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-fds-validate-subs-items-provider.md) -- Configure the sample data received from the consumer to validate a foundation data sync (FDS) subscription item.
        - [Accept FDS subscription for provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-fds-accept-sups-provider.md) -- Accept a foundation data sync (FDS) subscription to complete the FDS configuration and begin receiving data from the consumer.
    - [Use for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-administer.md) -- As a provider, learn how to use Service Exchange to submit requests from the service catalog, and track order fulfillment from your ServiceNow instances.
      - [Register a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-onboarding.md) -- Registering a new consumer in Service Exchange establishes an instance-to-instance integration between a provider and a consumer.
        - [Off-board a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-offboard-consumer.md) -- Off-board an onboarded consumer and remove all related records.
      - [Fulfill a request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-proactive-customer-care-csp.md) -- Service Exchange Remote Catalog items are ordered from the consumer's ServiceNow instance, and they create provider tasks in each instance. The provider's agent fulfills these provider tasks in their ServiceNow instance. The data in these tasks is synchronized between instances so that they both can track the progress.
      - [Using the Scratchpad](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-scratchpad.md) -- The Scratchpad feature facilitates exchange of additional data between provider and consumer instances while performing Service Exchange tasks.
      - [Enable magic links](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-magic-links.md) -- Configure magic links to enable consumer users to access provider instance resources directly without manual authentication. Magic links streamline cross-instance navigation by automatically handling login credentials.
      - [Update settings for authorized users](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-configure-settings.md) -- As a provider, you can configure the settings for Authorized Users who have been created on the consumer's instance.
      - [Adding or creating scripts to a RRP](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-add-scripts-to-rrp.md) -- As a provider, you can perform more complex tasks and gain better control over catalog requests from consumers by using various scripts in a remote record producer (RRP). Consumers must approve all scripts to use the RRP.
      - [Reestablish connection for a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-cloning-instances.md) -- After you clone your instance, you must reestablish the connection between the provider and consumer instances.
      - [Execute a scan suite as a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-execute-scan-check.md) -- Execute a scan suite to identify issues in your instance and review the scan results.
        - [Modify the scan suite schedule as a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-execute-scan-check.md) -- Execute a scan suite to identify issues in your instance and review the scan results.
  - [Service Exchange for Consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-consumers-landing-page.md) -- Use the Service Exchange for Consumers application to seamlessly interact and collaborate with your providers.
    - [Configure for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-install.md) -- As a consumer, follow these steps to set up the Service Exchange for Consumers application in your own instance.
      - [Install for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/install-service-bridge-v2-customer.md) -- If you have an admin role, you can install the Service Exchange for Consumers application. The application includes demo data and installations that are related to ServiceNow Store applications and plugins.
      - [Personas for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-customer-roles.md) -- Learn about the different personas in the Service Exchange application.
        - [Assign roles to groups](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-assign-roles-customer.md) -- Assign roles to control the actions that are available for each user. In the Service Exchange for Consumers application, you assign roles by group rather than by the individual user so that when the job descriptions of users change, their roles are automatically updated.
      - [Connect to a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-register.md) -- Complete the registration process to establish a connection to the provider instance.
        - [Off-board a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-offboard-provider.md) -- Off-board a provider connection and delete all related records.
      - [Activate a remote task definition](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-activate-remote-task.md) -- As a consumer, activate the remote task definitions in your instance so that you can create remote tasks.
      - [Activate a remote record producer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-activate-entitlements.md) -- Activate entitlements to use a service or product that you have purchased.
      - [Add an authorized user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-auth-user.md) -- As a consumer, add new authorized users to control the access to catalog items that are entitled to you by your provider.
      - [Attach a consumer pre-flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-conf-consumer-flow.md) -- As a consumer, you can control when data should be synced between the provider tasks on the consumer and provider instances.
      - [Add consumer variables to an RRP](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-consumer-variables.md) -- As a consumer, you can add your own variables to a provider's remote record producer (RRP) in your consumer instance using a variable set. Consumer variables are useful in a Consumer Pre-Flow for adding additional information to complete a flow.
      - [Configure settings on the consumer instance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-configure-consumer-settings.md) -- As a consumer, you can configure and define default settings on your instance.
      - [Configuring inbound FDS as consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-using-foundation-data-sync-for-consumer.md) -- As a consumer, receive the foundation data from your provider using foundation data sync (FDS).
        - [Request FDS offerings](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-request-fds-offerings.md) -- Request a foundation data sync (FDS) offering from your provider to receive foundational data.
        - [Validate FDS subscription items](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-validate-fds-subscription.md) -- Configure the sample data received from the provider to validate a foundation data sync (FDS) subscription item.
        - [Accept an FDS subscription](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-accept-fds-subscription.md) -- Accept a foundation data sync (FDS) subscription to complete the FDS configuration.
        - [Import and export FDS configuration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/import-and-export-fds-configuration.md) -- Export ETL configurations for foundation data sync (FDS) from one instance to another using update sets.
      - [Configuring outbound FDS as consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/using-provider-bound-fds-consumer.md) -- As a consumer, share foundational data with your provider using foundation data sync (FDS).
        - [Create an offering definition for provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-create-provider-bound-fds-consumer.md) -- Create a foundation data sync (FDS) offering definition to inform your providers about the data you're ready to share.
        - [Acknowledge provider's FDS offering request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-con-acknowledge-fds-request.md) -- Acknowledge a foundation data sync (FDS) offering request and send a sample payload to help your provider understand the type of data they will receive.
        - [Publish FDS subscription for a provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-publish-con-fds-subscription.md) -- Publish the foundation data sync (FDS) subscription to complete the foundation data sync after the provider configures and accepts the subscription.
    - [Use for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-consumer-using.md) -- As a consumer, learn how to use Service Exchange to activate various entitlements to fulfill your requirements.
      - [Using the Scratchpad for tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-scratchpad-consumer.md) -- The Scratchpad feature facilitates exchange of data between provider and consumer instances while performing Service Exchange tasks.
      - [Execute a scan suite as a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-con-execute-scan-check.md) -- Execute a scan suite to identify issues in your instance and review the scan results.
        - [Modify the scan suite schedule as a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/se-con-execute-scan-check.md) -- Execute a scan suite to identify issues in your instance and review the scan results.
      - [Reestablish connection for a consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-cloning-instances-con.md) -- After you clone your instance, you must reestablish the connection between the consumer and provider instances.
      - [Create remote tasks to sync data](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-task-create.md) -- Remote tasks provide linked tasks across multiple instances and enable business workflows without any custom integrations.
        - [Connect and Disconnect remote tasks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-remote-task-connect-disconnect.md) -- Remote tasks associated with active remote task definitions enable you to sync data between two parent tasks on the provider and consumer instances.
  - [Integrate](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-omt-intg.md) -- Providers can use Service Exchange to publish their product offers to a consumer using a Service Exchange Remote Record Producer.
  - [Reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-reference.md) -- Reference topics provide additional information about the Service Exchange data model and configuration.
    - [Components installed for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-installed-components-provider.md) -- Several types of components are installed when you activate the Service Exchange for Providers application, including tables, user roles, and business rules.
    - [Components installed for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-installed-components-customer.md) -- Several types of components are installed with activation of the Service Exchange for Consumers application including tables, user roles, and business rules.
    - [Data model](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-data-model.md) -- The Service Exchange applications data model provides insight into how the tables that are used in Service Exchange relate to each other.
      - [Data model for providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-datamodel-provider.md) -- The Service Exchange for Providers data model provides insight into how the tables that are used in the Service Exchange for Providers application relate to each other.
      - [Data model for consumers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-datamodel-customers.md) -- The Service Exchange for Consumers data model provides insight into how the tables that are used in the Service Exchange for Consumers application relate to each other.
    - [Domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-domain-separation.md) -- Domain separation is supported for Service Exchange. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
    - [Error log](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-error-log.md) -- Track errors on recent transactions, provide connection status, run health checks, and provide recommendations.
    - [Preservers and exclusions tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-cloning.md) -- When installing Service Exchange, certain tables must be preserved or excluded to maintain connectivity after a clone.
    - [List of scan checks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-list-of-scan-checks-in-sb.md) -- Multiple scan checks are available in Service Exchange to help you identify issues and system inconsistencies, enabling you to maintain system health and reduce downtime.
    - [Glossary](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [A](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [application scope](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [attachment sync](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [authorized user](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [B](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [bi-directional integration](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [C](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [consumer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [consumer application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [consumer criteria](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [configuration revision](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [D](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [E](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [entitlement](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [F](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [flow action](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [foundation data sync](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [H](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [health dashboard](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [I](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [instance scan checks](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [J](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [Journal Field Framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [K](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [L](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [M](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [magic link](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [N](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [P](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [Partner](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [persona](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [proactive case](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [provider](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [provider application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [provider task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [R](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [registration task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [remote catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [remote record producer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [remote task](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [S](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [scratchpad](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [Service Exchange](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [T](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [transform framework](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
      - [V](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [variable](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
        - [variable set](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-glossary-sb.md) -- A list of terms used in Service Exchange.
    - [Consumer criteria new record form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-consumer-criteria-new-record-form.md) -- Field descriptions for the consumer criteria new record form contains information on consumer criteria new record form field values.
    - [Catalog client script new record form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/service-exchange/service-bridge-v2-cat-script-fd.dita.md) -- Field descriptions for the catalog client script new record form contains information on catalog client script form field values.

```


### File: service-exchange\install-service-bridge-v2-customer.md

```text
---
title: Install Service Exchange for Consumers
description: If you have an admin role, you can install the Service Exchange for Consumers application. The application includes demo data and installations that are related to ServiceNow Store applications and plugins.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Install Service Exchange for Consumers

If you have an admin role, you can install the Service Exchange for Consumers application. The application includes demo data and installations that are related to ServiceNow® Store applications and plugins.

## Before you begin

-   Ensure that the application and all of its associated ServiceNow Store applications have valid ServiceNow entitlements. For more information, see [Get entitlement for a ServiceNow product or application](https://store.servicenow.com/$appstore.do#!/store/help?article=KB0030186).

Role required: admin

## About this task

The following plugins are installed with the Service Exchange for Consumers application:

-   sn\_sb
-   sn\_sb\_rps
-   sn\_transport
-   com.glide.hub.process.sync
-   com.snc.ihub\_spoke\_util\_pack

Apart from these, several components including roles, business rules, tables, and flows are also installed. For more information about the components that are installed with this application, see [Components installed with Service Exchange for Consumers](../reference/service-bridge-v2-installed-components-customer.md).

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Service Exchange for Consumers application by using the filter criteria and search bar.

    You can search for the application by its name or ID. If you can't find the application, you might have to request it from the ServiceNow Store.

    Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) to view all the available apps, and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

3.  If demo data is available and you want to install it, click **Load demo data**.

    Demo data comprises sample records that describe the application features for common use cases. Load demo data when you first install the application on a development or test instance.

    **Important:** If you don't load the demo data during installation, it's unavailable to load later.

4.  Select **Install**.



```


### File: service-exchange\install-service-bridge-v2-provider.md

```text
---
title: Install Service Exchange for Providers
description: If you have an admin role, you can install the Service Exchange for Providers \(sn\_sb\_pro\) application. The application includes the demo data and installations that are related to ServiceNow Store applications and plugins.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Install Service Exchange for Providers

If you have an admin role, you can install the Service Exchange for Providers \(sn\_sb\_pro\) application. The application includes the demo data and installations that are related to ServiceNow® Store applications and plugins.

## Before you begin

-   Ensure that the application and all of its associated ServiceNow Store applications have valid ServiceNow entitlements. For more information, see [Get entitlement for a ServiceNow product or application](https://store.servicenow.com/$appstore.do#!/store/help?article=KB0030186).

Role required: admin

## About this task

The following plugins are automatically installed with the Service Exchange for Providers application:

-   sn\_req\_criteria
-   sn\_sb
-   sn\_sb\_rps
-   sn\_transport
-   com.glide.hub.process.sync
-   com.snc.ihub\_spoke\_util\_pack

Apart from these, several components including roles, business rules, tables, and flows are also installed. For more information about the components that are installed with this application, see [Components installed with Service Exchange for Providers](../reference/service-bridge-v2-installed-components-provider.md).

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Service Exchange for Providers application \(sn\_sb\_pro\) by using the filter criteria and search bar.

    You can search for the application by its name or ID. If you can't find the application, you might have to request it from the ServiceNow Store.

    Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) to view all the available apps, and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

3.  In the application installation dialog, review the application dependencies.

    This listing indicates, for each dependent plugin and application if it's being installed, is already installed, or must be installed. If any plugins or applications must be installed, you must install them before you can install Service Exchange for Providers.

4.  If demo data is available and you want to install it, click **Load demo data**.

    Demo data contains the sample records that describe the application features for common use cases. Load demo data when you first install the application on a development or test instance. If you don't load the demo data during installation, it's unavailable to load later.

5.  Select **Install**.



```


### File: service-exchange\se-con-execute-scan-check.md

```text
---
title: Execute a scan suite as a consumer
description: Execute a scan suite to identify issues in your instance and review the scan results.Modify the scan suite schedule to change when a scan suite runs automatically in your consumer instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for consumers, Service Exchange for Consumers, Service Exchange]
---

# Execute a scan suite as a consumer

Execute a scan suite to identify issues in your instance and review the scan results.

## Before you begin

Role required: admin \(sb\_admin\)

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Administration** &gt; **Consumer Center**.

2.  Select the **Scan suite** tab.

3.  Select one or more scan suites to execute.

    You can select multiple scan suites based on your requirements. Use the filter builder to filter scan results based on specific criteria.

4.  Select **Execute scan suite**.

    The system runs the selected scan suites and displays the results. If no issues are found, the message "Scan complete with no issues" appears. If issues are found, a banner displays the number of issues.

5.  If issues are found, click Go to issues to view the complete list of issues.

    You see all identified issues categorized by priority: high, medium, and low. You can click an individual issue to view resolution details.


## Modify the scan suite schedule as a consumer

Modify the scan suite schedule to change when a scan suite runs automatically in your consumer instance.

### Before you begin

Role required: admin \(sb\_admin\)

### Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Consumer Center**.

2.  From the **Scan suite** tab, select the scan suite you want to modify.

3.  Select **Modify Schedule**.

4.  Update the schedule timing as needed, and select **Modify**.


**Related topics**  


[Service Exchange Center](../concept/se-se-center.md)


```


### File: service-exchange\se-consumer-using.md

```text
---
title: Use for consumers
description: As a consumer, learn how to use Service Exchange to activate various entitlements to fulfill your requirements.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange for Consumers, Service Exchange]
---

# Use for consumers

As a consumer, learn how to use Service Exchange to activate various entitlements to fulfill your requirements.


```


### File: service-exchange\se-execute-scan-check.md

```text
---
title: Execute a scan suite as a provider
description: Execute a scan suite to identify issues in your instance and review the scan results.Modify the scan suite schedule to change when a scan suite runs automatically in your instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Execute a scan suite as a provider

Execute a scan suite to identify issues in your instance and review the scan results.

## Before you begin

Role required: admin \(sb\_admin\)

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Provider Center**.

2.  Select the **Scan suite** tab.

3.  Select one or more scan suites to execute.

    You can select multiple scan suites based on your requirements. Use the filter builder to filter scan results based on specific criteria.

4.  Select **Execute scan suite**.

    The system runs the selected scan suites and displays the results. If no issues are found, the message "Scan complete with no issues" appears. If issues are found, a banner displays the number of issues.

5.  If issues are found, click Go to issues to view the complete list of issues.

    You see all identified issues categorized by priority: high, medium, and low. You can click an individual issue to view resolution details.


**Parent Topic:**[Using Service Exchange for providers](../concept/service-bridge-v2-administer.md)

## Modify the scan suite schedule as a provider

Modify the scan suite schedule to change when a scan suite runs automatically in your instance.

### Before you begin

Role required: admin \(sb\_admin\)

### Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Provider Center**.

2.  From the **Scan suite** tab, select the scan suite you want to modify.

3.  Select **Modify Schedule**.

4.  Update the schedule timing as needed, and select **Modify**.


**Related topics**  


[Service Exchange Center](../concept/se-se-center.md)


```


### File: service-exchange\se-se-center.md

```text
---
title: Service Exchange Center
description: Service Exchange center is a unified dashboard that consolidates connection health monitoring, issue resolution, and scan check management into a single interface.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Explore, Service Exchange]
---

# Service Exchange Center

Service Exchange center is a unified dashboard that consolidates connection health monitoring, issue resolution, and scan check management into a single interface.

Service Exchange Center provides administrators with a centralized location to monitor Service Exchange connections, track instance performance, and identify critical issues generated from scan suites.

## Role requirements

The Service Exchange Admin \(sb\_admin\) role is required to access the Service Exchange Center.

## How to access

The Service Exchange Center is accessible from the Administration menu under either the **Provider Center** or **Consumer Center** modules in the application menu, depending on your instance role. The dashboard displays data relevant to your entry point, with the option to switch between provider and consumer views when your instance supports both roles.

## Benefits

-   Quick visibility into connection health status.
-   Reduced downtime and troubleshooting efforts through early issue identification.
-   Known errors with detailed solutions for faster resolution.
-   Improved productivity through automation and visibility.
-   Consolidated health monitoring, connection management, and scan checks in one location.

## Service Exchange health

Service Exchange health dashboard is the part of Service Exchange Center and provides unified views of connection health. It also consolidates functionality that was previously available across multiple interfaces, including the Health Dashboard, and scan checks. Service Exchange Health includes the following tabs and elements:

![View of Service Exchange Health dashboard with four callouts highlighted. For descriptions of the numbered callouts, refer to the table that follows.](../image/se-health-dashboard.png)

|Feature|Description|
|-------|-----------|
|1. Tabs|Service Exchange Health dashboard contains three tabs: Resolution center, Connection health, and Scan suites.|
|2. Overview|The overview section shows a high-level summary of the connections.|
|3. Issue|The issue section lists all issues found during scan checks.|
|4. Provider/Consumer drop-down menu|The Provider/Consumer drop-down menu enables switching between provider and consumer views when the instance supports both roles.|

-   **Resolution center**

    The Resolution Center is the default landing page that provides an at-a-glance view of integration health. This tab contains the following components:

    -   **Connection Summary**

        Displays the overall health score calculated from connection statuses \(Up, Down, or Slow\), the down connections count indicates connections requiring attention. A donut chart visualizes the distribution of connection states.

    -   **Issue Distribution**

        A bar chart that categorizes issues by severity \(critical, high, moderate, low\) from scan checks.

    -   **Issues List**

        A comprehensive table listing all detected unresolved issues generated from scan checks and the Service Exchange Error table, with columns for issue summary, associated connection, count, assigned user, and other information.

        Selecting an issue summary, shows details about the issue, known errors include resolution steps and guidance. The issue dialog includes options to mute, assign, or follow the issue, and a **Validate &amp; Resolve** button to revalidate the issue status and resolve if no longer applicable. You can select the Navigate to Issue Report icon ![](../image/icon-se-center-Issue-report.svg) next to **Validate &amp; Resolve** button to get more details about the issue.

        Post comments or work notes using the Activity tab.

-   **Connection health**

    The Connection heath tab displays a list of connections grouped by their status, down, slow, or up. It also provides detailed information for each Service Exchange connection through individual connection cards. Each card contains:

    -   Connection name and status \(color-coded: green for Up, red for Down, purple for Slow\)
    -   Outbound and inbound status indicators
    -   Payload statistics \(sent and received\)
    -   App version
    -   Connection creation date
    -   Related issues associated with the connection
    You can also search, sort, and filter connections based on name, number, status, and so on.

-   **Scan suites**

    The Scan Suites tab provides access to automated health checks that detect issues and inconsistencies. To learn more about instance scan checks, see [Instance scan checks](service-bridge-v2-scan-checks.md).

    Scan suites are organized into two categories:

    -   **On-demand suites**

        Suites that are available for manual execution as needed. On-demand suites include suites for post-clone, pre-onboarding, post-upgrade, and post-onboarding scenarios.

    -   **Scheduled suites**

        Suites that run automatically at configured times.

    Each scan suite contains multiple scan checks. When you select a scan suite, you can view all scan checks included in that suite.

    Scan results appear as issues. Each issue is assigned a priority level: critical, high, medium, or low, based on its severity. You can run any scan suite as needed using **Execute scan suite** button.

-   **Provider/Consumer drop-down menu**

    Provides options for switching between provider and consumer views when the instance supports both roles.


**Related topics**  


[Execute a scan suite as a provider](../task/se-execute-scan-check.md#)

[Execute a scan suite as a consumer](../task/se-con-execute-scan-check.md#)


```


### File: service-exchange\service-bridge-consumers-landing-page.md

```text
---
title: Service Exchange for Consumers
description: Use the Service Exchange for Consumers application to seamlessly interact and collaborate with your providers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange]
---

# Service Exchange for Consumers

Use the Service Exchange for Consumers application to seamlessly interact and collaborate with your providers.

## Service Exchange Overview

As a consumer, you can:

-   Review remote catalog items entitled to you from your local catalog and send requests to your provider for fulfillment.
-   Bidirectionally integrate your tasks with your provider's tasks.
-   Receive proactive tasks from providers for transparency and collaboration.

<table id="table_k52_dyx_yxb" class="nav-card"><tbody><tr><td>

[Configure for consumers![](../image/bus-optimize-manage-sb.svg)Learn how to install and configure Service Exchange for consumers.](service-bridge-v2-install.md)

</td><td>

[User for consumers![](../../../reuse/icons/brand-icons/bus-try-a-demo.svg)Learn how to use Service Exchange for consumers.](se-consumer-using.md)

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-providers-landing-page.md

```text
---
title: Service Exchange for Providers
description: Use the Service Exchange for Providers application to create and publish catalogs of services, receive, and fulfill requests generated from consumers, and establish integrations with consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange]
---

# Service Exchange for Providers

Use the Service Exchange for Providers application to create and publish catalogs of services, receive, and fulfill requests generated from consumers, and establish integrations with consumer instances.

## Service Exchange Overview

As a provider, you can:

-   Create and publish remote service catalogs for your consumers on their instances.
-   Integrate your instance with your consumer's instance.
-   Receive and fulfill service requests on your instance from your consumer's ServiceNow instance.

<table id="table_k52_dyx_yxb" class="nav-card"><tbody><tr><td>

[Configure for providers![](../image/bus-optimize-manage-sb.svg)Learn how to install and configure Service Exchange for providers.](service-bridge-v2-configure-provider.md)

</td><td>

[User for providers![](../../../reuse/icons/brand-icons/bus-try-a-demo.svg)Learn how to use Service Exchange for providers.](service-bridge-v2-administer.md)

</td></tr></tbody>
</table>If you’re a consumer, see [Service Exchange for Consumers](service-bridge-consumers-landing-page.md).

**Related topics**  


[Service Exchange for Consumers](service-bridge-consumers-landing-page.md)


```


### File: service-exchange\service-bridge-v2-accept-fds-subscription.md

```text
---
title: Accept a foundation data sync subscription
description: Accept a foundation data sync \(FDS\) subscription to complete the FDS configuration.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring inbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Accept a foundation data sync subscription

Accept a foundation data sync \(FDS\) subscription to complete the FDS configuration.

## Before you begin

Role required: admin

## About this task

After the subscription item is validated, you must accept the subscription to complete the FDS configuration.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Open Records** &gt; **FDS Requests**.

2.  Select the request.

3.  From the Foundation Data Consumer Subscriptions related list, open the consumer subscription by selecting the record number in the **Number** column.

4.  Select **Accept**.

    If you reject the subscription by selecting **Reject**, your provider needs to resend the sample files, and you must reconfigure the subscription items before you can accept the subscription again.



```


### File: service-exchange\service-bridge-v2-acknowledge-FDS-request.md

```text
---
title: Acknowledge foundation data sync offering request
description: Acknowledge a foundation data sync \(FDS\) offering request and send a sample payload to help your consumer understand the type of data they’ll receive.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring outbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Acknowledge foundation data sync offering request

Acknowledge a foundation data sync \(FDS\) offering request and send a sample payload to help your consumer understand the type of data they’ll receive.

## Before you begin

Role required: admin

## About this task

After a consumer requests an FDS offering, the system generates an FDS request and corresponding FDS subscriptions in your Service Exchange instance.

If **Auto acknowledge FDS Requests** option isn't selected, you must manually acknowledge the consumer's FDS request to inform them that you’re working on the request. Then, send a sample payload to help them understand the type of data they’ll receive.

Also, when a consumer requests an FDS offering, you receive an email notification about the new request, including any required actions.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Open Records** &gt; **FDS Request**.

2.  Open the provider offering request by selecting the record number in the Number column.

3.  Select the **Acknowledge** button.

    The request state changes from Received to Work In Progress.

4.  Send a sample payload for each subscription.

    Each sample payload contains up to five records of sample data.

    1.  From the Foundation Data Provider Subscription related list, open the subscription by selecting the record number in the Number column.

    2.  Select the **Send Sample** button.

        The sample payload sent to your customer is listed under the **Sample Payload** column in the Subscription Items related list.


## Result

A sample payload for each subscription is sent to the consumer as sample data. Consumers can review the sample to verify the data structure and content before accepting the full data synchronization.

## What to do next

[Publish a foundation data subscription](service-bridge-v2-publish-fds-subscription.md).


```


### File: service-exchange\service-bridge-v2-activate-entitlements.md

```text
---
title: Activate a remote record producer in Service Exchange
description: Activate entitlements to use a service or product that you have purchased.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Activate a remote record producer in Service Exchange

Activate entitlements to use a service or product that you have purchased.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  Select the Number column to navigate to the Provider connection record.

    The list of entitlements available is displayed.

3.  Select the Remote record producers related list and select a remote record producer that you want to activate.

4.  In the Remote record producer page, select **Activate** to activate the entitlement.

    If the remote record producer contains scripts, the scripts get automatically approved when you select **Activate**.

5.  Approve scripts individually from the **Remote Script Approvals** tab.

    1.  In the Approved column, change the script status to true.

    You must approve all the scripts to activate the remote record producer. If you don't approve all the scripts, you can't activate the remote record producer.



```


### File: service-exchange\service-bridge-v2-activate-remote-task.md

```text
---
title: Activate a remote task definition record in Service Exchange
description: As a consumer, activate the remote task definitions in your instance so that you can create remote tasks.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Activate a remote task definition record in Service Exchange

As a consumer, activate the remote task definitions in your instance so that you can create remote tasks.

## Before you begin

Before you can activate a remote task definition \(RTD\) in your ServiceNow instance, your provider must create an RTD first in their ServiceNow instance. For more information, see [Create a remote task definition in Service Exchange for Providers](service-bridge-v2-create-remote-tasks-defs.md).

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  Select the Number column to navigate to the Provider connection record.

3.  Select the Remote task definition related list, and select an RTD to you want to activate.

4.  On the remote task definition form, review the Simple Trigger section on the form.

    If you set a simple trigger that matches a task record update, a remote task is automatically created for the task record.

5.  On the **Inbound fields** related tab, review the variables data.

    The provider defines these inbound fields. When you create a remote task, your provider receives the remote task data through these inbound fields. You can modify the **Field label**, **Sync when**, and **Target field** fields.

6.  On the **Outbound fields** related tab, perform the following actions.

    1.  Review the variables data.

        Your provider defines these outbound fields. When the provider responds to your remote task, you receive the remote task data through these outbound fields. You can only modify the **Source field** on these records.

    2.  Select the **Sync pre-existing entries** option to enable synchronization of all existing comments to the target task when a connection is established.

        If enabled, any comments made prior to the connection gets included in the sync process when a remote task is created.

        **Note:** This feature is only available for Service Exchange version 2.2.x.

7.  On the **Remote task variables** related tab, review the variables data.

    The remote task variables are created from your inbound fields to be displayed on the remote tasks form.

8.  Select **Activate**.

9.  Verify the mappings of the inbound and outbound variables and select **OK**.

    The pop-up window enables you to verify the inbound and outbound mappings.



```


### File: service-exchange\service-bridge-v2-add-scripts-to-rrp.md

```text
---
title: Adding or creating scripts to a remote record producer
description: As a provider, you can perform more complex tasks and gain better control over catalog requests from consumers by using various scripts in a remote record producer \(RRP\). Consumers must approve all scripts to use the RRP.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Adding or creating scripts to a remote record producer

As a provider, you can perform more complex tasks and gain better control over catalog requests from consumers by using various scripts in a remote record producer \(RRP\). Consumers must approve all scripts to use the RRP.

In Service Exchange, you can apply scripts to an RRP by:

-   Creating catalog client scripts: You can create catalog item scripts to customize an RRP. For details, see [Create catalog client scripts](../task/service-bridge-v2-create-client-script.md).
-   Adding scripts in variables: You can add scripts in a variable and use the variable in the RRP. For details see [Create variables for remote record producers in Service Exchange for Providers](../task/service-bridge-v2-assign-variables-ser-defn.md).
-   Adding scripts in UI policies: You can add scripts in a UI policy and apply the UI policy on an RRP. For details, see [Service catalog UI policy](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/c_ServiceCatalogUIPolicy.md).

**Parent Topic:**[Using Service Exchange for providers](service-bridge-v2-administer.md)


```


### File: service-exchange\service-bridge-v2-administer.md

```text
---
title: Using Service Exchange for providers
description: As a provider, learn how to use Service Exchange to submit requests from the service catalog, and track order fulfillment from your ServiceNow instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange for Providers, Service Exchange]
---

# Using Service Exchange for providers

As a provider, learn how to use Service Exchange to submit requests from the service catalog, and track order fulfillment from your ServiceNow® instances.

-   **[Register a Service Exchange consumer](../task/service-bridge-v2-onboarding.md)**  
Registering a new consumer in Service Exchange establishes an instance-to-instance integration between a provider and a consumer.
-   **[Fulfill a consumer request](service-bridge-v2-proactive-customer-care-csp.md)**  
Service Exchange Remote Catalog items are ordered from the consumer's ServiceNow instance, and they create provider tasks in each instance. The provider's agent fulfills these provider tasks in their ServiceNow instance. The data in these tasks is synchronized between instances so that they both can track the progress.
-   **[Using the Scratchpad for Service Exchange tasks](service-bridge-v2-scratchpad.md)**  
The Scratchpad feature facilitates exchange of additional data between provider and consumer instances while performing Service Exchange tasks.
-   **[Enable magic links](../task/service-bridge-v2-magic-links.md)**  
Configure magic links to enable consumer users to access provider instance resources directly without manual authentication. Magic links streamline cross-instance navigation by automatically handling login credentials.
-   **[Update settings for authorized users](../task/service-bridge-v2-configure-settings.md)**  
As a provider, you can configure the settings for Authorized Users who have been created on the consumer's instance.
-   **[Adding or creating scripts to a remote record producer](service-bridge-v2-add-scripts-to-rrp.md)**  
As a provider, you can perform more complex tasks and gain better control over catalog requests from consumers by using various scripts in a remote record producer \(RRP\). Consumers must approve all scripts to use the RRP.
-   **[Reestablish connection after a clone for a provider](../task/service-bridge-v2-cloning-instances.md)**  
After you clone your instance, you must reestablish the connection between the provider and consumer instances.
-   **[Execute a scan suite as a provider](../task/se-execute-scan-check.md#)**  
Execute a scan suite to identify issues in your instance and review the scan results.


```


### File: service-exchange\service-bridge-v2-assign-roles-customer.md

```text
---
title: Assign roles to groups for Service Exchange
description: Assign roles to control the actions that are available for each user. In the Service Exchange for Consumers application, you assign roles by group rather than by the individual user so that when the job descriptions of users change, their roles are automatically updated.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Personas for consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Assign roles to groups for Service Exchange

Assign roles to control the actions that are available for each user. In the Service Exchange for Consumers application, you assign roles by group rather than by the individual user so that when the job descriptions of users change, their roles are automatically updated.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Click the group that you want to assign the role to.

3.  In the Roles related list, click **Edit**.

4.  Add the desired roles to the group.

5.  Click **Save**.



```


### File: service-exchange\service-bridge-v2-assign-roles.md

```text
---
title: Assign roles to groups for Service Exchange
description: Assign roles to control the actions that are available for each user. In ServiceNow, you assign roles by group rather than by individual user. When the job descriptions of users change, their roles are automatically updated.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [User roles for providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Assign roles to groups for Service Exchange

Assign roles to control the actions that are available for each user. In ServiceNow, you assign roles by group rather than by individual user. When the job descriptions of users change, their roles are automatically updated.

## Before you begin

Role required: admin

## About this task

A user role is a preconfigured role in the application consisting of multiple granular roles. The user roles are designed to correspond to the common job titles for managers, analysts, and service owners in an IT organization. For more details, see [User roles for providers](../concept/service-bridge-v2-personas.md).

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Groups**.

2.  Select the group that you want to assign the role to.

3.  In the Roles related list, select **Edit**.

4.  Add the roles to the group.

5.  Select **Save**.



```


### File: service-exchange\service-bridge-v2-assign-variables-ser-defn.md

```text
---
title: Create variables for remote record producers in Service Exchange for Providers
description: Create variables for a remote record producer \(RRP\) in Service Exchange for Providers application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create variables for remote record producers in Service Exchange for Providers

Create variables for a remote record producer \(RRP\) in Service Exchange for Providers application.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Catalog Items**.

2.  Click a record producer that you want to create variables for.

3.  Click the **Variables** tab in the Related List and then click **New**.

4.  On the form, fill in the fields.

<table id="table_brn_vgs_jmb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Type

</td><td>

Supported variable types are as follows: -   Attachment
-   Break
-   CheckBox
-   Container End
-   Container Split
-   Container Start
-   Date
-   Date/Time
-   Duration
-   Email
-   HTML
-   IP Address
-   Label
-   List Collector
-   Lookup Multiple Choice
-   Lookup Select Box
-   Masked
-   Multiline text
-   Multiple Choice
-   Numeric Scale
-   Reference
-   Requested For
-   Rich Text Label
-   Select Box
-   Single Line Text
-   URL
-   Wide Single LineText
-   Yes/No
If you use unsupported variables, Service Exchange might not integrate the data in the right format.

</td></tr><tr><td>

Catalog item

</td><td>

Catalog item that uses the variable.

</td></tr><tr><td>

Application

</td><td>

This is a read only field and is set by default based on the application scope.

</td></tr><tr><td>

Mandatory

</td><td>

Option for making the variable mandatory as part of the ordering process.**Note:** This behavior is applicable only on a page load. You can change it by using client APIs.

</td></tr><tr><td>

Active

</td><td>

This is a read only field and is enabled based on the **Publish**, **Retire**, or **Edit** actions.

</td></tr><tr><td>

Order

</td><td>

Placement order of the variable on the catalog item page. You organize the variables from top to bottom, and from the least to the greatest order value. For example, a variable with an order value of 1 is placed ahead of other variables with higher-order values.

</td></tr><tr><td>

Question

</td><td>

Question that you can ask users who are ordering the catalog item to obtain related information.

</td></tr><tr><td>

Name

</td><td>

Name to identify the question.**Note:** If this field is empty, its value is auto-populated based on the **Question** field for all variable types except Break, Container Split, and Container End.

</td></tr><tr><td>

Tooltip

</td><td>

Tooltip text to display when users point to the variable. Enter a brief note to describe the purpose of the question.

</td></tr><tr><td>

Example Text

</td><td>

Question field hint that appears before a user enters a value.You can use a hint for the following variables:

-   IP Address
-   Email
-   URL
-   Single Line Text
-   Wide Single Line Text
-   Multiline Text
-   Date
-   Date/Time


</td></tr><tr><td>

Type Specification

</td><td>

Values specific to the type of variables.You can add scripts by selecting **Use reference qualifier condition** as **Advanced**.

</td></tr></tbody>
</table>5.  Add scripts in the variable.

    1.  On the Variable form, in the **Type** drop-down menu, select **Reference**.

    2.  In the **Type Specifications** tab, select the **Use reference qualifier** as **Advanced**.

    3.  In the **Reference qualifier** text field, add your scripts.

6.  Click **Submit**.

    Repeat the process to create additional variables for the same remote record producer.



```


### File: service-exchange\service-bridge-v2-auth-users.md

```text
---
title: Service Exchange authorized users and personas
description: The Authorized Users feature enables a provider to categorize remote catalog items by user personas so that only authorized users with these personas can access the catalog items. It also allows consumer admins to associate these personas to users in their instances to allow access.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Remote catalogs, Explore, Service Exchange]
---

# Service Exchange authorized users and personas

The Authorized Users feature enables a provider to categorize remote catalog items by user personas so that only authorized users with these personas can access the catalog items. It also allows consumer admins to associate these personas to users in their instances to allow access.

When a provider and a consumer initially register the Service Exchange application, the active contacts on the consumer's account in the provider's ServiceNow instance are automatically added to the Authorized Users table and synced with the consumer's ServiceNow instance.

Enables the provider to subdivide services by user personas giving the consumers an easy way to define access in their instance to the provider’s services. By using the Authorized Users feature, you can identify the specific users between the provider and consumer instances to manage the consumer requests for the provider's services. You can then assign personas to the authorized users so that you can control the access to remote catalog items.

-   Both providers and consumers can create Authorized Users.
-   The providers manage the approval state for an Authorized User. By default, the approval state is set **Approved**.
-   Consumers manage the active state for an Authorized User.
-   Providers can set the maximum number of authorized users for each connection. This requires all consumers to maintain a list of active authorized users of less than or equal to the limit set by the provider. If the value is not set, consumers can have as many active authorized users as they want.

To learn more, see [Add an authorized user](../task/service-bridge-v2-create-auth-user.md).


```


### File: service-exchange\service-bridge-v2-cat-script-fd.dita.md

```text
---
title: Catalog client script new record form
description: Field descriptions for the catalog client script new record form contains information on catalog client script form field values.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Service Exchange]
---

# Catalog client script new record form

Field descriptions for the catalog client script new record form contains information on catalog client script form field values.

|Field|Description|
|-----|-----------|
|Name|Name of the script.|
|Applies to|The item type to which the script applies.|
|Active|Option to make the script active.|
|UI type|The UI type where you want to apply the script.|
|Application|This field is automatically set to the default application based on the application scope.|
|Type|When the script runs, such as onLoad, onChange.|
|Catalog item|Name of the catalog item to apply the script.|
|Applies on a Catalog Item view|Option to apply the catalog client script to catalog items displayed within the order screen on the service catalog.|
|Applies on Target Record|Option to apply the catalog client script on a record created for task-extended tables via record producers.|
|Script|The script content.|


```


### File: service-exchange\service-bridge-v2-cloning-instances-con.md

```text
---
title: Reestablish connection after a clone for a consumer
description: After you clone your instance, you must reestablish the connection between the consumer and provider instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for consumers, Service Exchange for Consumers, Service Exchange]
---

# Reestablish connection after a clone for a consumer

After you clone your instance, you must reestablish the connection between the consumer and provider instances.

## Before you begin

Role required: admin

The clone must be completed. For more information on cloning, see [Instance Clone](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/system-clone-landing.md).

## About this task

After you clone your Service Exchange, the inbound and outbound connections move to an error or down state. You must reestablish the connection between provider and consumer target instances to promote proper functionality.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

    You see the Inbound and Outbound fields are in an error state.

2.  Open the Provider connection record by selecting the record number in the Number column.

3.  From the related list, select **RPS connections** &gt; **Provider Instance**.

4.  In the Process Sync Remote System Provider Instance page, select the **Validate and Activate Remote System** related links.

5.  Activate inactive Capture Definitions.

    1.  Navigate to **All** &gt; **IntegrationHub** &gt; **Remote Process Sync** &gt; **Process Sync Definitions**.

    2.  Select the Service Exchange Customer Definition.

    3.  Select the Capture Definitions related list, change the state of all inactive capture definition to **Active**.


**Related topics**  


[Reestablish connection after a clone for a provider](service-bridge-v2-cloning-instances.md)

[List of preservers and exclusions tables for cloning](../reference/service-bridge-v2-cloning.md)


```


### File: service-exchange\service-bridge-v2-cloning-instances.md

```text
---
title: Reestablish connection after a clone for a provider
description: After you clone your instance, you must reestablish the connection between the provider and consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Reestablish connection after a clone for a provider

After you clone your instance, you must reestablish the connection between the provider and consumer instances.

## Before you begin

Role required: admin

The clone must be completed. For more information on cloning, see [Instance Clone](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/system-clone-landing.md).

## About this task

After you clone your Service Exchange, the inbound and outbound connections move to an error or down state. You must reestablish the connection between provider and consumer target instances to promote proper functionality.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Consumer**.

    You see the Inbound and Outbound fields for the cloned consumer are in an error state.

2.  Open the Consumer connection record by selecting the record number in the Number column.

3.  From the related list, select **RPS connections** &gt; **Consumer Instance**.

4.  In the Process Sync Remote System Consumer Instance page, select the **Validate and Activate Remote System** related links.

5.  Activate inactive Capture Definitions.

    1.  Navigate to **All** &gt; **IntegrationHub** &gt; **Remote Process Sync** &gt; **Process Sync Definitions**.

    2.  Select the Service Exchange Provider Definition.

    3.  Select the Capture Definitions related list, change the state of all inactive capture definition to **Active**.


## Result

The state of the Outbound and the Inbound fields changes to **Active**.

**Parent Topic:**[Using Service Exchange for providers](../concept/service-bridge-v2-administer.md)

**Related topics**  


[Reestablish connection after a clone for a consumer](service-bridge-v2-cloning-instances-con.md)

[List of preservers and exclusions tables for cloning](../reference/service-bridge-v2-cloning.md)


```


### File: service-exchange\service-bridge-v2-cloning.md

```text
---
title: List of preservers and exclusions tables for cloning
description: When installing Service Exchange, certain tables must be preserved or excluded to maintain connectivity after a clone.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Reference, Service Exchange]
---

# List of preservers and exclusions tables for cloning

When installing Service Exchange, certain tables must be preserved or excluded to maintain connectivity after a clone.

If the default system profile is used, some of the Service Exchange table data isn’t preserved. To address this issue, you must create a custom clone profile with specific settings required for Service Exchange. Navigate to **All** &gt; **System Clone** &gt; **Clone Profiles** and select **New** to create a custom profile. For more details on clone profiles, see [Create a custom clone profile](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/configure-clone-profile.md). In this profile, you must:

-   Remove the **Remote Process Sync Disable Records** script from the Cleanup scripts related list,
-   Validate if the following Service Exchange tables are included in the custom profile.

**Note:** After a clone, you must reestablish the connection and activate the Capture Definitions. See [Reestablish connection after a clone for a provider](../task/service-bridge-v2-cloning-instances.md) and [Reestablish connection after a clone for a consumer](../task/service-bridge-v2-cloning-instances-con.md).

## Service Exchange tables to preserve and exclude

The following scenarios describe how clone operations affect table data based on table configuration in the preservers and the exclusions tables list.

|Preservers tables|Exclusions tables|Result on target instance|
|-----------------|-----------------|-------------------------|
|Included|Included|Target table retains existing data. The system preserves existing records and copies no records from the source.|
|Included|Not included|Target table retains existing records and receives additional records from the source table. The system does not overwrite existing records.|
|Not included|Included|Target table is empty after the clone. The system discards existing target records and copies no records from the source.|
|Not included|Not included|Target table contains only source table data. The system replaces all pre-existing target records with records from the source.|

Update the Clone Profile Preservers and Exclusions lists to include only the Service Exchange tables specified in the following preservers and exclusions tables. Add any missing tables from the specified lists and remove any Service Exchange tables that are not included in these lists.

<table id="table_rsh_4jy_wgc"><thead><tr><th>

 

</th><th>

Preservers table

</th><th>

Exclusions table

</th></tr></thead><tbody><tr><td>

Global

</td><td>

-   catalog\_ui\_policy
-   catalog\_ui\_policy\_action
-   ih\_sync\_capture\_definition
-   ih\_sync\_definition
-   ih\_sync\_inbound\_definition
-   ih\_sync\_outbound\_definition
-   ih\_sync\_process\_event
-   ih\_sync\_remote\_system
-   item\_option\_new
-   sc\_cat\_item\_catalog
-   sc\_cat\_item\_category
-   sc\_cat\_item\_user\_criteria\_mtom
-   sc\_cat\_item\_user\_criteria\_no\_mtom
-   sc\_category
-   scan\_finding
-   scan\_task
-   sn\_sb\_con\_entitlement
-   sn\_sb\_error
-   sn\_sb\_known\_error\_code
-   sn\_sb\_con\_provider\_connection
-   sn\_sb\_con\_provider\_task
-   sn\_sb\_release
-   sn\_sb\_remote\_script\_approval
-   sn\_sb\_rps\_connection
-   sn\_sb\_service\_bridge\_settings
-   sn\_sb\_transform\_line
-   sn\_transport\_queue
-   sn\_fds\_pro\_consumer\_criteria
-   sn\_fds\_pro\_inbound\_offering\_item
-   sn\_fds\_pro\_offering\_item
-   sn\_fds\_con\_outbound\_offering
-   sn\_fds\_con\_outbound\_subscription

</td><td>

-   ih\_sync\_capture\_definition
-   ih\_sync\_definition
-   ih\_sync\_inbound\_definition
-   ih\_sync\_outbound\_definition
-   ih\_sync\_process\_event
-   ih\_sync\_remote\_system
-   scan\_finding
-   scan\_task
-   sn\_sb\_error
-   sn\_sb\_pro\_persona
-   sn\_sb\_remote\_task
-   sn\_sb\_rps\_connection
-   sn\_sb\_service\_bridge\_settings
-   sn\_sb\_transform\_line
-   sn\_fds\_pro\_consumer\_criteria
-   sn\_fds\_pro\_inbound\_offering\_item
-   sn\_fds\_pro\_inbound\_subscription
-   sn\_fds\_pro\_offering\_item
-   sn\_fds\_con\_m2m\_company\_offering
-   sn\_fds\_con\_outbound\_offering\_item
-   sn\_fds\_con\_outbound\_subscription

</td></tr><tr><td>

Base

</td><td>

-   sn\_sb\_authorized\_user
-   sn\_sb\_error
-   sn\_sb\_identity
-   sn\_sb\_known\_error\_code
-   sn\_sb\_provider\_task
-   sn\_sb\_release
-   sn\_sb\_remote\_script\_approval
-   sn\_sb\_remote\_task
-   sn\_sb\_scratchpad
-   sn\_sb\_service\_bridge\_settings
-   sn\_sb\_transform\_line

</td><td>

-   sn\_sb\_authorized\_user
-   sn\_sb\_connection
-   sn\_sb\_entitlement
-   sn\_sb\_error
-   sn\_sb\_identity
-   sn\_sb\_provider\_task
-   sn\_sb\_remote\_record\_producer
-   sn\_sb\_remote\_script\_approval
-   sn\_sb\_remote\_task
-   sn\_sb\_scratchpad
-   sn\_sb\_service\_bridge\_settings
-   sn\_sb\_transform\_line

</td></tr><tr><td>

Provider

</td><td>

-   sn\_sb\_pro\_authorized\_user
-   sn\_sb\_pro\_consumer\_connection
-   sn\_sb\_pro\_entitlement
-   sn\_sb\_pro\_provider
-   sn\_sb\_pro\_provider\_task
-   sn\_sb\_pro\_registration
-   sn\_sb\_pro\_remote\_choice\_definition
-   sn\_sb\_pro\_remote\_record\_producer
-   sn\_sb\_pro\_remote\_service
-   sn\_sb\_pro\_remote\_task
-   sn\_sb\_pro\_remote\_task\_variable
-   sn\_sb\_pro\_service\_bridge\_settings
-   sn\_sb\_pro\_transform

</td><td>

-   sn\_sb\_pro\_inbound\_field
-   sn\_sb\_pro\_outbound\_field
-   sn\_sb\_pro\_provider
-   sn\_sb\_pro\_registration
-   sn\_sb\_pro\_remote\_record\_producer\_consumer\_criteria
-   sn\_sb\_pro\_remote\_task\_def
-   sn\_sb\_pro\_remote\_task\_def\_consumer\_criteria
-   sn\_sb\_pro\_remote\_task\_variable
-   sn\_sb\_pro\_transform

</td></tr><tr><td>

Consumer

</td><td>

-   sn\_sb\_con\_authorized\_user
-   sn\_sb\_con\_consumer
-   sn\_sb\_con\_entitlement
-   sn\_sb\_con\_inbound\_field
-   sn\_sb\_con\_outbound\_field
-   sn\_sb\_con\_provider\_task
-   sn\_sb\_con\_remote\_record\_producer
-   sn\_sb\_con\_remote\_task
-   sn\_sb\_con\_remote\_task\_def
-   sn\_sb\_con\_remote\_task\_variable
-   sn\_sb\_con\_service\_bridge\_settings
-   sn\_sb\_con\_transform

</td><td>

-   sn\_sb\_con\_consumer
-   sn\_sb\_con\_inbound\_field
-   sn\_sb\_con\_outbound\_field
-   sn\_sb\_con\_persona
-   sn\_sb\_con\_remote\_task\_def
-   sn\_sb\_con\_remote\_task\_variable
-   sn\_sb\_con\_transform

</td></tr><tr><td>

Remote Process Sync Transport

</td><td>

sn\_sb\_rps\_connection \(Provider only\)

</td><td>

sn\_sb\_rps\_connection \(Provider only\)

</td></tr><tr><td>

Transporter

</td><td>

-   sn\_transport\_profile\*
-   sn\_transport\_queue\*

</td><td>

N/a

</td></tr><tr><td>

Employee Profile

</td><td>

-   user\_criteria
-   sys\_alias
-   sys\_user
-   sys\_user\_has\_role

</td><td>

sys\_alias

</td></tr><tr><td>

Foundation Data Sync

</td><td>

-   sn\_fds\_data\_processing\_queue
-   sn\_fds\_offering
-   sn\_fds\_offering\_item
-   sn\_fds\_request
-   sn\_fds\_subscription
-   sn\_fds\_subscription\_item

</td><td>

-   sn\_fds\_data\_processing\_queue
-   sn\_fds\_offering\_item
-   sn\_fds\_subscription
-   sn\_fds\_subscription\_item

</td></tr><tr><td>

Foundation Data Sync for Providers

</td><td>

-   sn\_fds\_pro\_inbound\_offering\_request
-   sn\_fds\_pro\_offering
-   sn\_fds\_pro\_offering\_request

</td><td>

-   sn\_fds\_pro\_inbound\_offering
-   sn\_fds\_pro\_inbound\_offering\_request
-   sn\_fds\_pro\_inbound\_subscription\_item
-   sn\_fds\_pro\_offering
-   sn\_fds\_pro\_subscription
-   sn\_fds\_pro\_subscription\_item

</td></tr><tr><td>

Foundation Data Sync for Consumers

</td><td>

-   sn\_fds\_con\_offering
-   sn\_fds\_con\_offering\_item
-   sn\_fds\_con\_offering\_request
-   sn\_fds\_con\_outbound\_offering\_request
-   sn\_fds\_con\_subscription
-   sn\_fds\_con\_subscription\_item

</td><td>

-   sn\_fds\_con\_offering\_item
-   sn\_fds\_con\_subscription
-   sn\_fds\_con\_subscription\_item

</td></tr><tr><td>

Health

</td><td>

-   sn\_sb\_issue
-   sn\_sb\_health\_connection\_stats
-   sn\_sb\_health\_issue

</td><td>

-   sn\_sb\_issue
-   sn\_sb\_health\_connection\_stats
-   sn\_sb\_health\_issue

</td></tr></tbody>
</table>"\*" - Applicable for both provider and consumer.

The following scenarios describe how clone operations affect table data based on table configuration in the Clone profile preservers list and the Exclude tables list.

The following examples use tables from this page to illustrate each scenario:

**sn\_sb\_service\_bridge\_settings** \(included in both lists\): The system preserves connection settings you configured on the target instance after the clone. Settings from the source instance do not overwrite them.

**sn\_sb\_con\_entitlement** \(included in Clone profile preservers only\): The target instance retains existing entitlement records and receives additional entitlement records from the source instance.

**sn\_sb\_error** \(included in Exclude tables only\): The error records table is empty on the target instance after the clone. The system discards error records that existed on the target and copies none from the source.

**sn\_fds\_offering** \(not included in either list\): The system replaces the target table with source data. Records that existed on the target instance before the clone are replaced by source instance records.


```


### File: service-exchange\service-bridge-v2-con-acknowledge-fds-request.md

```text
---
title: Acknowledge foundation data sync offering request from your provider
description: Acknowledge a foundation data sync \(FDS\) offering request and send a sample payload to help your provider understand the type of data they will receive.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring outbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Acknowledge foundation data sync offering request from your provider

Acknowledge a foundation data sync \(FDS\) offering request and send a sample payload to help your provider understand the type of data they will receive.

## Before you begin

Role required: admin \(sb\_admin\)

## About this task

After a provider requests an FDS offering, the system generates an FDS request and corresponding FDS subscriptions in your Service Exchange instance.

If the **Auto acknowledge FDS Requests** option is not selected, you must manually acknowledge the provider's FDS request to inform them that you're working on the request. Then, send a sample payload to help them understand the type of data they will receive.

When a provider requests an FDS offering, you receive an email notification about the new request, including any required actions.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Open Records** &gt; **FDS Request**.

2.  Under **Type: Outbound**, open the FDS request by selecting the record number in the Number column.

    The FDS Request form displays details about the provider's data request.

3.  Select the **Acknowledge** button.

    The request state changes from Received to Work In Progress, and the provider is notified that you're processing their request.

4.  Send a sample payload for each subscription.

    Each sample payload contains up to five records of sample data to give providers visibility into the data structure and content they will receive.

    1.  In the Foundation Data Consumer Outbound Subscription related list, open the subscription by selecting the record number in the Number column.

    2.  Select the **Send Sample** button.

        The sample payload sent to the provider is listed in the **Sample Payload** column in the Subscription Items related list.


## Result

A sample payload for each subscription is sent to the provider as sample data. The provider can review the sample to verify the data structure and content before accepting the full data synchronization.

## What to do next

[Publish the foundation data subscription.](service-bridge-v2-publish-con-fds-subscription.md)

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)


```


### File: service-exchange\service-bridge-v2-conf-consumer-flow.md

```text
---
title: Service Exchange consumer pre-flows
description: As a consumer, you can control when data should be synced between the provider tasks on the consumer and provider instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Service Exchange consumer pre-flows

As a consumer, you can control when data should be synced between the provider tasks on the consumer and provider instances.

## Before you begin

-   Role required: admin
-   A subflow with the sync condition should have been created

Role required: admin

## About this task

You can attach a subflow with a Service Exchange remote record producer and run processes such as approvals, before syncing a task with the provider. When a new provider task is created, the attached subflow is executed before the data is synced between the consumer and provider instances. The subflow must set a field called **Sync** on the Provider task to **true** for the record to sync to the provider. If the remote record producer doesn’t have an attached subflow, provider tasks are immediately synced to the provider instance.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Provider Connections**.

2.  Select a remote record producer for which you want to attach a subflow.

3.  In the Flow field, select the subflow that is to be applied to the provider task.

    Data is synced to the provider instance only if the attached subflow sets the **Sync** flag to **true** on the provider task.

4.  Select **Update**.

    Depending on the conditions defined in the subflow, the provider task is synced to the provider instance.



```


### File: service-exchange\service-bridge-v2-config-revision.md

```text
---
title: Configuring revisions
description: As a provider, you can update the configurations of remote record producers, remote task definitions, foundation data sync offerings, and create new versions that can be entitled to consumers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Configuring revisions

As a provider, you can update the configurations of remote record producers, remote task definitions, foundation data sync offerings, and create new versions that can be entitled to consumers.

You can deploy new versions of entitlements with updated functionality to compatible consumers without impacting consumers who haven’t upgraded their Service Exchange applications. You can upgrade your Service Exchange applications to adopt new features even if your consumers haven’t upgraded to the latest version.

You can create multiple configuration revisions, but only the latest published revision is active and available as a new entitlement. Your consumers can either choose to activate the new entitlement or continue to use the older revision until it's archived or retired. If the consumers want to use the new revision, they must upgrade their Service Exchange application to the same version that is running on the provider's instance. Once the new revision is activated on the consumer's instance, the earlier revision is longer available and moves to an inactive state.

You can create configuration revisions for the following:

-   Remote record producers
-   Remote task definitions
-   Foundation data sync offerings

**Related topics**  


[Create configuration revisions](service-bridge-v2-create-config-rev.md)


```


### File: service-exchange\service-bridge-v2-configure-consumer-settings.md

```text
---
title: Configure settings on the consumer instance
description: As a consumer, you can configure and define default settings on your instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Configure settings on the consumer instance

As a consumer, you can configure and define default settings on your instance.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  Click the Number link on the Provider Connections page.

3.  Under the Related Links, click the **Settings** tab and click **New**.

4.  In the Settings page, click the **Remote Record Producers** tab under the Related Links.

5.  Enable the **Auto activate remote record producer** check box if you want the remote record producers to be automatically activated.

6.  Click the **Remote Task Definitions** tab.

7.  Enable the **Auto activate remote task definition** check box if you want the remote task definition to be automatically activated.

8.  Click the **Authorized Users** tab.

    -   Max authorized users: This field is available only if the Restrict authorized users flag has been enabled. Specify the maximum number authorized users that can be defined on the consumer's instance.
    -   Restrict authorized users: Select the check box if you want restrict the number of authorized users on the consumer's instance.
    -   Auto approve authorized users: If this check box is selected, authorized users created on the consumer instance are automatically approved.
9.  Click **Update**.



```


### File: service-exchange\service-bridge-v2-configure-inboun-fds-providers.md

```text
---
title: Configuring inbound foundation data sync as providers
description: As a provider, receive the foundation data from your provider using foundation data sync \(FDS\).
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Configuring inbound foundation data sync as providers

As a provider, receive the foundation data from your provider using foundation data sync \(FDS\).

Before you use FDS, you must request and configure foundation data. After your consumer creates and publishes FDS definitions, request and configure FDS.

<table id="table_tqf_wwj_5de"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[Request a foundation data offering from your consumer.](../task/service-bridge-v2-request-fds-offering-consumers.md)

</td><td>

Requests FDS offerings from your consumer based on the published offerings.After you request a foundation data offering, your consumer acknowledges your FDS request and sends a sample payload for each subscription.

</td></tr><tr><td>

2.

</td><td>

[Configure the sample data and validate subscription items.](../task/service-bridge-v2-fds-validate-subs-items-provider.md)

</td><td>

Configure the incoming data based on the CMDB or non-CMDB table to validate subscription items.After you validate subscription items, you must accept the subscription.

</td></tr><tr><td>

3.

</td><td>

[Accept the subscription.](../task/service-bridge-v2-fds-accept-sups-provider.md)

</td><td>

Accept the subscription.After you accept the subscription, your consumer publishes the subscription and data synchronizes according to the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[Foundation data sync](service-bridge-v2-explore-foundation-data-sync.md)

[Configuring outbound foundation data sync as consumers](using-provider-bound-fds-consumer.md)


```


### File: service-exchange\service-bridge-v2-configure-provider.md

```text
---
title: Configure Service Exchange for Providers
description: To set up and configure the Service Exchange for Providers application, follow these steps.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service Exchange for Providers, Service Exchange]
---

# Configure Service Exchange for Providers

To set up and configure the Service Exchange for Providers application, follow these steps.

## Pre-installation checks

**Check glide.servlet.uri property**: Ensure that the `glide.servlet.uri` property in the Glide instance is set to the correct instance URL. An issue can occur when an instance is cloned from production, but still refers to the production URL for the `glide.servlet.uri` property.

|Task|Link|
|----|----|
|Install the Service Exchange for Providers application.|See [Install Service Exchange for Providers](../task/install-service-bridge-v2-provider.md).|
|Set up a new provider record.|See [Set up a Service Exchange provider record](../task/service-bridge-v2-new-provider.md).|
|Assign Service Exchange roles for providers.|See [User roles for providers](service-bridge-v2-personas.md).|
|Create catalog personas.|See [Create catalog personas](../task/service-bridge-v2-create-catalog-persona.md).|
|Create remote choice definitions.|See [Create remote choice definitions in Service Exchange for Providers](../task/service-bridge-v2-create-remote-choice-fld-defs.md)|
|Create remote catalog items.|See [Create remote catalogs in Service Exchange for providers](service-bridge-v2-remote-catalog.md).|
|Create remote task definitions.|See [Create a remote task definition in Service Exchange for Providers](../task/service-bridge-v2-create-remote-tasks-defs.md).|
|Create transforms.|See [Create a transform in Service Exchange](../task/service-bridge-v2-create-transform.md).|
|Update Authorized Users settings.|See [Update settings for authorized users](../task/service-bridge-v2-configure-settings.md)|

If you’re a consumer, see [Configure Service Exchange for Consumers](service-bridge-v2-install.md).

**Related topics**  


[Configure Service Exchange for Consumers](service-bridge-v2-install.md)

[Service Exchange](../../tmt-service-bridge/concept/tmt-service-bridge-both-landing-page.md)


```


### File: service-exchange\service-bridge-v2-configure-settings.md

```text
---
title: Update settings for authorized users
description: As a provider, you can configure the settings for Authorized Users who have been created on the consumer's instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Update settings for authorized users

As a provider, you can configure the settings for Authorized Users who have been created on the consumer's instance.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Consumers**.

2.  Open the appropriate Consumer Connection form.

3.  Under the Related Links, click the **Settings** tab and open the record displayed.

4.  Click the **Authorized Users** tab.

    -   Max authorized users: This field is available only if the Restrict authorized users flag has been enabled. Specify the maximum number authorized users that can be defined on the consumer's instance.
    -   Restrict authorized users: Select the check box if you want restrict the number of authorized users on the consumer's instance.
    -   Auto approve authorized users: If this check box is selected, authorized users created on the consumer instance are automatically approved.
5.  Click **Update**.

    **Note:** You can view the settings defined in the Remote Record Producers and Remote Task Definitions tabs but cannot modify them.


**Parent Topic:**[Using Service Exchange for providers](../concept/service-bridge-v2-administer.md)


```


### File: service-exchange\service-bridge-v2-consumer-criteria-new-record-form.md

```text
---
title: Consumer criteria new record form
description: Field descriptions for the consumer criteria new record form contains information on consumer criteria new record form field values.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Service Exchange]
---

# Consumer criteria new record form

Field descriptions for the consumer criteria new record form contains information on consumer criteria new record form field values.

<table id="table_u2k_mpp_b1c"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the consumer condition.

</td></tr><tr><td>

Active

</td><td>

Select this check box to enable the consumer condition.

</td></tr><tr><td>

Condition for

</td><td>

Allows you to specify the Company or Account can be used to match the records on the table being queried. Select the corresponding option based on which field \(Company or Account\) is available on the table being queried. For example, this field can be used on the Sold Product table as the Account field is used to query the table.

</td></tr><tr><td>

Condition on

</td><td>

Field indicates which table is to be queried to find matching records.**Note:** Tables where Customer Field cannot be selected should not be used.

</td></tr><tr><td>

Customer field

</td><td>

Select the field on the table being queried that matches the Company or Account defined on the Service Exchange connection. If the consumer connected through Service Exchange is an Account, you can use either a Company or Account field to match against it. If the consumer connected is only a Company, you will be restricted to Company.

</td></tr><tr><td>

Condition

</td><td>

Details of the filter. For example, Active is True.

</td></tr></tbody>
</table>## Useful references

[Create a consumer criteria](../concept/service-bridge-v2-create-consumer-criteria.md).


```


### File: service-exchange\service-bridge-v2-consumer-variables.md

```text
---
title: Add consumer variables to a remote record producer
description: As a consumer, you can add your own variables to a provider's remote record producer \(RRP\) in your consumer instance using a variable set. Consumer variables are useful in a Consumer Pre-Flow for adding additional information to complete a flow.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Add consumer variables to a remote record producer

As a consumer, you can add your own variables to a provider's remote record producer \(RRP\) in your consumer instance using a variable set. Consumer variables are useful in a Consumer Pre-Flow for adding additional information to complete a flow.

## Before you begin

Note the following requirements:

-   You must be using Service Exchange version 2.1.x+.
-   You have added the necessary variables to a variable set. For more details, see [Using variable sets with Remote Record Producers](../concept/service-bridge-v2-variable-sets.md).

Role required: admin, itil, sn\_sb.admin

## About this task

-   You can add only one variable set to a provider's RRP in your consumer instance.
-   The variable set you add in your consumer instance doesn’t automatically synchronize with the provider instance.
-   You cannot edit any provider variables.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  On the Provider connection page, open your provider connection by selecting the relevant number link.

3.  Select the Remote record producers related list.

4.  Select the remote record producer.

    You can select only record producers with a Compatibility field value of 2.1.x+.

5.  In the Remote record producers form, in the Consumer variables field, select the variable set you want to add.

6.  Select **Update**.



```


### File: service-exchange\service-bridge-v2-copy-catalog-as-rrp.md

```text
---
title: Publish catalog items as remote record producers
description: As a provider, you can copy your local catalog items to Service Exchange as remote record producers \(RRP\) enabling you to avoid manual re-creation of catalog items as RRPs.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Publish catalog items as remote record producers

As a provider, you can copy your local catalog items to Service Exchange as remote record producers \(RRP\) enabling you to avoid manual re-creation of catalog items as RRPs.

## Before you begin

Make sure that the catalog items you want to copy meet the following requirements:

-   Must be in the published state
-   Must not have been already copied to Service Exchange

Role required: admin

## About this task

By default, you can copy hardware, software, record producers, and general catalog items to RRPs, either individually or in bulk. You can copy other catalog items as well by creating a property file to include all the catalog item type you want to copy.

**Tip:** If you create a system property, make sure to select the application scope as Service Exchange provider.

After you copy, you can edit and publish these RRPs.

## Procedure

1.  Navigate to **All** and type `sc_cat_item.list` in the navigation filter.

2.  Select the catalog item.

    You can select more than one.

    By default, you can copy 20 catalog items as RRPs at a time. If you want to change the limit, you need to add the **sn\_sb\_pro.max\_batch\_size\_covertable\_catalog\_items** system property, which is of type Integer.

3.  From the action menu, select **Publish to Service Exchange**.

    A message is displayed stating the publishing status.

    -   If the publishing to Service Exchange is successful, a success message is displayed.
    -   If the publishing isn’t successful, a failed message is displayed.

        Resolve the failed process by reviewing the logs to identify the issues, fixing the issues, and trying to publish to Service Exchange again.

4.  View copied RRPs by selecting **Click here** in the success message.

5.  Review the copied RRPs for accuracy.

6.  Add a variable to each RRP if not already available.

    Each RRP must have at least one variable. You can add more than one variable. For more details, see [Create variables for remote record producers in Service Exchange for Providers](service-bridge-v2-assign-variables-ser-defn.md).

7.  Add a flow to the RRP using **Flow** field.

    Each RRP must have a flow. Choose one of the default Service Exchange flows provided or create your own flow if required.

8.  Add a consumer criteria.

9.  Select **Publish**.



```


### File: service-exchange\service-bridge-v2-create-apps.md

```text
---
title: Remote catalogs
description: As an application developer for the provider, you can create a remote catalog item containing the services for your consumers. After you create these items, an administrator in the consumer’s instance can assign them to the consumer's catalogs and categories and then activate them, just like any other catalog item.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Remote catalogs

As an application developer for the provider, you can create a remote catalog item containing the services for your consumers. After you create these items, an administrator in the consumer’s instance can assign them to the consumer's catalogs and categories and then activate them, just like any other catalog item.

**Example:**

For example, let's say that you have multiple SD-WAN product offerings: Gold, Silver, and Bronze. Your remote catalog contains 20 services that are associated with the SD-WAN products.

-   The Gold product offering gives your consumer rights to all 20 services.
-   The Silver product offering gives your consumer rights to 15 of the 20 services.
-   The Bronze product offering gives your consumer rights to only 10 of the 20 services.

You can package all 20 of those services in a single catalog. The consumers for each product offering only have rights to the services to which they are entitled.

To learn more, see [Create remote catalogs in Service Exchange for providers](service-bridge-v2-remote-catalog.md).

**Related topics**  


[Create remote catalogs in Service Exchange for providers](service-bridge-v2-remote-catalog.md)


```


### File: service-exchange\service-bridge-v2-create-auth-user.md

```text
---
title: Add an authorized user
description: As a consumer, add new authorized users to control the access to catalog items that are entitled to you by your provider.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Add an authorized user

As a consumer, add new authorized users to control the access to catalog items that are entitled to you by your provider.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  On the Provider Connections page, click the **Number** link to open a Provider Connection record.

3.  Select the **Catalog Personas** related tab and check if you have any entitled personas from your provider.

4.  On the **Authorized Users** related tab, click **New**.

5.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Consumer user|Name of the user. You can select the name from the user's list.|
    |Provider connection|Name of the service provider. This field is auto-filled.|
    |Persona|Persona\(s\) that you want to add to the user.|

6.  Right click the form header and click **Save**.

7.  Click **Activate**.


## Result

The authorized user record syncs to the provider's ServiceNow instance for approval. After it is approved and activated, the user can see the remote record producers with their assigned personas.


```


### File: service-exchange\service-bridge-v2-create-catalog-persona.md

```text
---
title: Create catalog personas
description: Create catalog user personas to control the catalog items that consumers can access on their instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create catalog personas

Create catalog user personas to control the catalog items that consumers can access on their instance.

## Before you begin

Role required: admin, sn\_sb.admin

## About this task

You can assign personas to Remote Record Producers \(RRPs\). Personas are associated with a Remote Record Producer, and an Entitlement is generated for that record producer and synced with the consumer instance. An Entitlement is generated for all personas on the consumer's instance. Finally, personas can be related to Authorized Users to access the Remote Record Producers.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Catalog Personas**.

2.  Click **New**.

3.  Enter a name and description for the catalog persona.

4.  Click **Submit**.



```


### File: service-exchange\service-bridge-v2-create-client-script.md

```text
---
title: Create catalog client scripts
description: As a provider, create catalog client scripts in Service Exchange to control the behavior of the catalog items when presented to your consumers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create catalog client scripts

As a provider, create catalog client scripts in Service Exchange to control the behavior of the catalog items when presented to your consumers.

## Before you begin

You must be using Service Exchange version 2.1.x+.

Role required: admin

## About this task

You can apply catalog client scripts to a catalog item or a variable set. These scripts run on the browser instead of the server, enables you to control the information that the consumer submits better.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Catalog Items**.

2.  Select the Remote record producer.

    You can select only record producers with a Compatibility field value of 2.1.x+.

3.  In the Remote record producer form, select the Catalog Client Scripts related list and then select **New**.

4.  On the form, fill in the fields.

    For a description of the field values, see [Catalog client script new record form](../reference/service-bridge-v2-cat-script-fd.dita.md).

5.  Select **Submit**.



```


### File: service-exchange\service-bridge-v2-create-config-rev.md

```text
---
title: Create configuration revisions
description: As a provider, you can edit and create revisions of entitlements that contain updated functionality that can be developed and deployed to consumers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create configuration revisions

As a provider, you can edit and create revisions of entitlements that contain updated functionality that can be developed and deployed to consumers.

When the new revision is deployed, consumers can either activate and use the new revision, or continue to use the old revision. The new revision can be activated only if the consumer is using a Service Exchange application version that is compatible with the Service Exchange application version compatibility set on the revision. If the consumers want to use the new revision, they must upgrade their Service Exchange application to the minimum compatibility that is set on the configuration.

## Configuration revision life cycle

A configuration can be one of the following:

-   Remote task definition
-   Remote record producer

**Note:** The following sections describe the various stages in the configuration revision life-cycle of a remote task definition. You can:

-   [Create a configuration revision](service-bridge-v2-create-config-rev.md#section_l2g_psf_tbc)
-   [Archive a configuration revision](service-bridge-v2-create-config-rev.md#section_zjw_2qc_sbc)
-   [Retire a configuration](service-bridge-v2-create-config-rev.md#section_x1w_dqc_sbc)
-   [Copy a configuration revision](service-bridge-v2-create-config-rev.md#section_gst_43n_tbc)
-   [Delete a configuration](service-bridge-v2-create-config-rev.md#section_igy_2jn_tbc)

You can follow the same process to create revisions for a remote record producer.

## Create a configuration revision

1.  Navigate to the **All** &gt; **Service Exchange Provider** &gt; **Remote task definitions**.
2.  Select the remote task definition for which you want to create a configuration revision.

    **Note:** The remote task definition that you select must be in the **Published** state.

    ![Service Exchange Remote Task Definition](../image/service-bridge-v2-remote-task-defn1.jpg)

    Note the **Compatibility** field. This field shows the Service Exchange version that is being used by the provider. If the consumer is using a compatible Service Exchange version, data can be synced between the provider and consumer instances. But if the consumer isn’t using a compatible version, any new entitlements can’t be activated until the corresponding Service Exchange version is upgraded. See [Mismatched version support](service-bridge-v2-mismatch-version.md) for additional information.

3.  Select **Checkout**.
4.  A new revision of the configuration is created and the State is set to **In Draft**.

    ![Revisions related list for a Service Exchange](../image/service-bridge-v2-revision-rel-list.jpg)

    You can view the older revision by navigating to the Revisions tab under the Related List section. As you can see in the preceding image, the older revision is still in the **Published** state.

5.  Make the necessary changes and select **Save** to save the changes. Select **Publish** to activate the newly created configuration revision. The newly activated revision is synced to the consumer instance. The State of the older revision is set to **Inactive**.

    **Note:** The inactive configuration is still available to the consumers and data synchronization will continue until this configuration is either archived or retired.

6.  On the consumer instance, navigate to **Service Exchange Consumer** &gt; **Provider Connections**. You can see the newly published configuration revision under the Entitlements tab in the Related Links section.![Configuration revisions entitled to consumer](../image/service-bridge-v2-config-rev-entitle.jpg)
7.  Select the newly published configuration reference and select the **Entity reference** link to navigate to the Remote task definition page.
8.  Select **Activate** to activate the new configuration revision. When the new revision is activated, the earlier revision moves to an **Inactive** state. Consumers can continue to use the earlier revision until it’s archived or retired.
9.  You can create multiple configuration revisions for a single configuration but only the latest published revision is active and can be used by the consumers.

    **Note:**

    -   If you create a configuration revision and select **Save**, the revision is set to the **Draft** state. If you open the **Published** revision of this configuration, you’ll notice that the **Checkout** and **Retire** options are unavailable. In this case, you must open the draft version to make any changes.
    -   If the newly created draft revision isn’t required, select **Cancel** to delete that draft revision. The already published revision is available to **Checkout** or **Retire**.

## Archive a configuration revision

You can archive an inactive configuration revision. When a revision is archived by the provider, it’s deactivated and the State is set to **Archived** on the consumer instance. The following steps describe how to archive a remote task definition configuration revision. The same process is applicable to the remote record producers and foundation data sync offerings.

1.  Navigate to the **All** &gt; **Service Exchange Provider** &gt; **Remote task definitions**.
2.  Select a remote task definition in the list.
3.  Navigate to the **Revisions** tab in the Related List.
4.  Select the inactive revision that you want to the archive.
5.  Click **Archive** to deactivate the remote task definition. Once archived, this revision is no longer available to consumers.

    **Note:** You can’t Publish, Update, or Checkout an archived configuration revision. You can use the **Copy** option to make a copy of the configuration.


## Retire a configuration

You can retire a published configuration. When you retire a configuration, the entire set of revisions associated with the configuration are retired. To retire a configuration, follow these steps:

1.  Navigate to the **All** &gt; **Service Exchange Provider** &gt; **Remote task definitions**.
2.  Select a remote task definition configuration on the list.
3.  Select **Retire** and then select **OK**. Once retired, this configuration is no longer available to consumers.

    **Note:** This option retires published and inactive configuration revisions. But configuration revisions in the **Archived** state aren’t retired.

4.  If you want to use the remote task definition again, you can:
    -   Select **Checkout** to create a new configuration revision.
    -   Select **Copy** to make a duplicate copy of the new configuration.

## Copy a configuration revision

You can make a duplicate copy of a configuration revision that is one of the following states:

-   Published
-   Inactive
-   Archived
-   Retired

1.  Navigate to the **All** &gt; **Service Exchange Provider** &gt; **Remote task definitions**.
2.  Select a remote task definition configuration revision that is in any of the preceding states.
3.  Select **Copy** to make a copy of the configuration revision.

## Delete a configuration

You can delete a configuration that has been retired. There may be many retired revisions present but the **Delete** option is available only for the latest retired configuration revision. When a revision is deleted, the entire configuration set is deleted.

1.  Navigate to the **All** &gt; **Service Exchange Provider** &gt; **Remote task definitions**.
2.  Select a remote task definition that is in the **Retired** state.
3.  Select **Delete** to delete the configuration if it’s no longer required. Once deleted, all records associated with this identity are deleted and can’t be undone.


```


### File: service-exchange\service-bridge-v2-create-consumer-criteria.md

```text
---
title: Create a consumer criteria
description: Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a consumer criteria

Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.

## Before you begin

Role required: admin

## Procedure

1.  In the Consumer Criteria related table, select **New**.

2.  In the **Condition** field, select the Lookup using list icon, and then either select an existing condition or create a new condition![Lookup using list icon](../../../common/image/List_SearchIcon.png).

<table id="choicetable_yhh_n4d_5fc"><thead><tr><th align="left" id="d22226e75">

Option

</th><th align="left" id="d22226e78">

Action

</th></tr></thead><tbody><tr><td id="d22226e84">

**Select existing condition**

</td><td>

From the list, select an existing condition.

</td></tr><tr><td id="d22226e93">

**Create a new condition**

</td><td>

1.  In the Entity Criteria popup, select **New**.
2.  On the Consumer criteria new record form, fill in the fields.

For a description of the field values, see [Consumer criteria new record form](../reference/service-bridge-v2-consumer-criteria-new-record-form.md).

3.  Select **Submit.**
4.  From the criteria list, select your criteria.


</td></tr></tbody>
</table>
## Consumer criteria

The following examples show how consumer criteria can be configured.

This consumer criteria can be used to entitle content to Service Exchange customers that have an active sold product where product name contains **Laptop – DaaS**.

![Consumer criteria configuration example 1](../image/service-bridge-v2-consum-crit-ex1.jpg)

This consumer criteria entitles content to the Boxeo Service Exchange consumer. It is used to query the Service Exchange Connection table and is filtered with Boxeo as the consumer.

![Consumer criteria configuration example 2](../image/service-bridge-v2-consum-crit-ex2.jpg)

This consumer criteria entitles content to Service Exchange consumers that have an active contract where the Contract model is Print Solution and the Contract Type is Service Contract.

![Consumer criteria configuration example 3](../image/service-bridge-v2-consum-crit-ex3.jpg)


```


### File: service-exchange\service-bridge-v2-create-fds-offering-definition.md

```text
---
title: Create and publish a foundation data sync offering definition
description: Create an foundation data sync \(FDS\) offering definition to inform your consumers about the data you’re ready to share.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configuring outbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create and publish a foundation data sync offering definition

Create an foundation data sync \(FDS\) offering definition to inform your consumers about the data you’re ready to share.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **FDS Offering Definitions**.

2.  Select **New**.

3.  Determine whether to publish FDS subscriptions automatically or manually.

<table id="table_wl4_ddb_1gc"><thead><tr><th>

Method

</th><th>

Description

</th><th>

Action

</th></tr></thead><tbody><tr><td>

Auto publish FDS subscriptions \(default option\)

</td><td>

After the offering is published, when consumers accept the subscription, it’s automatically published and data is synchronized according to the defined cadence.

</td><td>

If it is not already selected, select the **Auto publish FDS subscriptions** check box.

</td></tr><tr><td>

Manually publish FDS subscriptions

</td><td>

After the offering is published, and consumers accept the subscription, you must acknowledge it and send sample files to let them know about the type of data they will receive.For the detailed procedure, see [Validate foundation data sync subscription items](service-bridge-v2-validate-fds-subscription.md).

</td><td>

Clear the**Auto publish FDS subscriptions** check box.

</td></tr></tbody>
</table>4.  Determine whether consumer FDS requests should be automatically acknowledged with a sample payload automatically sent to the consumer in response to each FDS request or manually acknowledged.

    |Method|Description|Action|
    |------|-----------|------|
    |Auto acknowledge FDS requests|After the offering is published, all FDS requests from consumers are automatically acknowledged and a sample payload is sent to the consumer in response to each FDS request.|If it is not already selected, select the **Auto Acknowledge FDS Requests** check box.|
    |Manually acknowledge FDS requests|After the offering is published, consumer FDS requests must be acknowledged manually. For the detailed procedure, see [Validate foundation data sync subscription items](service-bridge-v2-validate-fds-subscription.md)|Clear the**Auto Acknowledge FDS Requests** check box.|

5.  Provide a name and description.

6.  Select **Save**.

7.  In the Offering items related list, create an offering item.

    For each table you offer to share, you must create an offering item. You can create more than one offering.

    1.  Select **New**.

    2.  In the **Table name** field, select the table you want to share with your consumer.

    3.  In the **Outbound field**, select the table fields you want to share by selecting the lock icon and moving them from the **Available** to the **Selected** column.

    4.  If you selected a non-CMDB table, unlock the **Coalesce field** field, select the table fields you want to share, and move them from the **Available** to the**Selected** column.

    5.  Select **Save**.

8.  Create a dependent relationship for the offering item.

    If the table you are offering depends on another table, you must create a dependent table offering to share the related table. You can create multiple dependent offerings.

    1.  Select **Create Dependent Offering Item**.

    2.  From the drop-down menu, choose a dependent item and select **Create Offering Item**.

    3.  In the **Outbound field**, select the table fields you want to share by selecting the lock icon to unlock the field.

    4.  Select **Save**.

9.  Return to the main offering page by selecting **Back**.

10. In the Consumer criteria related list, add a consumer criteria to determine which consumer instances are eligible to receive the offering.

    For information on consumer criteria, see [Create a consumer criteria](../concept/service-bridge-v2-create-consumer-criteria.md) topic.

11. Select **Publish**.


## Result

The FDS offering is now published. Consumers can request foundation data based on the published FDS offering.

## What to do next

[Acknowledge foundation data sync offering request](service-bridge-v2-acknowledge-FDS-request.md).


```


### File: service-exchange\service-bridge-v2-create-provider-bound-fds-consumer.md

```text
---
title: Create and publish a provider-bound foundation data sync offering definition
description: Create a foundation data sync \(FDS\) offering definition to inform your providers about the data you're ready to share.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Configuring outbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Create and publish a provider-bound foundation data sync offering definition

Create a foundation data sync \(FDS\) offering definition to inform your providers about the data you're ready to share.

## Before you begin

Version required: 2.3.x.

Role required: admin \(sb\_admin\)

## About this task

As a consumer, you can create FDS offering definitions to share data with providers. This process enables you to configure which tables and fields you want to make available, set up automatic or manual publishing workflows, and define eligibility criteria for providers.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Administration** &gt; **FDS Offering Definitions**.

2.  Select **New**.

3.  Determine whether to publish FDS subscriptions automatically or manually.

<table id="table_wl4_ddb_1gc"><thead><tr><th>

Method

</th><th>

Description

</th><th>

Action

</th></tr></thead><tbody><tr><td>

Auto publish FDS subscriptions \(default option\)

</td><td>

After the offering is published, when your provider accepts the subscription, it's automatically published and data is synchronized according to the defined cadence.

</td><td>

If it isn’t already selected, select the **Auto publish FDS subscriptions** check box.

</td></tr><tr><td>

Manually publish FDS subscriptions

</td><td>

After the offering is published and the provider accepts the subscription, you must acknowledge it manually. Then send sample files to let them know about the type of data they’ll receive.For the detailed procedure, see TBD.

</td><td>

Clear the **Auto publish FDS subscriptions** check box.

</td></tr></tbody>
</table>4.  Determine whether provider FDS requests should be automatically acknowledged with a sample payload automatically sent to the provider in response to each FDS request or manually acknowledged.

    |Method|Description|Action|
    |------|-----------|------|
    |Auto acknowledge FDS requests|After the offering is published, all FDS requests from providers are automatically acknowledged and a sample payload is sent to the provider in response to each FDS request.|If it isn’t already selected, select the **Auto Acknowledge FDS Requests** check box.|
    |Manually acknowledge FDS requests|After the offering is published, provider FDS requests must be acknowledged manually. For the detailed procedure, see TBD.|Clear the **Auto Acknowledge FDS Requests** check box.|

5.  Provide a name and description for the offering definition.

6.  Select **Save**.

    The FDS offering definition is saved and you can now add offering items.

7.  In the Offering items related list, create an offering item.

    For each table you offer to share with providers, you must create an offering item. You can create more than one offering item to share data from multiple tables.

    1.  Select **New**.

    2.  In the **Table name** field, select the table you want to share with your providers.

    3.  In the **Outbound field**, select the table fields you want to share by selecting the lock icon and moving them from the **Available** to the **Selected** column.

    4.  If it isn’t already selected, select the **AccountSecure** check box to ensure data security.

        When enabled, only records where the company field matches the connection company are synchronized. Clear this option to synchronize all records regardless of company.

        **AccountSecure** option is selected by default.

    5.  If it isn’t already selected, select **Send attachment** check box to send attachment.

        When enabled, file attachments linked to records are included in the synchronization.

        **Send attachment** option is selected by default.

    6.  If you selected a non-CMDB table, unlock the **Coalesce fields**, select the table fields you want share, and move them from the **Available** to the **Selected** column.

        Coalesce fields help identify unique records when synchronizing data between instances.

    7.  If it isn’t already selected, for a non-CMDB table, select the **Maintain SysID** check box to preserve referential integrity.

        When enabled, new records created in the destination instance maintain their original sys\_id. However, if an existing record is updated, the sys\_id may not be preserved.

        **Maintain SysID** option is selected by default for non-CMDB tables and not available for CMDB tables.

    8.  If needed, add conditions to filter which records are shared with providers.

        Use the condition builder to specify criteria that determine which records from the selected table are included in the data sync.

    9.  Select **Save**.

        By default,

8.  Create a dependent relationship for the offering item.

    If the table you’re offering depends on another table, you must create a dependent table offering to share the related table. You can create multiple dependent offerings to maintain referential integrity.

    1.  Select **Create Dependent Offering Item**.

    2.  From the drop-down menu, choose a dependent item and select **Create Offering Item**.

    3.  In the **Outbound field**, select the table fields you want to share by selecting the lock icon to unlock the field.

    4.  Select **Save**.

9.  Preview data for the offering item connection.

    Preview the data that will be synchronized with your provider before publishing the offering. In the preview, you can visualizing available data, test filter conditions, and apply validated conditions directly to the offering item configuration.

    1.  Select **Preview for Connection**.

        You can also access this preview later by opening an existing offering item from the Offering Items related list.

    2.  On the Foundation Data Sync: Preview for connection page, from the Connection drop-down list, select the provider account.

    3.  Add conditions to filter which records are shared with providers.

        Use **Add Filter Condition** to add individual conditions or Add **OR Clause** to add alternative conditions.

    4.  Select **Run** to visualize the data.

        The preview displays all records matching your configuration and filter conditions.

    5.  Apply the filter conditions to the offering item by selecting **Apply to offering item**, then select **OK** when prompted for confirmation.

        The offering item form opens with a banner indicating conditions have changed.

    6.  In the offering item page, save the changes.

        You must save the offering item to apply any changes made during the preview.

10. Return to the main offering page by selecting **Back** or by selecting **offering record** link in the top banner.

11. In the Providers related list, select **Edit** and select a provider from the condition builder to determine which provider instances are eligible to receive the offering.

    Adding a provider help you control which providers can subscribe to your data offerings based on specific attributes or conditions. If you don't select any provider, your offering will be available to all the connected providers.

12. Select **Publish**.


## Result

The FDS offering is now published. Providers can request foundation data based on the published FDS offering.

## What to do next

[Acknowledge foundation data sync offering request.](service-bridge-v2-con-acknowledge-fds-request.md)

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)


```


### File: service-exchange\service-bridge-v2-create-remote-choice-fld-defs.md

```text
---
title: Create remote choice definitions in Service Exchange for Providers
description: As a provider, define remote choice fields that allow consumers to retrieve choice data from their instances in real time.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create remote choice definitions in Service Exchange for Providers

As a provider, define remote choice fields that allow consumers to retrieve choice data from their instances in real time.

## Before you begin

-   Role required for creating a Remote Choice Definition: security\_admin
-   Role required for creating Remote Choice fields: admin

## Procedure

1.  Elevate your role to security\_admin.

2.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Choice Definitions**.

3.  Click **New**.

4.  On the form, fill in the fields.

<table id="table_r2f_zkw_d5b"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Table

</td><td>

Name of the table that's available to your consumers to query for while they are selecting a catalog item on their service portal.

</td></tr><tr><td>

Name

</td><td>

Auto-assigned name that can be changed by an user with the `security_admin` role.

</td></tr><tr><td>

GlideRecordSecure

</td><td>

When this option is selected, all queries for this table follow the access control list \(ACL\) restrictions. When this option isn’t selected:-   Queries for this table ignore all ACL restrictions.
-   Reference qualifier conditions must be specified for each remote choice variable to limit data access.


</td></tr><tr><td>

AccountSecure

</td><td>

When this option is selected, all queries for this table limit the results that are based on the querying service account's **Company** field and the table's **Company** or **Account** field. **Note:** This flag is available only on the tables with references to the company or account where the field is named account, u\_account, company, or u\_company.

</td></tr><tr><td>

Short description

</td><td>

Additional information about the table.

</td></tr><tr><td>

Filter

</td><td>

Filter conditions that define the base conditions on the table.

</td></tr></tbody>
</table>5.  Click **Save**.

6.  Navigate to **Service Exchange Providers** &gt; **Administration** &gt; **Remote Catalog Items**.

7.  Select a remote record producer and click **Edit**.

8.  In the Variables related list, click **New**.

9.  On the form, fill in the fields.

<table id="table_b2w_2dk_dvb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Record producer table

</td><td>

Auto-selected table that appears when you select the field. This table can be selected manually if it isn't mapped to a field.

</td></tr><tr><td>

Type

</td><td>

Reference type.

</td></tr><tr><td>

Remote choice enabled

</td><td>

Option that you can select for a remote choice.

</td></tr><tr><td>

Catalog item

</td><td>

Name of the remote record producer.

</td></tr><tr><td>

Question

</td><td>

Questions that appear in a catalog record on your consumer's service portal.

</td></tr><tr><td>

Type Specifications

</td><td>

-   **Remote choice reference** that includes the remote choice definition that you use for consumer queries for this variable.
-   **Remote choice display** field that includes the primary data value that appears to your consumers in their querying results.
-   **Remote choice additional info** field that includes the secondary data value that appears to your consumers in their querying results.
-   **Remote choice dependent on** field is a variable that this remote choice variable depends on.
-   **Reference qualifier condition** that includes the filter options that you define to limit the data that is returned by the definition.


</td></tr></tbody>
</table>10. Click **Submit**.


## Result

A remote choice variable is created.


```


### File: service-exchange\service-bridge-v2-create-remote-rec-prod.md

```text
---
title: Create a remote record producers in a remote catalog in Service Exchange for Providers
description: Create remote record producers as part of creating a Remote Catalog in Service Exchange for Providers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a remote record producers in a remote catalog in Service Exchange for Providers

Create remote record producers as part of creating a Remote Catalog in Service Exchange for Providers.

## Before you begin

-   Ensure that the catalog scope is set to Global.
-   Role required: admin, sn\_sb.admin

**Note:** Users without the admin role must be granted a catalog admin role to modify and publish remote record producers.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Catalog Items**.

2.  Click **New**.

3.  On the form, fill in the fields.

<table id="table_uzj_fds_jmb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the remote record producer.

</td></tr><tr><td>

Application

</td><td>

This is a read only field and is set by default based on the application scope.

</td></tr><tr><td>

State

</td><td>

Shows the status of the remote record producer. When you create a remote record producer, this field is set to the **Draft** state. **Note:** This field is automatically updated when you Publish, Archive, or Retire a remote record producer.

</td></tr><tr><td>

Table name

</td><td>

Table name is Provider Task. This is a read only field.

</td></tr><tr><td>

Flow

</td><td>

Choose one of the default Service Exchange flows provided or create your own flow if required.

</td></tr><tr><td>

Active

</td><td>

This is a read only field and is enabled based on the Publish, Retire, Archive, or Delete actions.

</td></tr><tr><td>

Persona

</td><td>

Catalog personas that you want to assign to this record producer.

</td></tr><tr><td>

Compatibility

</td><td>

This field is populated by default. It shows the Service Exchange version that is being used by the provider. If the consumer is using a compatible Service Exchange version, data can be synced between the provider and consumer instances. But if the consumer is not using a compatible version, any new entitlements cannot be activated until the corresponding Service Exchange version is upgraded.

</td></tr><tr><td>

Short Description

</td><td>

Short description for the record producer.

</td></tr><tr><td>

Description

</td><td>

Detailed description for the record producer.

</td></tr></tbody>
</table>4.  Click the link next to the Icon field to attach a picture.

5.  Click the link next to the Picture field to attach a picture.

    **Note:** You can also delete the picture if it is no longer required.

6.  Click **Submit**.

7.  Add at least one variable.

    See [Create variables for remote record producers in Service Exchange for Providers](service-bridge-v2-assign-variables-ser-defn.md).

8.  Add a consumer criteria.

9.  Click **Publish** to publish the remote record producer and make it available in the provider and consumer instances.


## What to do next

You can create multiple configuration revisions of this published remote record producer. For details on how to create a configuration revision, see [Create configuration revisions](../concept/service-bridge-v2-create-config-rev.md). You can also perform the following operations:

-   Archive a configuration revision: See [Archive a configuration revision](../concept/service-bridge-v2-create-config-rev.md#section_zjw_2qc_sbc)
-   Copy a configuration revision: See [Copy a configuration revision](../concept/service-bridge-v2-create-config-rev.md#section_gst_43n_tbc).
-   Retire a configuration: [Retire a configuration](../concept/service-bridge-v2-create-config-rev.md#section_x1w_dqc_sbc).
-   Delete a configuration: See [Delete a configuration](../concept/service-bridge-v2-create-config-rev.md#section_igy_2jn_tbc).


```


### File: service-exchange\service-bridge-v2-create-remote-task-flow-desig.md

```text
---
title: Create a remote task using Workflow Studio in Service Exchange for Providers
description: As a provider, proactively create remote tasks for your customers by using Workflow Studio.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a remote task definition, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a remote task using Workflow Studio in Service Exchange for Providers

As a provider, proactively create remote tasks for your customers by using Workflow Studio.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Flow Designer**.

2.  On the Flow Designer landing page's main header, select **New** &gt; **Flow**.

3.  In the Flow properties window, fill in the following fields.

    |Field|Action|
    |-----|------|
    |Flow name|Enter the name of your flow|
    |Description|Description of your flow|
    |Application|Global|
    |Domain|Global|
    |Protection|None|
    |Run As|System User|

4.  Under the TRIGGER section, select **Add a trigger**.

5.  In the Trigger section, fill in the following fields and click **Done**.

    |Field|Value|
    |-----|-----|
    |Trigger|`Created or Updated`.|
    |Table|Table name that you want to create for your consumer. For example, a Case \[sn\_customerservice\_case\].|
    |Condition|Details of the filter. For example, `Account` is `consumer-name`.|
    |Run Trigger|For every update|

    **Note:** For Advanced Option fields, don't change any values.

6.  Under the ACTIONS section, select **Add an Action, Flow Logic, or Subflow**.

7.  Click **Action** &gt; **Service Exchange for Providers** &gt; **Create remote task for Consumer**.

8.  Fill in the following fields.

    |Field|Value|
    |-----|-----|
    |Action|**Create remote task for Consumer**|
    |Task record \[Task\]|**Trigger - Record Created or Updated - Record**|
    |Remote task def record|Select the remote task definition from the list.|

9.  Select **Done** and click **Save**.


## Result

A remote task is created on your \(provider\) ServiceNow instance and it gets synchronized on the consumer's ServiceNow instance.


```


### File: service-exchange\service-bridge-v2-create-remote-tasks-defs.md

```text
---
title: Create a remote task definition in Service Exchange for Providers
description: As a provider, create remote task definitions \(RTD\) that trigger the assignment of a remote task.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 9
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a remote task definition in Service Exchange for Providers

As a provider, create remote task definitions \(RTD\) that trigger the assignment of a remote task.

## Before you begin

Role required: admin

## About this task

Before you can create a remote task, you must first create an RTD. A remote task is generated based on the RTD you define. To learn more about how RTD and remote task works, see [Remote tasks](../concept/service-bridge-v2-remote-task-overview.md).

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Task Definitions**.

2.  Select **New**.

3.  On the form, fill in the fields.

<table id="table_r2f_zkw_d5b"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the remote task definition record.

</td></tr><tr><td>

Application

</td><td>

This is a read-only field and is set by default based on the application scope.

</td></tr><tr><td>

State

</td><td>

Shows the status of the remote task definition. When you create a remote task definition, this field is set to the **Draft** state. **Note:** This field is automatically updated when you Publish, Archive, or Retire a remote task definition.

</td></tr><tr><td>

Provider table

</td><td>

Any task table that you select from the list. For example, you can choose a case table or an incident table.

</td></tr><tr><td>

Consumer table

</td><td>

Any task table that you select from the list. For example, you can choose a case table or an incident table.

</td></tr><tr><td>

Compatibility

</td><td>

This field is populated by default. It shows the Service Exchange version that is being used by the provider. If the consumer is using a compatible Service Exchange version, data can be synced between the provider and consumer instances. But if the consumer isn’t using a compatible version, any new remote task definitions can’t be activated until the corresponding Service Exchange version is upgraded.

</td></tr><tr><td>

Send attachments

</td><td>

If this check box is selected, if an attachment is added on the parent record, it’s sent to the remote task.**Note:** When data, such as an attachment or task, is shared with another instance through Service Exchange, it becomes part of that instance’s data. Service Exchange does not delete data on remote instances; the receiving instance must handle the deletion if required.

</td></tr><tr><td>

Short description

</td><td>

Brief information about this remote task definition.

</td></tr><tr><td>

Description

</td><td>

More detailed information about this remote task definition.

</td></tr></tbody>
</table>4.  Select **Submit**.

5.  Open this new Remote task definition record.

6.  On the **Inbound fields** related tab, select **New**.

    Starting from Service Exchange version 2.2.x, an inbound field record is created with the source and target fields set as comments. This record enables comment-to-comment mappings for your RTD.

7.  On the form, fill in the fields.

    The inbound fields enable you to receive data from the consumer's instance when a remote task is created or updated.

    **Note:** If the inbound field values are updated, the updated information is shown in a work note on the parent record.

<table id="table_lkx_vzd_25b"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Field label

</td><td>

Field label that appears on the remote task form.

</td></tr><tr><td>

Field name

</td><td>

Field name that is used in the remote task flow and script.

</td></tr><tr><td>

Max length

</td><td>

Maximum length of the source field name.

</td></tr><tr><td>

Sync when

</td><td>

Enables you to specify when a target field on the remote task's parent record is directly updated. You can select:-   **Insert:** Updates the target field on the remote task's parent record only when the remote task is initially inserted.
-   **Insert or Update**: Updates the target field on the remote task's parent record every time the remote task is updated.
-   **Never**: The inbound field never updates a target field on the remote task's parent record directly. For example, you can use this field for state mapping where a flow is used to convert the incoming value before updating the target field.
**Note:** Irrespective of the option you select here, whenever an inbound field is updated, the changes are reflected in a worknote on parent record.

</td></tr><tr><td>

Source Mapping tab

</td><td>

This tab is not displayed if you have selected the **Virtual** check box to define a virtual field mapping.

</td></tr><tr><td>

Source table \(read-only\)

</td><td>

The Consumer table that you selected while creating the remote task definition.

</td></tr><tr><td>

Source field

</td><td>

Field from the source table that is sent to another ServiceNow instance.Source fields allow for [Dot-walking to data in related tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_DotWalking.md), which is useful when reference data is not available between ServiceNow instances. For example, you can create multiple inbound mappings for change incidents \(CIs\) to include the name, class, IP address, and asset tag.

</td></tr><tr><td>

Target Mapping tab

</td><td>

Displayed only in the following conditions:-   Sync when: You select **Insert** or **Insert or update**.
-   Virtual: You select this check box to enable virtual field mapping.


</td></tr><tr><td>

Target table \(read-only\)

</td><td>

The Provider table that you selected while creating the remote task definition.

</td></tr><tr><td>

Target field

</td><td>

Field from the target table that is sent to another ServiceNow instance.**Note:** If you are defining a virtual field mapping, the field you select in the target table is not present in the source table.

</td></tr><tr><td>

Active

</td><td>

This field is enabled by default.

</td></tr><tr><td>

Virtual

</td><td>

Select this check box to enable virtual inbound field mapping. A virtual field is a field that is present in the target table but does not exist in the source table.

 When a source table doesn’t contain a field that exists on a target table, the field is configured as a virtual field. The values specified for the virtual field are passed from the source instance to the target instance. The consumer can create a remote task to sync data and update the value of the virtual field in the associated target task record.

 The target field can be updated either by using the Virtual Inbound option described in the [Create a transform in Service Exchange](service-bridge-v2-create-transform.md) or by using the `updateVirtualField` API.

</td></tr></tbody>
</table>8.  Click **Submit**.

9.  On the **Outbound fields** related tab, click **New**.

    Starting from Service Exchange version 2.2.x, an outbound field record is created with the source and target fields set as comments. This record enables comment-to-comment mappings for your RTD.

10. On the form, fill in the fields.

    The outbound fields enable you to send data to the consumer's instance when a remote task is created or updated.

<table id="table_jfg_wzd_25b"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Field label

</td><td>

Name of the field label that appears on the remote task form.

</td></tr><tr><td>

Field name

</td><td>

Field name that is used in the remote task flow and script.

</td></tr><tr><td>

Max length

</td><td>

Maximum length of the field name.

</td></tr><tr><td>

Sync when suggestion

</td><td>

Enables you \(the provider\) to suggest to the consumer when a target field on the remote task's parent record should be directly updated. The consumer can change this setting before activating the definition-   **Insert:** Updates the target field on the remote task's parent record only when the remote task is initially inserted.
-   **Insert or Update**: Updates the target field on the remote task's parent record every time the remote task is updated.
-   **Never**: The inbound field never updates a target field on the remote task's parent record directly. For example, you can use this field for state mapping where a flow is used to convert the incoming value before updating the target field.


</td></tr><tr><td>

Sync pre-existing entries

</td><td>

Option to enable synchronization of all existing comments to the target task when a connection is established. If enabled, any comments made prior to the connection gets included in the sync process when a remote task is created.**Note:** This feature is available from Service Exchange version 2.2.x.

</td></tr><tr><td>

Source Mapping tab

</td><td>

This tab is not displayed if you have selected the **Virtual** check box to define a virtual field mapping.

</td></tr><tr><td>

Source table \(read-only\)

</td><td>

The Provider table that you selected while creating the remote task definition.

</td></tr><tr><td>

Source field

</td><td>

Field from the source table that is sent to another ServiceNow instance.Source fields allow for [Dot-walking to data in related tables](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-user-interface/c_DotWalking.md), which is useful when reference data is not available between ServiceNow instances. For example, you can create multiple inbound mappings for change incidents \(CIs\) to include the name, class, IP address, and asset tag.

 **Note:** From Service Exchange version 2.2.x, you can create

</td></tr><tr><td>

Target Mapping tab

</td><td>

Displayed only in the following conditions:-   Sync when: You select **Insert** or **Insert or update**.
-   Virtual: You select this check box to enable virtual field mapping.


</td></tr><tr><td>

Target table \(read-only\)

</td><td>

The Consumer table that you selected while creating the remote task definition.

</td></tr><tr><td>

Target field

</td><td>

Field from the target table that is sent to another ServiceNow instance.**Note:** If you are defining a virtual field mapping, the field you select in the target table is not present in the source table.

</td></tr><tr><td>

Active

</td><td>

This field is enabled by default.

</td></tr><tr><td>

Virtual

</td><td>

Select this check box to enable virtual inbound field mapping. A virtual field is a field that is present in the target table but does not exist in the source table.

 When a source table doesn’t contain a field that exists on a target table, the field is configured as a virtual field. The values specified for the virtual field are passed from the source instance to the target instance.

 The target field can be updated either by using the Virtual Outbound option described in the [Create a transform in Service Exchange](service-bridge-v2-create-transform.md) or by using the `updateVirtualField API`.

</td></tr></tbody>
</table>11. Click **Submit**.

12. On the **Consumer criteria** related tab, click **New**.

13. On the form, fill in the fields.

    Consumer criteria enable you to manage which consumers can use these remote task definitions.

    |Field|Description|
    |-----|-----------|
    |Consumer condition|Customer company or account that you want this remote task definition to be entitled to.|
    |Remote task definition|Name of this remote task definition record. This name is auto-filled.|

    For more details on consumer criteria, see [Creating entitlements in Service Exchange for Providers](../concept/service-bridge-v2-entitlements.md).

14. Click **Publish**.

    Remote task variables are automatically created when you publish a remote task definition. These variables are the data variables for the inbound fields displayed and can be accessed on the remote tasks.


## Result

A remote task definition record is created on your instance. This record is also synchronized with your customer's instance and is now pending activation on your consumer's instance. If the **Auto activate remote task definition** field has been enabled by the consumer, the remote task definition is automatically activated on your consumer's instance.

## What to do next

You can create multiple configuration revisions of this published remote task definition. For details on how to create a configuration revision, see [Create configuration revisions](../concept/service-bridge-v2-create-config-rev.md). You can also perform the following operations:

-   Archive a configuration revision: See [Archive a configuration revision](../concept/service-bridge-v2-create-config-rev.md#section_zjw_2qc_sbc)
-   Copy a configuration revision: See [Copy a configuration revision](../concept/service-bridge-v2-create-config-rev.md#section_gst_43n_tbc).
-   Retire a configuration: [Retire a configuration](../concept/service-bridge-v2-create-config-rev.md#section_x1w_dqc_sbc).
-   Delete a configuration: See [Delete a configuration](../concept/service-bridge-v2-create-config-rev.md#section_igy_2jn_tbc).

**Related topics**  


[Remote tasks](../concept/service-bridge-v2-remote-task-overview.md)


```


### File: service-exchange\service-bridge-v2-create-transform.md

```text
---
title: Create a transform in Service Exchange
description: As a provider or a consumer, create a transform in Service Exchange to integrate tasks between connected instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a transform in Service Exchange

As a provider or a consumer, create a transform in Service Exchange to integrate tasks between connected instances.

## Before you begin

Role required: admin

## About this task

The following steps describe the transform process for providers. Consumers can navigate to **All** &gt; **Service Exchange Consumer** &gt; **Transforms** and follow the same process.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Transforms**.

2.  Click **New**.

3.  On the form, fill in the fields.

<table id="table_r2f_zkw_d5b"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Number

</td><td>

Auto-generated number for the transform record.

</td></tr><tr><td>

Company

</td><td>

Consumer name for whom this transform is applicable.

</td></tr><tr><td>

All Companies

</td><td>

If this is selected, the transform runs for all companies except those with the same company level transform.

 Use this field to create a default transform definition that can be applied to all companies. The All companies field eliminates the need to define a specific transform for each customer account even when they have similar requirements. You can use the default definition to transform specific fields across all companies simultaneously.

 The global transform is applied only to companies that match the configuration and do not have a specific transform already defined. If a company specific transform for the same configuration already exists, this will override the global transform.

</td></tr><tr><td>

Type

</td><td>

-   **Simple**: Used when the field has a known and stable choice list on each instance. A related list of transform lines is created to match the inbound and outbound values.
-   **Advanced**: Used for complex criteria that requires a script to determine the new value.
-   **Virtual Inbound**: Used to transform a virtual inbound field. Requires a script to determine the new value.
-   **Virtual Outbound**: Used to transform a virtual outbound field. Requires a script to determine the new value.


</td></tr><tr><td>

Inbound

</td><td>

Option that enables an inbound transformation for this transform. This option is available only if you select the Type as Simple or Advanced.

</td></tr><tr><td>

Outbound

</td><td>

Option that enables an outbound transformation for this transform. This option is available only if you select the Type as Simple or Advanced.

</td></tr><tr><td>

Provider table

</td><td>

Option that designates the provider's task table. For example, Case.

</td></tr><tr><td>

Consumer table

</td><td>

Option that designates the consumer's task table. For example, Incident.

</td></tr><tr><td>

Provider field

</td><td>

Option that designates the provider's field. For example, State. This field is available only if you select the Type as Simple or Advanced.

</td></tr><tr><td>

Consumer field

</td><td>

Option that designates the consumer's field. For example, **State**. This field is available only if you select the Type as Simple or Advanced.

</td></tr><tr><td>

Virtual field

</td><td>

When Type field is set to **Virtual Inbound** or **Virtual Outbound**, this field is available to reference the virtual field this transform should populate.

</td></tr></tbody>
</table>4.  Click **Save**.

5.  Select one of the following:

    1.  **Simple:** Click **New** in the Transform lines related list, and fill in the fields on the form.

        |Field|Description|
        |-----|-----------|
        |Provider label|Option that designates the provider's choice label. For example, Open.|
        |Provider value|Option that designates the provider's choice value. For example, 10.|
        |Customer label|Option that designates the customer's choice label. For example, Progress.|
        |Customer value|Option that designates the customer's choice value. For example, 2.|

        **Note:** You can generate transform mappings between provider and consumer tables automatically using the Transform Mapping Assist feature. For more information, see [Automate transforms with Now Assist for TMT](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/telecom-media-technology/now-assist-for-telecom-media-and-technology/now-assist-tmt-generate-transform-maps.md).

    2.  **Advanced**: Use a script to define the outbound and inbound labels and values as shown in the following example:

        ```
        output.value=input.value;
        output.label=input.label;
        
        var ci=new GlideRecord('cmdb_ci');
        
        if(direction=='inbound'){
           if(ci.get('correlation_id',input.value)){
              output.value=ci.sys_id+";
              output.label=ci.getDisplayValue();
              }
        }
        if (direction=='outbound'){
          if(ci.get(input.value)){
             if(ci.correlation_id){
                output.value=ci.correlation_id+";
                output.label=input.label;
               }
            }
        }
              
        
        ```

    3.  **Virtual Inbound**: Use a script to determine the inbound label and value as shown in the following example:

        ```
        var inputArr = input.value.split(',');
        var outputValues = [];
        var outputLabels = [];
        for (i in inputArr) {
            getInstanceID(inputArr[i]);
        }
        output.value = outputValues+'';
        output.label = outputLabels+'';
        
        function getInstanceID(name) {
            var gr = new GlideRecord('cmdb_ci_server');
            if (gr.get('name', name)) {
                outputValues.push(gr.sys_id+'');
                outputLabels.push(name);
            }
        }
        ```

    4.  **Virtual Outbound**: Use a script to determine the outbound label and value as shown in the following example:

        ```
        /*
         ** The 'input' object contains the original value and label
         ** 'direction' contains an 'inbound' or 'outbound' value to determine transform direction
         ** 'object_data' contains the Remote Task GlideRecord
         ** It is required to set the variables 'output.value' and 'output.label' with your script.
         */
        output.value = 'condev,conprod';
        output.label = 'condev,conprod';
        ```

6.  Click **Submit**.

7.  On the transform form, click **Activate**.


## Result

A transform record is created on your ServiceNow® instance. Any Remote Task's inbound or outbound fields that match a transform will automatically use them. To learn more, see [Create a remote task definition in Service Exchange for Providers](service-bridge-v2-create-remote-tasks-defs.md).


```


### File: service-exchange\service-bridge-v2-create-variable-sets.md

```text
---
title: Create a variable set in Service Exchange for remote record producers
description: Create variable sets for a remote record producer in Service Exchange for Providers application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create a variable set in Service Exchange for remote record producers

Create variable sets for a remote record producer in Service Exchange for Providers application.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Remote Catalog Items**.

2.  Click a record producer that you want to create variables for.

3.  Click the **Variable Sets** tab in the Related List and then click **New**.

4.  Select one of the following:

    -   Single-Row Variable Set: Creates a variable set with variables that are grouped together. Type field is set to `Single Row`.
    -   Multi-Row Variable Set: Creates a variable set with multiple rows that captures variable data in a grid layout. Type field is set to `Multi Row`.
5.  Fill in the fields on the form.

<table id="table_c2q_s1c_xq"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Title

</td><td>

Title of a variable set.

</td></tr><tr><td>

Internal name

</td><td>

Variable set name for internal use. If this field is left blank, it is auto-populated based on the Title field.

</td></tr><tr><td>

Order

</td><td>

Order number for the variable set.

</td></tr><tr><td>

Type

</td><td>

Type of the variable set. Possible choices are:-   Single Row
-   Multi Row


</td></tr><tr><td>

Application

</td><td>

Applications that can use this variable set.

</td></tr><tr><td>

Display title

</td><td>

If selected, adds a title and an expandable header to the right of the variable set.

</td></tr><tr><td>

Variable Set attributes

</td><td>

Attributes for configuring a multi-row variable set. Use the **max\_rows** attribute to set a limit to the number of rows that you can add to a multi-row variable set. For example, specify `max_rows=1` as the field value.

</td></tr><tr><td>

Layout

</td><td>

The layout display. Set to **1 Column Wide** or **2 Columns Wide, alternating sides** or **2 Columns Wide, one side, then the other**.

</td></tr><tr><td>

Description

</td><td>

Description of the variable set.

</td></tr></tbody>
</table>6.  Right-click and select **Save**.

7.  Create the variables to use in that set.

    1.  In the Variables related list, click **New**.

    2.  Follow the steps listed in [Create variables for remote record producers in Service Exchange for Providers](service-bridge-v2-assign-variables-ser-defn.md) to create variables.

        **Note:** For a multi-row variable set:

        -   The included variables are displayed as columns of a table.
        -   The column order is the order of variables defined in the variable set.
8.  Click **Submit**.

    Repeat the above steps to create additional variable sets for the same remote record producer.

    For more information on variable sets and the layout, see [Variable set layout](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/c_DefineVariableSetLayout.md).



```


### File: service-exchange\service-bridge-v2-customer-roles.md

```text
---
title: Personas for consumers
description: Learn about the different personas in the Service Exchange application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Personas for consumers

Learn about the different personas in the Service Exchange application.

Remote record producers can be associated with personas. If a remote record producer does not have a persona, any user with the Service Exchange Requestor role can place an order for the item. However, if one or more personas are assigned to a remote record producer, the user must have the Requestor role and at least one of the listed personas. Personas are assigned to users through the Authorized Users table. To access items protected by personas, the user's Authorized User record must be approved by the provider, activated in the consumer instance, and have the appropriate persona\(s\).

<table id="table_h2n_nkm_cmb"><thead><tr><th>

Persona

</th><th>

Skills

</th><th>

Tasks

</th><th>

Roles

</th></tr></thead><tbody><tr><td>

System administrator

</td><td>

Is a certified ServiceNow system administrator

</td><td>

-   Creates provider and connection records.
-   Installs the Service Exchange applications.
-   Creates and maintains transforms.
-   Activates published remote task definitions and remote record producers.
-   Troubleshoots Service Exchange transport payloads.

</td><td>

-   admin
-   sn\_sb.admin
-   sn\_transport.admin

</td></tr><tr><td>

Service Exchange Requester

</td><td>

Is an IT administrator

</td><td>

-   Responsible for some form of IT service that is either completely or in part supported by one or more external vendors.
-   Requests and monitors the service requests that are placed with the external provider from their own instance.

</td><td>

-   itil
-   sn\_sb.requestor

</td></tr><tr><td>

Consumer Requestor

</td><td>

End user

</td><td>

Makes requests from the Remote Catalog.

</td><td>

sn\_sb.requestor

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-data-model.md

```text
---
title: Service Exchange data model
description: The Service Exchange applications data model provides insight into how the tables that are used in Service Exchange relate to each other.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Service Exchange]
---

# Service Exchange data model

The Service Exchange applications data model provides insight into how the tables that are used in Service Exchange relate to each other.

The data model uses a combination of the following types of tables to store data:

-   Service Exchange application tables.
-   ServiceNow AI Platform standard tables.

The following table lists the Access Control Rights \(ACR\) for specific Service Exchange base table.

<table id="table_kgs_tm3_gzb"><thead><tr><th>

Table

</th><th>

Read

</th><th>

Write

</th><th>

Delete

</th><th>

Create

</th></tr></thead><tbody><tr><td>

Authorized user

 \[sn\_sb\_authorized\_user\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Connection

 \[sn\_sb\_connection\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Entitlement

 \[sn\_sb\_entitlement\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Provider Task

 \[sn\_sb\_provider\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td><td>

admin

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td></tr><tr><td>

Remote Record Producer

 \[sn\_sb\_remote\_record\_producer\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Remote Task

 \[sn\_sb\_remote\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_creator

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Scratchpad

 \[sn\_sb\_scratchpad\]

</td><td>

admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Transform

 \[sn\_sb\_transform\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Transform Line

 \[sn\_sb\_transform\_line\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-datamodel-customers.md

```text
---
title: Service Exchange for Consumers data model
description: The Service Exchange for Consumers data model provides insight into how the tables that are used in the Service Exchange for Consumers application relate to each other.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Data model, Reference, Service Exchange]
---

# Service Exchange for Consumers data model

The Service Exchange for Consumers data model provides insight into how the tables that are used in the Service Exchange for Consumers application relate to each other.

The Service Exchange for Consumers data model uses a combination of the following types of tables to store data:

-   Service Exchange for Consumers application tables.
-   Customer Service Management application tables.
-   ServiceNow AI Platform standard tables.

The following table lists the Access Control Rights \(ACR\) for specific Service Exchange for Consumer tables.

<table id="table_umg_zc4_gzb"><thead><tr><th>

Table

</th><th>

Read

</th><th>

Write

</th><th>

Delete

</th><th>

Create

</th></tr></thead><tbody><tr><td>

Authorized User

 \[sn\_sb\_con\_authorized\_user\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Consumer

 \[sn\_sb\_con\_consumer\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Entitlement

 \[sn\_sb\_con\_entitlement\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Inbound Field

 \[sn\_sb\_con\_inbound\_field\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Outbound Field

 \[sn\_sb\_con\_outbound\_field\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Persona

 \[sn\_sb\_con\_persona\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Provider Connection

 \[sn\_sb\_con\_provider\_connection\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

None

</td></tr><tr><td>

Provider Task

 \[sn\_sb\_con\_provider\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_requestor

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_requestor

</td><td>

admin

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_requestor

</td></tr><tr><td>

Remote Choice Cache

 \[sn\_sb\_con\_remote\_choice\_cache\]

</td><td>

admin

</td><td>

admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Remote Record Producer

 \[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_requestor

</td><td>

None

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td></tr><tr><td>

Remote Task

 \[sn\_sb\_con\_remote\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_remote\_task\_

 creator

</td></tr><tr><td>

Remote Task Definition

 \[sn\_sb\_con\_remote\_task\_def\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td></tr><tr><td>

Variable

 \[sn\_sb\_con\_remote\_task\_variable\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Service Exchange Settings

 \[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Remote Choice

 \[sn\_sb\_con\_st\_remote\_choice\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_requestor

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Transform

 \[sn\_sb\_con\_transform\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-datamodel-provider.md

```text
---
title: Service Exchange for Providers data model
description: The Service Exchange for Providers data model provides insight into how the tables that are used in the Service Exchange for Providers application relate to each other.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Data model, Reference, Service Exchange]
---

# Service Exchange for Providers data model

The Service Exchange for Providers data model provides insight into how the tables that are used in the Service Exchange for Providers application relate to each other.

The Service Exchange for Providers application data model uses a combination of the following types of tables to store data:

-   Service Exchange of Providers application tables.
-   Customer Service Management application tables.
-   ServiceNow AI Platform standard tables.

The following table lists the Access Control Rights \(ACR\) for specific Service Exchange for Provider tables.

<table id="table_fgp_3q3_gzb"><thead><tr><th>

Table

</th><th>

Read

</th><th>

Write

</th><th>

Delete

</th><th>

Create

</th></tr></thead><tbody><tr><td>

Authorized user

 \[sn\_sb\_pro\_authorized\_user\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Consumer Connection

 \[sn\_sb\_pro\_consumer\_connection\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Entitlement

 \[sn\_sb\_pro\_entitlement\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Inbound Field

 \[sn\_sb\_pro\_inbound\_field\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Outbound Field

 \[sn\_sb\_pro\_outbound\_field\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Persona

 \[sn\_sb\_pro\_persona\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Provider

 \[sn\_sb\_pro\_provider\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Provider Task

 \[sn\_sb\_pro\_provider\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td><td>

admin

</td><td>

admin

 sn\_sb.admin

 sn\_sb.requestor

</td></tr><tr><td>

Registration

 \[sn\_sb\_pro\_registration\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb\_pro\_consumer

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Remote Choice Definition

 \[sn\_sb\_pro\_remote\_choice\_definition\]

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Remote Record

 Producer

 \[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Consumer Criteria

 \[sn\_sn\_pro\_remote\_record\_producer\_consumer\_criteria\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Remote Service

 \[sn\_sb\_pro\_remote\_service\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Remote Task

 \[sn\_sb\_con\_remote\_task\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td></tr><tr><td>

Remote Task

 Definition

 \[sn\_sb\_con\_remote\_task\_def\]

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

 sn\_sb.remote\_task\_

 creator

</td></tr><tr><td>

Consumer Criteria

 \[sn\_sv\_pro\_remote\_task\_def\_consumer\_criteria\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr><tr><td>

Variable

 \[sn\_sb\_con\_remote\_task\_variable\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

</td><td>

admin

</td><td>

admin

</td></tr><tr><td>

Service Exchange

 Settings

 \[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

None

</td><td>

None

</td></tr><tr><td>

Transform

 \[sn\_sb\_con\_transform\]

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td><td>

admin

 sn\_sb.admin

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-domain-separation.md

```text
---
title: Domain separation and Service Exchange
description: Domain separation is supported for Service Exchange. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Service Exchange]
---

# Domain separation and Service Exchange

Domain separation is supported for Service Exchange. Domain separation enables you to separate data, processes, and administrative tasks into logical groupings called domains. You can control several aspects of this separation, including which users can see and access data.

## Support level: Basic



-   Business logic: Ensure that data goes into the proper domain for the application’s service provider use cases.
-   The application supports domain separation at run time. The domain separation includes separation from the user interface, cache keys, reporting, rollups, and aggregations.
-   The owner of the instance must set up the application to function across multiple tenants.

Sample use case: When a service provider \(SP\) uses chat to respond to a tenant-customer’s message, the customer must be able to see the SP's response.

For more information on support levels, see [Application support for domain separation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-separated-apps.md).

The Provider Task and Remote Task tables have domain separation available. When data is added to these tables, Service Exchange inserts them into the domain of the parent task if available, or the connected instance based on the associated company by default. If necessary, the instance admin can apply their own business rule to redirect the data after the Service Exchange default rule has been applied. However, this should only be done by setting a different company on the records before inserting them.

## How domain separation works in Service Exchange

-   The Provider Task and Remote Task tables in the application are domain-separated.
-   Make sure that the consumer company and account tables are associated to the right domain for the domain separation logic to work.

## Use cases

When providers have their consumer data separated by domains, the provider tasks, remote tasks, and the corresponding parent tasks are associated with the respective customer domains.

**Related topics**  


[Domain separation for service providers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/domain-sep-landing-page.md)


```


### File: service-exchange\service-bridge-v2-entitlements.md

```text
---
title: Creating entitlements in Service Exchange for Providers
description: Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Creating entitlements in Service Exchange for Providers

Using consumer criteria associated with record producers and other configurations, Service Exchange automatically generates the entitlement records that are replicated to eligible consumer instances.

Consumer Criteria records are used to entitle Service Exchange content, such as Remote Record Producers and Remote Task Definitions, to Service Exchange consumers. Consumer criteria enables you to ensure that a consumer has access only to the appropriate Service Exchange content. Using consumer criteria, you can entitle content explicitly to a single customer or to multiple customers.

A few examples of how you configure the consumer criteria are given below. For example, you can entitle content:

-   To a specific consumer.
-   To all consumers that have an active sold product of a specific model.
-   To all consumers that have an active service contract.

The Service Exchange entitlement process runs as a scheduled job each night. During the entitlement process, filters defined in the condition builder of the consumer criteria record are applied to the selected table to find records that match the condition. If a matching record is found, the associated Service Exchange content is entitled to the consumer. For example, when a consumer with an active sold product creates an order, the appropriate Service Exchange content is automatically entitled to the consumer. Entitlements are updated daily, reflecting changes if the data in the tables being queried has changed.

## Benefits

Your consumers can see and request the content entitled to them. A scheduled job runs nightly and updates the entitlements, based on any changes made to the tables or records that are queried by the consumer criteria. Additionally, entitlements are checked immediately when updates are made.

You can update Service Exchange entitlements in the following ways:

-   Define the consumer criteria in the Remote Record Producer.
-   Register a new consumer in Service Exchange.
-   Click the **Refresh Entitlements** related link in the Consumer Connections record or the Provider record.

## Define a consumer criteria

To define a consumer criteria, see [Create a consumer criteria](service-bridge-v2-create-consumer-criteria.md).


```


### File: service-exchange\service-bridge-v2-error-log.md

```text
---
title: Service Exchange error log
description: Track errors on recent transactions, provide connection status, run health checks, and provide recommendations.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Service Exchange]
---

# Service Exchange error log

Track errors on recent transactions, provide connection status, run health checks, and provide recommendations.

## About this task

**Note:** The Australia release, includes a framework to capture Service Exchange errors. Currently, the table displays the following known errors:

1.  Global Script Include check: Checks if this script has been installed and if it is the latest version.
2.  During registration for provider: Captures errors from the creation of the registration task through closed complete. An email notification with the list of errors captured in the last one hour along with the cause and solution is sent to the Service Exchange administrator.
3.  During Registration for consumer: Captures errors from the creation of the Provider Connection record through closed complete. An email notification with the list of errors captured in the last one hour along with the cause and solution is sent to the Service Exchange administrator.
4.  Remote system inbound and outbound errors
5.  Heartbeat connection

You can view and diagnose errors and follow the steps provided to resolve the errors. Errors are logged as they occur, and if there have been any new ones in the last hour, an email notification is sent to the Service Exchange administrators. Each error record provides the following details:

-   A detailed description of the error.
-   Reason the error has occurred.
-   Steps to resolve the error.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Administration** &gt; **Error Log**.

    The list of errors that have occurred is displayed.

    **Note:** You can view errors on the consumer instance. To do so, login to consumer instance, and navigate to **All** &gt; **Service Exchange Consumer** &gt; **Administration** &gt; **Error Log**.

2.  Click on the Number link to view the error.

3.  The following details are displayed.

    |Field|Description|
    |-----|-----------|
    |Number|The number assigned to the error.|
    |Known error|Detailed information about the error and how to resolve it. This information is displayed in the fields below.|
    |Error|A detailed description of the error.|
    |Cause|Reason the error has occurred. If this is not a known issue, the Cause is set to **Unknown**.|
    |Solution|A link is provided to the Knowledge Base article that contains the steps that need to be followed to resolve the error.|
    |Connection|This field is populated if the error is caused by connection issue.|
    |Created|Date and time at which the error occurred.|



```


### File: service-exchange\service-bridge-v2-explore-foundation-data-sync.md

```text
---
title: Foundation data sync
description: Foundation data sync \(FDS\) enables structured, periodic data sharing from provider to consumer and consumer to provider instances. FDS ensures that both providers and consumers can share and receive accurate, up‑to‑date foundational data, supporting better service delivery and operational alignment.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Explore, Service Exchange]
---

# Foundation data sync

Foundation data sync \(FDS\) enables structured, periodic data sharing from provider to consumer and consumer to provider instances. FDS ensures that both providers and consumers can share and receive accurate, up‑to‑date foundational data, supporting better service delivery and operational alignment.

FDS is a data synchronization mechanism that enables a provider instance to share foundational data, such as server, hardware, network information with consumer instances and consumers instance to provider instances on a scheduled cadence \(daily, weekly, or monthly\).

FDS supports two separate unidirectional data flows, allowing both providers and consumers to act as either data source or recipient depending on the business need:

-   **Consumer-bound FDS**

    Provider shares data with consumer instances.

-   **Provider-bound FDS**

    Consumer shares data with provider instances.


**Note:** These are independent flows. Each flow must be configured separately. Establishing data sharing in one direction does not automatically enable data sharing in the reverse direction.

FDS supports all CMDB CI extended tables and the following non-CMDB tables: Asset, Company, User, Group, Location, Department, Stockroom, Product Model, Knowledge, Hardware Model, Consumable Model, Hardware, and Consumable. If you need support for any additional table, contact Support.

## Benefits of FDS

FDS supports the service life cycle by enabling providers to share foundational data with consumers in a structured, automated way. This data transfer provides the essential context for operational workflows, reduces manual effort, and eliminates the need to exchange data through external channels.

## FDS data flow scenarios

FDS provides two ways to collaborate by sharing date in either direction:

-   **Consumer-bound FDS \(Provider shares data\)**

    The provider creates FDS offering definitions and publishes them to make data available. Consumers browse available offerings and request the data they need. After validation and acceptance, data flows from the provider instance to the consumer instance on the defined schedule.

    The provider controls which tables, fields, and records are shared. Consumers configure how the incoming data maps to their instance tables.

    **Note:** Consumer-bound FDS \(Provider shares data\) is supported from Service Exchange version 2.2.x.

-   **Provider-bound FDS \(Consumer shares data\)**

    The consumer creates FDS offering definitions and publishes them to make data available. Providers browse available offerings and request the data they need. After validation and acceptance, data flows from the consumer instance to the provider instance on the defined schedule.

    The consumer controls which tables, fields, and records are shared. Providers configure how the incoming data maps to their instance tables.

    **Note:** Provider-bound FDS \(Consumer shares data\) is supported from Service Exchange version 2.3.x.


## Use Case Example

A telecom provider, XYZ company, does not own or manage its own servers. Instead, it relies on a third-party infrastructure provider, ABC company. ABC maintains the configuration data for the servers, including hardware specifications and network dependencies.

XYZ needs this data to assign users to the correct servers based on bandwidth requirements. FDS enables ABC to push this data to XYZ regularly, ensuring XYZ has the information it requires to deliver reliable services.

In this scenario, ABC is the provider, XYZ is the consumer, and the data flows from ABC to XYZ.

ABC company also needs visibility into XYZ to understand the consumption pattern. To enable ABC to provide better infrastructure support, XYZ needs to share data back to ABC. FDS enables XYZ company to share usage data with ABC regularly, enabling ABC to make informed decisions about capacity planning and infrastructure optimization.

**Related topics**  


[Configuring outbound foundation data sync as providers](service-bridge-v2-using-foundation-data-sync.md)

[Configuring inbound foundation data sync as providers](service-bridge-v2-configure-inboun-fds-providers.md)

[Configuring inbound foundation data sync as a consumer](service-bridge-v2-using-foundation-data-sync-for-consumer.md)

[Configuring outbound foundation data sync as consumers](using-provider-bound-fds-consumer.md)


```


### File: service-exchange\service-bridge-v2-explore-magic-link.md

```text
---
title: Magic links
description: Magic links enable seamless authentication from a consumer instance to a provider instance in Service Exchange, enabling consumers to access shared resources without manual login. This mechanism supports both per-user and single-user login modes and is particularly useful for HR tasks, catalog submissions, and knowledge base access.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Magic links

Magic links enable seamless authentication from a consumer instance to a provider instance in Service Exchange, enabling consumers to access shared resources without manual login. This mechanism supports both per-user and single-user login modes and is particularly useful for HR tasks, catalog submissions, and knowledge base access.

**Related topics**  


[Enable magic links](../task/service-bridge-v2-magic-links.md)


```


### File: service-exchange\service-bridge-v2-exploring-service-bridge.md

```text
---
title: Exploring Service Exchange
description: Service Exchange helps providers, consumers, and partners connect their ServiceNow instances to build secure business workflows across the ServiceNow ecosystem.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Service Exchange]
---

# Exploring Service Exchange

Service Exchange helps providers, consumers, and partners connect their ServiceNow instances to build secure business workflows across the ServiceNow ecosystem.

## Service Exchange overview

Service Exchange connects multiple ServiceNow instances to provide seamless support and service experiences across the ecosystem, from enterprise customers to suppliers and system integrators. Service Exchange provides a frictionless experience that makes it easy to collaborate and process requests while giving users the convenience of working in their own ServiceNow instance.

Watch this short video for an introduction to the Service Exchange application.An overview of Service Exchange 

Service Exchange has two components or applications:

-   Provider application: An application that enables the service provider to deliver a streamlined and comprehensive solution for managing their service offerings.
-   Consumer application: An application that enables consumers to interact and collaborate with service providers.

## Service Exchange workflow

Service Exchange enables providers to integrate their ServiceNow instances with their customers and partners seamlessly.

![Infographic showing how Service Exchange connects various ServiceNow instances.](../image/service-bridge-v2-explore-sb-lp.svg)

1.  -   **Service Exchange establishes the connection**

    The provider initiates a registration task using Service Exchange to establish a secure, bi-directional connection between multiple instances to enable better collaboration. All necessary instances such as enterprise or partner instances are connected using Service Exchange.

2.  -   **Enterprise initiates a request**

    The workflow begins with the enterprise, also known as the consumer, accessing catalog items that have been published by the provider. These catalog items are integrated into the enterprise’s ServiceNow instance. The enterprise user submits a request for one of these items and a task is created in the consumer instance. This task is then synchronized with the provider’s instance, enabling the provider to fulfill the request while the consumer retains visibility into its progress.

3.  -   **Provider executes and manages services**

    After the connection between the provider and consumer is established, the provider takes charge of delivering and managing the requested services that involves setting up remote tasks, which are mirrored between the provider and consumer instances to support collaborative work. In addition, provider tasks are created to give the consumer visibility into the progress of the request, although the consumer doesn’t participate in fulfilling these tasks. The provider can also initiate proactive cases, which automatically generate provider tasks in the consumer’s instance when specific alerts or conditions are met, enabling timely communication and action.

4.  -   **Partner supports fulfillment**

    The provider can delegate specific tasks to its fulfillment partners. These partners operate within the same Service Exchange infrastructure and receive tasks that are tracked and updated in real-time. This mechanism promotes transparency and continuity across all parties involved in the service delivery process.


Service Exchange promotes real-time collaboration by keeping all connected instances updated with the latest changes, comments, and status updates. These updates are synchronized based on the configured settings, enabling both providers and consumers to stay aligned throughout the service process. This continuous flow of information improves collaboration, enhances transparency, and maintains a secure exchange of data between ServiceNow instances.

## Service Exchange benefits

|Feature|Benefit|
|-------|-------|
|[Mismatched versions](service-bridge-v2-mismatch-version.md)|Run provider and consumer instances on different platform releases and application versions without disrupting the active entitlements or processes.|
|[Configuration revisions](service-bridge-v2-config-revision.md)|Edit or create revisions of entitlements such as remote tasks, remote catalogs, with updated functionality, and deploy them to consumers.|
|[Remote catalog](service-bridge-v2-create-apps.md)|Keep the development of shared catalogs and the workflows/integrations in the provider instance while sharing them with consumers as simple record producers that generate integrated requests in the provider instance.|
|[Proactive cases](service-bridge-v2-proactive-case.md)|Collaborate and foster transparency with your customers by sending Provider Tasks to the consumer instance.|
|[Provider task](service-bridge-v2-provider-tasks.md)|Send case alerts proactively from the provider task table to connected consumers without additional setup or configuration to promote transparency and collaboration.|
|[Remote task](service-bridge-v2-remote-task-overview.md)|Use remote task as a sustainable alternative to custom eBonding to create linked tasks across multiple instances without building an integration. A remote task transmits comments, attachments, and mapped fields between instances, enabling better business workflows.|
|[ScratchPad](service-bridge-v2-scratchpad-consumer.md)|Share name-value pairs as JSON data on provider tasks and remote tasks to enable structured data exchange between instances.|
|[Foundation data sync](service-bridge-v2-explore-foundation-data-sync.md)|Share selected foundational data types with your consumers on a scheduled cadence to reduce manual effort, and eliminate the need to share data externally.|
|[Journal field framework](service-bridge-v2-expolre-journal-field-framework.md)|Map and synchronize journal-type fields between provider and consumer instances to keep critical operational updates current. It also maintains historical continuity by synchronizing previous journal entries, and enhances authenticity and accountability by writing journal entries as a named user rather than using a generic company name.|
|[Flow action](service-bridge-v2-flow-action.md)|Ensure that remote tasks and remote record producers continue to function correctly as you adopt newer revisions by maintaining flow compatibility across configuration updates using four new Flow Actions that preserve mapped variable integrity.|
|[Magic link](service-bridge-v2-explore-magic-link.md)|Convert regular links sent from a provider instance into magic links that enable consumer users to access the linked resource directly in the provider instance without having to log in manually.|

## Applications

<table id="table_jyd_yjw_ffc"><thead><tr><th>

Application

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Provider

</td><td>

This application enables the provider to deliver services and support to consumers.-   Create and publish remote catalogs from your instance for consumers to generate service requests that can be fulfilled in your instance.
-   Integrate your tasks bidirectionally with your consumer's tasks.
-   Send incidents and cases to your consumer's ServiceNow instance via Provider Task with no setup needed.

</td></tr><tr><td>

Consumer

</td><td>

This application enables the consumer to receive services and support from providers.-   Incorporate remote catalog items assigned to you from your provider into your local catalog and send the requests generated back to your provider for fulfillment.
-   Bidirectionally integrate your tasks with your provider's tasks.
-   Receive proactive tasks from providers to enhance transparency and collaboration.

</td></tr></tbody>
</table>## Service Exchange users

|Application|User|Description|
|-----------|----|-----------|
|Provider|Administrator|The provider administrator is responsible for setting up and maintaining the technical components of Service Exchange. This includes establishing connections, configuring Workflow Studio flows, and publishing service content to consumer instances. They also support registration and troubleshoot integration issues to promote smooth and secure collaboration between provider and consumer instances.|
|Provider|Provider Fulfiller/Agent|The fulfiller/agent is responsible for resolving consumer questions and issues, and may also engage in network operations when needed to support service delivery.|
|Provider|Consumer|The consumer is responsible for consumer registration tasks.|
|Consumer|Administrator|The consumer administrator is responsible for setting up and managing the Service Exchange connection from the consumer side. This includes installing the Service Exchange applications, creating provider and connection records, maintaining transforms, and troubleshooting transport payloads to promote smooth and reliable integration with the provider instance.|
|Consumer|Fulfiller/Agent|The consumer agent is responsible for managing IT services that rely partly or entirely on external providers. They place and track service requests with the provider from within their own instance, promoting that issues are addressed and services are delivered as expected.|
|Consumer|Requester|The requester is responsible for making requests from the remote catalog.|

## What to explore next

-   [Service Exchange for Providers](service-bridge-providers-landing-page.md)
-   [Service Exchange for Consumers](service-bridge-consumers-landing-page.md)
-   [Service Exchange reference](../reference/service-bridge-v2-reference.md)


```


### File: service-exchange\service-bridge-v2-expolre-journal-field-framework.md

```text
---
title: Journal field frameworks
description: The Journal Field Framework \(JFF\) enables real-time synchronization of journal type fields, such as comments and work notes, between provider and consumer.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Explore, Service Exchange]
---

# Journal field frameworks

The Journal Field Framework \(JFF\) enables real-time synchronization of journal type fields, such as comments and work notes, between provider and consumer.

JFF also enhances operational transparency, preserves historical context, and verifies that updates are attributed to actual users for greater transparency.

The synchronization of journal type fields between consumer and provider instances is enabled through a Remote Task Definition \(RTD\) configured with compatibility version 2.2.x or later.

With JFF, you can do the following:

-   **Journal field mapping**

    Map and synchronize any journal type fields between provider and consumer instances based on the **Inbound** and **Outbound** field configurations in a remote task definition.

    For example, while creating an RTD, you can create mappings such as:

    -   Comments to work notes
    -   Work notes to comments
    When a remote task is created based on the RTD, these mapped journal fields are automatically synchronized between the provider and consumer instances. As a result, when comments or work notes are posted in one instance, they appear in the connected instance as well.

    A comment-to-comment mapping is created by default in both the **Inbound** and the **Outbound** field configurations while creating a remote task definition from Service Exchange version 2.2.x. For more information, see [Create a remote task definition in Service Exchange for Providers](../task/service-bridge-v2-create-remote-tasks-defs.md).

    -   **Rules of journal field mapping**

        Journal field framework supports the following format \(source to target\).

        -   journal field \(source\) to journal field \(target\)
        -   journal field \(source\) to non-journal field \(target\)
    Journal field framework doesn’t supports non-journal field \(source\) to journal field \(target\) mapping.

    **Note:** In a Remote Task Definition \(RTD\), you cannot use the same journal source field twice for different mappings. For example, work notes to work notes and work notes to comments in the same RTD are not allowed.

-   **Write journal entries as an actual user**

    Write journal entries using user identities rather than a generic company name. For example, all comments for user David would appear as David \(xyz company\).

-   **Synchronize historical journal entries**

    Synchronize all historical journal entries between consumer and provider instances for a remote task.

    If the **Sync pre-existing entries** option is configured during Remote Task Definition \(RTD\) setup and while activating the RTD, all journal comments made in a task are synchronized between the consumer and provider instances when a remote task is connected.


## Considerations

Journal synchronization or synchronize of historical journals might not work for the following scenarios:

-   Synchronization of Journal fields won’t work if a remote task is deleted and a new remote task is later created for the same parent task and RTD.
-   Synchronization of historical journal entries stops and doesn’t resume if a remote task is disconnected and later reconnected, even if the **Sync pre-existing entries** option is enabled in the connected RTD.

**Related topics**  


[Create a remote task definition in Service Exchange for Providers](../task/service-bridge-v2-create-remote-tasks-defs.md)

[Activate a remote task definition record in Service Exchange](../task/service-bridge-v2-activate-remote-task.md)


```


### File: service-exchange\service-bridge-v2-fds-accept-sups-provider.md

```text
---
title: Accept a foundation data sync \(FDS\) subscription as a provider
description: Accept a foundation data sync \(FDS\) subscription to complete the FDS configuration and begin receiving data from the consumer.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [foundation data sync, FDS subscription, accept subscription, provider inbound, activate sync]
breadcrumb: [Configure inbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Accept a foundation data sync \(FDS\) subscription as a provider

Accept a foundation data sync \(FDS\) subscription to complete the FDS configuration and begin receiving data from the consumer.

## Before you begin

Role required: admin \(sb\_admin\)

## About this task

After the subscription items are validated, you must accept the subscription to complete the FDS configuration and activate data synchronization.

If the consumer has enabled auto-publish for the subscription, accepting it will automatically publish the subscription and begin data synchronization. Otherwise, your consumer need to manually publish the subscription before data sync begins.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Open Records** &gt; **FDS Requests**.

2.  In the **Type: Inbound**, select the request.

3.  From the Foundation Data Provider Inbound Subscriptions related list, open the provider subscription by selecting the record number in the **Number** column.

4.  Select **Accept**.

    If you reject the subscription by selecting **Reject**, your consumer needs to resend the sample files, and you must reconfigure the subscription items before you can accept the subscription again.


## Result

If the consumer has enabled auto-publish, the subscription automatically moves to Active state and data synchronization begins immediately. Otherwise, the subscription remains in Accepted state until the consumer manually publishes it.

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)


```


### File: service-exchange\service-bridge-v2-fds-validate-subs-items-provider.md

```text
---
title: Validate FDS subscriptions items as a provider
description: Configure the sample data received from the consumer to validate a foundation data sync \(FDS\) subscription item.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [foundation data sync, FDS subscription, validate subscription, field mapping, provider inbound]
breadcrumb: [Configure inbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Validate FDS subscriptions items as a provider

Configure the sample data received from the consumer to validate a foundation data sync \(FDS\) subscription item.

## Before you begin

Role required: admin \(sb\_admin\)

## About this task

After you create an FDS offering request, the consumer acknowledges the request and sends you a sample payload. This payload helps you understand the structure and type of data you will receive.

After the consumer sends the sample, the system creates a subscription for each offering in the FDS request. Each subscription includes a subscription item for every table the consumer shares. Configure the incoming sample data to validate each subscription item.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Open Records** &gt; **FDS Requests**.

2.  From the **Type: Inbound**, select the request.

3.  From the Foundation Data Provider Inbound Subscriptions related list, open the provider subscription by selecting the record number in the **Number** column.

4.  From the Subscription Items related list, open the subscription item by selecting the record number in the **Number** column.

    Each subscription item represents a specific table that the consumer is sharing with you.

5.  Configure incoming data using either IntegrationHub ETL or a transform map depending on whether you are working with a Configuration Management Database \(CMDB\) or a non-CMDB table.

<table id="choicetable_msz_gll_sfc"><thead><tr><th align="left" id="d35211e135">

Option

</th><th align="left" id="d35211e138">

Description

</th></tr></thead><tbody><tr><td id="d35211e144">

**Configure data integration for CMDB tables**

</td><td>

1.  Select the **ETL Transform Map Assistance** button.

A message is displayed stating that you're about to navigate to the ETL Transform Map Assistant guided setup.

2.  Confirm your choice by selecting **OK**.
3.  Use the guided setup to complete the mapping to integrate the consumer's data into your CMDB. For details, see [IntegrationHub ETL](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/integration-hub-etl/integrationhub-etl.md).

The system creates a basic field mappings based on matching field names. Review and customize the mappings as needed for your instance.

**Note:** Since FDS provides display values for reference fields, if you want to use reference data, you must create a table look up transform mapping to retrieve the Sys ID from the reference table. For more details, see [Foundation Data Sync :: Known issues and workarounds \[KB2299760\]](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=8a2b463c873aaadc57288519dabb354b)

4.  Close the browser tab to return to the Subscription Item page.


</td></tr><tr><td id="d35211e190">

**Configure data integration for non-CMDB table**

</td><td>

1.  Select the **Transform Map** button.

A message is displayed stating that you're about to navigate to the Transform Map to complete the configuration.

2.  Confirm your choice by selecting **OK**.
3.  Complete the configuration. For details on working with transform maps, see [Create a transform map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/system-import-sets/t_CreateATransformMap.md).
4.  Close the browser tab to return to the Subscription Item page.


</td></tr></tbody>
</table>    You must configure incoming data for each subscription item except dependent subscription items.


## Result

After you complete the configuration, the state of the subscription item and of the subscription changes to Validated.

## What to do next

[Accept the subscription.](service-bridge-v2-fds-accept-sups-provider.md)

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)


```


### File: service-exchange\service-bridge-v2-flow-action.md

```text
---
title: Flow action
description: Workflow Studio predefined actions help you preserve mapped variable integrity and maintain flow compatibility across configuration revisions.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Flow action

Workflow Studio predefined actions help you preserve mapped variable integrity and maintain flow compatibility across configuration revisions.

Service Exchange provides a set of predefined Workflow Studio actions that you can use in your flows or subflows to retrieve variable values from remote tasks and provider tasks. For details on flows, see [Getting started with flows](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/getting-started-flow.md).

Service Exchange provides the following actions in Workflow Studio:

**Note:** To avoid upgrade issues, use these predefined actions in your flows and subflows.

<table id="table_x1x_ch2_zfc"><thead><tr><th>

Action

</th><th>

Description

</th><th>

Input

</th><th>

Purpose

</th><th>

Output

</th></tr></thead><tbody><tr><td>

Get Provider Task Variables for RRP

</td><td>

Retrieve variable values from a Provider task based on a selected remote record producer \(RRP\) as data pills for use in other actions.Must be in the `sn_sb` base scope.

</td><td>

provider task, RRP.

</td><td>

Use variables in automation flows, such as updating a parent task or ordering a local catalog item.

</td><td>

Returns named data pills based on the variables within the RRP.

</td></tr><tr><td>

Get Remote Task Variables from Consumer

</td><td>

Retrieves variable answers from a remote task based on a selected remote task definition \(RTD\) identity, exposing them as data pills for use in other actions.Must be in the provider scope.

</td><td>

remote task, RTD identity.

</td><td>

Use variables in automation flows, such as updating a parent task.

</td><td>

Returns named data pills based on the variables within the latest published RTD.

</td></tr><tr><td>

Get Remote Task Variables from Provider

</td><td>

Retrieve variable values from a remote task based on selected remote task definitions.Must be in the consumer scope.

</td><td>

remote task,RTD identity.

</td><td>

Use variables in automation flows, such as updating a parent task.

</td><td>

Returns named data pills based on the variables within the latest published RTD.

</td></tr><tr><td>

Order Remote Record Producer

</td><td>

Automate ordering a RRP.Must be in the consumer scope.

</td><td>

RRP.

</td><td>

Streamline processes such as hardware asset management \(HAM\) by scripting RRP ordering.

</td><td>

Returns the newly created provider task GlideRecord.

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-glossary-sb.md

```text
---
title: Service Exchange glossary
description: A list of terms used in Service Exchange.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.Glossary terms are grouped alphabetically.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 9
keywords: [glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms, glossary terms]
breadcrumb: [Reference, Service Exchange]
---

# Service Exchange glossary

A list of terms used in Service Exchange.

## A

Glossary terms are grouped alphabetically.

### application scope

A unique namespace and a set of permissions to access application files and data. Admins can specify the data that is accessible to other applications from the application record or from each table record.

### attachment sync

A feature that synchronizes file attachments between provider and consumer instances, ensuring both parties have access to attachments.

### authorized user

An individual user record that is permitted to access Service Exchange instances, as defined by the admins.

**Related topics**  


[Add an authorized user](../task/service-bridge-v2-create-auth-user.md)

## B

Glossary terms are grouped alphabetically.

### bi-directional integration

A connection that enables data and updates to flow both ways between provider and consumer Service Exchange instances to keep linked records in sync.

## C

Glossary terms are grouped alphabetically.

### consumer

A person or an organization that receives services from a provider through Service Exchange.

**Related topics**  


[Service Exchange for Consumers](../concept/service-bridge-consumers-landing-page.md)

### consumer application

A Service Exchange component installed on the consumer's instance that enables users to request services, track fulfillment, and exchange updates with their provider.

**Related topics**  


[Components installed with Service Exchange for Consumers](service-bridge-v2-installed-components-customer.md)

### consumer criteria

A filter criteria that determine which consumers are entitled to specific Service Exchange content, such as catalog items or tasks.

**Related topics**  


[Create a consumer criteria](../concept/service-bridge-v2-create-consumer-criteria.md)

### configuration revision

A versioned update to various [entitlements](service-bridge-v2-glossary-sb.md#), such as a remote record producer, remote task definition, or FDS offering, which enables providers to introduce new features without disrupting existing consumer entitlements.

**Related topics**  


[Configuring revisions](../concept/service-bridge-v2-config-revision.md)

## D

Glossary terms are grouped alphabetically.

### domain separation

A process to separate data, processes, and administrative tasks into logical groupings called domains. Admins can then control the information available to each domain, including which users can see and access the data. Typically used only in Multiple Service Provider \(MSP\) organizations.

**Related topics**  


[Domain separation and Service Exchange](service-bridge-v2-domain-separation.md)

## E

Glossary terms are grouped alphabetically.

### entitlement

A configuration mechanism in Service Exchange that determines which remote content, such as catalog items, record producers, remote tasks definitions, a consumer instance is allowed to access.

**Related topics**  


[Creating entitlements in Service Exchange for Providers](../concept/service-bridge-v2-entitlements.md)

## F

Glossary terms are grouped alphabetically.

### flow action

A predefined automation step in Workflow Studio that helps manage repetitive tasks in Service Exchange.

**Related topics**  


[Flow action](../concept/service-bridge-v2-flow-action.md)

### foundation data sync

A mechanism for scheduled, structured synchronization of foundational data \(such as assets, users, or locations\) from provider to consumer instances.

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

## H

Glossary terms are grouped alphabetically.

### health dashboard

A centralized UI that displays health of connected instances, the results of system health checks, errors, and scan statuses in Service Exchange.

**Related topics**  


[Service Exchange Center](../concept/se-se-center.md)

## I

Glossary terms are grouped alphabetically.

### instance scan checks

Automated tests that identify configuration issues or system inconsistencies in Service Exchange to help administrators maintain system health and reduce downtime.

**Related topics**  


[Instance scan checks](../concept/service-bridge-v2-scan-checks.md)

[List of scan checks](service-bridge-v2-list-of-scan-checks-in-sb.md)

## J

Glossary terms are grouped alphabetically.

### Journal Field Framework

A framework that synchronizes journal-type fields, such as comments and work notes, between provider and consumer instances, preserving operational history and user attribution.

**Related topics**  


[Journal field frameworks](../concept/service-bridge-v2-expolre-journal-field-framework.md)

## K

Glossary terms are grouped alphabetically.

## L

Glossary terms are grouped alphabetically.

## M

Glossary terms are grouped alphabetically.

### magic link

A special URL that allows a consumer user to access a resource in the provider instance directly, bypassing manual login for a seamless experience.

**Related topics**  


[Magic links](../concept/service-bridge-v2-explore-magic-link.md)

## N

Glossary terms are grouped alphabetically.

## P

Glossary terms are grouped alphabetically.

### Partner

A person or an organization that supports service fulfillment on behalf of a provider, so a partner is essentially a provider for the provider's. Providers can delegate specific tasks to fulfillment partners, who operate within the same Service Exchange infrastructure. These partners receive, update, and complete tasks in real time, ensuring transparency, continuity, and coordinated service delivery across all participating parties.

### persona

A category used to define entitlement to catalog items or services by grouping authorized users.

**Related topics**  


[User roles for providers](../concept/service-bridge-v2-personas.md)

### proactive case

A case automatically generated to proactively notify and address impacted customers before they report an issue.

**Related topics**  


[Proactive cases](../concept/service-bridge-v2-proactive-case.md)

### provider

An organization or instance that offers and fulfills services for consumers using Service Exchange.

**Related topics**  


[Service Exchange for Providers](../concept/service-bridge-providers-landing-page.md)

### provider application

The Service Exchange component installed on the service provider's instance. It allows providers to publish service catalogs, manage requests, and fulfill tasks for consumers.

**Related topics**  


[Components installed with Service Exchange for Providers](service-bridge-v2-installed-components-provider.md)

### provider task

A task created in the provider instance to fulfill a consumer request, with status and updates synchronized to the consumer instance.

**Related topics**  


[Provider tasks](../concept/service-bridge-v2-provider-tasks.md)

## R

Glossary terms are grouped alphabetically.

### registration task

A task record initiates and monitors the status of a secure, bi-directional connection between provider and consumer instances, typically initiated by the provider.

### remote catalog

A catalog of services created by the provider and made available to consumers as catalog items in their own instance.

**Related topics**  


[Create remote catalogs in Service Exchange for providers](../concept/service-bridge-v2-remote-catalog.md)

### remote record producer

A configuration record that defines variables and inputs a consumer must provide to submit a request. When used, it creates a [provider task](service-bridge-v2-glossary-sb.md#) on the provider instance and triggers the appropriate fulfillment action. Task updates remain visible in both the provider and consumer instances throughout the process.

Also know as RRP.

**Related topics**  


[Remote record producers in Service Exchange](../concept/service-bridge-v2-remote-record.md)

### remote task

A linked task that enables synchronization of incidents, cases, or service requests between provider and consumer instances.

**Related topics**  


[Remote tasks](../concept/service-bridge-v2-remote-task-overview.md)

### role

A category assigned to a group or user to grant access to specific privileges in Service Exchange.

**Related topics**  


[User roles for providers](../concept/service-bridge-v2-personas.md)

## S

Glossary terms are grouped alphabetically.

### scratchpad

A feature that allows providers and consumers to exchange additional structured data \(name-value pairs\) associated with tasks, synchronized automatically between instances.

**Related topics**  


[Using the Scratchpad for Service Exchange tasks](../concept/service-bridge-v2-scratchpad.md)

### Service Exchange

An application that connects multiple ServiceNow instances \(provider, consumer, partner\) to enable seamless, bi-directional service delivery, collaboration, and data synchronization across organizational boundaries.

**Related topics**  


[Exploring Service Exchange](../concept/service-bridge-v2-exploring-service-bridge.md)

## T

Glossary terms are grouped alphabetically.

### transform framework

A tool for mapping and converting data between provider and consumer instances during remote task synchronization in Service Exchange. Transforms can be created once and reused across all remote task definitions.

**Related topics**  


[Transform data with the Service Exchange transform framework](../concept/service-bridge-v2-transform-about.md)

## V

Glossary terms are grouped alphabetically.

### variable

A form field that collects user input data in catalog items or remote record producers. Variables define the type, format, and validation rules for the information users provide when submitting service requests.

### variable set

A modular collection of variables that can be reused across multiple remote record producers to ensure consistency in data collection.


```


### File: service-exchange\service-bridge-v2-install.md

```text
---
title: Configure Service Exchange for Consumers
description: As a consumer, follow these steps to set up the Service Exchange for Consumers application in your own instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Service Exchange for Consumers, Service Exchange]
---

# Configure Service Exchange for Consumers

As a consumer, follow these steps to set up the Service Exchange for Consumers application in your own instance.

## Pre-installation checks

**Check glide.servlet.uri property**: Ensure that the `glide.servlet.uri` property in the Glide instance is set to the correct instance URL. An issue can occur when an instance is cloned from production, but still refers to the production URL for the `glide.servlet.uri` property.

|Task|Link|
|----|----|
|Install the Service Exchange for Consumers application.|See [Install Service Exchange for Consumers](../task/install-service-bridge-v2-customer.md).|
|Add Service Exchange roles for consumers.|See [Personas for consumers](service-bridge-v2-customer-roles.md).|
|Register with a provider.|See [Connect to a provider](../task/service-bridge-v2-register.md).|
|Activate entitlements.|See [Activate a remote record producer in Service Exchange](../task/service-bridge-v2-activate-entitlements.md).|
|Configure consumer pre-flows.|See [Service Exchange consumer pre-flows](../task/service-bridge-v2-conf-consumer-flow.md).|
|Add authorized users.|See [Add an authorized user](../task/service-bridge-v2-create-auth-user.md).|
|Create transforms.|See [Create a transform in Service Exchange](../task/service-bridge-v2-create-transform.md).|
|Create remote tasks to sync data.|See [Create remote tasks to sync data](../task/service-bridge-v2-remote-task-create.md).|
|Configure settings.|See [Configure settings on the consumer instance](../task/service-bridge-v2-configure-consumer-settings.md).|

**Related topics**  


[Service Exchange](../../tmt-service-bridge/concept/tmt-service-bridge-both-landing-page.md)

[Use for consumers](se-consumer-using.md)


```


### File: service-exchange\service-bridge-v2-installed-components-customer.md

```text
---
title: Components installed with Service Exchange for Consumers
description: Several types of components are installed with activation of the Service Exchange for Consumers application including tables, user roles, and business rules.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Reference, Service Exchange]
---

# Components installed with Service Exchange for Consumers

Several types of components are installed with activation of the Service Exchange for Consumers application including tables, user roles, and business rules.

**Note:** The Application Files \[sys\_metadata\] table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Roles installed

The following roles are installed with the Service Exchange for Consumers application.

<table id="table_gtr_pw3_bmb"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains roles

</th></tr></thead><tbody><tr><td>

Service Exchange admin \[sn\_sb.admin\]

</td><td>

-   Typically assigned to an administrator for the Service Exchange applications on both the customer and the provider side.
-   Provides read access to all Service Exchange tables

</td><td>

-   sn\_sb.read
-   sn\_sb.requestor
-   sn\_sb.remote\_task\_creator
-   flow\_designer
-   catalog

</td></tr><tr><td>

Service Exchange read \[sn\_sb.read\]

</td><td>

Provides read-only access to provider tasks

</td><td>

N/A

</td></tr><tr><td>

Service Exchange requester \[sn\_sb.requestor\]

</td><td>

Provides access to remote record producers and provider tasks

</td><td>

N/A

</td></tr></tbody>
</table>## Business rules installed

The following business rules are installed with the Service Exchange for Consumers application.

<table id="table_lgm_zdq_gzb"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Abort Duplicate Remote Task Insert

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Aborts remote task insert if one already exists matching the same parent and remote task definition.

</td></tr><tr><td>

Abort if duplicate transform is found

</td><td>

\[sn\_sb\_con\_transform\]

</td><td>

Aborts transform insert if duplicate is found.

</td></tr><tr><td>

Abort if duplicate URL

</td><td>

\[sn\_sb\_con\_provider\_connection\]

</td><td>

Aborts connection record insert if record with same URL is found.

</td></tr><tr><td>

Abort Remote Task Create If Missing Conn

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Aborts remote task insert if connection field is empty.

</td></tr><tr><td>

Add provider connection data to session

</td><td>

\[sn\_sb\_con\_provider\_connection\]

</td><td>

Saves connection data for later use.

</td></tr><tr><td>

Change state to Work in Progress

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Updates State to Work in Progress for provider tasks.

</td></tr><tr><td>

Check provider published variable

</td><td>

\[item\_option\_new\]

</td><td>

Verifies if the provider side variable published is valid.

</td></tr><tr><td>

Check Remote Task Def Simple Triggers

</td><td>

\[task\]

</td><td>

Checks if changes to parent task have triggered changes in the Remote Task Definition simple trigger conditions.

</td></tr><tr><td>

Clear Remote Task Client Data

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Clears client data associated with remote tasks after the transaction is completed.

</td></tr><tr><td>

Create or Update Transport Connection

</td><td>

\[sn\_sb\_con\_provider\_connection\]

</td><td>

Manages transport connection insert and update.

</td></tr><tr><td>

Create parent on synced remote task

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Creates parent task for synced remote tasks.

</td></tr><tr><td>

Delete associated records

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Deletes related records when Remote Task Definition is deleted.

</td></tr><tr><td>

Disconnect RT when RTD Deleted

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Disconnects all associated remote tasks when Remote Task Definition is deleted.

</td></tr><tr><td>

Error RT when Parent Deleted

</td><td>

\[task\]

</td><td>

Errors out all associated remote tasks when parent task is deleted.

</td></tr><tr><td>

Generate OAuth registry

</td><td>

\[sn\_sb\_con\_provider\_connection\]

</td><td>

Creates OAuth registry for a connection.

</td></tr><tr><td>

Handle authorized user transport

</td><td>

\[sn\_sb\_con\_authorized\_user\]

</td><td>

Sends authorized user records through transport layer.

</td></tr><tr><td>

Inactive Remote Task Definition when archived

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Deactivates Remote Task Definition on consumer instance when archived by provider.

</td></tr><tr><td>

Populate Company on Consumer

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Sets company field on provider tasks on Insert.

</td></tr><tr><td>

Populate Provider task data

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Adds extra data on Insert of Provider Task.

</td></tr><tr><td>

Process Deleted Entitlements

</td><td>

\[sn\_sb\_con\_entitlement\]

</td><td>

Manages entitlement deletion by deleting associated elements.

</td></tr><tr><td>

 

</td><td>

 

</td><td>

 

</td></tr><tr><td>

Process Entitlement attachment changes

</td><td>

\[sys\_attachment\]

</td><td>

Manages changes to attachments for entitlements.

</td></tr><tr><td>

Process New and Updated Entitlements

</td><td>

\[sn\_sb\_con\_entitlement\]

</td><td>

Manages creation of new entitlements and updates to existing entitlements.

</td></tr><tr><td>

Propagate Service Exchange Version Changes

</td><td>

\[v\_plugin\]

</td><td>

Tracks and updates settings when Service Exchange version is updated.

</td></tr><tr><td>

Remote Choice: cache user selection

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Caches user selections to prevent repeat requests for the same data.

</td></tr><tr><td>

Retry Errored RT on RTD Activation

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Attempts to create parent task creation for remote tasks with errors when the associated remote task definition is activated.

</td></tr><tr><td>

Set company field on remote task insert

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Sets the company field for remote tasks during Insert.

</td></tr><tr><td>

Set Connection Id from RRP

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Sets the Connection Id from the Remote Record Producer associated with the Provider Task.

</td></tr><tr><td>

Set Customer Version on Settings Insert

</td><td>

\[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

Sets the Service Exchange for Consumer application version on Settings during the Insert operation.

</td></tr><tr><td>

Set default values

</td><td>

\[sn\_sb\_con\_authorized\_user\]

</td><td>

Sets default values on authorized users when created.

</td></tr><tr><td>

Set outbound vars json on insert

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Sets the outbound json field on remote tasks when inserted by current instance.

</td></tr><tr><td>

Set Provider task number

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Sets provider task number on insert from client data

</td></tr><tr><td>

Set Remote Task number

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Sets remote task number on insert from client data

</td></tr><tr><td>

Set Table Details On Virtual Transform

</td><td>

\[sn\_sb\_con\_transform\]

</td><td>

Sets table data on virtual transforms.

</td></tr><tr><td>

Sync Attachment from Parent Task

</td><td>

\[sys\_attachment\]

</td><td>

Syncs attachments from parent task to all remote tasks associated with parent task.

</td></tr><tr><td>

Sync Remote Task Attachment to Parent

</td><td>

\[sys\_attachment\]

</td><td>

Syncs attachments from remote task to parent task.

</td></tr><tr><td>

Trigger changed attachment transport

</td><td>

\[sys\_attachment\]

</td><td>

Triggers attachment sync through transport layer when updated.

</td></tr><tr><td>

Trigger consumer PT transport

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Triggers provider task sync through transport layer.

</td></tr><tr><td>

Trigger consumer remote task transport

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Triggers remote task sync through transport layer during Insert or Delete operations.

</td></tr><tr><td>

Trigger inserted attachment transport

</td><td>

\[sys\_attachment\]

</td><td>

Triggers attachment sync through transport layer during Insert operation.

</td></tr><tr><td>

Trigger remote task transport update

</td><td>

\[sn\_sb\_con\_remote\_task\]

</td><td>

Triggers remote task sync through transport layer when updated.

</td></tr><tr><td>

Trigger SBScratchpad Transport

</td><td>

\[sn\_sb\_scratchpad\]

</td><td>

Triggers scratchpad sync through transport layer.

</td></tr><tr><td>

Trigger settings transport

</td><td>

\[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

Triggers settings record sync through transport layer.

</td></tr><tr><td>

Update entitlement status on delete

</td><td>

\[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

Updates entitlement status when deleted.

</td></tr><tr><td>

Update entitlement status on delete

</td><td>

\[sn\_sb\_con\_persona\]

</td><td>

Updates persona record on entitlement when deleted.

</td></tr><tr><td>

Update entitlement status on delete

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Updates Remote Task Definition record on entitlement when deleted.

</td></tr><tr><td>

Update entitlement status on update

</td><td>

\[sn\_sb\_con\_persona\]

</td><td>

Manages persona record on entitlement when updated.

</td></tr><tr><td>

Update entitlement status on update

</td><td>

\[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Manages Remote Task Definition record on entitlement when updated.

</td></tr><tr><td>

Update entitlement status on update

</td><td>

\[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

Manages Remote Record Producer record on entitlement when updated.

</td></tr><tr><td>

Validate activation and complete setup

</td><td>

\[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

Validates Remote Record Producer before activation.

</td></tr><tr><td>

Validate request on customer

</td><td>

\[sn\_sb\_con\_provider\_task\]

</td><td>

Checks for valid connection on Provider Task.

</td></tr><tr><td>

Warn if Global Script Include is missing

</td><td>

\[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

Displays warning if global script include is not present when processing Remote Record Producer.

</td></tr></tbody>
</table>## Tables installed

<table id="table_ttz_z2q_gzb"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Authorized user \[sn\_sb\_con\_authorized\_user\]

</td><td>

Authorized users.

</td></tr><tr><td>

Connection \[sn\_sb\_con\_consumer\]

</td><td>

Consumer side connection record.

</td></tr><tr><td>

Entitlement \[sn\_sb\_con\_entitlement\]

</td><td>

Consumer side table extending entitlements.

</td></tr><tr><td>

Inbound Field \[sn\_sb\_con\_inbound\_field\]

</td><td>

Consumer side inbound fields for Remote Task Definitions.

</td></tr><tr><td>

Outbound Field \[sn\_sb\_con\_outbound\_field\]

</td><td>

Consumer side outbound fields for Remote Task Definitions.

</td></tr><tr><td>

Personas \[sn\_sb\_con\_persona\]

</td><td>

Consumer side persona records.

</td></tr><tr><td>

Provider Connection \[sn\_sb\_con\_provider\_connection\]

</td><td>

Provider Connection record linking consumer to provider instance, extending base connection table.

</td></tr><tr><td>

Provider Task \[sn\_sb\_con\_provider\_task\]

</td><td>

Consumer side provider task records, extends Provider Task base table.

</td></tr><tr><td>

Remote Choice Cache \[sn\_sb\_con\_remote\_choice\_cache\]

</td><td>

Consumer side cache for remote choice queries.

</td></tr><tr><td>

Remote Record Producer \[sn\_sb\_con\_remote\_record\_producer\]

</td><td>

Consumer side Remote Record Producer records.

</td></tr><tr><td>

Remote Task \[sn\_sb\_con\_remote\_task\]

</td><td>

Consumer side remote task records, extends remote task base table.

</td></tr><tr><td>

Remote Task Definition \[sn\_sb\_con\_remote\_task\_def\]

</td><td>

Consumer side Remote Task Definition records.

</td></tr><tr><td>

Remote Task Variable\[sn\_sb\_con\_remote\_task\_variable\]

</td><td>

Remote Task associated variable table extending glide vars.

</td></tr><tr><td>

Service Exchange Settings \[sn\_sb\_con\_service\_bridge\_settings\]

</td><td>

Consumer side Service Exchange setting records, extends settings base table.

</td></tr><tr><td>

Remote Choice \[sn\_sb\_con\_st\_remote\_choice\]

</td><td>

Consumer side remote choice records.

</td></tr><tr><td>

Transform \[sn\_sb\_con\_transform\]

</td><td>

Consumer side transform records, extends transform base table.

</td></tr></tbody>
</table>## Flows installed

The following flows are installed with the Service Exchange for Consumers application.

<table id="table_qwz_zkc_kmb"><thead><tr><th>

Flow

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Process Remote Record Producer Entitlements with Remote Choice Variables\[process\_remote\_record\_producer\_entitlements\_with\_remote\_choice\_variables\]

</td><td>

Processes entitlements for remote record producers on consumer with remote choice variables included.

</td></tr></tbody>
</table>## Subflows installed

The following subflows are installed with the Service Exchange for Consumers application.

<table id="table_ud5_pht_fzb"><thead><tr><th>

Subflow

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Repair RPS Provider Connection Error \[repair\_rps\_provider\_connection\_error\]

</td><td>

Handles provider connection errors with Remote Process Sync when in error state.

</td></tr></tbody>
</table>## Flow actions installed

The following flow actions are installed with the Service Exchange for Consumers application.

|Action|Description|
|------|-----------|
|Create Parent From Remote Task \[create\_parent\_from\_remote\_task\]|Creates a parent record for a synced remote task.|
|Create Record Producer and Remote Choice Dependent Variables \[create\_record\_producer\_and\_entities\]|Creates a remote record producer and the associated remote choice dependent variables from a synced entitlement.|
|Create Remote Task \[create\_remote\_task\]|Creates a remote task for a given parent and remote task definition.|
|Repair RPS Provider Connection \[repair\_rps\_provider\_connection\]|Attempts to fix Remote Process Sync errors on Provider Connection.|


```


### File: service-exchange\service-bridge-v2-installed-components-provider.md

```text
---
title: Components installed with Service Exchange for Providers
description: Several types of components are installed when you activate the Service Exchange for Providers application, including tables, user roles, and business rules.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 10
breadcrumb: [Reference, Service Exchange]
---

# Components installed with Service Exchange for Providers

Several types of components are installed when you activate the Service Exchange for Providers application, including tables, user roles, and business rules.

The Application Files \[sys\_metadata\] table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Roles installed

The following roles are installed with the Service Exchange for Providers application.

<table id="table_gtr_pw3_bmb"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains roles

</th></tr></thead><tbody><tr><td>

Service Exchange requester \[sn\_sb.requestor\]

</td><td>

-   Enables members of the customer IT staff to request and monitor services from the provider from their service catalog.

**Note:** Any member of the customer's staff who needs access to the provider's remote record producers requires this role.

-   Provides access to the remote record producers and provider tasks.

</td><td>

N/A

</td></tr><tr><td>

Service Exchange read \[sn\_sb.read\]

</td><td>

-   Enables the provider's customer service agents to read the contents of the provider task record.
-   Provides read-only access to the Service Exchange application.

</td><td>

N/A

</td></tr><tr><td>

Service Exchange admin \[sn\_sb.admin\]

</td><td>

-   Typically assigned to an administrator for the Service Exchange applications on both the customer and the provider side.
-   Provides read access to all Service Exchange tables

</td><td>

-   sn\_sb.requestor
-   sn\_sb.remote\_task\_creator
-   sn\_sb.read
-   flow\_designer
-   sn\_customerservice.case\_viewer
-   sn\_customerservice.customer\_data\_viewer
-   catalog

</td></tr></tbody>
</table>## Business rules installed

The following business rules are installed with the Service Exchange for Providers application.

<table id="table_ejs_r4p_gzb"><thead><tr><th>

Business rule

</th><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Abort duplicate remote task insert

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Aborts insert of remote task if it already exists.

</td></tr><tr><td>

Abort if duplicate transform is found

</td><td>

sn\_sb\_pro\_transform

</td><td>

Aborts insert or update of transform if duplicate found.

</td></tr><tr><td>

Abort if duplicate URL

</td><td>

sn\_sb\_pro\_consumer\_

 connection

</td><td>

Aborts insert of consumer connection if duplicate URL already exists.

</td></tr><tr><td>

Abort if field name already in use

</td><td>

sn\_sb\_pro\_inbound\_field

</td><td>

Aborts insert of inbound field if name is a duplicate.

</td></tr><tr><td>

Abort if field name already in use

</td><td>

sn\_sb\_pro.outbound\_field

</td><td>

Aborts insert of outbound field if name is a duplicate.

</td></tr><tr><td>

Abort if remote task def is not editable

</td><td>

sn\_sb\_pro\_remote\_task\_

 def\_customer\_criteria

</td><td>

Blocks creating or editing consumer criteria if associated remote task def is not in an editable state.

</td></tr><tr><td>

Abort if remote task def is not editable

</td><td>

sn\_sb\_pro\_inbound\_field

</td><td>

Blocks insert of inbound fields if associated remote task definition is not in an editable state.

</td></tr><tr><td>

Abort if remote task def is not editable

</td><td>

sn\_sb\_pro\_outbound\_field

</td><td>

Blocks insert of outbound fields if associated remote task definition is not in an editable state.

</td></tr><tr><td>

Abort publish if duplicate record

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Blocks publishing of remote task definition if is a duplicate record.

</td></tr><tr><td>

Abort Remote Task Create If Missing Conn

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Sets connection on remote task if present, or aborts insert if none found.

</td></tr><tr><td>

Abort remote task def delete by provider

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Prevents remote task definition deletion if definition is not in retired state.

</td></tr><tr><td>

Add cat\_item name to g\_scratchpad

</td><td>

item\_option\_new

</td><td>

Adds the catalog item name to the scratchpad on display.

</td></tr><tr><td>

Add consumer connection data to session

</td><td>

sn\_sb\_pro\_consumer\_

 connection

</td><td>

Adds consumer connection data to session data.

</td></tr><tr><td>

Approve approval record

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Handles record approvals through provider tasks.

</td></tr><tr><td>

Assure deletable

</td><td>

sn\_sb\_pro\_remote\_

 choice\_definition

</td><td>

Checks that a remote task definition is deletable.

</td></tr><tr><td>

Assure persona name uniqueness

</td><td>

sn\_sb\_pro\_persona

</td><td>

Prevents persona records being created with same name.

</td></tr><tr><td>

Assure unique and updatable

</td><td>

sn\_sb\_pro\_remote\_choice\_

 definition

</td><td>

Ensures that only unique remote task definitions are inserted or updated.

</td></tr><tr><td>

Assure uniqueness of criteria for RRP

</td><td>

sn\_sb\_pro\_remote\_record\_

 producer\_consumer\_criteria

</td><td>

Ensures the criteria added to a remote record producer is unique.

</td></tr><tr><td>

Clear remote task client data

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Clears session data for remote task transactions.

</td></tr><tr><td>

Copy attachment from Provider Task

</td><td>

sys\_attachment

</td><td>

Copies attachments from synced provider tasks to parent task.

</td></tr><tr><td>

Copy attachment to Provider Task

</td><td>

sys\_attachment

</td><td>

Copies attachments from parent task to provider tasks.

</td></tr><tr><td>

Create default user criteria on Insert

</td><td>

sn\_sb\_pro\_remote\_

 record\_producer

</td><td>

Creates default user criteria on insert of remote record producer.

</td></tr><tr><td>

Create or Update transport connection

</td><td>

sn\_sb\_pro\_consumer\_

 connection

</td><td>

Manages transport connection on connection changes.

</td></tr><tr><td>

Create parent on synced remote task

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Creates parent task on synced remote task insert.

</td></tr><tr><td>

Delete associated criteria record

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Deletes associated criteria records on delete of a remote task definition.

</td></tr><tr><td>

Delete associated records

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Deletes inbound and outbound mapping records associated with remote task definition.

</td></tr><tr><td>

Disconnect RT when RTD Deleted

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Disconnects all associated remote tasks when a remote task definition is deleted.

</td></tr><tr><td>

Display Scope mismatch warning

</td><td>

Item\_option\_new

</td><td>

Shows warning on variable records when in incorrect scope.

</td></tr><tr><td>

Error RT when Parent Deleted

</td><td>

task

</td><td>

When a parent task is deleted, all associated remote tasks status is set to the Error state.

</td></tr><tr><td>

Force RRP to Draft State on Edits

</td><td>

catalog\_ui\_policy\_action

</td><td>

Sets remote record producer state to Draft when associated records are edited.

</td></tr><tr><td>

Force RRP to Draft State on Edits

</td><td>

sys\_attachment

</td><td>

Sets remote record producer state to Draft when associated records are edited.

</td></tr><tr><td>

Force RRP to Draft State on Edits

</td><td>

catalog\_ui\_policy

</td><td>

Sets remote record producer state to Draft when associated records are edited.

</td></tr><tr><td>

Force RRP to Draft State on Edits

</td><td>

question\_choice

</td><td>

Sets remote record producer state to Draft when associated records are edited.

</td></tr><tr><td>

Force RRP to Draft State on Edits

</td><td>

item\_option\_new

</td><td>

Sets remote record producer State to Draft when associated records are edited.

</td></tr><tr><td>

Force Updates to Update Sets

</td><td>

item\_option\_new

</td><td>

Forces update sets to update on record edits.

</td></tr><tr><td>

Force Updates to Update Sets

</td><td>

catalog\_ui\_policy

</td><td>

Forces update sets to update on record edits.

</td></tr><tr><td>

Force Updates to Update Sets

</td><td>

catalog\_ui\_policy\_action

</td><td>

Forces update sets to update on record edits.

</td></tr><tr><td>

Force Updates to Update Sets

</td><td>

question\_choice

</td><td>

Forces update sets to update on record edits.

</td></tr><tr><td>

Gen entitlements for publish/retire RRP

</td><td>

sn\_sb\_pro\_remote\_

 record\_producer

</td><td>

Generates entitlements for remote record producers that are published or retired.

</td></tr><tr><td>

Gen entitlements for update Persona

</td><td>

sn\_sb\_pro\_persona

</td><td>

Generates entitlements for personas when edited.

</td></tr><tr><td>

Generate entitlements for remote task def

</td><td>

sn\_sb\_pro\_remote\_

 task\_def

</td><td>

Generates entitlements for remote task definition changes.

</td></tr><tr><td>

Handle authorized user transport

</td><td>

sn\_sb\_pro\_authorized\_user

</td><td>

Manages transmission of authorized user changes through the transport layer.

</td></tr><tr><td>

Limit registration tasks by Company and URL

</td><td>

sn\_sb\_pro\_registration

</td><td>

Controls registration tasks by company and URL.

</td></tr><tr><td>

Populate customer details on provider

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Populates inserted provider task information from consumer connection.

</td></tr><tr><td>

Populate scratchpad

</td><td>

sn\_sb\_pro\_registration

</td><td>

Populates scratchpad with relevant information on registration.

</td></tr><tr><td>

Propagate Service Exchange Version Changes

</td><td>

v\_plugin

</td><td>

Adds Service Exchange version changes on settings record.

</td></tr><tr><td>

Reject approval record

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Handles rejection through provider tasks.

</td></tr><tr><td>

Remote Choice: Update attributes field

</td><td>

item\_option\_new

</td><td>

Updates Attributes field on remote choice for variable changes.

</td></tr><tr><td>

Reset Consumer table on mappings

</td><td>

sn\_sb\_pro\_remote\_

 task\_def

</td><td>

Resets the consumer table field on mappings associated with remote task definition when consumer table mappings change.

</td></tr><tr><td>

Reset Provider table on mappings

</td><td>

sn\_sb\_pro\_remote\_

 task\_def

</td><td>

Resets the provider table field on mappings associated with remote task definition on definition provider table change.

</td></tr><tr><td>

Restrict RRP variable types

</td><td>

item\_option\_new

</td><td>

Restricts the types of variables allowed when associated with a remote task definition.

</td></tr><tr><td>

Retry Errored RT on RTD Activation

</td><td>

sn\_sb\_pro\_remote\_

 task\_def

</td><td>

Retry parent creation for remote tasks if associated remote task definition is activated and remote task parent is null.

</td></tr><tr><td>

Send auto approval

</td><td>

sn\_sb\_pro\_authorized\_user

</td><td>

Manages automatic approvals of authorized users.

</td></tr><tr><td>

Service Exchange bootstrap

</td><td>

sn\_sb\_pro\_registration

</td><td>

Helps manage onboarding for Service Exchange.

</td></tr><tr><td>

Set company on remote task insert

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Sets the company \(and account if present\) on remote tasks on insert through sync.

</td></tr><tr><td>

Set copied RRP state to default

</td><td>

sn\_sb\_pro\_remote\_

 record\_producer

</td><td>

Manages setting remote record producer state when copied.

</td></tr><tr><td>

Set default values

</td><td>

sn\_sb\_pro\_authorized\_user

</td><td>

Sets default values on authorized users on insert.

</td></tr><tr><td>

Set outbound vars json on insert

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Sets the outbound vars json field on remote task insert by current instance.

</td></tr><tr><td>

Set Provider task number

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Sets the provider task number to synced provider task number.

</td></tr><tr><td>

Set Remote task number

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Sets remote task number on synced remote task number.

</td></tr><tr><td>

Show warning messages

</td><td>

sn\_sb\_pro\_remote\_

 record\_producer

</td><td>

Shows warning messages for remote record producer errors.

</td></tr><tr><td>

Show warning on incomplete Remote Task Definition

</td><td>

sn\_sb\_pro\_remote\_task\_def

</td><td>

Shows warnings on remote task definition if required related records are missing.

</td></tr><tr><td>

Sync Attachment from Parent Task

</td><td>

sys\_attachment

</td><td>

Syncs attachments from parent tasks to associated remote tasks.

</td></tr><tr><td>

Sync comments from provider task

</td><td>

sys\_journal\_field

</td><td>

Syncs comments from synced provider tasks to parent task.

</td></tr><tr><td>

Sync Remote Task Attachment to Parent

</td><td>

sys\_attachment

</td><td>

Copies synced remote task attachments to parent task.

</td></tr><tr><td>

Trigger changed attachment transport

</td><td>

sys\_attachment

</td><td>

Handles attachment changes syncing through the transport layer.

</td></tr><tr><td>

Trigger entitlement transport

</td><td>

sn\_sb\_pro\_entitlement

</td><td>

Manages entitlements syncing through transport layer

</td></tr><tr><td>

Trigger inserted attachment transport

</td><td>

sys\_attachment

</td><td>

Manages attachment insert syncing through the transport layer.

</td></tr><tr><td>

Trigger provider PT transport

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Manages provider task syncing through the transport layer.

</td></tr><tr><td>

Trigger provider remote task transport

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Manages remote task insert and delete syncing through the transport layer.

</td></tr><tr><td>

Trigger remote task transport update

</td><td>

sn\_sb\_pro\_remote\_task

</td><td>

Manages remote task update syncing through the transport layer.

</td></tr><tr><td>

Trigger SBScratchpad Transport

</td><td>

sn\_sb\_scratchpad

</td><td>

Manages scratchpad update syncing through the transport layer.

</td></tr><tr><td>

Trigger settings transport

</td><td>

sn\_sb\_pro\_service\_bridge\_

 settings

</td><td>

Manages Service Exchange setting syncing through the transport layer.

</td></tr><tr><td>

Update comments from Task to PT

</td><td>

task

</td><td>

Handles syncing of comments from parent task to provider task.

</td></tr><tr><td>

Update consumer registration

</td><td>

sn\_sb\_pro\_service\_bridge\_

 settings

</td><td>

Updates consumer registration on insert of settings record.

</td></tr><tr><td>

Update Persona RRPs on Change

</td><td>

sn\_sb\_pro\_persona

</td><td>

Updates remote record producer persona when modified.

</td></tr><tr><td>

Validate Authorized Users Field Values

</td><td>

sn\_sb\_pro\_service\_bridge\_

 settings

</td><td>

Validates authorized users field values when updated.

</td></tr><tr><td>

Validate max authorized user

</td><td>

sn\_sb\_pro\_service\_bridge\_

 settings

</td><td>

Ensures max authorized user number is within valid range.

</td></tr><tr><td>

Validate Provider task

</td><td>

sn\_sb\_pro\_provider\_task

</td><td>

Validates a provider task insert or update is allowed.

</td></tr></tbody>
</table>## Tables installed

The following tables are installed with the Service Exchange for Providers application.

<table id="table_hnb_j13_bme"><thead><tr><th>

Table

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Authorized Users \[sn\_sb\_pro\_authorized\_user\]

</td><td>

Contains the authorized user records.

</td></tr><tr><td>

Consumer Connection \[sn\_sb\_pro\_consumer\_connection\]

</td><td>

Consumer connection record for provider, extends the base connection table.

</td></tr><tr><td>

Entitlement \[sn\_sb\_pro\_entitlement\]

</td><td>

Provider entitlements associating records to entitled consumers, extends base entitlement table.

</td></tr><tr><td>

Inbound Field \[sn\_sb\_pro\_inbound\_field\]

</td><td>

Manages provider side inbound field mappings for remote task definitions.

</td></tr><tr><td>

Outbound Field \[sn\_sb\_pro\_outbound\_field\]

</td><td>

Manages provider side outbound field mappings for remote task definitions.

</td></tr><tr><td>

Personas \[sn\_sb\_pro\_persona\]

</td><td>

Manages personas for Service Exchange.

</td></tr><tr><td>

Provider \[sn\_sb\_pro\_provider\]

</td><td>

Provider association record to tie provider side records together.

</td></tr><tr><td>

Provider Task \[sn\_sb\_pro\_provider\_task\]

</td><td>

Provider tasks on provider side, created by consumers through remote record producers.

</td></tr><tr><td>

Registration \[sn\_sb\_pro\_registration\]

</td><td>

Service Exchange registration records.

</td></tr><tr><td>

Remote Choice Definition \[sn\_sb\_pro\_remote\_choice\_definition\]

</td><td>

Remote choice definitions for remote record producer.

</td></tr><tr><td>

Consumer Criteria

 \[sn\_sb\_pro\_remote\_record\_producer\_consumer\_criteria\]

</td><td>

Consumer criteria records attributed to remote record producers, controls which consumers are entitled to a given remote record producer.

</td></tr><tr><td>

Remote service \[sn\_sb\_pro\_remote\_service\]

</td><td>

Remote service record.

</td></tr><tr><td>

Remote Task \[sn\_sb\_pro\_remote\_task\]

</td><td>

Remote tasks for managing data transfer between parent tasks on synced instances.

</td></tr><tr><td>

Remote Task Definition \[sn\_sb\_pro\_remote\_task\_def\]

</td><td>

Remote task definition, controls creation and processing of remote tasks.

</td></tr><tr><td>

Consumer Criteria

 \[sn\_sb\_pro\_remote\_task\_def\_consumer\_criteria\]

</td><td>

Consumer criteria records attributed to remote task definitions, controls which consumers are entitled to a given remote task definition.

</td></tr><tr><td>

Remote Task Variable \[sn\_sb\_pro\_remote\_task\_variable\]

</td><td>

Glide variables associated with a remote task, allows displaying incoming synced data

</td></tr><tr><td>

Service Exchange Settings \[sn\_sb\_pro\_service\_bridge\_settings\]

</td><td>

Settings record for provider, manages various Service Exchange settings alignment between provider and consumer.

</td></tr><tr><td>

Transform \[sn\_sb\_pro\_transform\]

</td><td>

Provider side transform records.

</td></tr></tbody>
</table>## Flows installed

The following flows are installed with the Service Exchange for Providers application.

<table id="table_cyl_nyp_gzb"><thead><tr><th>

Flow

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Create Proactive Provider task from Case

 \[create\_proactive\_provider\_task\_from\_case\]

</td><td>

Creates provider task from case in proactive use case.

</td></tr><tr><td>

Process Incoming Consumer Provider Task

 \[process\_incoming\_consumer\_provider\_task\]

</td><td>

Manages incoming provider tasks from consumer.

</td></tr><tr><td>

Process Service Exchange registration

 \[process\_service\_bridge\_registration\]

</td><td>

Manages Service Exchange registration.

</td></tr><tr><td>

Service Exchange Attachment Sync to Task

 \[attachment\_sync\_provider\_task\_to\_task\]

</td><td>

Syncs attachments from provider task to parent task.

</td></tr><tr><td>

Service Exchange Case to Provider task Update

 \[service\_bridge\_case\_to\_provider\_task\_update\]

</td><td>

Manages creating provider tasks on case update.

</td></tr><tr><td>

Service Exchange Change Request to Provider

 task Update

 \[service\_bridge\_change\_request\_to\_provider\_task\_update\]

</td><td>

Manages creating provider tasks on change update.

</td></tr><tr><td>

Service Exchange Incident to Provider task\_Update

 \[service\_bridge\_incident\_to\_provider\_task\_update\]

</td><td>

Manages creating provider tasks on incident update.

</td></tr><tr><td>

Service Exchange Provider Task to Case Update

 \[service\_bridge\_provider\_task\_to\_case\_update\]

</td><td>

Manages processing of provider tasks and creation of associated parent case task.

</td></tr><tr><td>

Service Exchange provider task to Change

 Request Update

 \[service\_bridge\_provider\_task\_to\_change\_request\_update\]

</td><td>

Manages processing of provider tasks and creation of associated parent change request task.

</td></tr><tr><td>

Service Exchange provider task to Incident Update

 \[service\_bridge\_provider\_task\_to\_incident\_update\]

</td><td>

Manages processing of provider tasks and creation of associated parent incident task.

</td></tr></tbody>
</table>## Subflows installed

The following subflows are installed with the Service Exchange for Providers application.

<table id="table_m3v_kzp_gzb"><thead><tr><th>

Subflow

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Create Case from Provider task

 \[create\_case\_from\_provider\_task\]

</td><td>

Creates parent task case from a Provider Task.

</td></tr><tr><td>

Create Change from Provider task

 \[create\_change\_from\_provider\_task\]

</td><td>

Creates parent task change from Provider Task.

</td></tr><tr><td>

Create Incident from Provider task

 \[create\_incident\_from\_provider\_task\]

</td><td>

Creates parent task incident from Provider Task.

</td></tr><tr><td>

Create OAuth Client

 \[create\_oauth\_client\]

</td><td>

Creates the OAuth client on onboarding.

</td></tr><tr><td>

Process invalid Provider task

 \[process\_invalid\_provider\_task\]

</td><td>

Manages provider tasks that have invalid configurations.

</td></tr><tr><td>

Repair RPS Consumer Connection Error

 \[repair\_rps\_consumer\_connection\_error\]

</td><td>

Attempts to fix Remote Process Sync errors in the Consumer Connection.

</td></tr></tbody>
</table>## Flow actions installed

The following flow actions are installed with the Service Exchange for Providers application.

<table id="table_ybb_wzp_gzb"><thead><tr><th>

Flow action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Copy attachment

 \[copy\_attachment\]

</td><td>

Copies a given attachment to a given record.

</td></tr><tr><td>

Copy task variables

 \[copy\_task\_variables\]

</td><td>

Retrieves task variable data for use in flows.

</td></tr><tr><td>

Create parent from remote task

 \[create\_parent\_from\_remote\_task\]

</td><td>

Creates a parent task from a given remote task.

</td></tr><tr><td>

Create remote task for consumer

 \[create\_remote\_task\_for\_consumer\]

</td><td>

Creates a remote task for a given parent task and consumer.

</td></tr><tr><td>

File Service Exchange registration email event

 \[file\_service\_bridge\_registration\_email\_event\]

</td><td>

Files email with information during Service Exchange registration.

</td></tr><tr><td>

Is Transporter User

 \[is\_transporter\_user\]

</td><td>

Checks if current user is transport user.

</td></tr><tr><td>

Parse Provider Task vars\_json

 \[parse\_provider\_task\_vars\_json\]

</td><td>

Parses out the vars json field on the Provider Task.

</td></tr><tr><td>

Repair RPS Consumer Connection

 \[repair\_rps\_consumer\_connection\]

</td><td>

Attempts to fix Remote Process Sync errors on Consumer Connection.

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-list-of-scan-checks-in-sb.md

```text
---
title: List of scan checks
description: Multiple scan checks are available in Service Exchange to help you identify issues and system inconsistencies, enabling you to maintain system health and reduce downtime.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Reference, Service Exchange]
---

# List of scan checks

Multiple scan checks are available in Service Exchange to help you identify issues and system inconsistencies, enabling you to maintain system health and reduce downtime.

|Check|Description|Suite|Check Type|Execution Type|
|-----|-----------|-----|----------|--------------|
|\[PRO\] All dependent apps installation versions are correct|Dependent application's installation versions are incorrect|Service Exchange Post-Clone, Post-Upgrade, Pre-Onboarding, Connection Health|PRO|On-Demand, Scheduled|
|\[PRO\] Check Entitlement Consumer Active Revision is 0|Entitlement was not activated by consumer|Service Exchange Entitlements, Post-Clone, Post-Upgrade, Post-Onboarding|PRO|On-Demand, Scheduled|
|\[PRO\] Checking Entitlements Stuck in Pending|Entitlement in "pending" state longer than expected|Service Exchange Entitlements, Post-Clone, Post-Upgrade, Post-Onboarding|PRO|On-Demand, Scheduled|
|\[PRO\] Connection status is not active or valid|Consumer Connection status isn’t active or valid|Service Exchange Connection Health|PRO|Scheduled|
|\[PRO\] Entitlement with invalid entity reference|Entitlement doesn’t reference a valid entity|Service Exchange Entitlements, Post-Clone, Post-Upgrade, Post-Onboarding|PRO|On-Demand, Scheduled|
|\[PRO\] Entitlement with invalid identity reference|Entitlement doesn’t reference a valid identity|Service Exchange Post-Upgrade, Post-Onboarding, Post-Clone|PRO|On-Demand|
|\[PRO\] Entitlements missing connection|Entitlement doesn’t reference a consumer connection|Service Exchange Entitlements, Post-Onboarding, Post-Upgrade, Post-Clone|PRO|On-Demand, Scheduled|
|\[PRO\] Integration user name does not start with sb\_user|Integration user name doesn’t start with "sb\_user."|Service Exchange Post-Clone, Post-Onboarding|PRO|On-Demand|
|\[PRO\] Magic Links is not configured|Magic Links is not correctly configured|Service Exchange Magic Links Configurations|PRO|Scheduled|
|\[PRO\] Magic Links is not fully enabled|Magic Links is not fully enabled|Service Exchange Magic Links Configurations|PRO|Scheduled|
|\[PRO\] Process Sync Definition configuration is valid|Service Exchange connections' RPS Process Sync Definition is missing|Service Exchange Connection Health, Post-Clone, Pre-Onboarding|PRO|On-Demand, Scheduled|
|\[PRO\] Provider \(sn\_sb\_pro\_provider\) is missing|Provider \(sn\_sb\_pro\_provider\) is missing|Service Exchange Pre-Onboarding|PRO|On-Demand|
| | | | | |
| | | | | |
|\[PRO\] Provider Task parent domain mismatch|Provider Task domain doesn’t match parent task domain|Service Exchange Post-Clone, Provider Task Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Provider task missing Connection reference|Provider Task doesn’t reference a consumer connection|Service Exchange Post-Clone, Post-Upgrade, Provider Task Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Provider task missing Parent reference|Provider Task doesn’t reference a parent task|Service Exchange Post-Upgrade, Provider Task Configurations, Post-Clone|PRO|On-Demand, Scheduled|
|\[PRO\] RRP consumer criteria matches no consumers|No consumers are being entitled to published Remote Record Producer|Service Exchange Remote Record Producer Configurations|PRO|Scheduled|
|\[PRO\] RTD consumer criteria matches no consumers|No consumers are being entitled to published Remote Task Definition|Service Exchange Remote Task Definition Configurations|PRO|Scheduled|
|\[PRO\] Remote Record Producer is invalid|Remote Record Producer doesn’t reference a valid identity|Service Exchange Remote Record Producer Configurations|PRO|Scheduled|
|\[PRO\] Remote Task Definition is invalid|Remote Task Definition has one or more issues|Service Exchange Remote Task Definition Configurations|PRO|Scheduled|
|\[PRO\] Remote choice definition is missing or unpublished|Remote Catalog Variable references a missing or unpublished remote choice definition|Service Exchange Post-Clone, Remote Record Producer Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Remote choice dependent variable is invalid|Remote Choice variable is referencing an invalid or missing dependency|Service Exchange Remote Record Producer Configurations|PRO|Scheduled|
|\[PRO\] Remote task domain matching parent task domain|Remote Task domain doesn’t match parent task domain|Service Exchange Post-Clone, Remote Task Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Remote task missing Connection reference|Remote task doesn’t reference a connection|Service Exchange Remote Task Configurations, Post-Clone, Post-Upgrade|PRO|On-Demand, Scheduled|
|\[PRO\] Remote task missing Parent reference|Remote task doesn’t reference a parent task|Service Exchange Post-Clone, Post-Upgrade, Remote Task Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Settings synced with Provider and Consumer version available|Service Exchange Settings is missing or invalid|Service Exchange Connection Health, Post-Onboarding|PRO|On-Demand, Scheduled|
|\[PRO\] Stale Consumer Connection records|Stale \(unused\) Consumer Connection records|Service Exchange Post-Clone, Pre-Onboarding, Base Configurations|PRO|On-Demand, Scheduled|
|\[PRO\] Stale OAuth registry records|Stale \(unused\) OAuth registry record|Service Exchange Base Configurations, Pre-Onboarding, Post-Clone|PRO|On-Demand, Scheduled|
|\[PRO\] Stale Service Exchange service account records from onboarding retries|Stale \(Unused\) Service Exchange integration user|Service Exchange Pre-Onboarding, Post-Clone|PRO|On-Demand|
|\[CON\] All dependent apps installation versions are correct|Dependent applications installation versions are incorrect|Service Exchange Post-Clone, Post-Upgrade, Pre-Onboarding, Connection Health|CON|On-Demand, Scheduled|
|\[CON\] Check Entitlement Consumer Active Revision is 0|Entitlement hasn’t been activated by the consumer|Service Exchange Entitlements, Post-Onboarding, Post-Upgrade, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Connection status is not active or valid|Provider Connection status isn’t active or valid|Service Exchange Connection Health|CON|Scheduled|
|\[CON\] Entitlement with invalid entity reference|Entitlement doesn’t reference a valid entity|Service Exchange Entitlements, Post-Onboarding, Post-Upgrade, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Entitlement with invalid identity reference|Entitlements does not reference a valid identity|Service Exchange Entitlements, Post-Onboarding, Post-Upgrade, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Entitlements missing connection|Entitlement does not reference a provider connection|Service Exchange Entitlements, Post-Onboarding, Post-Upgrade, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Inbound RRP Timed Out|Remote Record Producer did not finish building Variables and UI Policies|Service Exchange Remote Record Producer Configurations|CON|Scheduled|
|\[CON\] Integration user name does not start with sb\_user|Integration user name does not start with "sb\_user."|Service Exchange Post-Clone, Post-Onboarding|CON|On-Demand|
|\[CON\] Process Sync Definition configuration is valid|Service Exchange Consumer RPS Process Sync Definition is missing|Service Exchange Pre-Onboarding, Connection Health, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Provider services catalog category missing|The Provider Services category is missing|Service Exchange Remote Record Producer Configurations|CON|Scheduled|
|\[CON\] Provider Task parent domain mismatch|Provider Task domain does not match its parent task domain|Service Exchange Provider Task Configurations, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Provider task missing Connection reference|Provider Task does not reference a provider connection|Service Exchange Provider Task Configurations, Post-Clone, Post-Upgrade|CON|On-Demand, Scheduled|
|\[CON\] Remote Record Producer is invalid|Remote Record Producer is missing identity or entitlement|Service Exchange Remote Record Producer Configurations|CON|Scheduled|
|\[CON\] Remote Task Definition is invalid|Remote Task Definition has one or more issues|Service Exchange Remote Task Definition Configurations|CON|Scheduled|
|\[CON\] Remote task domain matching parent task domain|Remote task domain does not match its parent task domain|Service Exchange Remote Task Configurations, Post-Clone|CON|On-Demand, Scheduled|
| | | | | |
| | | | | |
|\[CON\] Remote task missing Connection reference|Remote task does not reference a Connection|Service Exchange Post-Clone, Post-Upgrade, Remote Task Configurations|CON|On-Demand, Scheduled|
|\[CON\] Remote task missing Parent reference|Remote task does not have reference to a parent task|Service Exchange Post-Upgrade, Post-Clone, Remote Task Configurations|CON|On-Demand, Scheduled|
|\[CON\] Settings synced with Provider and Consumer version available|Service Exchange Settings is not valid|Service Exchange Post-Onboarding, Connection Health|CON|On-Demand, Scheduled|
|\[CON\] Stale OAuth registry records|Stale \(Unused\) OAuth registry record|Service Exchange Base Configurations, Pre-Onboarding, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Stale Provider Connection records|Stale \(Unused\) Provider Connection record|Service Exchange Base Configurations, Pre-Onboarding, Post-Clone|CON|On-Demand, Scheduled|
|\[CON\] Stale Service Exchange service account records from onboarding retries|Stale \(Unused\) Service Exchange integration user records|Service Exchange Pre-Onboarding, Post-Upgrade, Post-Clone|CON|On-Demand|
|\[PRO\]\[CON\] Attachment is too large|Attachment size is unsupported|Service Exchange Attachment Handling, Performance|Both|Scheduled|
|\[PRO\]\[CON\] Attachments are very large|Large, performance degrading attachments found|Service Exchange Attachment Handling|Both|Scheduled|
|\[PRO\]\[CON\] Capture Definitions state is invalid|Required RPS connection Capture Definitions are missing|Service Exchange Connection Health, Post-Clone|Both|On-Demand, Scheduled|
|\[PRO\]\[CON\] Global script include version check|Global Service Exchange script include needs updating|Service Exchange Post-Clone, Post-Upgrade, Pre-Onboarding, Base Configurations|Both|On-Demand, Scheduled|
|\[PRO\]\[CON\] KMF is unhealthy|KMF Key Management is not healthy|Service Exchange Pre-Onboarding, Post-Clone, Post-Upgrade|Both|On-Demand|
|\[PRO\]\[CON\] Large number of attachments|Unusally large number of attachments|Service Exchange Performance, Attachment Handling|Both|Scheduled|
|\[PRO\]\[CON\] OAuth crypto module access policy check|OAuth crypto module has incorrect access policy|Service Exchange Pre-Onboarding|Both|On-Demand|
|\[PRO\]\[CON\] Provider and Consumer app versions are same on the instance|Service Exchange Provider and Consumer app installed versions are not matching|Service Exchange Pre-Onboarding, Base Configurations, Post-Upgrade, Post-Clone|Both|On-Demand, Scheduled|
|\[PRO\]\[CON\] Remote System Inbound and Outbound state is valid|Connection's RPS Remote System not in active state|Service Exchange Post-Clone, Connection Health|Both|On-Demand, Scheduled|
|\[PRO\]\[CON\] Skipped files listed in Upgrade History|Skipped files are present in Upgrade History|Service Exchange Post-Upgrade|Both|On-Demand|
|\[PRO\]\[CON\] Transport inbound queue processing is slow|Some inbound records are taking abnormally long to process|Service Exchange Base Configurations|Both|Scheduled|
|\[PRO\]\[CON\] Transport System user domain and user\_id is not modified|The sn\_transport\_system user's domain or user\_id was modified|Service Exchange Connection Health|Both|Scheduled|
|\[PRO\]\[CON\] User Not Authenticated error with RPS|OAuth Client tokens have expired \("User Not Authenticated"\)|Service Exchange Base Configurations|Both|Scheduled|
|\[PRO\]\[CON\] glide.servlet.uri is empty|System property "glide.servlet.uri" is empty|Service Exchange Pre-Onboarding|Both|On-Demand|

**Related topics**  


[Instance scan checks](../concept/service-bridge-v2-scan-checks.md)


```


### File: service-exchange\service-bridge-v2-magic-links.md

```text
---
title: Enable magic links
description: Configure magic links to enable consumer users to access provider instance resources directly without manual authentication. Magic links streamline cross-instance navigation by automatically handling login credentials.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Enable magic links

Configure magic links to enable consumer users to access provider instance resources directly without manual authentication. Magic links streamline cross-instance navigation by automatically handling login credentials.

## Before you begin

Role required: sn\_sb.admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Consumers**.

2.  Open the appropriate Consumer Connection form.

3.  Under the Related Links, select the **Settings** tab and open the record displayed.

4.  In the **Magic link** tab, perform the following steps:

<table id="table_eff_bfp_rfc"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Enable magic links

</td><td>

Option to enable magic links functionality. When enabled, the magic link routes consumer user \(remote user\) to provider instance for completion of tasks.

</td></tr><tr><td>

Single user mode

</td><td>

Option to enable the consumer user to be authenticated as a specific user when accessing the provider instance.

</td></tr><tr><td>

Redirect timeout

</td><td>

Option to specify the number of seconds taken to redirect consumer user to provider instance. The default value is 5, and the maximum limit is 30.**Note:** The redirect timeout can be set only in the consumer instance; it is read-only field on the provider instance. If Redirect timeout value is 0 or empty, consumer user is automatically redirected to the provider instance without any loader UI.

</td></tr></tbody>
</table>5.  Select **Update**.


**Parent Topic:**[Using Service Exchange for providers](../concept/service-bridge-v2-administer.md)


```


### File: service-exchange\service-bridge-v2-migrate.md

```text
---
title: Migrate from Service Exchange \(legacy\)
description: This section describes the process to migrate from the Service Exchange \(legacy\) version.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Migrate from Service Exchange \(legacy\)

This section describes the process to migrate from the Service Exchange \(legacy\) version.

To migrate from the legacy version, follow the steps listed in [Service Exchange for Providers \(Legacy\) - Migration Utility \(KB1499823\)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1499823).


```


### File: service-exchange\service-bridge-v2-mismatch-version.md

```text
---
title: Mismatched version support
description: Providers and consumers using different versions of the Service Exchange applications can exchange and synchronize data between their ServiceNow instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Mismatched version support

Providers and consumers using different versions of the Service Exchange applications can exchange and synchronize data between their ServiceNow instances.

-   Providers can upgrade their Service Exchange application and deploy new capabilities without interrupting services to consumers who haven’t upgraded to their application.
-   Consumers who haven’t upgraded can use existing entitlements from their provider, as well as new entitlements at or below their current compatibility level. However, they can’t activate entitlements on newer compatibility levels until they upgrade to the latest version.

The following is an example scenario:

-   The provider and consumer are using Service Exchange for Providers 1.0 and Service Exchange for Consumers 1.0. The provider has created some configurations \(such as remote task definitions, remote record producers, or foundation data sync offerings\) and the consumer is using these entitlements.
-   The provider decides to upgrade to Service Exchange for Providers 2.0 but the consumer is still using the older version. In this case, the consumer can continue to use the entitlements created using the older version of Service Exchange and sync data with the provider.
-   To use the latest configuration revisions \(created with the upgraded application\), the consumer must upgrade to a version that is compatible with the provider.

**Related topics**  


[Configuring revisions](service-bridge-v2-config-revision.md)


```


### File: service-exchange\service-bridge-v2-new-provider.md

```text
---
title: Set up a Service Exchange provider record
description: Set up a new provider record to establish a unique identifier for the Service Exchange for Providers \(sn\_sb\_pro\) application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Set up a Service Exchange provider record

Set up a new provider record to establish a unique identifier for the Service Exchange for Providers \(sn\_sb\_pro\) application.

## Before you begin

-   Role required: admin, sn\_sb.admin
-   This version of Service Exchange requires a global script that must be installed before you set up the Service Exchange for Providers application. Follow instructions in [KB1225292](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1225292) on the Now Support instance to install the script.

## About this task

This one-time setup task must be completed from your ServiceNow instance.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Provider**.

2.  Enter a name for the provider.

    This can contain only alphanumeric characters and dashes. Names that include spaces or special characters result in an error.

3.  Click **Submit**.



```


### File: service-exchange\service-bridge-v2-offboard-consumer.md

```text
---
title: Off-board a Service Exchange consumer
description: Off-board an onboarded consumer and remove all related records.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Register a consumer, Use for providers, Service Exchange for Providers, Service Exchange]
---

# Off-board a Service Exchange consumer

Off-board an onboarded consumer and remove all related records.

## Before you begin

Role required: admin, sn\_sb.admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Consumers**.

2.  Select the **Number** column to open the consumer connection record.

3.  Select the **Off-Board Consumer** related link on the form.

    You see a confirmation message indicating that this action will off-board this connection and delete all related connection records.

4.  Select **OK** to off-board the consumer connection.

5.  If you want to delete all related tasks, select the **Delete all existing tasks for this connection** check box in the confirmation message, and enter **Delete** in the dialog box that appears and select **OK**.

    The consumer is off-boarded and all related data is deleted.


## Result

The following tables are deleted:

-   Connection tables:
    -   ih\_sync\_capture\_definition
    -   ih\_sync\_outbound\_definition
    -   ih\_sync\_inbound\_definition
    -   ih\_sync\_process\_event
    -   ih\_sync\_remote\_system
    -   http\_connection
    -   sys\_user
    -   sys\_user\_has\_role
    -   sys\_alias
    -   oauth\_2\_0\_credentials
    -   oauth\_credential
    -   oauth\_requestor\_profile
    -   oauth\_entity\_profile
    -   oauth\_entity
    -   sn\_sb\_rps\_connection
    -   sn\_transport\_queue
    -   sn\_transport\_profile
    -   sn\_sb\_pro\_registration
    -   sn\_sb\_pro\_service\_bridge\_settings
    -   sn\_sb\_pro\_authorized\_user
    -   sn\_sb\_pro\_consumer\_connection
    -   sn\_sb\_pro\_entitlement
-   Tasks \(records from the following tables are deleted only if you choose to delete all existing tasks\)
    -   sn\_sb\_pro\_provider\_task
    -   sn\_sb\_pro\_remote\_task

**Parent Topic:**[Register a Service Exchange consumer](service-bridge-v2-onboarding.md)


```


### File: service-exchange\service-bridge-v2-offboard-provider.md

```text
---
title: Off-board a Service Exchange provider
description: Off-board a provider connection and delete all related records.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Connect to a provider, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Off-board a Service Exchange provider

Off-board a provider connection and delete all related records.

## Before you begin

Role required: admin, sn\_sb.admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

2.  Click on the **Number** column to open the provider connection record.

3.  Click **Off-Board Provider**.

    You will see a confirmation message indicating that this action will off-board this connection and delete all related connection records.

4.  Click **OK** to off-board the provider connection.

5.  If you want to delete all related tasks, select the **Delete all existing tasks for this connection** checkbox in the confirmation message, and enter **Delete** in the dialog box that appears and click **OK**.

    The consumer will be off-boarded and all related data will be deleted.


## Result

The following tables are deleted:

-   Connection tables:
    -   ih\_sync\_capture\_definition
    -   ih\_sync\_outbound\_definition
    -   ih\_sync\_inbound\_definition
    -   ih\_sync\_process\_event
    -   ih\_sync\_remote\_system
    -   http\_connection
    -   sys\_user
    -   sys\_user\_has\_role
    -   sys\_alias
    -   oauth\_2\_0\_credentials
    -   oauth\_credential
    -   oauth\_requestor\_profile
    -   oauth\_entity\_profile
    -   oauth\_entity
    -   sn\_sb\_rps\_connection
    -   sn\_transport\_queue
    -   sn\_transport\_profile
    -   sn\_sb\_con\_service\_bridge\_settings
    -   sn\_sb\_con\_authorized\_user
    -   sn\_sb\_con\_persona
    -   sn\_sb\_con\_provider\_connection
    -   sn\_sb\_con\_entitlement
-   The following tables are deleted only if you select the **Delete all existing tasks for this connection** checkbox in the confirmation dialog:
    -   Tasks
        -   sn\_sb\_con\_provider\_task
        -   sn\_sb\_con\_remote\_task
    -   Entitlements
        -   sn\_sb\_con\_remote\_record\_producer
            -   item\_option\_new
            -   item\_option\_new\_set
        -   sn\_sb\_con\_remote\_task\_def \(and child tables\)
            -   sn\_sb\_con\_remote\_task\_variable
            -   sn\_sb\_con\_inbound\_field
            -   sn\_sb\_con\_outbound\_field


```


### File: service-exchange\service-bridge-v2-omt-intg.md

```text
---
title: Integration with Sales Customer Relationship Management
description: Providers can use Service Exchange to publish their product offers to a consumer using a Service Exchange Remote Record Producer.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange]
---

# Integration with Sales Customer Relationship Management

Providers can use Service Exchange to publish their product offers to a consumer using a Service Exchange Remote Record Producer.

Consumers can order a connected provider’s Sales Customer Relationship Management product offering from service catalogs in their ServiceNow instances, enabling faster order fulfillment, improved accuracy, and improved customer satisfaction. For more details, see [Order Management for providers with Service Exchange](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/order-management/service-bridge-om-for-providers.md).


```


### File: service-exchange\service-bridge-v2-onboarding.md

```text
---
title: Register a Service Exchange consumer
description: Registering a new consumer in Service Exchange establishes an instance-to-instance integration between a provider and a consumer.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Register a Service Exchange consumer

Registering a new consumer in Service Exchange establishes an instance-to-instance integration between a provider and a consumer.

## Before you begin

-   Role required: admin
-   A provider record must have been created. See [Set up a Service Exchange provider record](service-bridge-v2-new-provider.md).
-   A company or account must exist for the consumer in the provider’s instance, and a user or contact with the sn\_sb\_pro.consumer role must be associated with the company. If this is a production instance, the user must have a valid email address to receive the registration email.
-   Run the **Key Management** &gt; **Health \(Diagnostics\)** to ensure that the Key Management Framework health check has passed. Your administrator must have the sn\_kmf.admin and sn\_kmf.cryptographic\_manager roles to access the health diagnostics. If your administrator does not have access, follow the instructions in [Assign Key Management Framework roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/assign-kmf-roles.md) to grant the required roles.

## About this task

Register a new consumer by creating a registration task for the company and instance you want them to connect with. The company contact will receive an email when this registration task is created in a production instance or any other instance where email sending is enabled. If email sending is not enabled, the provider admin can copy the link from the registration task comments and send it to the consumer admin. The email contains instructions and a link that allows the consumer to complete the registration process.

**Note:** When setting up two instances for demonstration purposes, it is vital to ensure that the consumer contact matches the user who is currently logged into the provider instance when attempting to complete the registration from the consumer instance. In the consumer instance, selecting the **Connect to Provider** option will open an OAUTH page in the provider instance, where the consumer admin must authenticate the OAUTH token. If the contact listed on the registration task does not match the logged-in user, this process will fail.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Consumer Registrations** and select **New**.

2.  Enter the following details:

    -   Select the Company associated with the consumer instance being registered.
    -   Select the contact details associated with the Company you have selected.

        **Note:** This contact must be an admin user in the consumer instance, otherwise the registration process cannot be completed. On the provider instance, only a Service Exchange Consumer role is required.

    -   Select the **Lock** icon on the URL field and enter the URL of the consumer ServiceNow instance.
3.  Select **Save**.

    After you save the registration record, the state changes to **Awaiting Validation** while the pre-onboarding scan suite runs validation checks in the background.

    The validation state changes to either Open or Validation Failed.

    -   If all validation checks pass, the state changes to **Open**. An email is generated and sent to the consumer contact specified during registration if email sending is enabled. If email sending is not enabled, the admin must copy the link from the work notes and manually send it to the consumer admin. The consumer contact must follow the steps listed in the [Connect to a provider](service-bridge-v2-register.md) to complete the registration process on the consumer instance.
    -   If any validation checks fail, the state changes to **Validation Failed**. The registration record displays a validation failed banner indicating that one or more Pre-Onboarding suite checks did not pass with a link to the Health Dashboard. The consumer registration link is not generated until all issues are resolved.

If the state is **Validation Failed**, you must resolve all issues identified during the pre-onboarding checks.

1.  Select the **Health Dashboard** links validation failed banner at the top of the registration record.
2.  Review and resolve all the pre-onboarding scan issues.

    After all issues are resolved, the state automatically changes to Open and the registration process resumes.


-   **[Off-board a Service Exchange consumer](service-bridge-v2-offboard-consumer.md)**  
Off-board an onboarded consumer and remove all related records.

**Parent Topic:**[Using Service Exchange for providers](../concept/service-bridge-v2-administer.md)

**Related topics**  


[Service Exchange Center](../concept/se-se-center.md)

[Instance scan checks](../concept/service-bridge-v2-scan-checks.md)

[Connect to a provider](service-bridge-v2-register.md)


```


### File: service-exchange\service-bridge-v2-personas.md

```text
---
title: User roles for providers
description: Learn about the roles, skills, and tasks for the different users in the Service Exchange for Providers application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# User roles for providers

Learn about the roles, skills, and tasks for the different users in the Service Exchange for Providers application.

A user role is a pre-configured role in the application that is made up of multiple granular roles. The user roles are designed to correspond to the common job titles for managers, analysts, and service owners in an IT organization. If you want your users and groups to have more access than a role permits, you can add more granular roles to your users and groups. If you want to limit the access for specific users and groups at the task level, you can remove the granular roles. You can also build custom roles and access controls \(ACLs\) to suit your needs.

<table id="table_skr_1km_cmb"><thead><tr><th>

Persona

</th><th>

Skills

</th><th>

Tasks

</th><th>

Roles

</th></tr></thead><tbody><tr><td>

Developer

</td><td>

-   Is a certified ServiceNow administrator
-   Is a certified ServiceNow application developer

</td><td>

-   Creates provider connection records.
-   Creates and maintains remote task definitions and transforms.
-   Creates and maintains Workflow Studio flows to determine the request fulfillment processes.
-   Creates and maintains remote record producers.

</td><td>

-   admin
-   sn\_sb.admin

 **Note:** If the user does not have the admin role, the catalog admin role is required to modify and publish Remote Record Producers.

</td></tr><tr><td>

Administrator

</td><td>

Is a certified ServiceNow system administrator

</td><td>

-   Completes the Service Exchange registration requests.
-   Assists the consumer's system administrator as needed.
-   Publishes remote catalogs to the consumer's instance.
-   Publishes remote task definitions to the consumer's instance.
-   Troubleshoots Service Exchange transport payloads.

</td><td>

-   admin
-   sn\_sb.admin
-   sn\_transport.admin

</td></tr><tr><td>

Provider Fulfiller

</td><td>

Has agent skills

</td><td>

-   Resolves consumer questions and issues.
-   Engages in network operations when needed.

</td><td>

-   \*itil
-   sn\_sb.requestor
-   \*sn\_customerservice\_agent
-   \*incident\_read​
-   \*problem\_read​
-   \*change\_read

</td></tr><tr><td>

Consumer Requestor

</td><td>

End user

</td><td>

Makes requests from the Remote Catalog

</td><td>

sn\_sb.requestor

</td></tr></tbody>
</table>
```


### File: service-exchange\service-bridge-v2-proactive-case.md

```text
---
title: Proactive cases
description: Proactively notifies consumer users of case alerts and enables real-time collaboration with providers without any additional configuration in connected consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Proactive cases

Proactively notifies consumer users of case alerts and enables real-time collaboration with providers without any additional configuration in connected consumer instances.

A proactive case in Service Exchange is similar to the synchronization that occurs between a provider's and customer's instances when the customer submits a service request. However, in this case, the fulfillment process proactively triggers by alert monitoring.

After a customer on boards through Service Exchange, that customer gets notified of cases that are created from alert monitoring. Customers proactively receive up-to-date information about issues that affect them, and are informed about the progress of the resolution of those issues.

The process is as follows:

1.  An alert that is related to an on boarded Service Exchange customer triggers in the provider's instance, and a case record is created.
2.  A link to the provider task is added as a comment in that case.
3.  An automatic Customer Service Management notification is sent to the primary customer contact, and a link to the provider task is also included.
4.  Any state changes or additional comments that are added to the case record in the provider's instance appear in the customer's instance. The status change in the case triggers creation of a case on the provider's instance.

For more information about the Service Exchange synchronization for resolving cases, see [Fulfill a consumer request](service-bridge-v2-proactive-customer-care-csp.md).


```


### File: service-exchange\service-bridge-v2-proactive-customer-care-csp.md

```text
---
title: Fulfill a consumer request
description: Service Exchange Remote Catalog items are ordered from the consumer's ServiceNow instance, and they create provider tasks in each instance. The provider's agent fulfills these provider tasks in their ServiceNow instance. The data in these tasks is synchronized between instances so that they both can track the progress.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Fulfill a consumer request

Service Exchange Remote Catalog items are ordered from the consumer's ServiceNow instance, and they create provider tasks in each instance. The provider's agent fulfills these provider tasks in their ServiceNow instance. The data in these tasks is synchronized between instances so that they both can track the progress.

Some common Service Exchange Remote Catalog items are as follows:

-   Help requests
-   Service-affecting issues​
-   Requests for changes in service

## Service Exchange request fulfillment process

1.  The consumer selects a Service Exchange related item from the service catalog.
2.  The consumer provides the information in the Service Exchange request form and clicks **Submit**. When the consumer places the request, the Task View appears.

    Within the view, the consumer can add comments that are replicated in the provider's instance.

3.  In the consumer's instance, a single tracking task type, the Provider Task, is generated, regardless of the service.
4.  The Provider Task is replicated on the provider's instance, triggering a flow that triggers the parent task.
5.  The state of the task in the consumer's instance is set to Received.
6.  In the provider's instance, an agent takes ownership of the parent task by clicking **Assign to me**.
7.  After an agent takes ownership, the state of the Provider Task in the consumer's instance is updated to Work in Progress.

    When the agent posts a comment on the provider's instance, the comment is replicated in the consumer's instance. Comments that the consumer posts are replicated in the provider's instance.

8.  After the agent resolves the request, sets a resolution code, and clicks **Propose solution**, the state of the Provider Task in the consumer's instance is updated to Resolved.

    The Actions menu displays the following options, **Accept**, **Reject**, or **Cancel**.

9.  If the consumer accepts the resolution, the state of the provider task on the consumer's instance, and the state of the request on the provider's instance, are updated to **Closed**.

**Parent Topic:**[Using Service Exchange for providers](service-bridge-v2-administer.md)

**Related topics**  


[Create remote catalogs in Service Exchange for providers](service-bridge-v2-remote-catalog.md)


```


### File: service-exchange\service-bridge-v2-provider-tasks.md

```text
---
title: Provider tasks
description: Enable all providers using Service Exchange to be transparent and collaborative with their consumers who use ServiceNow.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Provider tasks

Enable all providers using Service Exchange to be transparent and collaborative with their consumers who use ServiceNow.

Provider tasks represent work that is being performed in a provider's ServiceNow instance and monitored in a consumer's instance. By using Provider Tasks, consumers can collaborate with all of their providers without the need for any additional configuration to their instances. For more information, see [Remote record producers in Service Exchange](service-bridge-v2-remote-record.md).

**Related topics**  


[Remote record producers in Service Exchange](service-bridge-v2-remote-record.md)


```


### File: service-exchange\service-bridge-v2-publish-con-fds-subscription.md

```text
---
title: Publish an outbound FDS subscription as a consumer
description: Publish the foundation data sync \(FDS\) subscription to complete the foundation data sync after the provider configures and accepts the subscription.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring outbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Publish an outbound FDS subscription as a consumer

Publish the foundation data sync \(FDS\) subscription to complete the foundation data sync after the provider configures and accepts the subscription.

## Before you begin

Role required: admin \(sb\_admin\)

## About this task

If the **Auto publish FDS subscriptions** option is not selected in your offering definition, you must manually publish each subscription after the provider accepts the subscriptions.

Publishing the subscription activates the data synchronization process and begins sending data to the provider according to the defined cadence.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Open Records** &gt; **FDS Request**.

2.  Open the FDS request by selecting the record number in the **Number** column.

3.  In the Foundation Data Consumer Outbound Subscriptions related list, open the foundation data subscription by selecting the record number in the **Number** column.

    Each subscription represents a specific table or data set that the provider has requested.

4.  Select **Publish**.

    You must publish each subscription that is accepted by your provider to activate the subscription and begin data synchronization.

    The subscription state changes to Published.


## Result

The foundation data subscription is now active. Data is synchronized to the provider instance based on the defined cadence and filter criteria.

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)


```


### File: service-exchange\service-bridge-v2-publish-fds-subscription.md

```text
---
title: Publish a foundation data subscription
description: Publish the foundation data sync \(FDS\) subscription to complete the foundation data sync after the consumer configures and accepts the subscription.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring outbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Publish a foundation data subscription

Publish the foundation data sync \(FDS\) subscription to complete the foundation data sync after the consumer configures and accepts the subscription.

## Before you begin

Role required: admin

## About this task

If the **Auto publish FDS subscriptions** option isn’t selected, you must manually publish each subscription.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Open Records** &gt; **FDS Request**.

2.  Open the provider offering request by selecting the record number in the **Number** column.

3.  From the Foundation Data Provider Subscriptions related list, open the foundation data provider subscription by selecting the record number in the **Number** column.

4.  Select **Publish**.

    You must publish each subscription that is accepted by your consumer to complete the FDS.



```


### File: service-exchange\service-bridge-v2-reference.md

```text
---
title: Service Exchange reference
description: Reference topics provide additional information about the Service Exchange data model and configuration.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Exchange]
---

# Service Exchange reference

Reference topics provide additional information about the Service Exchange data model and configuration.


```


### File: service-exchange\service-bridge-v2-register.md

```text
---
title: Connect to a provider
description: Complete the registration process to establish a connection to the provider instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Connect to a provider

Complete the registration process to establish a connection to the provider instance.

## Before you begin

-   Role required: admin
-   Run the **Key Management** &gt; **Health \(Diagnostics\)** to ensure that the Key Management Framework health check has passed. Your administrator must have the sn\_kmf.admin and sn\_kmf.cryptographic\_manager roles to access the health diagnostics. If your administrator does not have access, follow the instructions in [Assign Key Management Framework roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/platform-encryption/assign-kmf-roles.md) to grant the required roles.

## About this task

Before proceeding, the provider should have requested the contact details of an admin to set as the main point of contact on their registration record. This designated contact person will receive an email either from the provider's instance or directly from the provider's admin, containing a registration link. Clicking on this link will generate a Provider Connection record in your consumer instance. The following steps assume that you have already clicked the registration link.

## Procedure

1.  Select the **Connect to Provider** link sent in the provider's registration email or follow the link given to you directly by the provider’s admin.

    This link will generate the Provider connection record.

    **Note:** The consumer admin completing the registration process must be the named contact on the provider’s registration task or an admin in the provider's instance. Registration will fail during the OAUTH authentication step if attempted by another user.

2.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Provider Connections**.

3.  On the Provider Connection form in the consumer instance, select the name of the Company that the provider is associated with and select **Save**.

    After you save the provider connection record, the state changes to Awaiting Validation while the pre-onboarding scan suite runs validation checks on the background.

    -   If all validation checks pass, the state changes to Validated.
    -   If any validation checks fail, the state changes to Validation Failed. A banner appears at the top of the provider connection record indicating that one or more pre-onboarding suite checks did not pass, along with a link to the Health Dashboard. Review the Health Dashboard to fix the issues. When the all the issues are resolved, the connection automatically moves to Validated.
4.  Select **Connect to Provider** in the Provider connection record page.

    The **Connect to Provider** button is not available if there are any unresolved validation errors. Resolve all pre-onboarding scan issues before proceeding.

5.  Select **Authenticate** when the Service Exchange registration message appears.

    The OAuth authentication page appears.

6.  Select **Allow** and then select **Submit** to proceed with the registration.

    You are redirected to the Registration task where you can view the state. When registration is completed, a connection is established between the provider and the consumer instances, and the registration task State is set to **Closed Complete** on the provider's instance.


If the state is **Validation Failed**, you must resolve all issues identified during the pre-onboarding checks.

1.  Select the **Health Dashboard** link in the Validation Failed banner at the top of the Provider Connection record.
2.  Review and resolve all the pre-onboarding scan issues.

    After all issues are resolved, the state automatically changes to Open and the registration process resumes.


**Related topics**  


[Service Exchange Center](../concept/se-se-center.md)

[Instance scan checks](../concept/service-bridge-v2-scan-checks.md)

[Register a Service Exchange consumer](service-bridge-v2-onboarding.md)


```


### File: service-exchange\service-bridge-v2-remote-catalog.md

```text
---
title: Create remote catalogs in Service Exchange for providers
description: As a provider, you can create remote catalogs to automate the task fulfillment process for your consumers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Create remote catalogs in Service Exchange for providers

As a provider, you can create remote catalogs to automate the task fulfillment process for your consumers.

By using remote catalogs, providers can maintain the development of shared catalogs on their instances and provide consumers with native catalog items in their instances.

The process for providers to create a remote catalog is as follows:

1.  Create a remote record producer in a remote catalog. See [Create a remote record producers in a remote catalog in Service Exchange for Providers](../task/service-bridge-v2-create-remote-rec-prod.md).
2.  Create variables for remote record producers. See [Create variables for remote record producers in Service Exchange for Providers](../task/service-bridge-v2-assign-variables-ser-defn.md).
3.  Associate flows to the record producers.


```


### File: service-exchange\service-bridge-v2-remote-choice-fields.md

```text
---
title: Using remote choice fields to directly access provider data
description: Remote choice fields provide your consumers direct access to your \(provider\) data in real time while they submit a remote catalog item from their instance.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Remote catalogs, Explore, Service Exchange]
---

# Using remote choice fields to directly access provider data

Remote choice fields provide your consumers direct access to your \(provider\) data in real time while they submit a remote catalog item from their instance.

Remote choice fields enable consumers to view the choice list for a catalog reference field directly from the provider's instance. They provide the following advantages:

-   Removes the need to replicate foundation data.
-   Reduces the cost and maintenance of integrations.

You can control the data that your consumers access by defining a remote choice field. To learn more, see [Create remote choice definitions in Service Exchange for Providers](../task/service-bridge-v2-create-remote-choice-fld-defs.md).


```


### File: service-exchange\service-bridge-v2-remote-record.md

```text
---
title: Remote record producers in Service Exchange
description: Remote record producers in Service Exchange for Providers are service requests published in consumer instances. They enable your consumer to request provider services through their service catalog.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Remote catalogs, Explore, Service Exchange]
---

# Remote record producers in Service Exchange

Remote record producers in Service Exchange for Providers are service requests published in consumer instances. They enable your consumer to request provider services through their service catalog.

## Overview of record producers

Remote record producers contain the variables that determine the information that a consumer can or must provide to submit a request. When a remote record producer is submitted from the consumer's service catalog, it generates a Provider Task record on the provider's instance and triggers a Create Case, Create Incident, or Create Change Request fulfillment task.

As the task moves through the fulfillment flow in the provider's instance, updates are visible in both the provider and the consumer's ServiceNow instances.

The remote record producer table is an extension of the sc\_cat\_item\_producer table and uses the sn\_sb\_pro\_remote\_request table.


```


### File: service-exchange\service-bridge-v2-remote-task-connect-disconnect.md

```text
---
title: Connect and Disconnect remote tasks
description: Remote tasks associated with active remote task definitions enable you to sync data between two parent tasks on the provider and consumer instances.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create remote tasks to sync data, Use for consumers, Service Exchange for Consumers, Service Exchange]
---

# Connect and Disconnect remote tasks

Remote tasks associated with active remote task definitions enable you to sync data between two parent tasks on the provider and consumer instances.

When you create a remote task for an active remote task definition, the Status of the remote task is set to **Connected** on the provider and consumer instances if there are no errors. This ensures that the remote task syncs data including field updates, attachments, and comments between the parent tasks.

To stop synching of data between the instances, navigate to the Remote Task page on the provider or consumer instance and click **Disconnect**. When disconnected, the remote task pauses copying or transfer of data including work notes and comments between the instances.

**Note:** To resume syncing of data, you can navigate to the Remote Task page and click **Connect**. This option works only if the existing configuration is valid and has not been modified, and the remote task definition is active.


```


### File: service-exchange\service-bridge-v2-remote-task-create.md

```text
---
title: Create remote tasks to sync data
description: Remote tasks provide linked tasks across multiple instances and enable business workflows without any custom integrations.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Use for consumers, Service Exchange for Consumers, Service Exchange]
---

# Create remote tasks to sync data

Remote tasks provide linked tasks across multiple instances and enable business workflows without any custom integrations.

## Before you begin

-   Role required: admin
-   Remote task definition must already exist.

## About this task

As a consumer, you can integrate tasks like incidents, cases, and service requests bi-directionally with your providers using remote tasks.

## Procedure

1.  Navigate to **All** &gt; **Incidents** &gt; **Open**.

2.  Click on the **Number** link to open an incident.

3.  Click **Create Remote Task for Provider** in the Related Links section.

    **Note:** The **Create Task for Provider** link appears in this section only if at least one active and valid remote task definition is available for the provider table associated with the task.

4.  The Remote Task page appears.

    In the Remote Task page, the Parent field is populated with the task record and the Status field is set to New.

5.  Select a Remote Task Definition from the list.

    **Note:**

    -   Only active and valid remote task definitions associated with the parent task are displayed.
    -   The Provider Connection field is automatically filled in based on the Remote Task Definition selected.
    -   If only one Remote Task Definition is available, the Remote Task Definition field is automatically populated.
6.  Click **Submit**.

    When you navigate back to the parent task, you can see the newly created remote task in the Remote Tasks related list.

    **Note:** The Remote Task is created asynchronously and may not show initially if the parent task form is quickly loaded. You may need to refresh the form to see the newly created Remote Task.

7.  Navigate to **Service Exchange Consumer** &gt; **Remote Tasks**.

    The list of remote tasks is displayed. When the newly created Remote Task is received in the provider instance, a new parent task based on the Remote Task is created.

8.  Click on the newly created task and then click on the remote task under the Remote Tasks tab in the Related Links section.

    You can see the Status field is set to Connected and that the description has been updated.

9.  Navigate back to the parent task.

10. Update the Short Description for the parent task and click **Save**.

11. Log into the consumer instance and open the task.

    You can see that the data has been synced and Short Description field has been updated in the consumer instance. You can also see a work note indicating that the Short Description has been updated by the provider.

    **Note:**

    -   You can create a remote task on the provider instance by following the same steps. Data is synced between the consumer and provider instances and any changes you make in the consumer instance are automatically updated in the provider instance.
    -   Once an attachment is shared with another instance through Service Exchange using a remote task or a provider task, it becomes part of that instance’s data. Service Exchange does not delete attachments on remote instances — the receiving instance must handle deletion.
    -   When you create a remote task on the consumer instance, the Provider Connection field is automatically populated when you select a Remote Task Definition.


```


### File: service-exchange\service-bridge-v2-remote-task-overview.md

```text
---
title: Remote tasks
description: Learn how you, as a provider, can resolve and fulfill multiple consumer tasks, such as incidents, cases, and service requests, by using remote tasks. Also as a consumer, you can assign the incidents to multiple providers for resolution.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Remote tasks

Learn how you, as a provider, can resolve and fulfill multiple consumer tasks, such as incidents, cases, and service requests, by using remote tasks. Also as a consumer, you can assign the incidents to multiple providers for resolution.

Remote tasks enable you to assign and synchronize the task's data on separate instances so that you can quickly fulfill the service requests from your consumers. Some examples of the consumer requests are as follows:

1.  Request help for issues that your consumers are having with your services.​
2.  Request for service changes to the services that your consumers have purchased.
3.  Request to assign the existing tasks to you so that you can support your consumer's issues​.

## How a remote task works

As a provider, you must first create and publish the remote task definitions that your consumers can use for creating a remote task. You entitle these definitions to your consumers who can adjust the mappings and field data rules or simply activate the definition. Your consumers can apply a trigger on the definition or manually create a remote task for you, the provider, based on an active definition.

For more information, see [Create a remote task definition in Service Exchange for Providers](../task/service-bridge-v2-create-remote-tasks-defs.md).

The remote task feature includes a Remote Task table, which is an extension of the Task table in the ServiceNow AI Platform. With remote tasks, you can enable bidirectional linking of workflows between multiple ServiceNow instances.

**Note:** When data, such as an attachment or task, is shared with another instance through Service Exchange, it becomes part of that instance’s data. Service Exchange does not delete data on remote instances; the receiving instance must handle the deletion if required.

For example, an incident on a consumer instance must be assigned to a provider's instance as a case. The Remote Task record in each instance facilitates the bidirectional flow of the task's data between the case and the incident.


```


### File: service-exchange\service-bridge-v2-request-fds-offering-consumers.md

```text
---
title: Request foundation data sync offerings from a consumer
description: Request a foundation data sync \(FDS\) offering from your consumer to receive foundational data.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [foundation data sync, FDS offerings, request offering, provider inbound, receive data]
breadcrumb: [Configure inbound FDS as providers, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Request foundation data sync offerings from a consumer

Request a foundation data sync \(FDS\) offering from your consumer to receive foundational data.

## Before you begin

Role required: admin \(sb\_admin\)

## About this task

Browse and request FDS offerings that consumers have published. After you submit a request, the consumer is notified and can acknowledge your request.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Provider** &gt; **Request FDS Offerings**.

2.  From the **Offerings** drop-down menu, select your consumer.

3.  From the list of offerings, select an offering.

    You can select more than one offering to request multiple datasets from the same consumer.

4.  In the Additional details section, specify the sync interval and UTC time to define the data sync schedule.

    The sync interval determines how frequently data is synchronized from the consumer instance to your provider instance.

5.  In the **Share any additional changes to the offering** field, add information about any changes you want.

    Use this field to communicate specific requirements or customizations to the consumer, such as additional field mappings or filter conditions.

6.  Select **Submit**.


## Result

A provider offering request is created. After the provider offering is created, a corresponding record is generated in your consumer's instance.

The request state displays as Received until the consumer acknowledges it. If the consumer has enabled auto-acknowledge, and you’ll receive a sample payload automatically and the state changes to Work In Progress. Otherwise, you must wait for the consumer to acknowledge your request.

## What to do next

[Validate FDS subscriptions items as a provider](service-bridge-v2-fds-validate-subs-items-provider.md)

**Related topics**  


[Foundation data sync](../concept/service-bridge-v2-explore-foundation-data-sync.md)

[Configuring inbound foundation data sync as providers](../concept/service-bridge-v2-configure-inboun-fds-providers.md)

[Configuring outbound foundation data sync as consumers](../concept/using-provider-bound-fds-consumer.md)


```


### File: service-exchange\service-bridge-v2-request-fds-offerings.md

```text
---
title: Request foundation data sync offerings
description: Request a foundation data sync \(FDS\) offering from your provider to receive foundational data.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configuring inbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Request foundation data sync offerings

Request a foundation data sync \(FDS\) offering from your provider to receive foundational data.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **Request FDS Offerings**.

2.  From the **Offerings** drop-down menu, select your provider.

3.  From the list of offerings, select an offering.

    You can select more than one offering.

4.  In the Additional details section, specify the sync interval and UTC time to define the data sync schedule.

5.  In the **Share any additional changes to the offering** field, add information about any changes you want.

6.  Select **Submit**.


## Result

A consumer offering request is created, and the state changes to Work in Progress. After the consumer offering is created, a corresponding record is generated in your provider's instance.

## What to do next

[Validate the subscription](service-bridge-v2-validate-fds-subscription.md) to start receiving foundation data.


```


### File: service-exchange\service-bridge-v2-scan-checks.md

```text
---
title: Instance scan checks
description: Instance scan checks in Service Exchange proactively identify issues and system inconsistencies, helping administrators maintain system health and reduce downtime. The health dashboard displays findings, errors, and check statuses, helping you quickly identify and resolve problems.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Explore, Service Exchange]
---

# Instance scan checks

Instance scan checks in Service Exchange proactively identify issues and system inconsistencies, helping administrators maintain system health and reduce downtime. The health dashboard displays findings, errors, and check statuses, helping you quickly identify and resolve problems.

Service Exchange scan checks provide the following benefits:

-   Reduce case task loads and promote stability and reliability of Service Exchange integrations.
-   Reduce downtime and troubleshooting efforts by identifying issues early.
-   Provide known errors with detailed solutions.
-   Improve overall productivity through automation and visibility.

## Supported Service Exchange scan checks

Service Exchange provides two main suites, on-demand and scheduled.

Each suite contains multiple child suites and each child suite contains multiple scan checks. For more information on suite and scan checks, see [Instance Scan](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-landing-page.md).

-   On-demand suites: On-demand checks can be run as and when required.
-   Scheduled suites: Scheduled checks run at a scheduled time every day.

You can also customize when scheduled suites run or assign a scheduled execution time to on-demand suites.

To view the list of Service Exchange supported scan checks, see [List of scan checks](../reference/service-bridge-v2-list-of-scan-checks-in-sb.md).

These Service Exchange scan checks are available through the Service Exchange Health plugin. This plugin is activated when you install or upgrade Service Exchange. You can also activate this plugin manually. For activation instruction, see [Activate a plugin](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_ActivateAPlugin.md).

**Note:** The Service Exchange Health plugin is backward compatible. If you're using an older version of the Service Exchange application, you can install this plugin to use its features.

## Health Dashboard

The Service Exchange Health Dashboard consolidates findings, errors, and scan task statuses into a single view. You can select any widget to view information about the scan checks.

Each scan task includes a work note that contains a link to relevant known error documentation. This documentation provides step-by-step guidance that may help you resolve the problem.

You can access the Health Dashboard from the Service Exchange **Administration** menu.

**Related topics**  


[List of scan checks](../reference/service-bridge-v2-list-of-scan-checks-in-sb.md)


```


### File: service-exchange\service-bridge-v2-scratchpad-consumer.md

```text
---
title: Using the Scratchpad for Service Exchange tasks
description: The Scratchpad feature facilitates exchange of data between provider and consumer instances while performing Service Exchange tasks.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for consumers, Service Exchange for Consumers, Service Exchange]
---

# Using the Scratchpad for Service Exchange tasks

The Scratchpad feature facilitates exchange of data between provider and consumer instances while performing Service Exchange tasks.

Both providers and consumers can add, update, and remove information to and from the Scratchpad table. See [Using the Scratchpad for Service Exchange tasks](service-bridge-v2-scratchpad.md) for detailed information on how to use the Scratchpad feature.


```


### File: service-exchange\service-bridge-v2-scratchpad.md

```text
---
title: Using the Scratchpad for Service Exchange tasks
description: The Scratchpad feature facilitates exchange of additional data between provider and consumer instances while performing Service Exchange tasks.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use for providers, Service Exchange for Providers, Service Exchange]
---

# Using the Scratchpad for Service Exchange tasks

The Scratchpad feature facilitates exchange of additional data between provider and consumer instances while performing Service Exchange tasks.

Both providers and consumers can add, update, and remove information to and from the Scratchpad table. Using server side scripts, name-value pairs are associated with Provider Tasks and Remote tasks and this data is automatically synced between the instances. Shared data must be associated with a Provider or a Remote Task, and is automatically synced if the associated task is active.

The PSBScratchpadUtil API allows providers to share extra information that is outside of any other Service Exchange service, with their consumers. See [PSBScratchpadUtil - Scoped](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/PSBScratchpadUtilScopedAPI.md) for more details.

The CSBScratchpadUtil API allows consumers to share extra information that is outside of any Service Exchange service with their providers. See [CSBScratchpadUtil - Scoped](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/server-api-reference/CSBScratchpadUtilScopedAPI.md) for more details.

**Note:**

-   If the associated task is deactivated or deleted, the scratchpad data is deleted after 3 days. This setting can be modified using the `sn_sb.scratchpad.autodelete.days` property.
-   Each task can have a maximum of 50 scratchpad entries.
-   Data in the scratchpad cannot exceed 4000 characters.

**Example Scratchpad use case:** This example shows how data in the Scratchpad is synced between the consumer and provider instances.

-   A consumer orders a laptop from the local catalog. The local catalog in this case is a [Remote Record Producer](service-bridge-v2-remote-record.md).
-   This request is immediately forwarded the provider and appears as a Provider Task on the provider's instance.
-   The provider then selects a laptop from the inventory, sets it up and adds relevant information like the serial number, model, configuration to the Scratchpad which is automatically sent to the consumer.
-   On the consumer's instance, the Scratchpad data is retrieved and updated on the local database.
-   The laptop is then assigned to the consumer.

**Parent Topic:**[Using Service Exchange for providers](service-bridge-v2-administer.md)


```


### File: service-exchange\service-bridge-v2-transform-about.md

```text
---
title: Transform data with the Service Exchange transform framework
description: Use the Transform Framework to integrate tasks between two ServiceNow instances to transform remote task data in the Service Exchange application.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Remote tasks, Explore, Service Exchange]
---

# Transform data with the Service Exchange transform framework

Use the Transform Framework to integrate tasks between two ServiceNow instances to transform remote task data in the Service Exchange application.

As a provider, you can use the Transform Framework to transform your inbound and outbound data \(such as incidents, cases, and service requests\) of the remote tasks between your ServiceNow instance and your consumer's instance. To learn what a remote task is, see [Remote tasks](service-bridge-v2-remote-task-overview.md).

While using the Service Exchange for Providers application, you and your consumer can exchange the remote task data through tables and fields. The Transform Framework helps you to convert the data between those tables and fields so that you and your consumer can easily communicate with each other while resolving the incidents, cases, and consumer requests. Transforms can be created once and used across all remote task definitions.

You can use the following transform types in the Transform Framework for your remote tasks:

-   **Simple**: Select the simple transform option to use the predefined values of the inbound and outbound fields for your remote tasks. For example, by using this transform type, you’re converting the Open state of an incident in the provider's ServiceNow® instance to the In Progress state in the consumer's ServiceNow instance.
-   **Advanced**: Use an advanced transform where you run a script to determine the inbound and outbound data values for your remote tasks. For example, use this transform type to convert an incoming sys\_id into a correlated sys\_id for a reference field.
-   **Virtual Inbound**: Use this to transform or set a value for an Inbound Virtual field. This option uses a script to transform the data and adds a mandatory Inbound Field field.
-   **Virtual Outbound**: Use this to transform or set a value for an Outbound Virtual field. This option uses a script to transform the data and adds a mandatory Outbound Field field.
-   **Global**: Use the global transform option to create a default transform definition that can be applied to all consumer accounts.

    **Note:** A matching company or account specific transform overrides the Global transform option.


To learn how to create a transform, see [Create a transform in Service Exchange](../task/service-bridge-v2-create-transform.md).


```


### File: service-exchange\service-bridge-v2-using-foundation-data-sync-for-consumer.md

```text
---
title: Configuring inbound foundation data sync as a consumer
description: As a consumer, receive the foundation data from your provider using foundation data sync \(FDS\).
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Configuring inbound foundation data sync as a consumer

As a consumer, receive the foundation data from your provider using foundation data sync \(FDS\).

Before you use FDS, you must request and configure foundation data. After your provider creates and publishes the FDS definitions, request and configure FDS.

<table id="table_tqf_wwj_5fc"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[Request a foundation data offering.](../task/service-bridge-v2-request-fds-offerings.md)

</td><td>

Requests FDS offerings from your provider based on the published offerings.After you request a foundation data offering, your provider acknowledges your FDS request and sends a sample payload for each subscription.

</td></tr><tr><td>

2.

</td><td>

[Configure the sample data and validate subscription items.](../task/service-bridge-v2-validate-fds-subscription.md)

</td><td>

Configure the incoming data based on the CMDB or non-CMDB table to validate subscription items.After you validate subscription items, you must accept the subscription.

</td></tr><tr><td>

3.

</td><td>

[Accept the subscription](../task/service-bridge-v2-accept-fds-subscription.md)

</td><td>

Accept the subscription.After you accept the subscription, your provider publishes the subscription and data synchronizes according to the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[Foundation data sync](service-bridge-v2-explore-foundation-data-sync.md)


```


### File: service-exchange\service-bridge-v2-using-foundation-data-sync.md

```text
---
title: Configuring outbound foundation data sync as providers
description: As a provider, share foundational data with your consumer using foundation data sync \(FDS\).
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Configuring outbound foundation data sync as providers

As a provider, share foundational data with your consumer using foundation data sync \(FDS\).

Before using FDS, you must configure it.

<table id="table_tqf_wwj_5fc"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[Create an FDS Definition.](../task/service-bridge-v2-create-fds-offering-definition.md)

</td><td>

Define the data that you want to share with your consumer.After you create and publish an FDS definition, wait for your consumers to request FDS offerings based on the published definition.

</td></tr><tr><td>

2.

</td><td>

[Acknowledge FDS requests and send a sample payload.](../task/service-bridge-v2-acknowledge-FDS-request.md)

</td><td>

After receiving an FDS request from your consumer, acknowledge it and send a sample payload for each subscription.After you send the payload, your consumer configures the incoming data for each subscription and accepts it.

</td></tr><tr><td>

3.

</td><td>

[Publish subscriptions.](../task/service-bridge-v2-publish-fds-subscription.md)

</td><td>

After the consumer accepts the subscription, publish it.After the FDS configuration is complete, data starts synchronizing with the consumer based on the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[Foundation data sync](service-bridge-v2-explore-foundation-data-sync.md)

[Configuring inbound foundation data sync as a consumer](service-bridge-v2-using-foundation-data-sync-for-consumer.md)


```


### File: service-exchange\service-bridge-v2-validate-fds-subscription.md

```text
---
title: Validate foundation data sync subscription items
description: Configure the sample data received from the provider to validate a foundation data sync \(FDS\) subscription item.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring inbound FDS as consumers, Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Validate foundation data sync subscription items

Configure the sample data received from the provider to validate a foundation data sync \(FDS\) subscription item.

## Before you begin

Role required: admin

## About this task

After you create an FDS offering request, the provider acknowledges the request and sends you a sample payload. This payload helps you understand the structure and type of data you’ll receive.

After the provider sends the sample, a subscription is generated for each offering in the FDS offering request and each subscription contains a subscription item for each table the provider is sharing. You must configure the incoming sample data to validate the FDS subscription items.

## Procedure

1.  Navigate to **All** &gt; **Service Exchange Consumer** &gt; **FDS Requests**.

2.  Select the request.

3.  From the Foundation Data Consumer Subscriptions related list, open the consumer subscription by selecting the record number in the **Number** column.

4.  From the Subscription Items related list, open the subscription item by selecting the record number in the **Number** column.

5.  Configure incoming data using either IntegrationHub ETL or a transform map depending on whether you are working with a Configuration Management Database \(CMDB\) or a non-CMDB table.

<table id="choicetable_msz_gll_sfc"><thead><tr><th align="left" id="d25756e113">

Option

</th><th align="left" id="d25756e116">

Description

</th></tr></thead><tbody><tr><td id="d25756e122">

**Configure data integration for CMDB tables**

</td><td>

1.  Select the **ETL Transform Map Assistance** button.

A message is displayed stating that you’re about to navigate to the ETL Transform Map Assistant guided setup.

2.  Confirm your choice by selecting **OK**.
3.  Use the guided setup to complete the mapping to integrate third-party data into CMDB. For details, see [IntegrationHub ETL](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/integration-hub-etl/integrationhub-etl.md).

**Note:** Since FDS provides display values for reference fields, if you want to use reference data, you must create a table lookup transform mapping to retrieve the Sys ID from the reference table. For more details, see [Foundation Data Sync :: Known issues and workarounds \[KB2299760\]](https://support.servicenow.com/kb?id=kb_article_view&sys_kb_id=8a2b463c873aaadc57288519dabb354b)

4.  Close the browser tab to return to the Subscription Item page.


</td></tr><tr><td id="d25756e166">

**Configure data integration for non-CMDB table**

</td><td>

1.  Select the **Transform Map** button.

A message is displayed stating that you’re about to navigate to the Transform Map to complete the configuration.

2.  Confirm your choice by selecting **OK**.
3.  Complete the configuration. For details, see [Create a transform map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/system-import-sets/t_CreateATransformMap.md).
4.  Close the browser tab to return to the Subscription Item page.


</td></tr></tbody>
</table>    You must configure incoming data for each subscription item except dependent subscription items.


## Result

After you complete the configuration, the state of the subscription item and of the subscription changes to Validated.

## What to do next

[Accept the subscription](service-bridge-v2-accept-fds-subscription.md).


```


### File: service-exchange\service-bridge-v2-variable-sets.md

```text
---
title: Using variable sets with Remote Record Producers
description: Use single and multi-row variable sets with remote record producers.
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create remote catalogs, Configure for providers, Service Exchange for Providers, Service Exchange]
---

# Using variable sets with Remote Record Producers

Use single and multi-row variable sets with remote record producers.

Variable sets allow you to create a collection of variables that can be reused across multiple catalog items and order guides. Using variable sets saves time because you do not have to create the same variables individually for many catalog items. Also, when variables should be modified, you can modify the variable set and the changes are reflected across all the remote record producers that are associated with the variable set.

As a provider, you can create and associate variable sets with remote record producers. Any changes made to these variable sets are automatically synced to the remote record producers that the consumers are entitled to. You can create the following types of variable sets:

-   Single-row variable set: Use a single-row variable set to capture data from variables that are grouped together.
-   Multi-row variable set: Use a multi-row variable set to capture variable data in a grid layout for a group of entities. For example, for HR during the reorganization of employees, a single remote record producer should be able to capture the relevant information such as the department and manager for a group of employees.

**Note:**

-   Variable sets containing variables with unsupported variable types \(Custom, Custom with Label, and UIPage\) will not be synced until the invalid variables are removed.
-   Remote record producers containing invalid variable sets cannot be published. To publish the remote record producer, you must either resolve the validation issues or unassign the invalid variable set from the remote record producer.

For more details on variable sets and how they are used, see [Service catalog variable sets](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/c_ServiceCatalogVariableSets.md).


```


### File: service-exchange\tmt-service-bridge-both-landing-page.md

```text
---
title: Service Exchange
description: ServiceNow Service Exchange connects multiple ServiceNow instances to provide seamless support and service experiences across the ecosystem, from enterprise customers to suppliers and system integrators. Service Exchange provides a frictionless experience that makes it easy to collaborate and process requests while giving users the convenience of working in their own ServiceNow instance.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
---

# Service Exchange

ServiceNow® Service Exchange connects multiple ServiceNow instances to provide seamless support and service experiences across the ecosystem, from enterprise customers to suppliers and system integrators. Service Exchange provides a frictionless experience that makes it easy to collaborate and process requests while giving users the convenience of working in their own ServiceNow instance.

## Get started

<table id="table_k52_dyx_yxb" class="nav-card"><tbody><tr><td>

[Explore![](../../../reuse/icons/brand-icons/bus-explore.svg)Learn about the benefits of Service Exchange and how it is used.](../../tmt-service-bridge-2/concept/service-bridge-v2-exploring-service-bridge.md)

</td><td>

[Configure for providers![](../../../reuse/icons/brand-icons/bus-optimize-manage.svg)Learn how to install and configure Service Exchange for providers.](../../tmt-service-bridge-2/concept/service-bridge-v2-configure-provider.md)

</td><td>

[Configure for consumers![](../../../reuse/icons/brand-icons/bus-sdlc.svg)Learn how to install and configure Service Exchange for consumers.](../../tmt-service-bridge-2/concept/service-bridge-v2-install.md)

</td></tr><tr><td>

[Integrate![](../../../reuse/icons/brand-icons/bus-switch.svg)Extend Service Exchange capabilities by integrating with other applications.](../../tmt-service-bridge-2/concept/service-bridge-v2-omt-intg.md)

</td><td>

[Create remote record producers![](../../../reuse/icons/brand-icons/bus-service-catalog.svg)Offer catalog items to a consumer using remote catalog.](../../tmt-service-bridge-2/task/service-bridge-v2-create-remote-rec-prod.md)

</td><td>

[Configure outbound FDS for providers![](../../../reuse/icons/brand-icons/bus-transaction.svg)Configure outbound foundation data sync \(FDS\) settings for provider instances.](../../tmt-service-bridge-2/concept/service-bridge-v2-using-foundation-data-sync.md)

</td></tr><tr><td>

[Configure outbound FDS for consumers![](../../../reuse/icons/brand-icons/bus-transaction-data.svg)Configure outbound foundation data sync settings \(FDS\) for consumer instances.](../../tmt-service-bridge-2/concept/using-provider-bound-fds-consumer.md)

</td><td>

[Create remote task definitions![](../../../reuse/icons/brand-icons/bus-learn.svg)Create remote task definitions to define the task types that can be shared across connected instances.](../../tmt-service-bridge-2/task/service-bridge-v2-create-remote-tasks-defs.md)

</td><td>

[Reference![](../../../reuse/icons/brand-icons/bus-work-order.svg)Get additional details about Service Exchange, including data model, error log, and cloning instances.](../../tmt-service-bridge-2/reference/service-bridge-v2-reference.md)

</td></tr></tbody>
</table>## Additional resources

-   Learn more about what's new and changed, see the [Service Exchange \(formerly Service Bridge\) release notes](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/release-notes/service-bridge-rn.md).
-   Access real-time courses, self-paced training, and career resources at [ServiceNow University](https://learning.servicenow.com/lxp/en/pages/servicenow)
-   Connect with other Service Exchange users at [Now Community](https://www.servicenow.com/community/).
-   Find useful resources related to your role and explore best practices at the [Customer Success Center](https://www.servicenow.com/success.html).
-   View KB articles at [Service Exchange Knowledge Base.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1509053)
-   Access Service Exchange product page from [Service Exchange product](https://www.servicenow.com/products/service-bridge.html).


```


### File: service-exchange\using-provider-bound-fds-consumer.md

```text
---
title: Configuring outbound foundation data sync as consumers
description: As a consumer, share foundational data with your provider using foundation data sync \(FDS\).
locale: en-US
release: australia
product: Service Exchange
classification: service-exchange
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure for consumers, Service Exchange for Consumers, Service Exchange]
---

# Configuring outbound foundation data sync as consumers

As a consumer, share foundational data with your provider using foundation data sync \(FDS\).

<table id="table_msw_fm4_4hc"><thead><tr><th>

Step

</th><th>

Action

</th><th>

Description

</th></tr></thead><tbody><tr><td>

1.

</td><td>

[Create an FDS Definition.](../task/service-bridge-v2-create-provider-bound-fds-consumer.md)

</td><td>

Define the data that you want to share with your provider.After you create and publish an FDS definition, wait for your provider to request FDS offerings based on the published definition.

</td></tr><tr><td>

2.

</td><td>

[Acknowledge FDS requests and send a sample payload.](../task/service-bridge-v2-con-acknowledge-fds-request.md)

</td><td>

After receiving an FDS request from your provider, acknowledge it and send a sample payload for each subscription.After you send the payload, your provider configures the incoming data for each subscription and accepts it.

</td></tr><tr><td>

3.

</td><td>

[Publish subscriptions.](../task/service-bridge-v2-publish-con-fds-subscription.md)

</td><td>

After the provider accepts the subscription, publish it.After the FDS configuration is complete, data starts synchronizing with the provider based on the defined cadence.

</td></tr></tbody>
</table>**Related topics**  


[Foundation data sync](service-bridge-v2-explore-foundation-data-sync.md)


```
