-- functions.sql

-- 1. Search contacts by pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern VARCHAR)
RETURNS TABLE(contact_name VARCHAR, contact_surname VARCHAR, contact_phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name AS contact_name,
           c.surname AS contact_surname,
           c.phone AS contact_phone
    FROM phonebook c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.surname ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Paginated query
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(contact_name VARCHAR, contact_surname VARCHAR, contact_phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.name AS contact_name,
           pb.surname AS contact_surname,
           pb.phone AS contact_phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;