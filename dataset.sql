create TABLE words(
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    pl_word text NOT NULL,
    en_word text NOT NULL,
    category text NOT NULL
);

SELECT * FROM words;

SELECT count(*) from words;

select  DISTINCT category from words;

select * from words where pl_word = 'None' or en_word = 'None';

update words set pl_word='sześcian liczby', en_word='cube of the number' where id = 52;

delete from words where id in (197, 198);

delete from words where id in (212, 213);

update words set pl_word='silnia', en_word='factorial' where id = 350;

update words set pl_word='silnia podwójna', en_word='double factorial' where id = 351;

update words set pl_word='silnia wielokrotna', en_word='multifactorial' where id = 352;

select * from words where category = 'Permutacje';

-- Duplicate delete
delete from words where id in (361, 365);

select category from words where id in (350,351,352);

select * from words where category = 'silnia';

delete from words where category = 'Silnia';

update words set pl_word='liczba możliwych permutacji z powtórzeniami ciągu n-elementowego' WHERE id = 378;

update words set pl_word='funkcja wykładnicza o podstawie e "exp(x)"', en_word='exponential function with base e "exp(e)"' WHERE id = 471;

delete from words where id = 516;

delete from words where id = 530;

update words set pl_word='współczynnik kierunkowy na podstawie jednego punktu leżącego na prostej (potrzebna jest znajomość wyrazu wolnego)', en_word='slope from one point lying on the line (free parameter is needed)' where id = 599;

delete from words where id = 604;