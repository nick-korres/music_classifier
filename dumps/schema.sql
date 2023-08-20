--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: track_attributes; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.track_attributes (
    id integer NOT NULL,
    file_path character varying,
    duration double precision,
    chroma_stft_mean double precision,
    chroma_stft_var double precision,
    rms_mean double precision,
    rms_var double precision,
    spectral_centroid_mean double precision,
    spectral_centroid_var double precision,
    spectral_rolloff_mean double precision,
    spectral_rolloff_var double precision,
    zero_crossing_rate_mean double precision,
    zero_crossing_rate_var double precision,
    harmonic_mean double precision,
    harmonic_var double precision,
    perceptual_weighting_mean double precision,
    perceptual_weighting_var double precision,
    tempo double precision,
    mfcc_mean_1 double precision,
    mfcc_var_1 double precision,
    mfcc_mean_2 double precision,
    mfcc_var_2 double precision,
    mfcc_mean_3 double precision,
    mfcc_var_3 double precision,
    mfcc_mean_4 double precision,
    mfcc_var_4 double precision,
    mfcc_mean_5 double precision,
    mfcc_var_5 double precision,
    mfcc_mean_6 double precision,
    mfcc_var_6 double precision,
    mfcc_mean_7 double precision,
    mfcc_var_7 double precision,
    mfcc_mean_8 double precision,
    mfcc_var_8 double precision,
    mfcc_mean_9 double precision,
    mfcc_var_9 double precision,
    mfcc_mean_10 double precision,
    mfcc_var_10 double precision,
    mfcc_mean_11 double precision,
    mfcc_var_11 double precision,
    mfcc_mean_12 double precision,
    mfcc_var_12 double precision,
    mfcc_mean_13 double precision,
    mfcc_var_13 double precision,
    mfcc_mean_14 double precision,
    mfcc_var_14 double precision,
    mfcc_mean_15 double precision,
    mfcc_var_15 double precision,
    mfcc_mean_16 double precision,
    mfcc_var_16 double precision,
    mfcc_mean_17 double precision,
    mfcc_var_17 double precision,
    mfcc_mean_18 double precision,
    mfcc_var_18 double precision,
    mfcc_mean_19 double precision,
    mfcc_var_19 double precision,
    mfcc_mean_20 double precision,
    mfcc_var_20 double precision,
    label character varying
);


ALTER TABLE public.track_attributes OWNER TO root;

--
-- Name: track_attributes_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.track_attributes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.track_attributes_id_seq OWNER TO root;

--
-- Name: track_attributes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.track_attributes_id_seq OWNED BY public.track_attributes.id;


--
-- Name: track_attributes id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.track_attributes ALTER COLUMN id SET DEFAULT nextval('public.track_attributes_id_seq'::regclass);


--
-- PostgreSQL database dump complete
--

