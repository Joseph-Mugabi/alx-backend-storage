-- creates a stored procedure AddBonus 
-- that adds a new correction for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    -- check if the project already exists in the proj table
    SELECT id INTO project_id FROM projects WHERE name = project_name AND user_id = user_id LIMIT 1;
    -- IF PROJECT doesn't exist, create a new one
    if project_id IS NULL
    THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT id INTO project_id FROM projects WHERE name = project_name;
    END IF;
    -- insert the correction for the student
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;