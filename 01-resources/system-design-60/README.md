Days 1-10: System Design Foundations

1.	Introduction to System Design [a relative link](1_introduction.md)
	Overview of system design, why it's important, common challenges.

2.	Scalability Basics
	Vertical vs horizontal scaling, pros and cons.

3.	Latency and Throughput
	Definitions, differences, and techniques to optimize.

4.	CAP Theorem (Consistency, Availability, Partition Tolerance)
	Understanding the trade-offs in distributed systems.

5.	Load Balancing
	Types (Round-robin, Least Connections, Consistent Hashing), implementation.

6.	Sharding
	Database and cache sharding, partitioning strategies.

7.	Caching
	Techniques (Write-through, Write-back, Write-around), cache invalidation.

8.	Content Delivery Networks (CDN)
	How CDNs work, benefits for global systems.

9.	Proxies (Forward and Reverse)
	The role of proxies in system design, use cases.

10.	Rate Limiting
	Techniques to prevent system abuse and ensure fair usage.
_________________________________________________________________________________________

Days 11-20: Database Design & Storage Systems

11.	Relational Databases (SQL)
	Database design, normalization, ACID properties.

12.	NoSQL Databases
	Types (Key-Value, Document, Columnar, Graph), CAP trade-offs.

13.	Database Indexing
	Index types, performance impacts, B-trees, and Hash indexes.

14.	Database Replication
	Master-slave replication, leaderless replication, eventual consistency.

15.	Database Partitioning
	Horizontal, vertical partitioning, pros and cons.

16.	Data Warehousing
	OLAP vs OLTP, star schema, snowflake schema.

17.	Time Series Databases
	When to use them, specific use cases (e.g., monitoring, IoT).

18.	Distributed Databases (Cassandra, DynamoDB)
	Basics of distributed storage systems.

19.	Eventual Consistency
	Trade-offs and importance in distributed systems.

20.	Cold vs Hot Storage
	Use cases and considerations for data storage.
_________________________________________________________________________________

Days 21-30: Networking, APIs, and Communication

21.	Network Protocols (HTTP, HTTPS, TCP/IP)
	Differences, use cases in system design.

22.	WebSockets and Long Polling
	Real-time communication strategies.

23.	API Design (REST, GraphQL, gRPC)
	Differences, pros, and cons.

24.	API Gateway
	Role of API gateways in modern system architectures.

25.	Microservices Architecture
	What is it, advantages, disadvantages, best practices.

26.	Service Discovery
	DNS-based, client-side, and server-side discovery.

27.	Message Queues (Kafka, RabbitMQ, SQS)
	Asynchronous communication, benefits, and examples.

28.	Pub/Sub Systems
	How pub/sub models work in system design.

29.	Throttling and Backpressure
	Techniques to handle overload and maintain system stability.

30.	Circuit Breakers
	Prevent cascading failures, implementation strategies.
_________________________________________________________________________________

Days 31-40: Advanced System Design Patterns

31.	Event-Driven Architecture
	Designing systems with event-driven paradigms.

32.	Command Query Responsibility Segregation (CQRS)
	Separating read and write responsibilities for scalability.

33.	Event Sourcing
	Capturing system changes as events, implementation.

34.	Saga Pattern
	Managing distributed transactions in microservices.

35.	Distributed Systems Basics
	Fundamental principles of distributed systems.

36.	Consensus Algorithms (Paxos, Raft)
	Achieving consensus in distributed systems.

37.	Zookeeper
	Coordination service for distributed systems.

38.	Leader Election Algorithms
	How leader election works in distributed systems.

39.	Replication and Consistency Protocols
	Techniques for maintaining data consistency across replicas.

40.	Data Redundancy and Availability
	Ensuring high availability through redundancy.
________________________________________________________________________________

Days 41-50: Performance Optimization & Scaling

41.	Database Optimization Techniques
	Query optimization, caching results, denormalization.

42.	Distributed Caching (Redis, Memcached)
	Role of distributed caches in system design.

43.	Rate Limiting Techniques (Token Bucket, Leaky Bucket)
	Implementing rate limiting in distributed systems.

44.	Queuing Systems for Load Leveling
	How to manage system load using queues.

45.	Asynchronous Processing
	Using background jobs and workers for performance.

46.	Auto-Scaling
	Horizontal scaling using load-based triggers.

47.	Designing for High Availability
	Building systems with redundancy and fault tolerance.

48.	Failover Strategies
	Techniques to handle failures in distributed systems.

49.	Data Compression
	Lossy and lossless compression techniques.

50.	Log Aggregation and Distributed Tracing
	Tools and techniques for monitoring and debugging large systems.
_________________________________________________________________________

Days 51-60: Real-World System Designs & Case Studies

51.	Designing a URL Shortener
	Core components and scaling considerations.

52.	Designing a Social Media Feed (Instagram/Twitter)
	Managing posts, notifications, scalability.

53.	Designing a Chat System (WhatsApp/Slack)
	Real-time messaging, load handling, storage.

54.	Designing a Video Streaming Platform (YouTube/Netflix)
	Content delivery, scaling, latency optimization.

55.	Designing a Ride-Sharing App (Uber/Lyft)
	GPS tracking, matching algorithms, scaling.

56.	Designing an E-commerce System (Amazon)
	Product catalog, inventory management, checkout system.

57.	Designing a Notification System
	Push notifications, real-time alerts, scaling.

58.	Designing a Real-Time Analytics Platform
	Data pipelines, processing, performance optimization.

59.	Designing a Web Crawler (Google Search)
	Web scraping, index building, scaling crawlers.

60.	Designing a Global Distributed System
	Multi-region architecture, consistency, latency management.

