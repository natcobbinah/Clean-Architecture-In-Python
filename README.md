# Clean-Architecture-In-Python by ( Leonardo Giordani )
As coined by Robert Martin in his book Clean Architecture: A Craftsman’s Guide to Software Structure and Design, this sample codebase follows 
through the Development of a Rental Platform, using software design methodologies eg: TDD (Test-Driven Design), 
designing and implementing loosely coupled codebase using design patterns,
helping to improve testability, easy extensibility of codebase and interfacing with external-systems such as Web Frameworks (Flask), cli(Command Line Interface) 
programs etc.


## LAYERS OF CLEAN ARCHITECTURE
1. Entities - Represents the domain models, and what our system nees to interact with
2. Use-Cases - Implements Business-Rules, which are the core reason for the existence of the system itself
3. Gateways - Defines interfaces for external systems to interact with our application inwardly, or outwardly
4. External Systems - Defines components that implements interfaces defined in the Gateway Layer
