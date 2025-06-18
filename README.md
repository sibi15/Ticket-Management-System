# Ticket Management System
A command-line based ticketing system designed for parking lot management. This project simulates real-time ticket generation, duration tracking, and dynamic billing using Python and MySQL. It models the entry-exit flow in parking spaces and integrates a timer-based mechanism for fee computation. This system demonstrates database handling, time-based logic, and user interaction in Python—ideal for understanding how digital infrastructure can manage real-world parking scenarios.

Key Features:
- Random alphanumeric ticket ID generation using Python's random and string libraries
- Real-time parking duration tracking using time.perf_counter()
- MySQL database integration for dynamic data storage and update operations
- Custom recursive validation for ticket ID authentication
- Automatic cost calculation based on time spent in the parking lot
- Manual date input with SQL updates to simulate real-world timestamp recording
- Reset feature to clear and reinitialize ticket logs for fresh simulation
