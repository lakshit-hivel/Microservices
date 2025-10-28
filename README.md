# Microservice Architecture 🌐

This repository showcases a microservice architecture implemented using Node.js, Java, and Python. Each microservice handles user authentication and management, demonstrating inter-service communication and independent deployment capabilities. This project aims to provide a practical example of building scalable and maintainable applications using a microservices approach.

## 🚀 Key Features

*   **User Authentication:** Secure registration and login functionalities using JWT (JSON Web Tokens).
*   **User Management:** Comprehensive CRUD (Create, Read, Update, Delete) operations for user data.
*   **Rate Limiting:** Protection against abuse with rate limiting middleware.
*   **Microservice Architecture:** Independent services for Node.js, Java, and Python.
*   **Database Integration:** Utilizes Prisma with PostgreSQL for Node.js, Spring Data JPA with PostgreSQL for Java, and SQLAlchemy with PostgreSQL for Python.
*   **CORS Configuration:** Enables Cross-Origin Resource Sharing for frontend integration.
*   **Authentication Middleware:** JWT-based authentication middleware to protect routes.
*   **Soft Delete:** Implements soft delete functionality for user records.

## 🛠️ Tech Stack

Here's a breakdown of the technologies used in each microservice:

**Node.js Microservice:**

*   **Backend:** Node.js, Express
*   **Database:** PostgreSQL (via Prisma)
*   **ORM:** Prisma
*   **Authentication:** JSON Web Tokens (JWT)
*   **Middleware:** CORS, Rate Limiter
*   **Environment Variables:** dotenv

**Java Microservice:**

*   **Backend:** Java, Spring Boot
*   **Database:** PostgreSQL (via Spring Data JPA)
*   **ORM:** Spring Data JPA, Hibernate
*   **Authentication:** JSON Web Tokens (JWT)
*   **Security:** Spring Security
*   **Build Tool:** Maven
*   **Logging:** SLF4J

**Python Microservice:**

*   **Backend:** Python, FastAPI
*   **Database:** PostgreSQL (via SQLAlchemy)
*   **ORM:** SQLAlchemy
*   **Authentication:** JSON Web Tokens (JWT)
*   **Middleware:** CORS, Rate Limiter
*   **Dependency Injection:** FastAPI's `Depends`
*   **Environment Variables:** dotenv

## 📦 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

*   **Node.js Microservice:**
    *   Node.js (>=14)
    *   npm or yarn
    *   PostgreSQL
    *   Prisma CLI (`npm install -g prisma`)

*   **Java Microservice:**
    *   Java Development Kit (JDK) (>=11)
    *   Maven
    *   PostgreSQL

*   **Python Microservice:**
    *   Python (>=3.8)
    *   pip
    *   PostgreSQL

### Installation

**Node.js Microservice:**

```bash
cd node-microservice
npm install # or yarn install
npm install -D prisma  # Install Prisma as a dev dependency
npx prisma generate   # Generate Prisma client
```

Create a `.env` file in the `node-microservice` directory and configure the `DATABASE_URL` environment variable.

```
DATABASE_URL="postgresql://user:password@host:port/database?schema=public"
JWT_SECRET="your-secret-key"
```

**Java Microservice:**

```bash
cd java-microservice
mvn clean install
```

Create an `application.properties` file in `java-microservice/src/main/resources` and configure the database connection details.

```properties
spring.datasource.url=jdbc:postgresql://your_db_host:5432/your_db_name?sslmode=require
spring.datasource.username=your_db_username
spring.datasource.password=your_db_password
spring.jpa.hibernate.ddl-auto=none
spring.jpa.hibernate.naming.physical-strategy=org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl
spring.jpa.show-sql=true
```

**Python Microservice:**

```bash
cd python-microservice
pip install -r requirements.txt
```

Create a `.env` file in the `python-microservice` directory and configure the `DATABASE_URL` environment variable.

```
DATABASE_URL="postgresql://user:password@host:port/database"
```

### Running Locally

**Node.js Microservice:**

```bash
cd node-microservice
npm run dev # or yarn dev
```

**Java Microservice:**

```bash
cd java-microservice
mvn spring-boot:run
```

**Python Microservice:**

```bash
cd python-microservice
python main.py
```

## 📂 Project Structure

```
├── node-microservice/
│   ├── src/
│   │   ├── app.ts
│   │   ├── routes/
│   │   │   ├── auth.ts
│   │   │   ├── userRoute.ts
│   │   ├── middlewares/
│   │   │   ├── auth.middleware.ts
│   │   ├── utils/
│   │   │   ├── prismaClient.ts
│   │   │   ├── rateLimiter.ts
│   ├── prisma/
│   │   ├── schema.prisma
│   ├── .env
│   ├── package.json
│   ├── tsconfig.json
├── java-microservice/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/javamicroservice/UserDirectoryJavaBackend/
│   │   │   │   │   ├── AuthUserController.java
│   │   │   │   │   ├── SecurityConfig.java
│   │   │   │   │   ├── UserController.java
│   │   │   │   │   ├── JwtAuthFilter.java
│   │   │   ├── resources/
│   │   │   │   ├── application.properties
│   ├── pom.xml
├── python-microservice/
│   ├── main.py
│   ├── authMiddleware.py
│   ├── database.py
│   ├── router/
│   │   ├── user.py
│   │   ├── auth.py
│   ├── models.py
│   ├── auth/
│   │   ├── jwt_handler.py
│   ├── requirements.txt
│   ├── .env
```


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

For questions or feedback, please contact: [Lakshit Agarwal] - [lakshit@hivel.ai]

## 💖 Thanks Message

Thank you for checking out this microservice architecture example! We hope it helps you in your development endeavors.

This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
