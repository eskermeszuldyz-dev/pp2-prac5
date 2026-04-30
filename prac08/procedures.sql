-- procedures.sql

-- 1. Upsert single contact
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name AND surname = p_surname) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook(name, surname, phone)
        VALUES(p_name, p_surname, p_phone);
    END IF;
END;
$$;

-- 2. Bulk insert with phone validation
CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    p_names VARCHAR[],
    p_surnames VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_entries TEXT := '';
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' THEN
            PERFORM upsert_contact(p_names[i], p_surnames[i], p_phones[i]);
        ELSE
            invalid_entries := invalid_entries || p_names[i] || ' ' || p_surnames[i] || ': ' || p_phones[i] || E'\n';
        END IF;
    END LOOP;

    IF invalid_entries <> '' THEN
        RAISE NOTICE 'Invalid phone entries:%', invalid_entries;
    END IF;
END;
$$;

-- 3. Delete contact by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(
    p_name VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSE
        RAISE EXCEPTION 'Provide either a name or a phone to delete a contact';
    END IF;
END;
$$;