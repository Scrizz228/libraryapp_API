PGDMP                      }            library-database    17.2    17.2     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    74675    library-database    DATABASE     �   CREATE DATABASE "library-database" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
 "   DROP DATABASE "library-database";
                     postgres    false            �            1259    74834    books    TABLE     +  CREATE TABLE public.books (
    id integer NOT NULL,
    title character varying NOT NULL,
    author character varying NOT NULL,
    publication_year integer NOT NULL,
    isbn character varying NOT NULL,
    image_url character varying,
    available boolean DEFAULT true,
    description text
);
    DROP TABLE public.books;
       public         heap r       postgres    false            �            1259    74833    books_id_seq    SEQUENCE     �   CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.books_id_seq;
       public               postgres    false    220                       0    0    books_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;
          public               postgres    false    219            �            1259    74846    loans    TABLE     �   CREATE TABLE public.loans (
    id integer NOT NULL,
    book_id integer NOT NULL,
    user_id integer NOT NULL,
    issue_date date NOT NULL,
    return_date date
);
    DROP TABLE public.loans;
       public         heap r       postgres    false            �            1259    74845    loans_id_seq    SEQUENCE     �   CREATE SEQUENCE public.loans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.loans_id_seq;
       public               postgres    false    222                       0    0    loans_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.loans_id_seq OWNED BY public.loans.id;
          public               postgres    false    221            �            1259    74821    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying
);
    DROP TABLE public.users;
       public         heap r       postgres    false            �            1259    74820    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public               postgres    false    218                       0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public               postgres    false    217            b           2604    74837    books id    DEFAULT     d   ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);
 7   ALTER TABLE public.books ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219    220            d           2604    74849    loans id    DEFAULT     d   ALTER TABLE ONLY public.loans ALTER COLUMN id SET DEFAULT nextval('public.loans_id_seq'::regclass);
 7   ALTER TABLE public.loans ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    222    221    222            a           2604    74824    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218                      0    74834    books 
   TABLE DATA           m   COPY public.books (id, title, author, publication_year, isbn, image_url, available, description) FROM stdin;
    public               postgres    false    220   �                 0    74846    loans 
   TABLE DATA           N   COPY public.loans (id, book_id, user_id, issue_date, return_date) FROM stdin;
    public               postgres    false    222   �                 0    74821    users 
   TABLE DATA           E   COPY public.users (id, username, password, email, phone) FROM stdin;
    public               postgres    false    218                     0    0    books_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.books_id_seq', 2, true);
          public               postgres    false    219                       0    0    loans_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.loans_id_seq', 23, true);
          public               postgres    false    221                       0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 4, true);
          public               postgres    false    217            l           2606    74844    books books_isbn_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_isbn_key UNIQUE (isbn);
 >   ALTER TABLE ONLY public.books DROP CONSTRAINT books_isbn_key;
       public                 postgres    false    220            n           2606    74842    books books_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.books DROP CONSTRAINT books_pkey;
       public                 postgres    false    220            p           2606    74851    loans loans_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.loans
    ADD CONSTRAINT loans_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.loans DROP CONSTRAINT loans_pkey;
       public                 postgres    false    222            f           2606    74832    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public                 postgres    false    218            h           2606    74828    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    218            j           2606    74830    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public                 postgres    false    218               �   x���1n�0�ڜb.�Y����V��2ER��K#{69}��J�v���ײ����Hy<ٝ������kq	�e����-;�;uUl%:�S����c�G���)nͱF�u��4Ru�g�h4��������1>�n�K~���e�-P*���(��d��iq�>]�$�/I�V	i���t{�oB�Y�h��d�L����	�'L%�y��;����?`�            x������ � �         0   x�3�LL����44261��r3s�J9-,LLM�,�b���� ;N     