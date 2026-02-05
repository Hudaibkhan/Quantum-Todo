# Evolution Todo - Authentication, Database & UI Fixes

This project implements comprehensive fixes for critical authentication, database, and UI issues in the Evolution Todo application.

## Features Implemented

### 1. Authentication System
- **Secure Registration**: Added username field and confirm password validation
- **Login System**: Support for username or email login
- **JWT Token Management**: Secure token-based authentication
- **Session Persistence**: Proper session management using localStorage
- **Password Security**: Bcrypt hashing with secure storage

### 2. Database Integration
- **PostgreSQL Schema**: Neon PostgreSQL database with proper table structure
- **User Isolation**: All operations are user-specific with foreign key constraints
- **Alembic Migrations**: Automated database schema management
- **SQLModel ORM**: Type-safe database operations with validation

### 3. UI/UX Improvements
- **Password Input Component**: Secure password input with show/hide toggle
- **Enhanced Forms**: Improved signup and login forms with proper validation
- **Protected Routes**: Authentication middleware for route protection
- **Loading States**: Proper loading indicators and error handling

### 4. Security Features
- **Rate Limiting**: API rate limiting to prevent abuse
- **Input Validation**: Client and server-side validation
- **User Isolation**: Strict data isolation between users
- **Secure Storage**: Proper token storage and management

## Architecture

### Backend (FastAPI)
- **Models**: SQLModel entities for User, Task, and Session
- **API Routes**: `/auth` for authentication, `/tasks` for task management
- **Services**: Business logic in service layer
- **Utilities**: Password hashing, token management, validation utilities

### Frontend (Next.js)
- **Components**: Reusable components including PasswordInput and ProtectedRoute
- **Context**: AuthContext for global authentication state
- **API Integration**: Proxy routes for backend communication
- **Pages**: Protected task management page

## Database Schema
- **users**: Stores user information (id, username, email, password_hash, timestamps)
- **tasks**: Stores user tasks (id, title, description, completed, user_id, timestamps)
- **sessions**: Manages user sessions (id, user_id, token, expires_at, created_at)

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user

### Tasks
- `GET /api/tasks` - Get user's tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

## Security Measures
- Rate limiting on sensitive endpoints
- User-specific data isolation
- JWT token validation and expiration
- Password hashing with bcrypt
- Input sanitization and validation

## Installation & Setup

1. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Update with your database credentials
   ```

3. Run database migrations:
   ```bash
   python -m alembic upgrade head
   ```

4. Start the backend:
   ```bash
   uvicorn src.main:app --reload
   ```

5. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

6. Start the frontend:
   ```bash
   npm run dev
   ```

## Tech Stack

- **Frontend**: Next.js 15+ (App Router), TypeScript, TailwindCSS, Framer Motion
- **Backend**: FastAPI, SQLModel, PostgreSQL (Neon), Alembic
- **Auth**: JWT with HTTP-only cookies

## Testing
- Unit tests for authentication and task management
- Integration tests for API endpoints
- End-to-end tests for user flows

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET`: Secret key for JWT token signing
- `JWT_ALGORITHM`: Algorithm for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (default: 1440)
- `CORS_ORIGINS`: Comma-separated list of allowed origins
"# Quantum-Todo" 
