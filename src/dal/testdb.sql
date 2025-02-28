DROP SCHEMA IF EXISTS test CASCADE;
CREATE SCHEMA test;

-- יצירת טבלת תפקידים
CREATE TABLE test.roles (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL CHECK (role_name IN ('admin', 'user'))
);

-- יצירת טבלת משתמשים
CREATE TABLE test.users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES test.roles(id) ON DELETE CASCADE
);

-- יצירת טבלת מדינות
CREATE TABLE test.countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(100) UNIQUE NOT NULL
);

-- יצירת טבלת חופשות
CREATE TABLE test.vacations (
    id SERIAL PRIMARY KEY,
    country_id INT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price DECIMAL(7,2) NOT NULL CHECK (price >= 0),
    image_file_name VARCHAR(255),
    CONSTRAINT fk_vacations_country FOREIGN KEY (country_id) REFERENCES test.countries(id) ON DELETE CASCADE
);

-- יצירת טבלת לייקים
CREATE TABLE test.likes (
    user_id INT NOT NULL,
    vacation_id INT NOT NULL,
    PRIMARY KEY (user_id, vacation_id),
    CONSTRAINT fk_likes_user FOREIGN KEY (user_id) REFERENCES test.users(id) ON DELETE CASCADE,
    CONSTRAINT fk_likes_vacation FOREIGN KEY (vacation_id) REFERENCES test.vacations(id) ON DELETE CASCADE
);

-- הכנסת נתונים לטבלת תפקידים
INSERT INTO test.roles (role_name) VALUES ('admin'), ('user');

-- הכנסת נתונים לטבלת משתמשים
INSERT INTO test.users (first_name, last_name, email, password, role_id) VALUES
    ('John', 'Doe', 'john.doe@example.com', 'password123', 1),
    ('Jane', 'Smith', 'jane.smith@example.com', 'password123', 2),
    ('Alice', 'Brown', 'alice.brown@example.com', 'password123', 2),
    ('Bob', 'Johnson', 'bob.johnson@example.com', 'password123', 2),
    ('Charlie', 'White', 'charlie.white@example.com', 'password123', 2),
    ('David', 'Miller', 'david.miller@example.com', 'password123', 2),
    ('Emma', 'Davis', 'emma.davis@example.com', 'password123', 2),
    ('Frank', 'Wilson', 'frank.wilson@example.com', 'password123', 2),
    ('Grace', 'Moore', 'grace.moore@example.com', 'password123', 2),
    ('Henry', 'Taylor', 'henry.taylor@example.com', 'password123', 2);

-- הכנסת נתונים לטבלת מדינות
INSERT INTO test.countries (country_name) VALUES
    ('USA'), ('Canada'), ('Mexico'), ('France'), ('Germany'),
    ('Italy'), ('Spain'), ('Japan'), ('China'), ('Australia');

-- הכנסת נתונים לטבלת חופשות
INSERT INTO test.vacations (country_id, description, start_date, end_date, price, image_file_name) VALUES
    (1, 'Beach vacation in Miami', '2025-06-01', '2025-06-10', 1500.00, 'miami.jpg'),
    (2, 'Skiing trip in Canada', '2025-12-15', '2025-12-25', 2000.00, 'canada_ski.jpg'),
    (3, 'Cultural trip in Mexico City', '2025-05-10', '2025-05-20', 1200.00, 'mexico.jpg'),
    (4, 'Romantic getaway in Paris', '2025-04-05', '2025-04-12', 2500.00, 'paris.jpg'),
    (5, 'Historical tour in Berlin', '2025-07-01', '2025-07-10', 1800.00, 'berlin.jpg'),
    (6, 'Wine tasting in Tuscany', '2025-09-15', '2025-09-25', 2200.00, 'tuscany.jpg'),
    (7, 'Beach relaxation in Barcelona', '2025-08-10', '2025-08-20', 1700.00, 'barcelona.jpg'),
    (8, 'Cherry blossom season in Tokyo', '2025-03-20', '2025-03-30', 3000.00, 'tokyo.jpg'),
    (9, 'Great Wall tour in China', '2025-10-01', '2025-10-10', 2500.00, 'greatwall.jpg'),
    (10, 'Surfing adventure in Australia', '2025-11-05', '2025-11-15', 2800.00, 'australia_surf.jpg'),
    (1, 'Road trip across California', '2025-06-15', '2025-07-01', 3500.00, 'california.jpg'),
    (2, 'Northern Lights tour in Canada', '2025-01-10', '2025-01-20', 2600.00, 'northern_lights.jpg'),
    (3, 'Diving in Cozumel', '2025-07-15', '2025-07-25', 2000.00, 'cozumel.jpg'),
    (4, 'Luxury shopping in Paris', '2025-05-01', '2025-05-07', 4000.00, 'paris_shopping.jpg'),
    (5, 'Castle tour in Bavaria', '2025-06-10', '2025-06-20', 3200.00, 'bavaria.jpg'),
    (6, 'Gondola ride in Venice', '2025-08-05', '2025-08-15', 2800.00, 'venice.jpg'),
    (7, 'Flamenco experience in Madrid', '2025-07-01', '2025-07-07', 1500.00, 'flamenco.jpg'),
    (8, 'Snowboarding in Hokkaido', '2025-12-01', '2025-12-10', 3300.00, 'hokkaido.jpg'),
    (9, 'Yangtze River Cruise', '2025-09-10', '2025-09-20', 2900.00, 'yangtze.jpg');
