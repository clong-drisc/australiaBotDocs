# core-business-suite



---

## Folder: core-business-suite



### File: core-business-suite\activate-ai-search.md

```text
---
title: Activate AI Search
description: Activate AI Search to enable conversational search capabilities in Now Assist for Core Business Suite.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-05"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Activate AI Search

Activate AI Search to enable conversational search capabilities in Now Assist for Core Business Suite.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **AI Search** &gt; **AI Search Status**.

2.  Select **Request AI Search**.

    A message confirms that the AI Search activation request has been submitted.

    **Note:** AI Search activation is processed in the background.

3.  Navigate again to **All** &gt; **AI Search** &gt; **AI Search Status**.

    When activation is complete, the status indicates that AI Search is ready.

    For more information about the AI Search, see [AI Search](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/ai-search/overview-ais.md).


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\activate-cbs-bu-version.md

```text
---
title: Enable Core Business Suite Foundation business units
description: If you’re using any standard business unit included in Core Business Suite Foundation, update the system properties to enable the Core Business Suite business units for installation.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-06"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Enable Core Business Suite Foundation business units

If you’re using any standard business unit included in Core Business Suite Foundation, update the system properties to enable the Core Business Suite business units for installation.

## Before you begin

**Note:**

-   If you are already using a standard business unit such as Human Resources, Finance, Health and Safety, Legal, Workplace Services, or Source‑to‑Pay that is included in Core Business Suite Foundation, the Core Business Suite business unit does not appear in the installation section.
-   After you update the required system properties, the Core Business Suite business unit appears in the installation section.
-   After you install a Core Business Suite business unit and apply the default configurations, the existing business unit customizations such as notifications and intake forms are overridden.

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Properties** &gt; **All Properties**.

2.  In the name column, search for **\*cbs**.

    The search lists all Core Business Suite business unit system properties records:

    -   `sn_cbs.override_WSD_tile`
    -   `sn_cbs.override_HEALTH_tile`
    -   `sn_cbs.override_FINANCE_tile`
    -   `sn_cbs.override_HR_tile`
    -   `sn_cbs.override_LEGAL_tile`
    -   `sn_cbs.override_S2P_tile`
3.  Select the system property record for the required business unit.

4.  In the notification bar, select **here** to edit the record in the Core Business Suite application.

5.  Set the value field to **true**.

6.  Select **Update**.


## Result

The Core Business Suite business unit appears in the installation section.

**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\assign-cbs-requestor-role.md

```text
---
title: Assign the CBS Requester role
description: Assign the CBS requester role to enable users to access services and submit requests through Employee Center.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-27"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Assign the CBS Requester role

Assign the CBS requester role to enable users to access services and submit requests through Employee Center.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  From the Configuration Summary navigation menu, select **Requestor role** under Requester experience.

5.  Select **Requestor role configuration**.

    **Note:** The CBS requester role is preassigned to the CBS requesters group.

6.  To add users to the group.

    1.  Select the **Group members** tab.
    2.  Select **New**.
    3.  On the form, fill in the fields and select **Submit**.

        For more information to fill a new member form, see [New member form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/critical-event-management/new-member-form.md).

7.  On the manage requester role page, select **Mark as configured**.


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\cbs-admin-role.md

```text
---
title: Assign the CBS admin role
description: Assign the CBS Admin role to grant users full administrative access to configure Core Business Suite.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Assign the CBS admin role

Assign the CBS Admin role to grant users full administrative access to configure Core Business Suite.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Organization** &gt; **Users**.

2.  Search for and select the user from the user column.

3.  In the selected user record, select the **Roles** tab.

4.  Select **Edit**.

5.  In the collection list, search for and select sn\_cbs.admin.

6.  Add the role to the Roles list by selecting the right arrow.

7.  Select **Save**.


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\cbs-default-configs.md

```text
---
title: Core Business Suite Foundation default configurations
description: Details of the default configurations for Core Business Suite Foundation.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-28"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite Foundation, Configure, Core Business Suite]
---

# Core Business Suite Foundation default configurations

Details of the default configurations for Core Business Suite Foundation.

These default configurations are applied automatically when Apply default configurations is selected during installation.

<table id="table_hwg_l3x_43c"><thead><tr><th>

configuration

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Now Assist

</td><td>

Enables the Now Assist Virtual Agent in the Employee center.

</td></tr><tr><td>

Employee Center configuration

</td><td>

Applies default Employee Center settings to establish the Core Business Suite user experience and navigation, including:-   Taxonomy – Structures content and topic pages within Employee Center.
-   Navigation – Defines how employees browse and access core services.
-   Home page – Configures the layout and components of the employee landing page.
-   Quick links – Provides shortcuts to frequently used tools and resources.

</td></tr></tbody>
</table>**Parent Topic:**[Install Core Business Suite Foundation](../task/set-up-cbs.md)


```


### File: core-business-suite\cbs-landing.md

```text
---
title: Core Business Suite
description: Core Business Suite \(CBS\) lays the foundation to unify disjointed processes. It’s a collection of modules that fulfills different business needs, for different personas, within a single product suite.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
---

# Core Business Suite

Core Business Suite \(CBS\) lays the foundation to unify disjointed processes. It’s a collection of modules that fulfills different business needs, for different personas, within a single product suite.

Core Business Suite overview 

Leverage the employee support functionalities in CBS to empower your employees. You can raise the following requests and more as an employee:

-   Raise a payroll or a general benefits request on HR Service Delivery.
-   Raise general inquiries for workplace, legal, safety, finance, and procurement departments in your organization.

Provide suppliers in your organization an easy resolution for the following requests.

-   Raise a general inquiry from the supplier catalog.
-   Raise an invoice request on Accounts Payable Operations.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

Choose one of these tiles to get started.

<table id="table_nxz_wtc_hgc" class="nav-card"><tbody><tr><td>

[Employee support![](../../../reuse/icons/brand-icons/bus-webinar.svg)Learn more about the applications and features available in CBS to enable employee support system in your organization.](exploring-emp-home.md)

</td><td>

[Supplier support![](../../../reuse/icons/brand-icons/bus-webinar.svg)Learn more about the applications and features available in CBS to enable supplier support system in your organization.](exploring-supplr-home.md)

</td></tr></tbody>
</table>
```


### File: core-business-suite\cbs-notif.md

```text
---
title: Notifications in CBS
description: Notifications in CBS provide multi-faceted and timely communication when a request is raised or fulfilled.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Core Business Suite]
---

# Notifications in CBS

Notifications in CBS provide multi-faceted and timely communication when a request is raised or fulfilled.

## Portal notifications

As an employee or a supplier when you raise a request on the CBS application, a portal notification is triggered acknowledge the submission. You receive a notification when your request is commented on, a task is assigned to you, or the request is closed.

You can open the request on the portal and add your comments, add any supporting attachments, or respond to any query from the agent assigned to your support ticket. You can also view the details of your case as an employee or a supplier who has raised the request. For more information, see [Notification configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/service-creator/c_ConfiguringNotifications.md).

**Important:**

-   You must be on the Zurich release to have Notifications available by default in CBS.
-   You must be, at the earliest, on the Yokohama release to install and use Notifications for Employee Center plugin \(sn\_ex\_sp\_notifs\) in CBS.

## Workspace notifications

Workspace notifications are simultaneously triggered for the agent who is working on your request for the employee support ticket or the supplier support ticket. The agent can add a comment for the requester, employee or supplier, add work notes. The agents can also create a task and mark the request complete when is it fulfilled.

The agent gets notifications when the requester has added a comment or an attachment to a request assigned to them.

For more information on workspace notifications, see .

## Email notifications

The requester and the agent both receive email notifications when a request is raised, there's any new development on the request from either personas, or the request is closed.

You can view the request details along with a **View request** or **View case** button that opens either in the portal or the workspace depending on the persona.

For more information on email notifications, see [Email Notifications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/security-management/threat-intelligence-security-center/tisc-email-notifications.md).

**Parent Topic:**[Using Core Business Suite](cbs-using-parent.md)


```


### File: core-business-suite\cbs-reference-parent.md

```text
---
title: Core Business Suite reference
description: The reference topics provide details of the properties, forms, lists, roles, tables, and widgets you want to configure to use the CBS application.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [reference]
breadcrumb: [Core Business Suite]
---

# Core Business Suite reference

The reference topics provide details of the properties, forms, lists, roles, tables, and widgets you want to configure to use the CBS application.

-   **[Components installed with Core Business Suite](comp-inst-with-cbs.md)**  
Various components are installed with Core Business Suite.
-   **[Help topics instance options](helpt-instance-form.md)**  
The details provide the field and its descriptions of the widget instance options.

**Parent Topic:**[Core Business Suite](../concept/cbs-landing.md)


```


### File: core-business-suite\cbs-task-landing-emp.md

```text
---
title: Employee support areas
description: The employee support services in the Core Business Suite help you set up a simplified employee journey in your organization.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Exploring employee support, Core Business Suite]
---

# Employee support areas

The employee support services in the Core Business Suite help you set up a simplified employee journey in your organization.

## Get started

Choose one of the following tiles to learn more about the different applications and application suites supported in Core Business Suite \(CBS\).

**Note:** Only case and knowledge management functionalities are supported on CBS from each of the application suites.

<table id="table_ktr_z4w_hgc" class="nav-card"><tbody><tr><td>

[HR Service Delivery![](../../../reuse/icons/brand-icons/bus-explore.svg)Learn more about HR Service Delivery to ensure delivery of timely employee assistance.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/hr-service-delivery.md)

</td><td>

[Workplace Service Delivery![](../../../reuse/icons/brand-icons/bus-try-a-demo.svg)Learn more about Workplace Service Delivery to manage workplace-related tasks and requests in one place.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-service-delivery/workplace-service-delivery-suite-landing-page.md)

</td><td>

[Legal Service Delivery![](../../../reuse/icons/brand-icons/bus-learn.svg)Learn more about Legal Service Delivery that enables employees and legal support to manage legal requests.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-service-delivery/legal-management-overview.md)

</td></tr><tr><td>

[Health and Safety![](../../../reuse/icons/brand-icons/bus-handshake.svg)Learn more about creating safe and healthy working conditions for your employees.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/health-and-safety/health-safety-overview.md)

</td><td>

[Finance and Supply Chain applications![](../../../reuse/icons/brand-icons/bus-investor-relations-2.svg)Learn more about the finance and supply chain applications that enables employees and finance teams to manage finance-related requests.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/fsc-common-apps-landing.md)

</td><td>

[Sourcing and Procurement Operations![](../../../reuse/icons/brand-icons/bus-person.svg)Learn more about the sourcing and procurement operations to enable your employees to shop for goods and services at work with AI-assisted tools.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/psm-overview.md)

</td></tr></tbody>
</table>Find a breakdown of the supported features in CBS within the mentioned applications.

## HR requests

![General HR request form displayed in image.](../image/gen-hr-form-dec.png)

Raise a request for any query or issue as a general HR request on CBS. For more information, [Raise HR requests](../task/request-emp-cbs.md).

![Form to submit payslip discrepancy displayed in image.](../image/payroll-hr-form-dec.png)

Report an issue with your payslip as an employee. For more information, [Raise HR requests](../task/request-emp-cbs.md).

![Employee benefit inquiry form displayed in image.](../image/hr-benefits-form-dec.png)

Ask an HR benefit questions as an employee. For more information, see [Raise HR requests](../task/request-emp-cbs.md).

## Workplace requests

![General inquiry form displayed for Workplace Service Delivery.](../image/wsd-form-dec.png)

Submit a general workplace service request for issues that need human intervention.

Raise requests for issues that aren’t covered by current automated workflows.

For more information on the Core Business Suite request form for workplace requests, see [Raise requests on the employee portal](../task/request-emp-rest.md).

For more information on the Workplace Service Delivery inquiry form, if you're an existing user, see [Raise help request for a workplace inquiry](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/submit-gen-workplace-serv-req.md).

## Legal requests

![Image displays general legal requests form in Legal Service Delivery.](../image/legal-form-dec.png)

Submit a request to the legal department in your organization for general legal query.

For more information on the Core Business Suite request form for legal requests, see [Raise requests on the employee portal](../task/request-emp-rest.md).

For more information on the Legal Services request form, if you're an existing user, see [Submit a legal request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-request-management/submit-legal-request.md).

## Health and Safety requests

![Image displayed health and safety general request form.](../image/hns-form-dec.png)

Ask a Health and Safety question to the safety department, and request information such as Health and Safety procedures, training, or return to work policies.

For more information on the Core Business Suite request form for Health and Safety, see [Raise requests on the employee portal](../task/request-emp-rest.md).

For more information on the Health and Safety request form, if you're an existing user, see [Ask a Health and Safety question from Employee Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/health-and-safety-case-management/hs-ask-health-safety-question.md).

## Finance-related requests

![Image displays finance inquiry form.](../image/finance-req-form-dec.png)

Ask a general finance-related question, as an employee, targeted to the finance department in your organization. For more information, see [Submit a finance request from Employee Center catalog](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/finance-case-management/submit-fin-req.md).

## Procurement requests

![Image displays general inquiry form for procurement.](../image/procure-form-dec.png)

Raise an inquiry for any pre-existing purchase, as a buyer, or any other query regarding procurement functions​​.

For more information on the Core Business Suite request form, see [Raise requests on the employee portal](../task/request-emp-rest.md).

For more information on the procurement inquiry form, if you're an existing user, see [Raise a general inquiry for procurement](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/raise-general-inquiry-for-procurement.md).

## Workflows and applications

-   [Employee Service Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-service-management-overview.md)
-   [Finance and Supply Chain](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/finance-supply-chain-landing.md)


```


### File: core-business-suite\cbs-task-landing-sup.md

```text
---
title: Supplier support areas
description: The supplier support services in the Core Business Suite help you set up a simplified supplier journey for your organization.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Exploring supplier support, Core Business Suite]
---

# Supplier support areas

The supplier support services in the Core Business Suite help you set up a simplified supplier journey for your organization.

## Get started

Choose one of the following tiles to learn more about the different applications and application suites supported in Core Business Suite.

**Note:** Only general supplier request and invoice request are supported on CBS from the following product suites.

<table id="table_odc_qmb_kgc" class="nav-card"><tbody><tr><td>

[Supplier Lifecycle Operations![](../../../reuse/icons/brand-icons/bus-meetings.svg)Learn more about Supplier Lifecycle Operations to create collaboration with suppliers, mitigate risks, and monitor compliance and performance.](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/supplier-lifecycle-operations/supp-mgmt-landing-page.md)

</td><td>

Accounts Payable Operations![](../../../reuse/icons/brand-icons/bus-compliance.svg)Learn more about Accounts Payable Operations to manage invoices, invoice exceptions, approvals, and supplier inquiries.

</td></tr></tbody>
</table>Find a breakdown of the supported features in CBS within the mentioned applications.

## Supplier lifecycle requests

![Image displays General inquiry form template in SLO.](../image/slo-form-dec.png)

Ask a general category question, using the supplier catalog. For more information, [Raise a general supplier request](../task/request-slo.md).

## Accounts Payable requests

![Invoice inquiry form displayed for Accounts Payable team.](../image/apo-form-dec.png)

As a supplier, use the Supplier Collaboration Portal to create an inquiry related to an invoice and submit it to the Accounts Payable Operations team to evaluate and resolve the inquiry.

For more information, see [Raise an invoice request](../task/request-apo.md).

## Workflows and applications

[Finance and Supply Chain](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/finance-supply-chain-landing.md)


```


### File: core-business-suite\cbs-using-parent.md

```text
---
title: Using Core Business Suite
description: Core Business Suite application provides a unified request experience across departments for organizations.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [use]
breadcrumb: [Core Business Suite]
---

# Using Core Business Suite

Core Business Suite application provides a unified request experience across departments for organizations.

-   **[Now Assist requester experience](now-assist-configurations-requesters.md)**  
Requesters in CBS can use Now Assist in the conversational interface and in search functionality to raise requests and get AI-enabled responses.
-   **[Raise requests on the employee portal](../task/request-emp-rest.md)**  
Raise a general request across departments, as an employee, on CBS.
-   **[Raise HR requests](../task/request-emp-cbs.md)**  
Raise an HR request for general requests, payroll, or benefits on CBS.
-   **[Raise a general supplier request](../task/request-slo.md)**  
Raise a general request for any common query or issue as a supplier on CBS.
-   **[Raise an invoice request](../task/request-apo.md)**  
Raise an invoice request for any payment-related issues as a supplier on CBS.
-   **[Notifications in CBS](cbs-notif.md)**  
Notifications in CBS provide multi-faceted and timely communication when a request is raised or fulfilled.

**Parent Topic:**[Core Business Suite](cbs-landing.md)


```


### File: core-business-suite\comp-inst-with-cbs.md

```text
---
title: Components installed with Core Business Suite
description: Various components are installed with Core Business Suite.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Core Business Suite]
---

# Components installed with Core Business Suite

Various components are installed with Core Business Suite.

**Note:** The Application Files table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

## Core Business Suite Roles

<table id="table_dtg_nfg_xfc"><thead><tr><th>

Role title \[name\]

</th><th>

Description

</th><th>

Contains roles

</th></tr></thead><tbody><tr><td>

Core Business Suite Administrator

 \(sn\_cbs.admin\)

</td><td>

Provides administrative permissions for the Core Business Suite application and full access to configure its underlying services.

</td><td>

-   ESC Admin &amp; Taxonomy admin
-   Human Resources \(sn\_hr\_core.admin\)
-   Workplace Services Delivery \(sn\_wsd\_core.workplace\_admin\)
-   Legal \(sn\_lg\_ops.legal\_admin\)
-   Procurement \(sn\_spend\_psd.admin\)
-   Supplier Lifecycle Operations \(sn\_slm.admin\)
-   Accounts Payable Operations \(sn\_ap\_cm.admin\)
-   Finance \(sn\_fin\_ops.admin\)
-   Health and Safety \(sn\_ohs\_im.admin\)

</td></tr><tr><td>

Core Business Suite requester

 \(sn\_cbs.requestor\)

</td><td>

Grants permissions to submit requests for services included in the Core Business Suite application.

</td><td>

-   Human Resources \(sn\_hr\_core.hrsm\_employee\)
-   Legal \(sn\_lg\_ops.legal\_user\)
-   Workplace Services Delivery \(sn\_wsd\_core.workplace\_user\)
-   Procurement \(sn\_spend\_psd.requestor\)
-   Finance \(sn\_fin\_ops.requester\)
-   Health and Safety \(sn\_hs\_cm.case\_reporter\)

</td></tr></tbody>
</table>## Components installed with Core Business Suite applications

|Application|Component information|
|-----------|---------------------|
|Legal Service Delivery|[Components installed with Legal Request Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/legal-request-management/installed-with-legal-request-management.md)|
|HR Service Delivery|[Components installed with Case and Knowledge Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/components-installed-with-case-and-knowledge-management.md)|
|Workplace Services Delivery|[Components installed with Workplace Case Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/components-installed-with-workplace-case-mgmt.md)|
|Health and Safety|[Components installed with Health and Safety Risk Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/health-and-safety-risk-management/components-installed-with-hs-risk-mgmt.md)|
|Sourcing and Procurement Operations|[Components installed with Sourcing and Procurement Operations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/sourcing-and-procurement-operations/installed-with-FSC.md)|
|Finance and Supply Chain applications|[Components installed with Finance Case Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/finance-case-management/installed-with-fin-ops.md)|
|Supplier Lifecycle Operations|[Components installed with Supplier Case Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/source-to-pay-operations/supplier-lifecycle-operations/installed-with-supp-mgmt.md)|
|Accounts Payable Operations||

**Parent Topic:**[Core Business Suite reference](cbs-reference-parent.md)


```


### File: core-business-suite\config-cbs-using-guided-setup.md

```text
---
title: Configure Core Business Suite using guided setup
description: Configure Core Business Suite business units using guided setup in the configuration console.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-24"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Configure Core Business Suite using guided setup

Configure Core Business Suite business units using guided setup in the configuration console.

To move your Core Business Suite configurations to a new instance using an update set, see [Manage update set for Now Assist for Setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/ia-update-set.md).

**Note:** Some instance-specific tasks might require manual configuration after moving to the new instance.

-   **[Configure Human Resources](../task/config-human-resources.md)**  
Configure the Human Resources \(HR\) business unit to manage payroll inquiries, benefits questions, and general HR requests.
-   **[Configure Legal](../task/config-legal.md)**  
Configure the Legal business unit to submit and manage legal requests.
-   **[Configure Finance](../task/config-finance.md)**  
Configure the Finance business unit to enable employees to submit and manage finance‑related requests.
-   **[Configure Health and Safety](../task/config-health-safety.md)**  
Configure the Health and Safety business unit to enable employees to submit and manage health and safety‑related requests.
-   **[Configure Workplace Services](../task/config-workplace.md)**  
Configure the Workplace Services business unit to manage workplace service requests and space arrangements.
-   **[Configure Source-to-Pay](../task/config-source-to-pay.md)**  
Configure the Source‑to‑Pay business unit to manage procurement, supplier, and invoice requests from submission to fulfillment.

**Parent Topic:**[Configure Core Business Suite Foundation](configure-cbs.md)


```


### File: core-business-suite\config-finance.md

```text
---
title: Configure Finance
description: Configure the Finance business unit to enable employees to submit and manage finance‑related requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Finance

Configure the Finance business unit to enable employees to submit and manage finance‑related requests.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Finance**.

    Alternatively, select **Continue** on the Finance tile.

    Configure the following settings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize an existing intake form or create intake forms to collect finance requests.

    The following intake form is preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |General finance request|Submit general finance questions or request finance services.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle finance requests and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Finance groups|Description|
        |--------------|-----------|
        |Finance request handlers|Receive, assign, and respond to Finance requests.|
        |Finance administrators|Manage Finance roles, processes, and tools.|
        |Employee Center managers|Manage support topics, quick links, and knowledge articles in the Employee Center.|

        To assign users to a default group:

        1.  Select **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize your Finance team.
        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned finance requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notification, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\config-groups.md

```text
---
title: Configure groups and roles
description: Configure groups and roles for Core Business Suite business units through the Now Assist conversational experience.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-22"
reading_time_minutes: 1
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Configure groups and roles

Configure groups and roles for Core Business Suite business units through the Now Assist conversational experience.

## Before you begin

Ensure that the following are activated:

-   AI search \([Activate AI Search](activate-ai-search.md)\)
-   Now Assist panel \([Activate Now Assist panel](enable-now-assist-panel.md)\)

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  Select **Manage Groups** under the business unit that you want to configure \(for example, Human Resources, Legal, Finance, Health and Safety, Workplace Services, or Source-to-Pay\).

5.  Select **Configure with Now Assist**.

    Now Assist opens the conversational panel, detects the current page context, and invokes the Groups and Roles agent.

    **Note:** Now Assist guides you through follow‑up questions and requests confirmation before completing an action.

6.  Select one of the following options or enter a natural‑language prompt.

    -   Assign user\(s\) to a group
    -   Assign roles\(s\) to a group
    -   Create group
    Example prompts:

    -   `Add [username] to the [group name]`
    -   `Assign [role] to the [group name]`
    -   `Create [group name]`
    Now Assist processes your input and displays the available groups.

7.  Select the required group from the list.

8.  Respond to the follow‑up questions provided by Now Assist.

9.  Provide any additional information requested in the conversation panel.

    Now Assist prepares an action summary based on your responses.

10. Review the action summary.

11. Select **Yes** to confirm and proceed, or **No** to cancel.

12. If prompted, provide additional confirmation.

    Now Assist completes the action and displays a success message.


**Parent Topic:**[Now Assist for Core Business Suite](../concept/now-assist-cbs.md)


```


### File: core-business-suite\config-health-safety.md

```text
---
title: Configure Health and Safety
description: Configure the Health and Safety business unit to enable employees to submit and manage health and safety‑related requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Health and Safety

Configure the Health and Safety business unit to enable employees to submit and manage health and safety‑related requests.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Health and Safety**.

    Alternatively, select **Continue** on the Health and Safety tile.

    Configure the following settings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize an existing intake form or create intake forms to collect Health and Safety requests.

    The following intake form is preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |Health and Safety request|Get help with risk or compliance issues or submit general health and safety questions.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle health and safety requests, manage content, and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Health and Safety groups|Description|
        |------------------------|-----------|
        |Health and Safety request handlers|Receive, assign, and respond to Health and Safety requests.|
        |Health and Safety administrators|Manage Health and Safety roles, processes, and tools.|
        |Health and Safety Employee Center managers|Manage support topics, quick links, and knowledge articles in the Employee Center.|

        To assign users to a default group:

        1.  Select **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize your Health and Safety team.

        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned Health and Safety requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notification, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\config-human-resources.md

```text
---
title: Configure Human Resources
description: Configure the Human Resources \(HR\) business unit to manage payroll inquiries, benefits questions, and general HR requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Human Resources

Configure the Human Resources \(HR\) business unit to manage payroll inquiries, benefits questions, and general HR requests.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Human Resources**.

    Alternatively, select **Continue** on the Human Resources tile.

    Configure the followings settings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Email address
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize existing intake forms or create intake forms to collect HR requests.

    The following intake forms are preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |General HR request|Submit general Human Resources questions.|
    |Payroll request|Get help with payroll-related issues.|
    |Benefits request|Ask questions about employee benefits.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle HR requests, manage knowledge, and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Human Resources group|Description|
        |---------------------|-----------|
        |HR request handlers|Receive, assign, and respond to HR requests.|
        |HR administrators|Manage HR roles, oversee processes, and access HR tools.|
        |HR Employee Center managers|Manage support topics, quick links, and knowledge articles.|

        To assign users to a default group:

        1.  Select the **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize HR team.

        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure Human Resources email address by adding the email address and select **Save**.

    Emails sent to this address automatically create requests and send the request number to the sender.

9.  Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notification, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\config-legal.md

```text
---
title: Configure Legal
description: Configure the Legal business unit to submit and manage legal requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Legal

Configure the Legal business unit to submit and manage legal requests.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Legal**.

    Alternatively, select **Continue** on the Legal tile.

    Configure the following settings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize an existing intake form or create intake forms to collect legal requests.

    The following intake form is preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |Legal request|Submits general legal questions or requests legal services.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle legal requests, manage content, and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Legal groups|Description|
        |------------|-----------|
        |Legal administrators|Manage Legal roles, processes, and workflows.|
        |Legal Employee Center managers|Manage Legal support topics, quick links, and knowledge articles in the Employee Center.|
        |Legal request managers|Receive, assign, and respond to Legal requests.|

        To assign user to a default group:

        1.  Select the **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize your Legal team.

        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned legal requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notification, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\config-source-to-pay.md

```text
---
title: Configure Source-to-Pay
description: Configure the Source‑to‑Pay business unit to manage procurement, supplier, and invoice requests from submission to fulfillment.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Source-to-Pay

Configure the Source‑to‑Pay business unit to manage procurement, supplier, and invoice requests from submission to fulfillment.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Source-to-Pay**.

    Alternatively, select **Continue** on the Source‑to‑Pay tile.

    Configure the following settings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Supplier management
    -   Supplier contacts
    -   Email address
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize existing intake forms or create intake forms to collect Source‑to‑Pay requests.

    The following intake forms are preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |General supplier request|Submit general questions related to suppliers.|
    |Procurement request|Submit procurement‑related questions or requests.|
    |Invoice request|Submit invoice‑related questions to Accounts Payable.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle Source‑to‑Pay requests and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Source-to-Pay groups|Description|
        |--------------------|-----------|
        |Accounts payable admins|Manage Accounts Payable roles, processes, and workflows.|
        |Procurement admins|Manage Procurement roles, processes, and workflows.|
        |Supplier operations admins|Manage supplier operations roles and supplier management activities.|
        |S2P Employee Center managers|Manage Source‑to‑Pay content in the Employee Center.|
        |Invoice Request managers|Receive, assign, and respond to invoice requests.|
        |Procurement request managers|Receive, assign, and respond to procurement requests.|
        |Supplier request managers|Receive, assign, and respond to supplier requests.|

        To assign user to a default group:

        1.  Select **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize your Source‑to‑Pay team.

        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure the Source‑to‑Pay email address.

    1.  Enter the email address.
    2.  Select **Save**.
    3.  Select **Mark as configured**.
    **Note:** Emails sent to this address automatically create requests and send the request number to the sender.

9.  Supplier management.

    Manage suppliers by adding supplier details or by uploading a template.

    -   Add suppliers:

        1.  Select **Add suppliers**.
        2.  On the form, fill in the fields.

<table id="table_n13_tw1_s3c"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Legal name

</td><td>

Legal name of the supplier.

</td></tr><tr><td>

Country of registration

</td><td>

Country where the supplier is registered.

</td></tr><tr><td>

Website

</td><td>

Supplier’s official website.

</td></tr><tr><td>

DUNS number

</td><td>

DUNS identifier for the supplier.

</td></tr><tr><td>

Description

</td><td>

Short description of the supplier.

</td></tr><tr><td>

ERP company code

</td><td>

Unique ERP company code.If no code exists, assign a unique code for each record \(for example, 100, 101, 102\)

</td></tr><tr><td>

ERP source

</td><td>

ERP source for the supplier.If no source is available, select CBS.

</td></tr><tr><td>

Active

</td><td>

Indicates whether the supplier is active.

</td></tr></tbody>
</table>        3.  Select **Save**.
        4.  On the manage your supplier details page, select **Mark as configured**.
        **Note:** To add multiple suppliers, select **+ New supplier** and repeat the steps.

    -   Bulk upload:
        1.  Select **Upload suppliers**.
        2.  Download the supplier template.
        3.  Enter the supplier details in the template.
        4.  Save the file in .xlsx or .xls format.
        5.  Upload the updated file.
        6.  Select **Complete upload**.
        7.  On the manage your supplier details page, select **Mark as configured**.
    **Note:** Verify that all required fields are completed and the file size doesn’t exceed 50 MB.

10. Add or upload contacts associated with each supplier.

    Add contacts:

    1.  Select **Add contacts**.
    2.  On the form, fill in the fields.

        |Field|Description|
        |-----|-----------|
        |First name|First name of the contact.|
        |Last name|Last name of the contact.|
        |Email|Email address of the contact.|
        |Is this primary contact|Designates the primary contact. Default is Yes.|
        |Organization \(Supplier\)|Supplier associated with the contact.|

    3.  Select **Save**.
    4.  On the manage your supplier contacts page, select **Mark as configured**.
    **Note:** You can add up to 10 contacts at a time by selecting **+ New contact**.

    Bulk upload:

    1.  Select **Upload contacts**.
    2.  Download the template.
    3.  Update the contact details.
    4.  Upload the updated template.
    5.  Select **Save**.
    6.  On the manage your supplier contacts page, select **Mark as configured**.
    **Note:** Verify that all fields are complete and accurate before uploading.

11. Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned Source‑to‑Pay requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notifications, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\config-workplace.md

```text
---
title: Configure Workplace Services
description: Configure the Workplace Services business unit to manage workplace service requests and space arrangements.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Configure Core Business Suite using guided setup, Configure, Core Business Suite]
---

# Configure Workplace Services

Configure the Workplace Services business unit to manage workplace service requests and space arrangements.

## Before you begin

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the configuration console.

4.  From the configuration summary navigation menu, select **Workplace Services**.

    Alternatively, select **Continue** on the Workplace Services tile.

    Configure the followings as needed:

    -   Intake forms \(preconfigured by default\)
    -   Manage groups
    -   Role assignment
    -   Email address
    -   Workplace locations
    -   Notifications \(preconfigured by default\)
    **Note:** By default, only the admin can configure the manage groups or role assignment.

5.  Customize an existing intake form or create intake forms to collect workplace requests.

    The following intake form is preconfigured by default:

    |Intake form|Description|
    |-----------|-----------|
    |Workplace Services request|Report outages, maintenance issues, or submit general workplace services questions.|

    -   To customize an existing intake forms, select the **Edit** icon.
    -   To create an intake form, select **Create new**. For more information, see [Catalog Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/catalog-builder.md).

        **Note:** Create intake forms directly in the new instance. Moving intake forms configurations to a new instance using an update set isn’t supported.

    -   After customizing or creating an intake form, select **Mark as configured**.
6.  Manage groups to organize users who handle workplace requests, manage content, and configure access.

    -   Default groups

        The following groups are preconfigured with associated roles:

        |Workplace Services groups|Description|
        |-------------------------|-----------|
        |WSD administrators|Manage Workplace Services roles, processes, and workflows.|
        |WSD Employee Center managers|Manage Workplace Services support topics, quick links, and knowledge articles in the Employee Center.|
        |WSD request managers|Receive, assign, and respond to Workplace Services requests.|

        To assign users to a default group:

        1.  Select **Assign people** icon next to the group name.
        2.  In the assign people to this group field, search for and select users.
        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
    -   Create custom groups to organize your Workplace Services team.

        1.  Select **Create Group**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Group name|Name used to identify the group within the business unit.|
            |Group manager|Person responsible for managing the group.|
            |Group description|Brief description of the group’s purpose.|
            |Assign people to this group|People that you add as group members.|
            |Assign role|Roles assigned to group members.|

        3.  Select **Save**.
        4.  On the mange groups page, select **Mark as configured**.
7.  Assign roles to give groups the required access.

    1.  Select a role.
    2.  Select **Assign groups**.
    3.  Select the group from the list.
    4.  Select **Update**.
    5.  On the role assignment page, select **Mark as configured**.
8.  Configure the Workplace Services email address.

    1.  Enter the email address.
    2.  Select **Save**.
    3.  Select **Mark as configured**.
    **Note:** Emails sent to this address automatically create requests and send the request number to the sender.

9.  Manage your work spaces by adding space details or by uploading a template file.

    -   Add spaces:

        1.  Select **Add spaces**.
        2.  On the form, fill in the fields.

            |Field|Description|
            |-----|-----------|
            |Region|Geographic region of the space.|
            |Site|Site name, such as a city or campus.|
            |Campus|Campus associated with the site.|
            |Building|Building where the space is located.|
            |Floor|Floor number or identifier.|
            |Space name|Name of the space, such as a meeting room.|
            |Space type|Type of space, such as office or conference room.|
            |Time zone|Time zone for accurate scheduling.|

        3.  Select **Save**.
        4.  On the manage your work spaces page, select **Mark as configured**.
        **Note:** To add multiple spaces, select **+ New Space** and repeat the steps.

    -   Bulk upload:

        1.  Select **Upload spaces**.
        2.  Download the space template.
        3.  Enter space details in the template.
        4.  Save the file in .xlsx or .xls format.
        5.  Upload the updated file.
        6.  Select **Complete upload**.
        7.  On the manage your work spaces page, select **Mark as configured**.
        **Note:** Verify that all required fields are completed and the file size doesn’t exceed 50 MB.

    -   Bulk edit:
        1.  From the more options menu \(three dots\), select **Bulk edit spaces**.
        2.  Download the file and update the space details.
        3.  Save the file in .xlsx or .xls format.
        4.  Upload the updated file.
        5.  Select **Complete upload**.
        6.  On the manage your work spaces page, select **Mark as configured**.
    **Note:** Verify that all changes are accurate before uploading.

10. Configure notifications sent through Email, Portal, and Workspace to users about submitted or assigned workplace requests.

    -   To create an email notification, see [Create an email notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/t_CreateANotification.md).
    -   To create Portal or Workspace notification, see [Trigger conditions form](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md).
    -   After configuring notifications, select **Mark as configured**.

**Parent Topic:**[Configure Core Business Suite using guided setup](../concept/config-cbs-using-guided-setup.md)


```


### File: core-business-suite\configure-cbs-using-now-assist.md

```text
---
title: Configure Core Business Suite using Now Assist
description: Configure Core Business Suite using a conversational interface provided by Now Assist.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-24"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Configure Core Business Suite using Now Assist

Configure Core Business Suite using a conversational interface provided by Now Assist.

For information on configuring the product modules in Now Assist, see [Configure in Now Assist for Setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/ia-config-landing.md).

-   **[Now Assist for Core Business Suite](now-assist-cbs.md)**  
Now Assist for Core Business Suite supports administrators during Core Business Suite configuration through a guided conversational experience. It can help drive setup completion by displaying next actions, tracking configuration progress, and assisting with error resolution from a single chat interface.

**Parent Topic:**[Configure Core Business Suite Foundation](configure-cbs.md)


```


### File: core-business-suite\configure-cbs.md

```text
---
title: Configure Core Business Suite Foundation
description: Configure Core Business Suite Foundation to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Source‑to‑Pay, and Workplace Services.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [configure]
breadcrumb: [Core Business Suite]
---

# Configure Core Business Suite Foundation

Configure Core Business Suite Foundation to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Source‑to‑Pay, and Workplace Services.

-   **[Install Implementation agent](../task/inst-implement-agent.md)**  
Install the Implementation Agent to enable an Admin Home dashboard where you can access and set up Core Business Suite.
-   **[Activate AI Search](../task/activate-ai-search.md)**  
Activate AI Search to enable conversational search capabilities in Now Assist for Core Business Suite.
-   **[Activate Now Assist panel](../task/enable-now-assist-panel.md)**  
Enable the Now Assist panel to provide generative AI assistance through a conversational interface in Now Assist for Core Business Suite.
-   **[Install Core Business Suite Foundation](../task/set-up-cbs.md)**  
Install Core Business Suite Foundation to configure employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
-   **[Enable Core Business Suite Foundation business units](../task/activate-cbs-bu-version.md)**  
If you’re using any standard business unit included in Core Business Suite Foundation, update the system properties to enable the Core Business Suite business units for installation.
-   **[Assign the CBS admin role](../task/cbs-admin-role.md)**  
Assign the CBS Admin role to grant users full administrative access to configure Core Business Suite.
-   **[Install Core Business Suite applications](install-cbs-apps.md)**  
Install Core Business Suite applications to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
-   **[Reapply the default configurations](../task/reset-default-configurations.md)**  
If the default configurations aren’t applied for Core Business Suite or its business units, reapply the default configurations by running a script.
-   **[Assign the CBS Requester role](../task/assign-cbs-requestor-role.md)**  
Assign the CBS requester role to enable users to access services and submit requests through Employee Center.
-   **[Configure instance options for Help topics widget](../task/instance-option-helpt.md)**  
Configure the instance options for the Help topics widget on the CBS employee portal according to your organizational requirement.
-   **[Configure Core Business Suite using guided setup](config-cbs-using-guided-setup.md)**  
Configure Core Business Suite business units using guided setup in the configuration console.
-   **[Configure Core Business Suite using Now Assist](configure-cbs-using-now-assist.md)**  
Configure Core Business Suite using a conversational interface provided by Now Assist.

**Parent Topic:**[Core Business Suite](cbs-landing.md)


```


### File: core-business-suite\create-notification-using-na.md

```text
---
title: Create a notification
description: Create notifications for Core Business Suite business units through the Now Assist conversational experience.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-27"
reading_time_minutes: 1
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Create a notification

Create notifications for Core Business Suite business units through the Now Assist conversational experience.

## Before you begin

Ensure that the following are activated:

-   AI search \([Activate AI Search](activate-ai-search.md)\)
-   Now Assist panel \([Activate Now Assist panel](enable-now-assist-panel.md)\)

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  Select **Notifications** under the business unit that you want to configure \(for example, Human Resources, Legal, Finance, Health and Safety, Workplace Services, or Source-to-Pay\).

5.  Select **Configure with Now Assist**.

    Now Assist opens the conversational panel, detects the current page context, and invokes the Notification agent.

    **Note:** Now Assist guides you through follow‑up questions and requests confirmation before creating the notification.

6.  Select **Create a new notification**, or enter a natural‑language prompt.

    Example prompts:

    -   `Notify the fulfiller when a [BU name] case is assigned`
    -   `Notify the employee when a [BU name] case is resolved or closed`
    -   `Set up a notification for managers when their direct reports open a [BU name] request`
7.  Respond to the follow‑up questions provided by Now Assist, such as:

    -   The table the notification applies to
    -   The trigger criteria \(on create, update, or both\)
    -   The recipients \(users, groups, or fields\)
    Now Assist processes your responses and prepares the notification details.

8.  Review the notification details.

9.  Select one of the following options:

    -   **No, looks good** to confirm
    -   **Yes, I’d like to make changes** to update the details
10. If you select **Yes, I’d like to make changes**, enter the changes when prompted.

    Now Assist revises the notification and presents the updated details.

11. Review the updated notification details and confirm.

    Now Assist creates the notification and displays a success message.


**Parent Topic:**[Now Assist for Core Business Suite](../concept/now-assist-cbs.md)


```


### File: core-business-suite\edit-existing-notification-using-na.md

```text
---
title: Edit a notification
description: Edit notifications for Core Business Suite business units through the Now Assist conversational experience.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-27"
reading_time_minutes: 1
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Edit a notification

Edit notifications for Core Business Suite business units through the Now Assist conversational experience.

## Before you begin

Ensure that the following are activated:

-   AI search \([Activate AI Search](activate-ai-search.md)\)
-   Now Assist panel \([Activate Now Assist panel](enable-now-assist-panel.md)\)

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  Select **Notifications** under the business unit that you want to configure \(for example, Human Resources, Legal, Finance, Health and Safety, Workplace Services, or Source-to-Pay\).

5.  Select **Configure with Now Assist**.

    Now Assist opens the conversational panel, detects the current page context, and invokes the Notification agent.

    **Note:** Now Assist guides you through follow‑up questions and requests confirmation before saving changes.

6.  Select **Edit an existing notification**, or enter a natural‑language prompt.

    Example prompts:

    -   `Update the notification for a [BU name] case assignment to fulfiller`.
    -   `Update the notification for a [BU name] case resolution or closure to employee`.
    -   `Update the notification for managers when direct reports open a [BU name] request`.
7.  Enter the name of the email notification when prompted.

    Now Assist retrieves the notification record and displays a link for review.

8.  Review the notification record.

9.  Enter the changes that you want to make.

    Now Assist applies your updates and presents the revised notification details.

10. Review the updated notification details and confirm.

    Now Assist saves the changes and displays a success message.


**Parent Topic:**[Now Assist for Core Business Suite](../concept/now-assist-cbs.md)


```


### File: core-business-suite\enable-now-assist-panel.md

```text
---
title: Activate Now Assist panel
description: Enable the Now Assist panel to provide generative AI assistance through a conversational interface in Now Assist for Core Business Suite.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-05"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Activate Now Assist panel

Enable the Now Assist panel to provide generative AI assistance through a conversational interface in Now Assist for Core Business Suite.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Now Assist Admin** &gt; **Experiences**.

    The Now Assist panel page opens.

2.  In the summary section, select **Turn on**.

3.  Under settings, select **Visit Assistant Designer**.

4.  On the Visit Assistant Designer page, select **Activate**.

    The Now Assist panel is activated. For more information, see [Now Assist panel](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/now-assist-panel-overview.md).


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\exploring-emp-home.md

```text
---
title: Exploring employee support
description: Explore the home page for the employee requester persona along with the associated functionalities available with Core Business Suite.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [explore]
breadcrumb: [Core Business Suite]
---

# Exploring employee support

Explore the home page for the employee requester persona along with the associated functionalities available with Core Business Suite.

## Core Business Suite employee support overview

Core Business Suite application helps you set up an employee journey in your organization across departments. Raise a request with the CBS employee portal related to HR, finance, legal, procurement, and more in one place. For more information, see [Employee support areas](cbs-task-landing-emp.md).

Apart from raising requests, you can track and manage your tasks and activities with different functionalities like, My active items, My favorites, My tasks, Requests, and Org charts. For more information on each of the functionality, see [Employee Center](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/employee-center-landing-page.md).

## Core Business Suite employee users

<table id="table_lcs_nps_3hc"><thead><tr><th>

User

</th><th>

Description

</th></tr></thead><tbody><tr><td>

CBS admin\[sn\_cbs.admin\]

</td><td>

Manages the administrative permissions for the CBS application and has complete access to all configurations in CBS.

</td></tr><tr><td>

CBS requestersn\_cbs.requestor

</td><td>

Has permission to submit requests for different services in CBS.

</td></tr></tbody>
</table>## Core Business Suite benefits

<table id="table_ocs_nps_3hc"><thead><tr><th>

Benefit

</th><th>

Feature

</th><th>

Users

</th></tr></thead><tbody><tr><td>

Access Help Center to raise a request on the Employee portal in CBS.

</td><td>

Help Center

</td><td>

CBS requester\[sn\_cbs.requestor\]

</td></tr><tr><td>

Leverage an intuitive portal navigation with the Advanced Portal Navigation \(APN\) in CBS. Access all your employee portal request forms under APN.**Note:** Merge your existing APN record with the CBS APN record or use the active and default APN setup provided in CBS. For more information on merging your existing APN record to use it in CBS, see .

</td><td>

[Advanced Portal Navigation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/adv-portal-navigation-overview.md)

</td><td>

CBS requester\[sn\_cbs.requestor\]

</td></tr><tr><td>

Provide targeted content and communication for employees in CBS.

</td><td>

[Create campaign stages with Content Experience Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ecpro-campaign-builder.md)

</td><td>

CBS admin\[sn\_cbs.admin\]

</td></tr><tr><td>

Access the employee request forms from different departments under the Help topics widget.For more information on the Help topics widget display settings, see [Configure instance options for Help topics widget](../task/instance-option-helpt.md).

</td><td>

Help topics

</td><td>

CBS requester\[sn\_cbs.requestor\]

</td></tr><tr><td>

-   Create quick links, associate quick links to topics, and restrict access to quick links as an admin.
-   Access internal and external resources related to specific departments within your organization as an employee.

 **Note:** You can access any existing Quick links from your Employee Center portal, if you're already a user, on the CBS employee portal.

</td><td>

[Quick links](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/emp-center-quick-link-config.md)

</td><td>

-   CBS admin

\[sn\_cbs.admin\]

-   CBS requester

\[sn\_cbs.requestor\]


</td></tr></tbody>
</table>## What to explore next

To learn more about configuring and using Core Business Suite, see:

-   
-   [Using Core Business Suite](cbs-using-parent.md)
-   [Core Business Suite reference](../reference/cbs-reference-parent.md)


```


### File: core-business-suite\exploring-supplr-home.md

```text
---
title: Exploring supplier support
description: Explore the home page for the supplier requester persona along with the associated functionalities available with Core Business Suite.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [explore]
breadcrumb: [Core Business Suite]
---

# Exploring supplier support

Explore the home page for the supplier requester persona along with the associated functionalities available with Core Business Suite.

## Core Business Suite supplier support overview

Leverage the Supplier Collaboration Portal for the suppliers in your organization to raise a general request or an invoice request on the Core Business Suite application.

You can select the **Raise a request** button on the portal and access the request forms.

## Core Business Suite supplier users

<table id="table_mlz_d2t_3hc"><thead><tr><th>

User

</th><th>

Description

</th></tr></thead><tbody><tr><td>

CBS admin\[sn\_cbs.admin\]

</td><td>

Manages the administrative permissions for the CBS application and has complete access to all configurations in CBS.

</td></tr><tr><td>

Supplier requester\[sn\_slm.contact\]

</td><td>

Manually assigned to users by the admin who has access to the Supplier Collaboration Portal to raise requests on the supplier portal on CBS.

</td></tr></tbody>
</table>## What to explore next

To learn more about configuring and using Core Business Suite, see:

-   
-   [Using Core Business Suite](cbs-using-parent.md)
-   [Core Business Suite reference](../reference/cbs-reference-parent.md)


```


### File: core-business-suite\finance-default-configurations.md

```text
---
title: Finance default configurations
description: Details of the default configurations for Finance.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Finance, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Finance default configurations

Details of the default configurations for Finance.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Finance case workflows and communication.|
|Intake forms|Activates required intake forms for submitting Finance requests and capturing case details.|

**Parent Topic:**[Install Finance](../task/install-finance.md)


```


### File: core-business-suite\health-and-safety-default-configurations.md

```text
---
title: Health and Safety default configurations
description: Details of the default configurations for Health and Safety.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Health and Safety, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Health and Safety default configurations

Details of the default configurations for Health and Safety.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Health and Safety workflows and communication.|
|Intake forms|Activates required intake forms for submitting Health and Safety requests and capturing case details.|

**Parent Topic:**[Install Health and Safety](../task/install-health-and-safety.md)


```


### File: core-business-suite\helpt-instance-form.md

```text
---
title: Help topics instance options
description: The details provide the field and its descriptions of the widget instance options.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Reference, Core Business Suite]
---

# Help topics instance options

The details provide the field and its descriptions of the widget instance options.

<table id="table_jb5_g4f_khc"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Widget Title

</td><td>

Title or name of the widget.

</td></tr><tr><td>

Heading Level

</td><td>

Heading level on the user interface for the widget.

</td></tr><tr><td>

Topic Card Display Style

</td><td>

The following are the available options:-   **None**: Default number of content is selected on the card to display. For more than 2 content or request forms it selects **Compact** and for more it automatically selects **Detailed**.
-   **Compact**: Card details displayed with a brief detail without any card content visible.
-   **Detailed**: Card content or the request forms are visible as selected in the **Topic Card Content Limit**.

</td></tr><tr><td>

Card Limit

</td><td>

Number of cards to display on the widget.

</td></tr><tr><td>

Topic Card Content Limit

</td><td>

Number of card content to display on a card.The options are **None**, **2**, and **3**. The default value is 3.

</td></tr><tr><td>

Load Configuration

</td><td>

The following options are available:-   **Asynchronous**
-   **Synchronous**

</td></tr></tbody>
</table>**Parent Topic:**[Core Business Suite reference](cbs-reference-parent.md)


```


### File: core-business-suite\hr-default-configurations.md

```text
---
title: Human Resources default configurations
description: Details of the default configurations for Human Resources.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Human Resources, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Human Resources default configurations

Details of the default configurations for Human Resources.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Human Resources workflows and employee communication.|
|Intake forms|Activates required intake forms for submitting Human Resources requests and capturing request details.|
|Human Resources services|Configures required Human Resources services that define service offerings and support request routing and fulfillment.|

**Parent Topic:**[Install Human Resources](../task/install-human-resources.md)


```


### File: core-business-suite\index.md

```text
---
title: Australia Core Business Suite
locale: en-US
release: australia
bundle: cbs
doc_type: toc
---

# Australia Core Business Suite

- [Core Business Suite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-landing.md) -- Core Business Suite (CBS) lays the foundation to unify disjointed processes. It’s a collection of modules that fulfills different business needs, for different personas, within a single product suite.
  - [Exploring employee support](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/exploring-emp-home.md) -- Explore the home page for the employee requester persona along with the associated functionalities available with Core Business Suite.
    - [Employee support areas](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-task-landing-emp.md) -- The employee support services in the Core Business Suite help you set up a simplified employee journey in your organization.
  - [Exploring supplier support](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/exploring-supplr-home.md) -- Explore the home page for the supplier requester persona along with the associated functionalities available with Core Business Suite.
    - [Supplier support areas](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-task-landing-sup.md) -- The supplier support services in the Core Business Suite help you set up a simplified supplier journey for your organization.
  - [Configure](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/configure-cbs.md) -- Configure Core Business Suite Foundation to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Source‑to‑Pay, and Workplace Services.
    - [Install Implementation agent](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/inst-implement-agent.md) -- Install the Implementation Agent to enable an Admin Home dashboard where you can access and set up Core Business Suite.
    - [Activate AI Search](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/activate-ai-search.md) -- Activate AI Search to enable conversational search capabilities in Now Assist for Core Business Suite.
    - [Activate Now Assist panel](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/enable-now-assist-panel.md) -- Enable the Now Assist panel to provide generative AI assistance through a conversational interface in Now Assist for Core Business Suite.
    - [Install Core Business Suite Foundation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/set-up-cbs.md) -- Install Core Business Suite Foundation to configure employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
      - [Core Business Suite Foundation default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-default-configs.md) -- Details of the default configurations for Core Business Suite Foundation.
    - [Enable Core Business Suite Foundation business units](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/activate-cbs-bu-version.md) -- If you’re using any standard business unit included in Core Business Suite Foundation, update the system properties to enable the Core Business Suite business units for installation.
    - [Assign the CBS admin role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-admin-role.md) -- Assign the CBS Admin role to grant users full administrative access to configure Core Business Suite.
    - [Install Core Business Suite applications](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-cbs-apps.md) -- Install Core Business Suite applications to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
      - [Install Human Resources](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-human-resources.md) -- Install Human Resources to configure its settings and requests.
        - [Human Resources default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/hr-default-configurations.md) -- Details of the default configurations for Human Resources.
      - [Install Legal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-legal.md) -- Install Legal to configure its settings and requests.
        - [Legal default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/legal-default-configurations.md) -- Details of the default configurations for Legal.
      - [Install Finance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-finance.md) -- Install Finance to configure its settings and requests.
        - [Finance default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/finance-default-configurations.md) -- Details of the default configurations for Finance.
      - [Install Health and Safety](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-health-and-safety.md) -- Install Health and Safety to configure its settings and requests.
        - [Health and Safety default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/health-and-safety-default-configurations.md) -- Details of the default configurations for Health and Safety.
      - [Install Workplace Services](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-workplace-services.md) -- Install Workplace Services to configure its settings and requests.
        - [Workplace Services default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/workplace-default-configurations.md) -- Details of the default configurations for Workplace Services.
      - [Install Source-to-Pay](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/install-source-to-pay.md) -- Install Source-to-Pay to configure its settings and requests.
        - [Source-to-Pay default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/source-to-pay-default-configurations.md) -- Details of the default configurations for Source-to-Pay.
    - [Reapply the default configurations](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/reset-default-configurations.md) -- If the default configurations aren’t applied for Core Business Suite or its business units, reapply the default configurations by running a script.
    - [Assign the CBS Requester role](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/assign-cbs-requestor-role.md) -- Assign the CBS requester role to enable users to access services and submit requests through Employee Center.
    - [Configure instance options for Help topics widget](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/instance-option-helpt.md) -- Configure the instance options for the Help topics widget on the CBS employee portal according to your organizational requirement.
    - [Configure Core Business Suite using guided setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-cbs-using-guided-setup.md) -- Configure Core Business Suite business units using guided setup in the configuration console.
      - [Configure Human Resources](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-human-resources.md) -- Configure the Human Resources (HR) business unit to manage payroll inquiries, benefits questions, and general HR requests.
      - [Configure Legal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-legal.md) -- Configure the Legal business unit to submit and manage legal requests.
      - [Configure Finance](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-finance.md) -- Configure the Finance business unit to enable employees to submit and manage finance‑related requests.
      - [Configure Health and Safety](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-health-safety.md) -- Configure the Health and Safety business unit to enable employees to submit and manage health and safety‑related requests.
      - [Configure Workplace Services](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-workplace.md) -- Configure the Workplace Services business unit to manage workplace service requests and space arrangements.
      - [Configure Source-to-Pay](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-source-to-pay.md) -- Configure the Source‑to‑Pay business unit to manage procurement, supplier, and invoice requests from submission to fulfillment.
    - [Configure Core Business Suite using Now Assist](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/configure-cbs-using-now-assist.md) -- Configure Core Business Suite using a conversational interface provided by Now Assist.
      - [Now Assist for Core Business Suite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/now-assist-cbs.md) -- Now Assist for Core Business Suite supports administrators during Core Business Suite configuration through a guided conversational experience. It can help drive setup completion by displaying next actions, tracking configuration progress, and assisting with error resolution from a single chat interface.
        - [Agentic Workflow in Now Assist for Core Business Suite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/using-ai-agent-workflows-na-cbs.md) -- Agentic workflow in Now Assist for Core Business Suite supports the Core Business Suite setup process through a conversational interface.
        - [Configure groups and roles](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/config-groups.md) -- Configure groups and roles for Core Business Suite business units through the Now Assist conversational experience.
        - [Create a notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/create-notification-using-na.md) -- Create notifications for Core Business Suite business units through the Now Assist conversational experience.
        - [Edit a notification](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/edit-existing-notification-using-na.md) -- Edit notifications for Core Business Suite business units through the Now Assist conversational experience.
        - [Bulk upload](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/manage-bulk-upload-using-na.md) -- Upload records in bulk for Core Business Suite business units through the Now Assist conversational experience.
        - [Bulk edit](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/manage-bulk-edit-using-na.md) -- Edit records in bulk for Core Business Suite business units through the Now Assist conversational experience.
  - [Use](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-using-parent.md) -- Core Business Suite application provides a unified request experience across departments for organizations.
    - [Now Assist requester experience](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/now-assist-configurations-requesters.md) -- Requesters in CBS can use Now Assist in the conversational interface and in search functionality to raise requests and get AI-enabled responses.
    - [Raise requests on the employee portal](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/request-emp-rest.md) -- Raise a general request across departments, as an employee, on CBS.
    - [Raise HR requests](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/request-emp-cbs.md) -- Raise an HR request for general requests, payroll, or benefits on CBS.
    - [Raise a general supplier request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/request-slo.md) -- Raise a general request for any common query or issue as a supplier on CBS.
    - [Raise an invoice request](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/request-apo.md) -- Raise an invoice request for any payment-related issues as a supplier on CBS.
    - [Notifications in CBS](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-notif.md) -- Notifications in CBS provide multi-faceted and timely communication when a request is raised or fulfilled.
  - [Reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/cbs-reference-parent.md) -- The reference topics provide details of the properties, forms, lists, roles, tables, and widgets you want to configure to use the CBS application.
    - [Components installed with Core Business Suite](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/comp-inst-with-cbs.md) -- Various components are installed with Core Business Suite.
    - [Help topics instance options](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/core-business-suite/helpt-instance-form.md) -- The details provide the field and its descriptions of the widget instance options.

```


### File: core-business-suite\inst-implement-agent.md

```text
---
title: Install Implementation agent
description: Install the Implementation Agent to enable an Admin Home dashboard where you can access and set up Core Business Suite.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Install Implementation agent

Install the Implementation Agent to enable an Admin Home dashboard where you can access and set up Core Business Suite.

## Before you begin

For information on using a centralized Admin Home dashboard to set up and manage applications, see [Now Assist for Setup](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/ia-landing.md).

**Note:** Core Business Suite guided setup is supported only on Australia patch 1 and later. Verify that your instance meets this requirement before installing the Implementation Agent.

To purchase a subscription, contact your ServiceNow account manager. When you purchase a subscription, certain plugins are activated automatically. If a paid plugin isn't activated automatically, you can manually activate it from the All Applications list in your instance.

**Note:**

Before purchasing a subscription, you can evaluate the feature on a non-production instance without charge by requesting it from the Now Support Service Catalog.

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the Implementation agent \(sn\_ia\) application using the filter criteria and search bar.

    You can search for the application by its name or ID. If you can’t find the application, you might have to request it from the ServiceNow Store.

    The available versions are displayed.

3.  Review the available versions displayed.

4.  Select a version from the list and select **Install**.

    In the Review Installation Details dialog box, any dependencies installed with your application are listed.

5.  If you're prompted, follow the links to the ServiceNow Store to get any additional entitlements for dependencies.

6.  Select **Install** to start the installation process.

    **Note:** When domain separation and delegated admin are enabled in an instance, the administrative user must be in the **global** domain. Otherwise, the following error appears: `Application installation is unavailable because another operation is running: Plugin Activation for <plugin name>.`

    You will see a message after installation is completed. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).


## What to do next

Set up the Core Business Suite. For more information, see [Install Core Business Suite Foundation](set-up-cbs.md).

**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\install-cbs-apps.md

```text
---
title: Install Core Business Suite applications
description: Install Core Business Suite applications to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Install Core Business Suite applications

Install Core Business Suite applications to support employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.

-   **[Install Human Resources](../task/install-human-resources.md)**  
Install Human Resources to configure its settings and requests.
-   **[Install Legal](../task/install-legal.md)**  
Install Legal to configure its settings and requests.
-   **[Install Finance](../task/install-finance.md)**  
Install Finance to configure its settings and requests.
-   **[Install Health and Safety](../task/install-health-and-safety.md)**  
Install Health and Safety to configure its settings and requests.
-   **[Install Workplace Services](../task/install-workplace-services.md)**  
Install Workplace Services to configure its settings and requests.
-   **[Install Source-to-Pay](../task/install-source-to-pay.md)**  
Install Source-to-Pay to configure its settings and requests.

**Parent Topic:**[Configure Core Business Suite Foundation](configure-cbs.md)


```


### File: core-business-suite\install-finance.md

```text
---
title: Install Finance
description: Install Finance to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Finance

Install Finance to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Finance** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Finance. For information about default configurations, see [Finance default configurations](../concept/finance-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Finance business unit appears in the ready to configure section.

-   **[Finance default configurations](../concept/finance-default-configurations.md)**  
Details of the default configurations for Finance.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\install-health-and-safety.md

```text
---
title: Install Health and Safety
description: Install Health and Safety to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Health and Safety

Install Health and Safety to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Health and Safety** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Health and Safety. For information about default configurations, see [Health and Safety default configurations](../concept/health-and-safety-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Health and Safety business unit appears in the ready to configure section.

-   **[Health and Safety default configurations](../concept/health-and-safety-default-configurations.md)**  
Details of the default configurations for Health and Safety.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\install-human-resources.md

```text
---
title: Install Human Resources
description: Install Human Resources to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Human Resources

Install Human Resources to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Human Resources** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Human Resources. For information about default configurations, see [Human Resources default configurations](../concept/hr-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Human Resources business unit appears in the ready to configure section.

-   **[Human Resources default configurations](../concept/hr-default-configurations.md)**  
Details of the default configurations for Human Resources.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\install-legal.md

```text
---
title: Install Legal
description: Install Legal to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Legal

Install Legal to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Legal** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Legal. For information about default configurations, see [Legal default configurations](../concept/legal-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Legal business unit appears in the ready to configure section.

-   **[Legal default configurations](../concept/legal-default-configurations.md)**  
Details of the default configurations for Legal.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\install-source-to-pay.md

```text
---
title: Install Source-to-Pay
description: Install Source-to-Pay to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Source-to-Pay

Install Source-to-Pay to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Source-to-Pay** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Source-to-Pay. For information about default configurations, see [Source-to-Pay default configurations](../concept/source-to-pay-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Source-to-Pay business unit appears in the ready to configure section.

-   **[Source-to-Pay default configurations](../concept/source-to-pay-default-configurations.md)**  
Details of the default configurations for Source-to-Pay.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\install-workplace-services.md

```text
---
title: Install Workplace Services
description: Install Workplace Services to configure its settings and requests.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-02"
reading_time_minutes: 1
breadcrumb: [Install Core Business Suite applications, Configure, Core Business Suite]
---

# Install Workplace Services

Install Workplace Services to configure its settings and requests.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  On the Core Business Suite Foundation page, select **Workplace Services** in the Install section.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for the Workplace Services. For information about default configurations, see [Workplace Services default configurations](../concept/workplace-default-configurations.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## Result

The installed Workplace Services business unit appears in the ready to configure section.

-   **[Workplace Services default configurations](../concept/workplace-default-configurations.md)**  
Details of the default configurations for Workplace Services.

**Parent Topic:**[Install Core Business Suite applications](../concept/install-cbs-apps.md)


```


### File: core-business-suite\instance-option-helpt.md

```text
---
title: Configure instance options for Help topics widget
description: Configure the instance options for the Help topics widget on the CBS employee portal according to your organizational requirement.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Configure instance options for Help topics widget

Configure the instance options for the Help topics widget on the CBS employee portal according to your organizational requirement.

## Before you begin

Role required: sn\_cbs.admin

## Procedure

1.  Navigate to **Employee Center** &gt; **Help topics**.

2.  Press **Control** and select and hold \(or right-click\) on the Help topics widget to view the Instance options and select it.

3.  In the Instance form, fill in the fields, and select **Save**.

    For a description of the field values, see [Help topics instance options](../reference/helpt-instance-form.md).


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\legal-default-configurations.md

```text
---
title: Legal default configurations
description: Details of the default configurations for Legal.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Legal, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Legal default configurations

Details of the default configurations for Legal.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Legal workflows and communication.|
|Intake forms|Activates required intake forms for submitting Legal requests and capturing request details.|

**Parent Topic:**[Install Legal](../task/install-legal.md)


```


### File: core-business-suite\manage-bulk-edit-using-na.md

```text
---
title: Bulk edit
description: Edit records in bulk for Core Business Suite business units through the Now Assist conversational experience.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-26"
reading_time_minutes: 1
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Bulk edit

Edit records in bulk for Core Business Suite business units through the Now Assist conversational experience.

## Before you begin

Ensure that the following are activated:

-   AI search \([Activate AI Search](activate-ai-search.md)\)
-   Now Assist panel \([Activate Now Assist panel](enable-now-assist-panel.md)\)

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  Select **Workplace locations** under Workplace Services.

5.  Select **Configure with Now Assist**.

    Now Assist opens the conversational panel, detects the current page context, and invokes the CBS Bulk Upload agent.

    **Note:** The CBS Bulk Upload Agent supports Workplace Locations for bulk edit.

6.  Select **Bulk edit** or enter a natural‑language prompt.

    Example prompts:

    -   `Bulk edit workplace locations`.
    -   `Edit workplace locations using a template`.
    -   `Bulk edit records for workplace locations`.
    Now Assist processes your request, identifies the relevant template based on the selection, and provides it for download.

7.  Download the template.

    The template downloads as a .csv file.

8.  Open the file in Excel \(.xlsx or .xls\), make the required changes, and save the file.

9.  Upload the updated template when prompted.

    Now Assist analyzes the uploaded file and validates the data.

10. Review the validation results.

11. If errors are reported, review and update the template file as needed, and re‑upload it.

12. If validation is successful, select **Process all rows**.

    Now Assist processes the updates and provides access to the import set.

13. Select **Import Set** to review the updated records.

14. Confirm that the changes are reflected.

15. Select **Mark as configured** when prompted.

    Now Assist confirms that the bulk edit is complete with a success message.

16. Refresh the Core Business Suite Configuration Console to verify that the records are updated successfully.


**Parent Topic:**[Now Assist for Core Business Suite](../concept/now-assist-cbs.md)


```


### File: core-business-suite\manage-bulk-upload-using-na.md

```text
---
title: Bulk upload
description: Upload records in bulk for Core Business Suite business units through the Now Assist conversational experience.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-26"
reading_time_minutes: 2
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Bulk upload

Upload records in bulk for Core Business Suite business units through the Now Assist conversational experience.

## Before you begin

Ensure that the following are activated:

-   AI search \([Activate AI Search](activate-ai-search.md)\)
-   Now Assist panel \([Activate Now Assist panel](enable-now-assist-panel.md)\)

Role required: admin, sn\_cbs.admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **View product overview**.

3.  In the Configuration insights section, select **Configure**.

    The Configure Core Business Suite page opens in the Configuration Console.

4.  From the navigation menu, select the section to which you want to bulk upload the details:

    -   **Workplace locations** under Workplace Services
    -   **Supplier management** or **Supplier contacts** under Source-to-Pay
5.  Select **Configure with Now Assist**.

    Now Assist opens the conversational panel, detects the current page context, and invokes the CBS Bulk Upload agent.

    **Note:** Now Assist guides you through follow‑up questions and requests confirmation before completing the bulk upload.

6.  Select **Bulk upload** or enter a natural‑language prompt:

    Example prompts:

    -   `Bulk upload workplace locations`.
    -   `Upload multiple workplace locations using a template`.
    -   `Bulk upload records for workplace locations`.
    Now Assist processes your request, identifies the relevant template based on the selection, and provides it for download.

7.  Download the bulk upload template.

8.  Enter the required data in the template and save the file.

9.  Upload the updated template when prompted.

    Now Assist analyzes the uploaded file and validates the data.

10. Review the validation results.

11. If errors are reported, review and update the template file as needed, and re-upload it.

12. If validation is successful, select **Process all rows**.

    Now Assist processes the import and provides access to the import set.

13. Select **Import Set** to review the imported records.

14. Confirm that the updates are reflected.

15. Select **Mark as configured** when prompted.

    Now Assist confirms that the bulk upload is complete with a success message.

16. Refresh the Core Business Suite Configuration Console to verify that the records are created successfully.


**Parent Topic:**[Now Assist for Core Business Suite](../concept/now-assist-cbs.md)


```


### File: core-business-suite\now-assist-cbs.md

```text
---
title: Now Assist for Core Business Suite
description: Now Assist for Core Business Suite supports administrators during Core Business Suite configuration through a guided conversational experience. It can help drive setup completion by displaying next actions, tracking configuration progress, and assisting with error resolution from a single chat interface.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-22"
reading_time_minutes: 4
breadcrumb: [Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Now Assist for Core Business Suite

Now Assist for Core Business Suite supports administrators during Core Business Suite configuration through a guided conversational experience. It can help drive setup completion by displaying next actions, tracking configuration progress, and assisting with error resolution from a single chat interface.

## Now Assist for Core Business Suite overview

Now Assist for Core Business Suite overview describes how the conversational setup experience is implemented using Now Assist panel, AI agents, skills, and tools. Now Assist maintains context across setup steps and reflects the current system state to help guide configuration activities through a structured conversational flow.

## Now Assist for Core Business Suite conversational flow

Now Assist for Core Business Suite conversational flow guides administrators through Core Business Suite setup using an interactive, chat‑based experience. The conversational flow provides context-based recommendations, displays default configurations, and dynamically triggers setup tasks such as intake form creation, role assignment, and notification configuration. This guided approach can help reduce setup effort and might enable faster completion of Core Business Suite business unit configurations.

The flow adapts based on completed steps and current configuration status, helping administrators move through the setup in a logical sequence.

## AI Skills

The following AI skills are available in Now Assist for Core Business Suite:

-   Next Best Action: Identifies the next setup task based on the current configuration state. Recommendations update as the setup progresses and additional configuration steps are available.
-   Error Resolution: Provides contextual guidance when a configuration step doesn’t complete successfully. The skill displays possible actions that might help address common setup issues and continue the setup process.

## AI capabilities

The following generative AI capabilities are available in Now Assist for Core Business Suite:

-   Conversational Setup Guidance: Guides administrators through Core Business Suite business unit setup steps using the Now Assist panel conversational interface.
-   Contextual Awareness: Maintains awareness of completed setup steps and installed business units, enabling administrators to continue configuration from the current setup state.
-   Dynamic Recommendations: Displays the next configuration step based on the current setup state.
-   Multi–Business Unit Support: Supports configuring multiple business units from a single guided setup flow in the Configuration Console.

## AI limitations

This application uses artificial intelligence \(AI\) and machine learning, which are rapidly evolving fields of study that generate predictions based on patterns in data. As a result, this application may not always produce accurate, complete, or appropriate information. Furthermore, there is no guarantee that this application has been fully trained or tested for your use case. To mitigate these issues, it is your responsibility to test and evaluate your use of this application for accuracy, harm, and appropriateness for your use case, employ human oversight of output, and refrain from relying solely on AI-generated outputs for decision-making purposes. This is especially important if you choose to deploy this application in areas with consequential impacts such as healthcare, finance, legal, employment, security, or infrastructure. You agree to abide by [ServiceNow’s AI Acceptable Use Policy](https://www.servicenow.com/ai-acceptable-use-policy.html), which may be updated by ServiceNow.

## Data processing

This application requires data to be transferred from ServiceNow customers' individual instances to a centralized ServiceNow environment, which may be located in a different data center region from the one where your instance is, and potentially to a third-party cloud provider, such as Microsoft Azure. This data is handled per ServiceNow's internal policies and procedures, including our policies available through our [CORE Compliance Portal](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564067).

## Data collection

ServiceNow collects and uses the inputs, outputs, and edits to outputs of this application to develop and improve ServiceNow technologies including ServiceNow models and AI products. In addition, this application will collect data about workplace requests \(e.g. reservations\). Customers can opt out of future data collection at any time, as described in the [Now Assist Opt-Out page](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/opt-out-of-data-sharing-for-now-assist.md).

For more information, see the [Now Assist documentation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/platform-now-assist-landing.md).

## Troubleshoot and get help

-   [ServiceNow Community on AI and Intelligence](https://www.servicenow.com/community/ai-intelligence-articles/tkb-p/ai-platform-kb)
-   [Search the Known Error Portal for known error articles](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597477)
-   [Contact Customer Service and Support.](https://support.servicenow.com/now?draw=case)

-   **[Agentic Workflow in Now Assist for Core Business Suite](using-ai-agent-workflows-na-cbs.md)**  
Agentic workflow in Now Assist for Core Business Suite supports the Core Business Suite setup process through a conversational interface.
-   **[Configure groups and roles](../task/config-groups.md)**  
Configure groups and roles for Core Business Suite business units through the Now Assist conversational experience.
-   **[Create a notification](../task/create-notification-using-na.md)**  
Create notifications for Core Business Suite business units through the Now Assist conversational experience.
-   **[Edit a notification](../task/edit-existing-notification-using-na.md)**  
Edit notifications for Core Business Suite business units through the Now Assist conversational experience.
-   **[Bulk upload](../task/manage-bulk-upload-using-na.md)**  
Upload records in bulk for Core Business Suite business units through the Now Assist conversational experience.
-   **[Bulk edit](../task/manage-bulk-edit-using-na.md)**  
Edit records in bulk for Core Business Suite business units through the Now Assist conversational experience.

**Parent Topic:**[Configure Core Business Suite using Now Assist](configure-cbs-using-now-assist.md)


```


### File: core-business-suite\now-assist-configurations-requesters.md

```text
---
title: Now Assist requester experience
description: Requesters in CBS can use Now Assist in the conversational interface and in search functionality to raise requests and get AI-enabled responses.
locale: en-US
release: australia
topic_type: concept
last_updated: "2024-12-19"
reading_time_minutes: 1
keywords: [Now Assist configuration requesters CBS conversational interface search business units Employee Center]
breadcrumb: [Use, Core Business Suite]
---

# Now Assist requester experience

Requesters in CBS can use Now Assist in the conversational interface and in search functionality to raise requests and get AI-enabled responses.

After the Core Business Suite application setup, requesters gain access to enhanced Now Assist capabilities. These configurations enable AI assistance for raising and managing requests across HR, Legal services, Health &amp; Safety, Workplace services, Finance, and Procurement.

**Note:** Depending on your license, you will have access to certain application features, generative AI skills, agentic workflows, and AI agents. For more information, see [ServiceNow product tiers](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/ai-native-sku-overview.md).

The Now Assist configuration activates automatically when the **CBS NAVA preset** runs during installation. This one-time action establishes the foundation for Now Assist enabled requester interactions. For more information, see [Core Business Suite Foundation default configurations](cbs-default-configs.md).

The conversational interface provides natural language interaction for request submission and support. Enhanced search functionality delivers relevant results from comprehensive data sources across departments.

The configuration aggregates data from all business units within your organization. This comprehensive data integration ensures requesters receive consistent and accurate information regardless of business unit affiliation.

The Now Assist search sources also consider your Employee Center content to resolve queries and service requests.

**Parent Topic:**[Using Core Business Suite](cbs-using-parent.md)


```


### File: core-business-suite\request-apo.md

```text
---
title: Raise an invoice request
description: Raise an invoice request for any payment-related issues as a supplier on CBS.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Core Business Suite]
---

# Raise an invoice request

Raise an invoice request for any payment-related issues as a supplier on CBS.

## Before you begin

Role required: sn\_slm.contact

**Note:** This role is manually assigned to anyone by the admin who has access to the Supplier Collaboration Portal.

## Procedure

1.  Navigate to **Supplier Lifecycle Operations** &gt; **Supplier Collaboration Portal** &gt; **Raise a request**.

2.  In the Categories list, go to **Invoices**, and select **Invoice request**.

3.  In the invoice request form, fill in the fields.

<table id="table_kqt_njk_khc"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Supplier

</td><td>

Name of the supplier who is raising the request.

</td></tr><tr><td>

Invoice number

</td><td>

Number of the invoice for which the request is raised.

</td></tr><tr><td>

What type of request is this?

</td><td>

The following are the options available:-   **None**
-   **Payment inquiry**
-   **Invoice inquiry**
-   **Expedite payment request**
-   **Payment terms issue**
-   **Invoice entry assistance**
-   **Other**


</td></tr><tr><td>

What can we help you with?

</td><td>

Field to provide details of the request or the issue.

</td></tr><tr><td>

Add attachments

</td><td>

Option to add an attachment related to the request.

</td></tr></tbody>
</table>4.  Select **Submit**.


**Parent Topic:**[Using Core Business Suite](../concept/cbs-using-parent.md)


```


### File: core-business-suite\request-emp-cbs.md

```text
---
title: Raise HR requests
description: Raise an HR request for general requests, payroll, or benefits on CBS.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Core Business Suite]
---

# Raise HR requests

Raise an HR request for general requests, payroll, or benefits on CBS.

## Before you begin

Role required: sn\_cbs.requestor

## Procedure

1.  Navigate to **Self-Service** &gt; **Employee Center**.

2.  In the **Help topics** widget, go to the topic card you require, in this case **Human resources**.

3.  Select any of the following options, fill in the required fields, and select **Submit**.

    -   **Benefits request**
    -   **Payroll request**
    -   **General HR request**

        For more information on the field descriptions of each request form, see the following:

        -   [HR service catalog management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/hr-service-catalog-management.md).
        -   [Report an issue with your payslip](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/employee-service-management/hr-service-delivery/payslips-awd.md).

**Parent Topic:**[Using Core Business Suite](../concept/cbs-using-parent.md)


```


### File: core-business-suite\request-emp-rest.md

```text
---
title: Raise requests on the employee portal
description: Raise a general request across departments, as an employee, on CBS.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Core Business Suite]
---

# Raise requests on the employee portal

Raise a general request across departments, as an employee, on CBS.

## Before you begin

Role required: sn\_cbs.requestor

## Procedure

1.  Navigate to **Self-Service** &gt; **Employee Center**.

2.  In the **Help topics** widget, go to the topic card as require, and select a request form.

    The following general request forms are available on the employee portal of CBS.

    -   **Human resources**
    -   **Workplace services**
    -   **Legal services**
    -   **Health and safety**
    -   **Finance**
    -   **Procurement**
    You can raise general, payroll, and benefits requests with the HR department on CBS. For more information, see [Raise HR requests](request-emp-cbs.md).

    For more information on configuring the Help topic widget display, see [Configure instance options for Help topics widget](instance-option-helpt.md).

3.  Provide the request details and select **Submit**.


**Parent Topic:**[Using Core Business Suite](../concept/cbs-using-parent.md)


```


### File: core-business-suite\request-slo.md

```text
---
title: Raise a general supplier request
description: Raise a general request for any common query or issue as a supplier on CBS.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, Core Business Suite]
---

# Raise a general supplier request

Raise a general request for any common query or issue as a supplier on CBS.

## Before you begin

Role required: sn\_slm.contact

**Note:** This role is manually assigned to anyone by the admin who has access to the Supplier Collaboration Portal.

## Procedure

1.  Navigate to **Supplier Lifecycle Operations** &gt; **Supplier Collaboration Portal** &gt; **Raise a request**.

2.  In the Categories list, go to **General**, and select **General request**.

3.  In the general request form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Who is this for?|Drop-down menu to select the name of the requester.|
    |Supplier|Name of the supplier who is raising the request.|
    |What can we help you with?|Field to provide details of the request or the issue.|
    |Add attachments|Option to add an attachment related to the request.|

4.  Select **Submit**.


**Parent Topic:**[Using Core Business Suite](../concept/cbs-using-parent.md)


```


### File: core-business-suite\reset-default-configurations.md

```text
---
title: Reapply the default configurations
description: If the default configurations aren’t applied for Core Business Suite or its business units, reapply the default configurations by running a script.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-04-05"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Reapply the default configurations

If the default configurations aren’t applied for Core Business Suite or its business units, reapply the default configurations by running a script.

## Before you begin

**Note:** When the default configurations aren’t applied, the following message appears:

Installation succeeded, but some default configurations couldn't be applied. Review and complete the remaining steps in configuration.

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Definition** &gt; **Script - Background**.

    The run script page opens.

2.  Copy this script and paste it into the script editor.

    ```
    var driverScript = new sn_cbs.CBSDriver();
    var result = driverScript.onBUTrigger("placeholder");
    gs.info(JSON.stringify(result, null, 2));
    ```

3.  Replace `placeholder` with the appropriate business unit name.

    **Note:** Use only the supported business unit names when replacing the text placeholder. Using an incorrect name can cause the script to fail.

    Business unit names are: CBS, WSD, LEGAL, HR, S2P, HEALTH, FCM.

4.  Select **Run Script**.

    After the script completes, the script-completed page displays the execution logs followed by a success message.


**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\set-up-cbs.md

```text
---
title: Install Core Business Suite Foundation
description: Install Core Business Suite Foundation to configure employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Configure, Core Business Suite]
---

# Install Core Business Suite Foundation

Install Core Business Suite Foundation to configure employee and supplier requests across Human Resources, Finance, Health and Safety, Legal, Workplace Services, and Source‑to‑Pay.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **Admin** &gt; **Admin Home**.

2.  On the Core Business Suite Foundation card, select **Set up**.

3.  Under available for installation, select **Core Business Suite**.

    The Application Manager opens in a new tab.

4.  Select **Install**, and then follow the on-screen instructions to complete the installation.

    **Note:** To install the latest versions, don’t modify the items listed in the Review Installation Details dialog box.

    Required dependent plugins are installed automatically, and required roles are added. For information about the components installed with a plugin, see [Find components installed with an application](https://www.servicenow.com/docs/bundle/australia-platform-administration/page/administer/plugins/task/find-components.html).

5.  Select **Apply default configurations**.

    Applying default configurations sets the required default settings for Core Business Suite.

    For information about the default configurations, see [Core Business Suite Foundation default configurations](../concept/cbs-default-configs.md).

    If the default configurations aren’t applied, run the script to apply them. For more information, see [Reapply the default configurations](reset-default-configurations.md).


## What to do next

Install the Core Business Suite applications. For more information, see [Install Core Business Suite applications](../concept/install-cbs-apps.md).

-   **[Core Business Suite Foundation default configurations](../concept/cbs-default-configs.md)**  
Details of the default configurations for Core Business Suite Foundation.

**Parent Topic:**[Configure Core Business Suite Foundation](../concept/configure-cbs.md)


```


### File: core-business-suite\source-to-pay-default-configurations.md

```text
---
title: Source-to-Pay default configurations
description: Details of the default configurations for Source-to-Pay.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Source-to-Pay, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Source-to-Pay default configurations

Details of the default configurations for Source-to-Pay.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Source‑to‑Pay workflows and communication.|
|Intake forms|Activates required intake forms for submitting supplier, procurement, and invoice‑related requests and capturing request details.|
|Supplier collaboration|Configures supporting settings that enable collaboration between internal users and suppliers.|

**Parent Topic:**[Install Source-to-Pay](../task/install-source-to-pay.md)


```


### File: core-business-suite\using-ai-agent-workflows-na-cbs.md

```text
---
title: Agentic Workflow in Now Assist for Core Business Suite
description: Agentic workflow in Now Assist for Core Business Suite supports the Core Business Suite setup process through a conversational interface.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-23"
reading_time_minutes: 1
breadcrumb: [Now Assist for Core Business Suite, Configure Core Business Suite using Now Assist, Configure, Core Business Suite]
---

# Agentic Workflow in Now Assist for Core Business Suite

Agentic workflow in Now Assist for Core Business Suite supports the Core Business Suite setup process through a conversational interface.

<table id="table_gyx_brq_l2c"><thead><tr><th>

Agentic workflow name

</th><th>

Description

</th><th>

Available AI agents

</th></tr></thead><tbody><tr><td>

AI agentic workflow for the CBS setup

</td><td>

Supports Core Business Suite configuration through a guided, conversational setup flow. The workflow walks administrators through setup steps, tracks configuration progress, and identifies the next configuration actions. If a setup step doesn’t complete successfully, the workflow provides contextual guidance to address the issue and continue the setup process.

</td><td>

-   IA Orchestration agent
-   Manage groups and roles agent
-   Notification agent
-   CBS bulk upload agent

</td></tr></tbody>
</table>## AI agents used in the AI agentic workflow for the CBS Setup

The following AI agents are used to support the conversational setup process for Core Business Suite.

|AI agent name|Description|
|-------------|-----------|
|IA orchestration agent|Coordinates CBS and business unit setup steps by sequencing installation and configuration actions based on user input and the current system state.|
|Manage groups and roles agent|Creates and assigns groups and roles across CBS business units to support setup requirements without manual navigation.|
|Notification agent|Configures notification settings for CBS business units to support request, approval, and workflow notifications.|
|CBS bulk upload agent|Processes bulk data uploads for Workplace Services and Source‑to‑Pay business units by importing records and configuration data.|

For more information on the AI agents, see [Now Assist AI agents](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/intelligent-experiences/na-ai-agents.md).

**Parent Topic:**[Now Assist for Core Business Suite](now-assist-cbs.md)


```


### File: core-business-suite\workplace-default-configurations.md

```text
---
title: Workplace Services default configurations
description: Details of the default configurations for Workplace Services.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-29"
reading_time_minutes: 1
breadcrumb: [Install Workplace Services, Install Core Business Suite applications, Configure, Core Business Suite]
---

# Workplace Services default configurations

Details of the default configurations for Workplace Services.

These default configurations are applied automatically when Apply default configurations is selected during installation.

|configuration|Description|
|-------------|-----------|
|Notifications|Configures standard notifications to support Workplace Services workflows and communication.|
|Intake forms|Activates required intake forms for submitting Workplace Services requests and capturing case details.|
|Workplace services|Configures required Workplace Services that support request handling and fulfillment.|

**Parent Topic:**[Install Workplace Services](../task/install-workplace-services.md)


```
