```
Author:  Jake Lewandosky
Company: 55B Labs
Project: GovFlex Teammate Match
Date:    05/07/2019
File:    RouteMap.md

Latest Revision date: 05/07/2019

Brief:   Attempts to document GovFlex's new proposed site order and flow of operations. This will offer a clear plan and checklist to ensure all system requirements are met. This is accurate as of the latest revision date above. 
```

## UI Mock-up Site:
https://preview.uxpin.com/85e933f647a09aece41f1eaf4872c15561d2d4aa#/pages/108476406/simulate/sitemap?mode=if

# README
```
Assumptions made:

  The reader has a program that can read markdown documents. Writer suggestion is to download the latest version of Microsoft VS Code and use the extension markdownlint, version 0.26.0 or greater, by David Anson.


How to read this:

  - All things marked in bold and have the word view imply new web pages.
  - Everything marked in italics is a section of a webpage.
  - All things tagged with a question mark have unclear or unknown requirements.
  - Any place that there is inline text, is either a clearly understood purpose of the page or a useful tool-tip from the GovFlex site project owners.
  - Anything in quotes is direct verbage from the mock-up site. 
  - Words in square brackets are writer's insertion.
  - Words marked with curly braces and percent signs are shorthand variables for easy understanding of data displayed to the user.
```

# **Route Map**
***
## Table of contents:

### 1.) Home

### 2.) Market Research

### 3.) Start a Project

### 4.) Find a Provider

### 5.) Manage Projects

### 6.) Message Inbox

### 7.) Manage Invoice

***
***

## 1.) **HOME VIEW**
***

```
Purpose:

Landing page
```

### Header **TEMPLATE *[Base]* INHERITANCE** 
> GovFlex Title
> - Goes to **HOME VIEW** unless already there

> Legal Docs
> - Currently Empty _?_

> Academy
> - Open new tab to academy.govflexapp.com

> Blog
> - Open new tab to www.govflex.com/blog/

> Messages
> - Dropdown of recent messages
> - Currently empty [clicking on a message presumably redirects to the **MESSAGE THREAD VIEW**]
>> View All Messages
>> - **MESSAGE INBOX VIEW**

> Profile Picture Dropdown (Top Right)
>> Picture Area
>> - Listing of subscription plan and date
>> - Profile name
>> - Company _?_
>
>> **ACCOUNT VIEW**
>> - Currently empty _?_
>>> **PERSONAL SETTINGS VIEW**
>>> - Pop-up form with checkboxes auto-filled with user settings
>>> - Save settings button at bottom [pop-up saying *Settings Saved* after server responds]
>>
>>> **MANAGE ACCOUNT USERS VIEW**
>>> - Currently empty _?_
>>
>>> **ORGANIZATION PROFILE VIEW**
>>> - Currently empty _?_
>
>> Sharing
>>> **REFER A FRIEND OR COLLEAGUE VIEW**
>>> - Pop-up with a text field expecting a list of comma separated emails
>>> - Send email sends the email [from either the GovFlex site's email or the user's email _?_]
>>
>>> Email Website Link
>>> - Currently empty? [tool-tip saying the linked has been copied to clipboard]
>
>> Need Help
>>> Open Help Center
>>> - Open new tab for helpcenter.govflex.com
>>
>> - **SUBSCRIPTION VIEW**
> - Sign Out
***

### Body
> **2.) MARKET RESEARCH VIEW** button
> - "Learn more" directly beneath of button has tool-tip
>
> **3.) START A PROJECT VIEW** button
> - "Learn more" directly beneath of button has tool-tip
>
> **4.) FIND A PROVIDER VIEW** button
> - "Learn more" directly beneath of button has tool-tip
>
> **5.) MANAGE PROJECTS VIEW** button
> - "Learn more" directly beneath of button has tool-tip
>
> **6.) MANAGE INVOICES VIEW** button
> - "Learn more" directly beneath of button has tool-tip
***

### Footer
> - Twitter redirect
> - Facebook redirect
> - LinkedIn redirect
> - Terms of Service button
> - Contact Us button

***
***

## 2.) **MARKET RESEARCH VIEW**
***
```
Purpose:

"1.)  Based on a proprietary algorithm consisting of several points, calculate an opportunity releavance score (ORS) and win probability (PWIN) for any federal opportunity to a GovFlex customer.

2.)  Identity top 5 companies from SAM with highest ORS and PWIN based on a selected opportunity. These companies can be considered potential partners or competitors.

3.) Identify top 5 consultants from GovFlex Consultant database (DB) with highest ORS based on a selected opportunity that when added to the PWIN calculation, improves the PWIN."
```

### Header **TEMPLATE INHERITED from *[Base]***
> Insert the following to the left of the base buttons and to the right of the logo:
>> Market Research
>>- Same page
>
>> Find A Provider
>> - **FIND A PROVIDER VIEW**
>
>> Manage Projects
>> - **MANAGE PROJECTS VIEW**
***

### Searchbar
> Opportunity Search
> - Text field to "Search all opportunities" with a button to clear the entry and search button [Appears to take white space delineated data]
>> Dropdown to perform search with:
>> - "match any search term"
>> - "match all search terms"
>
>> Dropdown to show data with:
>> - "all results"
>> - "opportunity data"
>> - "award data"
>> - "favorites"
>
>> Dropdown to sort data with:
>> - "relevance"
>> - "award date"
>> - "NAICS code"
>> - "completion date"
>> - "pricing type"
>
>> Dropdown to view data in:
>> - "export"?
>> - "excel format"
>> - "CSV format"

> Opportunity Pipeline
>> - Display toggle pops up *Opportunity Pipeline*

> PWIN Score: {% variable %}
> - *PWIN Score Details* toggle
> - *PWIN Score Boost* toggle (only displays when *PWIN Details* is toggled on)  _?_
***

### PWIN Details panel
> Pie chart percentages of:
> - Opportunity Relevance
> - Customer Knowledge
> - D&B Z-Score
> - Win Rate
> - Win Probability
***

### PWIN Boost panel
> Left Panel
> - GovFlex IQ Teammate Recommendations (Top 5)
> Button to send a message to the selected teammate
>> Tile Entries:
>> - Radio button that selects only 1 of 5 tiles
>> - Name a representative from the company
>> - Picture _?_
>> - Company name
>> - Percentage of teammate match


> Right Panel
> - GovFlex IQ Provider Recommendations (Top 5)
>> Buttons:
>> - Add selected provider(s) to favorites
>> - Add selected provider(s) to Shared Providers
>> - Invite selected provider(s) to send a quote for services
>> - Send a message to the selected provider(s)
>
>> Tile Entries:
>> - Checkbox to select provider(s)
>> - Position of provider
>> - Picture of provider
>> - 4-star [5-star _?_] rating of provider
>> - Payment rate
***

### Filters sidebar
- Of all results, list all attribute that are available from the search into each category and use it as a checkbox
- Button to clear all currently checkboxed entries
> Categories:
> - NAICS Code
> - Potential Value
> - Opportunity Relevance
> - Agency
> - Product Services Code
> - Contract Type
> - Opportunity Type
> - Set-Aside Type
> - Pricing Type
***

### Search Results table
Attributes:
- Awarding Agency
- Contract Award
- Funding Agency
- NAICS
- PSC
- Posted Date
- Completion Date
- Relevance

> Entries
>> Awarding Agency
>> - Company name (all caps)
>> - Company picture
>> - Subsidiary _?_
>> - Radio button that selects the company to perform PWIN Score calculation and show algorithm
>
>> Contract Award
>> - Color coded string of variable length and composition
>> - Details
>>
>> Action Button (gear button) pop-up *Action Menu*
>>> Action Menu
>>> - Add to [user] favorites
>>> - Add to Pipeline
>>> - Post a Project
>>> - Tag Opportunity
>
>> Funding Agency
>> PSC
>> Posted Date
>> Completion Date
>> Relevance
>> - Percentage of relevance to search _?_
>
> - Various tags from aforementioned *Filters*
***

### Opportunity Pipeline table
```
Purpose:

"The Pipeline allows customers to import opportunities derived from the Federal Business Opportunities (FBO) and Grants.gov databases and track the opportunities from the lead stage through the award stage. The tool provides an organized view of opportunities including notations and important milestones.

Companies that track business development activities around their opportunties are more likely to reduce cost by streamlining opportunities and promoting those opportunities they are well positioned to pursue and win."
```

> Table Header
>> Actions for table
>> - Configure Stages
>> - Edit Opportunity
>> - Delete Opportunity
>> - Add Custom Opportunity
>> - Create a Project
>
> First data cell
> - Number of opportunities
> - Total money worth of some value _?_
>
> Following columns
> - Stage 1 Lead
> - Stage 2 Capture Planning
> - Stage 3 Proposal Development
> - Stage 4 Pending Award
> - Stage 5 Post Award
***
***

## 3.) **START A PROJECT VIEW**
***
### Post A Project panel
> Warnings of unfilled form data:
> - Project title
> - Project description
> - Service Provider Skills
 - GovFlex Non-Circumvention checkbox
 - Publish button (redirect to **FIND A PROVIDER VIEW**)
 - Cancel button (redirect to **MANAGE PROJECTS VIEW**)
***

### Tell Us About Your Project block
 - Exit button in the top-right (redirects to **MANAGE PROJECTS VIEW**)
 - Text field for project title [REQUIRED]
 - Project owner dropwdown lists employees _?_
 - Yes/No radio buttons for "Is this project associated witha Government Solicitation?"
 - Invoice label text field
 - Project description text field [REQUIRED]
 - Yes/No radio buttons for "Is the Service Provider required to work onsite?"
***

### Service Provider Skills block
 - Text field for essential keywords for provider profile [assuming to be dilineated with commas and/or white space] [REQUIRED]
 - Any/All radio buttons for search should use any or all of the keywords in text field
 - Button to attach files useful to service provider
***

### Project Visibility
Radio buttons to:
- "Browse" GovFlex marketplace for providers
- "Auto-Invite" to send an automatic alert to each matched service provider
- "Public" to make the project visibile to anyone on GovFlex marketplace.
***

### Privacy Mode
```
Purpose:

"Conceal company name and contact information until after quotes for work engagements have been received."
```
- On/Off radio buttons to use or not use private mode
***
***

## 4.) **FIND A PROVIDER VIEW**
***
### Header **TEMPLATE INHERITED from *[Base]***
> Insert the following to the left of the base buttons and to the right of the logo:
>> Market Research
>> - **MARKET RESEARCH VIEW**
>
>> Find A Provider
>> - Same page
>
>> Manage Projects
>> - **MANAGE PROJECTS VIEW**
***

### Provider Profiles flipbook tiles
>Buttons on the left to:
> - Message provider
> - Favorite the provider
> - Add to shared providers
> - Ask for quote from provider

- Profile picture
- Name
- Location

> Cards of profile:
>> Overview
>> - Position
>> - Title
>> - Ratings with number of reviews
>> - Payment rate
>> - Profile description
>> - Provider key skills
>> - Verification level
>> - Service Type
>> - Availability
>> - GovFlex Projects
>> - Experience
>
>> Agencies _?_
>
>> Contracts _?_
>
>> Resume _?_
>
>> Educations & Certs _?_
>
>> Reviews _?_
>
>> Tags _?_
***

### Filter sidebar
Checkboxes for:
- Performance Rating
- Category of expertise
- Service Provider Type/Cost _?_
- Availability
- Product Services Code
- Location
- Security Clearance
- Certifications
- References
- Agency
- Profile Completion
- Resume
***

### Search Bar and Results block
> Top search bar
> - Text field for search, button to clear, button submit search terms
>> Dropdown to show results for:
>> - Global search
>> - Shared providers
>> - Favorite providers
>
>> Dropdown for:
>> - Match any search term
>> - Match all search terms
>
>> Dropdown to sort by:
>> - Rating
>> - Best match
>> - Number of reviews
>> - Cost Low-High
>> - Most popular
>> - Name

> Profile cards table
> - Number of results shown at top
>> Card entries
>> - Act as buttons that select the profile to show at the top in *Provider Profiles* flipbook tiles
>>> Buttons on side of card to:
>>> - Favorite the provider
>>> - Add provider to bench [shared providers  _?_]
>>> - Get quote from provider
>>> - Message provider
>>
>> - Profile picture
>> - Job title
>> - Checkbox to select more than one provider and show at the top in *Provider Profiles* flipbook tiles, also displays the payment rate
>> - Verification level displayed on the side of the profile picture
***
***

## 5.) **MANAGE PROJECTS VIEW**
***
### Header **TEMPLATE INHERITED from *[Base]***
> Insert the following to the left of the base buttons and to the right of the logo:
>> Market Research
>> - **MARKET RESEARCH VIEW**
>
>> Find A Provider
>> - **FIND A PROVIDER VIEW**
>
>> Manage Projects
>> - Same page
***

### Project Owner Profile flipbook tiles
- Profiles cycle by the order of profiles listed in the *Search Results Table* below
> Profile picture block
> - Profile name and title
> - Profile picture
> - Profile company association

> Cards of Profile
>> Description block
>> - Name of project at the top
>> - Button to edit project
>> - Agency of project
>> - Solicitation number
>> - Estimated cost: {% amount %}
>> - Description
>> - 3 Key Provider Skills
>> - Posted date
>> - Start date
>> - End date
>> - Visibility
>> - Privacy Mode
>
>> Documents _?_
>
>> Messages
>
>> Tags _?_
***

### Searchbar and Search Results table
- Text field for searching projects, button to clear, button submit search terms
> Dropdown to show projects that are:
> - My Projects
> - Organization Projects
> - Closed Projects
> - Archived Projects
> - All Projects

> Dropdown to match by:
> - Any search term
> - All search terms

> Sort projects by:
> - Date posted
> - Status
> - Estimated Cost
> - Project Title
> - Customer
> - Organization

- Button to "Post a Project" which redirects to **START A PROJECT VIEW**

> Search table columns: {% numResults %}
> - Date posted
> - Project title
> - Project summary
> - Estimate
> - Status
***

### Project Steps collapsible blocks

 Card entries [BASE INHERITANCE]
 - Profile picture
 - Job title on side of photo
> Buttons to:
> - Message provider
> - View provider profile
> - Revise quote invitation
 - Name of provider
 - Payment rate

> Step 1: Quote Invitations Sent to Providers ({% numSent %})
>
> Card entries [CHILD INHERITANCE]
> - Sent date
> - Expiration date button _?_

> Step 2: Review Quotes & Choose a Provider ({% numReviewed %})
> Card entries [CHILD INHERITANCE]
> - Received date
>> Button to review quote
>> - Pop-up to reject, award, or cancel the quote (buttons at the bottom)
>>> Time and Rate block
>>> - Begin Date
>>> - Completion Date
>>> - Quote Hours
>>> - Payment Rate
>>
>>> Invoice block
>>>> Provider information
>>>> - Service Provider
>>>> - Quote total
>>> - GovFlex processing Fee
>>> - Expenses (Travel)
>>> - Finance charge
>>> - Invoice total

> Step 3: Active Work Engagements ({% numActive %})
> Card entries [CHILD INHERITANCE]
> - Awarded date
> - Status

> Step 4: Completed Work Engagements ({% numCompleted %}) _?_
***
***

## 6.) **MESSAGE INBOX VIEW**
***
### Header **TEMPLATE INHERITED from *[Base]***
> Insert the following to the left of the base buttons and to the right of the logo:
>> Market Research
>> - **MARKET RESEARCH VIEW**
>
>> Find A Provider
>> - **FIND A PROVIDER VIEW**
>
>> Manage Projects
>> - Same page
***

### Searchbar
> Messages
> - Text field to search with, button to clear, button submit search terms
>> Dropdown to show results:
>> - None
>> - Shared providers
>> - Favorite providers
>
>> Dropdown to match by:
>> - any search term
>> - all search terms
>
>> Sort by:
>> - Date (Newest)
>> - Date (Oldest)
>> - Provider
>> - Project Title
***

### Message Inbox block
 Header for inbox
 - Display number of message threads
 - Checkbox to select all [that are visible in table]
> Dropdown to mark all selected items as:
> - Read
> - Unread
> - Archived
 - Button to delete selected message threads

 Filter block
> Checkboxes to filter by:
> - Inbox ({% numInbox %})
> - Sent ({% numSent %})
> - Archived ({% numArchived %})

> Message thread entries
> - Name of recipient button [pulls up recipient profile]
> - Name of recipient company
> - Title of message thread button [pulls up thread]
> - [First] message quoted [may or may not be in full]
> - [Last] message received/sent date
> - Reply button opens up *Message Thread pop-up*
> - Archive button to mark thread as archived
***

### Message Thread pop-up
- Subject title at the top
- Exit button
- Number of messages displayed at the top
- Button to expand all quoted messages
- [Unnecessary _?_] Reply button
- Archive button to mark the thread as archived
> Prior messages
> - Name of sender
> - Profile picture of sender
> - Quote of message
> - Time sent
- Text field to type response message
- Button to attach files [store in a separate area of message thread _?_]
- Button to send message to recipient
***

### Footer
> - Twitter redirect
> - Facebook redirect
> - LinkedIn redirect
> - Terms of Service button
> - Contact Us button
***
***

## 7.) **MANAGE INVOICES VIEW**
***
### Header **TEMPLATE INHERITED from *[Base]***
> Insert the following to the left of the base buttons and to the right of the logo:
>> Market Research
>> - **MARKET RESEARCH VIEW**
>
>> Find A Provider
>> - **FIND A PROVIDER VIEW**
>
>> Manage Projects
>> - Same page
***

### Sub-header
- Total Outstanding ({% invoiceCostTotal %})
- Number of Engagements ({% numEngagements %})
- Number of Providers ({% numProviders %})
- YTD Expended ({% YTDExpended %})

### Searchbar and Search Results table
> - Text field to search with, button to clear, button submit search terms
>> Dropdown for payment status
>> - None
>> - Awaiting Payment
>> - GovFlex Processing
>> - Provider Paid
>
>> Dropdown to match results by:
>> - any search term
>> - all search terms
>
>> Dropdown to [sort by]:
>> - Invoice number
>> - Payment status
>> - Customer
>> - Due date

> Result entries by column
>> First column:
>> - Invoice number
>> - Due date
>> - [Type _?_] of project
>> - Name of who authorized payment and date
>> - Name of who accepted work and date
>
>> Second column:
>> - Job title
>> - Profile picture
>> - Name of profile
>
>> Third column:
>> - Graphic of current business step business transaction is in
>
>> Fourth column:
>> - Invoice amount _?_
>>> Action required (color coded)
>>> - None (green)
>>> - Pay Now (red)
>>> - GovFlex (yellow)
***

### Footer
> - Twitter redirect
> - Facebook redirect
> - LinkedIn redirect
> - Terms of Service button
> - Contact Us button
***
***