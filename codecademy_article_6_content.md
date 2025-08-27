> **Note:** The following article is reproduced verbatim from  
> Codecademy Team, *Codecademy* (2025):  
> [Figma Make Tutorial: Build Interactive Apps with AI](https://www.codecademy.com/article/figma-make-tutorial)  
> for internal educational use only (non-profit).

# Figma Make Tutorial: Build Interactive Apps with AI

Ever designed a great UI and thought, "I wish I could just make this work without jumping through extra tools or workflows"? What if you could bring your designs to life by describing what you want, no handoff, plugins, or context switching? That's precisely where Figma Make comes in!

Figma Make, launched at Config 2025, is Figma's AI-powered prompt-to-code environment that allows designers to build real, functional prototypes directly inside Figma. Unlike traditional files, it lets us use plain English to add logic, navigation, responsiveness, and interactivity to our designs without requiring manual coding.

Let's build a personalized finance app using Figma Make.

## Building a finance tracker app

In this project, we'll build a personalized finance tracker that helps users do exactly that, with a clean and interactive dashboard powered by Figma Make. This app gives users a snapshot of their financial health. It includes features like:

- A dashboard showing income, expenses, and account balances
- Monthly report generation, styled like a bank statement
- A transaction history with filters, tags, and categories

It's inspired by tools like Plaid, QuickBooks, and Notion-style finance templates, but it's streamlined for personal use.

Let's start by defining the visual structure, the wireframe. A strong wireframe sets the foundation for meaningful AI output.

Also, here's a video tutorial that walks through the same concepts step by step—with visuals, examples, and a real-time build. Use it alongside the text or on its own—whatever helps you learn best.

### Step 1: Create wireframes for your app

A wireframe is a low-fidelity blueprint of your app's layout. Create a wireframe for this app, focusing on the structure, which answers:

- "What goes where?"
- "How do screens connect?"
- "What components does the user need to interact with?"

Unlike typical prototypes, where wireframes are handed off to developers, in Figma Make, your wireframe becomes part of the functional build process. You can:

- Use it to plan the layout and logic clearly
- Feed it directly into the Figma Make file
- Guide your prompts more effectively, since the visual hierarchy already exists

Let's look at each screen in detail.

#### Screen 1: Dashboard overview

The dashboard is the main landing screen. It gives the user details of their current financial health, including their earnings and spending, and forming trends.

This screen will have:

- A top navigation bar with the app name and profile access
- Summary cards for total income and total expenses
- A toggleable line chart that switches views between income and expenses
- Quick action buttons like "Add Transaction", "View Report", "Export Data"

Here's a sample wireframe of the dashboard screen:

![Wireframe of a personal finance dashboard showing income, expenses, trends chart, and action buttons](https://static-assets.codecademy.com/figma-make/Wireframe-1-dashboard.png)
<sub>Source: *Codecademy*, Codecademy Team (2025).</sub>

> Note: The wireframes used here are just examples and you can use your layouts as the foundation for your prompts in Figma Make.

#### Screen 2: Monthly report page

The monthly report page will mimic a formatted statement view. Think of it like a printable snapshot of a user's income and expenses for any given month. It'll have the following components:

- A header with the report title and date filters
- A summary block showing totals and net savings
- A breakdown table by spending category
- A footer for optional disclaimers or notes

Here's a sample wireframe of this screen:

![Wireframe of a monthly financial summary with filters, income and expense overview, and a category breakdown table](https://static-assets.codecademy.com/figma-make/Wireframe-2-Monthly-financial-summary.png)
<sub>Source: *Codecademy*, Codecademy Team (2025).</sub>

#### Screen 3: Transactions details page

This is the most data-dense screen, designed to show the user a history of every transaction they've made. It'll have the following components:

- A search bar and filter options
- A list of transactions with details like date, amount, category, and description
- Pagination controls for large datasets
- Export functionality

Here's a sample wireframe of this screen:

![Wireframe of a transaction history page with search, filters, transaction list, and pagination](https://static-assets.codecademy.com/figma-make/Wireframe-3-Transaction-history.png)
<sub>Source: *Codecademy*, Codecademy Team (2025).</sub>

### Step 2: Set up your Figma Make file

Now that we have our wireframes, let's set up the Figma Make environment:

1. **Create a new Figma Make file**: Go to Figma and create a new file. You'll see a "Make" option in the file type selector.

2. **Import your wireframes**: You can either:
   - Create the wireframes directly in Figma Make
   - Import existing wireframes from other Figma files
   - Use the sample wireframes provided above as reference

3. **Set up the canvas**: Organize your screens in a logical flow, typically left to right or top to bottom.

### Step 3: Start with the dashboard screen

Let's begin building the dashboard. In Figma Make, you can use natural language to describe what you want:

**Prompt example**: "Create a dashboard with a header navigation bar, two summary cards for income and expenses, a line chart that can toggle between income and expense views, and three action buttons at the bottom."

The AI will generate the layout and basic styling. You can then refine it with more specific prompts:

**Refinement prompt**: "Make the income card green and the expense card red. Add icons to the action buttons and make them rounded with a subtle shadow."

### Step 4: Add interactivity and logic

This is where Figma Make really shines. You can add functionality without writing code:

**Navigation prompt**: "When the user clicks 'View Report', navigate to the monthly report screen."

**Data handling prompt**: "Create a data structure for transactions with fields for date, amount, category, and description. Display sample data in the dashboard."

**Chart functionality prompt**: "Make the line chart interactive. When users click the 'Income' or 'Expenses' toggle, update the chart data accordingly."

### Step 5: Build the monthly report screen

For the monthly report, you'll want to focus on data presentation and filtering:

**Layout prompt**: "Create a monthly report layout with a header showing the month and year, summary cards for total income, expenses, and net savings, and a detailed breakdown table."

**Filtering prompt**: "Add date picker controls that allow users to select different months. Update the report data when the date changes."

**Styling prompt**: "Style the report to look like a professional bank statement with clean typography and proper spacing."

### Step 6: Create the transaction history screen

The transaction history screen requires more complex data handling:

**Data structure prompt**: "Create a comprehensive transaction data structure with fields for ID, date, amount, category, description, and tags."

**Search functionality prompt**: "Add a search bar that filters transactions by description or category. Make it work in real-time as the user types."

**Pagination prompt**: "Implement pagination for the transaction list, showing 10 transactions per page with navigation controls."

### Step 7: Connect all screens together

Now it's time to make everything work together:

**Navigation system prompt**: "Create a navigation system that allows users to move between the dashboard, monthly report, and transaction history screens. Add a bottom navigation bar or breadcrumbs."

**Data consistency prompt**: "Ensure that data changes in one screen are reflected across all screens. For example, adding a transaction should update the dashboard totals and appear in the transaction history."

**State management prompt**: "Implement state management so that user preferences, filters, and current view are preserved when navigating between screens."

### Step 8: Add advanced features

Once the basic functionality is working, you can add more sophisticated features:

**Responsive design prompt**: "Make the app responsive so it works well on different screen sizes. Adjust layouts for mobile, tablet, and desktop views."

**Animations prompt**: "Add smooth transitions between screens and subtle animations for user interactions like button clicks and data updates."

**Export functionality prompt**: "Add the ability to export transaction data as CSV or PDF reports."

### Step 9: Test and refine

Testing is crucial for any app, even AI-generated ones:

**User testing prompt**: "Create a test scenario where a user adds a new transaction, views the monthly report, and exports their data. Ensure all flows work correctly."

**Error handling prompt**: "Add error handling for edge cases like empty data, network issues, or invalid user input."

**Performance optimization prompt**: "Optimize the app for performance, especially when handling large datasets or complex calculations."

## Best Practices for Figma Make

### 1. Start with Clear Requirements

Before diving into prompts, clearly define what you want to build:

- **User stories**: Write down what users should be able to do
- **Functional requirements**: List specific features and behaviors
- **Technical constraints**: Consider performance, compatibility, and scalability

### 2. Use Iterative Development

Build your app in small, manageable steps:

- **Start simple**: Begin with basic layouts and functionality
- **Add complexity gradually**: Build upon working features
- **Test frequently**: Verify each addition works before moving on

### 3. Write Effective Prompts

The quality of your prompts directly affects the output:

- **Be specific**: Include details about layout, styling, and behavior
- **Use clear language**: Avoid ambiguous terms and jargon
- **Provide context**: Reference existing elements and relationships
- **Iterate**: Refine prompts based on the results you get

### 4. Leverage Figma's Design System

Take advantage of Figma's built-in design capabilities:

- **Use components**: Create reusable UI elements
- **Apply styles**: Use consistent colors, typography, and spacing
- **Maintain consistency**: Ensure visual coherence across screens

### 5. Test Across Different Scenarios

Don't just test the happy path:

- **Edge cases**: Test with empty data, invalid inputs, and error conditions
- **User flows**: Walk through complete user journeys
- **Performance**: Test with realistic data volumes
- **Accessibility**: Ensure the app works for users with different needs

## Common Challenges and Solutions

### Challenge 1: Complex Data Relationships

**Problem**: Managing relationships between different data entities (transactions, categories, accounts).

**Solution**: Use clear data structures and implement proper state management. Break complex relationships into smaller, manageable pieces.

### Challenge 2: Performance with Large Datasets

**Problem**: The app becomes slow when handling many transactions.

**Solution**: Implement pagination, lazy loading, and efficient data filtering. Consider data virtualization for very large datasets.

### Challenge 3: Responsive Design

**Problem**: The app doesn't work well on different screen sizes.

**Solution**: Design with mobile-first approach and use flexible layouts. Test on various devices and screen sizes.

### Challenge 4: State Management

**Problem**: Data gets out of sync between different screens.

**Solution**: Implement a centralized state management system and ensure all components update consistently.

## Advanced Techniques

### 1. Custom Components

Create reusable components for common UI patterns:

**Prompt**: "Create a reusable transaction card component that displays date, amount, category, and description. Make it customizable for different transaction types."

### 2. Data Visualization

Add charts and graphs to make data more meaningful:

**Prompt**: "Create a pie chart showing spending by category and a line chart showing spending trends over time."

### 3. User Preferences

Allow users to customize their experience:

**Prompt**: "Add a settings screen where users can choose their preferred currency, date format, and default view."

### 4. Offline Functionality

Make the app work without an internet connection:

**Prompt**: "Implement local storage so users can add transactions offline and sync when they're back online."

## Conclusion

Figma Make represents a significant shift in how designers and developers can collaborate. By combining the visual design capabilities of Figma with AI-powered code generation, it opens up new possibilities for rapid prototyping and development.

The key to success with Figma Make is understanding that it's not just about generating code—it's about creating a seamless workflow between design and development. The better you can describe what you want, the better the results will be.

Remember that Figma Make is still evolving, and the quality of your prompts will improve with practice. Start with simple projects, experiment with different approaches, and gradually build up to more complex applications.

As you become more comfortable with Figma Make, you'll find that it can significantly speed up your development process while maintaining the quality and consistency of your designs. The ability to iterate quickly and see immediate results makes it an invaluable tool for modern app development.

Whether you're a designer looking to bring your ideas to life or a developer wanting to prototype quickly, Figma Make provides a powerful platform for building interactive applications with AI assistance.
