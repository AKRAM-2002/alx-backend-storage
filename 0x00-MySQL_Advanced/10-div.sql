-- Create function "SafeDiv"
-- Divides and returns the first by the second number

DELIMITER $$

-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv $$

-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
DETERMINISTIC
BEGIN

    	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END $$

DELIMITER ;

