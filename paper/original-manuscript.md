# Master Data Management: Business Case and Roadmap for MDM Architecture

**Author:** Sujit Adhikari

> **Archival transcription:** This file reproduces text extracted from the author's supplied 23-page academic manuscript. The original contained page layout, a Data Service Federation diagram, and tabular material that may not be faithfully represented in the text extraction. Minor extraction artifacts, typographical errors, and original claims remain. It is presented as historical coursework, not as a revised or peer-reviewed publication. For research interpretation and corrections see [research overview](research-overview.md).



---

<!-- Original manuscript page 1 -->


    Business Case and Roadmap
      for MDM Architecture
                           Sujit Adhikari


Table of Contents
   1. Executive Summary                     3


---

<!-- Original manuscript page 2 -->


   2. Introduction                                              6

   3. MDM Program Journey Map                                   8
         a. Key Assumptions of MDM Program                      8
         b. IT Governance Plan                                  9
         c. Set Clear Objectives                                10
         d. Own/Access Data Map                                 12
         e. Data Sources Described                              14
         f. Define Master Data Domaine                          15
         g. Identify Hierarchies, Relationships and Groupings   17
         h. RoadMap/Implementation Plan                         18
   4. Summary                                                   20
   5. Conclusion                                                22


Executive Summary:


---

<!-- Original manuscript page 3 -->


Master Data Management is the framework of processes and technologies aimed at creating and
maintaining an authoritative, reliable, sustainable, accurate, and secure data environment that
represents a “single and holistic version of truth” for master data and its relationships, as well as
an accepted benchmark used within an enterprise as well as across enterprises and spanning a
diverse set of applications systems, lines of business, channels, and user communities (Berson &
Dubov, 2010). In short, Master Data Management provides a unified service which provides
accurate, consistent, and complete master data across the industry and to the stakeholders. One of
the key details to understand in the Master Data Management is that MDM is not just a
technological problem, rather it is more of a political problem since the business has been
changing dynamically these days. Moreover, Master Data Management includes both creating
and maintain master data. It is futile to invest a lot of money, time, and effort in creating a clean,
consistent set of master data unless the solution includes tools and processes to keep the master
data clean and consistent as it gets updated and expands over time.

The company we are discussing in this paper is the ABC company, which specializes in the sale
of pet foods. ABC company has Click and Mortar business model, which means the company
has both online and physical store in operation. The company was established in 2015 in San
Francisco. The company has been running smoothly and has seen exponential growth during 5
years of its operation. Due to COVID, the company has seen the drastic decrease in its physical
store sales and has seen a good increase in the online sales. The buying behavior of customers
has really changed during COVID, however, the company used to make more sales in the
physical store before, and now that the company must use the shipping method to send the
products to its customers, the company is incurring more sales cost. ABC company is looking to
expand its line of product. Before it used to sell pet foods only, but now the company is focusing
on expanding the line of product to pet foods, pet beds, pet toys and other pet related accessories.
The goal of the company is to increase the customer satisfaction while providing the best quality
of product.

The business case we are looking to address in this paper is the extension of new product line
and merging of departments. There are three different departments in the company, namely Sales
Department, Accounting and Finance Department and Operation Department. Now that the
company is looking to expand the line pf product, the company’s research team has come up


---

<!-- Original manuscript page 4 -->


with the plan to work Sales Department and Accounting and Finance Department together. It
does not necessarily mean that the two departments will be merged, but it does mean that they
will be working interconnectedly.

Since the company is looking for further business development by expanding its product line, it
is essential to identify the key business drivers while building the Master Data Management
System in the company. Some of the business drivers are listed below:

       Screening new prospects
       Cross-sell/up-sell existing customers
       Effectiveness of Marketing Campaigns
       Recurring revenue from existing customers
       Retention of “good” customers
       Recognition of “bad” customers

This paper’s recommendation for the effective expansion of the product line is by investing in
the Master Data Management platform. Since ABC company has a limited amount of budget, it
is suggested that they invest in Virtual Integration (Data Service Federation) at first. This pattern
uses data virtualization to provide one or more on-demand integrated views of master data
entities such as customer, product, asset, employee etc. even though the master data is fractured
across multiple underlying systems. One of the major advantages of Data Service Federation
architecture is that it is less costly than the available architectures, since the data does not have to
be physically copied from one location to another nor any additional storage space is required. In
this architecture, applications, processes, portals, reporting tools and data integration workflows
needing master data can acquire it on-demand via a web service interface or via a query interface
such as SQL (Kumar, Pavan. (2014)).


---

<!-- Original manuscript page 5 -->


                            Data Service Federation (DSF), VI Model

Master Data Management system not only allows the company to enable centralized and de-
centralized management of data, but also links all the critical business data of an enterprise to a
single point of reference, which helps in reducing errors and makes business processes less
redundant (Caous, 2019).


---

<!-- Original manuscript page 6 -->


Introduction:

The main business case for this company is the expansion of the product line. It means the
company is looking for further business development, which comprises of enabling strong sales
and marketing team as well. It is key to understand that the company is already in a proper shape
and due to COVID, the company was able to shift its focus from physical store to the online
store. To expand the new product lines, the company is hesitant to invest in the technology, and
is not sure how the data management plays a significant role in helping the company’s growth
and decisions. In order to make the company understand how the installation of Master Data
Management System in the company works, it is vital for the company to understand the major
drivers that drive the current business case of the company. Some of these business drivers are
listed below:

      Screening new prospects
      Cross-sell/up-sell existing customers
      Effectiveness of Marketing Campaigns
      Recurring revenue from existing customers
      Retention of “good” customers
      Recognition of “bad” customers



The purpose of this business case is to distinguish the value the business drivers will bring to the
targeted changes in the company. Let’s analyze each business cases with their values:

Screening new Prospects: Since the company is looking to expand the current market they are in;
it is essential to analyze and value the new prospects. For example: it must be analyzed how the
addition of new product line will affect the current products, how the addition of the new
products will change the operation of the industry and most importantly how it will push the
company for changes. For all this, one of the crucial tools to use is the data analytics, which will
help predict the future growth of the company and will help decide if it is the right time for the
company to move forward with the product. In addition, the better data analytics can be carried
out if the structure of the company is conducive, and for this Master Data Management System is
a best option.


---

<!-- Original manuscript page 7 -->


Cross-sell/up-sell existing customers: Cross-selling to the existing customers will be one of the
main targets of this company, since the line of product the company is looking to bring in is
similar to what it was already selling. However, the issue with cross-sell is that the company will
need to find out if the customer is the existing customer or the new customer. The company does
not have the database system that allows them to understand the recurring customers. This limits
the company from distinguishing the loyal customers to seasonal customers. The proper Master
Data Management system would elude such company’s weaknesses and will help in architecting
the ideas and solutions in an effective manner.

Effectiveness of Marketing Campaigns: ABC company has been in operation since 2015 with a
single store in San Francisco and has been doing well until now, however, the company wants to
scale its operation, which requires several other tools to succeed. Marketing Campaigns are one
of those crucial tools to help the company boost sales, however, it is equally imperative for the
company to keep track of the effectiveness of marketing campaigns. This can be done with the
proper IT or database foundation in the company, which will provide information on how the
campaigns are going. Based on the data, the management can decide whether they want to stick
to the plan or change the nature of the campaign.


---

<!-- Original manuscript page 8 -->


MDM Program Journey Map:

Key Assumptions of MDM Program

The crucial thing to understand while building Master Data Management Platform is that it is
essential to understand the data first. There are certain criteria that should be considered together
when deciding if a data entity is treated as a master data. Some of those criteria are data
behavior, lifecycle, cardinality, lifetime, complexity, value, volatility and reuse. In short, while it
is simple to enumerate the various master data entity types, it is sometimes more challenging to
decide which data items in a company should be treated as master data (Master Data
Management - What, Why, How & Who, 2019). In this scenario, it is better to categorize them in
terms of their behavior and attributes within the context of the business needs. Hence, Master
Data Management system plays a significant role in this aspect of keeping the master data.
Master Data Management includes both the creation and maintenance of master data. The
solution includes tools and processes to keep the master data clean and consistent.

There are six key disciplines of a strong Master Data Management Program. They are briefly
discussed below:

Governance: Basically, data governance is a crucial part in MDM program and it comprises of
directives that manage the institutional bodies, principles, policies and qualities to promote
access to accurate and certified Master Data. In short, this process is the gateway for a cross-
functional team that defines various aspects of the MDM program.

Measurement: This defines the KPIs. KPIs are the key performance indicators to check where
the company/department stand in achieving the specific goal. These KPIs look at data quality
and continuous improvement.

Organization: It is essential to put right people/resources at a right place in a right time. This
includes master data owners, data stewards and those participating in the governance.

Policy: The requirements, policies, and standards to which the MDM program should adhere.

Process: These are the processes defined to manage master data across the data lifecycle.

Technology: The master data hub and any enabling technology.


---

<!-- Original manuscript page 9 -->


IT Governance Plan:

IT Governance consists of the leadership, structures and processes that enable an organization to
make decisions to ensure that its IT sustains and extends its strategic and objectives (IT
Governance, 2016). Data Governance Plan is just like a law. This is required as the MDM project
is being developed and once the project is developed as well. For example: When the
departments which use the MDM get confused which data to choose from (in case of data
discrepancy), then they should have something to look up to. This will ease the confusion.
Without it, the MDM program will be full of confusion after certain weeks, which will result in it
to be more expensive, lost opportunities and eventually lost or dissatisfied customers.

ABC company is not a highly established company; therefore, the budget of the company is
limited. The company is seeking to invest in the Master Data Management Program to remain
competitive in the market. Virtual Integration architecture called Data Service Federation have
been suggested for ABC company. The proper IT Governance Plan are listed below:

   a. The management of data in ABC company cannot be only categorized as IT problem, but
       as the MDM system will start taking place, it will be managerial challenge as well. Since
       this company is not a very big company, and the recommended architecture does not also
       require highly technical architecture, it is recommended that the MDM management
       should be heavily linked with the business and least with the IT group. With proper
       training, the business team should be able to grasp the idea of handling the recommended
       MDM platform. As the company grows and the need to upgrade the MDM systems arise,
       the share of responsibilities between business and IT shall be discussed and decided
       accordingly.
   b. As per the business needs, the platform will be customized.
   c. Since Virtual Integration model is the cloud model, there will be an option for storage
       expansion.
   d. Training will be provided to ABC company’s teams to operate the MDM platform. The
       recommended MDM platform does not require relatively higher technical skills, therefore
       the training and education can be completed within a month time.


---

<!-- Original manuscript page 10 -->


Set Clear Objectives:

It is important to align the business needs with the solution that we are presenting. In order to do
so, it is imperative to understand the business problem at first. The business case we are looking
to address here is the extension of new product line and merging of departments. There used to
be three different departments in the company, namely Sales Department, Accounting and
Finance Department and Operation Department. Now that the company is looking to expand the
line ff product, the company’s executive has come up with the plan to work Sales Department
and Accounting and Finance Department together. It does not necessarily mean that the two
departments will be merged, but it does mean that they will be working interconnectedly.

While building the objectives, many things are taken into consideration. Firstly, the most
important aspect is the budget of the company. It makes sense to build the MDM platform as per
the customer’s needs and budget. The second thing is the requirement of resources. The central
repository needs to be formed which collects all the data of the company, and then the automated
system will create the virtual integration for the company in one place to see how the company is
performing. This helps the company compare among the KPIs and can make data-based
decisions.

The objectives of this Master Data Management Platform are as follows:

   a. To make master data and make it available to end users of the company. This allows the
       company to make informed decisions.
   b. To connect the central repository with the virtual integration system. In this case we will
       be building Data Service Federation architecture. This allows the result to be seen at one
       place, which can then be evaluated with the company’s KPIs. This helps the company to
       analyze if the company’s strategy in expanding the new product line was right.
   c. To minimize data redundancies and duplicates for accurate data analysis.
   d. To enhance existing data from either internal systems or external vendors. The company
       right now has the internal data, which will soon be transferred into a central repository
       system in a cloud storage. After we collect the data, it is important to validate the data
       quality. To do that, one of the things we can do it match customer records with that of the
       third-party corporate hierarchies such as D&B or InfoUSA will provide that view.


---

<!-- Original manuscript page 11 -->


   e. To engage the stakeholders early in the journey to educate them about MDM and the
      value it will bring the organization. If this is done, then the MDM platform can be
      implemented by the business as well. When the business becomes capable of
      implementing its own MDM, then time, effort and cost can be saved from the IT.
      Independent team in an organization can bring value to the company faster.
   f. To properly define the business problem that the MDM is trying to help solve, In ABC
      company, the company is looking for the system that will help it make more informed
      decision on whether they should expand the new product line, and eventually acquire the
      company and go full e-commerce. The only thing that can provide solution to this
      dilemma is the study of the data, which is accurate and comes in the right format. When
      the analysis is done on this, it makes the company’s job much easier to make an informed
      decision.
   g. To scale the ABC company. The main purpose of the MDM platform in ABC company is
      to help in making decision in expanding product line. Once this is done, the company
      also seeks to scale its MDM platform as the size of the business also grows.


---

<!-- Original manuscript page 12 -->


Master Data Hub Focus:

Generally, an MDM hub can be used for either operational or analytical purposes. In our case,
we will be using MDM hub for analytical purpose. This will support ABC company in deciding
on whether the company should expand its product line. For the analytical data hub, the data may
be stored in a data warehouse or data marts to be utilized by BI tools for predictive analytics.
With the use of the predictive analytics tool, the company can decide whether it is the right time
to expand the product line. Several ad hoc queries and reports can be generated to help the
decision-making process.

MDM hub is the database with the software to manage the master data that is stored in the
database and keep it synchronized with the transactional systems that use the master data (Serra,
2020). Master Data Management hub has three basic styles. They are briefly discussed below:

   a. Repository: The entire collection of the master data is stored in database. This database
       includes all the attributes required by all the applications that use the master data. The
       applications that consume, create or maintain master data are all modified to use the
       master data in the hub. For example, if the system has the CRM application, then it would
       be modified to use the customer table in the master data hub instead of its own customer
       table.
   b. Registry: Registry is the opposite of the repository approach. In registry, each source
       system remains in control of its own data and remains the system of entry, so none of the
       master data records are stored in the MDM hub (Serra, 2020). All source system data
       records are mapped in the master data registry, making the master data registry the
       system of record. Data Maps play a vital role in registry. It shows the relationship
       between the keys of the difference source systems.
   c. Hybrid: This system includes the features of both repository and registry models. They
       way this hybrid system works is that it leaves the master data records in the application
       databases and maintains keys in the MDM hub, as the registry model does. It reproduces
       the attributes for each master entity in the MDM hub. With this, a significant number of
       MDM queries can be satisfied directly from hub database. In addition, the only queries
       that reference less-common attributes have to reference the application database.


---

<!-- Original manuscript page 13 -->


The key benefits of this model are as follows:

   a. Acceleration of revenue growth
   b. Enrichment in customer insights
   c. Improvement of customer experience
   d. Enhancement of regulatory compliance

   A customer MDM hub is a centralized repository of customer information from which
   multiple applications and downstream systems can pull the most accurate and timely
   information (Lyons, 2020). This specific hub automates the business process of optimizing
   accuracy and availability of shared customer data with the goal of establishing absolute
   confidence in data-driven decision-making (Lyons, 2020). The key reason why customer
   mdm hub is in practice is because it ensures that the customer data is accurate, consistent,
   timely and available, which can be used to better execute operational and analytical
   processes.


---

<!-- Original manuscript page 14 -->


Own/Access Data Map

The producers, consumers, and owners of the data may be different, depending on whether the
system is being used for operational or analytical purposes. It really does not matter what the
MDM can do, but what is needed, therefore the important aspect to understand is the usage.
Since the focus of the company currently is on the analytical MDM, users typically access the
data through a data warehouse or data mart rather than accessing it directly from the hub. In this
scenario, the IT department normally addresses the requirement made by the analytical team of
the company, however, the concern is that the users need to be involved early in the development
process so that they can determine which data is needed. The analytical team wants the data to be
directly fed into their systems.

Therefore, the data from this MDM is intended to be used by the analytical team to make the
decision for the company’s business issues.


---

<!-- Original manuscript page 15 -->


Data Sources

The objective of the MDM program will dictate what data sources are loaded into the hub. One
of the key reasons that the company uses Master Data Management Systems is to resolve a
duplication issue or to create a golden record from multiple sources. Anything can happen while
managing the data, especially the duplication of data. Therefore, it is even more crucial to choose
the proper data sources and build a model around it. The data duplication can come from the
same source system or from the multiple one. There are certain companies that use third-party
data sources.

For ABC company, there are two kind of data sources that are required. One is the internal data
sources, and the other one is the third-party data sources or the external data sources. The reason
why these two data sources are required for ABC company are briefly discussed below:

   a. Internal Data Sources: As discussed, the business focus of ABC company is to expand
       the product line. It is important to learn about the other companies and the market in
       order to make a decision on this issue, however, it is even more crucial for the company
       to look at the internal structure of the company. The company needs to look at what is
       happening with its finances, what are the effects of being e-commerce focused company,
       how are the operational costs functioning in the company and etc. In order to find out all
       these, the company needs to look at the data it collected internally. In the internal data,
       there might be some redundancies, and duplications, which will require match and merge
       to avoid the duplication and help in proper analytics.
   b. External Data Sources: The decision to expand the product line does not always depend
       on how the company is functioning currently. It requires more research than just internal
       evaluation. ABC company, in this case, needs to assess the market demand for the
       products, prevalent competitions, competitive advantages if available, and so on. In order
       to carry out the analytics on these aspects, the company requires external/third-party data.
       This data will help the analytical team to better analyze the market and make data-driven
       decisions.


---

<!-- Original manuscript page 16 -->


Define Master Data Domaine:

One of the most difficult questions every company struggles with in the MDM program is the
definition of data domain (Team, 2020). The company needs to define the elements in the data.
For example: how is “customer” defined? Does customer include inactive customers or
prospects? How is “products” defined? What kind of elements does a product include? What is a
location? Is it a place or a building or a department?

The main goal of MDM system is to match and merge data, not to create a data mart or data
warehouse. The elements of the data need to be concisely and precisely crafted because the
nature of the data determines the quality of data the company gets to perform analytics.


---

<!-- Original manuscript page 17 -->


Identify Hierarchies, Relationships, and Groupings:

In most of the cases, hierarchies, relationships, and groupings are an afterthought, decided on
during an implementation (Team, 2020). Hierarchies are typically more ueful for analytical MDM
than for operational MDM. The key hierarchies needed for ABC company to carry out the
desired output is customer hierarchies, market share hierarchies, market competition hierarchies,
sales hierarchies, operational cost hierarchies etc.

Relationships between the master data elements are very useful. Some examples of the
relationships are parent-child relationship, spouse to spouse for customers. The relationships play
a vital role in analytics as well. For example: If ABC company can find out that its most loyal
customers are getting the pet products from other stores, then it would be very useful. At least,
they know that if the company can match the market price, then it already has the customers.

Groupings are similar to relationships. Most of the MDM systems handle groupings same way
internally. An example of grouping can be housings and region. For this, address is a prerequisite
before being able to create these two groupings. For ABC company, it can use the grouping
functionality to filter its customers, based on location, gender or marital status. Then it can use
the data to select the target audience. For example: unmarried people are more lonely, so they
might have pets more than married couple might. If the analytical team says this is true, then the
company can decide to focus more on single people than married couples.


---

<!-- Original manuscript page 18 -->


RoadMap/ Implementation Plan:

An enterprise that begins an MDM program without a properly defined implementation roadmap
will not be able to proactively understand the target state of MDM and tis evolution from release
to release. This will adversely impact planning and the ability to execute the program (Berson &
Dubov, 2010). The following roadmap views are included in the roadmap development plan:

   a. Business Benefits: This tops the list of roadmap views. The business benefit for the ABC
       company would be that the MDM system implementation will help the company in
       deciding whether they should go on to expand the product line.
   b. Systems and Applications in Scope of MDM: ABC company is the small company,
       therefore for now, the company is not looking to heavily invest in the MDM system. The
       company is looking to build the central repository that collects all the data, and connects
       the repository to the Data Service Federation, which is the MDM framework. This will
       help in analytical aspect of the business.
   c. Data Domains, Entities, and High-Level Data Model: The data domains, entities and
       data models need to be defined properly before building the MDM system. MDM hub is
       to be used here. ABC will be using the single domain system because this is cost
       effective and can carry out the task required.
   d. Relationships, Hierarchies, and Metadata: The value of MDM highly relies on what
       the program does to manage relationships among master entities. If the relationships are
       well-built, then the result will also come to be very useful, however, if the relationship is
       not based on proper attributes, then the end-result will not be useful. In order to build
       entity relationships and hierarchies in ABC company, we will use an external trusted
       source of relationships and build relationships and hierarchies by comparing in-house
       master data with external trusted sources. This helps in analyzing external environment as
       well as matching and merging to avoid redundancies.
   e. Third-Party Data Sources: Here, a data hub matches enterprise master data with the
       third-party data, which helps improve the quality of the matching process and enhances
       entity and relationship resolution (Berson & Dubov, 2010).
   f. Decommissioning of Systems and Applications: Since the MDM system we are
       building for ABC company is very simple, and we have thoughtfully put together the


---

<!-- Original manuscript page 19 -->


      needed elements only, we do not have to decommission systems and applications.
      However, during the course, if the team finds out any component that is irrelevant, then it
      will be decommissioned to save the cost.
   g. Data Hub Usage Style: Since most of the business value is dependent on the analysis of
      the data, we will be selecting the analytical Master Data Management. This focuses on
      data warehousing, business intelligence, reporting, and analytical applications.
   h. Data Volumes and Performance Considerations: Since the company is in the growth
      phase, the data volumes and performance will be considered based on the budget they can
      afford.
   i. Deployment Strategy: The roadmap view defines what users will be impacted by the
      new processes and applications enabled by MDM, as well as when and how. For ABC
      company, the company, as a whole, will be impacted with the new processes and
      applications. Even if the company finds out that it is probably not the right time to
      expand the new product line, it can pull together several other analytics to increase the
      sales of the existing products i.e. pet foods. This can be done by performing predictive
      and ad hoc analyses on the data that are put in the data warehouse or data marts.
   j. Related Initiatives: For ABC company, there are several other related initiatives that
      come along with the admission of MDM project. The strong data warehouse will be built,
      there will be client and product hierarchy management, and CRM initiative.
   k. Master Data Governance Maturity: This is the key roadmap in implementing MDM
      plan. ABC company is not a highly established company; therefore, the budget of the
      company is limited. The company is seeking to invest in the Master Data Management
      Program to remain competitive in the market. Virtual Integration architecture called Data
      Service Federation have been suggested for ABC company.
   l. Master Data Quality Processes, Metrics, and Technology Support: The kind of MDM
      system the ABC company is planning to implement does not require high level of
      technology support. It does require certain level of training and education.
   m. Enabling Technologies: Since the MDM system will comprise of the data warehouse or
      data marts, there will be the need of ETL. SOA (service-oriented architectures) is also
      important to facilitate an MDM implementation from the integration perspective.


---

<!-- Original manuscript page 20 -->


Conclusion:

To conclude, ABC company is a small sized company, who is looking to scale up by expanding
its product line in San Francisco Bay Area. Since the company is looking for further business
development by expanding its product line, it is essential to identify the key business drivers
while building the Master Data Management System in the company. Some of the business
drivers are listed below:

       Screening new prospects
       Cross-sell/up-sell existing customers
       Effectiveness of Marketing Campaigns
       Recurring revenue from existing customers
       Retention of “good” customers
       Recognition of “bad” customers

This paper’s recommendation for the effective expansion of the product line is by investing in
the Master Data Management platform. Since ABC company has a limited amount of budget, it
is suggested that they invest in Virtual Integration (Data Service Federation) at first. This pattern
uses data virtualization to provide one or more on-demand integrated views of master data
entities such as customer, product, asset, employee etc. even though the master data is fractured
across multiple underlying systems. One of the major advantages of Data Service Federation
architecture is that it is less costly than the available architectures, since the data does not have to
be physically copied from one location to another nor any additional storage space is required. In
this architecture, applications, processes, portals, reporting tools and data integration workflows
needing master data can acquire it on-demand via a web service interface or via a query interface
such as SQL.

There are basically certain aspects that need to be constructed for the MDM program Journey.
The key disciplines for strong Master Data Management Program are Governance,
Measurement, Organization, Policy, Process and Technology. These all are the foundations that
the MDM system is built on. It is equally crucial to define the governance plan, which consists of
the leadership, structures and processes that enable an organization to make decisions to ensure
that it IT sustains and extends its strategic objectives. The objectives need to be set clear because
without the mission and vision, the MDM system will meet the requirement of the customer.


---

<!-- Original manuscript page 21 -->


Moreover, Since the focus of the company currently is on the analytical MDM, users typically
access the data through a data warehouse or data mart rather than accessing it directly from the
hub. In this scenario, the IT department normally addresses the requirement made by the
analytical team of the company, however, the concern is that the users need to be involved early
in the development process so that they can determine which data is needed. In addition, an
enterprise that begins an MDM program without a properly defined implementation roadmap
will not be able to proactively understand the target state of MDM and its evolution from release
to release.

The next steps required to move forward with the MDM program are as follows:

    a. Assess the budgetary commitment from the management
    b. Review the Business Case of ABC company.
    c. Get the analytical team ready

The above listed three things are very important before committing to the MDM system. Firstly,
the proposed MDM system aligns with the budgetary outlook of the company, however, it is
suggested that the company look at the budget of the MDM system again. In addition, the
proposed MDM system is based on the business case of expansion of product line. The
management needs to decide if expansion of the product line is the route they are taking for
scaling the company. Finally, the entire MDM system is based on analytical approach, therefore,
the company needs to have their analytical team ready. This is important because the MDM
system suggested is a low-budget system and does not provide much IT support. It has been
considered that the company already has an analytical team or will get an analytical team ready
for the task.

Therefore, I hereby request the approval to proceed with the proposed MDM system.


References:


---

<!-- Original manuscript page 22 -->


Berson, A., & Dubov, L. (2010). MASTER DATA MANAGEMENT AND DATA GOVERNANCE,
       2/E (2nd ed.). McGraw-Hill Education.
Caous, J. (2019, October 31). Importance of Master Data Management for Business Success. To
       Increase. https://www.to-increase.com/business-integration/blog/importance-of-master-
       data-management-for-business-success#:
       %7E:text=Master%20Data%20Management%20(MDM)
       %20is,makes%20business%20processes%20less%20redundant.&text=MDM%20enables
       %20centralized%20and%20de%2Dcentralized%20management%20of%20data.
Data Federation - an overview | ScienceDirect Topics. (2012). Science Direct.
       https://www.sciencedirect.com/topics/computer-science/data-federation
Enterprise Master Data Management Trends and Solutions. APOSTOL, Constantin-Gelu,
http://revistaie.ase.ro, Vol. XI, no. 3/2007

IT Governance. (2016, February 24). The MITRE Corporation.
       https://www.mitre.org/publications/systems-engineering-guide/enterprise-engineering/
       enterprise-planning-and-management/it-governance
Kumar, Pavan. (2014). Master Data Management.

Lyons, B. (2020, October 21). Four Ways a Customer MDM Hub Can Add Value. First San
       Francisco Partners. https://www.firstsanfranciscopartners.com/blog/four-ways-a-
       customer-mdm-hub-can-add-value/
Master Data Management - What, Why, How & Who. (2019, November 20). Enterprise Master
       Data Management • Profisee. https://profisee.com/master-data-management-what-why-
       how-who/
Serra, J. (2020, September 4). Master Data Management (MDM) Hub Architecture | James
       Serra’s Blog. James Serra’s Blog | Big Data and Data Warehousing.
       https://www.jamesserra.com/archive/2013/01/master-data-management-mdm-hub-
       architecture/#:
       %7E:text=The%20Master%20Data%20Management%20(MDM,that%20use%20the%20
       master%20data.


---

<!-- Original manuscript page 23 -->


Team, E. I. S. (2020). Launching a Master Data Management Program: Eight Key Steps in the
Journey. Earley. https://www.earley.com/insights/launching-master-data-management-program-
eight-key-steps-journey
