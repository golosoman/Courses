-- 1 Создание таблицы colors
CREATE TABLE IF NOT EXISTS colors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(50)
);

-- 2 Вставка значений в colors
INSERT INTO colors (color)
SELECT DISTINCT * FROM(
    SELECT DISTINCT
    color1 AS color
    FROM animals
    UNION ALL
    SELECT DISTINCT
        color2 AS color
    FROM animals
)
 WHERE color IS NOT NULL;

-- 3 Создание таблицы outcome
CREATE TABLE IF NOT EXISTS outcome(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subtype VARCHAR(50),
    "type" VARCHAR(50),
    "month" VARCHAR(50),
    "year" VARCHAR(50)
);

-- 4 Создание таблицы animal_type
CREATE TABLE animal_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_type VARCHAR(50)
);

-- 5 Вставка значений в animal_type
INSERT INTO animal_type(animal_type)
SELECT DISTINCT animal_type
FROM animals;

-- 6 Создание таблицы animal_breed
CREATE TABLE animal_breed(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed VARCHAR(50)
);

-- 7 Вставка значений в animal_breed
INSERT INTO animal_breed(breed)
SELECT DISTINCT breed
FROM animals;

-- 8 Создание таблицы animals_final
CREATE TABLE IF NOT EXISTS animals_final(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age_upon_outcome VARCHAR(50),
    animal_id VARCHAR(50),
    animal_type_id INTEGER,
    name VARCHAR(50),
    breed_id INTEGER,
    date_of_birth VARCHAR(50),
    outcome_id INTEGER,
    FOREIGN KEY (outcome_id) REFERENCES outcome(id),
    FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
    FOREIGN KEY (breed_id) REFERENCES animal_breed(id)
);

-- 9 Вставка значений в outcome
INSERT INTO outcome(subtype, "type", "month", "year")
SELECT DISTINCT
    animals.outcome_subtype,
    animals.outcome_type,
    animals.outcome_month,
    animals.outcome_year
FROM animals;

-- 10 Вставка значений в animals_final
INSERT INTO animals_final(
    age_upon_outcome,
    animal_id,
    animal_type_id,
    name,
    breed_id,
    date_of_birth,
    outcome_id)
SELECT
    animals.age_upon_outcome,
    animals.animal_id,
    animals.animal_type,
    animals.name,
    animals.breed,
    animals.date_of_birth,
    outcome.id
FROM animals
INNER JOIN outcome
    ON outcome.subtype = animals.outcome_subtype
    AND outcome."type" = animals.outcome_type
    AND outcome."month" = animals.outcome_month
    AND outcome."year" = animals.outcome_year;

-- 11 Создание таблицы animals_colors
CREATE TABLE IF NOT EXISTS animals_colors(
    animals_id INTEGER,
    colors_id INTEGER,
    FOREIGN KEY (animals_id) REFERENCES animals_final(id),
    FOREIGN KEY (colors_id) REFERENCES colors(id)
);

-- 12 Вставка значений в animals_colors
INSERT INTO animals_colors (animals_id, colors_id)
SELECT DISTINCT animals_final.id, colors.id
FROM animals
JOIN colors ON colors.color = animals.color1
JOIN animals_final ON animals_final.animal_id = animals.animal_id
UNION ALL
SELECT DISTINCT animals_final.id, colors.id
FROM animals
JOIN colors ON colors.color = animals.color2
JOIN animals_final ON animals_final.animal_id = animals.animal_id;