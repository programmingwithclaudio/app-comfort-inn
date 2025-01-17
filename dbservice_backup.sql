PGDMP     7    3        
        |         	   dbservice    15.1 (Debian 15.1-1.pgdg110+1)    15.1 (Debian 15.1-1.pgdg110+1) l    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16581 	   dbservice    DATABASE     t   CREATE DATABASE dbservice WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE dbservice;
                postgres    false            {           1247    17159    account_type    TYPE     v   CREATE TYPE public.account_type AS ENUM (
    'ASSET',
    'LIABILITY',
    'EQUITY',
    'REVENUE',
    'EXPENSE'
);
    DROP TYPE public.account_type;
       public          postgres    false            u           1247    17087    booking_status    TYPE     _   CREATE TYPE public.booking_status AS ENUM (
    'PENDING',
    'CONFIRMED',
    'CANCELLED'
);
 !   DROP TYPE public.booking_status;
       public          postgres    false            �           1247    17177 	   flow_type    TYPE     F   CREATE TYPE public.flow_type AS ENUM (
    'INCOME',
    'EXPENSE'
);
    DROP TYPE public.flow_type;
       public          postgres    false            �           1247    17222    invoice_status    TYPE     X   CREATE TYPE public.invoice_status AS ENUM (
    'PENDING',
    'PAID',
    'OVERDUE'
);
 !   DROP TYPE public.invoice_status;
       public          postgres    false            i           1247    17008 
   prevention    TYPE     a   CREATE TYPE public.prevention AS ENUM (
    'No Preference',
    'Non Smoking',
    'Smoking'
);
    DROP TYPE public.prevention;
       public          postgres    false            f           1247    17000    reservation_type    TYPE     Z   CREATE TYPE public.reservation_type AS ENUM (
    'Single',
    'Double',
    'Deluxe'
);
 #   DROP TYPE public.reservation_type;
       public          postgres    false            �            1259    17170    account    TABLE     �   CREATE TABLE public.account (
    account_id integer NOT NULL,
    name character varying(100) NOT NULL,
    type public.account_type NOT NULL,
    balance double precision NOT NULL
);
    DROP TABLE public.account;
       public         heap    postgres    false    891            �            1259    17169    account_account_id_seq    SEQUENCE     �   CREATE SEQUENCE public.account_account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.account_account_id_seq;
       public          postgres    false    228            �           0    0    account_account_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.account_account_id_seq OWNED BY public.account.account_id;
          public          postgres    false    227            �            1259    16582    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    17198    bank    TABLE     �   CREATE TABLE public.bank (
    bank_id integer NOT NULL,
    name character varying(100) NOT NULL,
    account_id integer NOT NULL
);
    DROP TABLE public.bank;
       public         heap    postgres    false            �            1259    17197    bank_bank_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bank_bank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.bank_bank_id_seq;
       public          postgres    false    234            �           0    0    bank_bank_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.bank_bank_id_seq OWNED BY public.bank.bank_id;
          public          postgres    false    233            �            1259    17094    booking    TABLE     �   CREATE TABLE public.booking (
    id integer NOT NULL,
    cid integer NOT NULL,
    status public.booking_status,
    notes character varying(500)
);
    DROP TABLE public.booking;
       public         heap    postgres    false    885            �            1259    17093    booking_id_seq    SEQUENCE     �   CREATE SEQUENCE public.booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.booking_id_seq;
       public          postgres    false    226            �           0    0    booking_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.booking_id_seq OWNED BY public.booking.id;
          public          postgres    false    225            �            1259    17182    cashflow    TABLE     �   CREATE TABLE public.cashflow (
    flow_id integer NOT NULL,
    date date NOT NULL,
    type public.flow_type NOT NULL,
    amount double precision NOT NULL,
    description character varying(500),
    account_id integer NOT NULL
);
    DROP TABLE public.cashflow;
       public         heap    postgres    false    897            �            1259    17181    cashflow_flow_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cashflow_flow_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.cashflow_flow_id_seq;
       public          postgres    false    230            �           0    0    cashflow_flow_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.cashflow_flow_id_seq OWNED BY public.cashflow.flow_id;
          public          postgres    false    229            �            1259    17054 	   complaint    TABLE     �   CREATE TABLE public.complaint (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    email character varying(120) NOT NULL,
    phone character varying(20) NOT NULL,
    complaints_details text NOT NULL
);
    DROP TABLE public.complaint;
       public         heap    postgres    false            �            1259    17053    complaint_id_seq    SEQUENCE     �   CREATE SEQUENCE public.complaint_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.complaint_id_seq;
       public          postgres    false    222            �           0    0    complaint_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.complaint_id_seq OWNED BY public.complaint.id;
          public          postgres    false    221            �            1259    17074    customer    TABLE     �   CREATE TABLE public.customer (
    cid integer NOT NULL,
    identifier character varying(20) NOT NULL,
    fullname character varying(100) NOT NULL,
    email character varying(50) NOT NULL,
    phone character varying(25)
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    17073    customer_cid_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_cid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.customer_cid_seq;
       public          postgres    false    224            �           0    0    customer_cid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.customer_cid_seq OWNED BY public.customer.cid;
          public          postgres    false    223            �            1259    17230    invoice    TABLE     0  CREATE TABLE public.invoice (
    invoice_id integer NOT NULL,
    booking_id integer NOT NULL,
    issue_date date NOT NULL,
    due_date date NOT NULL,
    subtotal double precision NOT NULL,
    taxes double precision NOT NULL,
    total double precision NOT NULL,
    status public.invoice_status
);
    DROP TABLE public.invoice;
       public         heap    postgres    false    912            �            1259    17229    invoice_invoice_id_seq    SEQUENCE     �   CREATE SEQUENCE public.invoice_invoice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.invoice_invoice_id_seq;
       public          postgres    false    238            �           0    0    invoice_invoice_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.invoice_invoice_id_seq OWNED BY public.invoice.invoice_id;
          public          postgres    false    237            �            1259    16988    pricing    TABLE     �   CREATE TABLE public.pricing (
    pricing_id integer NOT NULL,
    booking_id integer NOT NULL,
    nights integer NOT NULL,
    total_price double precision NOT NULL,
    booked_date date NOT NULL
);
    DROP TABLE public.pricing;
       public         heap    postgres    false            �            1259    16987    pricing_pricing_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pricing_pricing_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.pricing_pricing_id_seq;
       public          postgres    false    218            �           0    0    pricing_pricing_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.pricing_pricing_id_seq OWNED BY public.pricing.pricing_id;
          public          postgres    false    217            �            1259    17016    reservation    TABLE     �  CREATE TABLE public.reservation (
    id integer NOT NULL,
    booking_id integer NOT NULL,
    start timestamp without time zone NOT NULL,
    "end" timestamp without time zone NOT NULL,
    type public.reservation_type,
    requirement public.prevention,
    adults integer NOT NULL,
    children integer,
    requests character varying(500),
    "timestamp" timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    hash character varying(100)
);
    DROP TABLE public.reservation;
       public         heap    postgres    false    870    873            �            1259    17015    reservation_id_seq    SEQUENCE     �   CREATE SEQUENCE public.reservation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.reservation_id_seq;
       public          postgres    false    220            �           0    0    reservation_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.reservation_id_seq OWNED BY public.reservation.id;
          public          postgres    false    219            �            1259    17191    supplier    TABLE     �   CREATE TABLE public.supplier (
    supplier_id integer NOT NULL,
    contact character varying(50) NOT NULL,
    address character varying(200),
    identifier character varying(20) NOT NULL,
    fullname character varying(100) NOT NULL
);
    DROP TABLE public.supplier;
       public         heap    postgres    false            �            1259    17190    supplier_supplier_id_seq    SEQUENCE     �   CREATE SEQUENCE public.supplier_supplier_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.supplier_supplier_id_seq;
       public          postgres    false    232            �           0    0    supplier_supplier_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.supplier_supplier_id_seq OWNED BY public.supplier.supplier_id;
          public          postgres    false    231            �            1259    17210    supply    TABLE     �   CREATE TABLE public.supply (
    supply_id integer NOT NULL,
    supplier_id integer NOT NULL,
    item character varying(100) NOT NULL,
    quantity integer NOT NULL,
    cost double precision NOT NULL,
    date date NOT NULL
);
    DROP TABLE public.supply;
       public         heap    postgres    false            �            1259    17209    supply_supply_id_seq    SEQUENCE     �   CREATE SEQUENCE public.supply_supply_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.supply_supply_id_seq;
       public          postgres    false    236            �           0    0    supply_supply_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.supply_supply_id_seq OWNED BY public.supply.supply_id;
          public          postgres    false    235            �            1259    16957 
   user_login    TABLE     9  CREATE TABLE public.user_login (
    id integer NOT NULL,
    firstname character varying(64) NOT NULL,
    lastname character varying(64) NOT NULL,
    email character varying(32) NOT NULL,
    password character varying(256) NOT NULL,
    phone character varying(25),
    role character varying(10) NOT NULL
);
    DROP TABLE public.user_login;
       public         heap    postgres    false            �            1259    16956    user_login_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_login_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.user_login_id_seq;
       public          postgres    false    216            �           0    0    user_login_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.user_login_id_seq OWNED BY public.user_login.id;
          public          postgres    false    215            �           2604    17173    account account_id    DEFAULT     x   ALTER TABLE ONLY public.account ALTER COLUMN account_id SET DEFAULT nextval('public.account_account_id_seq'::regclass);
 A   ALTER TABLE public.account ALTER COLUMN account_id DROP DEFAULT;
       public          postgres    false    227    228    228            �           2604    17201    bank bank_id    DEFAULT     l   ALTER TABLE ONLY public.bank ALTER COLUMN bank_id SET DEFAULT nextval('public.bank_bank_id_seq'::regclass);
 ;   ALTER TABLE public.bank ALTER COLUMN bank_id DROP DEFAULT;
       public          postgres    false    233    234    234            �           2604    17097 
   booking id    DEFAULT     h   ALTER TABLE ONLY public.booking ALTER COLUMN id SET DEFAULT nextval('public.booking_id_seq'::regclass);
 9   ALTER TABLE public.booking ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    17185    cashflow flow_id    DEFAULT     t   ALTER TABLE ONLY public.cashflow ALTER COLUMN flow_id SET DEFAULT nextval('public.cashflow_flow_id_seq'::regclass);
 ?   ALTER TABLE public.cashflow ALTER COLUMN flow_id DROP DEFAULT;
       public          postgres    false    229    230    230            �           2604    17057    complaint id    DEFAULT     l   ALTER TABLE ONLY public.complaint ALTER COLUMN id SET DEFAULT nextval('public.complaint_id_seq'::regclass);
 ;   ALTER TABLE public.complaint ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            �           2604    17077    customer cid    DEFAULT     l   ALTER TABLE ONLY public.customer ALTER COLUMN cid SET DEFAULT nextval('public.customer_cid_seq'::regclass);
 ;   ALTER TABLE public.customer ALTER COLUMN cid DROP DEFAULT;
       public          postgres    false    224    223    224            �           2604    17233    invoice invoice_id    DEFAULT     x   ALTER TABLE ONLY public.invoice ALTER COLUMN invoice_id SET DEFAULT nextval('public.invoice_invoice_id_seq'::regclass);
 A   ALTER TABLE public.invoice ALTER COLUMN invoice_id DROP DEFAULT;
       public          postgres    false    238    237    238            �           2604    16991    pricing pricing_id    DEFAULT     x   ALTER TABLE ONLY public.pricing ALTER COLUMN pricing_id SET DEFAULT nextval('public.pricing_pricing_id_seq'::regclass);
 A   ALTER TABLE public.pricing ALTER COLUMN pricing_id DROP DEFAULT;
       public          postgres    false    217    218    218            �           2604    17019    reservation id    DEFAULT     p   ALTER TABLE ONLY public.reservation ALTER COLUMN id SET DEFAULT nextval('public.reservation_id_seq'::regclass);
 =   ALTER TABLE public.reservation ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    17194    supplier supplier_id    DEFAULT     |   ALTER TABLE ONLY public.supplier ALTER COLUMN supplier_id SET DEFAULT nextval('public.supplier_supplier_id_seq'::regclass);
 C   ALTER TABLE public.supplier ALTER COLUMN supplier_id DROP DEFAULT;
       public          postgres    false    232    231    232            �           2604    17213    supply supply_id    DEFAULT     t   ALTER TABLE ONLY public.supply ALTER COLUMN supply_id SET DEFAULT nextval('public.supply_supply_id_seq'::regclass);
 ?   ALTER TABLE public.supply ALTER COLUMN supply_id DROP DEFAULT;
       public          postgres    false    235    236    236            �           2604    16960    user_login id    DEFAULT     n   ALTER TABLE ONLY public.user_login ALTER COLUMN id SET DEFAULT nextval('public.user_login_id_seq'::regclass);
 <   ALTER TABLE public.user_login ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �          0    17170    account 
   TABLE DATA           B   COPY public.account (account_id, name, type, balance) FROM stdin;
    public          postgres    false    228   �|       y          0    16582    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    214   �|       �          0    17198    bank 
   TABLE DATA           9   COPY public.bank (bank_id, name, account_id) FROM stdin;
    public          postgres    false    234   }       �          0    17094    booking 
   TABLE DATA           9   COPY public.booking (id, cid, status, notes) FROM stdin;
    public          postgres    false    226   :}       �          0    17182    cashflow 
   TABLE DATA           X   COPY public.cashflow (flow_id, date, type, amount, description, account_id) FROM stdin;
    public          postgres    false    230   �~       �          0    17054 	   complaint 
   TABLE DATA           O   COPY public.complaint (id, name, email, phone, complaints_details) FROM stdin;
    public          postgres    false    222   �~       �          0    17074    customer 
   TABLE DATA           K   COPY public.customer (cid, identifier, fullname, email, phone) FROM stdin;
    public          postgres    false    224   �~       �          0    17230    invoice 
   TABLE DATA           o   COPY public.invoice (invoice_id, booking_id, issue_date, due_date, subtotal, taxes, total, status) FROM stdin;
    public          postgres    false    238   
      }          0    16988    pricing 
   TABLE DATA           [   COPY public.pricing (pricing_id, booking_id, nights, total_price, booked_date) FROM stdin;
    public          postgres    false    218   
                0    17016    reservation 
   TABLE DATA           �   COPY public.reservation (id, booking_id, start, "end", type, requirement, adults, children, requests, "timestamp", hash) FROM stdin;
    public          postgres    false    220   �
      �          0    17191    supplier 
   TABLE DATA           W   COPY public.supplier (supplier_id, contact, address, identifier, fullname) FROM stdin;
    public          postgres    false    232   �      �          0    17210    supply 
   TABLE DATA           T   COPY public.supply (supply_id, supplier_id, item, quantity, cost, date) FROM stdin;
    public          postgres    false    236   �      {          0    16957 
   user_login 
   TABLE DATA           [   COPY public.user_login (id, firstname, lastname, email, password, phone, role) FROM stdin;
    public          postgres    false    216         �           0    0    account_account_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.account_account_id_seq', 1, false);
          public          postgres    false    227            �           0    0    bank_bank_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.bank_bank_id_seq', 1, false);
          public          postgres    false    233            �           0    0    booking_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.booking_id_seq', 54, true);
          public          postgres    false    225            �           0    0    cashflow_flow_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.cashflow_flow_id_seq', 1, false);
          public          postgres    false    229            �           0    0    complaint_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.complaint_id_seq', 1, false);
          public          postgres    false    221            �           0    0    customer_cid_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.customer_cid_seq', 1002, true);
          public          postgres    false    223            �           0    0    invoice_invoice_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.invoice_invoice_id_seq', 1, false);
          public          postgres    false    237            �           0    0    pricing_pricing_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.pricing_pricing_id_seq', 20, true);
          public          postgres    false    217            �           0    0    reservation_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.reservation_id_seq', 34, true);
          public          postgres    false    219            �           0    0    supplier_supplier_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.supplier_supplier_id_seq', 1, false);
          public          postgres    false    231            �           0    0    supply_supply_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.supply_supply_id_seq', 1, false);
          public          postgres    false    235            �           0    0    user_login_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.user_login_id_seq', 5, true);
          public          postgres    false    215            �           2606    17175    account account_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (account_id);
 >   ALTER TABLE ONLY public.account DROP CONSTRAINT account_pkey;
       public            postgres    false    228            �           2606    16586 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    214            �           2606    17203    bank bank_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.bank
    ADD CONSTRAINT bank_pkey PRIMARY KEY (bank_id);
 8   ALTER TABLE ONLY public.bank DROP CONSTRAINT bank_pkey;
       public            postgres    false    234            �           2606    17101    booking booking_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.booking DROP CONSTRAINT booking_pkey;
       public            postgres    false    226            �           2606    17189    cashflow cashflow_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.cashflow
    ADD CONSTRAINT cashflow_pkey PRIMARY KEY (flow_id);
 @   ALTER TABLE ONLY public.cashflow DROP CONSTRAINT cashflow_pkey;
       public            postgres    false    230            �           2606    17061    complaint complaint_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.complaint
    ADD CONSTRAINT complaint_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.complaint DROP CONSTRAINT complaint_pkey;
       public            postgres    false    222            �           2606    17122    customer customer_email_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_email_key UNIQUE (email);
 E   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_email_key;
       public            postgres    false    224            �           2606    17108     customer customer_identifier_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_identifier_key UNIQUE (identifier);
 J   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_identifier_key;
       public            postgres    false    224            �           2606    17079    customer customer_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cid);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    224            �           2606    17235    invoice invoice_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (invoice_id);
 >   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_pkey;
       public            postgres    false    238            �           2606    16993    pricing pricing_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.pricing
    ADD CONSTRAINT pricing_pkey PRIMARY KEY (pricing_id);
 >   ALTER TABLE ONLY public.pricing DROP CONSTRAINT pricing_pkey;
       public            postgres    false    218            �           2606    17024    reservation reservation_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.reservation DROP CONSTRAINT reservation_pkey;
       public            postgres    false    220            �           2606    17247     supplier supplier_identifier_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_identifier_key UNIQUE (identifier);
 J   ALTER TABLE ONLY public.supplier DROP CONSTRAINT supplier_identifier_key;
       public            postgres    false    232            �           2606    17196    supplier supplier_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (supplier_id);
 @   ALTER TABLE ONLY public.supplier DROP CONSTRAINT supplier_pkey;
       public            postgres    false    232            �           2606    17215    supply supply_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.supply
    ADD CONSTRAINT supply_pkey PRIMARY KEY (supply_id);
 <   ALTER TABLE ONLY public.supply DROP CONSTRAINT supply_pkey;
       public            postgres    false    236            �           2606    16964    user_login user_login_email_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_email_key UNIQUE (email);
 I   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_email_key;
       public            postgres    false    216            �           2606    16962    user_login user_login_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_pkey;
       public            postgres    false    216            �           2606    17204    bank bank_account_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bank
    ADD CONSTRAINT bank_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.account(account_id);
 C   ALTER TABLE ONLY public.bank DROP CONSTRAINT bank_account_id_fkey;
       public          postgres    false    234    228    3287            �           2606    17102    booking booking_cid_fkey    FK CONSTRAINT     w   ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_cid_fkey FOREIGN KEY (cid) REFERENCES public.customer(cid);
 B   ALTER TABLE ONLY public.booking DROP CONSTRAINT booking_cid_fkey;
       public          postgres    false    3283    226    224            �           2606    17241 !   cashflow cashflow_account_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cashflow
    ADD CONSTRAINT cashflow_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.account(account_id);
 K   ALTER TABLE ONLY public.cashflow DROP CONSTRAINT cashflow_account_id_fkey;
       public          postgres    false    3287    228    230            �           2606    17236    invoice invoice_booking_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_booking_id_fkey FOREIGN KEY (booking_id) REFERENCES public.booking(id);
 I   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_booking_id_fkey;
       public          postgres    false    226    3285    238            �           2606    17129    pricing pricing_booking_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.pricing
    ADD CONSTRAINT pricing_booking_id_fkey FOREIGN KEY (booking_id) REFERENCES public.booking(id);
 I   ALTER TABLE ONLY public.pricing DROP CONSTRAINT pricing_booking_id_fkey;
       public          postgres    false    218    3285    226            �           2606    17134 '   reservation reservation_booking_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_booking_id_fkey FOREIGN KEY (booking_id) REFERENCES public.booking(id);
 Q   ALTER TABLE ONLY public.reservation DROP CONSTRAINT reservation_booking_id_fkey;
       public          postgres    false    226    220    3285            �           2606    17216    supply supply_supplier_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.supply
    ADD CONSTRAINT supply_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES public.supplier(supplier_id);
 H   ALTER TABLE ONLY public.supply DROP CONSTRAINT supply_supplier_id_fkey;
       public          postgres    false    236    3293    232            �      x������ � �      y      x�331N53LJM2L3����� +�      �      x������ � �      �   F  x�m�AN�0E�ߧ�	P<3'K�T�ĚMU"T��Ώ�E��o���?IBh��������v�~�q��k���������렳G\<�4n��xt��4L��;;����R�����BqZ�T�ſ��V ������a�� ��u挀�J�`���ڔ�lΔ�Š\Y����.q� ��zK������t&��b��rȾ����|����}��gQ�,i�s��U��a7�ٕh�TWĕ�֌g�%���J<5�I��DP�҅��@�q��d�E2���LBi���tH�>6H�>$c	��G������1���9��Z�i      �      x������ � �      �      x������ � �      �      x�l}ɖ�J��8���(��73����N���{Ϊ����M�ʯ{#(e�ֽdUIb� 6����Ȼr�+'�V�v����6�~P��Ev���
=Φ}U�
}�*I�$�ݍ�<߹����]���~�����8�j�V����?��U�'��W����(�?M��q޾��?�c)���}���G�U�W~�{�@%�sEWQ�;�i����7�Ѩ�]%?���n(��8L�\׽�</ل*r�+/��R/Vo�e:mo��lzUN��4c�;ɇ�лrq���8�H�Nz�W����R��Y��3�f�e�U
�C=�C�{3��DAt�{�U��&V~�^���:�z��4��aig=�jW�R��7�9�Fp�5�~m$�U^EA��G۷�n��j,e����)��U�|e�&Uq���^�a���c���k=L?�Q5�YL�7����~�+Hq�:��u�f�+��D��>������K3���5��q8����EBq��*�t�*ҫ��J�E�ݾk[|�4\4�|��J�[��A	p�Qn\O�n|�G�xA���~��lߏ��CL��MSه���U�O=��U�W�����C���͌g����[Ƴ��R#<�4q6n�����*�G}i�ߛb?6m���*��n���i֯��RQ��Ǣ�$t�������N\�ǥjD�?����lJUWg�d�_Uý
�Ub;��)��/HW]x۸�>�Q�����`�h�.�û�$ٸ�����7�����?��N�j�W�ʎ���-�Ix��$���q	n|���n��ø�،SQ㓽��\gw�~�Ł�kH�<'p7.�0�D	t��� ����pi��_����Q����d�Q	~8������?V�\�j���rZ���^��px��*���Z=m�{l�RŸJ�l��f^Fc�->����V�σ��Ɓʇ��~h��w��KY۬�˟���9�z<�h���y�z�Wp�7��uÇVp�\7�bo<t�?�̈́��x��p�<i◗���{3���'�F��E��࿞W��>�m�x�/T^=q����a�~hKl��ow`�!���g	���&�Ƌ�4"�N�MS�}�l?,f�A�X��!;.�aX�ʞ�ia�n��}|U����?�	�~����������ȷ��F���n�D��s�'���KW�ͯ��g؊1�2fŨ�j���e�%�4)}���K��y���O}6��gg�dNj��:eE>��h�Z�x�0���]��U����x�۷����R�9f�z��*6���w}��s�?�9~��nZ~|��d���f��7_�@��x����q��xx���Ƚ�zgz�oe��~����=���9���}������b��?�&f�:g}�:�Ǭ���Δ��M"�<�4�z��8||. ��}?6���pt�1j�`��YC��I���ˍ���$�7~�}PmR/��Z&h*]��&�YOYa�����r�P!R�����a�^�]3�\���cvJ�O�z��*�k�B������� �����d��aNꮴ��d�d/"���9`�p	$n���|�	��s(�5�.��٠���}��o�`���?�?�tཨ�x~���F�h�w����������J�;�B���	.'��z8.v�?0s�-���E]��"�~��L_YϏ]t�nW��E^�t�lo�̪ÿn��頭��Ķ�3KR���\�N�W�5�|X�� �؝E7̦�h�Q&�nX�����Y[�-����B��~6݄ݰ���FY�.��3p
��at�d�����9�flF���^S�AM���ƙ^Jq�|)~�����X("��<i�b�~���5�
 p;�j�Ϣ�d�������2)?�¼�~�l�{.�/���]>S�����ؘ���P���cM�j���L\��U@`
�G�z36USj��/�����l�j�è�ƢA����q�f<&��>$,��5�O�zs���t��E��1�^j��a��h(����H���V���- ��byx�0a8L�QB�%a����6�#���v��4�_��O�Z�MC�0� 8u6؉Dq�!�����cɗ��QV�dMDp�W�R��'�5�f ���{XַKQ�]�uߗg��eE=��M��"(�9rcw���L��@G��.���fi�ᤦNV��VD�x�Y%��G��x�1���� �{��w]�F,mq8�n�GX@�b.��!���%�f��x ��yh��4��t��&;1f�M�r!A/#��sB$N�U�������j�S�ܻ�Z	<W�Kl�tLH\RE�T]�#�j��"��eu�x-�3��Q�� �ݦ!L�5�����	���3�Gl3�����܌ò�>7�k�#�񯈞b|���o?i<�I�w���KB��8�����n
��ؙ	B-�ia�H�e�aVw�*�=j�/��v�@�az�b���>��01FC�1,#7Gq��!;���7��Fʋ6MgJ��㩟�<Lp�M�1����l^�y(�A����&&	R|�����&��X�q��˴�eue��QP��8q�D'$���׈8�Iƥ��.��
.�Ӫ�Xg]�țQT3���D�����)�ħ�o��G���j.l/FE�*�؊�;!����G_��@ 7��Ϲ� R���*`pa ��>e����v�6��_agp꾷�� x�:Cq�	��� ����� ��8���p<qK岺�4�=���L�7��ÃC��Ⱥ
;a�J��Pye���M-�!�uMhQ�t;*�~�p�W��2�A�����ΊS.h�;�g�B�"�'X�M�"��h�w�`�r�_�܊�?��{B�0`�����=q7��]F�����[n���E���NV��_^fB=�Y���������9��P��no�"� EQ��9�@�� ��> ��B�'���<�~s��h�?�G���Fn���A�.�7>��� ��!A���)a�q�q�</;Nw��KagCC���0��4~д��0)#�v5���#&I��cp_A�h����	@C�	�{�n�m����W�����cS%q����V7��~�7����nf�L�*z!|�}����S�o��H=�������f�q)U�Y��^�XD` v�p�0�#��s 	�6#�ԏ!oZ\��Wɋ�jD(?k�Q��"��l��1<1"M?Ņ�m5��?��B7���d���3��ȧh��S�f6	�s!��;\�=�����gV���^����6(C\wTI��pC�ۿ���T�5���;Y=����^|�Um�k=nw\�&�\�Лq.B��UL��'5"\�E���P5 �	�`Bܓ�bF�5i|�/�Q����y��%�G� ��F��9)�=�c�u�K oUV�+��# l��LD	4YRP��^����<�����X�����	l&Ԃf�s��������~]o�-]/�M����؍6I*��H��T��~��c��ԟ�*y���!����`z1uӥ���Wo5��b��-�q$�(�U�j83^�Z�8�:���d�"'2��9ѓ���F�"y��̏'0�gv3��%0�̋��D}G�e��-|�Q���w�]� qB8q/�7�x�>z�Slo��_o�/���2���� �{a�]����'^2ӪK��Ci������0R``/@sX�4��bF�?^�����T�;�L��uP'�Al�n2v��&�����e���Jt�zUM4��^�MM/��WE�<D�t`���4��0#��7���1�6�zCv4y?���/7%a���C�3��om$@uR� \���y(�iM:C#b�z*�8@��AI�T��=հW��
�/�;C��� �����a�qLZK|C���WL~������ّy��L���$��+p�fX
`��oxD-�@KY�)[zIcyt�xީ'�������UG�-���cW�ZVo�z}�� ��O0�����5C���݉/�.    q�]}�%+�}�䫍���Kx�����@b�y�ʹ ȥ�*x�U�^"*���X���	�$1#�7˸d��*�W�;f9�+ޅl+`���,?D@ �W�&}�7"�:�%�ŧY�������f�I�I�Ø��|/d_6L�oo�8a�IV�Ѽ���A�lZ _�(N�i��F��7��Ш�\V�!�u��4�����kH�|?)���&��h����M_�~���0��O�#:B�`k� ė �0���}�m���-�@�WU)��f }��m�/��$�9цe�����1K8Ȍ��z�=z7Y��2�;���P��Z�`�aӲ������7�d��NV���G��t�����#�&�� �_ +���'|L��*�A�0?+H��f��`���Q1�	5��ۓ��r�	Fko��̇��ΐ�7��I�),���`#ֽ�u7,%L�)��Z+�Q�j �]g�!������MLW�r���Șe��?o���	��R?�[��0q��@��-!F`��I�m�سzQ��'Y#:7�n�A�M����h�k��Sìҗ��]wbhL����[%?�$S�a4�W�3����@\�Q�̧�D2�e-��������q $������ �;oƖ1�l����0B�=��0/�Y8d!'��
�}����7P�^Z�� �4%����|f�}N��
`J	�aҘ�� ��iv��ƴ��_b�w�U��T"�0;��>�D
!���@�}?�Sy�U�V�7ٱ^����}�i��»�.�w���yY����Y��G��.i0��.l���0I�3CϏ�5��ر���E�ů^VH��*���H2`	s>��� ��&�����q���$�CnV��B�R��F�R܁~#�J}����i���.�eRU%��d��W��|:�|Y��Î".am	 K}�l�~�g��V��i:�� 8ۇ��S���
�=�a�ջ��l�1��QV��f>c�X���7a�ϳ� �e8�sm�,�yٌ��f������TA��Sq���.(�������PȲ4#���
~��aE��M@��ȠϾg˄dU�>���_LU,����L�M�k���g5�g]1e���4�������[�^֦����g����2B	L`v���'i��m`���,���2D��j�=�!б@qFT��OF�F_/%����sq��_�RL"��6�lt���O+�����!�,ȏ`����{ �a-�%��(
i�`1}XL|��r���H���2M�g�۟��@ R��͚��J`B��D�P�������=<"�F��
��$�C ��Q�\%=c� �����]���
��5�Z���!�H<� �f�jZ���b�r�퓿��K0F��S�� ��Xon��6~���a'ţb:��1k��ۛ�nQ� �!2�"���/`����]VV��s��"*������/$�a�W��� ����̓����,��L��<���fvY���,�s��Wx����)��IVU��������/��	���-,�/w*7fU��B|�G���aI�f.	&>3�	� ��aY�:���D\�~OK��7���` ��L�m�2C��|8{�I$�ў�m��R���\�9�᫠�\���- 	��*��O��O�w�>/� ���Z�pfص�rETuր�c�QJ�~7���=��ӽ	���M|&cI��I����O$ЍaĮJg�< �VO� �GK��ZX����d'�	]a�1Tg=��^csr��
A$y�34#�	Ĳ^�K�$��7l���dn��J�{�U
��-�A�	��^F@��P���
LuS���o"�I<P�-l')�gU3��PE�gߓ��n't�3ߙ�~��JA���R���
��,�@ B���} M�����ߖvi*+:������DPK �-En_�P�wG���;fJe��A�u'D�y,��@��_F4a�~.�����
A!���DP��"��!|80+�� 7��T}��8d�V�,_&�!���~��<fY�5)�&�:yv	�����/na1N�.X��Y��q����~�M����q�ze &'�ԗ��`��ն�����P	m=� |�=o	 �6�2,�b_i�ړ�wV*@����k��#,�/&ؔ@R�R�K}?���)w�uV53��f��<������g��G�	�PsO��c7+�M6�!��%�Cg$t��1�6�Kbk��"�LK����e؜s��q P�8B�V���9�٘�a�̓�U
��N�Ecu�����AIY����TMt�Tx������u%�N8	�(������徚�6�Iս��{l����.�S����?�������Ǟ��-,@u�5�~:�)�r���2=A�u
l$�\ ���]n�`���Ɛ�OZ� �GLAz�	���I�c/���
���c�����)���.B���G������Iol���?� F���\,�ߔ���W��#�ҧJ�����q���[F$��
����L����#��ݙ�d2�?z,N[�L��(�U
�l�M� �%�4F\ ,��2�g@��-\&l�[�"�����b0gЬӊ�3؄��w�B����"Dq�)Ɋ�Uw��%�D�l%�zЊ8�z.�~⑾V6���lM��B �,�5`Mo��ǒ�h!�F>�������\Ǭ?-��}�Y��%*�X� ��*�0�����9���5���"�Y�%U�e��h"$#ʻJ��?G�����&�'�G�%`����E�_�_ï#�F��X9&g��h����j�X�����w����,�d{2_q� %D���>?��>GXi��9�?|u�x@�������;= ����O�4����E 0<2F��
�F��/q�˸��մ9�ŏ�hz��Q��˚��/Y�8f�Bd ����2������~i��~�C?�~-M�2�R�L�C%K��%�ҿOZ���iǡ-�W!*��u��	�+��FB��0Ad�q!�z�}(KU�o
y�T�J)���@ӒX�X@�R�/au��;ą'U.a��z���1�	y�d�&4��S�I�&�?p���GY�8+r`*-�!"� ��2)� ^��VGnR��yP�$k� K6����f�I��ŧ��P��������f)Ǫ��5L/LO�:3bK`�R* k���0-��w��0�K��]�?�5�pr�b~�6��~Q( ��%�3h�<��T�s���r8�E>�l %�4��v��-�=�e��_�9���A"�ˬ���~�6��ms�TդƉKXf`M�1����g��MCD(�R����<M�/�(���54�4}$�8B%�:��ǎ�}�]�F�[���ɨa^�p�M���ֺ�����K���� 	������y����
a��r~�-&�����y�ArGB4~~>�ݤ���ݻ�w<��O�$�I��	v �Ȳ�����0�n���)T}j��U��	��=<=/�|xD���� �<C������ɨ,f�t�!_3�\��;���a��U=Y!�gd?0��Z�$��1I� ?4�Pk���d�����T�[!l�B`!��?��<>��,ސ-��Q�G	]��ƌG�k8����tTg��˽��>�N�����ȉ~w�#>NV�gd�(�߆��Q`��(<���s���s���>�R��v���H����H*ZxqȪr+96�J�U
��De$�����PZg(�z#�w��6i��b��_��lfu�|�����F��@a���i�.��S�x�����ee��k�� �
@��%�a��'�7�!ǿ���@�"ZP/�ɪrh٬�a�z�NX""J!��~�"��Qf���X��H�E�Ft�@�pV�F�PT���9��3+�3��B�X�A���-ea��8�b~��xsg����1�nW���o<�}��uF�Z��/�0=�����0�ox�ٶ��5��d�1��O����&3�0    �tc?d�$���x8��<����$J"���/��C�3S·d�~�-�bU[!<=x�+��\�<7Zuh������qem�b�p��Ia�]&^��#ʬ4�7S��c��6Ls=,�4ۿ�]����$r�iW�nl� ���� �vT:�؁ۊ�fL(�%�F�s}eP�KLK}e��y��|9��*�豟J�F��,F�%]��H��(T�_ � %�z��n�7��KY#����G�պ�Z�陽�Q?�����;��%
2�["f!�R�uI�gB�Ia�5�i2�ì��0���w�v���c��{�z3��#��$_���R.��dG>��]��������m�,F=�%/��E�Ij�GO}F��%_��\�(~�JF�����/H��ѳ���+&�J:�	+EIf���4w����:�Ex���G,]�o�ײFiv�	�f��D���:6�,	�O
V���C���2>��i	�`!��f'��v�	Q<��U�5���vx3�d�(Ϧ���5Ocs^�Hu�f}�o,Ou�K������kX��5��i�ߑ< �k��-=>7BC]�'@Ϣ�bT�
�|�.aQ�fb��f��`���1~��e���̰�<����\"�G�	�Sb���3���#�q�9Lfo�B��2��{���(`+�k	�@�0(���,��}�k�v�x�l��'Q�������5����H<$hklq-1�?�!xJ�򤧚4���E��g���G�gDH�/
�)���ϧ��i��k+D͓z����P$Fa ��:��쓀�۾.u��U�e��2����G�ME�;�\A�����g���e��#����}�6��%v�J�	=�a ��%��.�������G�ԝj�U��l7���B���SQR��F��|�X�82wV���?���9��kr��]��ARf���w]�%��]O9<�K�g�0۞P���/��
\��a��1|Z)������e�����$I���S<�.v1`��^W����N��q^��i o���{�Z���>YZB�����A���%��$8K����rD���r	=�@��(�j������b�5CA23{��ļ�P�F����<�1?��<�=bܫ�2mJӐݕ��ahXD��y�4eU�#���͗���[��<@����`#��Pi��i�,,��!>!�a�����nRҲl���l�G .�@5ԫݿ���3��bK'���H(f�U ��f$��#\�F�j+D@cz��\͎�n/�TpK�nF�N |��x�lܬ���K�1%�1l1�cS�^��ǰ����nOj�<E��I�g,�݃��'�'�A��D��F��7�'6�|�a�ȣ*�;;�����xȁ+dO*��8Hع����dڶ�X��;��j:��*Mb�4�$V�yI�; ��}ݒȨZ-k��|�/��L����!vcJ;��;襪���(@*� Ug1��u��?�}a�������D��V��n�`�UW�R����=���B> 6��qZ�s����T�xB䭫�ٴX.-���Z#�rRI@Ĭ�#l�9.�zXU+d��'t��U4�S�i��䳉���~�I�ݾ7c>B��*wg1����=xOX$P��Q	+���3Q���mv;U����x�eY���x�R�b�u
��Mm���Z��'ϻe� /���'�;��?�qhO�,��8}Nv���	
#�*�P����c�����-�y/}���
��0�)Vᷰ����ul7��*�k[V& ���K�?)H�����k:Tx�u�\o����ad����$}�r%¡&b3}Ċc��C�>�Il�����f��O:�VY�&I(�4V,`��HS��pi�a���1,��M�sDHl�o�xW,�&0:��ca�Ae�P]Kך��C�vTP`��.;�;B�F\�6�<9�0D:��Pײ���3�R�f��B\e��f3��D�$�uĎ9g;��|nFv|� 5_"���R�a��GW����9��P>Ko	"��u�}n��y2$�NwHl{�g�K���#�:�V&�t|�!D�C_�3�+�M<@4�{B�	I#ء��� ��zO��}65V�%���T��bvA ������R����5������4��>N��/>q��꥖q	����œ`�J�{+��J�l����2��2b��M�D��훆���0�
���G�K�g��#?��-X�I i��'��9�����K<d�|�9��LH兩 ��9�V4Q�� �|�����Ƈ?j.� ��	0\�X�1��l���R���_�.��^a�y9��7�#��ԣ��:�_@@|�}��x� 0y͚Bz|�+�C����ޅXyZ�@�]�x��($*Ȟ�b+�}��	X9��;�U3�dI��T����%<<:v�02d������k)�H��#�ݪ�&,�]���1Xqz�$��+�C_�N'<��g�8q��>�,�_@Y���$D�x���}XtT��M`���}n)*�/=m��C��u�	�@�7�����'�&+Ŀ�v�	��
홈��<I�u��vUO��LF�V�O�w���:q�t��
 /�<�:c೛���<P�n�%~�&E�DX�Ѭ Pł�$Ql9j������r�'�����ϣ[bǎ���np�M�]��������@��%k�>N~���-)2�pż|�,l�ܜ�����o�eUh���3��o{v6,P�o�>�ޘ�8�� k�׏�o2�ə!�#�W3�����q��V!p��$x6����">I1`8��/#�%61�0f�Z�W��'!b����-B�ς�lI�v�d�(�De f��n��]�R�F��*v�;zҸC���3�n8a(!�G�����/�hCRG]8D%��@h:�Ktj��{2���Ir���3n"�h��D�$$&p��P�'��,$�fnП����=����,O�I�*-�	��$��L��c=���;�-���D�k�7H�HĘl|Ǫ&�)d��g�s�Y1T�U������Dk#,���e�N��c�8+ʗ�
�Fz�ZJ��0$
I���q�J�����c_�a*$<!闁I����dt�v^��|lu<*���7�K�-��160?��׍�U!kbcya��D+�>�{"����e3���A��o�;W"�d	e"����2Ăe6X=��6�}M%\��
	 ��P5�ی��N����ϛ�,7�J���4�'<���4��κ��sCr	Y;x|R�|�� �:�V<S��V]�k�a���A��,&͋��`�lKwþ��3��������P(�UJ�	�|(|��X>�
���z��8!�V�/��-�M�O:�DRi �!n�]<�D'��A�æ���BҾ�s�3PA��A������یᴕ��0�/r�=�	λ����	6gٸ�;��ty+c:�싋��L�N�^�B�d��!����'[�:��_O�	�7ѡҖ��f�MɤE�������m��!a^��Kr�j�{m#�S�5���wC�v@2�DxmwTr����y��_x����?�-M�ϑN�*�Q��fO�e@n�d|9�����	���/�%[�$�O�W��MUq �(k2e�a�L����Ǉ����K�L��7�O53f��U�Hb]\����$���C���x.az�� k�\F������ϙ!�9�n�ȟU�o��a��vw8���_Li��� ����0>52%S�uO`�}�/�I��_��Xp�Lh%<O�-��	���&�����~�t>��{�7�oS�����.S�����Y��ӓ�!ˆĶdW =te �����I����%�mʜ.r�p��2�p�,��i�(�O7xt	��F�R�dk�gp�T���� �DRte^ -$���r�.��}VʗVdZŀ㨼X��=�]D�7'v��<r�Lo;A��z�F�!N�'��%�ׇ�=�O��~f���5H1�/��K��rh_Y�I$N��b��l�f    ~踙\���4x�4]�}��]�3��r-I�D����=���%�����UC��w�EB	č� �q������eM#D���_
X,>�^t��I91[��-s�?��:��|���~��KӚ�Vґ#�
���x���n��$����X�fk.�&>Ȕ8�ݤ1��i�Ed���XT+��ī�S�r�F~(��Q
�?�/-��������ʚ��r�NnfD��"v����I�Π2������YL��-���4'I��I�3;�Oi��׺��_|��.���"c��L�(�!_�K��e�_�_��.��@]/R����đLX�2k���T���>���O����k����rI�CZ��	I�F�sG�ƒV�XE���t�5�e���ՒY�Q�{a��Do2|N���k�rf+���Vx��mk��
V/Rv��*&����_����B�m�i��M�|��u�)~@��,�2��e�QU�2��FrЯ���D�!���DÛ�%�����M��MVH�2xm�TcBg�!/��徑_�����-k���,����DXy �"P �s�F�`%�Ji3�[+�m��b9	G�<�f,m9|lg�ӕ�~�[�W�� 5�dM�u:��=MR�"^C"E"�:��Q�p��mה���Ji��U��,56�&tA*c�B�4�����)u��6UC���.B:<�9�l:p�(إ�}�.�L_��yE]�����Gz���Ϊ���1�\��Cז9I��{�d؇Ash�\ɚ�z���K����B<��R�ˁ�훓�՘[!�>��v�{�Ә�V�B��_v:{D�i�n�2mo��VK��N�GՐ��ɤ� ~gm�a<�7��6@��fK����B:g$J�g&�L]"���"Xy� ��5����o?r6�~P��
��a���ŬK������y��b��z�M��V��{�\X+����ü0�"S>�XƔ���̘��L�F��DV�jwg1=>.I�g�QQ M9cUF�KD�9�b�_�#�v�ʚ�fU�ܯ@&L��h,b�2�3��$^
��7NZ�hk��^��tAF��l���OG��Ѝ���2��ƔLTX!}�k�$�k��Ƈ3�8D�}����}�m��nf5���h�c���qB2�_�)�w9��M��ب��%0��l7�L�Gn#�#�q�#_�%uP���	�o�\�Ք�j�I�3��V�˻�f�>���T�����qg�Y�V���hǤ�'#����r�2� �?��zz�c���O�*��|0�A��qaX�س#3� u��%�1��E)�/c�\���g#���¬r�&�3ϛ��@��wV�Q�k�9���C�Y�Bԍ�H�R���D����}b��r��'�|[��b��zg�����(U�ƥ8v�a�,��N��K]f1i�w.D$�}����7F31uT�|�t�����uM���=�㤔�?��ю�BI�W�YA�'Q��#N�DcO��"�$�����y�J �:B�IX�f�!��}i�N�� ��,��=����հ��.^t����|�%P�A�kE�� 8���Z��}n]f�A�ꂜ+�1��c�C�N��߷a�Y�0����y�&g߇O�8c,��2��g�����fj��IL��NY��1���zl��Vc ��JP>.���È��0櫤���*%nd��9 ��DDוa���q�s��6�C����Ά�<6Hj��*H< &��0 %��66�6���4�'�<��#�=���]C���r`���?�D�%�F)���p+��ȱ5�l�B�}OpC+o&�D�.��_��_,����EVY�3�@�F�r|��'p�	D��>r����� b���ۧ�P���sp�J8����B����f{�cGR��Y�]�� ��l�LIHŎO�l�>�`lfQح� �ɜIV�?�妖����	cSԌ4&���؏䐵5�����bJ��|fI�![W׫7��.����"����>���6e5+	�	����:�P}�{�c3p��OCݫ��,�_�9�0�2U����DL�5��t~�|J�C���
z|Rrf���S�\�&�]x�I(9��N��$0���q�u��I�O�
B� n�DI/�i�Z�+� �Ϣ�_���ӜpϚ'3)ϊ�'-���������������p�U��x�����!�d����ROrH����Y<�M���Y�Z�0���~6_�9Nf�y��Ȭ�c�oO�����,��3��mA���=4Fj9	�_r=���ؖVп��}�Є�8�g�v��`�	]e�L&��g�t+�>=�^p��0cJ��H�;8��f��n;X�n��~�d�D�x�D[�Qi�Y���N�o;�W1q���
��A�;HIl��?Md:=۞ؘ(G�0���m�A����&w31?;,�A�#ci*�6d_���A��Cu��8sR�h��{Va#`��^�o��K��Z�g'�����G.������{��+�9�� �B3U�y��I��S!�md�����'Κǘ��"�����֏r'k�Q9����2u���t4����~�-��[!���:�XF!r"
b� �
�
�h=r|h�����o�s2$=�'����B��w �����������[��G����P�Hj��\��/X��������/���L�D1�;��e$^��g��gݱQo�ڊ�~<�D�m�#߀ �mr��K��.\s��<�b����;��������KX;�����&�����F�����0��B��&`+P �P7b����@��R�b^>�zD̅�7��y�v�`��NRg����p�WE#kn�:�P�!b׌�<q�ly#%�� 93�p;+�/V)ߝI���.��+e���Ȑ0��p�Ӫ���A�V�K�k��W)+�SY��H�̿��aF䎌P��"�u�����@
����|(:�GC~����o�<�3j�UʛKJ5u��pl1��H������Q����YN�\�G�JeD��oùd!0[*��lRB��j;.�޸Z�F�<� wE��=_'��:�l��r��;֢;Y���P�W�^��Ax�����(����3��Bv��|Ԩ���y':���%��<�M�92ݙ���1��f�S�����
y�$��Hi���q�+�"2��9����4U�����c!k><���j�� �"�����L�_�%So��@P��9g�wy�&VRi.b�	��->�%�}�YC�$�ٰ(=IEz��8+(�N��{>�ёμ�@�C���yn��N�||����Dg2F��k&�!J���� j��_�s��9������O�T&�"��r����vB,��hwz�r��Ff��)�bp�/,6糑��!>ۑ��9I7vVȗ�#���l�	��cL�)ɣ����]��D��>�:���Z��̣l`���1D��IN��V
5��F�#K�����#=�'��M 6��"�pɒۀp��1�}k[�'�+M�;s,��Ϲ*6�0�s�sZ�d�D��e�0v~zC<��6/a���8}�Ik�_7�Mg��ت��"���ݩL&�|"�����Y���]o������3j���8b��n|����P7�p��׌s����
7�ݼ�4��HNt�ð�<:,��]�=�`ԶPuЫTxY]�k!�"�Eغ#��
�t�oms �A�a�
����xGN�qB��X:V�&��@&�#��N���ϫT�ol�U��<�ˣX]LP��^�-Tm��-BX���aV�G@͎1���ʀ�|d��Xy�=;9N�j�be�Y���L$�9R��F�k�b6��JNl�������S�"�v@r�+��G�������*[����JY�x�"y���C6X���N�=�:�5T�o\&�@<���5Y�HY��+��r"�R&�[$dS��_?�;���K�_d��V!�%r\�̀��m0�Ј���7��c�WSX�ȟ��c�3Ǝ������$��O�����\��E.8ѳ2����db^�F��l    E��>Id��@�>,�$��INU�E.�g&Sr�,%���Ndcnz�Φ�!���xڛ�
+�����%&	� �#.��<�PP�5��PӲX�b�f|��<�"%�f*\<�ԁX�g���i��9ժ>���ʶ�D+v�:�h�a,�G4|���&�j��:k�v=<��<8ڟ'-!秓�%�_��,$����&ە+�,U91%�K�%���&������CGj}��n��?����&��+������7$p�oO��~�g#U=*V*�<����V��BL7O�
���������7k��ݭR�B�F��֨��,O&F|��p/����o�,��=�$P�B�Gt��螤���ɟ.�V|Ǯ�t�^�Q+�!�.H��*�V(�?��3�bh�u �)g�����H'�޴��:p)���0y2T�O6�;F,����d!�h�Yq��R�>��8<=#,�x��v[�[1>�����g�nʚ�����Q�R�+��+љf���1g�I�>��l���OB�汶`���b'Y�0�x#�+�A�����}��҆K�/���d��+
xNOW$���v��c_��Hc�b^K�y��x�	��2ԥp��yk~s��O�E�k�r>�Œ=�E\��N'�p�29��`��v;��CF������Iu�$2HN���X�p®�,�iZV{H��R/3:>�(�n85����$[���a_In�n���Y,~?a.,O�<4�u��%%�9��<m4�|�n�Bqz1���8�+�D!���sOl/�w�X��t�B��`G�4+�I�р
�V�X��6|���ݩ��Y,_��YV�8���&E�R�O�پ�_��Z�7�U*ݧO��)�1G �Ζ�P΄���:fZ�E<��k�=����f;&�i�I?3G���5v2��}���Z��3m�9A#��n������H�!��?Oe����m&��t��ف�!���Ba�	��╢�`.e�e���J8���h$�q�*����P��O�i�������if,}�	�1�]$=k<5��O��|}�vV㊺�_T�x��І�/�#�ZJ{����$�cF+�ɿ�y`UZ�/I�U�P5ȏ�9��:�)���Y�L�5I"�^��±��C	+����?P�-��i��Gn�]��P�g��^aeC�6A��
#ɸ��p:c������>oO��e�~�+�07�Z�&gd���t
q��x1蚺#��C�x��E ��7�R^�k+�e�P��RZBr���&+s����ȶb�/T�b�R���>qtG ��t0�=޻�V�Γ��m��@Q����ijϒET���ǘw@����c�n���"�Y+�ՓS���Km*���e��ٗ��hV,맷���W�i"�g��ِ��xӌ%�- ��K.%��M����`E�a퉉1�v�`�͎([�{�a)y:��d-�`�i�D.Z�$g�_��)�Z�U*�Y����}�i��Sy")I�ؓ~˼҈�F�=����a#��W���6&SR��X�-�y�B7�d����.M�=k�!ך'5z$_����$��qd�p�!�g��r1�1kAn
S�M�IR�.a����u��9�lfY��1��ZgI8��ci�@�NIi��ԇ�D�Y��p	�������^`
?��� u=�>�˨Y�_�sޜ �3��`��q�)�x8�3y�73Z��w����b9�F��C��RK@�8�8��x0�}��J������ϑ3*8&)	h�D�sek QЏ���F/��1Y"��'��d���]i*��K��+3�8�Ccϵ�*+���Y{r��6+�<|����5>l��Ȭ�*�X�?��`6�n17,�p&4	�/9�b�8tJ��s����c�W�x0�ٸ@3�:�̳'�D<b��d�Ќ��ORQ����O��<�Qz� ��p�Ad����c�FO��jb��2M�4��B�F;�
��0�q��}͞@��=��X>d�a���9���9l!�69�kuou!<�C	a�<^d�\o���8�]>�H�2H�;�ϡӓ��Hü�s+7�����ٍ�H���h��Od�[�a�+5�T��X̻|���?%�D�4�ТS^F"0��j������9gR�^�v����f:09~$��@���d�X}4MoO%�J�����?L�������Ru$�����#�@����%�Q:߷��:*f�p���AX0��P!�0�'_Jڿ8z����B9$���΢����9�sHҀ���ox�.�6>��]q�<�GÁcj�`�,�s�(L���V�����V�#����P�H�L7�X�$��P8�U�D�a�NF�H ,�o>���ng�>M-
S��y�8
N�cEWZ�fr�]}*���JFgFZ��'	^���Ni�H��&��S^���`�9�����?L�M�y���m�j·���<��t�$�y~3HŴJ�����_�A�r- OI&�ÓVv���y"�&AΚ��U2��$$)�:ªz���V�Y�e��`�"���)j���ʵ	=&���q���FR#}#E��9_%�{�5!Q��as����M�!;>���Ȗ�Z�,�K��b\��FgGJ]��?ޱo�yfDQ˜��E6��'
�A��P���YR~�O���MIf��\;�E������l�Z �GXLL2+q�%{Q�d�2�[w�~�p�}É�.��x*�[����4^.<���`�JV��L�l�����C� "�X%�|k:��`�?�09���"��8�ǎ,�Y��מ&�=�.��j�`��D>@N5O���zr.�Q��d�^�$b�9Ygj
K�,�9|'����A���>�,�f���"��Yj>���!J�I6f�"�8���pgQ�䱒9\R)�L*X )�#}�ȓ�N�X�Zlڵ>،�X����/�����G�4��=&���V��6γ�$Atد��p�Xy����9�F�t����=��e�8+v,Q0�儈��e�1��a�Pj�6�&�n� ����;+���q�<)�J&g)�~(�8R�'��l��G?��xPs�Jf������l�f}脇�GP�Hf�Aj�hu��͚}�<񈂹���B9~��<E,���zDu�j��ӇÊI�ڋl�/Jy,ʧ� 0$��DzmX�pM{%��Ka�}k��1s*�u�Df}���~*΂�T��.=�_�q�l����9��?�_����.��������?����T�S4xjX%�pa�$��]��p
��Ǌ����rt�Mq́|��=tEq�c�<'��ue�?��٬܊�z3�_8�x>Y�˺s_��L�'�ByE�'��x��񾵆��u�j(��yJ넶-���ad�� �����e��i����/�G�Tb�Bl� �c��3W}�5�ڞ�SZ�]��Ke��5�'�eؖ$��H�|R����w�qd+MCs����]�l�P��Mҫ��b/A>�L-���r��P��"�"!�ғ1�e]�q=�� �Y�tf�
[^0�ׁ#x(g+`�ŗ#
]��@�e,�����`�g����@���=>��K�8����)����Б��yr���s��g�p:���Q�qjYf9���bƃK|�C�1WJ��G��j��K;\9��N?Aa>�5��<���@{�LCG�H��8��rؾ��G�j�����_�r�&.��K|�s���Q�<C;������U�O�D������3�bߑ���lq������]����b^(ʎ/ms��^��Θ����f� ��<v���E?�8�K$�	����V:���5^��v�<7�a#�� a����@x���~9o�.=bv�q�UY�̶� �R�e��E��d��m?iܫ��q��/NY����(L�&�q~$���Bۛ�ˮy���E��j��<F#���X���������r,.�Q��ڣ��B�P�T���I��>[zyz؟d2c�OΏsex�ץ���@�C���rٵ�Σ [f�0�x�]�Ty�m�s<�    J�]��F�4�\�
�<�LV�<��<Ń����0jPme�]���هp8j��m����D���)�D��-����b�q5gq7����CL82 �_Ir5���������m�.�NƏ6��J}:wH�5��Q�xƲ��=�`8O��A
�w�*�~=1��I�r�#�GK�Or�!�!9N���Vq7�9�ʋ�8l�K�Pf��yZ{G$/f��5eK���ȉ$��x4!g���ϟ�2\�g��\v�3�¾1����Wĳ�x����Ի{v���P�^���wxU��!&�&�<ՐmGLps]�d-��g����%�KN���acC��Pν�y��k��x�;>oh��'��A1�*��f8Bu]���R&���"��wv���d���E�S��U?���Y����@���I��)�'�t�,  t	��H��9W��)���O����w�o��Ri#tbÃ���E�-v~ߏ��Atj?Z�r����I��"	Qb7����a<��zh`&�>������HB��0���sT��M��{��Y+/;qG%P^kEh$c��#s"�����ms�Ўp�����Z���E6���0�hDV����~��v���aw/k\R�$�P�]����kvs3�O����ζ֊��ig�*�r�&u�ؗ@:�l93.�V��Cgޝ�B�Rŉ�TE��+�Z8��IX�$8��h{+a�\�ke~��8���0�t?R���jtb!��AP�INM��� K��{.U�M�xo��ٟ�!a�A��'Pj�b9h���j)�x�.0���+���Lx�D��wmI=Ll��*��%4�4�:���J?ϰoȕ�'?��I�^�'=bɩ�?G��O2�a�r�g�^�j6�� ���$DN?�y���d��Qo)�T��U�GAJ�I;�0�:2�{�Sqn�a��x���2Z�bU>-Jg�Tڔ��csy��$d3��rlvV��
��؞��<�Wȵ1��f#�m�� 4B���j��.����n����������tA;0JNlb���WU=��rd��RXO�d�3�@�!m+Ѡ�D��~F�v��2CC��x� �q����k�GbZ�:<P`��&#fX�+�s`9RK��8�XNϻ�C#�_u��Vw�����@��9>o��;�.-j�9Q�[��[Y��3>![�y,K���C�<ĉ�_
�x��1$�2qs��b�f�����yN|L��ϑ��P��{-�|��V�ű���0"�0EI�n"#�=��c�X��8����JU��@H�LR!�=b�Q�z}1���O���$#r�Y��'%�o�q�� �k�Y�<��o�U�޾c��c0V��*�/=��g�Q�V�Hf�{̺�5�P�_`KY�_O��1Nz�#�q<�.�|[������(�װ����1�H�[gQ���o76���x`��v��6x�|��I�jz�`�e\�P�y����L�q����#��S�饟��,R5?iHHW�+앏����,Q{����p�A\���f�j�;i��+0اQ�,� ���4�ٽ�G{��d���|L-ˑn Ͷ��
*C]"�|�l��:DQ��������Ls!���9N�_�.]�ߒ(h�(>5����[��H�%@к!}�s�9'֗a�p��|#�Z�B�:]��K��
�y���)�4L�Y�'���8FD�T�Xߺ���v��ދo�向|��N�;�Ci��
��8�N���Y^%���Hfn0k���n���~w���{��!��a���#�~?N�|-3�Jic�	tJ��]��4�}!k�*�ٓpƑ3�2:��`���N��-k+�~P�JR���
8Q[ɍ,�� ��Z�İ�Լ����8#g�<B(80e7����	Q��g-���K>���<%{�(_~j������a`+c�̨��
utF �H'��س��M��v(9
�	!�����u���x��[%��8=�A<Q	����Ȃ��왃�u�-��"R�9M'�^`@:�syʽ�y��D�aar,�,k�">�<�&��6���P"��R3�r�Ǌa>�`>������`�TN��a7���I��k�?}þ�C�Ju.���9�#ƒ���r	V%�ʒ�a^!�,�ă�"cg��h����� ��q.l�g=���f{;�5�ŃǬX�ˁ;���B�K���l'ڴ�I"��g.�Ɋ	�9gwH�&��M\G��I"}�g�Z�����lz��U�w���3iR��X�+�}��B}3ý�ʮrؾUq߸j@@��_��gA�i�A��Ya�H:�n�^˶�%I���mG�0I=�B�������쾪�v��%�zE�ўǓ[�
�ٙ�F�'���Q-��S���e�ADk�z��J5=����tY�bP.
��&�����w(L���0Z��'87^$�#�� %�քh�E	ڥ��"@�� ��~��/OgjG�¶�H�)Ix3Fj���	�Вa����S ��.,�����/������d����q�Lmn�&B��7���ꠟ0g��}��/^�|��r���\��:�"�b1�؊� �#������b��6
��$����nA�����s_#q�Pr���="��ːF������[�/�}	*�:ĩ��0N@X��q8�>���P�Ǽ�������aF���Y�)�Ƕ��h �{�@Z�K���0�z���\��^[]jj!�?��~`>�s��Xa&���
jKZT�G�XGk=ܤ�)=Q�4o�Z^��#PZϾ2�nCu_Ͻa1Z����u����X�q�+�vI�[��/�ptէ��b��?S��N�!�X$�<�}�����m�)��g�OS����@�-�zcn���Ti�L�[��칀b��[d\���(�p`��*9`a�E,����\MQ�/�C�ZӍz��/��b
`=��VT�JLms0bvKD�bͼ'�&�L��?~>��F�$�3��IB/R���A���m�&��=����l]�	8����d�\����H
�ELm0_&s�_"2葦�95k
������7�g�p�~�h��Kg����dc.�[nża*�I���>�3x��KA��G�up��*�E^+�\�Ha��X��NZE_A�UG�1jxLm��W�yꊤǖ���NJ��R����{[��В�lVΨ�
H�� C���G��9����=A����?V[o�c������8Jm���,��z�+�Xx6yS.,���3�ɋ�|�C���>n��ۈ�"�_f������a~1�t�r��V��\pl��S�BK�*	���֞P��:��2^,.f�������X����8%u��؂Qۓ�k0��Ss��C�O��܂Kv&�D�G��Mr�@0����7�"��6C���XP���Uo���4������4�#	�Ƃ��y@i���䭭�yl~1Zu	r�.��9ڧD�'�#�t"�3_:�J:O5<�l���݂��߶ꂀ9b[]��٦��	ևz��W�����c	�BB8y��'oA^���F�m��+�{�C����W�Es���cy����4R#G����d5ĕ{��k�u�������A�;Mc��hG���i���հj�3�h��.��ˑM�[�.���ca�P���w i�4X�Ǚ�^5��<��_�'p��ܼ;�{I�A1@\@F�f��^���q��^����v���Eh3,IBۑ�[�*��+x�ՠ��-+�B`cy'�*��d��@����ߕ���A�7?s�Ǵ>���ЧdW T����X҆]W>>�]�f�}��	�'�3�Pl������mA�"5^����b�͓�mJm9	�p[j� ��B�������*��v�����Խ�{�8�&hJ �-Hu���JG�k�PwS�w�B�,D,3�W�E�W����A EB�������y�B�Tl��r�˝Y<�H{�,�ys�iTя3�k�w7)�H�	\�9M\I:��M{K�L�����y�*/\;i���f��qC8MC.q�D1Q�fq�Ѭ����?�����Jh����=R �ZՆ�Z�&��-�ÕpH3,Y�s�v`2yܰ}��^��J��f����em;/2	���5    �t�b Q���?�`[��RY,�UM�pA7�;;!K�'��l/�H	����~�6�HN���b��S>#�'!�F��Ox-��`{�g�9-I�,���G�~��܂ܑ�*JG�`�>���q�ZT�W,g�?^�r�I;e�Gh�U=$�Γ�噖�C}�Y�S�ϱC>� �s¡�W��7= sRȌ��-A
<�q��`Gz��$�����=M��,�f��/H`��;i���gz�خ�+E���R�;%��36�mC/j��[�J�噂
vz9�y�;-b�26����-P��`��u��@;�������0CߑG)k]~s� a�!|i"��_�)��������0Z�xZ��c������h�O~:w�z
�	7���I~�M�I�-ǜ{1�©�����]�Pn�� ��h�+�Mzm�a*�U�� ��|_Ԑ���*BΉ��P�;c��h�NGi���G���4���.-�;]� gm��U`c�_r�a�#��n�@��N$)H�+gl��N'�2�/�<l�Q3�I��m�o�7��RW�g�My�{UHX� ���S5��
��{(BF1��4nf��`�+F��"�<Kx�2c����W����D��{x���F./q�G�t\��z�uhM�M8U+ۡ�fͰY��wȪ�-��H?,���'� i�z�{���I��g�<���w�x'�Б���T�k�}[0���bn��肵�>W�C�+ű@SO��8����<-8����ۙ��
.;���J�l_I�����6�+�����>�@#�K�EP���QjX�67��	9=\�5r�-Z�0�k ,�|'�.M'U@����<����}#&���V��lr������Rρ���U4����z�,$���D�x~�3��iaaFE�EƦy���.��a�W��4'i��3aL�iL��9�X�|=�\�
�J�g�$.ѧ�"?93�����t�^%��(��E�5
�CȠ��]��¡�;p��\��&�H�%A�LB�wt{@g ��#u�c���x`~�磵����J7���B�T ޚ ����4�|3���gqp�f��)����EqGF+��4BT�>W���P-m̽��^-;$nE`��$LZ�늨��M-����t�HR����<�g���E����G�3��>D��£n�ϝD��`�)�� :6�,�d+�c���n�sglN�Ȳ���3�����)�"Ap�dZ�����������L4��(2���%�'�S�Q8�Wv	]dl�%I��=#N�^K�F.%]��@&�Z�Γ��gyeϰ��"II�-��n�7@�Z��Q�Q�~Z�Zo=7g����;���J/����D�Ą�3$^�b�ര�>�0��=L�%��L�m�UAD'��80ll��5MEC��S�4n��
4r�H{��0�J��m�Ԏv���N6�hm��5��`@Cb/�KE�d%�i��n+l�/�٢�����E��(7+���Y,���4���㴩ɸ}N� rl�.}{w@52�w"��O�9u�B��R.E�0Z���B!�RF9�#Y��Tܮ�^��8s��Pe���)��[d�E��j½�U"Dk�0��ئ7�� ���N;�s��ӈ�U��9�.�����f7�t%�Go��^
���y���������W������E`��ȝ�WAC�тRZ_m�;-�'����p���sֻ�)x��űK�}B
8ѽ?�1�������m��d9k�[�w`�u�&�)�GRw蒼�Ky�0{�e;�6�y?&���	I��6U�-��5�E#�p �����v����'(�2�L��Vu��l�����eM��{���v�$*�"_�G6G"�^��"�b[�e?�Vuռ<��a��մ��9{)�@�j�:^�G��;4��_�`��ذ]j�_!��A��?�IB����_k�9��hw޷6��Yy���j�&�����8��Lz��Ҍ�q��y��:�2l���-![sEI���D$o7n(��d�>�mߗ��P�]흱�og:�3�0�9]���C����>L�+�d�Mo~�n ��t����(bfԓ@,B�OpR�͡\0��8c��D��Apn��)����e��/�ڼ�w%��UŰ�Y�'�-{��<�z�����|]���o-��bz�m���R��#�gz�!�Pt=�vV3��g.�hn���R֤��w���2Zp�qG]ƈ����XDO蛈�I����R㳏�f+A�^�v7����)��%:���l�Q3n��jD�\��F��*}�����b�L��jG����O\+���V���,Ԫ�S>���9��������H��B����Z��� �A=��5n��@�6u����X툄Ep䏅�ɗjqA�v���=�������n�����t�(�Pc��Jܯ�X��;̜�=M�'�p��	&�9
�]��S?��D���V����{����mq�\�i"�Ǡ��hBQ�_��E_�7�Ma��x�F�t�
���c������0�O���y��v������1����⍱�"I�0+��'�n![;�y�kgl�R��/���
o�4>e��;�=

⛶GpDηm5no��4�/� 3m�H2qt�'a2
�}g��soH����h��Y`��&v�zY��*IH>��,zm�+����ޞ��0
ՙY��m毚�y�jcg�W�M�(�rirG��W����=ňP䭻rm���,X��\y$�a�?#�t�7� .���z>�_D@d�KF��'tSŴ ���$S$�$s�C�����ڝ����&y�&j�Ep�F"!�f�p{��}?(uݶ�դ7����*LcA¡W2�~���a��ު��Mv�a��"�ŭK��:�Mt6&o���3��EoC���=����� rR�q�=�J���d�"�a�?�(*ɮ��<>�^$�?�*�5�����n{�-i7q�5%��Վ%=�E��c�	[��*��h�t牝�{�TMW��pBV�ۥ�!Ř"cf�6�tW`K9Q��*�F����f~�3&�?r��9�(�ل�CT��5��[���3��P]E`�Y89g�;̓��Mο��{Xɪ'�rt�H�a�Ce��#aD�xZ���V7�;hl�$���GDA��s�mn�X��Ҳ���P�"��Y�7s<6�g�5�}
)�y�AĞ�É�*?��9"��C����\0�A��OT�@ҒPw�S��KE6��6=3s9 �Qr��q�P��`���,Bo6v���G�el�ab;uԑr�Àp����s��mS����=J�DmD���LL�6S��M�>�I���kW�i�jr`!�)p'̊Z��� �蛥gN�M{�� ��-�3b��,�m�*ATNf��t7�E`1�]��e�'������+�5"h�TG��m��X�.9i���0mG�CU
ru{BYD����'���SINw)�Y��H�0�9���������������މr\ 6v;�H��0�շ'1/��9:�d� ���D�Z<S�m����
9��{hG�!eu�[I���ok�n�LeI{���9��U;>���-�O�4�i�_���R���J���@���9�w�ʵ�F�9����-������(C�DGaٯH{�H�U��l�:+0�݀+��P��+q#�KmK����[u���_�#�q�G9p|��Ќ��<�C���₮�{�͏�y�r8]:R�7�q�Olk(�R���Uٔj56�+u�/)&2�Gᨺ��"��F��?�6���<g���(&�+F^0�hv�|��?��d�,cl��ټPz,Ӏ�_�u�d���zQ�CTS�n���|�?�F�T(j���eS
�� Ks�8w"�|�k�d���1B�h��J��dC��c�pW�� �j*�9hl���L�	�P\�|�Lڳ�?�/϶_4��f��gW����U�T��d�mr��BE��g����y��b��t>��� 
 ����M�=�(ɠ����xJ{�jo5�6��e#�^    c���6OU��m���]��֦����\�6�v���!Dc�sQ�eނ�P3B��� )4����6��=j���!�NhĊ�Ȯ�3��������Ni��lv1���E'b��(b����D9=G��"3�iOI��6��%|��2�I�-��Rej���[x�����n����,�9�Nc�b�b����|~M^5����~N�n �6���l��	�(�*�NRa�H�J�f�٘�9͐g�3������C����d�<R�P�K�K�"8���bv���� �A:��c��%1&���mi��@�~7Z��SO*��ْr���!�q��Oޗhè�fy1�յ���f��)$ж�:bհy�'_m�{��U���� ��&�yvw �)g��.��8��d��C��n�������x[H�&�QO��^����v�;���Jc���P�}e�B���dE
5�5���PR�h�ӧ(�A�n��c��n�|M��9��}�̱����l���P��P�-�K%R
 wV�Cy�쐃���3ږ��j�u[b�=�u��f����kޒ�L��v/4A�P��Ю�9i	&�-�7玈�Sa�7o4���2 j�j�"�f�
�΄1��~8�\d�tF�����c�_E]��QEg�t���!���2��i���sSR�2S��m!�)
U-��gs-���$1o0���d�� �YX�e�v*4oiN�|/ى�{{����rt�|�k�Qa*��/�gs��K�o����!�G�����0o�6���^�x��;EZ�S�����n������3����VCG�L����P��V�"�3���C�CM�,��繛D�/���S7���96�xg���}��x��NY%���v�T�'b1�r�,knc�Mf���U��Qx'��3�ElS�Ch7�����6�x�1��+1�ér���Bº�U n��\z��ڂv�y��q:�v��:�EXj)�ޒ�|����Z��v���g�OmY��v+ Z�:r�+B�̀���C��Q��j6Z]�B�`���}�"�ܶ愐F�GWj)ǫX(]�Mh����s<d�Xc�9 �1�	��$8\V���o��E/!�	aj"��NQ�Q�O9�b�q�?~`UЌcC�Tnh*�R��!��P������S�`�^3�1�e�W�K��?�	\��vn�YLpf�������*P[v�r~1�tZ�-n��>Xx="���'d�6O�T�WAa��ұ�jA}�D���eR���d���Ą�K����� 2b����K�.I�D�#����E�8	oS��z"���p��9vFWLm��[��6�k���i ^�m����Q$�;G�ќbz#���&�D���k���7J��  *{] �(���͞�B��ت���v�Ƣ��~�������n�����ei> ��Cj�ǡ&��˖2k�n�n��z�3���s�2�G��?����9q$"�M�Xy�CW]�d��V����͑ 
5��� �Cu:0�l�/!��f �"�c�xMY������?���Æ�[M�|��:�se�2�#Xb��h?,�������7�U�5����m��?E�Z�{խ��8M����՗$<�z7��~�Km�9�Ā��.;M�+�ۼ@��a�H��E�6�(Y��{_:��l��r�n��
g���0�Z*n� %1�P����?o{�$�g0'����ıNv��M�K��N��9�'�{t�J���hu��� _�x�,N�D�%$"2��L4��0]g��[�E�
�'�I�5I��J����Ac��³�ԈS�Q٤Hb�6�I�޷�RRo����,���^4��pBr�V5Q���Bl��j�H���3�=]$s���ѣ �?1I=`����,��n��z����ϼnR)`�QV$1�xQ�)3����;�	��[����_,qV��\]0h	�h�� 9)T�W���KH
/�Q���Ør�I4���� Af}X{bǤ�s�������Ґ��^("E�
	-#�k	Ě�m/de3�=h��i���r,`�G�:r$ю�!��W��<�3�Q��<L�u�0��b�����K����|S��[S��w80t?nHd���^@ �� ��_/� �_�>�6�t�vFw��3��,*ō��Z��
�p�i��
�' o���=�E���GFk\9����J�I{�&v�_�A������F�J\��"{l�3zn�F�!N֛��[��(��$�0��˴ D�p`ێ�v���+ ��XЁه��Pޗ�������R��i0_R�l�1�C�U���G�j=��Q3�9�G!!�D\�	�Ӊ0�C}|��4��'�8����Y J<�C��I���罝�;�>���@��p���8Jx�°%/R���L�����yv�$x>� ��G}<�ݞ��Ѿ��������)��;b���]n#��;:T�#���`��K�}>��m9�'���s+�ܰ�,�h�m}|w�C�:b����=��M�r�}si"�Nd������jVg�}y��#�^�JQ��H��n���jm3��q�~6N�"`}���ث�SR6B\��5W�O���~��X8 ��,)�(HU��p��"z]�x�E����K��S=�/�P���w
�ڜ�Ŋƨ�8Z}�3`��L���=?����3�bq�X`=�گ�p��3��M��ͅL����}�<� �w&W��7�x7�rI���WW>q�rs6qɉ������;׭=y{B�jC�aq���tF�R>]?��u�K�<��V�A�@"��"ёڢG�c�s�j��M6�6��el�(B�
r��	�,4�-�������)������6O�EnÎ��eۺfp'�r<�V����#�Cv����S��#E��Oݛg�H�g����ʇK�'�.��j�v�LzS1�lA�]��`��5������bbQQ���s�}Gs��؟�Gbsw��n
������Ωx��Jh�SHD�8V#C�z��K�O�vur;<�B�Pc�N�Ķ ���UC��u����j�]ues�����������~
]5	�~�r�u������E��_�P��H���a@<I����9	�A;�?N�����/�*  x9as �,��T�j7�Z�fgR����B��[��Z�Q6W��{�D���U�����S��֥t�QOl����4��]��n����U�-��v��'ZUP+h_I��+~(��Ha|�O�;��Axw�(���M�V\h	9o2�E&�_�/� ���V��հ���ᶏ�J5|Z9@���!u����^z�-.A�����������������G�Љv�A��V�v�П�7�E������z���(���o6C��윅H�lMi�ʩ�pfPA�V��qѱ�_̝?E˴�	֎[l.uÄT>��H�}���bm�?!�c�oY��E�	�Hd\�"%y���h�wc�����̮�;�]xw_y��)@Y�ދ��V&6���2���S�P�h�8c�Ih>���Bc+�mi��v�đ$�����k��f׀"��`���Q��Z�M}��P�O�#ɲ/uG��4�g���{��3ɯAZ�DC��>(9��AL��]��C��!%A��)E�E�k�G����d�+�e��Z5�[��-*|�HQ��ߨ��*-z��.7�&R��1�n��n'�=d�c��-a�j�ulVv�7����/!����+����r����J���`�?x۹�]9}!�J����N�ݖ�]$�<�"Sj�N	^��6p�6�f������!��UaLdov�ڡ���ؚa7�ϻjW��E	|�:� ��5��A望��S����v��e$�`;�"H� -J��?D��r�$)��
�6=���v�c} ǭ�)�\��@N��������'��_�M��a��[>_��n���U�K �8�$�l\���v�A��и[��K
4��-ZΊ w%hu��K�_������ag�YO� r�#�/qGF�L5� 
�n�]��    ������W�>v�lI�㏐���畋���-F\T��m_�ӛ���\�@=j�� ����q��v~�~�e�}A|�'���v;Z
����G�AO"���7{__<:���C�a$��5�?��]�Izj�]{%VH"�:�2E�$��s���ȼZ�`b�)�u�q�M��ll�"�"r�E��6(ũ����T*����6s�������: �8�c�l%2�~��xt~��j�v��(��B�A���n$�(x�pk�3����"���j���:Y��r5��\ё.@��.�_��w-#�v��4^wиn��YZ�h��c�/*�=�g��~*W��$����ï:�L-�˄��EN�+P�!�񸮫����^������i&I9���WZysxIm3�"?O�_��V���:�wee���4G$o�{;a��ιP�sw���f��''�Z�H���}��l6��]ʼ�n���˂��f�_�&Q,	I��y����R[��5���K�m1��4<GX�|'Q���華��f�a[hK�������h�3\T�DJJ���C5y�C?��1����o��&G��)T�w�� '��V��o�q���&ƪ�_ 3�ȪԌ�v =��M�����T�$v���	��!��`G�#�3�|暈\̅�f���OŽDi�H[�]A�(ǥ��z�==����ΣGs8���&5��R�C��r Fk�7���e߃�=ڮ���O�t'�����6'�B
5�L{�x����kws����B�)���h�KęQj������O�>�ɣ��n��.�X��O�`>_ζ]��ǰ�l�<8�6�Цq9���#���8�lJY4D���b�s8�{:�cN�*�D�Su�B�IU���B���lmu�y�q���0W��V�����7G�q��5����v�u6����/oȓ!�l���\Ĺ�<S�ƱG�=���q�$�3�3ʢv.�b�p� �G"X�C-,S?4�I�������qb?���( �R��8()������b��@�O�?�h�7M��Ԃ��H��Lǧ��L4�4���|�i�_:!�G�,�In�r̂���?��Sв�����/.�~9�NC��}��!�E���l5v��S���D����������~5m�1K9r�$p�I�6,�t4e|;������S>z��������n|))e(���9���!�𦩆�\B��'�P��J�~��l�A2D���J��1������{�3��_6H�R�DjO!�{;���P�\���Fk��`A��D�&�r�ɮB ����i� �߮��o~N��\��j�j-֤w�d�T�I�v�l1ӸooY�8�(w�~b%�%fw�h9���ym���7�Fk�M���X
ǐz�v6=2�3�1����l0�.	��sƾFZG��]�B#n�.����w���0�"����=��Z��!�|[3T�����w�cuo~���}9?x�V�~�T��H��4ҶN��4�8�"���D����A3���\�7� ����G��RNt�J������Zo�ժ����2Ǎ�s>B����9�[��_���'�0^-f1N��@
YQ@�t��4o�v#���n �(7!v���y��'r��xU	�2�v�������[� �#���9���4}ƪz3����x��ל:�_��-p�%��N�R���k��J@
���/#WJ�T�>�$���T�m/���W:�{?�O{�Q���t��B���ҩ4����{����M�[,4Y8c�(���w!��W;����t��	��p��Ip�n�i�1����	$��z.w;��8"}a5$����������F��*� (�vj��]�tH�~y���;��-f��1����#�G&c�#�+Ďz!|d
l��\��R��!�M�����\;�dO���k�����zv1�֗�/����Ao��=��Ա#Sag�۲?�v�0$W*�\1���[)�QD�1�l<���b��搾h݈ [�d T]��%�l��� �u�p8_�aȞ%i8�7��@S�T�I3(�W�6v�B���;c�o�d4`�I`�/�P�@��x�W��KQ�oj�C1��Ԫ����|8��~��XeaW�VwJ#���+�w�|�w%ݨ1Rb���2ߏ�j�j���J��d�k�Ej� ���^�ڒ��ɑB�p�h6��Pޏ�0������h��\�K$c��ׂ�ߛ��+�i������aq+!B�T�<d�rz=\��D_�y#��͜a�^��@]���.�jC9��n6~Y�˥��!���dA:	(lQ0�E$���oՏcmo�aX]�хk�e�WP�j���&��_/�����[P�-��5�/��P���2;Ċ@l�ĖB�$���afF�d7ZC��#�ViH]h�)l
8o�̽��@���8�ɀNr�y�{����9,ج�H�*'�����2�+o9�8l�M�+S_,g�;lbPhU�\���{n�����鑝ح��69���m>'y��5Z~��8)���f��j7ZC{�&��g�Q��zO$"Oڍp�YN>��`{��

Kń�u�G�x:�O2mo��Tc�d����_�eJw"�\��r�����8m�z�Ot������3Te��Efw�%D��৴�M]r����v�x������ma`?��;`���T��9�������m�kow�a�Y�0�F3���"�W�sLר��0a�~�ԅ7�OW#�g������7N�w��B �����HHӽAp��~����_YA       �      x������ � �      }   �   x�m��C!��"�m��K��#�"E2p��c�����h:�N1p�!~�	p��aqj�I���e�օ	��0W���½����q�/�Ϟ/�[�S���Rۚ�0+�/ec�-���=��3�~���D�         
  x����j1��~����9�P�5��m)1y��j���+�zkr&�1�_cT�����z�X �o�������������ï�}x�9ؿ�;�m�� ��9e��x����p��q��d0��Dgԭ�;N��h� )U'9�[a�|��p�H���/Nv����w��$b�Cv^l�0����-e��^Y�R�HǑ��PX<i�09�'t��K&F�D�\v|M��=Ԧ�jy�mg�W�$�>����Y��'���	����Z��6��#��gKN�A#M��a>R;L�Ɉz�L�_��'��Í�u����G�50:�q���	e������T-�$YF���|&��!��H�����k����^m�c��׬Ju����q�8X�
�O��<h�<�8�`^l������e�c�p�/��� ��Cq�L�������uz��6ְz>�|�������u�����y�
;��q�my��jHQ�Hirĩ,�vYO��u09*E�Gu[?����QG�      �      x������ � �      �      x������ � �      {   �  x�}�Mo7�ϳ�c�	(QI��6q	ZHЋ(��fm���__�nr�����P��C�L�/k���������ʖ��zy8�]���}�����f\?\�a��G|���'?�2N~���m�)[d�c`2�C�!w*�j
�TU&[ǖ�+Ke��<��0���z�����m�l�1U(.Ԛ�I�śq��+׾��Z[�<�/6y���vd�����^�v~r��������3�m�d��G���4H���>�jǡ	K|V�hݚ���,IZӜ@��J	QU���&�%�h�XOU���S��"O'��ݍ]op���� :�G�#�5{m���'g�/i�p���k��QEh��������Z�X$�F8�r�R�,w�4�Hν9$I�� �mp�]a���Z0�v-��V4�
$���&�g��4��^����^�?=;9�������6���P�(�8��>O���R�-�^��k�[�4��k�`
�"��&��+��H���a,���J| ��>�,���U�fA��9x	��>��{�_n�8=>F��hf�
4�>@�a�
� ��1V�bJ�j��!+�%�f,6�H�`
�)r���Z�ģd1�9��B�s�3l8���#�ҫ0�����f���P4�     