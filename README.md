PROBLEM BEING SOLVED.
An inventory management system solves the challenge of efficiently tracking and managing inventory within a business or organization. It provides a centralized platform to monitor the movement, quantity, and status of various items or products in real-time. By automating processes such as stock tracking, order fulfillment, and reordering, it helps businesses optimize their inventory levels, reduce carrying costs, minimize stockouts, and improve overall operational efficiency. Additionally, it enables better decision-making by providing insights into inventory trends, demand forecasting, and supplier performance. Overall, an inventory management system streamlines operations, enhances inventory control, and contributes to better customer satisfaction through timely and accurate product availability.

HOW THE APPLICATION WORKS:
This inventory management application is designed to facilitate the efficient tracking and management of inventory within a business or organization. Here's how it works in detail:
1. User Interface: The application provides a graphical user interface (GUI) built using the Tkinter library in Python. It offers a user-friendly interface for interacting with the inventory management system.
2. Database Connectivity: The application connects to a MySQL database hosted locally, allowing it to store and retrieve inventory data. It uses the `MySQL. Connector` module to establish a connection and interact with the database.
3. Data Entry and Validation: Users can enter details of new items into the system, including the item name, price per kilogram, quantity in kilograms, supplier, and date of purchase. The application validates the input data to ensure completeness and correctness, including checking the format of the purchase date (YYYY-MM-DD).
4. Functionality:
   - Add Item: Users can add new items to the inventory by filling out the required fields and clicking the "Add Item" button. Upon successful addition, the item details are inserted into the database.
   - Update Item: Existing items can be updated by modifying their price, quantity, and supplier information. The application updates the corresponding database records accordingly.
   - View Inventory: Users can view the current inventory, displaying details such as item name, price, quantity, supplier, and purchase date. The information is fetched from the database and presented to the user in a pop-up window.
   - Delete Item: Items can be removed from the inventory by specifying their name. The application deletes the corresponding database records upon confirmation.
- Search Item: Items can be searched for from the inventory simply by entering their names in the search input
 - Print Inventory: The application provides the functionality to export the inventory data to a text file named "inventory.txt". It writes the item details, including name, price, quantity, supplier, and purchase date, to the file.

5. **Main Function**: The `main()` function initializes the Tkinter root window and creates an instance of the `InventoryApp` class, starting the GUI application. The application runs in a loop until the user exits the interface.

Overall, this inventory management application offers a comprehensive solution for businesses to effectively monitor, update, and maintain their inventory, enhancing operational efficiency and facilitating better decision-making.
