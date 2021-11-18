--
-- PostgreSQL database dump
--

-- Dumped from database version 10.17 (Debian 10.17-1.pgdg90+1)
-- Dumped by pg_dump version 10.17 (Debian 10.17-1.pgdg90+1)

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

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: admin_event_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.admin_event_entity (
    id character varying(36) NOT NULL,
    admin_event_time bigint,
    realm_id character varying(255),
    operation_type character varying(255),
    auth_realm_id character varying(255),
    auth_client_id character varying(255),
    auth_user_id character varying(255),
    ip_address character varying(255),
    resource_path character varying(2550),
    representation text,
    error character varying(255),
    resource_type character varying(64)
);


ALTER TABLE public.admin_event_entity OWNER TO keycloak;

--
-- Name: associated_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.associated_policy (
    policy_id character varying(36) NOT NULL,
    associated_policy_id character varying(36) NOT NULL
);


ALTER TABLE public.associated_policy OWNER TO keycloak;

--
-- Name: authentication_execution; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authentication_execution (
    id character varying(36) NOT NULL,
    alias character varying(255),
    authenticator character varying(36),
    realm_id character varying(36),
    flow_id character varying(36),
    requirement integer,
    priority integer,
    authenticator_flow boolean DEFAULT false NOT NULL,
    auth_flow_id character varying(36),
    auth_config character varying(36)
);


ALTER TABLE public.authentication_execution OWNER TO keycloak;

--
-- Name: authentication_flow; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authentication_flow (
    id character varying(36) NOT NULL,
    alias character varying(255),
    description character varying(255),
    realm_id character varying(36),
    provider_id character varying(36) DEFAULT 'basic-flow'::character varying NOT NULL,
    top_level boolean DEFAULT false NOT NULL,
    built_in boolean DEFAULT false NOT NULL
);


ALTER TABLE public.authentication_flow OWNER TO keycloak;

--
-- Name: authenticator_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authenticator_config (
    id character varying(36) NOT NULL,
    alias character varying(255),
    realm_id character varying(36)
);


ALTER TABLE public.authenticator_config OWNER TO keycloak;

--
-- Name: authenticator_config_entry; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authenticator_config_entry (
    authenticator_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.authenticator_config_entry OWNER TO keycloak;

--
-- Name: broker_link; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.broker_link (
    identity_provider character varying(255) NOT NULL,
    storage_provider_id character varying(255),
    realm_id character varying(36) NOT NULL,
    broker_user_id character varying(255),
    broker_username character varying(255),
    token text,
    user_id character varying(255) NOT NULL
);


ALTER TABLE public.broker_link OWNER TO keycloak;

--
-- Name: client; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client (
    id character varying(36) NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    full_scope_allowed boolean DEFAULT false NOT NULL,
    client_id character varying(255),
    not_before integer,
    public_client boolean DEFAULT false NOT NULL,
    secret character varying(255),
    base_url character varying(255),
    bearer_only boolean DEFAULT false NOT NULL,
    management_url character varying(255),
    surrogate_auth_required boolean DEFAULT false NOT NULL,
    realm_id character varying(36),
    protocol character varying(255),
    node_rereg_timeout integer DEFAULT 0,
    frontchannel_logout boolean DEFAULT false NOT NULL,
    consent_required boolean DEFAULT false NOT NULL,
    name character varying(255),
    service_accounts_enabled boolean DEFAULT false NOT NULL,
    client_authenticator_type character varying(255),
    root_url character varying(255),
    description character varying(255),
    registration_token character varying(255),
    standard_flow_enabled boolean DEFAULT true NOT NULL,
    implicit_flow_enabled boolean DEFAULT false NOT NULL,
    direct_access_grants_enabled boolean DEFAULT false NOT NULL,
    always_display_in_console boolean DEFAULT false NOT NULL
);


ALTER TABLE public.client OWNER TO keycloak;

--
-- Name: client_attributes; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_attributes (
    client_id character varying(36) NOT NULL,
    value character varying(4000),
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_attributes OWNER TO keycloak;

--
-- Name: client_auth_flow_bindings; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_auth_flow_bindings (
    client_id character varying(36) NOT NULL,
    flow_id character varying(36),
    binding_name character varying(255) NOT NULL
);


ALTER TABLE public.client_auth_flow_bindings OWNER TO keycloak;

--
-- Name: client_initial_access; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_initial_access (
    id character varying(36) NOT NULL,
    realm_id character varying(36) NOT NULL,
    "timestamp" integer,
    expiration integer,
    count integer,
    remaining_count integer
);


ALTER TABLE public.client_initial_access OWNER TO keycloak;

--
-- Name: client_node_registrations; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_node_registrations (
    client_id character varying(36) NOT NULL,
    value integer,
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_node_registrations OWNER TO keycloak;

--
-- Name: client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope (
    id character varying(36) NOT NULL,
    name character varying(255),
    realm_id character varying(36),
    description character varying(255),
    protocol character varying(255)
);


ALTER TABLE public.client_scope OWNER TO keycloak;

--
-- Name: client_scope_attributes; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_attributes (
    scope_id character varying(36) NOT NULL,
    value character varying(2048),
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_scope_attributes OWNER TO keycloak;

--
-- Name: client_scope_client; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_client (
    client_id character varying(255) NOT NULL,
    scope_id character varying(255) NOT NULL,
    default_scope boolean DEFAULT false NOT NULL
);


ALTER TABLE public.client_scope_client OWNER TO keycloak;

--
-- Name: client_scope_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_role_mapping (
    scope_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.client_scope_role_mapping OWNER TO keycloak;

--
-- Name: client_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session (
    id character varying(36) NOT NULL,
    client_id character varying(36),
    redirect_uri character varying(255),
    state character varying(255),
    "timestamp" integer,
    session_id character varying(36),
    auth_method character varying(255),
    realm_id character varying(255),
    auth_user_id character varying(36),
    current_action character varying(36)
);


ALTER TABLE public.client_session OWNER TO keycloak;

--
-- Name: client_session_auth_status; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_auth_status (
    authenticator character varying(36) NOT NULL,
    status integer,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_auth_status OWNER TO keycloak;

--
-- Name: client_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_note (
    name character varying(255) NOT NULL,
    value character varying(255),
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_note OWNER TO keycloak;

--
-- Name: client_session_prot_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_prot_mapper (
    protocol_mapper_id character varying(36) NOT NULL,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_prot_mapper OWNER TO keycloak;

--
-- Name: client_session_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_role (
    role_id character varying(255) NOT NULL,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_role OWNER TO keycloak;

--
-- Name: client_user_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_user_session_note (
    name character varying(255) NOT NULL,
    value character varying(2048),
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_user_session_note OWNER TO keycloak;

--
-- Name: component; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.component (
    id character varying(36) NOT NULL,
    name character varying(255),
    parent_id character varying(36),
    provider_id character varying(36),
    provider_type character varying(255),
    realm_id character varying(36),
    sub_type character varying(255)
);


ALTER TABLE public.component OWNER TO keycloak;

--
-- Name: component_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.component_config (
    id character varying(36) NOT NULL,
    component_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(4000)
);


ALTER TABLE public.component_config OWNER TO keycloak;

--
-- Name: composite_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.composite_role (
    composite character varying(36) NOT NULL,
    child_role character varying(36) NOT NULL
);


ALTER TABLE public.composite_role OWNER TO keycloak;

--
-- Name: credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.credential (
    id character varying(36) NOT NULL,
    salt bytea,
    type character varying(255),
    user_id character varying(36),
    created_date bigint,
    user_label character varying(255),
    secret_data text,
    credential_data text,
    priority integer
);


ALTER TABLE public.credential OWNER TO keycloak;

--
-- Name: databasechangelog; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE public.databasechangelog OWNER TO keycloak;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE public.databasechangeloglock OWNER TO keycloak;

--
-- Name: default_client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.default_client_scope (
    realm_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL,
    default_scope boolean DEFAULT false NOT NULL
);


ALTER TABLE public.default_client_scope OWNER TO keycloak;

--
-- Name: event_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.event_entity (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    details_json character varying(2550),
    error character varying(255),
    ip_address character varying(255),
    realm_id character varying(255),
    session_id character varying(255),
    event_time bigint,
    type character varying(255),
    user_id character varying(255)
);


ALTER TABLE public.event_entity OWNER TO keycloak;

--
-- Name: fed_user_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_attribute (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    value character varying(2024)
);


ALTER TABLE public.fed_user_attribute OWNER TO keycloak;

--
-- Name: fed_user_consent; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_consent (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    created_date bigint,
    last_updated_date bigint,
    client_storage_provider character varying(36),
    external_client_id character varying(255)
);


ALTER TABLE public.fed_user_consent OWNER TO keycloak;

--
-- Name: fed_user_consent_cl_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_consent_cl_scope (
    user_consent_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.fed_user_consent_cl_scope OWNER TO keycloak;

--
-- Name: fed_user_credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_credential (
    id character varying(36) NOT NULL,
    salt bytea,
    type character varying(255),
    created_date bigint,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    user_label character varying(255),
    secret_data text,
    credential_data text,
    priority integer
);


ALTER TABLE public.fed_user_credential OWNER TO keycloak;

--
-- Name: fed_user_group_membership; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_group_membership (
    group_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_group_membership OWNER TO keycloak;

--
-- Name: fed_user_required_action; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_required_action (
    required_action character varying(255) DEFAULT ' '::character varying NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_required_action OWNER TO keycloak;

--
-- Name: fed_user_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_role_mapping (
    role_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_role_mapping OWNER TO keycloak;

--
-- Name: federated_identity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.federated_identity (
    identity_provider character varying(255) NOT NULL,
    realm_id character varying(36),
    federated_user_id character varying(255),
    federated_username character varying(255),
    token text,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.federated_identity OWNER TO keycloak;

--
-- Name: federated_user; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.federated_user (
    id character varying(255) NOT NULL,
    storage_provider_id character varying(255),
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.federated_user OWNER TO keycloak;

--
-- Name: group_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.group_attribute (
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255),
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.group_attribute OWNER TO keycloak;

--
-- Name: group_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.group_role_mapping (
    role_id character varying(36) NOT NULL,
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.group_role_mapping OWNER TO keycloak;

--
-- Name: identity_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider (
    internal_id character varying(36) NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    provider_alias character varying(255),
    provider_id character varying(255),
    store_token boolean DEFAULT false NOT NULL,
    authenticate_by_default boolean DEFAULT false NOT NULL,
    realm_id character varying(36),
    add_token_role boolean DEFAULT true NOT NULL,
    trust_email boolean DEFAULT false NOT NULL,
    first_broker_login_flow_id character varying(36),
    post_broker_login_flow_id character varying(36),
    provider_display_name character varying(255),
    link_only boolean DEFAULT false NOT NULL
);


ALTER TABLE public.identity_provider OWNER TO keycloak;

--
-- Name: identity_provider_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider_config (
    identity_provider_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.identity_provider_config OWNER TO keycloak;

--
-- Name: identity_provider_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    idp_alias character varying(255) NOT NULL,
    idp_mapper_name character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.identity_provider_mapper OWNER TO keycloak;

--
-- Name: idp_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.idp_mapper_config (
    idp_mapper_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.idp_mapper_config OWNER TO keycloak;

--
-- Name: keycloak_group; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.keycloak_group (
    id character varying(36) NOT NULL,
    name character varying(255),
    parent_group character varying(36) NOT NULL,
    realm_id character varying(36)
);


ALTER TABLE public.keycloak_group OWNER TO keycloak;

--
-- Name: keycloak_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.keycloak_role (
    id character varying(36) NOT NULL,
    client_realm_constraint character varying(255),
    client_role boolean DEFAULT false NOT NULL,
    description character varying(255),
    name character varying(255),
    realm_id character varying(255),
    client character varying(36),
    realm character varying(36)
);


ALTER TABLE public.keycloak_role OWNER TO keycloak;

--
-- Name: migration_model; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.migration_model (
    id character varying(36) NOT NULL,
    version character varying(36),
    update_time bigint DEFAULT 0 NOT NULL
);


ALTER TABLE public.migration_model OWNER TO keycloak;

--
-- Name: offline_client_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.offline_client_session (
    user_session_id character varying(36) NOT NULL,
    client_id character varying(255) NOT NULL,
    offline_flag character varying(4) NOT NULL,
    "timestamp" integer,
    data text,
    client_storage_provider character varying(36) DEFAULT 'local'::character varying NOT NULL,
    external_client_id character varying(255) DEFAULT 'local'::character varying NOT NULL
);


ALTER TABLE public.offline_client_session OWNER TO keycloak;

--
-- Name: offline_user_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.offline_user_session (
    user_session_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    created_on integer NOT NULL,
    offline_flag character varying(4) NOT NULL,
    data text,
    last_session_refresh integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.offline_user_session OWNER TO keycloak;

--
-- Name: policy_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.policy_config (
    policy_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value text
);


ALTER TABLE public.policy_config OWNER TO keycloak;

--
-- Name: protocol_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.protocol_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    protocol character varying(255) NOT NULL,
    protocol_mapper_name character varying(255) NOT NULL,
    client_id character varying(36),
    client_scope_id character varying(36)
);


ALTER TABLE public.protocol_mapper OWNER TO keycloak;

--
-- Name: protocol_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.protocol_mapper_config (
    protocol_mapper_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.protocol_mapper_config OWNER TO keycloak;

--
-- Name: realm; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm (
    id character varying(36) NOT NULL,
    access_code_lifespan integer,
    user_action_lifespan integer,
    access_token_lifespan integer,
    account_theme character varying(255),
    admin_theme character varying(255),
    email_theme character varying(255),
    enabled boolean DEFAULT false NOT NULL,
    events_enabled boolean DEFAULT false NOT NULL,
    events_expiration bigint,
    login_theme character varying(255),
    name character varying(255),
    not_before integer,
    password_policy character varying(2550),
    registration_allowed boolean DEFAULT false NOT NULL,
    remember_me boolean DEFAULT false NOT NULL,
    reset_password_allowed boolean DEFAULT false NOT NULL,
    social boolean DEFAULT false NOT NULL,
    ssl_required character varying(255),
    sso_idle_timeout integer,
    sso_max_lifespan integer,
    update_profile_on_soc_login boolean DEFAULT false NOT NULL,
    verify_email boolean DEFAULT false NOT NULL,
    master_admin_client character varying(36),
    login_lifespan integer,
    internationalization_enabled boolean DEFAULT false NOT NULL,
    default_locale character varying(255),
    reg_email_as_username boolean DEFAULT false NOT NULL,
    admin_events_enabled boolean DEFAULT false NOT NULL,
    admin_events_details_enabled boolean DEFAULT false NOT NULL,
    edit_username_allowed boolean DEFAULT false NOT NULL,
    otp_policy_counter integer DEFAULT 0,
    otp_policy_window integer DEFAULT 1,
    otp_policy_period integer DEFAULT 30,
    otp_policy_digits integer DEFAULT 6,
    otp_policy_alg character varying(36) DEFAULT 'HmacSHA1'::character varying,
    otp_policy_type character varying(36) DEFAULT 'totp'::character varying,
    browser_flow character varying(36),
    registration_flow character varying(36),
    direct_grant_flow character varying(36),
    reset_credentials_flow character varying(36),
    client_auth_flow character varying(36),
    offline_session_idle_timeout integer DEFAULT 0,
    revoke_refresh_token boolean DEFAULT false NOT NULL,
    access_token_life_implicit integer DEFAULT 0,
    login_with_email_allowed boolean DEFAULT true NOT NULL,
    duplicate_emails_allowed boolean DEFAULT false NOT NULL,
    docker_auth_flow character varying(36),
    refresh_token_max_reuse integer DEFAULT 0,
    allow_user_managed_access boolean DEFAULT false NOT NULL,
    sso_max_lifespan_remember_me integer DEFAULT 0 NOT NULL,
    sso_idle_timeout_remember_me integer DEFAULT 0 NOT NULL,
    default_role character varying(255)
);


ALTER TABLE public.realm OWNER TO keycloak;

--
-- Name: realm_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_attribute (
    name character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    value text
);


ALTER TABLE public.realm_attribute OWNER TO keycloak;

--
-- Name: realm_default_groups; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_default_groups (
    realm_id character varying(36) NOT NULL,
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_default_groups OWNER TO keycloak;

--
-- Name: realm_enabled_event_types; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_enabled_event_types (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_enabled_event_types OWNER TO keycloak;

--
-- Name: realm_events_listeners; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_events_listeners (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_events_listeners OWNER TO keycloak;

--
-- Name: realm_localizations; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_localizations (
    realm_id character varying(255) NOT NULL,
    locale character varying(255) NOT NULL,
    texts text NOT NULL
);


ALTER TABLE public.realm_localizations OWNER TO keycloak;

--
-- Name: realm_required_credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_required_credential (
    type character varying(255) NOT NULL,
    form_label character varying(255),
    input boolean DEFAULT false NOT NULL,
    secret boolean DEFAULT false NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_required_credential OWNER TO keycloak;

--
-- Name: realm_smtp_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_smtp_config (
    realm_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.realm_smtp_config OWNER TO keycloak;

--
-- Name: realm_supported_locales; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_supported_locales (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_supported_locales OWNER TO keycloak;

--
-- Name: redirect_uris; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.redirect_uris (
    client_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.redirect_uris OWNER TO keycloak;

--
-- Name: required_action_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.required_action_config (
    required_action_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.required_action_config OWNER TO keycloak;

--
-- Name: required_action_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.required_action_provider (
    id character varying(36) NOT NULL,
    alias character varying(255),
    name character varying(255),
    realm_id character varying(36),
    enabled boolean DEFAULT false NOT NULL,
    default_action boolean DEFAULT false NOT NULL,
    provider_id character varying(255),
    priority integer
);


ALTER TABLE public.required_action_provider OWNER TO keycloak;

--
-- Name: resource_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_attribute (
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255),
    resource_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_attribute OWNER TO keycloak;

--
-- Name: resource_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_policy (
    resource_id character varying(36) NOT NULL,
    policy_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_policy OWNER TO keycloak;

--
-- Name: resource_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_scope (
    resource_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_scope OWNER TO keycloak;

--
-- Name: resource_server; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server (
    id character varying(36) NOT NULL,
    allow_rs_remote_mgmt boolean DEFAULT false NOT NULL,
    policy_enforce_mode character varying(15) NOT NULL,
    decision_strategy smallint DEFAULT 1 NOT NULL
);


ALTER TABLE public.resource_server OWNER TO keycloak;

--
-- Name: resource_server_perm_ticket; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_perm_ticket (
    id character varying(36) NOT NULL,
    owner character varying(255) NOT NULL,
    requester character varying(255) NOT NULL,
    created_timestamp bigint NOT NULL,
    granted_timestamp bigint,
    resource_id character varying(36) NOT NULL,
    scope_id character varying(36),
    resource_server_id character varying(36) NOT NULL,
    policy_id character varying(36)
);


ALTER TABLE public.resource_server_perm_ticket OWNER TO keycloak;

--
-- Name: resource_server_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_policy (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(255),
    type character varying(255) NOT NULL,
    decision_strategy character varying(20),
    logic character varying(20),
    resource_server_id character varying(36) NOT NULL,
    owner character varying(255)
);


ALTER TABLE public.resource_server_policy OWNER TO keycloak;

--
-- Name: resource_server_resource; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_resource (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(255),
    icon_uri character varying(255),
    owner character varying(255) NOT NULL,
    resource_server_id character varying(36) NOT NULL,
    owner_managed_access boolean DEFAULT false NOT NULL,
    display_name character varying(255)
);


ALTER TABLE public.resource_server_resource OWNER TO keycloak;

--
-- Name: resource_server_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_scope (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    icon_uri character varying(255),
    resource_server_id character varying(36) NOT NULL,
    display_name character varying(255)
);


ALTER TABLE public.resource_server_scope OWNER TO keycloak;

--
-- Name: resource_uris; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_uris (
    resource_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.resource_uris OWNER TO keycloak;

--
-- Name: role_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.role_attribute (
    id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255)
);


ALTER TABLE public.role_attribute OWNER TO keycloak;

--
-- Name: scope_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.scope_mapping (
    client_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.scope_mapping OWNER TO keycloak;

--
-- Name: scope_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.scope_policy (
    scope_id character varying(36) NOT NULL,
    policy_id character varying(36) NOT NULL
);


ALTER TABLE public.scope_policy OWNER TO keycloak;

--
-- Name: user_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_attribute (
    name character varying(255) NOT NULL,
    value character varying(255),
    user_id character varying(36) NOT NULL,
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL
);


ALTER TABLE public.user_attribute OWNER TO keycloak;

--
-- Name: user_consent; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_consent (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    user_id character varying(36) NOT NULL,
    created_date bigint,
    last_updated_date bigint,
    client_storage_provider character varying(36),
    external_client_id character varying(255)
);


ALTER TABLE public.user_consent OWNER TO keycloak;

--
-- Name: user_consent_client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_consent_client_scope (
    user_consent_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.user_consent_client_scope OWNER TO keycloak;

--
-- Name: user_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_entity (
    id character varying(36) NOT NULL,
    email character varying(255),
    email_constraint character varying(255),
    email_verified boolean DEFAULT false NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    federation_link character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    realm_id character varying(255),
    username character varying(255),
    created_timestamp bigint,
    service_account_client_link character varying(255),
    not_before integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.user_entity OWNER TO keycloak;

--
-- Name: user_federation_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_config (
    user_federation_provider_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.user_federation_config OWNER TO keycloak;

--
-- Name: user_federation_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    federation_provider_id character varying(36) NOT NULL,
    federation_mapper_type character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.user_federation_mapper OWNER TO keycloak;

--
-- Name: user_federation_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_mapper_config (
    user_federation_mapper_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.user_federation_mapper_config OWNER TO keycloak;

--
-- Name: user_federation_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_provider (
    id character varying(36) NOT NULL,
    changed_sync_period integer,
    display_name character varying(255),
    full_sync_period integer,
    last_sync integer,
    priority integer,
    provider_name character varying(255),
    realm_id character varying(36)
);


ALTER TABLE public.user_federation_provider OWNER TO keycloak;

--
-- Name: user_group_membership; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_group_membership (
    group_id character varying(36) NOT NULL,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.user_group_membership OWNER TO keycloak;

--
-- Name: user_required_action; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_required_action (
    user_id character varying(36) NOT NULL,
    required_action character varying(255) DEFAULT ' '::character varying NOT NULL
);


ALTER TABLE public.user_required_action OWNER TO keycloak;

--
-- Name: user_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_role_mapping (
    role_id character varying(255) NOT NULL,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.user_role_mapping OWNER TO keycloak;

--
-- Name: user_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_session (
    id character varying(36) NOT NULL,
    auth_method character varying(255),
    ip_address character varying(255),
    last_session_refresh integer,
    login_username character varying(255),
    realm_id character varying(255),
    remember_me boolean DEFAULT false NOT NULL,
    started integer,
    user_id character varying(255),
    user_session_state integer,
    broker_session_id character varying(255),
    broker_user_id character varying(255)
);


ALTER TABLE public.user_session OWNER TO keycloak;

--
-- Name: user_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_session_note (
    user_session character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(2048)
);


ALTER TABLE public.user_session_note OWNER TO keycloak;

--
-- Name: username_login_failure; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.username_login_failure (
    realm_id character varying(36) NOT NULL,
    username character varying(255) NOT NULL,
    failed_login_not_before integer,
    last_failure bigint,
    last_ip_failure character varying(255),
    num_failures integer
);


ALTER TABLE public.username_login_failure OWNER TO keycloak;

--
-- Name: web_origins; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.web_origins (
    client_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.web_origins OWNER TO keycloak;

--
-- Data for Name: admin_event_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.admin_event_entity (id, admin_event_time, realm_id, operation_type, auth_realm_id, auth_client_id, auth_user_id, ip_address, resource_path, representation, error, resource_type) FROM stdin;
\.


--
-- Data for Name: associated_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.associated_policy (policy_id, associated_policy_id) FROM stdin;
96d81e07-e3f9-4206-88f3-76328cbbb9b8	3fc46920-3046-4423-9851-db767fbee3c7
a29acdd2-e748-4989-88ef-53d5280d664f	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f0aef9d4-46df-472b-8192-fd828046233e	47d172b5-7863-4175-9a62-a77cc63cf3da
35525fd7-3ec7-41c0-9ad4-af6fa1c7243c	47d172b5-7863-4175-9a62-a77cc63cf3da
\.


--
-- Data for Name: authentication_execution; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authentication_execution (id, alias, authenticator, realm_id, flow_id, requirement, priority, authenticator_flow, auth_flow_id, auth_config) FROM stdin;
a543175f-28fd-4915-9314-f49553abef8c	\N	auth-cookie	master	c7352f60-b9e1-47a6-a59b-80fec7a47336	2	10	f	\N	\N
02e9031d-36b0-4fe2-b466-62d95b4facbe	\N	auth-spnego	master	c7352f60-b9e1-47a6-a59b-80fec7a47336	3	20	f	\N	\N
39a9fc47-7b8e-4b82-bab5-0172d0cfd869	\N	identity-provider-redirector	master	c7352f60-b9e1-47a6-a59b-80fec7a47336	2	25	f	\N	\N
ca9a6d02-2c76-4972-beb2-ec4e030a793a	\N	\N	master	c7352f60-b9e1-47a6-a59b-80fec7a47336	2	30	t	56a27abb-fe12-4c9c-82e3-09c857c00cf4	\N
281eb541-eb1e-420f-980e-c580c2e6336b	\N	auth-username-password-form	master	56a27abb-fe12-4c9c-82e3-09c857c00cf4	0	10	f	\N	\N
eb9d59eb-37ce-434e-a167-33dd90227687	\N	direct-grant-validate-username	master	a3a5cfd1-1916-425e-9506-43346acc24d7	0	10	f	\N	\N
86e5493e-6840-493e-8882-7111fe1ea118	\N	direct-grant-validate-password	master	a3a5cfd1-1916-425e-9506-43346acc24d7	0	20	f	\N	\N
26ca69d3-4f24-4bee-8e23-a53918d46a5e	\N	registration-page-form	master	89b8d90b-255a-41b0-80d8-134a3f122410	0	10	t	33b7be4d-5577-4742-92a8-7444e5973e1d	\N
6429bd0c-4d81-4bd1-a6b6-e1a640c8c70f	\N	registration-user-creation	master	33b7be4d-5577-4742-92a8-7444e5973e1d	0	20	f	\N	\N
ea5ecf0c-c448-4646-abe7-3f8a8550e3c7	\N	registration-profile-action	master	33b7be4d-5577-4742-92a8-7444e5973e1d	0	40	f	\N	\N
275e9036-773e-4ad0-8ca9-73681d92bb18	\N	registration-password-action	master	33b7be4d-5577-4742-92a8-7444e5973e1d	0	50	f	\N	\N
a991ce95-c856-4a6d-bfe2-5929803793d3	\N	registration-recaptcha-action	master	33b7be4d-5577-4742-92a8-7444e5973e1d	3	60	f	\N	\N
fc837aaa-b933-45b2-a7b6-5d214671bff8	\N	reset-credentials-choose-user	master	952496b8-a35d-4607-9bb8-773b06d5ddf1	0	10	f	\N	\N
befcc82b-2c83-44c3-997f-d233c98d869e	\N	reset-credential-email	master	952496b8-a35d-4607-9bb8-773b06d5ddf1	0	20	f	\N	\N
49f53ec1-f25c-4264-8fe5-46b607c3be94	\N	reset-password	master	952496b8-a35d-4607-9bb8-773b06d5ddf1	0	30	f	\N	\N
02ffc29c-53f5-4c05-9592-3e622754db57	\N	client-secret	master	92ecb810-75b3-4d42-b661-8b3c30dbed58	2	10	f	\N	\N
c8c6a53f-dd19-4479-80a6-e8d1494450b5	\N	client-jwt	master	92ecb810-75b3-4d42-b661-8b3c30dbed58	2	20	f	\N	\N
810a42c2-4018-4e06-bc3e-5e0dec1ed94f	\N	client-secret-jwt	master	92ecb810-75b3-4d42-b661-8b3c30dbed58	2	30	f	\N	\N
1a985a13-d8e9-4243-8dfe-5b578873cf7f	\N	client-x509	master	92ecb810-75b3-4d42-b661-8b3c30dbed58	2	40	f	\N	\N
cdc5de55-9c03-468e-8322-a6ba5f0434b4	\N	idp-review-profile	master	db140d16-7464-46a4-9851-8492918875aa	0	10	f	\N	bfe1488b-b6a1-4748-b303-cd418714877b
a57a03a5-b344-44e2-b9c5-e9fa3088f646	\N	idp-confirm-link	master	7ecaf696-a7e5-4619-930d-32a2d12a9178	0	10	f	\N	\N
ef2fd14e-a6bc-4969-ae07-996182d78fbc	\N	idp-username-password-form	master	18a2346f-260c-4708-9ad6-a943ffea35cb	0	10	f	\N	\N
a0a56752-634c-43dd-8401-0a4519c689c8	\N	http-basic-authenticator	master	85942ea3-9136-4f04-8ff0-7f85e3d53a5a	0	10	f	\N	\N
f903b101-ae6a-475f-a431-4642acf47060	\N	docker-http-basic-authenticator	master	c6bda705-d01b-4202-804c-e1ee5508f2b7	0	10	f	\N	\N
6a07777e-4bc9-463a-8b97-1a21921bc0be	\N	no-cookie-redirect	master	3484bbb0-fe0f-4a6f-9a0b-68251b5306ea	0	10	f	\N	\N
4c1cb8ce-8fe4-44c6-bd86-455ee763c29f	\N	basic-auth	master	3484bbb0-fe0f-4a6f-9a0b-68251b5306ea	0	20	f	\N	\N
3c701e00-6b49-459f-ab9b-f0cc279b7de1	\N	basic-auth-otp	master	3484bbb0-fe0f-4a6f-9a0b-68251b5306ea	3	30	f	\N	\N
4a0c3ba1-e1b7-4f8d-b8ee-d6e32c5aa608	\N	auth-spnego	master	3484bbb0-fe0f-4a6f-9a0b-68251b5306ea	3	40	f	\N	\N
2b90421b-7bbc-4fd5-adcc-779696ed096c	\N	idp-confirm-link	francoralite	ddb3b086-7699-4de5-9b26-3fb8686ef28c	0	10	f	\N	\N
55368b20-531c-42a7-b37b-68e2798ba946	\N	idp-username-password-form	francoralite	8520a0ab-8df9-4059-b4ea-a79bbb4224f5	0	10	f	\N	\N
7c99918d-a0c2-402c-ada1-e162b52af26f	\N	auth-cookie	francoralite	c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	2	10	f	\N	\N
4ca91f1b-0d1b-458e-8e7c-9f45f9759570	\N	auth-spnego	francoralite	c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	3	20	f	\N	\N
91f2dce1-0939-4515-8d0c-ee5e29d940fd	\N	identity-provider-redirector	francoralite	c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	2	25	f	\N	\N
e525ca1f-c309-42f3-881a-57412d59e2d7	\N	\N	francoralite	c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	2	30	t	02b9d404-9d19-4ae4-8e6b-bb83a48adb74	\N
26da4468-da0c-423a-84f2-4d05312877a9	\N	client-secret	francoralite	88d730bb-34e8-4e93-bf18-ac5a8673d7d9	2	10	f	\N	\N
bdc1aced-5703-43ae-8062-4f7b2100cc81	\N	client-jwt	francoralite	88d730bb-34e8-4e93-bf18-ac5a8673d7d9	2	20	f	\N	\N
6529540d-281d-462e-a345-99b9750a1011	\N	client-secret-jwt	francoralite	88d730bb-34e8-4e93-bf18-ac5a8673d7d9	2	30	f	\N	\N
54f8210d-d07c-4e07-8dde-5c2e6a1eb5f6	\N	client-x509	francoralite	88d730bb-34e8-4e93-bf18-ac5a8673d7d9	2	40	f	\N	\N
1adcc9c5-2c3d-4e11-8eb5-1c730a538e08	\N	direct-grant-validate-username	francoralite	88edf78f-b77c-4538-a2da-50fb89041319	0	10	f	\N	\N
d0881d22-3165-48e7-965a-8568ac76c074	\N	direct-grant-validate-password	francoralite	88edf78f-b77c-4538-a2da-50fb89041319	0	20	f	\N	\N
ff447ef3-8d65-43f4-8b87-cd634d279432	\N	docker-http-basic-authenticator	francoralite	025ef783-6113-46c0-b997-534b69a01a87	0	10	f	\N	\N
8286df84-aaf8-46e5-914e-8805a3d76408	\N	idp-review-profile	francoralite	f899e141-23c4-49ba-8117-297eed468f12	0	10	f	\N	e70c7df6-98bd-4fe8-9c78-b094361cffb8
a001d48c-ea93-465c-b4de-621b154f15ab	\N	auth-username-password-form	francoralite	02b9d404-9d19-4ae4-8e6b-bb83a48adb74	0	10	f	\N	\N
38a73692-1af1-428a-bcd9-c489f73dbe09	\N	no-cookie-redirect	francoralite	409b9107-0742-465c-94e3-2fcde6028410	0	10	f	\N	\N
65168d30-73c7-43cb-bd89-1d8fc71f5dc0	\N	basic-auth	francoralite	409b9107-0742-465c-94e3-2fcde6028410	0	20	f	\N	\N
8137c3f2-d879-400c-9a16-94f759180acb	\N	basic-auth-otp	francoralite	409b9107-0742-465c-94e3-2fcde6028410	3	30	f	\N	\N
afd95141-beeb-4d0f-bcdc-dd64e1d65fae	\N	auth-spnego	francoralite	409b9107-0742-465c-94e3-2fcde6028410	3	40	f	\N	\N
fe506d4b-71ce-4721-aa6d-5bf77a857f26	\N	registration-page-form	francoralite	fb9a5a93-0804-4b67-9805-37e9630c3adc	0	10	t	5342cc78-6057-4833-95ed-36183881dc74	\N
f5d173f2-9e7f-4719-8e66-073ff1ad78ac	\N	registration-user-creation	francoralite	5342cc78-6057-4833-95ed-36183881dc74	0	20	f	\N	\N
4e978261-c7fb-4633-a595-b95e29858d23	\N	registration-profile-action	francoralite	5342cc78-6057-4833-95ed-36183881dc74	0	40	f	\N	\N
998ebcc7-c17c-43d7-b0f5-eb2924dc5c57	\N	registration-password-action	francoralite	5342cc78-6057-4833-95ed-36183881dc74	0	50	f	\N	\N
c6e8943d-1e15-49d8-ab7f-24b513f0bc9d	\N	registration-recaptcha-action	francoralite	5342cc78-6057-4833-95ed-36183881dc74	3	60	f	\N	\N
ae85c706-c5b9-4bae-8e14-1a00704b644f	\N	reset-credentials-choose-user	francoralite	3440df01-ffe2-4734-bd0a-0718162bbb80	0	10	f	\N	\N
d0db892b-9774-4451-9ba8-be11ccd4a63c	\N	reset-credential-email	francoralite	3440df01-ffe2-4734-bd0a-0718162bbb80	0	20	f	\N	\N
d2998674-d084-4a73-b870-8a3def33734f	\N	reset-password	francoralite	3440df01-ffe2-4734-bd0a-0718162bbb80	0	30	f	\N	\N
9a72570e-7d9d-45f5-bf14-e0272d7905a5	\N	http-basic-authenticator	francoralite	7d1b4ecd-8d96-4579-8d61-c06fdfa1ccdd	0	10	f	\N	\N
b5208b62-1aa4-4dcb-b4f4-a243e3474f1a	\N	\N	francoralite	8520a0ab-8df9-4059-b4ea-a79bbb4224f5	1	20	t	8ab226a6-e32a-44bc-873d-23a67876aef7	\N
74ebbdb7-cdd1-494d-a5d5-c44e6122689f	\N	conditional-user-configured	francoralite	8ab226a6-e32a-44bc-873d-23a67876aef7	0	10	f	\N	\N
7e6f4a8e-9496-4a32-88fc-fd8d1166259c	\N	auth-otp-form	francoralite	8ab226a6-e32a-44bc-873d-23a67876aef7	0	20	f	\N	\N
908b8ef5-cedf-4cdc-a425-98571987db47	\N	\N	francoralite	88edf78f-b77c-4538-a2da-50fb89041319	1	30	t	93a1e2bf-190a-4454-b713-8e44fe1dbc35	\N
ce3d6db2-2a94-42a0-a9a1-d2e7170841e6	\N	conditional-user-configured	francoralite	93a1e2bf-190a-4454-b713-8e44fe1dbc35	0	10	f	\N	\N
b68e7d4d-7dfc-41ad-86af-27f965d21262	\N	direct-grant-validate-otp	francoralite	93a1e2bf-190a-4454-b713-8e44fe1dbc35	0	20	f	\N	\N
6f278731-4553-4249-bcc6-5a1dafb540c0	\N	\N	francoralite	02b9d404-9d19-4ae4-8e6b-bb83a48adb74	1	20	t	47356490-a0c6-4c9d-aaa9-ca1d8b789aac	\N
16a4cf6f-3074-41f3-a841-3f7ceb970ce2	\N	conditional-user-configured	francoralite	47356490-a0c6-4c9d-aaa9-ca1d8b789aac	0	10	f	\N	\N
e13fe9a1-f824-4715-8b88-7ae7246477ba	\N	auth-otp-form	francoralite	47356490-a0c6-4c9d-aaa9-ca1d8b789aac	0	20	f	\N	\N
f1461771-c1ca-4be8-b248-8c431cf5830b	\N	\N	francoralite	3440df01-ffe2-4734-bd0a-0718162bbb80	1	40	t	7934b964-8960-4d72-b84d-dbbf633eddc9	\N
8b50d20e-9c42-4ef1-877e-04d48345de7a	\N	conditional-user-configured	francoralite	7934b964-8960-4d72-b84d-dbbf633eddc9	0	10	f	\N	\N
6c38ef74-90f7-477a-a2b7-c4473c9bb3e7	\N	reset-otp	francoralite	7934b964-8960-4d72-b84d-dbbf633eddc9	0	20	f	\N	\N
0504d203-f5ef-48c4-b789-7f322ba5cc97	\N	\N	master	56a27abb-fe12-4c9c-82e3-09c857c00cf4	1	20	t	33e580fa-9abd-42fb-9fb9-b5e6d52b37ee	\N
4716f620-66ff-4709-9628-de26c32250e6	\N	conditional-user-configured	master	33e580fa-9abd-42fb-9fb9-b5e6d52b37ee	0	10	f	\N	\N
cb92485f-96b7-4234-9ed3-51524ad1dccf	\N	auth-otp-form	master	33e580fa-9abd-42fb-9fb9-b5e6d52b37ee	0	20	f	\N	\N
426817b5-1637-42a8-89be-608664fd7d99	\N	\N	master	a3a5cfd1-1916-425e-9506-43346acc24d7	1	30	t	28cb0741-5838-4bbe-949b-0d570015074f	\N
2e938611-3dae-4d5a-a4db-7c026085d9b1	\N	conditional-user-configured	master	28cb0741-5838-4bbe-949b-0d570015074f	0	10	f	\N	\N
bfebe7ec-f9db-49cb-b4fa-7240f35c3ce3	\N	direct-grant-validate-otp	master	28cb0741-5838-4bbe-949b-0d570015074f	0	20	f	\N	\N
64822e10-bfb9-4bf7-a63b-0852c1f8e055	\N	\N	master	952496b8-a35d-4607-9bb8-773b06d5ddf1	1	40	t	fae77bff-c982-4724-9f94-716855a1965a	\N
e5f599c6-b881-4115-bde4-b3b5bd8d5ba2	\N	conditional-user-configured	master	fae77bff-c982-4724-9f94-716855a1965a	0	10	f	\N	\N
2f249a77-f001-493f-8c86-2c9ad1c554c1	\N	reset-otp	master	fae77bff-c982-4724-9f94-716855a1965a	0	20	f	\N	\N
50af2ac9-7673-4138-9261-62d166b31e5e	\N	\N	master	18a2346f-260c-4708-9ad6-a943ffea35cb	1	20	t	53c6bf9b-45b7-40eb-9930-bbf5af49a0f9	\N
91214533-5443-4ead-8f9e-6eab2b7177bb	\N	conditional-user-configured	master	53c6bf9b-45b7-40eb-9930-bbf5af49a0f9	0	10	f	\N	\N
63a5b2be-5e67-42f0-b2f1-6f3e1449fe61	\N	auth-otp-form	master	53c6bf9b-45b7-40eb-9930-bbf5af49a0f9	0	20	f	\N	\N
2abbc84f-9acc-4d41-86b8-aa6d8358a0db	\N	\N	francoralite	ddb3b086-7699-4de5-9b26-3fb8686ef28c	0	20	t	0884c6d7-77e8-46b9-af1c-53502ec21b41	\N
5940c3fe-a110-4797-96a4-fa541cfd3883	\N	idp-email-verification	francoralite	0884c6d7-77e8-46b9-af1c-53502ec21b41	2	10	f	\N	\N
880d3cbd-3c3a-49fa-8d5f-0ad40e8863ff	\N	\N	francoralite	0884c6d7-77e8-46b9-af1c-53502ec21b41	2	20	t	8520a0ab-8df9-4059-b4ea-a79bbb4224f5	\N
6882c641-0b57-42ec-b34e-ca1fb4c8fd68	\N	\N	francoralite	f899e141-23c4-49ba-8117-297eed468f12	0	20	t	29a55cbb-0c66-4f98-a0d3-b2e5d3cd9388	\N
8fb7ee18-4299-4fc1-bbe3-bec3a658bd11	\N	idp-create-user-if-unique	francoralite	29a55cbb-0c66-4f98-a0d3-b2e5d3cd9388	2	10	f	\N	0b36019e-b350-4008-81f9-a9f41940749d
f17310a0-9789-460d-9860-20d70750367a	\N	\N	francoralite	29a55cbb-0c66-4f98-a0d3-b2e5d3cd9388	2	20	t	ddb3b086-7699-4de5-9b26-3fb8686ef28c	\N
5378872b-a258-4a7d-86c7-f7546a73793b	\N	\N	master	db140d16-7464-46a4-9851-8492918875aa	0	20	t	87daa40a-f8d9-4818-8eee-0dbad261c18c	\N
ff5189da-dc5f-4e24-9629-df820c4a94d4	\N	idp-create-user-if-unique	master	87daa40a-f8d9-4818-8eee-0dbad261c18c	2	10	f	\N	9199d8c1-8251-486c-b773-d4bbc41590d9
57684141-665b-46cd-a4bd-a11b7a6f7be2	\N	\N	master	87daa40a-f8d9-4818-8eee-0dbad261c18c	2	20	t	7ecaf696-a7e5-4619-930d-32a2d12a9178	\N
4e7d9d40-5fbd-4218-8db9-a2c6309ff64e	\N	\N	master	7ecaf696-a7e5-4619-930d-32a2d12a9178	0	20	t	63e7d27f-b5ab-426f-8682-e787efdf5d4a	\N
0838ce72-1bd3-4736-8298-e00f2241a038	\N	idp-email-verification	master	63e7d27f-b5ab-426f-8682-e787efdf5d4a	2	10	f	\N	\N
b7dcde7e-8d7e-4e6b-8a15-beb4ef3aaf7c	\N	\N	master	63e7d27f-b5ab-426f-8682-e787efdf5d4a	2	20	t	18a2346f-260c-4708-9ad6-a943ffea35cb	\N
\.


--
-- Data for Name: authentication_flow; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authentication_flow (id, alias, description, realm_id, provider_id, top_level, built_in) FROM stdin;
c7352f60-b9e1-47a6-a59b-80fec7a47336	browser	browser based authentication	master	basic-flow	t	t
56a27abb-fe12-4c9c-82e3-09c857c00cf4	forms	Username, password, otp and other auth forms.	master	basic-flow	f	t
a3a5cfd1-1916-425e-9506-43346acc24d7	direct grant	OpenID Connect Resource Owner Grant	master	basic-flow	t	t
89b8d90b-255a-41b0-80d8-134a3f122410	registration	registration flow	master	basic-flow	t	t
33b7be4d-5577-4742-92a8-7444e5973e1d	registration form	registration form	master	form-flow	f	t
952496b8-a35d-4607-9bb8-773b06d5ddf1	reset credentials	Reset credentials for a user if they forgot their password or something	master	basic-flow	t	t
92ecb810-75b3-4d42-b661-8b3c30dbed58	clients	Base authentication for clients	master	client-flow	t	t
db140d16-7464-46a4-9851-8492918875aa	first broker login	Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account	master	basic-flow	t	t
7ecaf696-a7e5-4619-930d-32a2d12a9178	Handle Existing Account	Handle what to do if there is existing account with same email/username like authenticated identity provider	master	basic-flow	f	t
18a2346f-260c-4708-9ad6-a943ffea35cb	Verify Existing Account by Re-authentication	Reauthentication of existing account	master	basic-flow	f	t
85942ea3-9136-4f04-8ff0-7f85e3d53a5a	saml ecp	SAML ECP Profile Authentication Flow	master	basic-flow	t	t
c6bda705-d01b-4202-804c-e1ee5508f2b7	docker auth	Used by Docker clients to authenticate against the IDP	master	basic-flow	t	t
3484bbb0-fe0f-4a6f-9a0b-68251b5306ea	http challenge	An authentication flow based on challenge-response HTTP Authentication Schemes	master	basic-flow	t	t
ddb3b086-7699-4de5-9b26-3fb8686ef28c	Handle Existing Account	Handle what to do if there is existing account with same email/username like authenticated identity provider	francoralite	basic-flow	f	t
8520a0ab-8df9-4059-b4ea-a79bbb4224f5	Verify Existing Account by Re-authentication	Reauthentication of existing account	francoralite	basic-flow	f	t
c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	browser	browser based authentication	francoralite	basic-flow	t	t
88d730bb-34e8-4e93-bf18-ac5a8673d7d9	clients	Base authentication for clients	francoralite	client-flow	t	t
88edf78f-b77c-4538-a2da-50fb89041319	direct grant	OpenID Connect Resource Owner Grant	francoralite	basic-flow	t	t
025ef783-6113-46c0-b997-534b69a01a87	docker auth	Used by Docker clients to authenticate against the IDP	francoralite	basic-flow	t	t
f899e141-23c4-49ba-8117-297eed468f12	first broker login	Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account	francoralite	basic-flow	t	t
02b9d404-9d19-4ae4-8e6b-bb83a48adb74	forms	Username, password, otp and other auth forms.	francoralite	basic-flow	f	t
409b9107-0742-465c-94e3-2fcde6028410	http challenge	An authentication flow based on challenge-response HTTP Authentication Schemes	francoralite	basic-flow	t	t
fb9a5a93-0804-4b67-9805-37e9630c3adc	registration	registration flow	francoralite	basic-flow	t	t
5342cc78-6057-4833-95ed-36183881dc74	registration form	registration form	francoralite	form-flow	f	t
3440df01-ffe2-4734-bd0a-0718162bbb80	reset credentials	Reset credentials for a user if they forgot their password or something	francoralite	basic-flow	t	t
7d1b4ecd-8d96-4579-8d61-c06fdfa1ccdd	saml ecp	SAML ECP Profile Authentication Flow	francoralite	basic-flow	t	t
8ab226a6-e32a-44bc-873d-23a67876aef7	Verify Existing Account by Re-authentication - auth-otp-form - Conditional	Flow to determine if the auth-otp-form authenticator should be used or not.	francoralite	basic-flow	f	t
93a1e2bf-190a-4454-b713-8e44fe1dbc35	direct grant - direct-grant-validate-otp - Conditional	Flow to determine if the direct-grant-validate-otp authenticator should be used or not.	francoralite	basic-flow	f	t
47356490-a0c6-4c9d-aaa9-ca1d8b789aac	forms - auth-otp-form - Conditional	Flow to determine if the auth-otp-form authenticator should be used or not.	francoralite	basic-flow	f	t
7934b964-8960-4d72-b84d-dbbf633eddc9	reset credentials - reset-otp - Conditional	Flow to determine if the reset-otp authenticator should be used or not.	francoralite	basic-flow	f	t
33e580fa-9abd-42fb-9fb9-b5e6d52b37ee	forms - auth-otp-form - Conditional	Flow to determine if the auth-otp-form authenticator should be used or not.	master	basic-flow	f	t
28cb0741-5838-4bbe-949b-0d570015074f	direct grant - direct-grant-validate-otp - Conditional	Flow to determine if the direct-grant-validate-otp authenticator should be used or not.	master	basic-flow	f	t
fae77bff-c982-4724-9f94-716855a1965a	reset credentials - reset-otp - Conditional	Flow to determine if the reset-otp authenticator should be used or not.	master	basic-flow	f	t
53c6bf9b-45b7-40eb-9930-bbf5af49a0f9	Verify Existing Account by Re-authentication - auth-otp-form - Conditional	Flow to determine if the auth-otp-form authenticator should be used or not.	master	basic-flow	f	t
0884c6d7-77e8-46b9-af1c-53502ec21b41	Handle Existing Account - Alternatives - 0	Subflow of Handle Existing Account with alternative executions	francoralite	basic-flow	f	t
29a55cbb-0c66-4f98-a0d3-b2e5d3cd9388	first broker login - Alternatives - 0	Subflow of first broker login with alternative executions	francoralite	basic-flow	f	t
87daa40a-f8d9-4818-8eee-0dbad261c18c	first broker login - Alternatives - 0	Subflow of first broker login with alternative executions	master	basic-flow	f	t
63e7d27f-b5ab-426f-8682-e787efdf5d4a	Handle Existing Account - Alternatives - 0	Subflow of Handle Existing Account with alternative executions	master	basic-flow	f	t
\.


--
-- Data for Name: authenticator_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authenticator_config (id, alias, realm_id) FROM stdin;
bfe1488b-b6a1-4748-b303-cd418714877b	review profile config	master
9199d8c1-8251-486c-b773-d4bbc41590d9	create unique user config	master
0b36019e-b350-4008-81f9-a9f41940749d	create unique user config	francoralite
e70c7df6-98bd-4fe8-9c78-b094361cffb8	review profile config	francoralite
\.


--
-- Data for Name: authenticator_config_entry; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authenticator_config_entry (authenticator_id, value, name) FROM stdin;
bfe1488b-b6a1-4748-b303-cd418714877b	missing	update.profile.on.first.login
9199d8c1-8251-486c-b773-d4bbc41590d9	false	require.password.update.after.registration
0b36019e-b350-4008-81f9-a9f41940749d	false	require.password.update.after.registration
e70c7df6-98bd-4fe8-9c78-b094361cffb8	missing	update.profile.on.first.login
\.


--
-- Data for Name: broker_link; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.broker_link (identity_provider, storage_provider_id, realm_id, broker_user_id, broker_username, token, user_id) FROM stdin;
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client (id, enabled, full_scope_allowed, client_id, not_before, public_client, secret, base_url, bearer_only, management_url, surrogate_auth_required, realm_id, protocol, node_rereg_timeout, frontchannel_logout, consent_required, name, service_accounts_enabled, client_authenticator_type, root_url, description, registration_token, standard_flow_enabled, implicit_flow_enabled, direct_access_grants_enabled, always_display_in_console) FROM stdin;
9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	t	master-realm	0	f	2e4abc6c-1610-4238-a1b4-749df7fd72ed	\N	t	\N	f	master	\N	0	f	f	master Realm	f	client-secret	\N	\N	\N	t	f	f	f
d91bc61c-3f73-4e3a-add6-55fc753a31ec	t	f	broker	0	f	5da545d1-e0cb-4458-9fe1-7344f87043e5	\N	f	\N	f	master	openid-connect	0	f	f	${client_broker}	f	client-secret	\N	\N	\N	t	f	f	f
c7c3433f-faa6-45b8-a353-bdb6635cea0c	t	f	admin-cli	0	t	e76c570e-c190-4231-90c9-1a2c12cfe50c	\N	f	\N	f	master	openid-connect	0	f	f	${client_admin-cli}	f	client-secret	\N	\N	\N	f	f	t	f
ac6a2e53-830b-44ee-8fc0-775bb105330d	t	t	francoralite-realm	0	f	e1a184aa-9c71-4627-9db3-b86c93909466	\N	t	\N	f	master	\N	0	f	f	francoralite Realm	f	client-secret	\N	\N	\N	t	f	f	f
e8efb165-82f9-405c-98aa-e8535badd8ad	t	f	broker	0	f	**********	\N	f	\N	f	francoralite	openid-connect	0	f	f	${client_broker}	f	client-secret	\N	\N	\N	t	f	f	f
d2805f14-3eeb-490f-b559-eb0ad43364f9	t	f	realm-management	0	f	**********	\N	t	\N	f	francoralite	openid-connect	0	f	f	${client_realm-management}	f	client-secret	\N	\N	\N	t	f	f	f
6ca8b749-cba1-4453-8a20-0c189d9b9447	t	f	francoralite	0	f	557ef7aa-7100-411a-9305-5f19827872aa	http://nginx.francoralite.localhost:8080/	f	\N	f	francoralite	openid-connect	-1	f	f	Francoralite API	t	client-secret	http://nginx.francoralite.localhost:8080/	\N	\N	t	t	t	f
5def7547-cfd3-4473-946c-35f796c52df4	t	f	security-admin-console	0	t	**********	/admin/francoralite/console/	f	\N	f	francoralite	openid-connect	0	f	f	${client_security-admin-console}	f	client-secret	${authAdminUrl}	\N	\N	t	f	f	f
f896f42d-66e6-498f-bdc0-a90216659041	t	f	account	0	f	**********	/realms/francoralite/account/	f	\N	f	francoralite	openid-connect	0	f	f	${client_account}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	t	f	security-admin-console	0	t	4db5c283-ebce-4846-96d5-c9373cbbe225	/admin/master/console/	f	\N	f	master	openid-connect	0	f	f	${client_security-admin-console}	f	client-secret	${authAdminUrl}	\N	\N	t	f	f	f
310aabaf-651c-4959-b441-8fe27129a418	t	f	account	0	f	930fef10-4c9f-4ec7-9702-180eaee6160e	/realms/master/account/	f	\N	f	master	openid-connect	0	f	f	${client_account}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
dda53ff1-c096-4601-8a8c-30365fde853d	t	f	account-console	0	t	\N	/realms/francoralite/account/	f	\N	f	francoralite	openid-connect	0	f	f	${client_account-console}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
c041d458-ff12-4534-bcb0-cef6017935ab	t	f	account-console	0	t	\N	/realms/master/account/	f	\N	f	master	openid-connect	0	f	f	${client_account-console}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
4a71088e-ce91-4ba2-9887-c5558a7a1674	t	f	admin-cli	0	t	\N	\N	f	\N	f	francoralite	openid-connect	0	f	f	${client_admin-cli}	f	client-secret	\N	\N	\N	f	f	t	f
\.


--
-- Data for Name: client_attributes; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_attributes (client_id, value, name) FROM stdin;
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.assertion.signature
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.force.post.binding
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.multivalued.roles
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.encrypt
6ca8b749-cba1-4453-8a20-0c189d9b9447	keycloak	login_theme
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.server.signature
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.server.signature.keyinfo.ext
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	exclude.session.state.from.auth.response
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml_force_name_id_format
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.client.signature
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	tls.client.certificate.bound.access.tokens
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.authnstatement
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	display.on.consent.screen
6ca8b749-cba1-4453-8a20-0c189d9b9447	false	saml.onetimeuse.condition
5def7547-cfd3-4473-946c-35f796c52df4	S256	pkce.code.challenge.method
dda53ff1-c096-4601-8a8c-30365fde853d	S256	pkce.code.challenge.method
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	S256	pkce.code.challenge.method
c041d458-ff12-4534-bcb0-cef6017935ab	S256	pkce.code.challenge.method
\.


--
-- Data for Name: client_auth_flow_bindings; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_auth_flow_bindings (client_id, flow_id, binding_name) FROM stdin;
\.


--
-- Data for Name: client_initial_access; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_initial_access (id, realm_id, "timestamp", expiration, count, remaining_count) FROM stdin;
\.


--
-- Data for Name: client_node_registrations; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_node_registrations (client_id, value, name) FROM stdin;
\.


--
-- Data for Name: client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope (id, name, realm_id, description, protocol) FROM stdin;
01d946a1-1cbe-4115-baa3-f318f98063cc	offline_access	master	OpenID Connect built-in scope: offline_access	openid-connect
ff5789c8-4bb4-44c4-885f-a68d50e376ee	role_list	master	SAML role list	saml
dca376d8-cb66-4f66-a8eb-982b522bf009	profile	master	OpenID Connect built-in scope: profile	openid-connect
43c711ac-8d05-4374-962e-994721d09c71	email	master	OpenID Connect built-in scope: email	openid-connect
0c44a86a-d544-4d25-93ed-bb5f3cde8f08	address	master	OpenID Connect built-in scope: address	openid-connect
95d9bce2-c1e5-49a9-8071-2a79b5489b44	phone	master	OpenID Connect built-in scope: phone	openid-connect
ae3e0992-298c-42b0-bda3-c4671c460581	roles	master	OpenID Connect scope for add user roles to the access token	openid-connect
b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	web-origins	master	OpenID Connect scope for add allowed web origins to the access token	openid-connect
6b2ca845-56e5-456b-aa30-d582da23dc7f	offline_access	francoralite	OpenID Connect built-in scope: offline_access	openid-connect
2b4e74c3-c90b-4ea1-b5b5-dfb820147896	role_list	francoralite	SAML role list	saml
2bac4725-31a5-4315-bd97-562b7c764e2c	profile	francoralite	OpenID Connect built-in scope: profile	openid-connect
959efe5f-5b43-4d64-90f9-f52dda2eb527	email	francoralite	OpenID Connect built-in scope: email	openid-connect
a1274aaa-071f-46ae-bd24-807227b4a2c6	address	francoralite	OpenID Connect built-in scope: address	openid-connect
4cef35b9-dbad-41c5-b76c-448c12b35cea	phone	francoralite	OpenID Connect built-in scope: phone	openid-connect
0630fe1b-3718-401b-9aeb-5f4530d97637	roles	francoralite	OpenID Connect scope for add user roles to the access token	openid-connect
34ad7985-88ba-405d-a0ad-12ec0a905b8a	web-origins	francoralite	OpenID Connect scope for add allowed web origins to the access token	openid-connect
b9996171-4af7-4c35-be93-8b799022b095	microprofile-jwt	francoralite	Microprofile - JWT built-in scope	openid-connect
b6429998-dfca-4d5b-a0ca-300fcfa243ed	microprofile-jwt	master	Microprofile - JWT built-in scope	openid-connect
\.


--
-- Data for Name: client_scope_attributes; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_attributes (scope_id, value, name) FROM stdin;
01d946a1-1cbe-4115-baa3-f318f98063cc	true	display.on.consent.screen
01d946a1-1cbe-4115-baa3-f318f98063cc	${offlineAccessScopeConsentText}	consent.screen.text
ff5789c8-4bb4-44c4-885f-a68d50e376ee	true	display.on.consent.screen
ff5789c8-4bb4-44c4-885f-a68d50e376ee	${samlRoleListScopeConsentText}	consent.screen.text
dca376d8-cb66-4f66-a8eb-982b522bf009	true	display.on.consent.screen
dca376d8-cb66-4f66-a8eb-982b522bf009	${profileScopeConsentText}	consent.screen.text
dca376d8-cb66-4f66-a8eb-982b522bf009	true	include.in.token.scope
43c711ac-8d05-4374-962e-994721d09c71	true	display.on.consent.screen
43c711ac-8d05-4374-962e-994721d09c71	${emailScopeConsentText}	consent.screen.text
43c711ac-8d05-4374-962e-994721d09c71	true	include.in.token.scope
0c44a86a-d544-4d25-93ed-bb5f3cde8f08	true	display.on.consent.screen
0c44a86a-d544-4d25-93ed-bb5f3cde8f08	${addressScopeConsentText}	consent.screen.text
0c44a86a-d544-4d25-93ed-bb5f3cde8f08	true	include.in.token.scope
95d9bce2-c1e5-49a9-8071-2a79b5489b44	true	display.on.consent.screen
95d9bce2-c1e5-49a9-8071-2a79b5489b44	${phoneScopeConsentText}	consent.screen.text
95d9bce2-c1e5-49a9-8071-2a79b5489b44	true	include.in.token.scope
ae3e0992-298c-42b0-bda3-c4671c460581	true	display.on.consent.screen
ae3e0992-298c-42b0-bda3-c4671c460581	${rolesScopeConsentText}	consent.screen.text
ae3e0992-298c-42b0-bda3-c4671c460581	false	include.in.token.scope
b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	false	display.on.consent.screen
b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9		consent.screen.text
b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	false	include.in.token.scope
6b2ca845-56e5-456b-aa30-d582da23dc7f	${offlineAccessScopeConsentText}	consent.screen.text
6b2ca845-56e5-456b-aa30-d582da23dc7f	true	display.on.consent.screen
2b4e74c3-c90b-4ea1-b5b5-dfb820147896	${samlRoleListScopeConsentText}	consent.screen.text
2b4e74c3-c90b-4ea1-b5b5-dfb820147896	true	display.on.consent.screen
2bac4725-31a5-4315-bd97-562b7c764e2c	true	include.in.token.scope
2bac4725-31a5-4315-bd97-562b7c764e2c	true	display.on.consent.screen
2bac4725-31a5-4315-bd97-562b7c764e2c	${profileScopeConsentText}	consent.screen.text
959efe5f-5b43-4d64-90f9-f52dda2eb527	true	include.in.token.scope
959efe5f-5b43-4d64-90f9-f52dda2eb527	true	display.on.consent.screen
959efe5f-5b43-4d64-90f9-f52dda2eb527	${emailScopeConsentText}	consent.screen.text
a1274aaa-071f-46ae-bd24-807227b4a2c6	true	include.in.token.scope
a1274aaa-071f-46ae-bd24-807227b4a2c6	true	display.on.consent.screen
a1274aaa-071f-46ae-bd24-807227b4a2c6	${addressScopeConsentText}	consent.screen.text
4cef35b9-dbad-41c5-b76c-448c12b35cea	true	include.in.token.scope
4cef35b9-dbad-41c5-b76c-448c12b35cea	true	display.on.consent.screen
4cef35b9-dbad-41c5-b76c-448c12b35cea	${phoneScopeConsentText}	consent.screen.text
0630fe1b-3718-401b-9aeb-5f4530d97637	true	display.on.consent.screen
0630fe1b-3718-401b-9aeb-5f4530d97637	${rolesScopeConsentText}	consent.screen.text
34ad7985-88ba-405d-a0ad-12ec0a905b8a	false	include.in.token.scope
34ad7985-88ba-405d-a0ad-12ec0a905b8a	false	display.on.consent.screen
34ad7985-88ba-405d-a0ad-12ec0a905b8a		consent.screen.text
b9996171-4af7-4c35-be93-8b799022b095	false	display.on.consent.screen
b9996171-4af7-4c35-be93-8b799022b095	true	include.in.token.scope
b6429998-dfca-4d5b-a0ca-300fcfa243ed	false	display.on.consent.screen
b6429998-dfca-4d5b-a0ca-300fcfa243ed	true	include.in.token.scope
0630fe1b-3718-401b-9aeb-5f4530d97637	true	include.in.token.scope
\.


--
-- Data for Name: client_scope_client; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_client (client_id, scope_id, default_scope) FROM stdin;
310aabaf-651c-4959-b441-8fe27129a418	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
c7c3433f-faa6-45b8-a353-bdb6635cea0c	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
d91bc61c-3f73-4e3a-add6-55fc753a31ec	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
9b3d814d-33ff-45fd-9f13-a489b550ae9e	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
310aabaf-651c-4959-b441-8fe27129a418	dca376d8-cb66-4f66-a8eb-982b522bf009	t
310aabaf-651c-4959-b441-8fe27129a418	43c711ac-8d05-4374-962e-994721d09c71	t
310aabaf-651c-4959-b441-8fe27129a418	ae3e0992-298c-42b0-bda3-c4671c460581	t
310aabaf-651c-4959-b441-8fe27129a418	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
310aabaf-651c-4959-b441-8fe27129a418	01d946a1-1cbe-4115-baa3-f318f98063cc	f
310aabaf-651c-4959-b441-8fe27129a418	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
310aabaf-651c-4959-b441-8fe27129a418	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
c7c3433f-faa6-45b8-a353-bdb6635cea0c	dca376d8-cb66-4f66-a8eb-982b522bf009	t
c7c3433f-faa6-45b8-a353-bdb6635cea0c	43c711ac-8d05-4374-962e-994721d09c71	t
c7c3433f-faa6-45b8-a353-bdb6635cea0c	ae3e0992-298c-42b0-bda3-c4671c460581	t
c7c3433f-faa6-45b8-a353-bdb6635cea0c	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
c7c3433f-faa6-45b8-a353-bdb6635cea0c	01d946a1-1cbe-4115-baa3-f318f98063cc	f
c7c3433f-faa6-45b8-a353-bdb6635cea0c	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
c7c3433f-faa6-45b8-a353-bdb6635cea0c	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
d91bc61c-3f73-4e3a-add6-55fc753a31ec	dca376d8-cb66-4f66-a8eb-982b522bf009	t
d91bc61c-3f73-4e3a-add6-55fc753a31ec	43c711ac-8d05-4374-962e-994721d09c71	t
d91bc61c-3f73-4e3a-add6-55fc753a31ec	ae3e0992-298c-42b0-bda3-c4671c460581	t
d91bc61c-3f73-4e3a-add6-55fc753a31ec	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
d91bc61c-3f73-4e3a-add6-55fc753a31ec	01d946a1-1cbe-4115-baa3-f318f98063cc	f
d91bc61c-3f73-4e3a-add6-55fc753a31ec	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
d91bc61c-3f73-4e3a-add6-55fc753a31ec	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
9b3d814d-33ff-45fd-9f13-a489b550ae9e	dca376d8-cb66-4f66-a8eb-982b522bf009	t
9b3d814d-33ff-45fd-9f13-a489b550ae9e	43c711ac-8d05-4374-962e-994721d09c71	t
9b3d814d-33ff-45fd-9f13-a489b550ae9e	ae3e0992-298c-42b0-bda3-c4671c460581	t
9b3d814d-33ff-45fd-9f13-a489b550ae9e	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
9b3d814d-33ff-45fd-9f13-a489b550ae9e	01d946a1-1cbe-4115-baa3-f318f98063cc	f
9b3d814d-33ff-45fd-9f13-a489b550ae9e	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
9b3d814d-33ff-45fd-9f13-a489b550ae9e	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	dca376d8-cb66-4f66-a8eb-982b522bf009	t
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	43c711ac-8d05-4374-962e-994721d09c71	t
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	ae3e0992-298c-42b0-bda3-c4671c460581	t
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	01d946a1-1cbe-4115-baa3-f318f98063cc	f
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
ac6a2e53-830b-44ee-8fc0-775bb105330d	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
ac6a2e53-830b-44ee-8fc0-775bb105330d	dca376d8-cb66-4f66-a8eb-982b522bf009	t
ac6a2e53-830b-44ee-8fc0-775bb105330d	43c711ac-8d05-4374-962e-994721d09c71	t
ac6a2e53-830b-44ee-8fc0-775bb105330d	ae3e0992-298c-42b0-bda3-c4671c460581	t
ac6a2e53-830b-44ee-8fc0-775bb105330d	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
ac6a2e53-830b-44ee-8fc0-775bb105330d	01d946a1-1cbe-4115-baa3-f318f98063cc	f
ac6a2e53-830b-44ee-8fc0-775bb105330d	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
ac6a2e53-830b-44ee-8fc0-775bb105330d	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
e8efb165-82f9-405c-98aa-e8535badd8ad	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
e8efb165-82f9-405c-98aa-e8535badd8ad	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
e8efb165-82f9-405c-98aa-e8535badd8ad	2bac4725-31a5-4315-bd97-562b7c764e2c	t
e8efb165-82f9-405c-98aa-e8535badd8ad	0630fe1b-3718-401b-9aeb-5f4530d97637	t
e8efb165-82f9-405c-98aa-e8535badd8ad	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
e8efb165-82f9-405c-98aa-e8535badd8ad	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
e8efb165-82f9-405c-98aa-e8535badd8ad	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
e8efb165-82f9-405c-98aa-e8535badd8ad	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
d2805f14-3eeb-490f-b559-eb0ad43364f9	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
d2805f14-3eeb-490f-b559-eb0ad43364f9	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
d2805f14-3eeb-490f-b559-eb0ad43364f9	2bac4725-31a5-4315-bd97-562b7c764e2c	t
d2805f14-3eeb-490f-b559-eb0ad43364f9	0630fe1b-3718-401b-9aeb-5f4530d97637	t
d2805f14-3eeb-490f-b559-eb0ad43364f9	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
d2805f14-3eeb-490f-b559-eb0ad43364f9	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
d2805f14-3eeb-490f-b559-eb0ad43364f9	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
d2805f14-3eeb-490f-b559-eb0ad43364f9	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
f896f42d-66e6-498f-bdc0-a90216659041	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
f896f42d-66e6-498f-bdc0-a90216659041	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
f896f42d-66e6-498f-bdc0-a90216659041	2bac4725-31a5-4315-bd97-562b7c764e2c	t
f896f42d-66e6-498f-bdc0-a90216659041	0630fe1b-3718-401b-9aeb-5f4530d97637	t
f896f42d-66e6-498f-bdc0-a90216659041	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
f896f42d-66e6-498f-bdc0-a90216659041	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
f896f42d-66e6-498f-bdc0-a90216659041	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
f896f42d-66e6-498f-bdc0-a90216659041	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
5def7547-cfd3-4473-946c-35f796c52df4	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
5def7547-cfd3-4473-946c-35f796c52df4	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
5def7547-cfd3-4473-946c-35f796c52df4	2bac4725-31a5-4315-bd97-562b7c764e2c	t
5def7547-cfd3-4473-946c-35f796c52df4	0630fe1b-3718-401b-9aeb-5f4530d97637	t
5def7547-cfd3-4473-946c-35f796c52df4	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
5def7547-cfd3-4473-946c-35f796c52df4	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
5def7547-cfd3-4473-946c-35f796c52df4	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
5def7547-cfd3-4473-946c-35f796c52df4	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
4a71088e-ce91-4ba2-9887-c5558a7a1674	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
4a71088e-ce91-4ba2-9887-c5558a7a1674	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
4a71088e-ce91-4ba2-9887-c5558a7a1674	2bac4725-31a5-4315-bd97-562b7c764e2c	t
4a71088e-ce91-4ba2-9887-c5558a7a1674	0630fe1b-3718-401b-9aeb-5f4530d97637	t
4a71088e-ce91-4ba2-9887-c5558a7a1674	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
4a71088e-ce91-4ba2-9887-c5558a7a1674	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
4a71088e-ce91-4ba2-9887-c5558a7a1674	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
4a71088e-ce91-4ba2-9887-c5558a7a1674	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
6ca8b749-cba1-4453-8a20-0c189d9b9447	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
6ca8b749-cba1-4453-8a20-0c189d9b9447	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
6ca8b749-cba1-4453-8a20-0c189d9b9447	2bac4725-31a5-4315-bd97-562b7c764e2c	t
6ca8b749-cba1-4453-8a20-0c189d9b9447	0630fe1b-3718-401b-9aeb-5f4530d97637	t
6ca8b749-cba1-4453-8a20-0c189d9b9447	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
6ca8b749-cba1-4453-8a20-0c189d9b9447	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
6ca8b749-cba1-4453-8a20-0c189d9b9447	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
6ca8b749-cba1-4453-8a20-0c189d9b9447	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
f896f42d-66e6-498f-bdc0-a90216659041	b9996171-4af7-4c35-be93-8b799022b095	f
4a71088e-ce91-4ba2-9887-c5558a7a1674	b9996171-4af7-4c35-be93-8b799022b095	f
e8efb165-82f9-405c-98aa-e8535badd8ad	b9996171-4af7-4c35-be93-8b799022b095	f
6ca8b749-cba1-4453-8a20-0c189d9b9447	b9996171-4af7-4c35-be93-8b799022b095	f
5def7547-cfd3-4473-946c-35f796c52df4	b9996171-4af7-4c35-be93-8b799022b095	f
310aabaf-651c-4959-b441-8fe27129a418	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
c7c3433f-faa6-45b8-a353-bdb6635cea0c	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
d91bc61c-3f73-4e3a-add6-55fc753a31ec	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
dda53ff1-c096-4601-8a8c-30365fde853d	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
dda53ff1-c096-4601-8a8c-30365fde853d	0630fe1b-3718-401b-9aeb-5f4530d97637	t
dda53ff1-c096-4601-8a8c-30365fde853d	2bac4725-31a5-4315-bd97-562b7c764e2c	t
dda53ff1-c096-4601-8a8c-30365fde853d	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
dda53ff1-c096-4601-8a8c-30365fde853d	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
dda53ff1-c096-4601-8a8c-30365fde853d	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
dda53ff1-c096-4601-8a8c-30365fde853d	b9996171-4af7-4c35-be93-8b799022b095	f
dda53ff1-c096-4601-8a8c-30365fde853d	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
c041d458-ff12-4534-bcb0-cef6017935ab	dca376d8-cb66-4f66-a8eb-982b522bf009	t
c041d458-ff12-4534-bcb0-cef6017935ab	43c711ac-8d05-4374-962e-994721d09c71	t
c041d458-ff12-4534-bcb0-cef6017935ab	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
c041d458-ff12-4534-bcb0-cef6017935ab	ae3e0992-298c-42b0-bda3-c4671c460581	t
c041d458-ff12-4534-bcb0-cef6017935ab	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
c041d458-ff12-4534-bcb0-cef6017935ab	01d946a1-1cbe-4115-baa3-f318f98063cc	f
c041d458-ff12-4534-bcb0-cef6017935ab	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
c041d458-ff12-4534-bcb0-cef6017935ab	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
\.


--
-- Data for Name: client_scope_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_role_mapping (scope_id, role_id) FROM stdin;
01d946a1-1cbe-4115-baa3-f318f98063cc	b9c894e7-60c9-47ff-bbb4-db20b880c2d9
6b2ca845-56e5-456b-aa30-d582da23dc7f	818c584b-976b-40ee-a442-403c98bb668c
0630fe1b-3718-401b-9aeb-5f4530d97637	b012abe9-4360-4c1e-ad3f-7cedb43e5e4d
0630fe1b-3718-401b-9aeb-5f4530d97637	3d8b9944-d052-4e94-aba8-36358a0b5638
0630fe1b-3718-401b-9aeb-5f4530d97637	b801d083-6c88-4157-8d7e-303000280b1e
0630fe1b-3718-401b-9aeb-5f4530d97637	3c4f030e-51c7-489f-8f13-de85cf5a520d
\.


--
-- Data for Name: client_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session (id, client_id, redirect_uri, state, "timestamp", session_id, auth_method, realm_id, auth_user_id, current_action) FROM stdin;
\.


--
-- Data for Name: client_session_auth_status; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_auth_status (authenticator, status, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_note (name, value, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_prot_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_prot_mapper (protocol_mapper_id, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_role (role_id, client_session) FROM stdin;
\.


--
-- Data for Name: client_user_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_user_session_note (name, value, client_session) FROM stdin;
\.


--
-- Data for Name: component; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.component (id, name, parent_id, provider_id, provider_type, realm_id, sub_type) FROM stdin;
95b708dd-fb25-477e-bb4b-68de4feb4f1c	Trusted Hosts	master	trusted-hosts	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
cdc534cf-8b91-4dd8-9b15-d3b0723f3fea	Consent Required	master	consent-required	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
68edc6b7-0279-4027-9db7-cd13073a136e	Full Scope Disabled	master	scope	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
8d251c50-dfc8-48db-9c7e-a59269b7c89e	Max Clients Limit	master	max-clients	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
e127ea8a-dc28-4175-b2b6-c7309fa03183	Allowed Protocol Mapper Types	master	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
dc2f4a9c-e131-449c-b7b0-d9ce6846bcc4	Allowed Client Scopes	master	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
8ffb8525-3106-465b-b166-bcc5e3e0a424	Allowed Protocol Mapper Types	master	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	authenticated
6461a18c-a63b-4438-86dd-138f33e48970	Allowed Client Scopes	master	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	authenticated
dc822f9f-f2c0-4bda-b34d-458945e61d1d	rsa-generated	master	rsa-generated	org.keycloak.keys.KeyProvider	master	\N
7aa01332-1f47-4b1c-a09e-4891ebf49588	hmac-generated	master	hmac-generated	org.keycloak.keys.KeyProvider	master	\N
b21b2704-ee23-4449-8370-1c14226723aa	aes-generated	master	aes-generated	org.keycloak.keys.KeyProvider	master	\N
cec60a21-54a9-4eed-9b22-329139e43727	Allowed Client Scopes	francoralite	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
c3def567-77fe-4e84-93fe-39bfed0fdb68	Allowed Client Scopes	francoralite	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	authenticated
d11d1bbc-3fb0-4d39-9ed7-f83098b849bb	Consent Required	francoralite	consent-required	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
daf1cac5-356b-4ad5-981c-ecc8bd33dd71	Allowed Protocol Mapper Types	francoralite	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
871801fb-d8d4-4218-bf1b-c60d4b483392	Allowed Protocol Mapper Types	francoralite	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	authenticated
47de211e-8ef1-432c-97a2-0c70a6afe96e	Trusted Hosts	francoralite	trusted-hosts	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
8194eb43-806f-4df8-9b37-88bac5cd84b9	Full Scope Disabled	francoralite	scope	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
9164338d-81e7-479d-a8d6-093e88b54ace	Max Clients Limit	francoralite	max-clients	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	francoralite	anonymous
f4d6d623-396f-4bae-9d5c-0a9b4d5ea158	rsa-generated	francoralite	rsa-generated	org.keycloak.keys.KeyProvider	francoralite	\N
69774d94-7230-4371-ab90-ef095aa22c56	aes-generated	francoralite	aes-generated	org.keycloak.keys.KeyProvider	francoralite	\N
326cf4ed-dc1e-4778-b15f-b64d024f7f32	hmac-generated	francoralite	hmac-generated	org.keycloak.keys.KeyProvider	francoralite	\N
\.


--
-- Data for Name: component_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.component_config (id, component_id, name, value) FROM stdin;
eaa0d54e-e521-4d5e-85dd-9b2bb0a1c7fd	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	saml-user-property-mapper
2cf83881-4d8d-47a6-895b-470d5d8aa501	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
4641f5c9-367d-40f5-aaeb-82b78f06ddd2	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	saml-user-attribute-mapper
fb92a172-5fac-4b76-89a4-245a245b19ac	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	oidc-address-mapper
67bdc271-d686-47e7-ae55-1992fe6d8238	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
6e0aa011-03c4-4df5-970b-ca220f2a9cf5	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	oidc-full-name-mapper
e120d82d-a5c1-4601-b066-a4aaac878b50	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
298cb8e8-9e02-4982-9eb8-e0f4eab640be	8ffb8525-3106-465b-b166-bcc5e3e0a424	allowed-protocol-mapper-types	saml-role-list-mapper
9e46f448-b248-4896-bc53-f64e7d778440	8d251c50-dfc8-48db-9c7e-a59269b7c89e	max-clients	200
50e3a0f3-e66e-4885-85b0-3ae1b7ce26ad	95b708dd-fb25-477e-bb4b-68de4feb4f1c	host-sending-registration-request-must-match	true
fa7d5d17-4936-423e-8626-e1a08ca5ea30	95b708dd-fb25-477e-bb4b-68de4feb4f1c	client-uris-must-match	true
58dc3cff-b49a-468e-9ff2-9deb9b7077bf	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
4f2c643e-e6dc-455a-a967-c161bb81a281	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
f921c14f-b702-4466-b764-db8d9b104765	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	oidc-address-mapper
f111d2cc-a109-4903-850e-c11954c86ff9	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	saml-user-attribute-mapper
8c55fb59-1b27-46b3-8cda-0b1ab638374d	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	saml-user-property-mapper
19bde83d-1bc9-47ac-a826-72d01db5ced8	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	saml-role-list-mapper
b25fcbdd-60da-41fc-aa0e-3d22cd73f787	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	oidc-full-name-mapper
49664d65-2c3f-4a5d-ba6a-5a0e9e0e343b	e127ea8a-dc28-4175-b2b6-c7309fa03183	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
d6ee1d8e-4a33-4cb3-b13b-362c35a4042d	6461a18c-a63b-4438-86dd-138f33e48970	allow-default-scopes	true
12a28409-3ba6-4bb2-ba36-bf023b9bfede	dc2f4a9c-e131-449c-b7b0-d9ce6846bcc4	allow-default-scopes	true
222e76c6-0a77-47ac-a115-0a852fa93688	7aa01332-1f47-4b1c-a09e-4891ebf49588	priority	100
2559ace5-85a9-46ce-af0d-202c2daa77ae	7aa01332-1f47-4b1c-a09e-4891ebf49588	secret	X0WS2STDaowq4Dggln1faXKHf-HWX3QRHtKppEPqjl7MLhkJshhitbDYvJfZjg5stINmP2DB1jL4a_AcyO43xw
69641e7f-9a37-48f9-8087-fbbd50d51217	7aa01332-1f47-4b1c-a09e-4891ebf49588	algorithm	HS256
019ff8d8-80ac-4ef3-baf9-95268a974f87	7aa01332-1f47-4b1c-a09e-4891ebf49588	kid	31e94579-7ca1-429c-894a-167eab553004
4020fdd6-507d-4ddb-b593-92be667f6405	b21b2704-ee23-4449-8370-1c14226723aa	priority	100
3d156fff-fb90-447d-8bac-b1570dc6e1da	b21b2704-ee23-4449-8370-1c14226723aa	secret	OaeTAlBOqWkStvBC_RPKSw
2f8318b5-1dd9-450c-965d-ac9a6f400948	b21b2704-ee23-4449-8370-1c14226723aa	kid	a5bd2bd2-5b81-4adf-8cb3-e862b2d1850c
7e20114c-30cb-4261-9408-3639ae9e46f7	dc822f9f-f2c0-4bda-b34d-458945e61d1d	privateKey	MIIEpAIBAAKCAQEApMROcdl3ZPAEYlH6CHe1neuE4XLhchnz+c1HThGWR1P4fzvjdDyVlFcKc2tRR7K1OM1pTGKAs/VdXx7Gfb6zt03coHwcAGYRZWJ3Zta3HewFiY8NuQYaktXt9B/Elwf8jQJTUQ4qtSFcDPqL/sZaYltIYh8/xf9TkXKRnrjjt9oy6JVgqDT7wpMhSRI0KAvAzyrVck6/kOK1+afxlO4r+EtM4YVqv5gvpQCZetchAb/i79kCds5y2MYti/4DhB9xC0wAXrz26mCbaIieU23c7XsKK/Hd3fCc4sQXkvZUgXKhripnxs6a7GZZizV6r0lDfEzOmr6K/16GTfsmQZthuwIDAQABAoIBAFjReXflwnam67YUerQV09FNJFRjmSPo2ZvPDKEI2fmZSltL7VC7V+afBQMy1p3Pt+Dm2dxTPQ3FNpAQBu/B3R7y2fuo629LlhUQ/0xwckWu9U0x0DPtFmYQ7DSs60x/AaUBm+gVuu/pC7XzWYP9aLuceWhrb/VLrcC6AcWN5TM1jpGPPow2uO7dAkenaAriqp/WtrbrZeOslghkkwknZoGtUnJ6DOSbc+nzOQgRHRJ1sRzvEzGm/ErDsbyeKou8AOPlTmUgrbYNDzIDdb58OyP/XjMUviWpYxyImjeAYwOcVNPpW3QvYihvnCNwzEAl9W7a2p854+PvSCATp1ojsAECgYEA1zIur1WMBmV5555QfUeWsmzsYF6a72Z1aylj9FSTOG/8xcdUxS2o2X5BiUPtZSOYV77coUZSg/orgNIuG6SfOwBqRaeCIjGlC/hdjqS21UzBdChjKkdYDr8xofbkOS02hCRAbnU+G0nnNuoWLWNBu6jOuOSy+6LhBouxyfqZncUCgYEAxAI+OmY3TEebMCBAcPJ3c3eRTvL9zqpLBN1KSIOkWFYTe73PQpC3CvtVEhqMtgt3v+0K3xjfxilFXeILcrMp29cgb/k1IRQiA9nFq/VPMSIn8mbl/zkXkGo2PJC/XSe3w66QllJp2Aq3N9MdkKcHJG3PLPFCQxZSg1uXrvXEeX8CgYEAinjNF5/JkZgcoFD75BF7w+ZZGA3oTqI0bjddDSya6xcMpUuFnbeqzgDzNNuT15/W+KdlGxXAJRKGicc1Si5dE79JovaNw2kEljZEJXSR/aD9XrxaSytLW3nl+x1+b9hLGy6kky84PqEIegqZKK2U76dJFip7jXaaq/aZ+akazi0CgYEAroE8u6uDMeNSc89S7/u+g0uBT+OgOZ19OrB1UQf6ijbgE7vSSXYjsKBAheSjP/QHwhSdKDCyEW9u9X2pKY3/B12I4IfjWDbfbcQ1a7nzrk+1dudLfyVqKEWXUeagqKQSxCGnUl2/I/uuUQIhAUbjYfhtiZqlnqrB/XbPHZJrQKsCgYBgxn0BLxcvGh80JKs9qkvnOz+Nd7otRoAw4MwSGGRkTwU6JiNDf0jqi/AFN4ROGtuUuOpAig5sWVL8GvYWGmq3vvLLK+QPkRDy4ZwU6L9Mwtx7poc1rEzTxTEfYV9Ikme/Gru4sr51mzJwSz1j/orK2rTh5P1mTMlB9s3IYQ917g==
3b0a5708-9753-4164-8f9a-0ce438ccad84	dc822f9f-f2c0-4bda-b34d-458945e61d1d	priority	100
e2958771-021d-4b23-a9a2-5c83a36435d0	dc822f9f-f2c0-4bda-b34d-458945e61d1d	certificate	MIICmzCCAYMCBgFsiiaApzANBgkqhkiG9w0BAQsFADARMQ8wDQYDVQQDDAZtYXN0ZXIwHhcNMTkwODEzMDg0MjU0WhcNMjkwODEzMDg0NDM0WjARMQ8wDQYDVQQDDAZtYXN0ZXIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkxE5x2Xdk8ARiUfoId7Wd64ThcuFyGfP5zUdOEZZHU/h/O+N0PJWUVwpza1FHsrU4zWlMYoCz9V1fHsZ9vrO3TdygfBwAZhFlYndm1rcd7AWJjw25BhqS1e30H8SXB/yNAlNRDiq1IVwM+ov+xlpiW0hiHz/F/1ORcpGeuOO32jLolWCoNPvCkyFJEjQoC8DPKtVyTr+Q4rX5p/GU7iv4S0zhhWq/mC+lAJl61yEBv+Lv2QJ2znLYxi2L/gOEH3ELTABevPbqYJtoiJ5Tbdztewor8d3d8JzixBeS9lSBcqGuKmfGzprsZlmLNXqvSUN8TM6avor/XoZN+yZBm2G7AgMBAAEwDQYJKoZIhvcNAQELBQADggEBAIRWmNvR4k/Lnzip7IdNIrebz86nBLIzpkosrJxe9lDn/ys+GbqCFGZQEDSlxmDLSfTroAn/mKffxb/yEM6WCXBnnms7ahqIuT7B46H0i2I8hzZkukH0kpXXWPHruA26rqoEGjoJjhveCX+rrjclZ1nnPwIN6aDTwLDKospj2pJ4lFIYLNVskZpUwPGA6K3KK6Jr+zEivK8BvxHoRkX2MUmnZG4GqZ+lXh4wBlFZSGjFSaNAOQgdQr5dCzsjvXUsOKFySd3e3emQZG0SulFxYE9zM4Q4ysdRdssTxWeqyZMfxjsROpokJVupcwm7fjAqaFVJ9ecjr+kaPZ38/laCyrQ=
144b97a8-8f20-4438-bc64-5a1773e5fd8f	f4d6d623-396f-4bae-9d5c-0a9b4d5ea158	certificate	MIICpzCCAY8CBgFs8UWDgDANBgkqhkiG9w0BAQsFADAXMRUwEwYDVQQDDAxmcmFuY29yYWxpdGUwHhcNMTkwOTAyMDkxNzQwWhcNMjkwOTAyMDkxOTIwWjAXMRUwEwYDVQQDDAxmcmFuY29yYWxpdGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCA/+b5XajCbOLp6AEZB6QpOGxe5IOwQp9aNg2T2q4IJHgEEWVPTjjhvXFv3jzDsiLn04WivdQN+/Lz6YP1dKbnqCG5aG+68Bw4QZg+W+o49D6nkhe6bVvsuuMfVqWO0OZPoLo2jUP487OwvL0xAFG2jvNNuLdWJCiH7u0zLBQ+bpat5jGnA9MOFIIDb66m08mfZHm+qL84HjAi9D3Qle8fpETmhKSYdIxbXRRZEUY20IAEnLhdeUJcMOXoFb65O7LUu9VnEOKoG52oSaxt5WXaBcanjoFGqz5gNpuHXRXuuS4Xhd4djhtTcgJ9a77Vmrt9EXUSb9wxW5R+MpfLd0pnAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAFdFhXjZouY4dDyGgvVD4cvBqxhDLRfd6G5osu+Y5+xXCSEEqsjqSN1DFl0/sHuixiinq2KAvKxagdjCoMcR3aaJfLC38K5V1SiYp4e0xVFLVxTdhLEJFaVouNRCyeHbjjdmwJktal4xe+ilag368u8gx0qFrB/c/AsXLQ1kreaqW/xFzxOCYpzQTYSy7a6rWEEYEF1MuU/M1CojyKij6cwjxF0Jr0Qo7BnQnv/NMdOCEesV4XWcCSOvT9PgZiNwrWwxvoI2NNeq9IDVq9w6lCHp05MAPvBK3o+GUbbHgS8qiSPrVxk0QFqgOQwkYP7P1wMRecAoFEh+odMy2bT4bSM=
fc7b1b8a-b138-4591-8af6-b3343a89805d	f4d6d623-396f-4bae-9d5c-0a9b4d5ea158	privateKey	MIIEogIBAAKCAQEAgP/m+V2owmzi6egBGQekKThsXuSDsEKfWjYNk9quCCR4BBFlT0444b1xb948w7Ii59OFor3UDfvy8+mD9XSm56ghuWhvuvAcOEGYPlvqOPQ+p5IXum1b7LrjH1aljtDmT6C6No1D+POzsLy9MQBRto7zTbi3ViQoh+7tMywUPm6WreYxpwPTDhSCA2+uptPJn2R5vqi/OB4wIvQ90JXvH6RE5oSkmHSMW10UWRFGNtCABJy4XXlCXDDl6BW+uTuy1LvVZxDiqBudqEmsbeVl2gXGp46BRqs+YDabh10V7rkuF4XeHY4bU3ICfWu+1Zq7fRF1Em/cMVuUfjKXy3dKZwIDAQABAoIBAB+YjkY9vnwAl4ObI8mxqW+/Niv35JljeAxseN7iDQZJiGvWpu3Jxvzjnck8sb1tAEev82ds/2d9coBzjbKtI8RR1hDHl7Y94WuWBWggsznH+SCqE83Bw2Y0UDT40Awu9npCb9m0uBVd+4EqeVxrK5h/YvCCccVTjendh5OlFEBGFHSIGqQkHDpohR8cn52sQOrSA+4ABRpQjRPjPKu/5wuXlaWIh5RtbaMvH2fIswkDd6Vmw4zTCNvSl4ruLE9bja2HuDfWCR6yRwrtDwCawO5uAckzqHruNd4w1CxtKF7xVljnnzpy80utUW0RgC027B7A4X5mM8QEwjhwwYP+gSECgYEAygj+5El+X17KPPjQsqNKukxw6eDmPEpeQEJP0+8ZKyubTtKbew8nEHU4i5oVqe41CiCjyrORz/4nBHWdf2epmRJ+ZRU7f9ojNJDKgyQWJXu0o0iS4nCO5LeaZv6lapKwR36pGjFADRZSbyauR83QQbr8kpuW9uIfMRoCXAR3fDsCgYEAo3TLgHWXTtYQatAIEj2nEJ1ZxxxHBevv6zaxi8VYfJPLMK93ZvQTVf8S0oH+0aaZBp9LA63BFJw+xl/xRi8PoMpiF3ardXvxTUJMzFDc0JW0txBNsd59DBSRc0k49uNwesByOrxcouXICM6PUrBoyanjYKha7znLDocpwl4wA8UCgYBM1OzyLgzUAf1RAKKFPNofTRCnsLJ9/R4ou88V3tiodTXj3O3p95I4jQuK83cHn6ImDtGbNXzfJ1z5Mi1KFUcHAmR01oVBEtjOlb2d76xIZuoEKoZJfNqqmjQqtO59P/mvxrhSUKZ2E6YXxRMEFX38cTq6Gldn3ghUqPp6uewinwKBgGyyuLneeRaGKDi/yv5GXZkg6pkMZva7Jbsnjf5C6EtABXmE1kRyv4EKtTukEw7cWRscR0hU/fd0yBInr01a8muc6opr8i2YlKkqE+QzSgSz6Y9rmh9Us5ea/fbKlMUqDpyy6cPBi2EQqWuh4ZG9mpGxFnIqwv4fUreAjvagqBF5AoGAN+UDKbGYFh75xwTnB4WbLOtiUXe3Geyv29k40ppgcb5G8RQG8804PtNEUePMo97TT+ki+XxscghqhUcliL+NyCQGUwuaUIixsZaNt+TN284ZyxJioHvHzxWyqzBzNLjymkpS/TcXr2oNbhSWv62swcTsQWYmGr7Ab0CLEf2qjAo=
8c6ebe0d-f6cf-40e5-817d-3d4989fba0c9	f4d6d623-396f-4bae-9d5c-0a9b4d5ea158	priority	100
6751eca5-9bce-4c22-982e-69fe34345899	cec60a21-54a9-4eed-9b22-329139e43727	allow-default-scopes	true
aa1fe1d7-ef05-4433-82b2-ecb0089170ee	69774d94-7230-4371-ab90-ef095aa22c56	secret	Lo7-WyVARmAkzNZZ4UNsqA
aab7cf83-f575-4fa0-82cf-1ba9f3ed7d65	69774d94-7230-4371-ab90-ef095aa22c56	priority	100
fe648f76-913a-4785-adeb-7b86b1099190	69774d94-7230-4371-ab90-ef095aa22c56	kid	1aa670ae-4d93-43ce-ac5b-30cb390b181e
bea3151a-53cc-442e-b6b5-8f3bd7e228c6	326cf4ed-dc1e-4778-b15f-b64d024f7f32	secret	x9Tnnk3pGhJCZqW9hrn22PZdL9I9tCPI8GwC9_DWjmMI_jg0jc_fnTYRTKTsGICDpu-8yipdu3dspyeDnqoYGg
294d6f35-1d18-4959-96ea-bbec60461bda	326cf4ed-dc1e-4778-b15f-b64d024f7f32	kid	69f36a04-1a10-4de5-82c8-7f44d8cc61c3
94623c6e-2c36-4bce-9390-e74ef9b5dd24	326cf4ed-dc1e-4778-b15f-b64d024f7f32	algorithm	HS256
1a071752-ce4e-47bd-940d-b5db35b7e627	326cf4ed-dc1e-4778-b15f-b64d024f7f32	priority	100
02ef59dd-cbe9-40f9-8d87-3119651bdbda	c3def567-77fe-4e84-93fe-39bfed0fdb68	allow-default-scopes	true
4857c0cc-6679-48f4-b74b-fa7136c80aef	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	saml-user-attribute-mapper
3bbb9623-4372-4821-8519-1a722ad40ca8	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	oidc-address-mapper
4066282b-11b2-48ac-8da0-e967cc84fc32	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
722870ce-1405-4bfe-9e22-8fa7cdc4f40e	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	saml-role-list-mapper
a2cb3fcd-104e-4639-ba51-da3e7e237a5b	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
a51e17bf-c28e-458f-ab7c-cef380813366	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	saml-user-property-mapper
f20bcbad-4e3c-4ddd-b295-6c99cc67350e	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
616dd01f-9d04-42e2-aa1c-f4a42d74fb17	daf1cac5-356b-4ad5-981c-ecc8bd33dd71	allowed-protocol-mapper-types	oidc-full-name-mapper
a4c4fb10-408a-47f6-a659-9e2835b07cdf	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	saml-role-list-mapper
d3e1e7ec-ac24-4bdf-9055-8b8e25eadbc6	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	saml-user-property-mapper
7aa2140a-43de-4c81-ad2d-a9ef86ca00f8	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	oidc-address-mapper
206a17c1-8e1a-497d-8971-2358e435321f	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
22542ee0-5c15-444c-8b58-7a6748064c80	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
d93e61a7-2f67-4ba0-9dcc-db1f3094a565	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
6dbedee6-c4dd-4943-99dc-6e92250652bf	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	oidc-full-name-mapper
64eadd33-8711-42ef-9d61-94b23d747db8	871801fb-d8d4-4218-bf1b-c60d4b483392	allowed-protocol-mapper-types	saml-user-attribute-mapper
87ace9a3-bd9e-4367-803b-aa770a212cbb	47de211e-8ef1-432c-97a2-0c70a6afe96e	client-uris-must-match	true
2da77b23-e6e7-4b9d-b1b9-a48e5eaeaac2	47de211e-8ef1-432c-97a2-0c70a6afe96e	host-sending-registration-request-must-match	true
e872496d-efd2-4007-a248-2e8d98a215e6	9164338d-81e7-479d-a8d6-093e88b54ace	max-clients	200
\.


--
-- Data for Name: composite_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.composite_role (composite, child_role) FROM stdin;
398b3395-34b8-4668-9296-05ba7eb64bbb	636a3642-167a-432f-a6af-1c0630e1d3d5
398b3395-34b8-4668-9296-05ba7eb64bbb	26e019a5-44f6-404b-88b4-6b05b9846883
398b3395-34b8-4668-9296-05ba7eb64bbb	9be3b9f1-9fb4-46c1-906e-7ca638901fb5
398b3395-34b8-4668-9296-05ba7eb64bbb	f9d9318c-e4a6-4b36-a0f0-b9b19209e510
398b3395-34b8-4668-9296-05ba7eb64bbb	0e2a1a49-3f04-443f-b413-ed096fbc3db1
398b3395-34b8-4668-9296-05ba7eb64bbb	2543c7c6-6d57-496a-8684-fce33b9676e3
398b3395-34b8-4668-9296-05ba7eb64bbb	3c8882f0-a30b-4509-8874-6a0dd8e0f669
398b3395-34b8-4668-9296-05ba7eb64bbb	76fdc691-104d-4f70-98fc-2cbeb6c45658
398b3395-34b8-4668-9296-05ba7eb64bbb	ab5cc34c-5d27-4ad5-802f-fc87e9340cfd
398b3395-34b8-4668-9296-05ba7eb64bbb	e3f59d89-0dff-4fa5-a7b1-a3ab7dde510e
398b3395-34b8-4668-9296-05ba7eb64bbb	4765895f-7470-4702-b641-6045f6f6beca
398b3395-34b8-4668-9296-05ba7eb64bbb	926c9477-dbfb-44f1-892c-2069beaabb1b
398b3395-34b8-4668-9296-05ba7eb64bbb	5ea284a4-c64c-4fd3-9630-e5f685aef233
398b3395-34b8-4668-9296-05ba7eb64bbb	4cde772d-ed4b-45f5-a3ad-2a9d827da1cb
398b3395-34b8-4668-9296-05ba7eb64bbb	91b25ecc-17aa-4e61-b80f-92ffae4a2596
398b3395-34b8-4668-9296-05ba7eb64bbb	083d0f99-5fe3-4993-8540-ca638edf3a5b
398b3395-34b8-4668-9296-05ba7eb64bbb	a738a78e-752f-4836-b8e7-5f91d9c79cf4
398b3395-34b8-4668-9296-05ba7eb64bbb	dca87bca-200e-4e31-8d67-868e02e4e6d5
f9d9318c-e4a6-4b36-a0f0-b9b19209e510	91b25ecc-17aa-4e61-b80f-92ffae4a2596
f9d9318c-e4a6-4b36-a0f0-b9b19209e510	dca87bca-200e-4e31-8d67-868e02e4e6d5
0e2a1a49-3f04-443f-b413-ed096fbc3db1	083d0f99-5fe3-4993-8540-ca638edf3a5b
d5447076-ea4f-4493-b0f9-dbea011ad108	39965e67-dd49-4054-874a-5ce643fe1149
398b3395-34b8-4668-9296-05ba7eb64bbb	a1701289-7090-46d3-9f81-4bba96a05fd0
398b3395-34b8-4668-9296-05ba7eb64bbb	6d3855c3-6964-4931-8af6-4a471acbc6c9
398b3395-34b8-4668-9296-05ba7eb64bbb	485b20a6-7568-42e7-8b73-ae178e8aa1dd
398b3395-34b8-4668-9296-05ba7eb64bbb	01022f0e-4ca5-4315-af91-6a20189b7c7d
398b3395-34b8-4668-9296-05ba7eb64bbb	69073716-b9e8-4188-976f-e42afc6e9471
398b3395-34b8-4668-9296-05ba7eb64bbb	1bc444d1-48d7-42d1-ac21-3f09ca23c49a
398b3395-34b8-4668-9296-05ba7eb64bbb	eb68b146-9ee6-429d-8e97-e04f7da191b0
398b3395-34b8-4668-9296-05ba7eb64bbb	99ace0f9-25de-4b9c-95e3-dca31b2351dd
398b3395-34b8-4668-9296-05ba7eb64bbb	b5002289-a0a2-496c-b2d0-6c8ee6dc0071
398b3395-34b8-4668-9296-05ba7eb64bbb	83ff8fbc-63d5-431b-ad71-214e0d568ace
398b3395-34b8-4668-9296-05ba7eb64bbb	11297344-68b2-4d05-9581-029ccd3a3e71
398b3395-34b8-4668-9296-05ba7eb64bbb	0b4fe154-70b7-40e9-abdc-ae3ba6d34b44
398b3395-34b8-4668-9296-05ba7eb64bbb	b052bc08-bef9-44c9-9aac-450a0971ed33
398b3395-34b8-4668-9296-05ba7eb64bbb	11155683-35f4-4080-8346-2e4097112e68
398b3395-34b8-4668-9296-05ba7eb64bbb	b4e99917-8faf-4edf-8dcf-52f88b8eab7a
398b3395-34b8-4668-9296-05ba7eb64bbb	1d65077e-2297-44fb-8fd7-08ca17420ff9
398b3395-34b8-4668-9296-05ba7eb64bbb	24810ecb-1090-4c0d-9675-70a8f6e8a2da
398b3395-34b8-4668-9296-05ba7eb64bbb	8371eb96-4637-4713-a308-7f37f4bc6f51
01022f0e-4ca5-4315-af91-6a20189b7c7d	b4e99917-8faf-4edf-8dcf-52f88b8eab7a
01022f0e-4ca5-4315-af91-6a20189b7c7d	8371eb96-4637-4713-a308-7f37f4bc6f51
69073716-b9e8-4188-976f-e42afc6e9471	1d65077e-2297-44fb-8fd7-08ca17420ff9
95ace2ba-e3db-4730-b36f-7267c80f90d5	79f75c48-faa6-4f82-8f35-b396ce9ebb5a
95ace2ba-e3db-4730-b36f-7267c80f90d5	41603418-57aa-4736-8f27-b7f24054a9a3
9200e548-99db-4699-be64-d60aedc3a4f6	b39fa7d2-1db7-466f-8151-e26d9a9e38ab
9200e548-99db-4699-be64-d60aedc3a4f6	0d7e15c9-2c4d-446a-9287-2a37abb0e0ab
9200e548-99db-4699-be64-d60aedc3a4f6	3184fc22-943f-4425-a50d-aea41d91b69a
9200e548-99db-4699-be64-d60aedc3a4f6	6769e846-0726-42ff-b07b-46974672176c
9200e548-99db-4699-be64-d60aedc3a4f6	bef7cb79-04f1-46da-8ddd-728933ed4383
9200e548-99db-4699-be64-d60aedc3a4f6	7fedc9e8-90ea-4a77-898f-3b3fd6d01715
9200e548-99db-4699-be64-d60aedc3a4f6	383ce563-296d-48b4-a266-146cc84c6d43
9200e548-99db-4699-be64-d60aedc3a4f6	186a2ce5-0edd-4b05-b524-fceeae08f630
9200e548-99db-4699-be64-d60aedc3a4f6	79f75c48-faa6-4f82-8f35-b396ce9ebb5a
9200e548-99db-4699-be64-d60aedc3a4f6	95b8d4d7-001b-4581-bc55-4e3513d6cf14
9200e548-99db-4699-be64-d60aedc3a4f6	201d06f3-dc5d-4a59-af26-dfd843ce449f
9200e548-99db-4699-be64-d60aedc3a4f6	a62d9cd0-0166-4c69-a5d4-685c8de4feca
9200e548-99db-4699-be64-d60aedc3a4f6	4d2300e9-49ab-4097-905a-9629824afd41
9200e548-99db-4699-be64-d60aedc3a4f6	cce275a3-4210-46e5-83e9-5a00e6c7b9a6
9200e548-99db-4699-be64-d60aedc3a4f6	41603418-57aa-4736-8f27-b7f24054a9a3
9200e548-99db-4699-be64-d60aedc3a4f6	95ace2ba-e3db-4730-b36f-7267c80f90d5
9200e548-99db-4699-be64-d60aedc3a4f6	35bbea1c-2fc8-473d-a1c2-df3a8817b6d7
9200e548-99db-4699-be64-d60aedc3a4f6	2b64f08e-5007-4e1c-ba43-0961a04d27e4
2b64f08e-5007-4e1c-ba43-0961a04d27e4	35bbea1c-2fc8-473d-a1c2-df3a8817b6d7
5531c621-ad97-4da9-8896-bed73d09c285	12faee8b-64db-41cb-97cf-7c085d3cd410
398b3395-34b8-4668-9296-05ba7eb64bbb	3169b997-86b7-4d6c-a419-54f797a09030
cf336c4f-f1fc-447b-a686-2f44ac81a67f	b684e64f-9250-42e0-a055-2a18ffa4df88
cf336c4f-f1fc-447b-a686-2f44ac81a67f	818c584b-976b-40ee-a442-403c98bb668c
cf336c4f-f1fc-447b-a686-2f44ac81a67f	5531c621-ad97-4da9-8896-bed73d09c285
cf336c4f-f1fc-447b-a686-2f44ac81a67f	850b0803-fc35-445d-a23e-d6479241bb60
7079ef4e-6e2e-4bda-91d8-cf52142687be	b9c894e7-60c9-47ff-bbb4-db20b880c2d9
7079ef4e-6e2e-4bda-91d8-cf52142687be	59163355-f8e4-43f5-9064-c34167799f8f
7079ef4e-6e2e-4bda-91d8-cf52142687be	8f8f910c-2f7c-4bec-b66f-d7058b53e4c5
7079ef4e-6e2e-4bda-91d8-cf52142687be	d5447076-ea4f-4493-b0f9-dbea011ad108
6c0ac76f-a3f4-49b1-9faf-7c59a795e278	c72cf68d-44f2-423d-a684-d08c2bebac81
c2374f6d-7c7f-412f-a39f-a1c1229ae84e	17be79a5-a074-400f-b655-5f5ed9d35074
\.


--
-- Data for Name: credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.credential (id, salt, type, user_id, created_date, user_label, secret_data, credential_data, priority) FROM stdin;
67d3b1d2-23a6-4f56-9347-5e098d7f0f5b	\N	password	ddf2637a-e7d1-4396-93c2-514135e73261	\N	\N	{"value":"wd+QiB/M30ue7Dctr+QS1VmUdT6oLcHSXsG8YEO3hPtFdw/RQdVnWqjm8KguVXTe/l2jrvwJfWhELjuESK9+pg==","salt":"86vlKaC3bzvaHQzgR5dwfw=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
ccca885a-ce26-401b-bed8-f22f5e7b3423	\N	password	0914bbc4-0b4f-4768-93a3-a69d14d13114	1622987871234	\N	{"value":"VImB+MNGkvA24XuBmp2ZTWF8nnokju5OzLz6pPHe0FznpS3lpreFbKRtqGpJGKrj7YEq/lmHj++W4cdv/OBn/A==","salt":"ZYsK7g9sJSE6Y0AvcPR15A=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
1f6aa710-ff65-461e-bef0-6dd6583aa688	\N	password	25d39c71-cebd-4828-b750-3b8daad7778e	1622987810503	\N	{"value":"MCD/jIaWIKp+O4J4d8jhKQYGPzjuCYtVi98Jex5Rg2k9R1uKcgrFtW0ul1wSOQRKw83zI+wkHzy+SB3CVJThVA==","salt":"XB+ufmOoZmaxgyrRnq33Ww=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
a083bfe0-8b65-4de4-b4cd-184a5445b75e	\N	password	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955	1622987933940	\N	{"value":"auFIP6r7vd4AVLfIoLsFATaU0KW9h8ksJSrVm1hZquG7yFqy4YOd4IUhmkAC5fjVWle2ZDbgwhyUcw8SkzldyA==","salt":"2L6eIeY90s4+g8QVgw8YvA=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
\.


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
1.0.0.Final-KEYCLOAK-5461	sthorger@redhat.com	META-INF/jpa-changelog-1.0.0.Final.xml	2019-08-13 08:44:28.160527	1	EXECUTED	7:4e70412f24a3f382c82183742ec79317	createTable tableName=APPLICATION_DEFAULT_ROLES; createTable tableName=CLIENT; createTable tableName=CLIENT_SESSION; createTable tableName=CLIENT_SESSION_ROLE; createTable tableName=COMPOSITE_ROLE; createTable tableName=CREDENTIAL; createTable tab...		\N	3.5.4	\N	\N	5685867745
1.0.0.Final-KEYCLOAK-5461	sthorger@redhat.com	META-INF/db2-jpa-changelog-1.0.0.Final.xml	2019-08-13 08:44:28.175831	2	MARK_RAN	7:cb16724583e9675711801c6875114f28	createTable tableName=APPLICATION_DEFAULT_ROLES; createTable tableName=CLIENT; createTable tableName=CLIENT_SESSION; createTable tableName=CLIENT_SESSION_ROLE; createTable tableName=COMPOSITE_ROLE; createTable tableName=CREDENTIAL; createTable tab...		\N	3.5.4	\N	\N	5685867745
1.1.0.Beta1	sthorger@redhat.com	META-INF/jpa-changelog-1.1.0.Beta1.xml	2019-08-13 08:44:28.221388	3	EXECUTED	7:0310eb8ba07cec616460794d42ade0fa	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=CLIENT_ATTRIBUTES; createTable tableName=CLIENT_SESSION_NOTE; createTable tableName=APP_NODE_REGISTRATIONS; addColumn table...		\N	3.5.4	\N	\N	5685867745
1.1.0.Final	sthorger@redhat.com	META-INF/jpa-changelog-1.1.0.Final.xml	2019-08-13 08:44:28.225217	4	EXECUTED	7:5d25857e708c3233ef4439df1f93f012	renameColumn newColumnName=EVENT_TIME, oldColumnName=TIME, tableName=EVENT_ENTITY		\N	3.5.4	\N	\N	5685867745
1.2.0.Beta1	psilva@redhat.com	META-INF/jpa-changelog-1.2.0.Beta1.xml	2019-08-13 08:44:28.418905	5	EXECUTED	7:c7a54a1041d58eb3817a4a883b4d4e84	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=PROTOCOL_MAPPER; createTable tableName=PROTOCOL_MAPPER_CONFIG; createTable tableName=...		\N	3.5.4	\N	\N	5685867745
1.2.0.Beta1	psilva@redhat.com	META-INF/db2-jpa-changelog-1.2.0.Beta1.xml	2019-08-13 08:44:28.425088	6	MARK_RAN	7:2e01012df20974c1c2a605ef8afe25b7	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=PROTOCOL_MAPPER; createTable tableName=PROTOCOL_MAPPER_CONFIG; createTable tableName=...		\N	3.5.4	\N	\N	5685867745
1.2.0.RC1	bburke@redhat.com	META-INF/jpa-changelog-1.2.0.CR1.xml	2019-08-13 08:44:28.593342	7	EXECUTED	7:0f08df48468428e0f30ee59a8ec01a41	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=MIGRATION_MODEL; createTable tableName=IDENTITY_P...		\N	3.5.4	\N	\N	5685867745
1.2.0.RC1	bburke@redhat.com	META-INF/db2-jpa-changelog-1.2.0.CR1.xml	2019-08-13 08:44:28.597684	8	MARK_RAN	7:a77ea2ad226b345e7d689d366f185c8c	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=MIGRATION_MODEL; createTable tableName=IDENTITY_P...		\N	3.5.4	\N	\N	5685867745
1.2.0.Final	keycloak	META-INF/jpa-changelog-1.2.0.Final.xml	2019-08-13 08:44:28.602134	9	EXECUTED	7:a3377a2059aefbf3b90ebb4c4cc8e2ab	update tableName=CLIENT; update tableName=CLIENT; update tableName=CLIENT		\N	3.5.4	\N	\N	5685867745
1.3.0	bburke@redhat.com	META-INF/jpa-changelog-1.3.0.xml	2019-08-13 08:44:28.85713	10	EXECUTED	7:04c1dbedc2aa3e9756d1a1668e003451	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=ADMI...		\N	3.5.4	\N	\N	5685867745
1.4.0	bburke@redhat.com	META-INF/jpa-changelog-1.4.0.xml	2019-08-13 08:44:28.968913	11	EXECUTED	7:36ef39ed560ad07062d956db861042ba	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5685867745
1.4.0	bburke@redhat.com	META-INF/db2-jpa-changelog-1.4.0.xml	2019-08-13 08:44:28.97245	12	MARK_RAN	7:d909180b2530479a716d3f9c9eaea3d7	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5685867745
1.5.0	bburke@redhat.com	META-INF/jpa-changelog-1.5.0.xml	2019-08-13 08:44:29.100069	13	EXECUTED	7:cf12b04b79bea5152f165eb41f3955f6	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5685867745
1.6.1_from15	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2019-08-13 08:44:29.189243	14	EXECUTED	7:7e32c8f05c755e8675764e7d5f514509	addColumn tableName=REALM; addColumn tableName=KEYCLOAK_ROLE; addColumn tableName=CLIENT; createTable tableName=OFFLINE_USER_SESSION; createTable tableName=OFFLINE_CLIENT_SESSION; addPrimaryKey constraintName=CONSTRAINT_OFFL_US_SES_PK2, tableName=...		\N	3.5.4	\N	\N	5685867745
1.6.1_from16-pre	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2019-08-13 08:44:29.191912	15	MARK_RAN	7:980ba23cc0ec39cab731ce903dd01291	delete tableName=OFFLINE_CLIENT_SESSION; delete tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	5685867745
1.6.1_from16	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2019-08-13 08:44:29.194153	16	MARK_RAN	7:2fa220758991285312eb84f3b4ff5336	dropPrimaryKey constraintName=CONSTRAINT_OFFLINE_US_SES_PK, tableName=OFFLINE_USER_SESSION; dropPrimaryKey constraintName=CONSTRAINT_OFFLINE_CL_SES_PK, tableName=OFFLINE_CLIENT_SESSION; addColumn tableName=OFFLINE_USER_SESSION; update tableName=OF...		\N	3.5.4	\N	\N	5685867745
1.6.1	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2019-08-13 08:44:29.196368	17	EXECUTED	7:d41d8cd98f00b204e9800998ecf8427e	empty		\N	3.5.4	\N	\N	5685867745
1.7.0	bburke@redhat.com	META-INF/jpa-changelog-1.7.0.xml	2019-08-13 08:44:29.354039	18	EXECUTED	7:91ace540896df890cc00a0490ee52bbc	createTable tableName=KEYCLOAK_GROUP; createTable tableName=GROUP_ROLE_MAPPING; createTable tableName=GROUP_ATTRIBUTE; createTable tableName=USER_GROUP_MEMBERSHIP; createTable tableName=REALM_DEFAULT_GROUPS; addColumn tableName=IDENTITY_PROVIDER; ...		\N	3.5.4	\N	\N	5685867745
1.8.0	mposolda@redhat.com	META-INF/jpa-changelog-1.8.0.xml	2019-08-13 08:44:29.492373	19	EXECUTED	7:c31d1646dfa2618a9335c00e07f89f24	addColumn tableName=IDENTITY_PROVIDER; createTable tableName=CLIENT_TEMPLATE; createTable tableName=CLIENT_TEMPLATE_ATTRIBUTES; createTable tableName=TEMPLATE_SCOPE_MAPPING; dropNotNullConstraint columnName=CLIENT_ID, tableName=PROTOCOL_MAPPER; ad...		\N	3.5.4	\N	\N	5685867745
1.8.0-2	keycloak	META-INF/jpa-changelog-1.8.0.xml	2019-08-13 08:44:29.49886	20	EXECUTED	7:df8bc21027a4f7cbbb01f6344e89ce07	dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; update tableName=CREDENTIAL		\N	3.5.4	\N	\N	5685867745
authz-3.4.0.CR1-resource-server-pk-change-part1	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2019-08-13 08:44:30.302858	45	EXECUTED	7:6a48ce645a3525488a90fbf76adf3bb3	addColumn tableName=RESOURCE_SERVER_POLICY; addColumn tableName=RESOURCE_SERVER_RESOURCE; addColumn tableName=RESOURCE_SERVER_SCOPE		\N	3.5.4	\N	\N	5685867745
1.8.0	mposolda@redhat.com	META-INF/db2-jpa-changelog-1.8.0.xml	2019-08-13 08:44:29.501823	21	MARK_RAN	7:f987971fe6b37d963bc95fee2b27f8df	addColumn tableName=IDENTITY_PROVIDER; createTable tableName=CLIENT_TEMPLATE; createTable tableName=CLIENT_TEMPLATE_ATTRIBUTES; createTable tableName=TEMPLATE_SCOPE_MAPPING; dropNotNullConstraint columnName=CLIENT_ID, tableName=PROTOCOL_MAPPER; ad...		\N	3.5.4	\N	\N	5685867745
1.8.0-2	keycloak	META-INF/db2-jpa-changelog-1.8.0.xml	2019-08-13 08:44:29.504682	22	MARK_RAN	7:df8bc21027a4f7cbbb01f6344e89ce07	dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; update tableName=CREDENTIAL		\N	3.5.4	\N	\N	5685867745
1.9.0	mposolda@redhat.com	META-INF/jpa-changelog-1.9.0.xml	2019-08-13 08:44:29.523447	23	EXECUTED	7:ed2dc7f799d19ac452cbcda56c929e47	update tableName=REALM; update tableName=REALM; update tableName=REALM; update tableName=REALM; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=REALM; update tableName=REALM; customChange; dr...		\N	3.5.4	\N	\N	5685867745
1.9.1	keycloak	META-INF/jpa-changelog-1.9.1.xml	2019-08-13 08:44:29.528377	24	EXECUTED	7:80b5db88a5dda36ece5f235be8757615	modifyDataType columnName=PRIVATE_KEY, tableName=REALM; modifyDataType columnName=PUBLIC_KEY, tableName=REALM; modifyDataType columnName=CERTIFICATE, tableName=REALM		\N	3.5.4	\N	\N	5685867745
1.9.1	keycloak	META-INF/db2-jpa-changelog-1.9.1.xml	2019-08-13 08:44:29.530462	25	MARK_RAN	7:1437310ed1305a9b93f8848f301726ce	modifyDataType columnName=PRIVATE_KEY, tableName=REALM; modifyDataType columnName=CERTIFICATE, tableName=REALM		\N	3.5.4	\N	\N	5685867745
1.9.2	keycloak	META-INF/jpa-changelog-1.9.2.xml	2019-08-13 08:44:29.573656	26	EXECUTED	7:b82ffb34850fa0836be16deefc6a87c4	createIndex indexName=IDX_USER_EMAIL, tableName=USER_ENTITY; createIndex indexName=IDX_USER_ROLE_MAPPING, tableName=USER_ROLE_MAPPING; createIndex indexName=IDX_USER_GROUP_MAPPING, tableName=USER_GROUP_MEMBERSHIP; createIndex indexName=IDX_USER_CO...		\N	3.5.4	\N	\N	5685867745
authz-2.0.0	psilva@redhat.com	META-INF/jpa-changelog-authz-2.0.0.xml	2019-08-13 08:44:29.674838	27	EXECUTED	7:9cc98082921330d8d9266decdd4bd658	createTable tableName=RESOURCE_SERVER; addPrimaryKey constraintName=CONSTRAINT_FARS, tableName=RESOURCE_SERVER; addUniqueConstraint constraintName=UK_AU8TT6T700S9V50BU18WS5HA6, tableName=RESOURCE_SERVER; createTable tableName=RESOURCE_SERVER_RESOU...		\N	3.5.4	\N	\N	5685867745
authz-2.5.1	psilva@redhat.com	META-INF/jpa-changelog-authz-2.5.1.xml	2019-08-13 08:44:29.67838	28	EXECUTED	7:03d64aeed9cb52b969bd30a7ac0db57e	update tableName=RESOURCE_SERVER_POLICY		\N	3.5.4	\N	\N	5685867745
2.1.0-KEYCLOAK-5461	bburke@redhat.com	META-INF/jpa-changelog-2.1.0.xml	2019-08-13 08:44:29.755834	29	EXECUTED	7:f1f9fd8710399d725b780f463c6b21cd	createTable tableName=BROKER_LINK; createTable tableName=FED_USER_ATTRIBUTE; createTable tableName=FED_USER_CONSENT; createTable tableName=FED_USER_CONSENT_ROLE; createTable tableName=FED_USER_CONSENT_PROT_MAPPER; createTable tableName=FED_USER_CR...		\N	3.5.4	\N	\N	5685867745
2.2.0	bburke@redhat.com	META-INF/jpa-changelog-2.2.0.xml	2019-08-13 08:44:29.778667	30	EXECUTED	7:53188c3eb1107546e6f765835705b6c1	addColumn tableName=ADMIN_EVENT_ENTITY; createTable tableName=CREDENTIAL_ATTRIBUTE; createTable tableName=FED_CREDENTIAL_ATTRIBUTE; modifyDataType columnName=VALUE, tableName=CREDENTIAL; addForeignKeyConstraint baseTableName=FED_CREDENTIAL_ATTRIBU...		\N	3.5.4	\N	\N	5685867745
2.3.0	bburke@redhat.com	META-INF/jpa-changelog-2.3.0.xml	2019-08-13 08:44:29.804568	31	EXECUTED	7:d6e6f3bc57a0c5586737d1351725d4d4	createTable tableName=FEDERATED_USER; addPrimaryKey constraintName=CONSTR_FEDERATED_USER, tableName=FEDERATED_USER; dropDefaultValue columnName=TOTP, tableName=USER_ENTITY; dropColumn columnName=TOTP, tableName=USER_ENTITY; addColumn tableName=IDE...		\N	3.5.4	\N	\N	5685867745
2.4.0	bburke@redhat.com	META-INF/jpa-changelog-2.4.0.xml	2019-08-13 08:44:29.815166	32	EXECUTED	7:454d604fbd755d9df3fd9c6329043aa5	customChange		\N	3.5.4	\N	\N	5685867745
2.5.0	bburke@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2019-08-13 08:44:29.828201	33	EXECUTED	7:57e98a3077e29caf562f7dbf80c72600	customChange; modifyDataType columnName=USER_ID, tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	5685867745
2.5.0-unicode-oracle	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2019-08-13 08:44:29.832991	34	MARK_RAN	7:e4c7e8f2256210aee71ddc42f538b57a	modifyDataType columnName=DESCRIPTION, tableName=AUTHENTICATION_FLOW; modifyDataType columnName=DESCRIPTION, tableName=CLIENT_TEMPLATE; modifyDataType columnName=DESCRIPTION, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=DESCRIPTION,...		\N	3.5.4	\N	\N	5685867745
2.5.0-unicode-other-dbs	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2019-08-13 08:44:29.886191	35	EXECUTED	7:09a43c97e49bc626460480aa1379b522	modifyDataType columnName=DESCRIPTION, tableName=AUTHENTICATION_FLOW; modifyDataType columnName=DESCRIPTION, tableName=CLIENT_TEMPLATE; modifyDataType columnName=DESCRIPTION, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=DESCRIPTION,...		\N	3.5.4	\N	\N	5685867745
2.5.0-duplicate-email-support	slawomir@dabek.name	META-INF/jpa-changelog-2.5.0.xml	2019-08-13 08:44:29.933968	36	EXECUTED	7:26bfc7c74fefa9126f2ce702fb775553	addColumn tableName=REALM		\N	3.5.4	\N	\N	5685867745
2.5.0-unique-group-names	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2019-08-13 08:44:29.946606	37	EXECUTED	7:a161e2ae671a9020fff61e996a207377	addUniqueConstraint constraintName=SIBLING_NAMES, tableName=KEYCLOAK_GROUP		\N	3.5.4	\N	\N	5685867745
2.5.1	bburke@redhat.com	META-INF/jpa-changelog-2.5.1.xml	2019-08-13 08:44:29.954138	38	EXECUTED	7:37fc1781855ac5388c494f1442b3f717	addColumn tableName=FED_USER_CONSENT		\N	3.5.4	\N	\N	5685867745
3.0.0	bburke@redhat.com	META-INF/jpa-changelog-3.0.0.xml	2019-08-13 08:44:29.977037	39	EXECUTED	7:13a27db0dae6049541136adad7261d27	addColumn tableName=IDENTITY_PROVIDER		\N	3.5.4	\N	\N	5685867745
3.2.0-fix	keycloak	META-INF/jpa-changelog-3.2.0.xml	2019-08-13 08:44:29.980389	40	MARK_RAN	7:550300617e3b59e8af3a6294df8248a3	addNotNullConstraint columnName=REALM_ID, tableName=CLIENT_INITIAL_ACCESS		\N	3.5.4	\N	\N	5685867745
3.2.0-fix-with-keycloak-5416	keycloak	META-INF/jpa-changelog-3.2.0.xml	2019-08-13 08:44:29.983451	41	MARK_RAN	7:e3a9482b8931481dc2772a5c07c44f17	dropIndex indexName=IDX_CLIENT_INIT_ACC_REALM, tableName=CLIENT_INITIAL_ACCESS; addNotNullConstraint columnName=REALM_ID, tableName=CLIENT_INITIAL_ACCESS; createIndex indexName=IDX_CLIENT_INIT_ACC_REALM, tableName=CLIENT_INITIAL_ACCESS		\N	3.5.4	\N	\N	5685867745
3.2.0-fix-offline-sessions	hmlnarik	META-INF/jpa-changelog-3.2.0.xml	2019-08-13 08:44:29.991166	42	EXECUTED	7:72b07d85a2677cb257edb02b408f332d	customChange		\N	3.5.4	\N	\N	5685867745
3.2.0-fixed	keycloak	META-INF/jpa-changelog-3.2.0.xml	2019-08-13 08:44:30.252966	43	EXECUTED	7:a72a7858967bd414835d19e04d880312	addColumn tableName=REALM; dropPrimaryKey constraintName=CONSTRAINT_OFFL_CL_SES_PK2, tableName=OFFLINE_CLIENT_SESSION; dropColumn columnName=CLIENT_SESSION_ID, tableName=OFFLINE_CLIENT_SESSION; addPrimaryKey constraintName=CONSTRAINT_OFFL_CL_SES_P...		\N	3.5.4	\N	\N	5685867745
3.3.0	keycloak	META-INF/jpa-changelog-3.3.0.xml	2019-08-13 08:44:30.292215	44	EXECUTED	7:94edff7cf9ce179e7e85f0cd78a3cf2c	addColumn tableName=USER_ENTITY		\N	3.5.4	\N	\N	5685867745
authz-3.4.0.CR1-resource-server-pk-change-part2-KEYCLOAK-6095	hmlnarik@redhat.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2019-08-13 08:44:30.310748	46	EXECUTED	7:e64b5dcea7db06077c6e57d3b9e5ca14	customChange		\N	3.5.4	\N	\N	5685867745
authz-3.4.0.CR1-resource-server-pk-change-part3-fixed	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2019-08-13 08:44:30.314803	47	MARK_RAN	7:fd8cf02498f8b1e72496a20afc75178c	dropIndex indexName=IDX_RES_SERV_POL_RES_SERV, tableName=RESOURCE_SERVER_POLICY; dropIndex indexName=IDX_RES_SRV_RES_RES_SRV, tableName=RESOURCE_SERVER_RESOURCE; dropIndex indexName=IDX_RES_SRV_SCOPE_RES_SRV, tableName=RESOURCE_SERVER_SCOPE		\N	3.5.4	\N	\N	5685867745
authz-3.4.0.CR1-resource-server-pk-change-part3-fixed-nodropindex	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2019-08-13 08:44:30.393704	48	EXECUTED	7:542794f25aa2b1fbabb7e577d6646319	addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, tableName=RESOURCE_SERVER_POLICY; addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, tableName=RESOURCE_SERVER_RESOURCE; addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, ...		\N	3.5.4	\N	\N	5685867745
authn-3.4.0.CR1-refresh-token-max-reuse	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2019-08-13 08:44:30.42764	49	EXECUTED	7:edad604c882df12f74941dac3cc6d650	addColumn tableName=REALM		\N	3.5.4	\N	\N	5685867745
3.4.0	keycloak	META-INF/jpa-changelog-3.4.0.xml	2019-08-13 08:44:30.518257	50	EXECUTED	7:0f88b78b7b46480eb92690cbf5e44900	addPrimaryKey constraintName=CONSTRAINT_REALM_DEFAULT_ROLES, tableName=REALM_DEFAULT_ROLES; addPrimaryKey constraintName=CONSTRAINT_COMPOSITE_ROLE, tableName=COMPOSITE_ROLE; addPrimaryKey constraintName=CONSTR_REALM_DEFAULT_GROUPS, tableName=REALM...		\N	3.5.4	\N	\N	5685867745
3.4.0-KEYCLOAK-5230	hmlnarik@redhat.com	META-INF/jpa-changelog-3.4.0.xml	2019-08-13 08:44:30.584649	51	EXECUTED	7:d560e43982611d936457c327f872dd59	createIndex indexName=IDX_FU_ATTRIBUTE, tableName=FED_USER_ATTRIBUTE; createIndex indexName=IDX_FU_CONSENT, tableName=FED_USER_CONSENT; createIndex indexName=IDX_FU_CONSENT_RU, tableName=FED_USER_CONSENT; createIndex indexName=IDX_FU_CREDENTIAL, t...		\N	3.5.4	\N	\N	5685867745
3.4.1	psilva@redhat.com	META-INF/jpa-changelog-3.4.1.xml	2019-08-13 08:44:30.592982	52	EXECUTED	7:c155566c42b4d14ef07059ec3b3bbd8e	modifyDataType columnName=VALUE, tableName=CLIENT_ATTRIBUTES		\N	3.5.4	\N	\N	5685867745
3.4.2	keycloak	META-INF/jpa-changelog-3.4.2.xml	2019-08-13 08:44:30.599924	53	EXECUTED	7:b40376581f12d70f3c89ba8ddf5b7dea	update tableName=REALM		\N	3.5.4	\N	\N	5685867745
3.4.2-KEYCLOAK-5172	mkanis@redhat.com	META-INF/jpa-changelog-3.4.2.xml	2019-08-13 08:44:30.60666	54	EXECUTED	7:a1132cc395f7b95b3646146c2e38f168	update tableName=CLIENT		\N	3.5.4	\N	\N	5685867745
4.0.0-KEYCLOAK-6335	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2019-08-13 08:44:30.619121	55	EXECUTED	7:d8dc5d89c789105cfa7ca0e82cba60af	createTable tableName=CLIENT_AUTH_FLOW_BINDINGS; addPrimaryKey constraintName=C_CLI_FLOW_BIND, tableName=CLIENT_AUTH_FLOW_BINDINGS		\N	3.5.4	\N	\N	5685867745
4.0.0-CLEANUP-UNUSED-TABLE	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2019-08-13 08:44:30.624699	56	EXECUTED	7:7822e0165097182e8f653c35517656a3	dropTable tableName=CLIENT_IDENTITY_PROV_MAPPING		\N	3.5.4	\N	\N	5685867745
4.0.0-KEYCLOAK-6228	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2019-08-13 08:44:30.681852	57	EXECUTED	7:c6538c29b9c9a08f9e9ea2de5c2b6375	dropUniqueConstraint constraintName=UK_JKUWUVD56ONTGSUHOGM8UEWRT, tableName=USER_CONSENT; dropNotNullConstraint columnName=CLIENT_ID, tableName=USER_CONSENT; addColumn tableName=USER_CONSENT; addUniqueConstraint constraintName=UK_JKUWUVD56ONTGSUHO...		\N	3.5.4	\N	\N	5685867745
4.0.0-KEYCLOAK-5579-fixed	mposolda@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2019-08-13 08:44:30.838936	58	EXECUTED	7:6d4893e36de22369cf73bcb051ded875	dropForeignKeyConstraint baseTableName=CLIENT_TEMPLATE_ATTRIBUTES, constraintName=FK_CL_TEMPL_ATTR_TEMPL; renameTable newTableName=CLIENT_SCOPE_ATTRIBUTES, oldTableName=CLIENT_TEMPLATE_ATTRIBUTES; renameColumn newColumnName=SCOPE_ID, oldColumnName...		\N	3.5.4	\N	\N	5685867745
authz-4.0.0.CR1	psilva@redhat.com	META-INF/jpa-changelog-authz-4.0.0.CR1.xml	2019-08-13 08:44:30.951913	59	EXECUTED	7:57960fc0b0f0dd0563ea6f8b2e4a1707	createTable tableName=RESOURCE_SERVER_PERM_TICKET; addPrimaryKey constraintName=CONSTRAINT_FAPMT, tableName=RESOURCE_SERVER_PERM_TICKET; addForeignKeyConstraint baseTableName=RESOURCE_SERVER_PERM_TICKET, constraintName=FK_FRSRHO213XCX4WNKOG82SSPMT...		\N	3.5.4	\N	\N	5685867745
authz-4.0.0.Beta3	psilva@redhat.com	META-INF/jpa-changelog-authz-4.0.0.Beta3.xml	2019-08-13 08:44:30.96676	60	EXECUTED	7:2b4b8bff39944c7097977cc18dbceb3b	addColumn tableName=RESOURCE_SERVER_POLICY; addColumn tableName=RESOURCE_SERVER_PERM_TICKET; addForeignKeyConstraint baseTableName=RESOURCE_SERVER_PERM_TICKET, constraintName=FK_FRSRPO2128CX4WNKOG82SSRFY, referencedTableName=RESOURCE_SERVER_POLICY		\N	3.5.4	\N	\N	5685867745
authz-4.2.0.Final	mhajas@redhat.com	META-INF/jpa-changelog-authz-4.2.0.Final.xml	2019-08-13 08:44:30.989326	61	EXECUTED	7:2aa42a964c59cd5b8ca9822340ba33a8	createTable tableName=RESOURCE_URIS; addForeignKeyConstraint baseTableName=RESOURCE_URIS, constraintName=FK_RESOURCE_SERVER_URIS, referencedTableName=RESOURCE_SERVER_RESOURCE; customChange; dropColumn columnName=URI, tableName=RESOURCE_SERVER_RESO...		\N	3.5.4	\N	\N	5685867745
4.2.0-KEYCLOAK-6313	wadahiro@gmail.com	META-INF/jpa-changelog-4.2.0.xml	2019-08-13 08:44:30.997714	62	EXECUTED	7:14d407c35bc4fe1976867756bcea0c36	addColumn tableName=REQUIRED_ACTION_PROVIDER		\N	3.5.4	\N	\N	5685867745
4.3.0-KEYCLOAK-7984	wadahiro@gmail.com	META-INF/jpa-changelog-4.3.0.xml	2019-08-13 08:44:31.003725	63	EXECUTED	7:241a8030c748c8548e346adee548fa93	update tableName=REQUIRED_ACTION_PROVIDER		\N	3.5.4	\N	\N	5685867745
4.6.0-KEYCLOAK-7950	psilva@redhat.com	META-INF/jpa-changelog-4.6.0.xml	2019-08-13 08:44:31.010017	64	EXECUTED	7:7d3182f65a34fcc61e8d23def037dc3f	update tableName=RESOURCE_SERVER_RESOURCE		\N	3.5.4	\N	\N	5685867745
4.6.0-KEYCLOAK-8377	keycloak	META-INF/jpa-changelog-4.6.0.xml	2019-08-13 08:44:31.034208	65	EXECUTED	7:b30039e00a0b9715d430d1b0636728fa	createTable tableName=ROLE_ATTRIBUTE; addPrimaryKey constraintName=CONSTRAINT_ROLE_ATTRIBUTE_PK, tableName=ROLE_ATTRIBUTE; addForeignKeyConstraint baseTableName=ROLE_ATTRIBUTE, constraintName=FK_ROLE_ATTRIBUTE_ID, referencedTableName=KEYCLOAK_ROLE...		\N	3.5.4	\N	\N	5685867745
4.6.0-KEYCLOAK-8555	gideonray@gmail.com	META-INF/jpa-changelog-4.6.0.xml	2019-08-13 08:44:31.041791	66	EXECUTED	7:3797315ca61d531780f8e6f82f258159	createIndex indexName=IDX_COMPONENT_PROVIDER_TYPE, tableName=COMPONENT		\N	3.5.4	\N	\N	5685867745
4.7.0-KEYCLOAK-1267	sguilhen@redhat.com	META-INF/jpa-changelog-4.7.0.xml	2019-08-13 08:44:31.085691	67	EXECUTED	7:c7aa4c8d9573500c2d347c1941ff0301	addColumn tableName=REALM		\N	3.5.4	\N	\N	5685867745
4.7.0-KEYCLOAK-7275	keycloak	META-INF/jpa-changelog-4.7.0.xml	2019-08-13 08:44:31.126874	68	EXECUTED	7:b207faee394fc074a442ecd42185a5dd	renameColumn newColumnName=CREATED_ON, oldColumnName=LAST_SESSION_REFRESH, tableName=OFFLINE_USER_SESSION; addNotNullConstraint columnName=CREATED_ON, tableName=OFFLINE_USER_SESSION; addColumn tableName=OFFLINE_USER_SESSION; customChange; createIn...		\N	3.5.4	\N	\N	5685867745
4.8.0-KEYCLOAK-8835	sguilhen@redhat.com	META-INF/jpa-changelog-4.8.0.xml	2019-08-13 08:44:31.139572	69	EXECUTED	7:ab9a9762faaba4ddfa35514b212c4922	addNotNullConstraint columnName=SSO_MAX_LIFESPAN_REMEMBER_ME, tableName=REALM; addNotNullConstraint columnName=SSO_IDLE_TIMEOUT_REMEMBER_ME, tableName=REALM		\N	3.5.4	\N	\N	5685867745
authz-4.2.0.Final-KEYCLOAK-9944	hmlnarik@redhat.com	META-INF/jpa-changelog-authz-4.2.0.Final.xml	2021-10-20 09:14:07.046091	70	EXECUTED	7:9ac9e58545479929ba23f4a3087a0346	addPrimaryKey constraintName=CONSTRAINT_RESOUR_URIS_PK, tableName=RESOURCE_URIS		\N	3.5.4	\N	\N	4721247018
authz-7.0.0-KEYCLOAK-10443	psilva@redhat.com	META-INF/jpa-changelog-authz-7.0.0.xml	2021-10-20 09:14:07.063102	71	EXECUTED	7:b9710f74515a6ccb51b72dc0d19df8c4	addColumn tableName=RESOURCE_SERVER		\N	3.5.4	\N	\N	4721247018
8.0.0-adding-credential-columns	keycloak	META-INF/jpa-changelog-8.0.0.xml	2021-10-20 09:14:07.075418	72	EXECUTED	7:ec9707ae4d4f0b7452fee20128083879	addColumn tableName=CREDENTIAL; addColumn tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	4721247018
8.0.0-updating-credential-data-not-oracle-fixed	keycloak	META-INF/jpa-changelog-8.0.0.xml	2021-10-20 09:14:07.08791	73	EXECUTED	7:3979a0ae07ac465e920ca696532fc736	update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	4721247018
8.0.0-updating-credential-data-oracle-fixed	keycloak	META-INF/jpa-changelog-8.0.0.xml	2021-10-20 09:14:07.092757	74	MARK_RAN	7:5abfde4c259119d143bd2fbf49ac2bca	update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	4721247018
8.0.0-credential-cleanup-fixed	keycloak	META-INF/jpa-changelog-8.0.0.xml	2021-10-20 09:14:07.120454	75	EXECUTED	7:b48da8c11a3d83ddd6b7d0c8c2219345	dropDefaultValue columnName=COUNTER, tableName=CREDENTIAL; dropDefaultValue columnName=DIGITS, tableName=CREDENTIAL; dropDefaultValue columnName=PERIOD, tableName=CREDENTIAL; dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; dropColumn ...		\N	3.5.4	\N	\N	4721247018
8.0.0-resource-tag-support	keycloak	META-INF/jpa-changelog-8.0.0.xml	2021-10-20 09:14:07.182839	76	EXECUTED	7:a73379915c23bfad3e8f5c6d5c0aa4bd	addColumn tableName=MIGRATION_MODEL; createIndex indexName=IDX_UPDATE_TIME, tableName=MIGRATION_MODEL		\N	3.5.4	\N	\N	4721247018
9.0.0-always-display-client	keycloak	META-INF/jpa-changelog-9.0.0.xml	2021-10-20 09:14:07.204359	77	EXECUTED	7:39e0073779aba192646291aa2332493d	addColumn tableName=CLIENT		\N	3.5.4	\N	\N	4721247018
9.0.0-drop-constraints-for-column-increase	keycloak	META-INF/jpa-changelog-9.0.0.xml	2021-10-20 09:14:07.20893	78	MARK_RAN	7:81f87368f00450799b4bf42ea0b3ec34	dropUniqueConstraint constraintName=UK_FRSR6T700S9V50BU18WS5PMT, tableName=RESOURCE_SERVER_PERM_TICKET; dropUniqueConstraint constraintName=UK_FRSR6T700S9V50BU18WS5HA6, tableName=RESOURCE_SERVER_RESOURCE; dropPrimaryKey constraintName=CONSTRAINT_O...		\N	3.5.4	\N	\N	4721247018
9.0.0-increase-column-size-federated-fk	keycloak	META-INF/jpa-changelog-9.0.0.xml	2021-10-20 09:14:07.236607	79	EXECUTED	7:20b37422abb9fb6571c618148f013a15	modifyDataType columnName=CLIENT_ID, tableName=FED_USER_CONSENT; modifyDataType columnName=CLIENT_REALM_CONSTRAINT, tableName=KEYCLOAK_ROLE; modifyDataType columnName=OWNER, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=CLIENT_ID, ta...		\N	3.5.4	\N	\N	4721247018
9.0.0-recreate-constraints-after-column-increase	keycloak	META-INF/jpa-changelog-9.0.0.xml	2021-10-20 09:14:07.241474	80	MARK_RAN	7:1970bb6cfb5ee800736b95ad3fb3c78a	addNotNullConstraint columnName=CLIENT_ID, tableName=OFFLINE_CLIENT_SESSION; addNotNullConstraint columnName=OWNER, tableName=RESOURCE_SERVER_PERM_TICKET; addNotNullConstraint columnName=REQUESTER, tableName=RESOURCE_SERVER_PERM_TICKET; addNotNull...		\N	3.5.4	\N	\N	4721247018
9.0.1-add-index-to-client.client_id	keycloak	META-INF/jpa-changelog-9.0.1.xml	2021-10-20 09:14:07.281412	81	EXECUTED	7:45d9b25fc3b455d522d8dcc10a0f4c80	createIndex indexName=IDX_CLIENT_ID, tableName=CLIENT		\N	3.5.4	\N	\N	4721247018
9.0.1-KEYCLOAK-12579-drop-constraints	keycloak	META-INF/jpa-changelog-9.0.1.xml	2021-10-20 09:14:07.284622	82	MARK_RAN	7:890ae73712bc187a66c2813a724d037f	dropUniqueConstraint constraintName=SIBLING_NAMES, tableName=KEYCLOAK_GROUP		\N	3.5.4	\N	\N	4721247018
9.0.1-KEYCLOAK-12579-add-not-null-constraint	keycloak	META-INF/jpa-changelog-9.0.1.xml	2021-10-20 09:14:07.290005	83	EXECUTED	7:0a211980d27fafe3ff50d19a3a29b538	addNotNullConstraint columnName=PARENT_GROUP, tableName=KEYCLOAK_GROUP		\N	3.5.4	\N	\N	4721247018
9.0.1-KEYCLOAK-12579-recreate-constraints	keycloak	META-INF/jpa-changelog-9.0.1.xml	2021-10-20 09:14:07.292845	84	MARK_RAN	7:a161e2ae671a9020fff61e996a207377	addUniqueConstraint constraintName=SIBLING_NAMES, tableName=KEYCLOAK_GROUP		\N	3.5.4	\N	\N	4721247018
9.0.1-add-index-to-events	keycloak	META-INF/jpa-changelog-9.0.1.xml	2021-10-20 09:14:07.323549	85	EXECUTED	7:01c49302201bdf815b0a18d1f98a55dc	createIndex indexName=IDX_EVENT_TIME, tableName=EVENT_ENTITY		\N	3.5.4	\N	\N	4721247018
map-remove-ri	keycloak	META-INF/jpa-changelog-11.0.0.xml	2021-10-20 09:14:07.332617	86	EXECUTED	7:3dace6b144c11f53f1ad2c0361279b86	dropForeignKeyConstraint baseTableName=REALM, constraintName=FK_TRAF444KK6QRKMS7N56AIWQ5Y; dropForeignKeyConstraint baseTableName=KEYCLOAK_ROLE, constraintName=FK_KJHO5LE2C0RAL09FL8CM9WFW9		\N	3.5.4	\N	\N	4721247018
map-remove-ri	keycloak	META-INF/jpa-changelog-12.0.0.xml	2021-10-20 09:14:07.345004	87	EXECUTED	7:578d0b92077eaf2ab95ad0ec087aa903	dropForeignKeyConstraint baseTableName=REALM_DEFAULT_GROUPS, constraintName=FK_DEF_GROUPS_GROUP; dropForeignKeyConstraint baseTableName=REALM_DEFAULT_ROLES, constraintName=FK_H4WPD7W4HSOOLNI3H0SW7BTJE; dropForeignKeyConstraint baseTableName=CLIENT...		\N	3.5.4	\N	\N	4721247018
12.1.0-add-realm-localization-table	keycloak	META-INF/jpa-changelog-12.0.0.xml	2021-10-20 09:14:07.361393	88	EXECUTED	7:c95abe90d962c57a09ecaee57972835d	createTable tableName=REALM_LOCALIZATIONS; addPrimaryKey tableName=REALM_LOCALIZATIONS		\N	3.5.4	\N	\N	4721247018
default-roles	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.395322	89	EXECUTED	7:f1313bcc2994a5c4dc1062ed6d8282d3	addColumn tableName=REALM; customChange		\N	3.5.4	\N	\N	4721247018
default-roles-cleanup	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.406325	90	EXECUTED	7:90d763b52eaffebefbcbde55f269508b	dropTable tableName=REALM_DEFAULT_ROLES; dropTable tableName=CLIENT_DEFAULT_ROLES		\N	3.5.4	\N	\N	4721247018
13.0.0-KEYCLOAK-16844	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.442094	91	EXECUTED	7:d554f0cb92b764470dccfa5e0014a7dd	createIndex indexName=IDX_OFFLINE_USS_PRELOAD, tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	4721247018
map-remove-ri-13.0.0	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.4513	92	EXECUTED	7:73193e3ab3c35cf0f37ccea3bf783764	dropForeignKeyConstraint baseTableName=DEFAULT_CLIENT_SCOPE, constraintName=FK_R_DEF_CLI_SCOPE_SCOPE; dropForeignKeyConstraint baseTableName=CLIENT_SCOPE_CLIENT, constraintName=FK_C_CLI_SCOPE_SCOPE; dropForeignKeyConstraint baseTableName=CLIENT_SC...		\N	3.5.4	\N	\N	4721247018
13.0.0-KEYCLOAK-17992-drop-constraints	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.454055	93	MARK_RAN	7:90a1e74f92e9cbaa0c5eab80b8a037f3	dropPrimaryKey constraintName=C_CLI_SCOPE_BIND, tableName=CLIENT_SCOPE_CLIENT; dropIndex indexName=IDX_CLSCOPE_CL, tableName=CLIENT_SCOPE_CLIENT; dropIndex indexName=IDX_CL_CLSCOPE, tableName=CLIENT_SCOPE_CLIENT		\N	3.5.4	\N	\N	4721247018
13.0.0-increase-column-size-federated	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.464824	94	EXECUTED	7:5b9248f29cd047c200083cc6d8388b16	modifyDataType columnName=CLIENT_ID, tableName=CLIENT_SCOPE_CLIENT; modifyDataType columnName=SCOPE_ID, tableName=CLIENT_SCOPE_CLIENT		\N	3.5.4	\N	\N	4721247018
13.0.0-KEYCLOAK-17992-recreate-constraints	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.468907	95	MARK_RAN	7:64db59e44c374f13955489e8990d17a1	addNotNullConstraint columnName=CLIENT_ID, tableName=CLIENT_SCOPE_CLIENT; addNotNullConstraint columnName=SCOPE_ID, tableName=CLIENT_SCOPE_CLIENT; addPrimaryKey constraintName=C_CLI_SCOPE_BIND, tableName=CLIENT_SCOPE_CLIENT; createIndex indexName=...		\N	3.5.4	\N	\N	4721247018
json-string-accomodation-fixed	keycloak	META-INF/jpa-changelog-13.0.0.xml	2021-10-20 09:14:07.477267	96	EXECUTED	7:329a578cdb43262fff975f0a7f6cda60	addColumn tableName=REALM_ATTRIBUTE; update tableName=REALM_ATTRIBUTE; dropColumn columnName=VALUE, tableName=REALM_ATTRIBUTE; renameColumn newColumnName=VALUE, oldColumnName=VALUE_NEW, tableName=REALM_ATTRIBUTE		\N	3.5.4	\N	\N	4721247018
14.0.0-KEYCLOAK-11019	keycloak	META-INF/jpa-changelog-14.0.0.xml	2021-10-20 09:14:07.550039	97	EXECUTED	7:fae0de241ac0fd0bbc2b380b85e4f567	createIndex indexName=IDX_OFFLINE_CSS_PRELOAD, tableName=OFFLINE_CLIENT_SESSION; createIndex indexName=IDX_OFFLINE_USS_BY_USER, tableName=OFFLINE_USER_SESSION; createIndex indexName=IDX_OFFLINE_USS_BY_USERSESS, tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	4721247018
14.0.0-KEYCLOAK-18286	keycloak	META-INF/jpa-changelog-14.0.0.xml	2021-10-20 09:14:07.574571	98	EXECUTED	7:075d54e9180f49bb0c64ca4218936e81	createIndex indexName=IDX_CLIENT_ATT_BY_NAME_VALUE, tableName=CLIENT_ATTRIBUTES		\N	3.5.4	\N	\N	4721247018
14.0.0-KEYCLOAK-18286-mysql	keycloak	META-INF/jpa-changelog-14.0.0.xml	2021-10-20 09:14:07.577269	99	MARK_RAN	7:b558ad47ea0e4d3c3514225a49cc0d65	createIndex indexName=IDX_CLIENT_ATT_BY_NAME_VALUE, tableName=CLIENT_ATTRIBUTES		\N	3.5.4	\N	\N	4721247018
KEYCLOAK-17267-add-index-to-user-attributes	keycloak	META-INF/jpa-changelog-14.0.0.xml	2021-10-20 09:14:07.609097	100	EXECUTED	7:1a7f28ff8d9e53aeb879d76ea3d9341a	createIndex indexName=IDX_USER_ATTRIBUTE_NAME, tableName=USER_ATTRIBUTE		\N	3.5.4	\N	\N	4721247018
KEYCLOAK-18146-add-saml-art-binding-identifier	keycloak	META-INF/jpa-changelog-14.0.0.xml	2021-10-20 09:14:07.617847	101	EXECUTED	7:2fd554456fed4a82c698c555c5b751b6	customChange		\N	3.5.4	\N	\N	4721247018
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
1000	f	\N	\N
1001	f	\N	\N
\.


--
-- Data for Name: default_client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.default_client_scope (realm_id, scope_id, default_scope) FROM stdin;
master	01d946a1-1cbe-4115-baa3-f318f98063cc	f
master	ff5789c8-4bb4-44c4-885f-a68d50e376ee	t
master	dca376d8-cb66-4f66-a8eb-982b522bf009	t
master	43c711ac-8d05-4374-962e-994721d09c71	t
master	0c44a86a-d544-4d25-93ed-bb5f3cde8f08	f
master	95d9bce2-c1e5-49a9-8071-2a79b5489b44	f
master	ae3e0992-298c-42b0-bda3-c4671c460581	t
master	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9	t
francoralite	2b4e74c3-c90b-4ea1-b5b5-dfb820147896	t
francoralite	2bac4725-31a5-4315-bd97-562b7c764e2c	t
francoralite	959efe5f-5b43-4d64-90f9-f52dda2eb527	t
francoralite	0630fe1b-3718-401b-9aeb-5f4530d97637	t
francoralite	34ad7985-88ba-405d-a0ad-12ec0a905b8a	t
francoralite	6b2ca845-56e5-456b-aa30-d582da23dc7f	f
francoralite	a1274aaa-071f-46ae-bd24-807227b4a2c6	f
francoralite	4cef35b9-dbad-41c5-b76c-448c12b35cea	f
francoralite	b9996171-4af7-4c35-be93-8b799022b095	f
master	b6429998-dfca-4d5b-a0ca-300fcfa243ed	f
\.


--
-- Data for Name: event_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.event_entity (id, client_id, details_json, error, ip_address, realm_id, session_id, event_time, type, user_id) FROM stdin;
\.


--
-- Data for Name: fed_user_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_attribute (id, name, user_id, realm_id, storage_provider_id, value) FROM stdin;
\.


--
-- Data for Name: fed_user_consent; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_consent (id, client_id, user_id, realm_id, storage_provider_id, created_date, last_updated_date, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: fed_user_consent_cl_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_consent_cl_scope (user_consent_id, scope_id) FROM stdin;
\.


--
-- Data for Name: fed_user_credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_credential (id, salt, type, created_date, user_id, realm_id, storage_provider_id, user_label, secret_data, credential_data, priority) FROM stdin;
\.


--
-- Data for Name: fed_user_group_membership; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_group_membership (group_id, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: fed_user_required_action; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_required_action (required_action, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: fed_user_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_role_mapping (role_id, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: federated_identity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.federated_identity (identity_provider, realm_id, federated_user_id, federated_username, token, user_id) FROM stdin;
\.


--
-- Data for Name: federated_user; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.federated_user (id, storage_provider_id, realm_id) FROM stdin;
\.


--
-- Data for Name: group_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.group_attribute (id, name, value, group_id) FROM stdin;
\.


--
-- Data for Name: group_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.group_role_mapping (role_id, group_id) FROM stdin;
a3aa0084-b3a2-4bb9-bbc0-ea88991d6017	81f3b075-bc53-42ec-870a-67153ce10b51
3c4f030e-51c7-489f-8f13-de85cf5a520d	81f3b075-bc53-42ec-870a-67153ce10b51
afb187be-f83f-4122-a9d9-d609d1b85251	8baef50e-741a-41d8-bbff-0e5cc18b7211
b801d083-6c88-4157-8d7e-303000280b1e	8baef50e-741a-41d8-bbff-0e5cc18b7211
7f2da254-71c1-452b-b1e7-ab89ef429d94	8d6d3d77-1c07-48fc-b5fa-83b2a6b4dee2
b012abe9-4360-4c1e-ad3f-7cedb43e5e4d	8d6d3d77-1c07-48fc-b5fa-83b2a6b4dee2
\.


--
-- Data for Name: identity_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider (internal_id, enabled, provider_alias, provider_id, store_token, authenticate_by_default, realm_id, add_token_role, trust_email, first_broker_login_flow_id, post_broker_login_flow_id, provider_display_name, link_only) FROM stdin;
\.


--
-- Data for Name: identity_provider_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider_config (identity_provider_id, value, name) FROM stdin;
\.


--
-- Data for Name: identity_provider_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider_mapper (id, name, idp_alias, idp_mapper_name, realm_id) FROM stdin;
\.


--
-- Data for Name: idp_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.idp_mapper_config (idp_mapper_id, value, name) FROM stdin;
\.


--
-- Data for Name: keycloak_group; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.keycloak_group (id, name, parent_group, realm_id) FROM stdin;
81f3b075-bc53-42ec-870a-67153ce10b51	francoralite-administrators	 	francoralite
8baef50e-741a-41d8-bbff-0e5cc18b7211	francoralite-contributors	 	francoralite
8d6d3d77-1c07-48fc-b5fa-83b2a6b4dee2	francoralite-users	 	francoralite
\.


--
-- Data for Name: keycloak_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.keycloak_role (id, client_realm_constraint, client_role, description, name, realm_id, client, realm) FROM stdin;
398b3395-34b8-4668-9296-05ba7eb64bbb	master	f	${role_admin}	admin	master	\N	master
636a3642-167a-432f-a6af-1c0630e1d3d5	master	f	${role_create-realm}	create-realm	master	\N	master
26e019a5-44f6-404b-88b4-6b05b9846883	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_create-client}	create-client	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
9be3b9f1-9fb4-46c1-906e-7ca638901fb5	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-realm}	view-realm	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
f9d9318c-e4a6-4b36-a0f0-b9b19209e510	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-users}	view-users	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
0e2a1a49-3f04-443f-b413-ed096fbc3db1	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-clients}	view-clients	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
2543c7c6-6d57-496a-8684-fce33b9676e3	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-events}	view-events	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
3c8882f0-a30b-4509-8874-6a0dd8e0f669	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-identity-providers}	view-identity-providers	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
76fdc691-104d-4f70-98fc-2cbeb6c45658	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_view-authorization}	view-authorization	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
ab5cc34c-5d27-4ad5-802f-fc87e9340cfd	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-realm}	manage-realm	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
e3f59d89-0dff-4fa5-a7b1-a3ab7dde510e	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-users}	manage-users	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
4765895f-7470-4702-b641-6045f6f6beca	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-clients}	manage-clients	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
926c9477-dbfb-44f1-892c-2069beaabb1b	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-events}	manage-events	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
5ea284a4-c64c-4fd3-9630-e5f685aef233	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-identity-providers}	manage-identity-providers	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
4cde772d-ed4b-45f5-a3ad-2a9d827da1cb	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_manage-authorization}	manage-authorization	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
91b25ecc-17aa-4e61-b80f-92ffae4a2596	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_query-users}	query-users	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
083d0f99-5fe3-4993-8540-ca638edf3a5b	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_query-clients}	query-clients	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
a738a78e-752f-4836-b8e7-5f91d9c79cf4	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_query-realms}	query-realms	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
dca87bca-200e-4e31-8d67-868e02e4e6d5	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_query-groups}	query-groups	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
8f8f910c-2f7c-4bec-b66f-d7058b53e4c5	310aabaf-651c-4959-b441-8fe27129a418	t	${role_view-profile}	view-profile	master	310aabaf-651c-4959-b441-8fe27129a418	\N
d5447076-ea4f-4493-b0f9-dbea011ad108	310aabaf-651c-4959-b441-8fe27129a418	t	${role_manage-account}	manage-account	master	310aabaf-651c-4959-b441-8fe27129a418	\N
39965e67-dd49-4054-874a-5ce643fe1149	310aabaf-651c-4959-b441-8fe27129a418	t	${role_manage-account-links}	manage-account-links	master	310aabaf-651c-4959-b441-8fe27129a418	\N
3f97fe5c-0610-4120-9f9f-2391a032c7b8	d91bc61c-3f73-4e3a-add6-55fc753a31ec	t	${role_read-token}	read-token	master	d91bc61c-3f73-4e3a-add6-55fc753a31ec	\N
a1701289-7090-46d3-9f81-4bba96a05fd0	9b3d814d-33ff-45fd-9f13-a489b550ae9e	t	${role_impersonation}	impersonation	master	9b3d814d-33ff-45fd-9f13-a489b550ae9e	\N
b9c894e7-60c9-47ff-bbb4-db20b880c2d9	master	f	${role_offline-access}	offline_access	master	\N	master
59163355-f8e4-43f5-9064-c34167799f8f	master	f	${role_uma_authorization}	uma_authorization	master	\N	master
6d3855c3-6964-4931-8af6-4a471acbc6c9	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_create-client}	create-client	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
485b20a6-7568-42e7-8b73-ae178e8aa1dd	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-realm}	view-realm	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
01022f0e-4ca5-4315-af91-6a20189b7c7d	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-users}	view-users	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
69073716-b9e8-4188-976f-e42afc6e9471	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-clients}	view-clients	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
1bc444d1-48d7-42d1-ac21-3f09ca23c49a	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-events}	view-events	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
eb68b146-9ee6-429d-8e97-e04f7da191b0	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-identity-providers}	view-identity-providers	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
99ace0f9-25de-4b9c-95e3-dca31b2351dd	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_view-authorization}	view-authorization	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
b5002289-a0a2-496c-b2d0-6c8ee6dc0071	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-realm}	manage-realm	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
83ff8fbc-63d5-431b-ad71-214e0d568ace	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-users}	manage-users	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
11297344-68b2-4d05-9581-029ccd3a3e71	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-clients}	manage-clients	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
0b4fe154-70b7-40e9-abdc-ae3ba6d34b44	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-events}	manage-events	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
b052bc08-bef9-44c9-9aac-450a0971ed33	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-identity-providers}	manage-identity-providers	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
11155683-35f4-4080-8346-2e4097112e68	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_manage-authorization}	manage-authorization	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
b4e99917-8faf-4edf-8dcf-52f88b8eab7a	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_query-users}	query-users	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
1d65077e-2297-44fb-8fd7-08ca17420ff9	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_query-clients}	query-clients	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
24810ecb-1090-4c0d-9675-70a8f6e8a2da	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_query-realms}	query-realms	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
8371eb96-4637-4713-a308-7f37f4bc6f51	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_query-groups}	query-groups	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
b684e64f-9250-42e0-a055-2a18ffa4df88	francoralite	f	${role_uma_authorization}	uma_authorization	francoralite	\N	francoralite
afb187be-f83f-4122-a9d9-d609d1b85251	francoralite	f	\N	francoralite-contributors	francoralite	\N	francoralite
818c584b-976b-40ee-a442-403c98bb668c	francoralite	f	${role_offline-access}	offline_access	francoralite	\N	francoralite
7f2da254-71c1-452b-b1e7-ab89ef429d94	francoralite	f	\N	francoralite-users	francoralite	\N	francoralite
a3aa0084-b3a2-4bb9-bbc0-ea88991d6017	francoralite	f	\N	francoralite-administrators	francoralite	\N	francoralite
b39fa7d2-1db7-466f-8151-e26d9a9e38ab	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-events}	manage-events	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
0d7e15c9-2c4d-446a-9287-2a37abb0e0ab	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-realm}	manage-realm	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
3184fc22-943f-4425-a50d-aea41d91b69a	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-identity-providers}	manage-identity-providers	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
6769e846-0726-42ff-b07b-46974672176c	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-identity-providers}	view-identity-providers	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
bef7cb79-04f1-46da-8ddd-728933ed4383	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_query-realms}	query-realms	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
7fedc9e8-90ea-4a77-898f-3b3fd6d01715	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-events}	view-events	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
383ce563-296d-48b4-a266-146cc84c6d43	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-authorization}	view-authorization	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
186a2ce5-0edd-4b05-b524-fceeae08f630	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-authorization}	manage-authorization	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
79f75c48-faa6-4f82-8f35-b396ce9ebb5a	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_query-users}	query-users	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
95b8d4d7-001b-4581-bc55-4e3513d6cf14	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-clients}	manage-clients	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
201d06f3-dc5d-4a59-af26-dfd843ce449f	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-realm}	view-realm	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
a62d9cd0-0166-4c69-a5d4-685c8de4feca	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_create-client}	create-client	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
4d2300e9-49ab-4097-905a-9629824afd41	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_manage-users}	manage-users	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
cce275a3-4210-46e5-83e9-5a00e6c7b9a6	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_impersonation}	impersonation	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
41603418-57aa-4736-8f27-b7f24054a9a3	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_query-groups}	query-groups	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
95ace2ba-e3db-4730-b36f-7267c80f90d5	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-users}	view-users	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
35bbea1c-2fc8-473d-a1c2-df3a8817b6d7	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_query-clients}	query-clients	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
9200e548-99db-4699-be64-d60aedc3a4f6	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_realm-admin}	realm-admin	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
2b64f08e-5007-4e1c-ba43-0961a04d27e4	d2805f14-3eeb-490f-b559-eb0ad43364f9	t	${role_view-clients}	view-clients	francoralite	d2805f14-3eeb-490f-b559-eb0ad43364f9	\N
3d8b9944-d052-4e94-aba8-36358a0b5638	6ca8b749-cba1-4453-8a20-0c189d9b9447	t	\N	uma_protection	francoralite	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
3c4f030e-51c7-489f-8f13-de85cf5a520d	6ca8b749-cba1-4453-8a20-0c189d9b9447	t	\N	francoralite-administrators	francoralite	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b012abe9-4360-4c1e-ad3f-7cedb43e5e4d	6ca8b749-cba1-4453-8a20-0c189d9b9447	t	\N	francoralite-users	francoralite	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b801d083-6c88-4157-8d7e-303000280b1e	6ca8b749-cba1-4453-8a20-0c189d9b9447	t	\N	francoralite-contributors	francoralite	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1b33a084-8e12-4fb4-a21c-b90aab4c4884	e8efb165-82f9-405c-98aa-e8535badd8ad	t	${role_read-token}	read-token	francoralite	e8efb165-82f9-405c-98aa-e8535badd8ad	\N
5531c621-ad97-4da9-8896-bed73d09c285	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_manage-account}	manage-account	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
850b0803-fc35-445d-a23e-d6479241bb60	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_view-profile}	view-profile	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
12faee8b-64db-41cb-97cf-7c085d3cd410	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_manage-account-links}	manage-account-links	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
3169b997-86b7-4d6c-a419-54f797a09030	ac6a2e53-830b-44ee-8fc0-775bb105330d	t	${role_impersonation}	impersonation	master	ac6a2e53-830b-44ee-8fc0-775bb105330d	\N
cf336c4f-f1fc-447b-a686-2f44ac81a67f	francoralite	f	${role_default-roles-francoralite}	default-roles-francoralite	francoralite	\N	francoralite
7079ef4e-6e2e-4bda-91d8-cf52142687be	master	f	${role_default-roles-master}	default-roles-master	master	\N	master
c1faf604-09fa-4139-947b-85ae8d6f65e1	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_view-applications}	view-applications	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
c72cf68d-44f2-423d-a684-d08c2bebac81	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_view-consent}	view-consent	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
6c0ac76f-a3f4-49b1-9faf-7c59a795e278	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_manage-consent}	manage-consent	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
2e4e7a56-04b3-429e-95ad-d6fa7df67ec8	310aabaf-651c-4959-b441-8fe27129a418	t	${role_view-applications}	view-applications	master	310aabaf-651c-4959-b441-8fe27129a418	\N
17be79a5-a074-400f-b655-5f5ed9d35074	310aabaf-651c-4959-b441-8fe27129a418	t	${role_view-consent}	view-consent	master	310aabaf-651c-4959-b441-8fe27129a418	\N
c2374f6d-7c7f-412f-a39f-a1c1229ae84e	310aabaf-651c-4959-b441-8fe27129a418	t	${role_manage-consent}	manage-consent	master	310aabaf-651c-4959-b441-8fe27129a418	\N
de76cc98-9788-4e26-86a6-8eceeaa50506	f896f42d-66e6-498f-bdc0-a90216659041	t	${role_delete-account}	delete-account	francoralite	f896f42d-66e6-498f-bdc0-a90216659041	\N
7e030173-892c-4515-8440-19e997e9ddc3	310aabaf-651c-4959-b441-8fe27129a418	t	${role_delete-account}	delete-account	master	310aabaf-651c-4959-b441-8fe27129a418	\N
\.


--
-- Data for Name: migration_model; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.migration_model (id, version, update_time) FROM stdin;
SINGLETON	4.6.0	0
cja8i	14.0.0	1634721254
\.


--
-- Data for Name: offline_client_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.offline_client_session (user_session_id, client_id, offline_flag, "timestamp", data, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: offline_user_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.offline_user_session (user_session_id, user_id, realm_id, created_on, offline_flag, data, last_session_refresh) FROM stdin;
\.


--
-- Data for Name: policy_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.policy_config (policy_id, name, value) FROM stdin;
6cafc604-ca21-48ca-bf77-c1fed388c57a	code	// by default, grants any permission associated with this policy\n$evaluation.grant();\n
3fc46920-3046-4423-9851-db767fbee3c7	roles	[{"id":"b012abe9-4360-4c1e-ad3f-7cedb43e5e4d","required":true}]
b8b552c0-a8ec-44f7-8c6a-70df10e7a149	roles	[{"id":"afb187be-f83f-4122-a9d9-d609d1b85251","required":true}]
f0aef9d4-46df-472b-8192-fd828046233e	defaultResourceType	urn:francoralite:resources:default
47d172b5-7863-4175-9a62-a77cc63cf3da	roles	[{"id":"a3aa0084-b3a2-4bb9-bbc0-ea88991d6017","required":true}]
\.


--
-- Data for Name: protocol_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.protocol_mapper (id, name, protocol, protocol_mapper_name, client_id, client_scope_id) FROM stdin;
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	locale	openid-connect	oidc-usermodel-attribute-mapper	96e0973a-a61d-46a8-b1eb-ecd9e3953c25	\N
5c69905a-5481-4c87-9748-cadd39962376	role list	saml	saml-role-list-mapper	\N	ff5789c8-4bb4-44c4-885f-a68d50e376ee
4258d487-9901-4599-868f-aaadc072643b	full name	openid-connect	oidc-full-name-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
b4f83334-b4e4-4b93-87e4-14b329c5ce79	family name	openid-connect	oidc-usermodel-property-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
120186d9-7fd2-4062-9b69-d56b4ecdc216	given name	openid-connect	oidc-usermodel-property-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
a91de4e1-4bc3-4926-ad73-9d344b289f8e	middle name	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
63a90961-1b19-4665-bc20-a22edb75f593	nickname	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	username	openid-connect	oidc-usermodel-property-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	profile	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
04096e46-d403-461a-8e3a-19e9aee73cef	picture	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	website	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	gender	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	birthdate	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
b9e3bc19-7f61-480f-ab83-e267aef75cbd	zoneinfo	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
fecc870b-d164-4f29-9b36-cd5ff6b50efb	locale	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	updated at	openid-connect	oidc-usermodel-attribute-mapper	\N	dca376d8-cb66-4f66-a8eb-982b522bf009
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	email	openid-connect	oidc-usermodel-property-mapper	\N	43c711ac-8d05-4374-962e-994721d09c71
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	email verified	openid-connect	oidc-usermodel-property-mapper	\N	43c711ac-8d05-4374-962e-994721d09c71
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	address	openid-connect	oidc-address-mapper	\N	0c44a86a-d544-4d25-93ed-bb5f3cde8f08
5aeb6c57-0d21-4096-b881-aa9a7b975779	phone number	openid-connect	oidc-usermodel-attribute-mapper	\N	95d9bce2-c1e5-49a9-8071-2a79b5489b44
7949f9a1-db86-44ae-960d-c0805f120b1a	phone number verified	openid-connect	oidc-usermodel-attribute-mapper	\N	95d9bce2-c1e5-49a9-8071-2a79b5489b44
5314fcb5-4850-4c92-9399-85202275f9bd	realm roles	openid-connect	oidc-usermodel-realm-role-mapper	\N	ae3e0992-298c-42b0-bda3-c4671c460581
ec99bc05-2673-4fac-a7af-3f120cf52a33	client roles	openid-connect	oidc-usermodel-client-role-mapper	\N	ae3e0992-298c-42b0-bda3-c4671c460581
07568b03-ccf1-4e95-9fca-890d1dec4acc	audience resolve	openid-connect	oidc-audience-resolve-mapper	\N	ae3e0992-298c-42b0-bda3-c4671c460581
cae188e3-060a-40e5-94a6-34527c6fb983	allowed web origins	openid-connect	oidc-allowed-origins-mapper	\N	b65ccbb2-ee6a-49c1-841b-f9bcc4c4b4c9
2c4a36d9-cd7e-4a3e-abdb-7e446431b91c	role list	saml	saml-role-list-mapper	\N	2b4e74c3-c90b-4ea1-b5b5-dfb820147896
3cb886f9-8341-4b27-926f-008bfb578256	gender	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
459aa158-4c6f-4492-8248-a51821c6bb74	picture	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	zoneinfo	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
e144add0-ed03-4150-bbaa-24cdcf9f5c35	middle name	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
7e888c80-38c5-44fd-b36e-65300ee63bb9	website	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
694b487c-90f5-4984-a65e-630da67f7e2a	profile	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
6a9a3009-ecec-4683-8e2d-df5f362eb21d	birthdate	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
40471c08-9c11-4cc5-ad4f-2cb13248955e	given name	openid-connect	oidc-usermodel-property-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
6937c087-ed49-45ae-9108-daa77d5fab72	family name	openid-connect	oidc-usermodel-property-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
740b9ebe-083a-4a1e-a678-a3327bb48283	full name	openid-connect	oidc-full-name-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
6f88071e-0a10-432d-850a-45d8ce659430	updated at	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
0c247acd-c76c-408f-bd3b-2ed7153a5f93	locale	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
c2359b33-e367-4b43-85d0-e952fbc38993	username	openid-connect	oidc-usermodel-property-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
d8e82173-e652-49f2-8f2f-df8d2babe8c3	nickname	openid-connect	oidc-usermodel-attribute-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	email	openid-connect	oidc-usermodel-property-mapper	\N	959efe5f-5b43-4d64-90f9-f52dda2eb527
da193473-9cf8-49d9-9a07-b7823f6e43ad	email verified	openid-connect	oidc-usermodel-property-mapper	\N	959efe5f-5b43-4d64-90f9-f52dda2eb527
394e7b35-e5c2-4fa9-8624-b90e5e115383	address	openid-connect	oidc-address-mapper	\N	a1274aaa-071f-46ae-bd24-807227b4a2c6
5da2d08a-f744-4f6c-9301-2a16262cd772	phone number	openid-connect	oidc-usermodel-attribute-mapper	\N	4cef35b9-dbad-41c5-b76c-448c12b35cea
76329181-3bd2-4f58-b0f9-c34853063e11	phone number verified	openid-connect	oidc-usermodel-attribute-mapper	\N	4cef35b9-dbad-41c5-b76c-448c12b35cea
f0f42425-d6a1-4816-bf96-3d150e2dd87a	realm roles	openid-connect	oidc-usermodel-realm-role-mapper	\N	0630fe1b-3718-401b-9aeb-5f4530d97637
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	client roles	openid-connect	oidc-usermodel-client-role-mapper	\N	0630fe1b-3718-401b-9aeb-5f4530d97637
b59e132d-d245-4301-b1f0-af1429b7dfde	audience resolve	openid-connect	oidc-audience-resolve-mapper	\N	0630fe1b-3718-401b-9aeb-5f4530d97637
ed520836-9ae2-4804-bf24-c4c5351df248	allowed web origins	openid-connect	oidc-allowed-origins-mapper	\N	34ad7985-88ba-405d-a0ad-12ec0a905b8a
e33e5c73-4014-48e8-b4d8-ffe74a804374	locale	openid-connect	oidc-usermodel-attribute-mapper	5def7547-cfd3-4473-946c-35f796c52df4	\N
b94426f2-dcdc-4bf9-ab5d-21df027d9796	Client Host	openid-connect	oidc-usersessionmodel-note-mapper	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
be0239db-94bc-498c-ba3f-7a15e27cf0ba	francoralite-pm-audience	openid-connect	oidc-audience-mapper	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4710b262-17fe-46b7-bb27-180c9980bd8d	Client IP Address	openid-connect	oidc-usersessionmodel-note-mapper	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5780c55a-91a3-42f8-b81a-6776f20e17ec	Client ID	openid-connect	oidc-usersessionmodel-note-mapper	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f496f401-ffee-4634-8279-e8d9a1647521	upn	openid-connect	oidc-usermodel-property-mapper	\N	b9996171-4af7-4c35-be93-8b799022b095
99c28bd4-8549-457f-aa92-834fddbb9823	groups	openid-connect	oidc-usermodel-realm-role-mapper	\N	b9996171-4af7-4c35-be93-8b799022b095
cea28dbd-6a83-49fc-82ac-68ac77ea4672	upn	openid-connect	oidc-usermodel-property-mapper	\N	b6429998-dfca-4d5b-a0ca-300fcfa243ed
74748dc2-f3fc-4824-afba-a4fafd6a2054	groups	openid-connect	oidc-usermodel-realm-role-mapper	\N	b6429998-dfca-4d5b-a0ca-300fcfa243ed
bdd72bb8-06eb-4bce-b8f8-5f2be6618aee	audience resolve	openid-connect	oidc-audience-resolve-mapper	dda53ff1-c096-4601-8a8c-30365fde853d	\N
0d920434-3ede-43fd-90d1-5ff58d363ce5	audience resolve	openid-connect	oidc-audience-resolve-mapper	c041d458-ff12-4534-bcb0-cef6017935ab	\N
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	client roles	openid-connect	oidc-usermodel-client-role-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	groups	openid-connect	oidc-usermodel-realm-role-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
713c89aa-bf75-4645-9e58-8cbda1cb2252	realm roles	openid-connect	oidc-usermodel-realm-role-mapper	\N	2bac4725-31a5-4315-bd97-562b7c764e2c
\.


--
-- Data for Name: protocol_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.protocol_mapper_config (protocol_mapper_id, value, name) FROM stdin;
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	true	userinfo.token.claim
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	locale	user.attribute
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	true	id.token.claim
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	true	access.token.claim
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	locale	claim.name
8c087212-3fa8-4eb1-9a8c-b7089ac4e686	String	jsonType.label
5c69905a-5481-4c87-9748-cadd39962376	false	single
5c69905a-5481-4c87-9748-cadd39962376	Basic	attribute.nameformat
5c69905a-5481-4c87-9748-cadd39962376	Role	attribute.name
4258d487-9901-4599-868f-aaadc072643b	true	userinfo.token.claim
4258d487-9901-4599-868f-aaadc072643b	true	id.token.claim
4258d487-9901-4599-868f-aaadc072643b	true	access.token.claim
b4f83334-b4e4-4b93-87e4-14b329c5ce79	true	userinfo.token.claim
b4f83334-b4e4-4b93-87e4-14b329c5ce79	lastName	user.attribute
b4f83334-b4e4-4b93-87e4-14b329c5ce79	true	id.token.claim
b4f83334-b4e4-4b93-87e4-14b329c5ce79	true	access.token.claim
b4f83334-b4e4-4b93-87e4-14b329c5ce79	family_name	claim.name
b4f83334-b4e4-4b93-87e4-14b329c5ce79	String	jsonType.label
120186d9-7fd2-4062-9b69-d56b4ecdc216	true	userinfo.token.claim
120186d9-7fd2-4062-9b69-d56b4ecdc216	firstName	user.attribute
120186d9-7fd2-4062-9b69-d56b4ecdc216	true	id.token.claim
120186d9-7fd2-4062-9b69-d56b4ecdc216	true	access.token.claim
120186d9-7fd2-4062-9b69-d56b4ecdc216	given_name	claim.name
120186d9-7fd2-4062-9b69-d56b4ecdc216	String	jsonType.label
a91de4e1-4bc3-4926-ad73-9d344b289f8e	true	userinfo.token.claim
a91de4e1-4bc3-4926-ad73-9d344b289f8e	middleName	user.attribute
a91de4e1-4bc3-4926-ad73-9d344b289f8e	true	id.token.claim
a91de4e1-4bc3-4926-ad73-9d344b289f8e	true	access.token.claim
a91de4e1-4bc3-4926-ad73-9d344b289f8e	middle_name	claim.name
a91de4e1-4bc3-4926-ad73-9d344b289f8e	String	jsonType.label
63a90961-1b19-4665-bc20-a22edb75f593	true	userinfo.token.claim
63a90961-1b19-4665-bc20-a22edb75f593	nickname	user.attribute
63a90961-1b19-4665-bc20-a22edb75f593	true	id.token.claim
63a90961-1b19-4665-bc20-a22edb75f593	true	access.token.claim
63a90961-1b19-4665-bc20-a22edb75f593	nickname	claim.name
63a90961-1b19-4665-bc20-a22edb75f593	String	jsonType.label
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	true	userinfo.token.claim
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	username	user.attribute
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	true	id.token.claim
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	true	access.token.claim
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	preferred_username	claim.name
4a59b1bd-f1ee-4ac1-b4d7-2ca1e6aefabd	String	jsonType.label
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	true	userinfo.token.claim
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	profile	user.attribute
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	true	id.token.claim
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	true	access.token.claim
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	profile	claim.name
aac41e82-5a37-4e4f-a4ee-491cfae1eff0	String	jsonType.label
04096e46-d403-461a-8e3a-19e9aee73cef	true	userinfo.token.claim
04096e46-d403-461a-8e3a-19e9aee73cef	picture	user.attribute
04096e46-d403-461a-8e3a-19e9aee73cef	true	id.token.claim
04096e46-d403-461a-8e3a-19e9aee73cef	true	access.token.claim
04096e46-d403-461a-8e3a-19e9aee73cef	picture	claim.name
04096e46-d403-461a-8e3a-19e9aee73cef	String	jsonType.label
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	true	userinfo.token.claim
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	website	user.attribute
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	true	id.token.claim
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	true	access.token.claim
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	website	claim.name
ef4a3cfc-780d-461d-b472-06b1ead6b7b0	String	jsonType.label
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	true	userinfo.token.claim
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	gender	user.attribute
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	true	id.token.claim
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	true	access.token.claim
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	gender	claim.name
fc4a2120-3e7b-4e65-8aca-2a84216bd7d9	String	jsonType.label
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	true	userinfo.token.claim
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	birthdate	user.attribute
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	true	id.token.claim
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	true	access.token.claim
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	birthdate	claim.name
7c2190eb-52ed-44c9-964a-29a9c7cfb7d9	String	jsonType.label
b9e3bc19-7f61-480f-ab83-e267aef75cbd	true	userinfo.token.claim
b9e3bc19-7f61-480f-ab83-e267aef75cbd	zoneinfo	user.attribute
b9e3bc19-7f61-480f-ab83-e267aef75cbd	true	id.token.claim
b9e3bc19-7f61-480f-ab83-e267aef75cbd	true	access.token.claim
b9e3bc19-7f61-480f-ab83-e267aef75cbd	zoneinfo	claim.name
b9e3bc19-7f61-480f-ab83-e267aef75cbd	String	jsonType.label
fecc870b-d164-4f29-9b36-cd5ff6b50efb	true	userinfo.token.claim
fecc870b-d164-4f29-9b36-cd5ff6b50efb	locale	user.attribute
fecc870b-d164-4f29-9b36-cd5ff6b50efb	true	id.token.claim
fecc870b-d164-4f29-9b36-cd5ff6b50efb	true	access.token.claim
fecc870b-d164-4f29-9b36-cd5ff6b50efb	locale	claim.name
fecc870b-d164-4f29-9b36-cd5ff6b50efb	String	jsonType.label
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	true	userinfo.token.claim
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	updatedAt	user.attribute
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	true	id.token.claim
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	true	access.token.claim
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	updated_at	claim.name
19e7be85-7bb8-4e8c-97e1-6d100a6511d0	String	jsonType.label
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	true	userinfo.token.claim
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	email	user.attribute
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	true	id.token.claim
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	true	access.token.claim
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	email	claim.name
6c5bb907-a44d-48e8-ab07-b2287aa4ac92	String	jsonType.label
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	true	userinfo.token.claim
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	emailVerified	user.attribute
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	true	id.token.claim
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	true	access.token.claim
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	email_verified	claim.name
b0e275d6-9ae8-472f-91fe-f1dc4a1def8c	boolean	jsonType.label
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	formatted	user.attribute.formatted
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	country	user.attribute.country
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	postal_code	user.attribute.postal_code
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	true	userinfo.token.claim
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	street	user.attribute.street
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	true	id.token.claim
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	region	user.attribute.region
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	true	access.token.claim
97d95c7f-42c4-4f2e-8e30-3cc9d7b3adfc	locality	user.attribute.locality
5aeb6c57-0d21-4096-b881-aa9a7b975779	true	userinfo.token.claim
5aeb6c57-0d21-4096-b881-aa9a7b975779	phoneNumber	user.attribute
5aeb6c57-0d21-4096-b881-aa9a7b975779	true	id.token.claim
5aeb6c57-0d21-4096-b881-aa9a7b975779	true	access.token.claim
5aeb6c57-0d21-4096-b881-aa9a7b975779	phone_number	claim.name
5aeb6c57-0d21-4096-b881-aa9a7b975779	String	jsonType.label
7949f9a1-db86-44ae-960d-c0805f120b1a	true	userinfo.token.claim
7949f9a1-db86-44ae-960d-c0805f120b1a	phoneNumberVerified	user.attribute
7949f9a1-db86-44ae-960d-c0805f120b1a	true	id.token.claim
7949f9a1-db86-44ae-960d-c0805f120b1a	true	access.token.claim
7949f9a1-db86-44ae-960d-c0805f120b1a	phone_number_verified	claim.name
7949f9a1-db86-44ae-960d-c0805f120b1a	boolean	jsonType.label
5314fcb5-4850-4c92-9399-85202275f9bd	true	multivalued
5314fcb5-4850-4c92-9399-85202275f9bd	foo	user.attribute
5314fcb5-4850-4c92-9399-85202275f9bd	true	access.token.claim
5314fcb5-4850-4c92-9399-85202275f9bd	realm_access.roles	claim.name
5314fcb5-4850-4c92-9399-85202275f9bd	String	jsonType.label
ec99bc05-2673-4fac-a7af-3f120cf52a33	true	multivalued
ec99bc05-2673-4fac-a7af-3f120cf52a33	foo	user.attribute
ec99bc05-2673-4fac-a7af-3f120cf52a33	true	access.token.claim
ec99bc05-2673-4fac-a7af-3f120cf52a33	resource_access.${client_id}.roles	claim.name
ec99bc05-2673-4fac-a7af-3f120cf52a33	String	jsonType.label
2c4a36d9-cd7e-4a3e-abdb-7e446431b91c	false	single
2c4a36d9-cd7e-4a3e-abdb-7e446431b91c	Basic	attribute.nameformat
2c4a36d9-cd7e-4a3e-abdb-7e446431b91c	Role	attribute.name
3cb886f9-8341-4b27-926f-008bfb578256	true	userinfo.token.claim
3cb886f9-8341-4b27-926f-008bfb578256	gender	user.attribute
3cb886f9-8341-4b27-926f-008bfb578256	true	id.token.claim
3cb886f9-8341-4b27-926f-008bfb578256	true	access.token.claim
3cb886f9-8341-4b27-926f-008bfb578256	gender	claim.name
3cb886f9-8341-4b27-926f-008bfb578256	String	jsonType.label
459aa158-4c6f-4492-8248-a51821c6bb74	true	userinfo.token.claim
459aa158-4c6f-4492-8248-a51821c6bb74	picture	user.attribute
459aa158-4c6f-4492-8248-a51821c6bb74	true	id.token.claim
459aa158-4c6f-4492-8248-a51821c6bb74	true	access.token.claim
459aa158-4c6f-4492-8248-a51821c6bb74	picture	claim.name
459aa158-4c6f-4492-8248-a51821c6bb74	String	jsonType.label
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	true	userinfo.token.claim
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	zoneinfo	user.attribute
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	true	id.token.claim
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	true	access.token.claim
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	zoneinfo	claim.name
13d5313a-3b28-4bc7-ad1f-8b65b862f43e	String	jsonType.label
e144add0-ed03-4150-bbaa-24cdcf9f5c35	true	userinfo.token.claim
e144add0-ed03-4150-bbaa-24cdcf9f5c35	middleName	user.attribute
e144add0-ed03-4150-bbaa-24cdcf9f5c35	true	id.token.claim
e144add0-ed03-4150-bbaa-24cdcf9f5c35	true	access.token.claim
e144add0-ed03-4150-bbaa-24cdcf9f5c35	middle_name	claim.name
e144add0-ed03-4150-bbaa-24cdcf9f5c35	String	jsonType.label
7e888c80-38c5-44fd-b36e-65300ee63bb9	true	userinfo.token.claim
7e888c80-38c5-44fd-b36e-65300ee63bb9	website	user.attribute
7e888c80-38c5-44fd-b36e-65300ee63bb9	true	id.token.claim
7e888c80-38c5-44fd-b36e-65300ee63bb9	true	access.token.claim
7e888c80-38c5-44fd-b36e-65300ee63bb9	website	claim.name
7e888c80-38c5-44fd-b36e-65300ee63bb9	String	jsonType.label
694b487c-90f5-4984-a65e-630da67f7e2a	true	userinfo.token.claim
694b487c-90f5-4984-a65e-630da67f7e2a	profile	user.attribute
694b487c-90f5-4984-a65e-630da67f7e2a	true	id.token.claim
694b487c-90f5-4984-a65e-630da67f7e2a	true	access.token.claim
694b487c-90f5-4984-a65e-630da67f7e2a	profile	claim.name
694b487c-90f5-4984-a65e-630da67f7e2a	String	jsonType.label
6a9a3009-ecec-4683-8e2d-df5f362eb21d	true	userinfo.token.claim
6a9a3009-ecec-4683-8e2d-df5f362eb21d	birthdate	user.attribute
6a9a3009-ecec-4683-8e2d-df5f362eb21d	true	id.token.claim
6a9a3009-ecec-4683-8e2d-df5f362eb21d	true	access.token.claim
6a9a3009-ecec-4683-8e2d-df5f362eb21d	birthdate	claim.name
6a9a3009-ecec-4683-8e2d-df5f362eb21d	String	jsonType.label
40471c08-9c11-4cc5-ad4f-2cb13248955e	true	userinfo.token.claim
40471c08-9c11-4cc5-ad4f-2cb13248955e	firstName	user.attribute
40471c08-9c11-4cc5-ad4f-2cb13248955e	true	id.token.claim
40471c08-9c11-4cc5-ad4f-2cb13248955e	true	access.token.claim
40471c08-9c11-4cc5-ad4f-2cb13248955e	given_name	claim.name
40471c08-9c11-4cc5-ad4f-2cb13248955e	String	jsonType.label
6937c087-ed49-45ae-9108-daa77d5fab72	true	userinfo.token.claim
6937c087-ed49-45ae-9108-daa77d5fab72	lastName	user.attribute
6937c087-ed49-45ae-9108-daa77d5fab72	true	id.token.claim
6937c087-ed49-45ae-9108-daa77d5fab72	true	access.token.claim
6937c087-ed49-45ae-9108-daa77d5fab72	family_name	claim.name
6937c087-ed49-45ae-9108-daa77d5fab72	String	jsonType.label
740b9ebe-083a-4a1e-a678-a3327bb48283	true	id.token.claim
740b9ebe-083a-4a1e-a678-a3327bb48283	true	access.token.claim
740b9ebe-083a-4a1e-a678-a3327bb48283	true	userinfo.token.claim
6f88071e-0a10-432d-850a-45d8ce659430	true	userinfo.token.claim
6f88071e-0a10-432d-850a-45d8ce659430	updatedAt	user.attribute
6f88071e-0a10-432d-850a-45d8ce659430	true	id.token.claim
6f88071e-0a10-432d-850a-45d8ce659430	true	access.token.claim
6f88071e-0a10-432d-850a-45d8ce659430	updated_at	claim.name
6f88071e-0a10-432d-850a-45d8ce659430	String	jsonType.label
0c247acd-c76c-408f-bd3b-2ed7153a5f93	true	userinfo.token.claim
0c247acd-c76c-408f-bd3b-2ed7153a5f93	locale	user.attribute
0c247acd-c76c-408f-bd3b-2ed7153a5f93	true	id.token.claim
0c247acd-c76c-408f-bd3b-2ed7153a5f93	true	access.token.claim
0c247acd-c76c-408f-bd3b-2ed7153a5f93	locale	claim.name
0c247acd-c76c-408f-bd3b-2ed7153a5f93	String	jsonType.label
c2359b33-e367-4b43-85d0-e952fbc38993	true	userinfo.token.claim
c2359b33-e367-4b43-85d0-e952fbc38993	username	user.attribute
c2359b33-e367-4b43-85d0-e952fbc38993	true	id.token.claim
c2359b33-e367-4b43-85d0-e952fbc38993	true	access.token.claim
c2359b33-e367-4b43-85d0-e952fbc38993	preferred_username	claim.name
c2359b33-e367-4b43-85d0-e952fbc38993	String	jsonType.label
d8e82173-e652-49f2-8f2f-df8d2babe8c3	true	userinfo.token.claim
d8e82173-e652-49f2-8f2f-df8d2babe8c3	nickname	user.attribute
d8e82173-e652-49f2-8f2f-df8d2babe8c3	true	id.token.claim
d8e82173-e652-49f2-8f2f-df8d2babe8c3	true	access.token.claim
d8e82173-e652-49f2-8f2f-df8d2babe8c3	nickname	claim.name
d8e82173-e652-49f2-8f2f-df8d2babe8c3	String	jsonType.label
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	true	userinfo.token.claim
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	email	user.attribute
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	true	id.token.claim
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	true	access.token.claim
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	email	claim.name
9da3a8cf-d5fd-43ce-b781-9e17030bbea2	String	jsonType.label
da193473-9cf8-49d9-9a07-b7823f6e43ad	true	userinfo.token.claim
da193473-9cf8-49d9-9a07-b7823f6e43ad	emailVerified	user.attribute
da193473-9cf8-49d9-9a07-b7823f6e43ad	true	id.token.claim
da193473-9cf8-49d9-9a07-b7823f6e43ad	true	access.token.claim
da193473-9cf8-49d9-9a07-b7823f6e43ad	email_verified	claim.name
da193473-9cf8-49d9-9a07-b7823f6e43ad	boolean	jsonType.label
394e7b35-e5c2-4fa9-8624-b90e5e115383	formatted	user.attribute.formatted
394e7b35-e5c2-4fa9-8624-b90e5e115383	country	user.attribute.country
394e7b35-e5c2-4fa9-8624-b90e5e115383	postal_code	user.attribute.postal_code
394e7b35-e5c2-4fa9-8624-b90e5e115383	true	userinfo.token.claim
394e7b35-e5c2-4fa9-8624-b90e5e115383	street	user.attribute.street
394e7b35-e5c2-4fa9-8624-b90e5e115383	true	id.token.claim
394e7b35-e5c2-4fa9-8624-b90e5e115383	region	user.attribute.region
394e7b35-e5c2-4fa9-8624-b90e5e115383	true	access.token.claim
394e7b35-e5c2-4fa9-8624-b90e5e115383	locality	user.attribute.locality
5da2d08a-f744-4f6c-9301-2a16262cd772	true	userinfo.token.claim
5da2d08a-f744-4f6c-9301-2a16262cd772	phoneNumber	user.attribute
5da2d08a-f744-4f6c-9301-2a16262cd772	true	id.token.claim
5da2d08a-f744-4f6c-9301-2a16262cd772	true	access.token.claim
5da2d08a-f744-4f6c-9301-2a16262cd772	phone_number	claim.name
5da2d08a-f744-4f6c-9301-2a16262cd772	String	jsonType.label
76329181-3bd2-4f58-b0f9-c34853063e11	true	userinfo.token.claim
76329181-3bd2-4f58-b0f9-c34853063e11	phoneNumberVerified	user.attribute
76329181-3bd2-4f58-b0f9-c34853063e11	true	id.token.claim
76329181-3bd2-4f58-b0f9-c34853063e11	true	access.token.claim
76329181-3bd2-4f58-b0f9-c34853063e11	phone_number_verified	claim.name
76329181-3bd2-4f58-b0f9-c34853063e11	boolean	jsonType.label
f0f42425-d6a1-4816-bf96-3d150e2dd87a	foo	user.attribute
f0f42425-d6a1-4816-bf96-3d150e2dd87a	String	jsonType.label
f0f42425-d6a1-4816-bf96-3d150e2dd87a	true	multivalued
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	foo	user.attribute
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	String	jsonType.label
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	true	multivalued
e33e5c73-4014-48e8-b4d8-ffe74a804374	true	userinfo.token.claim
e33e5c73-4014-48e8-b4d8-ffe74a804374	locale	user.attribute
e33e5c73-4014-48e8-b4d8-ffe74a804374	true	id.token.claim
e33e5c73-4014-48e8-b4d8-ffe74a804374	true	access.token.claim
e33e5c73-4014-48e8-b4d8-ffe74a804374	locale	claim.name
f0f42425-d6a1-4816-bf96-3d150e2dd87a	false	access.token.claim
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	false	access.token.claim
e33e5c73-4014-48e8-b4d8-ffe74a804374	String	jsonType.label
b94426f2-dcdc-4bf9-ab5d-21df027d9796	clientHost	user.session.note
b94426f2-dcdc-4bf9-ab5d-21df027d9796	true	userinfo.token.claim
b94426f2-dcdc-4bf9-ab5d-21df027d9796	true	id.token.claim
b94426f2-dcdc-4bf9-ab5d-21df027d9796	true	access.token.claim
b94426f2-dcdc-4bf9-ab5d-21df027d9796	clientHost	claim.name
b94426f2-dcdc-4bf9-ab5d-21df027d9796	String	jsonType.label
be0239db-94bc-498c-ba3f-7a15e27cf0ba	francoralite	included.client.audience
be0239db-94bc-498c-ba3f-7a15e27cf0ba	false	id.token.claim
be0239db-94bc-498c-ba3f-7a15e27cf0ba	true	access.token.claim
be0239db-94bc-498c-ba3f-7a15e27cf0ba	false	userinfo.token.claim
4710b262-17fe-46b7-bb27-180c9980bd8d	clientAddress	user.session.note
4710b262-17fe-46b7-bb27-180c9980bd8d	true	userinfo.token.claim
4710b262-17fe-46b7-bb27-180c9980bd8d	true	id.token.claim
4710b262-17fe-46b7-bb27-180c9980bd8d	true	access.token.claim
4710b262-17fe-46b7-bb27-180c9980bd8d	clientAddress	claim.name
4710b262-17fe-46b7-bb27-180c9980bd8d	String	jsonType.label
5780c55a-91a3-42f8-b81a-6776f20e17ec	clientId	user.session.note
5780c55a-91a3-42f8-b81a-6776f20e17ec	true	userinfo.token.claim
5780c55a-91a3-42f8-b81a-6776f20e17ec	true	id.token.claim
5780c55a-91a3-42f8-b81a-6776f20e17ec	true	access.token.claim
5780c55a-91a3-42f8-b81a-6776f20e17ec	clientId	claim.name
5780c55a-91a3-42f8-b81a-6776f20e17ec	String	jsonType.label
f496f401-ffee-4634-8279-e8d9a1647521	true	userinfo.token.claim
f496f401-ffee-4634-8279-e8d9a1647521	username	user.attribute
f496f401-ffee-4634-8279-e8d9a1647521	true	id.token.claim
f496f401-ffee-4634-8279-e8d9a1647521	true	access.token.claim
f496f401-ffee-4634-8279-e8d9a1647521	upn	claim.name
f496f401-ffee-4634-8279-e8d9a1647521	String	jsonType.label
99c28bd4-8549-457f-aa92-834fddbb9823	true	multivalued
99c28bd4-8549-457f-aa92-834fddbb9823	foo	user.attribute
99c28bd4-8549-457f-aa92-834fddbb9823	true	id.token.claim
99c28bd4-8549-457f-aa92-834fddbb9823	true	access.token.claim
99c28bd4-8549-457f-aa92-834fddbb9823	groups	claim.name
99c28bd4-8549-457f-aa92-834fddbb9823	String	jsonType.label
cea28dbd-6a83-49fc-82ac-68ac77ea4672	true	userinfo.token.claim
cea28dbd-6a83-49fc-82ac-68ac77ea4672	username	user.attribute
cea28dbd-6a83-49fc-82ac-68ac77ea4672	true	id.token.claim
cea28dbd-6a83-49fc-82ac-68ac77ea4672	true	access.token.claim
cea28dbd-6a83-49fc-82ac-68ac77ea4672	upn	claim.name
cea28dbd-6a83-49fc-82ac-68ac77ea4672	String	jsonType.label
74748dc2-f3fc-4824-afba-a4fafd6a2054	true	multivalued
74748dc2-f3fc-4824-afba-a4fafd6a2054	foo	user.attribute
74748dc2-f3fc-4824-afba-a4fafd6a2054	true	id.token.claim
74748dc2-f3fc-4824-afba-a4fafd6a2054	true	access.token.claim
74748dc2-f3fc-4824-afba-a4fafd6a2054	groups	claim.name
74748dc2-f3fc-4824-afba-a4fafd6a2054	String	jsonType.label
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	foo	user.attribute
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	true	access.token.claim
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	resource_access.${client_id}.roles	claim.name
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	String	jsonType.label
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	true	multivalued
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	true	multivalued
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	foo	user.attribute
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	true	id.token.claim
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	true	access.token.claim
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	groups	claim.name
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	String	jsonType.label
713c89aa-bf75-4645-9e58-8cbda1cb2252	foo	user.attribute
713c89aa-bf75-4645-9e58-8cbda1cb2252	true	access.token.claim
713c89aa-bf75-4645-9e58-8cbda1cb2252	realm_access.roles	claim.name
713c89aa-bf75-4645-9e58-8cbda1cb2252	String	jsonType.label
713c89aa-bf75-4645-9e58-8cbda1cb2252	true	multivalued
713c89aa-bf75-4645-9e58-8cbda1cb2252	true	userinfo.token.claim
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	true	userinfo.token.claim
94fa1d5e-d8db-423d-aa82-b1b8e5b34ecb	true	userinfo.token.claim
713c89aa-bf75-4645-9e58-8cbda1cb2252	true	id.token.claim
80043e9d-0bf4-4ce0-9df2-9bd59be2b5ff	true	id.token.claim
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	false	id.token.claim
f0f42425-d6a1-4816-bf96-3d150e2dd87a	realm_access.roles	claim.name
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	false	userinfo.token.claim
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	resource_access.${client_id}.roles	claim.name
f0f42425-d6a1-4816-bf96-3d150e2dd87a	false	userinfo.token.claim
fee1bb68-a719-4e13-a8ed-f123c04fd9a5	admin-cli	usermodel.clientRoleMapping.clientId
\.


--
-- Data for Name: realm; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm (id, access_code_lifespan, user_action_lifespan, access_token_lifespan, account_theme, admin_theme, email_theme, enabled, events_enabled, events_expiration, login_theme, name, not_before, password_policy, registration_allowed, remember_me, reset_password_allowed, social, ssl_required, sso_idle_timeout, sso_max_lifespan, update_profile_on_soc_login, verify_email, master_admin_client, login_lifespan, internationalization_enabled, default_locale, reg_email_as_username, admin_events_enabled, admin_events_details_enabled, edit_username_allowed, otp_policy_counter, otp_policy_window, otp_policy_period, otp_policy_digits, otp_policy_alg, otp_policy_type, browser_flow, registration_flow, direct_grant_flow, reset_credentials_flow, client_auth_flow, offline_session_idle_timeout, revoke_refresh_token, access_token_life_implicit, login_with_email_allowed, duplicate_emails_allowed, docker_auth_flow, refresh_token_max_reuse, allow_user_managed_access, sso_max_lifespan_remember_me, sso_idle_timeout_remember_me, default_role) FROM stdin;
master	60	300	60	\N	\N	\N	t	f	0	\N	master	1567415903	\N	f	f	f	f	EXTERNAL	1800	36000	f	f	9b3d814d-33ff-45fd-9f13-a489b550ae9e	1800	f	\N	f	f	f	f	0	1	30	6	HmacSHA1	totp	c7352f60-b9e1-47a6-a59b-80fec7a47336	89b8d90b-255a-41b0-80d8-134a3f122410	a3a5cfd1-1916-425e-9506-43346acc24d7	952496b8-a35d-4607-9bb8-773b06d5ddf1	92ecb810-75b3-4d42-b661-8b3c30dbed58	2592000	f	900	t	f	c6bda705-d01b-4202-804c-e1ee5508f2b7	0	f	0	0	7079ef4e-6e2e-4bda-91d8-cf52142687be
francoralite	60	300	300	keycloak	keycloak	keycloak	t	f	0	keycloak	francoralite	1634836149	\N	f	f	f	f	NONE	1800	36000	f	f	ac6a2e53-830b-44ee-8fc0-775bb105330d	1800	t	fr	f	f	f	f	0	1	30	6	HmacSHA1	totp	c0214dcb-09b7-49b6-87a8-cb8e8ab1f12d	fb9a5a93-0804-4b67-9805-37e9630c3adc	88edf78f-b77c-4538-a2da-50fb89041319	3440df01-ffe2-4734-bd0a-0718162bbb80	88d730bb-34e8-4e93-bf18-ac5a8673d7d9	2592000	f	900	t	f	025ef783-6113-46c0-b997-534b69a01a87	0	f	0	0	cf336c4f-f1fc-447b-a686-2f44ac81a67f
\.


--
-- Data for Name: realm_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_attribute (name, realm_id, value) FROM stdin;
_browser_header.contentSecurityPolicyReportOnly	master	
_browser_header.xContentTypeOptions	master	nosniff
_browser_header.xRobotsTag	master	none
_browser_header.xFrameOptions	master	SAMEORIGIN
_browser_header.contentSecurityPolicy	master	frame-src 'self'; frame-ancestors 'self'; object-src 'none';
_browser_header.xXSSProtection	master	1; mode=block
_browser_header.strictTransportSecurity	master	max-age=31536000; includeSubDomains
bruteForceProtected	master	false
permanentLockout	master	false
maxFailureWaitSeconds	master	900
minimumQuickLoginWaitSeconds	master	60
waitIncrementSeconds	master	60
quickLoginCheckMilliSeconds	master	1000
maxDeltaTimeSeconds	master	43200
failureFactor	master	30
displayName	master	Keycloak
displayNameHtml	master	<div class="kc-logo-text"><span>Keycloak</span></div>
offlineSessionMaxLifespanEnabled	master	false
offlineSessionMaxLifespan	master	5184000
_browser_header.contentSecurityPolicyReportOnly	francoralite	
_browser_header.xContentTypeOptions	francoralite	nosniff
_browser_header.xRobotsTag	francoralite	none
_browser_header.xFrameOptions	francoralite	SAMEORIGIN
_browser_header.contentSecurityPolicy	francoralite	frame-src 'self'; frame-ancestors 'self'; object-src 'none';
_browser_header.xXSSProtection	francoralite	1; mode=block
_browser_header.strictTransportSecurity	francoralite	max-age=31536000; includeSubDomains
bruteForceProtected	francoralite	false
permanentLockout	francoralite	false
maxFailureWaitSeconds	francoralite	900
minimumQuickLoginWaitSeconds	francoralite	60
waitIncrementSeconds	francoralite	60
quickLoginCheckMilliSeconds	francoralite	1000
maxDeltaTimeSeconds	francoralite	43200
failureFactor	francoralite	30
defaultSignatureAlgorithm	francoralite	RS256
offlineSessionMaxLifespanEnabled	francoralite	false
offlineSessionMaxLifespan	francoralite	5184000
actionTokenGeneratedByAdminLifespan	francoralite	43200
actionTokenGeneratedByUserLifespan	francoralite	300
client-policies.profiles	francoralite	{"profiles":[]}
client-policies.policies	francoralite	{"policies":[]}
client-policies.profiles	master	{"profiles":[]}
client-policies.policies	master	{"policies":[]}
\.


--
-- Data for Name: realm_default_groups; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_default_groups (realm_id, group_id) FROM stdin;
\.


--
-- Data for Name: realm_enabled_event_types; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_enabled_event_types (realm_id, value) FROM stdin;
\.


--
-- Data for Name: realm_events_listeners; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_events_listeners (realm_id, value) FROM stdin;
master	jboss-logging
francoralite	jboss-logging
\.


--
-- Data for Name: realm_localizations; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_localizations (realm_id, locale, texts) FROM stdin;
\.


--
-- Data for Name: realm_required_credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_required_credential (type, form_label, input, secret, realm_id) FROM stdin;
password	password	t	t	master
password	password	t	t	francoralite
\.


--
-- Data for Name: realm_smtp_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_smtp_config (realm_id, value, name) FROM stdin;
\.


--
-- Data for Name: realm_supported_locales; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_supported_locales (realm_id, value) FROM stdin;
francoralite	en
francoralite	fr
\.


--
-- Data for Name: redirect_uris; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.redirect_uris (client_id, value) FROM stdin;
6ca8b749-cba1-4453-8a20-0c189d9b9447	http://nginx.francoralite.localhost:8080/**/*
6ca8b749-cba1-4453-8a20-0c189d9b9447	http://nginx.francoralite.localhost:8080/*
6ca8b749-cba1-4453-8a20-0c189d9b9447	*
5def7547-cfd3-4473-946c-35f796c52df4	/admin/francoralite/console/*
f896f42d-66e6-498f-bdc0-a90216659041	/realms/francoralite/account/*
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	/admin/master/console/*
310aabaf-651c-4959-b441-8fe27129a418	/realms/master/account/*
dda53ff1-c096-4601-8a8c-30365fde853d	/realms/francoralite/account/*
c041d458-ff12-4534-bcb0-cef6017935ab	/realms/master/account/*
\.


--
-- Data for Name: required_action_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.required_action_config (required_action_id, value, name) FROM stdin;
\.


--
-- Data for Name: required_action_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.required_action_provider (id, alias, name, realm_id, enabled, default_action, provider_id, priority) FROM stdin;
139dc071-565e-4bbc-837c-7954a581e55a	VERIFY_EMAIL	Verify Email	master	t	f	VERIFY_EMAIL	50
f4e513ad-9ca1-49a2-89a7-3f0770c3521a	UPDATE_PROFILE	Update Profile	master	t	f	UPDATE_PROFILE	40
c3482f64-ee24-4101-bcde-29ef05a4ad67	CONFIGURE_TOTP	Configure OTP	master	t	f	CONFIGURE_TOTP	10
8bb8ad76-cead-4bdd-b726-95d3aa6051ec	UPDATE_PASSWORD	Update Password	master	t	f	UPDATE_PASSWORD	30
aca47fdd-88a5-4f8d-a12a-f24b14db1531	terms_and_conditions	Terms and Conditions	master	f	f	terms_and_conditions	20
11b431d2-ae1d-4073-a469-f79f4bbc36a2	CONFIGURE_TOTP	Configure OTP	francoralite	t	f	CONFIGURE_TOTP	10
1a40f5f9-f9cf-4178-804a-6a99883e35b0	terms_and_conditions	Terms and Conditions	francoralite	f	f	terms_and_conditions	20
f1bc241e-925b-4a6f-8fe2-48a82dcad5ed	UPDATE_PASSWORD	Update Password	francoralite	t	f	UPDATE_PASSWORD	30
67a1823c-efa4-47a0-8c94-2a8d8e08b0b0	UPDATE_PROFILE	Update Profile	francoralite	t	f	UPDATE_PROFILE	40
a6cfb561-8a78-40c1-8043-fbe5e7280a95	VERIFY_EMAIL	Verify Email	francoralite	t	f	VERIFY_EMAIL	50
a157ba64-b7e5-4bd1-8222-b4dd75481061	update_user_locale	Update User Locale	francoralite	t	f	update_user_locale	1000
e45252d9-8f11-496b-90e6-830803344dcc	update_user_locale	Update User Locale	master	t	f	update_user_locale	1000
69dc85b4-5357-4bdf-83dc-7442252e0063	delete_account	Delete Account	francoralite	f	f	delete_account	60
aa2f9501-2b51-4249-ad2d-b37f5028438b	delete_account	Delete Account	master	f	f	delete_account	60
\.


--
-- Data for Name: resource_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_attribute (id, name, value, resource_id) FROM stdin;
\.


--
-- Data for Name: resource_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_policy (resource_id, policy_id) FROM stdin;
\.


--
-- Data for Name: resource_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_scope (resource_id, scope_id) FROM stdin;
2b5688da-3404-42a1-a79a-20d999bce9f1	d7600272-a9ed-4730-9653-81258ff9996a
2b5688da-3404-42a1-a79a-20d999bce9f1	58874d83-90b2-4a46-b4fd-6d16cfc92b38
2b5688da-3404-42a1-a79a-20d999bce9f1	11eec72e-8f59-4c5e-9095-817a6fad0b0b
2b5688da-3404-42a1-a79a-20d999bce9f1	de59e869-4a8c-425e-b65b-986675c547ac
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	cab2520d-32c3-4cb4-af28-edf94fe64920
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	83a46c2b-d09b-49ae-9ddb-f961032af8fb
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	6e6aa730-bf29-4071-8e6b-096933f3e261
57c23047-92d9-4637-8661-a2b93987d2d2	a3c9efc0-e66e-473d-be69-7f3cc120041e
57c23047-92d9-4637-8661-a2b93987d2d2	d0cf588c-060c-413b-83f2-99309eec50bb
57c23047-92d9-4637-8661-a2b93987d2d2	0bbc72e4-44a0-442a-aa74-b6a46ba27d1d
57c23047-92d9-4637-8661-a2b93987d2d2	b375a7ce-dfdb-43f0-8180-eaafd900c40c
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	b0b56afc-1579-48c2-9ffc-720440b1f601
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	f5256aab-117a-4ad3-b276-ddd27fc079bc
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	275ab079-aeb6-487b-ad02-d4cef821fdd6
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	f7a56634-10ca-4560-b372-31a11c6761f2
e71d05b8-41d0-4252-ac4d-acafceb69caf	0fcdd438-ca5f-4e47-a8ba-dc5a479535e7
e71d05b8-41d0-4252-ac4d-acafceb69caf	9a32db3b-e5c0-400b-8f7e-33dec4920219
e71d05b8-41d0-4252-ac4d-acafceb69caf	7fdf56e4-5687-465b-8c93-d520e40dba62
e71d05b8-41d0-4252-ac4d-acafceb69caf	ba953395-648d-4e90-89de-e1258b1e1d99
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	5cb685af-e5d9-429d-8f8f-c4a92b0b14ec
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	f2dd1707-c0f8-476c-b81e-ffaeeaec356a
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	6605c8ae-02af-40fb-ac1e-4653f7cb5ff7
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	702a1381-914b-462a-b19b-275bd4db7ff2
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	8db4eedb-0ade-4248-a1dd-e5f235d9ecaf
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	7d412b4f-83ba-4277-b188-cec153c32b2e
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	a2f206e1-5b4a-4c75-814b-5a2616306003
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	f98a8ddf-630d-4e5b-98db-fbe29d36a03a
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	b9881ee0-8a9b-4039-afec-e6bca3665e76
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	e7ace2bf-9dcc-4f39-97bf-289f3a7638e1
b1ce7e69-438d-44db-93b1-f13e094b0954	e4583cb5-5770-43a9-95e9-b39981b947cf
b1ce7e69-438d-44db-93b1-f13e094b0954	0e83a641-3da7-4012-8ce4-e6aa3dbabd7d
b1ce7e69-438d-44db-93b1-f13e094b0954	2e2a4648-f599-4f70-ac3a-7453b3b1055d
b1ce7e69-438d-44db-93b1-f13e094b0954	4350b070-3eea-4cb8-b3d0-7d3c753e33f3
689a7fbe-2911-40a3-891d-8306776e1a26	8607b79d-53fb-4562-b53c-7f0ea844c722
689a7fbe-2911-40a3-891d-8306776e1a26	0007acec-c38e-43c3-9d1c-84b22cf45223
689a7fbe-2911-40a3-891d-8306776e1a26	1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8
689a7fbe-2911-40a3-891d-8306776e1a26	1c76efdb-7597-4ab3-a6f0-7a94b64760e1
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	ebeaafd2-41a5-4289-926c-3dd61928d266
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	447dea2a-a078-47cf-ac2f-e03f8f6ef585
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	009e9aa5-e6bc-4a03-9052-be5866fede7b
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	5615a6cc-12af-4479-909d-6afd5d82d711
413e2a3b-83a4-4ed9-933b-61527de9652a	4d003da0-e5b9-46a8-9630-723d7d0ff2a1
413e2a3b-83a4-4ed9-933b-61527de9652a	b1d83932-0ea9-42dc-8578-8e6063f54ff3
413e2a3b-83a4-4ed9-933b-61527de9652a	49f9677e-47f9-46ee-91c3-45d0734f0e9a
413e2a3b-83a4-4ed9-933b-61527de9652a	22ae069e-4893-42bc-b4c3-9d4fb2a85792
528bb01e-7cb6-450a-baa2-96e96409711d	ed24b8d5-65b7-4e91-9438-6c663d160a8a
528bb01e-7cb6-450a-baa2-96e96409711d	64de3d9d-e116-438b-ae58-8de3e9e42384
528bb01e-7cb6-450a-baa2-96e96409711d	a2f08de8-cbf6-4711-b932-6d4adcf5200d
528bb01e-7cb6-450a-baa2-96e96409711d	09d23fad-d2da-4319-9408-5d9948971a18
de0b61a7-77dc-418b-a867-351973d9991d	86442a1f-c323-44b7-b773-2c1d42db7217
de0b61a7-77dc-418b-a867-351973d9991d	cb900cb7-6a98-45c8-9566-9da26559aedc
de0b61a7-77dc-418b-a867-351973d9991d	1ba00269-7f7b-4082-a530-32ac9ef79d61
de0b61a7-77dc-418b-a867-351973d9991d	f470bb89-8dc9-4279-8b81-f3c96da8933a
17fa4234-2a2e-4861-85e3-b99a4689861d	48348210-c240-4dd0-b377-bd6929f7bbaf
17fa4234-2a2e-4861-85e3-b99a4689861d	c399da7d-1c72-4e7c-959c-1dce9684916c
17fa4234-2a2e-4861-85e3-b99a4689861d	3e1a3a50-a7c4-45f9-ac13-cc82c9f7d405
17fa4234-2a2e-4861-85e3-b99a4689861d	4917596f-f29d-47e0-9cc5-56f326951b75
c3d1041b-b905-4b78-a66d-aae9acf96e24	8ee93852-790f-4183-9da1-8eab09b3c29a
c3d1041b-b905-4b78-a66d-aae9acf96e24	206d134c-a21c-47d6-9634-dea5832cc911
c3d1041b-b905-4b78-a66d-aae9acf96e24	51454aa6-be41-4445-972f-d40bb4a6ec61
c3d1041b-b905-4b78-a66d-aae9acf96e24	34851926-ba58-427f-aed2-408074f74bcc
19914ed5-dc9b-491c-8b4e-b2c332444333	f00c449c-be6f-4c2a-bf0a-0fc27caa6d06
19914ed5-dc9b-491c-8b4e-b2c332444333	d808320f-39c1-4193-88ab-cdb7a82af8b8
19914ed5-dc9b-491c-8b4e-b2c332444333	b868a581-fba5-4895-959d-80aaedc49f55
19914ed5-dc9b-491c-8b4e-b2c332444333	16835618-616f-47d6-a0f2-8592424270ba
2ef0daae-792f-46a4-befd-2e17721a039c	96ee2d9a-17ae-4bef-9196-c3b460b2a2f7
2ef0daae-792f-46a4-befd-2e17721a039c	3de82401-b5f7-4fd3-8938-b3812c3a6218
2ef0daae-792f-46a4-befd-2e17721a039c	830b2887-c9f7-4f20-bfa4-c95261ef3d30
2ef0daae-792f-46a4-befd-2e17721a039c	12c8dc7b-ca42-40fb-9cb3-38bb96b64674
41d801e6-b759-4b8b-bb10-5b30e37bed1f	5f76e419-73a6-4b89-ab4a-4abb8632e33c
41d801e6-b759-4b8b-bb10-5b30e37bed1f	24942230-212b-4b13-9931-4b5db634a7ab
41d801e6-b759-4b8b-bb10-5b30e37bed1f	7df2f5b2-eb93-4907-8f52-8c183ebfdf4e
41d801e6-b759-4b8b-bb10-5b30e37bed1f	538bdb7a-742b-44db-8b32-a5d9fbb434b9
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	dd927140-987b-45f9-8df3-2cc5b6510e9d
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	26504250-43fd-4151-a3ab-698514b4422f
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	8bbc7b0b-4d57-4f61-9e24-bcabd986bc2a
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	ea09f144-bf42-47b7-89db-c39393c7453e
af9d7eb3-1f47-4de6-b768-5602f2d3e824	253ed92b-51e7-4dc8-ab10-f9dd6d334209
af9d7eb3-1f47-4de6-b768-5602f2d3e824	4b9b80ad-1491-49d0-b624-e5e26aedf7e3
af9d7eb3-1f47-4de6-b768-5602f2d3e824	533a090b-5705-43fc-86bf-a24537cddb53
af9d7eb3-1f47-4de6-b768-5602f2d3e824	5331e26f-246f-46fa-b2a7-48df197d6fa9
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	4b34957c-86c5-4f7d-b169-fe0f36a8ab16
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	e39ed88a-fe46-4a3a-bca6-5840e52d2856
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	785e830b-5455-4ed8-a420-3165752f5b7c
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	636cd6e3-0937-4b87-9bf6-0f6946c11f57
b6f19f57-2c63-48a2-b88b-2cfaf4a2a9ad	dbc4c807-4f3a-44de-88be-3216cd078b29
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	86e01732-079f-4793-9f5b-72f69da8590b
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	39713fcb-1774-430b-972c-c712969b4aaa
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	f10febe0-07fa-43d1-8f03-4662c55f9e2c
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	14dd04c3-fda2-42ac-b7da-e46bc97f9f0e
37610f96-5d5f-497a-8bd1-4b75de93a0d1	982ed45e-4e07-44a4-b8f5-cc3d2c56f433
37610f96-5d5f-497a-8bd1-4b75de93a0d1	cb9f10e6-8121-4e91-a30f-f20c436a1f83
37610f96-5d5f-497a-8bd1-4b75de93a0d1	ff01ca02-94de-448b-98f7-019723a203fa
37610f96-5d5f-497a-8bd1-4b75de93a0d1	e907d88c-7e7e-4b4e-9b33-6865f4a6b11a
e5309082-73ae-432a-acf7-f6196fcc5dc9	d11e8639-90ac-49fc-9304-62a91b0c264d
e5309082-73ae-432a-acf7-f6196fcc5dc9	d3050429-e99e-46d1-9ebd-400e222d5134
e5309082-73ae-432a-acf7-f6196fcc5dc9	9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb
e5309082-73ae-432a-acf7-f6196fcc5dc9	b9894b0a-a062-4da7-b18b-8c827620c309
5e0a5f49-f6f2-45d3-a726-3895d2f32688	fbd5a8cb-09f4-4bfd-98c0-bf579c016b45
5e0a5f49-f6f2-45d3-a726-3895d2f32688	7eb6f8fb-17b1-4382-9566-35e4eec985cd
5e0a5f49-f6f2-45d3-a726-3895d2f32688	ccc731f5-6628-4278-8faa-ff90ffb7abaa
5e0a5f49-f6f2-45d3-a726-3895d2f32688	bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2
953f1689-4f6b-45f8-b9ad-9f759e7306ac	b82a2ace-49e8-43d3-b163-29df0c81b296
953f1689-4f6b-45f8-b9ad-9f759e7306ac	0f995a1e-25dd-4359-8a0d-ffba517654db
953f1689-4f6b-45f8-b9ad-9f759e7306ac	57b22cca-04fc-447f-ad5d-0d1eff401b5f
953f1689-4f6b-45f8-b9ad-9f759e7306ac	a17bc8e8-f215-4e18-b96a-61070db32d7b
73ef8143-0561-4cdb-a93f-7bf3205d4514	2ce28b99-a3d9-41a1-834b-ad09c808b12d
73ef8143-0561-4cdb-a93f-7bf3205d4514	d5176ee5-ace3-4939-9c92-f6e28f4a1154
73ef8143-0561-4cdb-a93f-7bf3205d4514	9a380bfb-edab-405b-add9-4e7cec35ef73
73ef8143-0561-4cdb-a93f-7bf3205d4514	d7575538-d923-4a71-95ab-a73d5ba019e5
0203e9e9-1e1d-4cf8-a46a-9e5585783407	6d470647-2a50-45c7-ab5f-d41f4ff2e8fb
0203e9e9-1e1d-4cf8-a46a-9e5585783407	639bd728-3a24-4225-928b-f8930732c70c
0203e9e9-1e1d-4cf8-a46a-9e5585783407	aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b
0203e9e9-1e1d-4cf8-a46a-9e5585783407	8529432f-7acc-4f75-bc7e-aa7af2f068aa
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	5f721066-1413-4483-8fdc-b3227aa5ae71
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	835503d8-7873-4139-bbf5-9bd46a4d7555
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	dde473d8-ca2c-44e1-8009-4a8eace8e57a
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	e081184b-1f03-4109-b27e-edfaa15180ee
01bb6e65-536f-442c-98ef-c792ace46119	9cd88c81-9bad-41e2-9cf5-b7faba2e1d76
01bb6e65-536f-442c-98ef-c792ace46119	9826691b-794a-4aec-ad2f-aca0d1066873
01bb6e65-536f-442c-98ef-c792ace46119	6cdbe9b1-2bd3-4069-8379-01a4d3ff1fe0
01bb6e65-536f-442c-98ef-c792ace46119	5c3b1f91-c37f-45f5-9a12-ee6dfdfd2879
86548857-44b5-44aa-910a-93d53c1ec6f8	2383aca2-bafb-40df-a4ed-a73c11cd33a5
86548857-44b5-44aa-910a-93d53c1ec6f8	37ccc457-85b1-4192-bad0-83bba00950b2
86548857-44b5-44aa-910a-93d53c1ec6f8	24b5087c-57d1-4dec-af85-b4418ab71ea3
86548857-44b5-44aa-910a-93d53c1ec6f8	65a29a73-9ff3-4423-9583-38df67506e97
abef55b5-b725-47a3-b756-32409de1cf3d	8bd6fead-d21a-4947-9e77-384dc9b2db45
abef55b5-b725-47a3-b756-32409de1cf3d	d88f0387-7041-4251-b2a4-3505c71e0145
abef55b5-b725-47a3-b756-32409de1cf3d	d751a181-a69c-4168-83c1-67a08cf77315
abef55b5-b725-47a3-b756-32409de1cf3d	7959cb7a-91c9-4a22-96e5-6f171555260d
2d324cb3-99e4-4552-ac91-a022d4ea136f	2a2c79fb-38bc-4909-adfb-fd1799fa02a3
2d324cb3-99e4-4552-ac91-a022d4ea136f	acfc0756-2a83-4b46-a4e4-0adbe441cd38
2d324cb3-99e4-4552-ac91-a022d4ea136f	fe4ff88e-5d57-421c-b406-714655fdbd1d
2d324cb3-99e4-4552-ac91-a022d4ea136f	52415e78-95a5-43d1-b455-b7598b42aeb9
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	d0432919-9773-4b20-bb8f-e65cf4d6f373
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	b3ac4a14-cd60-4705-bec3-648cfbc5635d
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	4d913333-8c13-4056-8593-32259ee3b787
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	0faad761-4f4d-4e53-936c-eff0f8f19d56
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	7042f286-956a-4dbc-b696-2c77581d86bb
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	b20de290-866f-45f1-a33c-122a5bf1b524
5afac379-6d2a-4727-8079-6efe6fe6c654	c098d34e-a341-4d3b-b4dd-eb3551b96ebd
5afac379-6d2a-4727-8079-6efe6fe6c654	6819ef1e-0478-4a68-b0b9-0bab0723819f
5afac379-6d2a-4727-8079-6efe6fe6c654	96d9118e-2b2f-4bc1-8813-47bf99ef578a
5afac379-6d2a-4727-8079-6efe6fe6c654	8fc8908f-b782-41c8-98fc-b46746f7bfba
e10b3d96-2915-446f-95f3-b76ad3364607	18fd272b-c4b7-4d22-b870-c81768c0bffc
e10b3d96-2915-446f-95f3-b76ad3364607	e0790f61-dc64-4ad7-92f5-07374ea3043d
e10b3d96-2915-446f-95f3-b76ad3364607	28580873-d8aa-49ad-808b-a4ded351b415
e10b3d96-2915-446f-95f3-b76ad3364607	0dab5ff3-04a2-43a7-9312-c296c4d45675
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	b78c5bd2-c526-430b-8ed4-4fedf2858cc5
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	a238a18e-512b-4aa5-bd8a-b26213de6739
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	7117f962-24c7-463d-8255-cf2ccb881dc8
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	9b94cb3a-52f5-4167-9db0-805bf8003cf1
80398263-0cf1-4375-a86c-66b3f980ae86	6a93f815-2bec-47d2-a159-ac376174559c
80398263-0cf1-4375-a86c-66b3f980ae86	2b7ffa8c-5e12-4627-9465-93d2ccb7d187
80398263-0cf1-4375-a86c-66b3f980ae86	c3afe823-fc30-478a-bfb7-ab60739aeca6
80398263-0cf1-4375-a86c-66b3f980ae86	1f1ba0dc-9c41-4e33-a891-8ed99eab961d
c9283a47-6276-4b33-9052-b5b8436d9e6d	25deb52f-6114-42f0-b594-d94e47f528a1
c9283a47-6276-4b33-9052-b5b8436d9e6d	67420711-e263-4276-899d-0cb6d8b4c704
c9283a47-6276-4b33-9052-b5b8436d9e6d	00d10d34-9060-4976-8941-454bd64e9712
c9283a47-6276-4b33-9052-b5b8436d9e6d	a811007a-334b-4692-81fe-01509f3e307d
0085478d-0489-4d0d-a318-09ff6f87a0f7	d0188960-83a2-44d9-87e6-ff241857c393
0085478d-0489-4d0d-a318-09ff6f87a0f7	7bd41e59-50b9-4287-a3eb-7d295155ed98
0085478d-0489-4d0d-a318-09ff6f87a0f7	782efc3c-27fd-4bbc-a4db-61f330521895
0085478d-0489-4d0d-a318-09ff6f87a0f7	a1231bfc-991a-427d-b578-9e361f16d571
26c1fa48-17ab-436b-8414-c5f13c23c533	7a199e98-ee84-4309-8d72-35ff7130ac47
26c1fa48-17ab-436b-8414-c5f13c23c533	e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c
26c1fa48-17ab-436b-8414-c5f13c23c533	63fd494e-7fe3-4488-8c10-347ec413fdfd
26c1fa48-17ab-436b-8414-c5f13c23c533	c9ba43e9-8652-4d34-89db-1a22a14adb07
78eacca0-37bd-47d8-ae9e-83ef914cba17	84f00d8e-2576-497f-8401-5dd68506f502
78eacca0-37bd-47d8-ae9e-83ef914cba17	5efbba82-03b2-40f9-a909-2423099cfd65
78eacca0-37bd-47d8-ae9e-83ef914cba17	9a35e10d-42af-48b3-9a10-cad37f018dab
78eacca0-37bd-47d8-ae9e-83ef914cba17	44fd3a81-1dcb-4070-9dee-57437b90ff80
36836a0c-f41e-48f7-9476-4d57234d2009	932746ea-68f2-4111-94c0-65be660c5d29
36836a0c-f41e-48f7-9476-4d57234d2009	210eb72b-b6db-4f86-9969-12e56da66cbe
36836a0c-f41e-48f7-9476-4d57234d2009	0283fc09-7bb4-4233-ae2b-d08f0f1c4f0f
36836a0c-f41e-48f7-9476-4d57234d2009	f4d71eaa-36e9-4f68-b4e3-d70d0d2f7e34
fc174355-1f0c-4e8d-841a-65b56b3e0203	b4aff203-ccf3-476b-af94-b6970ff46130
fc174355-1f0c-4e8d-841a-65b56b3e0203	54ed816e-0a55-4540-bfbf-ec16ec884957
fc174355-1f0c-4e8d-841a-65b56b3e0203	393bf858-8373-4b9c-9fcb-79adef17b823
fc174355-1f0c-4e8d-841a-65b56b3e0203	f0358778-456e-49eb-9c46-5694a41f0186
7e419804-0744-4e23-b36c-f0bf4b282ff7	c8d09ce1-456f-4dc8-b092-b717f0b4b5ab
7e419804-0744-4e23-b36c-f0bf4b282ff7	70b86c9f-030e-42c6-8fc4-647ad2b1dfeb
7e419804-0744-4e23-b36c-f0bf4b282ff7	701819ca-dc87-4932-9ef4-eb74900b3962
7e419804-0744-4e23-b36c-f0bf4b282ff7	f35462c3-94e6-480f-9aad-de440723e210
00aa3676-7909-46d5-bfaf-4fe38cef9640	8abc0aa6-5b30-4d94-9f0a-bdf8600c9285
00aa3676-7909-46d5-bfaf-4fe38cef9640	8f04d44e-bbcb-4743-926d-f795b8e65de8
00aa3676-7909-46d5-bfaf-4fe38cef9640	62fc499f-422d-48e2-9200-cd15cc409203
00aa3676-7909-46d5-bfaf-4fe38cef9640	0ec9af08-b459-4e79-b49d-b3bd93b5183d
97fb61e3-9758-47a0-b66a-220b0be7388a	9a4a7903-42c9-4af9-9aff-4ea86d0e8cfb
97fb61e3-9758-47a0-b66a-220b0be7388a	1c4a3eaa-6ad6-4ffe-91ac-b127201e0493
97fb61e3-9758-47a0-b66a-220b0be7388a	eda9ddd3-5d8e-431f-9a6d-b5eadb14405e
97fb61e3-9758-47a0-b66a-220b0be7388a	43bebee7-3f29-41f9-b422-780ca73aaaf3
a3bb484f-436a-480f-ba62-0b1b9f77b951	97877fcd-5162-4cb8-a810-ffb9e273b3db
a3bb484f-436a-480f-ba62-0b1b9f77b951	5cfa28ac-41cf-4072-840b-f1437ae4087e
a3bb484f-436a-480f-ba62-0b1b9f77b951	18b5f174-70fb-41c9-98c2-e92829150139
a3bb484f-436a-480f-ba62-0b1b9f77b951	fae35cea-412d-4e9a-811a-9496a6fbd663
9345fe77-177d-4df7-bf3f-a309e7531b92	595dd377-597e-4066-af12-b3a9835e630a
9345fe77-177d-4df7-bf3f-a309e7531b92	267a82d3-0338-4a28-8267-e2e52f05af39
9345fe77-177d-4df7-bf3f-a309e7531b92	1714a76b-e10e-48b3-a097-1486442f5eac
9345fe77-177d-4df7-bf3f-a309e7531b92	2420c15a-9f92-4e5b-97af-90acc3eecabe
c29ddc81-b1d4-4e22-9289-d9a287419ef2	b2622786-8c32-4971-bb0a-0a56b72df3ec
c29ddc81-b1d4-4e22-9289-d9a287419ef2	77becf3c-686e-4378-a750-0cc9365facc3
c29ddc81-b1d4-4e22-9289-d9a287419ef2	8c383dbf-7ba0-42d2-a048-430a04c866e7
c29ddc81-b1d4-4e22-9289-d9a287419ef2	93eda126-7711-4029-be8f-82e04d9f41f7
792bf5b2-8ad7-4a60-b460-c19d34ed3678	38544a76-1ee7-4569-9033-c8e08778c292
792bf5b2-8ad7-4a60-b460-c19d34ed3678	125735e5-09c4-4739-b7e7-adcb8413869d
792bf5b2-8ad7-4a60-b460-c19d34ed3678	3db4d7d2-251c-4024-b8be-827cab44e3d9
792bf5b2-8ad7-4a60-b460-c19d34ed3678	f561ea0b-4ce7-4118-8a77-f019f6339c53
\.


--
-- Data for Name: resource_server; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server (id, allow_rs_remote_mgmt, policy_enforce_mode, decision_strategy) FROM stdin;
6ca8b749-cba1-4453-8a20-0c189d9b9447	t	0	1
\.


--
-- Data for Name: resource_server_perm_ticket; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_perm_ticket (id, owner, requester, created_timestamp, granted_timestamp, resource_id, scope_id, resource_server_id, policy_id) FROM stdin;
\.


--
-- Data for Name: resource_server_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_policy (id, name, description, type, decision_strategy, logic, resource_server_id, owner) FROM stdin;
6cafc604-ca21-48ca-bf77-c1fed388c57a	Default Policy	A policy that grants access only for users within this realm	js	0	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
3fc46920-3046-4423-9851-db767fbee3c7	francoralite-users-pol	\N	role	0	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b8b552c0-a8ec-44f7-8c6a-70df10e7a149	francoralite-contributors-pol	\N	role	0	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
47d172b5-7863-4175-9a62-a77cc63cf3da	francoralite-administrators-pol	\N	role	0	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
96d81e07-e3f9-4206-88f3-76328cbbb9b8	francoralite-users-perm	\N	scope	1	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f0aef9d4-46df-472b-8192-fd828046233e	Default Permission	A permission that applies to the default resource type	resource	1	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a29acdd2-e748-4989-88ef-53d5280d664f	francoralite-contributors-perm	\N	scope	1	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
35525fd7-3ec7-41c0-9ad4-af6fa1c7243c	francoralite-administrators-perm	\N	scope	1	0	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
\.


--
-- Data for Name: resource_server_resource; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_resource (id, name, type, icon_uri, owner, resource_server_id, owner_managed_access, display_name) FROM stdin;
85c18a5c-1ecc-4cb3-9313-ad3849a3ada4	Default Resource	urn:francoralite:resources:default	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	\N
2b5688da-3404-42a1-a79a-20d999bce9f1	acquisition_mode	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Acquisition_mode
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	authority	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Authority
57c23047-92d9-4637-8661-a2b93987d2d2	collectioncollectors	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collectioncollectors
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	collection_informer	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collection_informer
e71d05b8-41d0-4252-ac4d-acafceb69caf	collection_language	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collection_language
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	collection_location	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collection_location
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	collection_publisher	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collection_publisher
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	collection	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Collection
b1ce7e69-438d-44db-93b1-f13e094b0954	coupe	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Coupe
689a7fbe-2911-40a3-891d-8306776e1a26	dance	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Dance
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	domain_music	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Domain_music
413e2a3b-83a4-4ed9-933b-61527de9652a	domain_song	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Domain_song
528bb01e-7cb6-450a-baa2-96e96409711d	domain_tale	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Domain_tale
de0b61a7-77dc-418b-a867-351973d9991d	domain_vocal	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Domain_vocal
17fa4234-2a2e-4861-85e3-b99a4689861d	emit_vox	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Emit_vox
c3d1041b-b905-4b78-a66d-aae9acf96e24	enumeration	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Enumeration
19914ed5-dc9b-491c-8b4e-b2c332444333	ext_media_item	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Ext_media_item
2ef0daae-792f-46a4-befd-2e17721a039c	fond	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Fond
41d801e6-b759-4b8b-bb10-5b30e37bed1f	hornbostelsachs	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Hornbostelsachs
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	institution	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Institution
af9d7eb3-1f47-4de6-b768-5602f2d3e824	instrument	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Instrument
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	item_analysis	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_analysis
b6f19f57-2c63-48a2-b88b-2cfaf4a2a9ad	globalsearch	\N		6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Globalsearch
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	item_collector	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_collector
37610f96-5d5f-497a-8bd1-4b75de93a0d1	item_dance	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_dance
e5309082-73ae-432a-acf7-f6196fcc5dc9	item_domain_music	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_domain_music
5e0a5f49-f6f2-45d3-a726-3895d2f32688	item_domain_song	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_domain_song
953f1689-4f6b-45f8-b9ad-9f759e7306ac	item_domain_tale	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_domain_tale
73ef8143-0561-4cdb-a93f-7bf3205d4514	item_domain_vocal	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_domain_vocal
0203e9e9-1e1d-4cf8-a46a-9e5585783407	item_informer	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_informer
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	item_marker	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_marker
01bb6e65-536f-442c-98ef-c792ace46119	item_musical_group	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_musical_group
86548857-44b5-44aa-910a-93d53c1ec6f8	item_musical_organization	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_musical_organization
abef55b5-b725-47a3-b756-32409de1cf3d	item	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item
2d324cb3-99e4-4552-ac91-a022d4ea136f	item_thematic	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_thematic
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	item_transcoding_flag	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_transcoding_flag
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	item_usefulness	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Item_usefulness
5afac379-6d2a-4727-8079-6efe6fe6c654	language	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Language
e10b3d96-2915-446f-95f3-b76ad3364607	legal_rights	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Legal_rights
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	location_gis	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Location_gis
80398263-0cf1-4375-a86c-66b3f980ae86	location	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Location
c9283a47-6276-4b33-9052-b5b8436d9e6d	media_item	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Media_item
0085478d-0489-4d0d-a318-09ff6f87a0f7	mediatype	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Mediatype
26c1fa48-17ab-436b-8414-c5f13c23c533	mission	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Mission
78eacca0-37bd-47d8-ae9e-83ef914cba17	musical_group	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Musical_group
36836a0c-f41e-48f7-9476-4d57234d2009	musical_organization	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Musical_organization
fc174355-1f0c-4e8d-841a-65b56b3e0203	performance_collection_musician	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Performance_collection_musician
7e419804-0744-4e23-b36c-f0bf4b282ff7	performance_collection	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Performance_collection
00aa3676-7909-46d5-bfaf-4fe38cef9640	publisher	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Publisher
97fb61e3-9758-47a0-b66a-220b0be7388a	recording_context	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Recording_context
a3bb484f-436a-480f-ba62-0b1b9f77b951	thematic	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Thematic
9345fe77-177d-4df7-bf3f-a309e7531b92	timeside_item	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Timeside_item
c29ddc81-b1d4-4e22-9289-d9a287419ef2	usefulness	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	Usefulness
792bf5b2-8ad7-4a60-b460-c19d34ed3678	user	\N	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	6ca8b749-cba1-4453-8a20-0c189d9b9447	f	User
\.


--
-- Data for Name: resource_server_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_scope (id, name, icon_uri, resource_server_id, display_name) FROM stdin;
dbc4c807-4f3a-44de-88be-3216cd078b29	globalsearch	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
11eec72e-8f59-4c5e-9095-817a6fad0b0b	acquisition_mode:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d7600272-a9ed-4730-9653-81258ff9996a	acquisition_mode:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
de59e869-4a8c-425e-b65b-986675c547ac	acquisition_mode:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
58874d83-90b2-4a46-b4fd-6d16cfc92b38	acquisition_mode:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179	authority:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6e6aa730-bf29-4071-8e6b-096933f3e261	authority:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
cab2520d-32c3-4cb4-af28-edf94fe64920	authority:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
83a46c2b-d09b-49ae-9ddb-f961032af8fb	authority:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a3c9efc0-e66e-473d-be69-7f3cc120041e	collectioncollectors:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b375a7ce-dfdb-43f0-8180-eaafd900c40c	collectioncollectors:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0bbc72e4-44a0-442a-aa74-b6a46ba27d1d	collectioncollectors:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d0cf588c-060c-413b-83f2-99309eec50bb	collectioncollectors:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
275ab079-aeb6-487b-ad02-d4cef821fdd6	collection_informer:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f7a56634-10ca-4560-b372-31a11c6761f2	collection_informer:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f5256aab-117a-4ad3-b276-ddd27fc079bc	collection_informer:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b0b56afc-1579-48c2-9ffc-720440b1f601	collection_informer:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0fcdd438-ca5f-4e47-a8ba-dc5a479535e7	collection_language:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ba953395-648d-4e90-89de-e1258b1e1d99	collection_language:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7fdf56e4-5687-465b-8c93-d520e40dba62	collection_language:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9a32db3b-e5c0-400b-8f7e-33dec4920219	collection_language:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f2dd1707-c0f8-476c-b81e-ffaeeaec356a	collection_location:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	collection_location:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5cb685af-e5d9-429d-8f8f-c4a92b0b14ec	collection_location:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
702a1381-914b-462a-b19b-275bd4db7ff2	collection_location:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7d412b4f-83ba-4277-b188-cec153c32b2e	collection_publisher:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	collection_publisher:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a2f206e1-5b4a-4c75-814b-5a2616306003	collection_publisher:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8db4eedb-0ade-4248-a1dd-e5f235d9ecaf	collection_publisher:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f98a8ddf-630d-4e5b-98db-fbe29d36a03a	collection:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b9881ee0-8a9b-4039-afec-e6bca3665e76	collection:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63	collection:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e7ace2bf-9dcc-4f39-97bf-289f3a7638e1	collection:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2e2a4648-f599-4f70-ac3a-7453b3b1055d	coupe:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	coupe:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4350b070-3eea-4cb8-b3d0-7d3c753e33f3	coupe:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e4583cb5-5770-43a9-95e9-b39981b947cf	coupe:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0007acec-c38e-43c3-9d1c-84b22cf45223	dance:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	dance:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1c76efdb-7597-4ab3-a6f0-7a94b64760e1	dance:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8607b79d-53fb-4562-b53c-7f0ea844c722	dance:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
009e9aa5-e6bc-4a03-9052-be5866fede7b	domain_music:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
447dea2a-a078-47cf-ac2f-e03f8f6ef585	domain_music:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5615a6cc-12af-4479-909d-6afd5d82d711	domain_music:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ebeaafd2-41a5-4289-926c-3dd61928d266	domain_music:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
22ae069e-4893-42bc-b4c3-9d4fb2a85792	domain_song:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
49f9677e-47f9-46ee-91c3-45d0734f0e9a	domain_song:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4d003da0-e5b9-46a8-9630-723d7d0ff2a1	domain_song:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b1d83932-0ea9-42dc-8578-8e6063f54ff3	domain_song:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ed24b8d5-65b7-4e91-9438-6c663d160a8a	domain_tale:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a2f08de8-cbf6-4711-b932-6d4adcf5200d	domain_tale:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
64de3d9d-e116-438b-ae58-8de3e9e42384	domain_tale:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
09d23fad-d2da-4319-9408-5d9948971a18	domain_tale:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
86442a1f-c323-44b7-b773-2c1d42db7217	domain_vocal:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1ba00269-7f7b-4082-a530-32ac9ef79d61	domain_vocal:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f470bb89-8dc9-4279-8b81-f3c96da8933a	domain_vocal:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
cb900cb7-6a98-45c8-9566-9da26559aedc	domain_vocal:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4917596f-f29d-47e0-9cc5-56f326951b75	emit_vox:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
48348210-c240-4dd0-b377-bd6929f7bbaf	emit_vox:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
c399da7d-1c72-4e7c-959c-1dce9684916c	emit_vox:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
3e1a3a50-a7c4-45f9-ac13-cc82c9f7d405	emit_vox:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8ee93852-790f-4183-9da1-8eab09b3c29a	enumeration:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
51454aa6-be41-4445-972f-d40bb4a6ec61	enumeration:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
206d134c-a21c-47d6-9634-dea5832cc911	enumeration:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
34851926-ba58-427f-aed2-408074f74bcc	enumeration:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b868a581-fba5-4895-959d-80aaedc49f55	ext_media_item:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
16835618-616f-47d6-a0f2-8592424270ba	ext_media_item:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f00c449c-be6f-4c2a-bf0a-0fc27caa6d06	ext_media_item:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d808320f-39c1-4193-88ab-cdb7a82af8b8	ext_media_item:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
12c8dc7b-ca42-40fb-9cb3-38bb96b64674	fond:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
830b2887-c9f7-4f20-bfa4-c95261ef3d30	fond:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
96ee2d9a-17ae-4bef-9196-c3b460b2a2f7	fond:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
3de82401-b5f7-4fd3-8938-b3812c3a6218	fond:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7df2f5b2-eb93-4907-8f52-8c183ebfdf4e	hornbostelsachs:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5f76e419-73a6-4b89-ab4a-4abb8632e33c	hornbostelsachs:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
24942230-212b-4b13-9931-4b5db634a7ab	hornbostelsachs:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
538bdb7a-742b-44db-8b32-a5d9fbb434b9	hornbostelsachs:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8bbc7b0b-4d57-4f61-9e24-bcabd986bc2a	institution:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ea09f144-bf42-47b7-89db-c39393c7453e	institution:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
26504250-43fd-4151-a3ab-698514b4422f	institution:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
dd927140-987b-45f9-8df3-2cc5b6510e9d	institution:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4b9b80ad-1491-49d0-b624-e5e26aedf7e3	instrument:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
533a090b-5705-43fc-86bf-a24537cddb53	instrument:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
253ed92b-51e7-4dc8-ab10-f9dd6d334209	instrument:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5331e26f-246f-46fa-b2a7-48df197d6fa9	instrument:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4b34957c-86c5-4f7d-b169-fe0f36a8ab16	item_analysis:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
636cd6e3-0937-4b87-9bf6-0f6946c11f57	item_analysis:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e39ed88a-fe46-4a3a-bca6-5840e52d2856	item_analysis:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
785e830b-5455-4ed8-a420-3165752f5b7c	item_analysis:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
39713fcb-1774-430b-972c-c712969b4aaa	item_collector:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
86e01732-079f-4793-9f5b-72f69da8590b	item_collector:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f10febe0-07fa-43d1-8f03-4662c55f9e2c	item_collector:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
14dd04c3-fda2-42ac-b7da-e46bc97f9f0e	item_collector:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
982ed45e-4e07-44a4-b8f5-cc3d2c56f433	item_dance:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
cb9f10e6-8121-4e91-a30f-f20c436a1f83	item_dance:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ff01ca02-94de-448b-98f7-019723a203fa	item_dance:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e907d88c-7e7e-4b4e-9b33-6865f4a6b11a	item_dance:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b9894b0a-a062-4da7-b18b-8c827620c309	item_domain_music:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d11e8639-90ac-49fc-9304-62a91b0c264d	item_domain_music:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d3050429-e99e-46d1-9ebd-400e222d5134	item_domain_music:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb	item_domain_music:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7eb6f8fb-17b1-4382-9566-35e4eec985cd	item_domain_song:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ccc731f5-6628-4278-8faa-ff90ffb7abaa	item_domain_song:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2	item_domain_song:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
fbd5a8cb-09f4-4bfd-98c0-bf579c016b45	item_domain_song:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
57b22cca-04fc-447f-ad5d-0d1eff401b5f	item_domain_tale:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b82a2ace-49e8-43d3-b163-29df0c81b296	item_domain_tale:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0f995a1e-25dd-4359-8a0d-ffba517654db	item_domain_tale:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a17bc8e8-f215-4e18-b96a-61070db32d7b	item_domain_tale:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2ce28b99-a3d9-41a1-834b-ad09c808b12d	item_domain_vocal:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d5176ee5-ace3-4939-9c92-f6e28f4a1154	item_domain_vocal:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9a380bfb-edab-405b-add9-4e7cec35ef73	item_domain_vocal:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d7575538-d923-4a71-95ab-a73d5ba019e5	item_domain_vocal:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b	item_informer:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
639bd728-3a24-4225-928b-f8930732c70c	item_informer:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6d470647-2a50-45c7-ab5f-d41f4ff2e8fb	item_informer:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8529432f-7acc-4f75-bc7e-aa7af2f068aa	item_informer:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
835503d8-7873-4139-bbf5-9bd46a4d7555	item_marker:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
dde473d8-ca2c-44e1-8009-4a8eace8e57a	item_marker:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e081184b-1f03-4109-b27e-edfaa15180ee	item_marker:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5f721066-1413-4483-8fdc-b3227aa5ae71	item_marker:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9cd88c81-9bad-41e2-9cf5-b7faba2e1d76	item_musical_group:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9826691b-794a-4aec-ad2f-aca0d1066873	item_musical_group:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5c3b1f91-c37f-45f5-9a12-ee6dfdfd2879	item_musical_group:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6cdbe9b1-2bd3-4069-8379-01a4d3ff1fe0	item_musical_group:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
37ccc457-85b1-4192-bad0-83bba00950b2	item_musical_organization:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
65a29a73-9ff3-4423-9583-38df67506e97	item_musical_organization:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
24b5087c-57d1-4dec-af85-b4418ab71ea3	item_musical_organization:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2383aca2-bafb-40df-a4ed-a73c11cd33a5	item_musical_organization:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d88f0387-7041-4251-b2a4-3505c71e0145	item:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d751a181-a69c-4168-83c1-67a08cf77315	item:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7959cb7a-91c9-4a22-96e5-6f171555260d	item:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8bd6fead-d21a-4947-9e77-384dc9b2db45	item:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
52415e78-95a5-43d1-b455-b7598b42aeb9	item_thematic:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	item_thematic:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
fe4ff88e-5d57-421c-b406-714655fdbd1d	item_thematic:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
acfc0756-2a83-4b46-a4e4-0adbe441cd38	item_thematic:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0faad761-4f4d-4e53-936c-eff0f8f19d56	item_transcoding_flag:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d0432919-9773-4b20-bb8f-e65cf4d6f373	item_transcoding_flag:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4d913333-8c13-4056-8593-32259ee3b787	item_transcoding_flag:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b3ac4a14-cd60-4705-bec3-648cfbc5635d	item_transcoding_flag:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7042f286-956a-4dbc-b696-2c77581d86bb	item_usefulness:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b20de290-866f-45f1-a33c-122a5bf1b524	item_usefulness:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6	item_usefulness:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4	item_usefulness:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
c098d34e-a341-4d3b-b4dd-eb3551b96ebd	language:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8fc8908f-b782-41c8-98fc-b46746f7bfba	language:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
96d9118e-2b2f-4bc1-8813-47bf99ef578a	language:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6819ef1e-0478-4a68-b0b9-0bab0723819f	language:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
28580873-d8aa-49ad-808b-a4ded351b415	legal_rights:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
18fd272b-c4b7-4d22-b870-c81768c0bffc	legal_rights:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e0790f61-dc64-4ad7-92f5-07374ea3043d	legal_rights:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0dab5ff3-04a2-43a7-9312-c296c4d45675	legal_rights:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b78c5bd2-c526-430b-8ed4-4fedf2858cc5	location_gis:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a238a18e-512b-4aa5-bd8a-b26213de6739	location_gis:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9b94cb3a-52f5-4167-9db0-805bf8003cf1	location_gis:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7117f962-24c7-463d-8255-cf2ccb881dc8	location_gis:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6a93f815-2bec-47d2-a159-ac376174559c	location:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	location:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1f1ba0dc-9c41-4e33-a891-8ed99eab961d	location:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
c3afe823-fc30-478a-bfb7-ab60739aeca6	location:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a811007a-334b-4692-81fe-01509f3e307d	media_item:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
67420711-e263-4276-899d-0cb6d8b4c704	media_item:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
00d10d34-9060-4976-8941-454bd64e9712	media_item:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
25deb52f-6114-42f0-b594-d94e47f528a1	media_item:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a1231bfc-991a-427d-b578-9e361f16d571	mediatype:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
782efc3c-27fd-4bbc-a4db-61f330521895	mediatype:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d0188960-83a2-44d9-87e6-ff241857c393	mediatype:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7bd41e59-50b9-4287-a3eb-7d295155ed98	mediatype:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7a199e98-ee84-4309-8d72-35ff7130ac47	mission:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	mission:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
63fd494e-7fe3-4488-8c10-347ec413fdfd	mission:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
c9ba43e9-8652-4d34-89db-1a22a14adb07	mission:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
84f00d8e-2576-497f-8401-5dd68506f502	musical_group:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9a35e10d-42af-48b3-9a10-cad37f018dab	musical_group:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5efbba82-03b2-40f9-a909-2423099cfd65	musical_group:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
44fd3a81-1dcb-4070-9dee-57437b90ff80	musical_group:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f4d71eaa-36e9-4f68-b4e3-d70d0d2f7e34	musical_organization:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
210eb72b-b6db-4f86-9969-12e56da66cbe	musical_organization:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
932746ea-68f2-4111-94c0-65be660c5d29	musical_organization:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0283fc09-7bb4-4233-ae2b-d08f0f1c4f0f	musical_organization:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
54ed816e-0a55-4540-bfbf-ec16ec884957	performance_collection_musician:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f0358778-456e-49eb-9c46-5694a41f0186	performance_collection_musician:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
393bf858-8373-4b9c-9fcb-79adef17b823	performance_collection_musician:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b4aff203-ccf3-476b-af94-b6970ff46130	performance_collection_musician:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
c8d09ce1-456f-4dc8-b092-b717f0b4b5ab	performance_collection:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	performance_collection:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f35462c3-94e6-480f-9aad-de440723e210	performance_collection:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
701819ca-dc87-4932-9ef4-eb74900b3962	performance_collection:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0ec9af08-b459-4e79-b49d-b3bd93b5183d	publisher:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
62fc499f-422d-48e2-9200-cd15cc409203	publisher:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8abc0aa6-5b30-4d94-9f0a-bdf8600c9285	publisher:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8f04d44e-bbcb-4743-926d-f795b8e65de8	publisher:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9a4a7903-42c9-4af9-9aff-4ea86d0e8cfb	recording_context:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
eda9ddd3-5d8e-431f-9a6d-b5eadb14405e	recording_context:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
43bebee7-3f29-41f9-b422-780ca73aaaf3	recording_context:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1c4a3eaa-6ad6-4ffe-91ac-b127201e0493	recording_context:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
18b5f174-70fb-41c9-98c2-e92829150139	thematic:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
97877fcd-5162-4cb8-a810-ffb9e273b3db	thematic:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5cfa28ac-41cf-4072-840b-f1437ae4087e	thematic:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
fae35cea-412d-4e9a-811a-9496a6fbd663	thematic:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
595dd377-597e-4066-af12-b3a9835e630a	timeside_item:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
267a82d3-0338-4a28-8267-e2e52f05af39	timeside_item:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1714a76b-e10e-48b3-a097-1486442f5eac	timeside_item:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
2420c15a-9f92-4e5b-97af-90acc3eecabe	timeside_item:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b2622786-8c32-4971-bb0a-0a56b72df3ec	usefulness:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
93eda126-7711-4029-be8f-82e04d9f41f7	usefulness:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8c383dbf-7ba0-42d2-a048-430a04c866e7	usefulness:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
77becf3c-686e-4378-a750-0cc9365facc3	usefulness:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
125735e5-09c4-4739-b7e7-adcb8413869d	user:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f561ea0b-4ce7-4118-8a77-f019f6339c53	user:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
3db4d7d2-251c-4024-b8be-827cab44e3d9	user:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
38544a76-1ee7-4569-9033-c8e08778c292	user:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8830549f-2a56-449b-972a-99f330ff6799	document_collection:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b716fd24-bc6a-4cd8-a59c-f62ac0e2adb6	document_collection:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ae655968-7c21-4d81-be06-2a0df0ed6b28	document_collection:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
34541214-0d98-4fcd-b432-1d812544dc93	document_collection:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7595af17-584d-4656-84eb-8c486e615576	document_fonds:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
e0b50865-fa93-46b9-a03a-ec30c0f686a2	document_fonds:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6538235a-0c96-4490-99ee-6c02bd461efa	item_author:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
b458b85f-6f29-4158-bad3-d9b89a337da4	item_author:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5d2f2e15-0f4a-456c-9260-e0abd9390c5c	item_author:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
86de09e2-9d5b-4cfe-92fa-34810c975fa2	item_author:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9542b213-74ae-4de2-bf9b-5fcc546cfcb9	item_coirault:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
acab7624-6acc-4a09-ba9f-54781922f9ce	item_coirault:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
bad56af4-15da-4f42-8f15-9b0464e0d333	item_coirault:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
7b489fe6-48b2-4a10-ac59-806d7b32b2f9	item_coirault:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
118ba66e-bb47-4de0-b0cc-34170d92e915	item_compositor:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
a1e98df4-f516-45b7-9515-da380ee8bb42	item_compositor:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5975d1f2-c365-4a2c-ac7f-c55dd7a5f9e1	item_compositor:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
08fd3bb1-bcb0-4458-bdab-bf9904fd9ecf	item_compositor:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
8634c4ab-4c4d-4d93-92eb-06ad76d6e4dd	item_language:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
5203668a-5842-4186-a1eb-753ac32c207b	item_language:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
be6e29d9-8353-46c7-8f6e-6f063101fe11	item_language:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d2bfc926-63eb-498c-b59e-43763d4cef7b	item_language:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
9546ca06-fcc7-4f7d-b9fa-1710433b9760	document:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
851cd81c-4648-4785-8035-f328276b74ca	document:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
4629d58e-7d46-4578-827d-e11a3310e33b	document:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
069a8fbd-3c49-41cf-b722-5a0f6006df54	document:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
612bd607-87b6-4f7e-ad81-eafbb45ad5f5	item_performance:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
f77a49ae-cc2a-44a9-8f4b-01508b95b2e2	item_performance:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
be1746e1-2e16-4bbb-95b5-dedeeee7d0a4	item_performance:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
0ac01b61-8af5-4f77-9d2d-4591321157e3	item_performance:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d91bc883-9d88-4027-a6c9-6c696c15c4aa	document_fonds:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
d08e6560-faac-4198-9c59-af90218cac26	document_fonds:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
85a36c92-cc5c-447b-848a-3ee52b7fc419	document_mission:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
522c6384-9e71-4e1e-b303-2a3e2e67ea10	document_mission:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
072f8500-842b-4bce-be47-eaf278261675	document_mission:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
6cf3311a-c0e7-445c-9728-9138d3e573b4	document_mission:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
1649b8bb-aafc-49cc-97b5-8fccadad8703	document_item:add	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
08cfea6b-acef-4f81-ad01-f9025cbbbd03	document_item:update	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
ea22c6d6-fc3b-4a40-bc89-343d312ee339	document_item:view	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
69cb5066-a268-4dca-a216-37a1767908bc	document_item:delete	\N	6ca8b749-cba1-4453-8a20-0c189d9b9447	\N
\.


--
-- Data for Name: resource_uris; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_uris (resource_id, value) FROM stdin;
85c18a5c-1ecc-4cb3-9313-ad3849a3ada4	/*
2b5688da-3404-42a1-a79a-20d999bce9f1	/api/acquisition_mode/{id}
05a8b63d-7d91-4a31-8973-5c57bd32d0ad	/api/authority/{id}
57c23047-92d9-4637-8661-a2b93987d2d2	/api/collectioncollectors/{id}
cc02a490-d0f7-48b6-95c8-fc3fe30f7206	/api/collection_informer/{id}
e71d05b8-41d0-4252-ac4d-acafceb69caf	/api/collection_language/{id}
8bf0d22a-cbdf-4b4f-8cbc-a78503d69acd	/api/collection_location/{id}
1524c0a5-4523-41d8-bf4f-142b58ea8e7a	/api/collection_publisher/{id}
bf5bd1b4-d4ba-4a13-a5fe-e2528162531b	/api/collection/{id}
b1ce7e69-438d-44db-93b1-f13e094b0954	/api/coupe/{id}
689a7fbe-2911-40a3-891d-8306776e1a26	/api/dance/{id}
2f6377b4-0407-47f4-b4e3-35b2b7473e9c	/api/domain_music/{id}
413e2a3b-83a4-4ed9-933b-61527de9652a	/api/domain_song/{id}
528bb01e-7cb6-450a-baa2-96e96409711d	/api/domain_tale/{id}
de0b61a7-77dc-418b-a867-351973d9991d	/api/domain_vocal/{id}
17fa4234-2a2e-4861-85e3-b99a4689861d	/api/emit_vox/{id}
c3d1041b-b905-4b78-a66d-aae9acf96e24	/api/enumeration/{id}
19914ed5-dc9b-491c-8b4e-b2c332444333	/api/ext_media_item/{id}
2ef0daae-792f-46a4-befd-2e17721a039c	/api/fond/{id}
41d801e6-b759-4b8b-bb10-5b30e37bed1f	/api/hornbostelsachs/{id}
57ed4e6f-528e-4fdd-8171-0d1c04922ec2	/api/institution/{id}
af9d7eb3-1f47-4de6-b768-5602f2d3e824	/api/instrument/{id}
b58f22a0-32f3-4bad-a7fc-48b9a14191b0	/api/item_analysis/{id}
b6f19f57-2c63-48a2-b88b-2cfaf4a2a9ad	/globalsearch
799d0ce7-79cf-4f83-b136-6a4fe16f64d8	/api/item_collector/{id}
37610f96-5d5f-497a-8bd1-4b75de93a0d1	/api/item_dance/{id}
e5309082-73ae-432a-acf7-f6196fcc5dc9	/api/item_domain_music/{id}
5e0a5f49-f6f2-45d3-a726-3895d2f32688	/api/item_domain_song/{id}
953f1689-4f6b-45f8-b9ad-9f759e7306ac	/api/item_domain_tale/{id}
73ef8143-0561-4cdb-a93f-7bf3205d4514	/api/item_domain_vocal/{id}
0203e9e9-1e1d-4cf8-a46a-9e5585783407	/api/item_informer/{id}
2a052629-f7ba-45b7-8fa1-1ac67c6b205b	/api/item_marker/{id}
01bb6e65-536f-442c-98ef-c792ace46119	/api/item_musical_group/{id}
86548857-44b5-44aa-910a-93d53c1ec6f8	/api/item_musical_organization/{id}
abef55b5-b725-47a3-b756-32409de1cf3d	/api/item/{id}
2d324cb3-99e4-4552-ac91-a022d4ea136f	/api/item_thematic/{id}
5ef6db4b-c8ec-4ee5-8a3b-6e6259eeedb6	/api/item_transcoding_flag/{id}
c18e6a43-1a8e-4179-9bea-6d95bfc38b25	/api/item_usefulness/{id}
5afac379-6d2a-4727-8079-6efe6fe6c654	/api/language/{id}
e10b3d96-2915-446f-95f3-b76ad3364607	/api/legal_rights/{id}
c21ecac0-0276-4df5-bfd1-a1a9bdc33b53	/api/location_gis/{id}
80398263-0cf1-4375-a86c-66b3f980ae86	/api/location/{id}
c9283a47-6276-4b33-9052-b5b8436d9e6d	/api/media_item/{id}
0085478d-0489-4d0d-a318-09ff6f87a0f7	/api/mediatype/{id}
26c1fa48-17ab-436b-8414-c5f13c23c533	/api/mission/{id}
78eacca0-37bd-47d8-ae9e-83ef914cba17	/api/musical_group/{id}
36836a0c-f41e-48f7-9476-4d57234d2009	/api/musical_organization/{id}
fc174355-1f0c-4e8d-841a-65b56b3e0203	/api/performance_collection_musician/{id}
7e419804-0744-4e23-b36c-f0bf4b282ff7	/api/performance_collection/{id}
00aa3676-7909-46d5-bfaf-4fe38cef9640	/api/publisher/{id}
97fb61e3-9758-47a0-b66a-220b0be7388a	/api/recording_context/{id}
a3bb484f-436a-480f-ba62-0b1b9f77b951	/api/thematic/{id}
9345fe77-177d-4df7-bf3f-a309e7531b92	/api/timeside_item/{id}
c29ddc81-b1d4-4e22-9289-d9a287419ef2	/api/usefulness/{id}
792bf5b2-8ad7-4a60-b460-c19d34ed3678	/api/user/{id}
\.


--
-- Data for Name: role_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.role_attribute (id, role_id, name, value) FROM stdin;
\.


--
-- Data for Name: scope_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.scope_mapping (client_id, role_id) FROM stdin;
6ca8b749-cba1-4453-8a20-0c189d9b9447	afb187be-f83f-4122-a9d9-d609d1b85251
6ca8b749-cba1-4453-8a20-0c189d9b9447	7f2da254-71c1-452b-b1e7-ab89ef429d94
6ca8b749-cba1-4453-8a20-0c189d9b9447	a3aa0084-b3a2-4bb9-bbc0-ea88991d6017
dda53ff1-c096-4601-8a8c-30365fde853d	5531c621-ad97-4da9-8896-bed73d09c285
c041d458-ff12-4534-bcb0-cef6017935ab	d5447076-ea4f-4493-b0f9-dbea011ad108
\.


--
-- Data for Name: scope_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.scope_policy (scope_id, policy_id) FROM stdin;
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	3fc46920-3046-4423-9851-db767fbee3c7
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	3fc46920-3046-4423-9851-db767fbee3c7
b20de290-866f-45f1-a33c-122a5bf1b524	3fc46920-3046-4423-9851-db767fbee3c7
a2f08de8-cbf6-4711-b932-6d4adcf5200d	3fc46920-3046-4423-9851-db767fbee3c7
67420711-e263-4276-899d-0cb6d8b4c704	3fc46920-3046-4423-9851-db767fbee3c7
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	3fc46920-3046-4423-9851-db767fbee3c7
639bd728-3a24-4225-928b-f8930732c70c	3fc46920-3046-4423-9851-db767fbee3c7
9a35e10d-42af-48b3-9a10-cad37f018dab	3fc46920-3046-4423-9851-db767fbee3c7
533a090b-5705-43fc-86bf-a24537cddb53	3fc46920-3046-4423-9851-db767fbee3c7
b82a2ace-49e8-43d3-b163-29df0c81b296	3fc46920-3046-4423-9851-db767fbee3c7
6e6aa730-bf29-4071-8e6b-096933f3e261	3fc46920-3046-4423-9851-db767fbee3c7
830b2887-c9f7-4f20-bfa4-c95261ef3d30	3fc46920-3046-4423-9851-db767fbee3c7
f0358778-456e-49eb-9c46-5694a41f0186	3fc46920-3046-4423-9851-db767fbee3c7
d7600272-a9ed-4730-9653-81258ff9996a	3fc46920-3046-4423-9851-db767fbee3c7
5f76e419-73a6-4b89-ab4a-4abb8632e33c	3fc46920-3046-4423-9851-db767fbee3c7
dde473d8-ca2c-44e1-8009-4a8eace8e57a	3fc46920-3046-4423-9851-db767fbee3c7
49f9677e-47f9-46ee-91c3-45d0734f0e9a	3fc46920-3046-4423-9851-db767fbee3c7
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	3fc46920-3046-4423-9851-db767fbee3c7
51454aa6-be41-4445-972f-d40bb4a6ec61	3fc46920-3046-4423-9851-db767fbee3c7
18fd272b-c4b7-4d22-b870-c81768c0bffc	3fc46920-3046-4423-9851-db767fbee3c7
62fc499f-422d-48e2-9200-cd15cc409203	3fc46920-3046-4423-9851-db767fbee3c7
ea09f144-bf42-47b7-89db-c39393c7453e	3fc46920-3046-4423-9851-db767fbee3c7
f561ea0b-4ce7-4118-8a77-f019f6339c53	3fc46920-3046-4423-9851-db767fbee3c7
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	3fc46920-3046-4423-9851-db767fbee3c7
f7a56634-10ca-4560-b372-31a11c6761f2	3fc46920-3046-4423-9851-db767fbee3c7
97877fcd-5162-4cb8-a810-ffb9e273b3db	3fc46920-3046-4423-9851-db767fbee3c7
d5176ee5-ace3-4939-9c92-f6e28f4a1154	3fc46920-3046-4423-9851-db767fbee3c7
210eb72b-b6db-4f86-9969-12e56da66cbe	3fc46920-3046-4423-9851-db767fbee3c7
9826691b-794a-4aec-ad2f-aca0d1066873	3fc46920-3046-4423-9851-db767fbee3c7
a238a18e-512b-4aa5-bd8a-b26213de6739	3fc46920-3046-4423-9851-db767fbee3c7
782efc3c-27fd-4bbc-a4db-61f330521895	3fc46920-3046-4423-9851-db767fbee3c7
93eda126-7711-4029-be8f-82e04d9f41f7	3fc46920-3046-4423-9851-db767fbee3c7
16835618-616f-47d6-a0f2-8592424270ba	3fc46920-3046-4423-9851-db767fbee3c7
1ba00269-7f7b-4082-a530-32ac9ef79d61	3fc46920-3046-4423-9851-db767fbee3c7
d11e8639-90ac-49fc-9304-62a91b0c264d	3fc46920-3046-4423-9851-db767fbee3c7
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	3fc46920-3046-4423-9851-db767fbee3c7
86e01732-079f-4793-9f5b-72f69da8590b	3fc46920-3046-4423-9851-db767fbee3c7
eda9ddd3-5d8e-431f-9a6d-b5eadb14405e	3fc46920-3046-4423-9851-db767fbee3c7
48348210-c240-4dd0-b377-bd6929f7bbaf	3fc46920-3046-4423-9851-db767fbee3c7
ba953395-648d-4e90-89de-e1258b1e1d99	3fc46920-3046-4423-9851-db767fbee3c7
267a82d3-0338-4a28-8267-e2e52f05af39	3fc46920-3046-4423-9851-db767fbee3c7
636cd6e3-0937-4b87-9bf6-0f6946c11f57	3fc46920-3046-4423-9851-db767fbee3c7
cb9f10e6-8121-4e91-a30f-f20c436a1f83	3fc46920-3046-4423-9851-db767fbee3c7
d751a181-a69c-4168-83c1-67a08cf77315	3fc46920-3046-4423-9851-db767fbee3c7
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	3fc46920-3046-4423-9851-db767fbee3c7
b375a7ce-dfdb-43f0-8180-eaafd900c40c	3fc46920-3046-4423-9851-db767fbee3c7
8fc8908f-b782-41c8-98fc-b46746f7bfba	3fc46920-3046-4423-9851-db767fbee3c7
d0432919-9773-4b20-bb8f-e65cf4d6f373	3fc46920-3046-4423-9851-db767fbee3c7
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	3fc46920-3046-4423-9851-db767fbee3c7
b9881ee0-8a9b-4039-afec-e6bca3665e76	3fc46920-3046-4423-9851-db767fbee3c7
65a29a73-9ff3-4423-9583-38df67506e97	3fc46920-3046-4423-9851-db767fbee3c7
ccc731f5-6628-4278-8faa-ff90ffb7abaa	3fc46920-3046-4423-9851-db767fbee3c7
447dea2a-a078-47cf-ac2f-e03f8f6ef585	3fc46920-3046-4423-9851-db767fbee3c7
96ee2d9a-17ae-4bef-9196-c3b460b2a2f7	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
0fcdd438-ca5f-4e47-a8ba-dc5a479535e7	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
701819ca-dc87-4932-9ef4-eb74900b3962	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7042f286-956a-4dbc-b696-2c77581d86bb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
83a46c2b-d09b-49ae-9ddb-f961032af8fb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b20de290-866f-45f1-a33c-122a5bf1b524	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
57b22cca-04fc-447f-ad5d-0d1eff401b5f	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
0f995a1e-25dd-4359-8a0d-ffba517654db	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
d3050429-e99e-46d1-9ebd-400e222d5134	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
639bd728-3a24-4225-928b-f8930732c70c	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
8db4eedb-0ade-4248-a1dd-e5f235d9ecaf	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
fe4ff88e-5d57-421c-b406-714655fdbd1d	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b82a2ace-49e8-43d3-b163-29df0c81b296	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
6e6aa730-bf29-4071-8e6b-096933f3e261	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
830b2887-c9f7-4f20-bfa4-c95261ef3d30	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f5256aab-117a-4ad3-b276-ddd27fc079bc	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f10febe0-07fa-43d1-8f03-4662c55f9e2c	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
702a1381-914b-462a-b19b-275bd4db7ff2	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f0358778-456e-49eb-9c46-5694a41f0186	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
a3c9efc0-e66e-473d-be69-7f3cc120041e	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
9a32db3b-e5c0-400b-8f7e-33dec4920219	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
d0cf588c-060c-413b-83f2-99309eec50bb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
1f1ba0dc-9c41-4e33-a891-8ed99eab961d	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
c9ba43e9-8652-4d34-89db-1a22a14adb07	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
12c8dc7b-ca42-40fb-9cb3-38bb96b64674	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
5cb685af-e5d9-429d-8f8f-c4a92b0b14ec	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
6d470647-2a50-45c7-ab5f-d41f4ff2e8fb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
cab2520d-32c3-4cb4-af28-edf94fe64920	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
39713fcb-1774-430b-972c-c712969b4aaa	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
54ed816e-0a55-4540-bfbf-ec16ec884957	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
393bf858-8373-4b9c-9fcb-79adef17b823	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
a2f206e1-5b4a-4c75-814b-5a2616306003	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
14dd04c3-fda2-42ac-b7da-e46bc97f9f0e	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f7a56634-10ca-4560-b372-31a11c6761f2	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
fbd5a8cb-09f4-4bfd-98c0-bf579c016b45	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7a199e98-ee84-4309-8d72-35ff7130ac47	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
8bd6fead-d21a-4947-9e77-384dc9b2db45	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
52415e78-95a5-43d1-b455-b7598b42aeb9	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7fdf56e4-5687-465b-8c93-d520e40dba62	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
6a93f815-2bec-47d2-a159-ac376174559c	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
3de82401-b5f7-4fd3-8938-b3812c3a6218	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
63fd494e-7fe3-4488-8c10-347ec413fdfd	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
a17bc8e8-f215-4e18-b96a-61070db32d7b	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
d11e8639-90ac-49fc-9304-62a91b0c264d	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
c8d09ce1-456f-4dc8-b092-b717f0b4b5ab	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
0bbc72e4-44a0-442a-aa74-b6a46ba27d1d	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b4aff203-ccf3-476b-af94-b6970ff46130	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
86e01732-079f-4793-9f5b-72f69da8590b	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
ba953395-648d-4e90-89de-e1258b1e1d99	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
982ed45e-4e07-44a4-b8f5-cc3d2c56f433	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b0b56afc-1579-48c2-9ffc-720440b1f601	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
acfc0756-2a83-4b46-a4e4-0adbe441cd38	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
c3afe823-fc30-478a-bfb7-ab60739aeca6	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f35462c3-94e6-480f-9aad-de440723e210	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
cb9f10e6-8121-4e91-a30f-f20c436a1f83	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
d751a181-a69c-4168-83c1-67a08cf77315	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7d412b4f-83ba-4277-b188-cec153c32b2e	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b375a7ce-dfdb-43f0-8180-eaafd900c40c	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b9894b0a-a062-4da7-b18b-8c827620c309	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
e7ace2bf-9dcc-4f39-97bf-289f3a7638e1	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
8529432f-7acc-4f75-bc7e-aa7af2f068aa	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f98a8ddf-630d-4e5b-98db-fbe29d36a03a	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
f2dd1707-c0f8-476c-b81e-ffaeeaec356a	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
b9881ee0-8a9b-4039-afec-e6bca3665e76	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
d88f0387-7041-4251-b2a4-3505c71e0145	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7eb6f8fb-17b1-4382-9566-35e4eec985cd	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
ff01ca02-94de-448b-98f7-019723a203fa	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
275ab079-aeb6-487b-ad02-d4cef821fdd6	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
ccc731f5-6628-4278-8faa-ff90ffb7abaa	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
e907d88c-7e7e-4b4e-9b33-6865f4a6b11a	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
7959cb7a-91c9-4a22-96e5-6f171555260d	b8b552c0-a8ec-44f7-8c6a-70df10e7a149
96ee2d9a-17ae-4bef-9196-c3b460b2a2f7	47d172b5-7863-4175-9a62-a77cc63cf3da
38544a76-1ee7-4569-9033-c8e08778c292	47d172b5-7863-4175-9a62-a77cc63cf3da
701819ca-dc87-4932-9ef4-eb74900b3962	47d172b5-7863-4175-9a62-a77cc63cf3da
7042f286-956a-4dbc-b696-2c77581d86bb	47d172b5-7863-4175-9a62-a77cc63cf3da
9a35e10d-42af-48b3-9a10-cad37f018dab	47d172b5-7863-4175-9a62-a77cc63cf3da
8f04d44e-bbcb-4743-926d-f795b8e65de8	47d172b5-7863-4175-9a62-a77cc63cf3da
639bd728-3a24-4225-928b-f8930732c70c	47d172b5-7863-4175-9a62-a77cc63cf3da
533a090b-5705-43fc-86bf-a24537cddb53	47d172b5-7863-4175-9a62-a77cc63cf3da
24b5087c-57d1-4dec-af85-b4418ab71ea3	47d172b5-7863-4175-9a62-a77cc63cf3da
830b2887-c9f7-4f20-bfa4-c95261ef3d30	47d172b5-7863-4175-9a62-a77cc63cf3da
a3c9efc0-e66e-473d-be69-7f3cc120041e	47d172b5-7863-4175-9a62-a77cc63cf3da
5f76e419-73a6-4b89-ab4a-4abb8632e33c	47d172b5-7863-4175-9a62-a77cc63cf3da
d7600272-a9ed-4730-9653-81258ff9996a	47d172b5-7863-4175-9a62-a77cc63cf3da
4b34957c-86c5-4f7d-b169-fe0f36a8ab16	47d172b5-7863-4175-9a62-a77cc63cf3da
24942230-212b-4b13-9931-4b5db634a7ab	47d172b5-7863-4175-9a62-a77cc63cf3da
595dd377-597e-4066-af12-b3a9835e630a	47d172b5-7863-4175-9a62-a77cc63cf3da
49f9677e-47f9-46ee-91c3-45d0734f0e9a	47d172b5-7863-4175-9a62-a77cc63cf3da
51454aa6-be41-4445-972f-d40bb4a6ec61	47d172b5-7863-4175-9a62-a77cc63cf3da
12c8dc7b-ca42-40fb-9cb3-38bb96b64674	47d172b5-7863-4175-9a62-a77cc63cf3da
cab2520d-32c3-4cb4-af28-edf94fe64920	47d172b5-7863-4175-9a62-a77cc63cf3da
9cd88c81-9bad-41e2-9cf5-b7faba2e1d76	47d172b5-7863-4175-9a62-a77cc63cf3da
39713fcb-1774-430b-972c-c712969b4aaa	47d172b5-7863-4175-9a62-a77cc63cf3da
62fc499f-422d-48e2-9200-cd15cc409203	47d172b5-7863-4175-9a62-a77cc63cf3da
aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b	47d172b5-7863-4175-9a62-a77cc63cf3da
8c383dbf-7ba0-42d2-a048-430a04c866e7	47d172b5-7863-4175-9a62-a77cc63cf3da
4350b070-3eea-4cb8-b3d0-7d3c753e33f3	47d172b5-7863-4175-9a62-a77cc63cf3da
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	47d172b5-7863-4175-9a62-a77cc63cf3da
37ccc457-85b1-4192-bad0-83bba00950b2	47d172b5-7863-4175-9a62-a77cc63cf3da
97877fcd-5162-4cb8-a810-ffb9e273b3db	47d172b5-7863-4175-9a62-a77cc63cf3da
1c76efdb-7597-4ab3-a6f0-7a94b64760e1	47d172b5-7863-4175-9a62-a77cc63cf3da
8bd6fead-d21a-4947-9e77-384dc9b2db45	47d172b5-7863-4175-9a62-a77cc63cf3da
3db4d7d2-251c-4024-b8be-827cab44e3d9	47d172b5-7863-4175-9a62-a77cc63cf3da
0283fc09-7bb4-4233-ae2b-d08f0f1c4f0f	47d172b5-7863-4175-9a62-a77cc63cf3da
2e2a4648-f599-4f70-ac3a-7453b3b1055d	47d172b5-7863-4175-9a62-a77cc63cf3da
0dab5ff3-04a2-43a7-9312-c296c4d45675	47d172b5-7863-4175-9a62-a77cc63cf3da
7fdf56e4-5687-465b-8c93-d520e40dba62	47d172b5-7863-4175-9a62-a77cc63cf3da
4b9b80ad-1491-49d0-b624-e5e26aedf7e3	47d172b5-7863-4175-9a62-a77cc63cf3da
6a93f815-2bec-47d2-a159-ac376174559c	47d172b5-7863-4175-9a62-a77cc63cf3da
5615a6cc-12af-4479-909d-6afd5d82d711	47d172b5-7863-4175-9a62-a77cc63cf3da
16835618-616f-47d6-a0f2-8592424270ba	47d172b5-7863-4175-9a62-a77cc63cf3da
86e01732-079f-4793-9f5b-72f69da8590b	47d172b5-7863-4175-9a62-a77cc63cf3da
eda9ddd3-5d8e-431f-9a6d-b5eadb14405e	47d172b5-7863-4175-9a62-a77cc63cf3da
b2622786-8c32-4971-bb0a-0a56b72df3ec	47d172b5-7863-4175-9a62-a77cc63cf3da
b0b56afc-1579-48c2-9ffc-720440b1f601	47d172b5-7863-4175-9a62-a77cc63cf3da
538bdb7a-742b-44db-8b32-a5d9fbb434b9	47d172b5-7863-4175-9a62-a77cc63cf3da
cb900cb7-6a98-45c8-9566-9da26559aedc	47d172b5-7863-4175-9a62-a77cc63cf3da
d808320f-39c1-4193-88ab-cdb7a82af8b8	47d172b5-7863-4175-9a62-a77cc63cf3da
b9894b0a-a062-4da7-b18b-8c827620c309	47d172b5-7863-4175-9a62-a77cc63cf3da
f98a8ddf-630d-4e5b-98db-fbe29d36a03a	47d172b5-7863-4175-9a62-a77cc63cf3da
5331e26f-246f-46fa-b2a7-48df197d6fa9	47d172b5-7863-4175-9a62-a77cc63cf3da
0fcdd438-ca5f-4e47-a8ba-dc5a479535e7	47d172b5-7863-4175-9a62-a77cc63cf3da
206d134c-a21c-47d6-9634-dea5832cc911	47d172b5-7863-4175-9a62-a77cc63cf3da
8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4	47d172b5-7863-4175-9a62-a77cc63cf3da
a2f08de8-cbf6-4711-b932-6d4adcf5200d	47d172b5-7863-4175-9a62-a77cc63cf3da
0f995a1e-25dd-4359-8a0d-ffba517654db	47d172b5-7863-4175-9a62-a77cc63cf3da
84f00d8e-2576-497f-8401-5dd68506f502	47d172b5-7863-4175-9a62-a77cc63cf3da
64de3d9d-e116-438b-ae58-8de3e9e42384	47d172b5-7863-4175-9a62-a77cc63cf3da
b1d83932-0ea9-42dc-8578-8e6063f54ff3	47d172b5-7863-4175-9a62-a77cc63cf3da
b78c5bd2-c526-430b-8ed4-4fedf2858cc5	47d172b5-7863-4175-9a62-a77cc63cf3da
11eec72e-8f59-4c5e-9095-817a6fad0b0b	47d172b5-7863-4175-9a62-a77cc63cf3da
b82a2ace-49e8-43d3-b163-29df0c81b296	47d172b5-7863-4175-9a62-a77cc63cf3da
f10febe0-07fa-43d1-8f03-4662c55f9e2c	47d172b5-7863-4175-9a62-a77cc63cf3da
4917596f-f29d-47e0-9cc5-56f326951b75	47d172b5-7863-4175-9a62-a77cc63cf3da
d0cf588c-060c-413b-83f2-99309eec50bb	47d172b5-7863-4175-9a62-a77cc63cf3da
dde473d8-ca2c-44e1-8009-4a8eace8e57a	47d172b5-7863-4175-9a62-a77cc63cf3da
0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6	47d172b5-7863-4175-9a62-a77cc63cf3da
c098d34e-a341-4d3b-b4dd-eb3551b96ebd	47d172b5-7863-4175-9a62-a77cc63cf3da
5cb685af-e5d9-429d-8f8f-c4a92b0b14ec	47d172b5-7863-4175-9a62-a77cc63cf3da
785e830b-5455-4ed8-a420-3165752f5b7c	47d172b5-7863-4175-9a62-a77cc63cf3da
09d23fad-d2da-4319-9408-5d9948971a18	47d172b5-7863-4175-9a62-a77cc63cf3da
ea09f144-bf42-47b7-89db-c39393c7453e	47d172b5-7863-4175-9a62-a77cc63cf3da
393bf858-8373-4b9c-9fcb-79adef17b823	47d172b5-7863-4175-9a62-a77cc63cf3da
a2f206e1-5b4a-4c75-814b-5a2616306003	47d172b5-7863-4175-9a62-a77cc63cf3da
f561ea0b-4ce7-4118-8a77-f019f6339c53	47d172b5-7863-4175-9a62-a77cc63cf3da
fbd5a8cb-09f4-4bfd-98c0-bf579c016b45	47d172b5-7863-4175-9a62-a77cc63cf3da
835503d8-7873-4139-bbf5-9bd46a4d7555	47d172b5-7863-4175-9a62-a77cc63cf3da
7a199e98-ee84-4309-8d72-35ff7130ac47	47d172b5-7863-4175-9a62-a77cc63cf3da
77becf3c-686e-4378-a750-0cc9365facc3	47d172b5-7863-4175-9a62-a77cc63cf3da
ebeaafd2-41a5-4289-926c-3dd61928d266	47d172b5-7863-4175-9a62-a77cc63cf3da
7df2f5b2-eb93-4907-8f52-8c183ebfdf4e	47d172b5-7863-4175-9a62-a77cc63cf3da
3de82401-b5f7-4fd3-8938-b3812c3a6218	47d172b5-7863-4175-9a62-a77cc63cf3da
de59e869-4a8c-425e-b65b-986675c547ac	47d172b5-7863-4175-9a62-a77cc63cf3da
782efc3c-27fd-4bbc-a4db-61f330521895	47d172b5-7863-4175-9a62-a77cc63cf3da
9b94cb3a-52f5-4167-9db0-805bf8003cf1	47d172b5-7863-4175-9a62-a77cc63cf3da
43bebee7-3f29-41f9-b422-780ca73aaaf3	47d172b5-7863-4175-9a62-a77cc63cf3da
26504250-43fd-4151-a3ab-698514b4422f	47d172b5-7863-4175-9a62-a77cc63cf3da
48348210-c240-4dd0-b377-bd6929f7bbaf	47d172b5-7863-4175-9a62-a77cc63cf3da
982ed45e-4e07-44a4-b8f5-cc3d2c56f433	47d172b5-7863-4175-9a62-a77cc63cf3da
f35462c3-94e6-480f-9aad-de440723e210	47d172b5-7863-4175-9a62-a77cc63cf3da
d751a181-a69c-4168-83c1-67a08cf77315	47d172b5-7863-4175-9a62-a77cc63cf3da
7d412b4f-83ba-4277-b188-cec153c32b2e	47d172b5-7863-4175-9a62-a77cc63cf3da
e7ace2bf-9dcc-4f39-97bf-289f3a7638e1	47d172b5-7863-4175-9a62-a77cc63cf3da
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	47d172b5-7863-4175-9a62-a77cc63cf3da
d88f0387-7041-4251-b2a4-3505c71e0145	47d172b5-7863-4175-9a62-a77cc63cf3da
ccc731f5-6628-4278-8faa-ff90ffb7abaa	47d172b5-7863-4175-9a62-a77cc63cf3da
9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb	47d172b5-7863-4175-9a62-a77cc63cf3da
7959cb7a-91c9-4a22-96e5-6f171555260d	47d172b5-7863-4175-9a62-a77cc63cf3da
a1231bfc-991a-427d-b578-9e361f16d571	47d172b5-7863-4175-9a62-a77cc63cf3da
932746ea-68f2-4111-94c0-65be660c5d29	47d172b5-7863-4175-9a62-a77cc63cf3da
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	47d172b5-7863-4175-9a62-a77cc63cf3da
83a46c2b-d09b-49ae-9ddb-f961032af8fb	47d172b5-7863-4175-9a62-a77cc63cf3da
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	47d172b5-7863-4175-9a62-a77cc63cf3da
b20de290-866f-45f1-a33c-122a5bf1b524	47d172b5-7863-4175-9a62-a77cc63cf3da
fae35cea-412d-4e9a-811a-9496a6fbd663	47d172b5-7863-4175-9a62-a77cc63cf3da
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	47d172b5-7863-4175-9a62-a77cc63cf3da
d0188960-83a2-44d9-87e6-ff241857c393	47d172b5-7863-4175-9a62-a77cc63cf3da
d3050429-e99e-46d1-9ebd-400e222d5134	47d172b5-7863-4175-9a62-a77cc63cf3da
6e6aa730-bf29-4071-8e6b-096933f3e261	47d172b5-7863-4175-9a62-a77cc63cf3da
f4d71eaa-36e9-4f68-b4e3-d70d0d2f7e34	47d172b5-7863-4175-9a62-a77cc63cf3da
f0358778-456e-49eb-9c46-5694a41f0186	47d172b5-7863-4175-9a62-a77cc63cf3da
25deb52f-6114-42f0-b594-d94e47f528a1	47d172b5-7863-4175-9a62-a77cc63cf3da
2ce28b99-a3d9-41a1-834b-ad09c808b12d	47d172b5-7863-4175-9a62-a77cc63cf3da
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	47d172b5-7863-4175-9a62-a77cc63cf3da
86442a1f-c323-44b7-b773-2c1d42db7217	47d172b5-7863-4175-9a62-a77cc63cf3da
1f1ba0dc-9c41-4e33-a891-8ed99eab961d	47d172b5-7863-4175-9a62-a77cc63cf3da
96d9118e-2b2f-4bc1-8813-47bf99ef578a	47d172b5-7863-4175-9a62-a77cc63cf3da
3e1a3a50-a7c4-45f9-ac13-cc82c9f7d405	47d172b5-7863-4175-9a62-a77cc63cf3da
b868a581-fba5-4895-959d-80aaedc49f55	47d172b5-7863-4175-9a62-a77cc63cf3da
8607b79d-53fb-4562-b53c-7f0ea844c722	47d172b5-7863-4175-9a62-a77cc63cf3da
e39ed88a-fe46-4a3a-bca6-5840e52d2856	47d172b5-7863-4175-9a62-a77cc63cf3da
54ed816e-0a55-4540-bfbf-ec16ec884957	47d172b5-7863-4175-9a62-a77cc63cf3da
c399da7d-1c72-4e7c-959c-1dce9684916c	47d172b5-7863-4175-9a62-a77cc63cf3da
f00c449c-be6f-4c2a-bf0a-0fc27caa6d06	47d172b5-7863-4175-9a62-a77cc63cf3da
14dd04c3-fda2-42ac-b7da-e46bc97f9f0e	47d172b5-7863-4175-9a62-a77cc63cf3da
0007acec-c38e-43c3-9d1c-84b22cf45223	47d172b5-7863-4175-9a62-a77cc63cf3da
4d913333-8c13-4056-8593-32259ee3b787	47d172b5-7863-4175-9a62-a77cc63cf3da
d5176ee5-ace3-4939-9c92-f6e28f4a1154	47d172b5-7863-4175-9a62-a77cc63cf3da
58874d83-90b2-4a46-b4fd-6d16cfc92b38	47d172b5-7863-4175-9a62-a77cc63cf3da
52415e78-95a5-43d1-b455-b7598b42aeb9	47d172b5-7863-4175-9a62-a77cc63cf3da
f470bb89-8dc9-4279-8b81-f3c96da8933a	47d172b5-7863-4175-9a62-a77cc63cf3da
210eb72b-b6db-4f86-9969-12e56da66cbe	47d172b5-7863-4175-9a62-a77cc63cf3da
9826691b-794a-4aec-ad2f-aca0d1066873	47d172b5-7863-4175-9a62-a77cc63cf3da
63fd494e-7fe3-4488-8c10-347ec413fdfd	47d172b5-7863-4175-9a62-a77cc63cf3da
9a380bfb-edab-405b-add9-4e7cec35ef73	47d172b5-7863-4175-9a62-a77cc63cf3da
93eda126-7711-4029-be8f-82e04d9f41f7	47d172b5-7863-4175-9a62-a77cc63cf3da
a17bc8e8-f215-4e18-b96a-61070db32d7b	47d172b5-7863-4175-9a62-a77cc63cf3da
1ba00269-7f7b-4082-a530-32ac9ef79d61	47d172b5-7863-4175-9a62-a77cc63cf3da
8ee93852-790f-4183-9da1-8eab09b3c29a	47d172b5-7863-4175-9a62-a77cc63cf3da
0bbc72e4-44a0-442a-aa74-b6a46ba27d1d	47d172b5-7863-4175-9a62-a77cc63cf3da
b4aff203-ccf3-476b-af94-b6970ff46130	47d172b5-7863-4175-9a62-a77cc63cf3da
ba953395-648d-4e90-89de-e1258b1e1d99	47d172b5-7863-4175-9a62-a77cc63cf3da
1714a76b-e10e-48b3-a097-1486442f5eac	47d172b5-7863-4175-9a62-a77cc63cf3da
267a82d3-0338-4a28-8267-e2e52f05af39	47d172b5-7863-4175-9a62-a77cc63cf3da
636cd6e3-0937-4b87-9bf6-0f6946c11f57	47d172b5-7863-4175-9a62-a77cc63cf3da
cb9f10e6-8121-4e91-a30f-f20c436a1f83	47d172b5-7863-4175-9a62-a77cc63cf3da
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	47d172b5-7863-4175-9a62-a77cc63cf3da
b375a7ce-dfdb-43f0-8180-eaafd900c40c	47d172b5-7863-4175-9a62-a77cc63cf3da
8fc8908f-b782-41c8-98fc-b46746f7bfba	47d172b5-7863-4175-9a62-a77cc63cf3da
bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2	47d172b5-7863-4175-9a62-a77cc63cf3da
a811007a-334b-4692-81fe-01509f3e307d	47d172b5-7863-4175-9a62-a77cc63cf3da
2383aca2-bafb-40df-a4ed-a73c11cd33a5	47d172b5-7863-4175-9a62-a77cc63cf3da
65a29a73-9ff3-4423-9583-38df67506e97	47d172b5-7863-4175-9a62-a77cc63cf3da
275ab079-aeb6-487b-ad02-d4cef821fdd6	47d172b5-7863-4175-9a62-a77cc63cf3da
447dea2a-a078-47cf-ac2f-e03f8f6ef585	47d172b5-7863-4175-9a62-a77cc63cf3da
ed24b8d5-65b7-4e91-9438-6c663d160a8a	47d172b5-7863-4175-9a62-a77cc63cf3da
67420711-e263-4276-899d-0cb6d8b4c704	47d172b5-7863-4175-9a62-a77cc63cf3da
7117f962-24c7-463d-8255-cf2ccb881dc8	47d172b5-7863-4175-9a62-a77cc63cf3da
57b22cca-04fc-447f-ad5d-0d1eff401b5f	47d172b5-7863-4175-9a62-a77cc63cf3da
00d10d34-9060-4976-8941-454bd64e9712	47d172b5-7863-4175-9a62-a77cc63cf3da
9a4a7903-42c9-4af9-9aff-4ea86d0e8cfb	47d172b5-7863-4175-9a62-a77cc63cf3da
8db4eedb-0ade-4248-a1dd-e5f235d9ecaf	47d172b5-7863-4175-9a62-a77cc63cf3da
fe4ff88e-5d57-421c-b406-714655fdbd1d	47d172b5-7863-4175-9a62-a77cc63cf3da
f5256aab-117a-4ad3-b276-ddd27fc079bc	47d172b5-7863-4175-9a62-a77cc63cf3da
6cdbe9b1-2bd3-4069-8379-01a4d3ff1fe0	47d172b5-7863-4175-9a62-a77cc63cf3da
702a1381-914b-462a-b19b-275bd4db7ff2	47d172b5-7863-4175-9a62-a77cc63cf3da
9a32db3b-e5c0-400b-8f7e-33dec4920219	47d172b5-7863-4175-9a62-a77cc63cf3da
b3ac4a14-cd60-4705-bec3-648cfbc5635d	47d172b5-7863-4175-9a62-a77cc63cf3da
5f721066-1413-4483-8fdc-b3227aa5ae71	47d172b5-7863-4175-9a62-a77cc63cf3da
44fd3a81-1dcb-4070-9dee-57437b90ff80	47d172b5-7863-4175-9a62-a77cc63cf3da
125735e5-09c4-4739-b7e7-adcb8413869d	47d172b5-7863-4175-9a62-a77cc63cf3da
8bbc7b0b-4d57-4f61-9e24-bcabd986bc2a	47d172b5-7863-4175-9a62-a77cc63cf3da
5cfa28ac-41cf-4072-840b-f1437ae4087e	47d172b5-7863-4175-9a62-a77cc63cf3da
c9ba43e9-8652-4d34-89db-1a22a14adb07	47d172b5-7863-4175-9a62-a77cc63cf3da
8abc0aa6-5b30-4d94-9f0a-bdf8600c9285	47d172b5-7863-4175-9a62-a77cc63cf3da
e4583cb5-5770-43a9-95e9-b39981b947cf	47d172b5-7863-4175-9a62-a77cc63cf3da
6d470647-2a50-45c7-ab5f-d41f4ff2e8fb	47d172b5-7863-4175-9a62-a77cc63cf3da
18fd272b-c4b7-4d22-b870-c81768c0bffc	47d172b5-7863-4175-9a62-a77cc63cf3da
e0790f61-dc64-4ad7-92f5-07374ea3043d	47d172b5-7863-4175-9a62-a77cc63cf3da
22ae069e-4893-42bc-b4c3-9d4fb2a85792	47d172b5-7863-4175-9a62-a77cc63cf3da
009e9aa5-e6bc-4a03-9052-be5866fede7b	47d172b5-7863-4175-9a62-a77cc63cf3da
f7a56634-10ca-4560-b372-31a11c6761f2	47d172b5-7863-4175-9a62-a77cc63cf3da
34851926-ba58-427f-aed2-408074f74bcc	47d172b5-7863-4175-9a62-a77cc63cf3da
253ed92b-51e7-4dc8-ab10-f9dd6d334209	47d172b5-7863-4175-9a62-a77cc63cf3da
4d003da0-e5b9-46a8-9630-723d7d0ff2a1	47d172b5-7863-4175-9a62-a77cc63cf3da
813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63	47d172b5-7863-4175-9a62-a77cc63cf3da
5c3b1f91-c37f-45f5-9a12-ee6dfdfd2879	47d172b5-7863-4175-9a62-a77cc63cf3da
0faad761-4f4d-4e53-936c-eff0f8f19d56	47d172b5-7863-4175-9a62-a77cc63cf3da
0ec9af08-b459-4e79-b49d-b3bd93b5183d	47d172b5-7863-4175-9a62-a77cc63cf3da
e081184b-1f03-4109-b27e-edfaa15180ee	47d172b5-7863-4175-9a62-a77cc63cf3da
a238a18e-512b-4aa5-bd8a-b26213de6739	47d172b5-7863-4175-9a62-a77cc63cf3da
7bd41e59-50b9-4287-a3eb-7d295155ed98	47d172b5-7863-4175-9a62-a77cc63cf3da
6819ef1e-0478-4a68-b0b9-0bab0723819f	47d172b5-7863-4175-9a62-a77cc63cf3da
2420c15a-9f92-4e5b-97af-90acc3eecabe	47d172b5-7863-4175-9a62-a77cc63cf3da
d11e8639-90ac-49fc-9304-62a91b0c264d	47d172b5-7863-4175-9a62-a77cc63cf3da
c8d09ce1-456f-4dc8-b092-b717f0b4b5ab	47d172b5-7863-4175-9a62-a77cc63cf3da
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	47d172b5-7863-4175-9a62-a77cc63cf3da
dd927140-987b-45f9-8df3-2cc5b6510e9d	47d172b5-7863-4175-9a62-a77cc63cf3da
5efbba82-03b2-40f9-a909-2423099cfd65	47d172b5-7863-4175-9a62-a77cc63cf3da
acfc0756-2a83-4b46-a4e4-0adbe441cd38	47d172b5-7863-4175-9a62-a77cc63cf3da
c3afe823-fc30-478a-bfb7-ab60739aeca6	47d172b5-7863-4175-9a62-a77cc63cf3da
28580873-d8aa-49ad-808b-a4ded351b415	47d172b5-7863-4175-9a62-a77cc63cf3da
8529432f-7acc-4f75-bc7e-aa7af2f068aa	47d172b5-7863-4175-9a62-a77cc63cf3da
d0432919-9773-4b20-bb8f-e65cf4d6f373	47d172b5-7863-4175-9a62-a77cc63cf3da
1c4a3eaa-6ad6-4ffe-91ac-b127201e0493	47d172b5-7863-4175-9a62-a77cc63cf3da
f2dd1707-c0f8-476c-b81e-ffaeeaec356a	47d172b5-7863-4175-9a62-a77cc63cf3da
b9881ee0-8a9b-4039-afec-e6bca3665e76	47d172b5-7863-4175-9a62-a77cc63cf3da
7eb6f8fb-17b1-4382-9566-35e4eec985cd	47d172b5-7863-4175-9a62-a77cc63cf3da
d7575538-d923-4a71-95ab-a73d5ba019e5	47d172b5-7863-4175-9a62-a77cc63cf3da
ff01ca02-94de-448b-98f7-019723a203fa	47d172b5-7863-4175-9a62-a77cc63cf3da
0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179	47d172b5-7863-4175-9a62-a77cc63cf3da
18b5f174-70fb-41c9-98c2-e92829150139	47d172b5-7863-4175-9a62-a77cc63cf3da
e907d88c-7e7e-4b4e-9b33-6865f4a6b11a	47d172b5-7863-4175-9a62-a77cc63cf3da
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	96d81e07-e3f9-4206-88f3-76328cbbb9b8
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	96d81e07-e3f9-4206-88f3-76328cbbb9b8
b20de290-866f-45f1-a33c-122a5bf1b524	96d81e07-e3f9-4206-88f3-76328cbbb9b8
a2f08de8-cbf6-4711-b932-6d4adcf5200d	96d81e07-e3f9-4206-88f3-76328cbbb9b8
67420711-e263-4276-899d-0cb6d8b4c704	96d81e07-e3f9-4206-88f3-76328cbbb9b8
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	96d81e07-e3f9-4206-88f3-76328cbbb9b8
639bd728-3a24-4225-928b-f8930732c70c	96d81e07-e3f9-4206-88f3-76328cbbb9b8
9a35e10d-42af-48b3-9a10-cad37f018dab	96d81e07-e3f9-4206-88f3-76328cbbb9b8
533a090b-5705-43fc-86bf-a24537cddb53	96d81e07-e3f9-4206-88f3-76328cbbb9b8
b82a2ace-49e8-43d3-b163-29df0c81b296	96d81e07-e3f9-4206-88f3-76328cbbb9b8
6e6aa730-bf29-4071-8e6b-096933f3e261	96d81e07-e3f9-4206-88f3-76328cbbb9b8
830b2887-c9f7-4f20-bfa4-c95261ef3d30	96d81e07-e3f9-4206-88f3-76328cbbb9b8
f0358778-456e-49eb-9c46-5694a41f0186	96d81e07-e3f9-4206-88f3-76328cbbb9b8
d7600272-a9ed-4730-9653-81258ff9996a	96d81e07-e3f9-4206-88f3-76328cbbb9b8
5f76e419-73a6-4b89-ab4a-4abb8632e33c	96d81e07-e3f9-4206-88f3-76328cbbb9b8
dde473d8-ca2c-44e1-8009-4a8eace8e57a	96d81e07-e3f9-4206-88f3-76328cbbb9b8
49f9677e-47f9-46ee-91c3-45d0734f0e9a	96d81e07-e3f9-4206-88f3-76328cbbb9b8
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	96d81e07-e3f9-4206-88f3-76328cbbb9b8
51454aa6-be41-4445-972f-d40bb4a6ec61	96d81e07-e3f9-4206-88f3-76328cbbb9b8
18fd272b-c4b7-4d22-b870-c81768c0bffc	96d81e07-e3f9-4206-88f3-76328cbbb9b8
62fc499f-422d-48e2-9200-cd15cc409203	96d81e07-e3f9-4206-88f3-76328cbbb9b8
ea09f144-bf42-47b7-89db-c39393c7453e	96d81e07-e3f9-4206-88f3-76328cbbb9b8
f561ea0b-4ce7-4118-8a77-f019f6339c53	96d81e07-e3f9-4206-88f3-76328cbbb9b8
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	96d81e07-e3f9-4206-88f3-76328cbbb9b8
f7a56634-10ca-4560-b372-31a11c6761f2	96d81e07-e3f9-4206-88f3-76328cbbb9b8
dbc4c807-4f3a-44de-88be-3216cd078b29	96d81e07-e3f9-4206-88f3-76328cbbb9b8
97877fcd-5162-4cb8-a810-ffb9e273b3db	96d81e07-e3f9-4206-88f3-76328cbbb9b8
d5176ee5-ace3-4939-9c92-f6e28f4a1154	96d81e07-e3f9-4206-88f3-76328cbbb9b8
210eb72b-b6db-4f86-9969-12e56da66cbe	96d81e07-e3f9-4206-88f3-76328cbbb9b8
9826691b-794a-4aec-ad2f-aca0d1066873	96d81e07-e3f9-4206-88f3-76328cbbb9b8
a238a18e-512b-4aa5-bd8a-b26213de6739	96d81e07-e3f9-4206-88f3-76328cbbb9b8
782efc3c-27fd-4bbc-a4db-61f330521895	96d81e07-e3f9-4206-88f3-76328cbbb9b8
93eda126-7711-4029-be8f-82e04d9f41f7	96d81e07-e3f9-4206-88f3-76328cbbb9b8
16835618-616f-47d6-a0f2-8592424270ba	96d81e07-e3f9-4206-88f3-76328cbbb9b8
1ba00269-7f7b-4082-a530-32ac9ef79d61	96d81e07-e3f9-4206-88f3-76328cbbb9b8
d11e8639-90ac-49fc-9304-62a91b0c264d	96d81e07-e3f9-4206-88f3-76328cbbb9b8
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	96d81e07-e3f9-4206-88f3-76328cbbb9b8
86e01732-079f-4793-9f5b-72f69da8590b	96d81e07-e3f9-4206-88f3-76328cbbb9b8
eda9ddd3-5d8e-431f-9a6d-b5eadb14405e	96d81e07-e3f9-4206-88f3-76328cbbb9b8
48348210-c240-4dd0-b377-bd6929f7bbaf	96d81e07-e3f9-4206-88f3-76328cbbb9b8
ba953395-648d-4e90-89de-e1258b1e1d99	96d81e07-e3f9-4206-88f3-76328cbbb9b8
267a82d3-0338-4a28-8267-e2e52f05af39	96d81e07-e3f9-4206-88f3-76328cbbb9b8
636cd6e3-0937-4b87-9bf6-0f6946c11f57	96d81e07-e3f9-4206-88f3-76328cbbb9b8
cb9f10e6-8121-4e91-a30f-f20c436a1f83	96d81e07-e3f9-4206-88f3-76328cbbb9b8
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	96d81e07-e3f9-4206-88f3-76328cbbb9b8
b375a7ce-dfdb-43f0-8180-eaafd900c40c	96d81e07-e3f9-4206-88f3-76328cbbb9b8
8fc8908f-b782-41c8-98fc-b46746f7bfba	96d81e07-e3f9-4206-88f3-76328cbbb9b8
d0432919-9773-4b20-bb8f-e65cf4d6f373	96d81e07-e3f9-4206-88f3-76328cbbb9b8
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	96d81e07-e3f9-4206-88f3-76328cbbb9b8
b9881ee0-8a9b-4039-afec-e6bca3665e76	96d81e07-e3f9-4206-88f3-76328cbbb9b8
65a29a73-9ff3-4423-9583-38df67506e97	96d81e07-e3f9-4206-88f3-76328cbbb9b8
ccc731f5-6628-4278-8faa-ff90ffb7abaa	96d81e07-e3f9-4206-88f3-76328cbbb9b8
447dea2a-a078-47cf-ac2f-e03f8f6ef585	96d81e07-e3f9-4206-88f3-76328cbbb9b8
96ee2d9a-17ae-4bef-9196-c3b460b2a2f7	a29acdd2-e748-4989-88ef-53d5280d664f
0fcdd438-ca5f-4e47-a8ba-dc5a479535e7	a29acdd2-e748-4989-88ef-53d5280d664f
701819ca-dc87-4932-9ef4-eb74900b3962	a29acdd2-e748-4989-88ef-53d5280d664f
8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4	a29acdd2-e748-4989-88ef-53d5280d664f
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	a29acdd2-e748-4989-88ef-53d5280d664f
7042f286-956a-4dbc-b696-2c77581d86bb	a29acdd2-e748-4989-88ef-53d5280d664f
83a46c2b-d09b-49ae-9ddb-f961032af8fb	a29acdd2-e748-4989-88ef-53d5280d664f
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	a29acdd2-e748-4989-88ef-53d5280d664f
b20de290-866f-45f1-a33c-122a5bf1b524	a29acdd2-e748-4989-88ef-53d5280d664f
a2f08de8-cbf6-4711-b932-6d4adcf5200d	a29acdd2-e748-4989-88ef-53d5280d664f
57b22cca-04fc-447f-ad5d-0d1eff401b5f	a29acdd2-e748-4989-88ef-53d5280d664f
0f995a1e-25dd-4359-8a0d-ffba517654db	a29acdd2-e748-4989-88ef-53d5280d664f
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	a29acdd2-e748-4989-88ef-53d5280d664f
d3050429-e99e-46d1-9ebd-400e222d5134	a29acdd2-e748-4989-88ef-53d5280d664f
639bd728-3a24-4225-928b-f8930732c70c	a29acdd2-e748-4989-88ef-53d5280d664f
fe4ff88e-5d57-421c-b406-714655fdbd1d	a29acdd2-e748-4989-88ef-53d5280d664f
b82a2ace-49e8-43d3-b163-29df0c81b296	a29acdd2-e748-4989-88ef-53d5280d664f
6e6aa730-bf29-4071-8e6b-096933f3e261	a29acdd2-e748-4989-88ef-53d5280d664f
830b2887-c9f7-4f20-bfa4-c95261ef3d30	a29acdd2-e748-4989-88ef-53d5280d664f
f5256aab-117a-4ad3-b276-ddd27fc079bc	a29acdd2-e748-4989-88ef-53d5280d664f
f10febe0-07fa-43d1-8f03-4662c55f9e2c	a29acdd2-e748-4989-88ef-53d5280d664f
702a1381-914b-462a-b19b-275bd4db7ff2	a29acdd2-e748-4989-88ef-53d5280d664f
f0358778-456e-49eb-9c46-5694a41f0186	a29acdd2-e748-4989-88ef-53d5280d664f
a3c9efc0-e66e-473d-be69-7f3cc120041e	a29acdd2-e748-4989-88ef-53d5280d664f
9a32db3b-e5c0-400b-8f7e-33dec4920219	a29acdd2-e748-4989-88ef-53d5280d664f
d7600272-a9ed-4730-9653-81258ff9996a	a29acdd2-e748-4989-88ef-53d5280d664f
5f76e419-73a6-4b89-ab4a-4abb8632e33c	a29acdd2-e748-4989-88ef-53d5280d664f
d0cf588c-060c-413b-83f2-99309eec50bb	a29acdd2-e748-4989-88ef-53d5280d664f
0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6	a29acdd2-e748-4989-88ef-53d5280d664f
49f9677e-47f9-46ee-91c3-45d0734f0e9a	a29acdd2-e748-4989-88ef-53d5280d664f
e7f78a9d-12cd-4ad4-8bc7-e29e40cff46c	a29acdd2-e748-4989-88ef-53d5280d664f
51454aa6-be41-4445-972f-d40bb4a6ec61	a29acdd2-e748-4989-88ef-53d5280d664f
1f1ba0dc-9c41-4e33-a891-8ed99eab961d	a29acdd2-e748-4989-88ef-53d5280d664f
c9ba43e9-8652-4d34-89db-1a22a14adb07	a29acdd2-e748-4989-88ef-53d5280d664f
12c8dc7b-ca42-40fb-9cb3-38bb96b64674	a29acdd2-e748-4989-88ef-53d5280d664f
5cb685af-e5d9-429d-8f8f-c4a92b0b14ec	a29acdd2-e748-4989-88ef-53d5280d664f
6d470647-2a50-45c7-ab5f-d41f4ff2e8fb	a29acdd2-e748-4989-88ef-53d5280d664f
e39ed88a-fe46-4a3a-bca6-5840e52d2856	a29acdd2-e748-4989-88ef-53d5280d664f
cab2520d-32c3-4cb4-af28-edf94fe64920	a29acdd2-e748-4989-88ef-53d5280d664f
39713fcb-1774-430b-972c-c712969b4aaa	a29acdd2-e748-4989-88ef-53d5280d664f
aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b	a29acdd2-e748-4989-88ef-53d5280d664f
54ed816e-0a55-4540-bfbf-ec16ec884957	a29acdd2-e748-4989-88ef-53d5280d664f
ea09f144-bf42-47b7-89db-c39393c7453e	a29acdd2-e748-4989-88ef-53d5280d664f
393bf858-8373-4b9c-9fcb-79adef17b823	a29acdd2-e748-4989-88ef-53d5280d664f
a2f206e1-5b4a-4c75-814b-5a2616306003	a29acdd2-e748-4989-88ef-53d5280d664f
14dd04c3-fda2-42ac-b7da-e46bc97f9f0e	a29acdd2-e748-4989-88ef-53d5280d664f
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	a29acdd2-e748-4989-88ef-53d5280d664f
f7a56634-10ca-4560-b372-31a11c6761f2	a29acdd2-e748-4989-88ef-53d5280d664f
fbd5a8cb-09f4-4bfd-98c0-bf579c016b45	a29acdd2-e748-4989-88ef-53d5280d664f
dbc4c807-4f3a-44de-88be-3216cd078b29	a29acdd2-e748-4989-88ef-53d5280d664f
7a199e98-ee84-4309-8d72-35ff7130ac47	a29acdd2-e748-4989-88ef-53d5280d664f
813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63	a29acdd2-e748-4989-88ef-53d5280d664f
52415e78-95a5-43d1-b455-b7598b42aeb9	a29acdd2-e748-4989-88ef-53d5280d664f
7fdf56e4-5687-465b-8c93-d520e40dba62	a29acdd2-e748-4989-88ef-53d5280d664f
6a93f815-2bec-47d2-a159-ac376174559c	a29acdd2-e748-4989-88ef-53d5280d664f
3de82401-b5f7-4fd3-8938-b3812c3a6218	a29acdd2-e748-4989-88ef-53d5280d664f
63fd494e-7fe3-4488-8c10-347ec413fdfd	a29acdd2-e748-4989-88ef-53d5280d664f
a17bc8e8-f215-4e18-b96a-61070db32d7b	a29acdd2-e748-4989-88ef-53d5280d664f
16835618-616f-47d6-a0f2-8592424270ba	a29acdd2-e748-4989-88ef-53d5280d664f
1ba00269-7f7b-4082-a530-32ac9ef79d61	a29acdd2-e748-4989-88ef-53d5280d664f
d11e8639-90ac-49fc-9304-62a91b0c264d	a29acdd2-e748-4989-88ef-53d5280d664f
c8d09ce1-456f-4dc8-b092-b717f0b4b5ab	a29acdd2-e748-4989-88ef-53d5280d664f
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	a29acdd2-e748-4989-88ef-53d5280d664f
0bbc72e4-44a0-442a-aa74-b6a46ba27d1d	a29acdd2-e748-4989-88ef-53d5280d664f
b4aff203-ccf3-476b-af94-b6970ff46130	a29acdd2-e748-4989-88ef-53d5280d664f
86e01732-079f-4793-9f5b-72f69da8590b	a29acdd2-e748-4989-88ef-53d5280d664f
48348210-c240-4dd0-b377-bd6929f7bbaf	a29acdd2-e748-4989-88ef-53d5280d664f
ba953395-648d-4e90-89de-e1258b1e1d99	a29acdd2-e748-4989-88ef-53d5280d664f
982ed45e-4e07-44a4-b8f5-cc3d2c56f433	a29acdd2-e748-4989-88ef-53d5280d664f
b0b56afc-1579-48c2-9ffc-720440b1f601	a29acdd2-e748-4989-88ef-53d5280d664f
acfc0756-2a83-4b46-a4e4-0adbe441cd38	a29acdd2-e748-4989-88ef-53d5280d664f
c3afe823-fc30-478a-bfb7-ab60739aeca6	a29acdd2-e748-4989-88ef-53d5280d664f
f35462c3-94e6-480f-9aad-de440723e210	a29acdd2-e748-4989-88ef-53d5280d664f
cb9f10e6-8121-4e91-a30f-f20c436a1f83	a29acdd2-e748-4989-88ef-53d5280d664f
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	a29acdd2-e748-4989-88ef-53d5280d664f
7d412b4f-83ba-4277-b188-cec153c32b2e	a29acdd2-e748-4989-88ef-53d5280d664f
b375a7ce-dfdb-43f0-8180-eaafd900c40c	a29acdd2-e748-4989-88ef-53d5280d664f
b9894b0a-a062-4da7-b18b-8c827620c309	a29acdd2-e748-4989-88ef-53d5280d664f
8529432f-7acc-4f75-bc7e-aa7af2f068aa	a29acdd2-e748-4989-88ef-53d5280d664f
bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2	a29acdd2-e748-4989-88ef-53d5280d664f
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	a29acdd2-e748-4989-88ef-53d5280d664f
f98a8ddf-630d-4e5b-98db-fbe29d36a03a	a29acdd2-e748-4989-88ef-53d5280d664f
f2dd1707-c0f8-476c-b81e-ffaeeaec356a	a29acdd2-e748-4989-88ef-53d5280d664f
b9881ee0-8a9b-4039-afec-e6bca3665e76	a29acdd2-e748-4989-88ef-53d5280d664f
7eb6f8fb-17b1-4382-9566-35e4eec985cd	a29acdd2-e748-4989-88ef-53d5280d664f
ff01ca02-94de-448b-98f7-019723a203fa	a29acdd2-e748-4989-88ef-53d5280d664f
0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179	a29acdd2-e748-4989-88ef-53d5280d664f
275ab079-aeb6-487b-ad02-d4cef821fdd6	a29acdd2-e748-4989-88ef-53d5280d664f
ccc731f5-6628-4278-8faa-ff90ffb7abaa	a29acdd2-e748-4989-88ef-53d5280d664f
447dea2a-a078-47cf-ac2f-e03f8f6ef585	a29acdd2-e748-4989-88ef-53d5280d664f
e907d88c-7e7e-4b4e-9b33-6865f4a6b11a	a29acdd2-e748-4989-88ef-53d5280d664f
9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb	a29acdd2-e748-4989-88ef-53d5280d664f
7959cb7a-91c9-4a22-96e5-6f171555260d	a29acdd2-e748-4989-88ef-53d5280d664f
1c5c0771-bd22-4f7f-9eeb-19176f5bf1a8	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8607b79d-53fb-4562-b53c-7f0ea844c722	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
96ee2d9a-17ae-4bef-9196-c3b460b2a2f7	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
932746ea-68f2-4111-94c0-65be660c5d29	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7042f286-956a-4dbc-b696-2c77581d86bb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
83a46c2b-d09b-49ae-9ddb-f961032af8fb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b20de290-866f-45f1-a33c-122a5bf1b524	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6605c8ae-02af-40fb-ac1e-4653f7cb5ff7	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
2a2c79fb-38bc-4909-adfb-fd1799fa02a3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d0188960-83a2-44d9-87e6-ff241857c393	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8f04d44e-bbcb-4743-926d-f795b8e65de8	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
639bd728-3a24-4225-928b-f8930732c70c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
24b5087c-57d1-4dec-af85-b4418ab71ea3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6e6aa730-bf29-4071-8e6b-096933f3e261	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
830b2887-c9f7-4f20-bfa4-c95261ef3d30	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f4d71eaa-36e9-4f68-b4e3-d70d0d2f7e34	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a3c9efc0-e66e-473d-be69-7f3cc120041e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d7600272-a9ed-4730-9653-81258ff9996a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5f76e419-73a6-4b89-ab4a-4abb8632e33c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4b34957c-86c5-4f7d-b169-fe0f36a8ab16	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
24942230-212b-4b13-9931-4b5db634a7ab	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
49f9677e-47f9-46ee-91c3-45d0734f0e9a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
51454aa6-be41-4445-972f-d40bb4a6ec61	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
86442a1f-c323-44b7-b773-2c1d42db7217	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
12c8dc7b-ca42-40fb-9cb3-38bb96b64674	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
3e1a3a50-a7c4-45f9-ac13-cc82c9f7d405	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b868a581-fba5-4895-959d-80aaedc49f55	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
cab2520d-32c3-4cb4-af28-edf94fe64920	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e39ed88a-fe46-4a3a-bca6-5840e52d2856	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9cd88c81-9bad-41e2-9cf5-b7faba2e1d76	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
62fc499f-422d-48e2-9200-cd15cc409203	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
aaf4c939-3cf2-4d4e-8f8e-a2e51ce9940b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
c399da7d-1c72-4e7c-959c-1dce9684916c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f00c449c-be6f-4c2a-bf0a-0fc27caa6d06	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4350b070-3eea-4cb8-b3d0-7d3c753e33f3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
bd8c5cf1-bf00-4e0b-b230-5fd93cdf0125	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
37ccc457-85b1-4192-bad0-83bba00950b2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4d913333-8c13-4056-8593-32259ee3b787	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
58874d83-90b2-4a46-b4fd-6d16cfc92b38	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
52415e78-95a5-43d1-b455-b7598b42aeb9	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0283fc09-7bb4-4233-ae2b-d08f0f1c4f0f	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
2e2a4648-f599-4f70-ac3a-7453b3b1055d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0dab5ff3-04a2-43a7-9312-c296c4d45675	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f470bb89-8dc9-4279-8b81-f3c96da8933a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7fdf56e4-5687-465b-8c93-d520e40dba62	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9826691b-794a-4aec-ad2f-aca0d1066873	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
210eb72b-b6db-4f86-9969-12e56da66cbe	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5615a6cc-12af-4479-909d-6afd5d82d711	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
1ba00269-7f7b-4082-a530-32ac9ef79d61	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
16835618-616f-47d6-a0f2-8592424270ba	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8ee93852-790f-4183-9da1-8eab09b3c29a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0bbc72e4-44a0-442a-aa74-b6a46ba27d1d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ba953395-648d-4e90-89de-e1258b1e1d99	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
eda9ddd3-5d8e-431f-9a6d-b5eadb14405e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b0b56afc-1579-48c2-9ffc-720440b1f601	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
538bdb7a-742b-44db-8b32-a5d9fbb434b9	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
636cd6e3-0937-4b87-9bf6-0f6946c11f57	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0e83a641-3da7-4012-8ce4-e6aa3dbabd7d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
cb900cb7-6a98-45c8-9566-9da26559aedc	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b375a7ce-dfdb-43f0-8180-eaafd900c40c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d808320f-39c1-4193-88ab-cdb7a82af8b8	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
bc3dc4e5-8e58-430e-b5f5-7bbde0e27fe2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
2383aca2-bafb-40df-a4ed-a73c11cd33a5	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f98a8ddf-630d-4e5b-98db-fbe29d36a03a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
65a29a73-9ff3-4423-9583-38df67506e97	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
275ab079-aeb6-487b-ad02-d4cef821fdd6	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
447dea2a-a078-47cf-ac2f-e03f8f6ef585	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0fcdd438-ca5f-4e47-a8ba-dc5a479535e7	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ed24b8d5-65b7-4e91-9438-6c663d160a8a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
206d134c-a21c-47d6-9634-dea5832cc911	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8d38ebb7-2e06-49e8-83cc-ff0831ec5fe4	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a2f08de8-cbf6-4711-b932-6d4adcf5200d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9a4a7903-42c9-4af9-9aff-4ea86d0e8cfb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b1d83932-0ea9-42dc-8578-8e6063f54ff3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
64de3d9d-e116-438b-ae58-8de3e9e42384	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8db4eedb-0ade-4248-a1dd-e5f235d9ecaf	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
11eec72e-8f59-4c5e-9095-817a6fad0b0b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
fe4ff88e-5d57-421c-b406-714655fdbd1d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f5256aab-117a-4ad3-b276-ddd27fc079bc	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6cdbe9b1-2bd3-4069-8379-01a4d3ff1fe0	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
702a1381-914b-462a-b19b-275bd4db7ff2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4917596f-f29d-47e0-9cc5-56f326951b75	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9a32db3b-e5c0-400b-8f7e-33dec4920219	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d0cf588c-060c-413b-83f2-99309eec50bb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b3ac4a14-cd60-4705-bec3-648cfbc5635d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5f721066-1413-4483-8fdc-b3227aa5ae71	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0ede0e6e-4cac-4f34-9d6b-092a2e6c7eb6	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
dde473d8-ca2c-44e1-8009-4a8eace8e57a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5cb685af-e5d9-429d-8f8f-c4a92b0b14ec	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8abc0aa6-5b30-4d94-9f0a-bdf8600c9285	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6d470647-2a50-45c7-ab5f-d41f4ff2e8fb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e4583cb5-5770-43a9-95e9-b39981b947cf	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e0790f61-dc64-4ad7-92f5-07374ea3043d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
785e830b-5455-4ed8-a420-3165752f5b7c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
22ae069e-4893-42bc-b4c3-9d4fb2a85792	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
09d23fad-d2da-4319-9408-5d9948971a18	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ea09f144-bf42-47b7-89db-c39393c7453e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a2f206e1-5b4a-4c75-814b-5a2616306003	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f7a56634-10ca-4560-b372-31a11c6761f2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
009e9aa5-e6bc-4a03-9052-be5866fede7b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
34851926-ba58-427f-aed2-408074f74bcc	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
fbd5a8cb-09f4-4bfd-98c0-bf579c016b45	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
dbc4c807-4f3a-44de-88be-3216cd078b29	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4d003da0-e5b9-46a8-9630-723d7d0ff2a1	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
835503d8-7873-4139-bbf5-9bd46a4d7555	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
813f7e0b-c9ae-4eb5-9e1d-ef6b0fe2be63	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5c3b1f91-c37f-45f5-9a12-ee6dfdfd2879	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0ec9af08-b459-4e79-b49d-b3bd93b5183d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0faad761-4f4d-4e53-936c-eff0f8f19d56	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ebeaafd2-41a5-4289-926c-3dd61928d266	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7df2f5b2-eb93-4907-8f52-8c183ebfdf4e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
3de82401-b5f7-4fd3-8938-b3812c3a6218	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e081184b-1f03-4109-b27e-edfaa15180ee	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7bd41e59-50b9-4287-a3eb-7d295155ed98	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
de59e869-4a8c-425e-b65b-986675c547ac	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
782efc3c-27fd-4bbc-a4db-61f330521895	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
43bebee7-3f29-41f9-b422-780ca73aaaf3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
48348210-c240-4dd0-b377-bd6929f7bbaf	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
acfc0756-2a83-4b46-a4e4-0adbe441cd38	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7d412b4f-83ba-4277-b188-cec153c32b2e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
28580873-d8aa-49ad-808b-a4ded351b415	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8529432f-7acc-4f75-bc7e-aa7af2f068aa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e7ace2bf-9dcc-4f39-97bf-289f3a7638e1	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d0432919-9773-4b20-bb8f-e65cf4d6f373	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
1c4a3eaa-6ad6-4ffe-91ac-b127201e0493	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f2dd1707-c0f8-476c-b81e-ffaeeaec356a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b9881ee0-8a9b-4039-afec-e6bca3665e76	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7eb6f8fb-17b1-4382-9566-35e4eec985cd	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0b7bfb33-e3d8-4c22-9ab1-13c7df7cd179	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ccc731f5-6628-4278-8faa-ff90ffb7abaa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a1231bfc-991a-427d-b578-9e361f16d571	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e7ace2bf-9dcc-4f39-97bf-289f3a7638e1	a29acdd2-e748-4989-88ef-53d5280d664f
0007acec-c38e-43c3-9d1c-84b22cf45223	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
1c76efdb-7597-4ab3-a6f0-7a94b64760e1	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8bd6fead-d21a-4947-9e77-384dc9b2db45	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
cb9f10e6-8121-4e91-a30f-f20c436a1f83	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8bbc7b0b-4d57-4f61-9e24-bcabd986bc2a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
dd927140-987b-45f9-8df3-2cc5b6510e9d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
26504250-43fd-4151-a3ab-698514b4422f	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
982ed45e-4e07-44a4-b8f5-cc3d2c56f433	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d751a181-a69c-4168-83c1-67a08cf77315	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d88f0387-7041-4251-b2a4-3505c71e0145	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ff01ca02-94de-448b-98f7-019723a203fa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e907d88c-7e7e-4b4e-9b33-6865f4a6b11a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7959cb7a-91c9-4a22-96e5-6f171555260d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8830549f-2a56-449b-972a-99f330ff6799	a29acdd2-e748-4989-88ef-53d5280d664f
b716fd24-bc6a-4cd8-a59c-f62ac0e2adb6	a29acdd2-e748-4989-88ef-53d5280d664f
34541214-0d98-4fcd-b432-1d812544dc93	a29acdd2-e748-4989-88ef-53d5280d664f
ae655968-7c21-4d81-be06-2a0df0ed6b28	a29acdd2-e748-4989-88ef-53d5280d664f
d08e6560-faac-4198-9c59-af90218cac26	a29acdd2-e748-4989-88ef-53d5280d664f
7595af17-584d-4656-84eb-8c486e615576	a29acdd2-e748-4989-88ef-53d5280d664f
d91bc883-9d88-4027-a6c9-6c696c15c4aa	a29acdd2-e748-4989-88ef-53d5280d664f
e0b50865-fa93-46b9-a03a-ec30c0f686a2	a29acdd2-e748-4989-88ef-53d5280d664f
d08e6560-faac-4198-9c59-af90218cac26	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7595af17-584d-4656-84eb-8c486e615576	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d91bc883-9d88-4027-a6c9-6c696c15c4aa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
e0b50865-fa93-46b9-a03a-ec30c0f686a2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9542b213-74ae-4de2-bf9b-5fcc546cfcb9	a29acdd2-e748-4989-88ef-53d5280d664f
7b489fe6-48b2-4a10-ac59-806d7b32b2f9	a29acdd2-e748-4989-88ef-53d5280d664f
b458b85f-6f29-4158-bad3-d9b89a337da4	a29acdd2-e748-4989-88ef-53d5280d664f
86de09e2-9d5b-4cfe-92fa-34810c975fa2	a29acdd2-e748-4989-88ef-53d5280d664f
8634c4ab-4c4d-4d93-92eb-06ad76d6e4dd	a29acdd2-e748-4989-88ef-53d5280d664f
acab7624-6acc-4a09-ba9f-54781922f9ce	a29acdd2-e748-4989-88ef-53d5280d664f
bad56af4-15da-4f42-8f15-9b0464e0d333	a29acdd2-e748-4989-88ef-53d5280d664f
d2bfc926-63eb-498c-b59e-43763d4cef7b	a29acdd2-e748-4989-88ef-53d5280d664f
5203668a-5842-4186-a1eb-753ac32c207b	a29acdd2-e748-4989-88ef-53d5280d664f
5d2f2e15-0f4a-456c-9260-e0abd9390c5c	a29acdd2-e748-4989-88ef-53d5280d664f
6538235a-0c96-4490-99ee-6c02bd461efa	a29acdd2-e748-4989-88ef-53d5280d664f
be6e29d9-8353-46c7-8f6e-6f063101fe11	a29acdd2-e748-4989-88ef-53d5280d664f
9546ca06-fcc7-4f7d-b9fa-1710433b9760	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4629d58e-7d46-4578-827d-e11a3310e33b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
851cd81c-4648-4785-8035-f328276b74ca	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
069a8fbd-3c49-41cf-b722-5a0f6006df54	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9546ca06-fcc7-4f7d-b9fa-1710433b9760	a29acdd2-e748-4989-88ef-53d5280d664f
4629d58e-7d46-4578-827d-e11a3310e33b	a29acdd2-e748-4989-88ef-53d5280d664f
851cd81c-4648-4785-8035-f328276b74ca	a29acdd2-e748-4989-88ef-53d5280d664f
069a8fbd-3c49-41cf-b722-5a0f6006df54	a29acdd2-e748-4989-88ef-53d5280d664f
533a090b-5705-43fc-86bf-a24537cddb53	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
4b9b80ad-1491-49d0-b624-e5e26aedf7e3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5331e26f-246f-46fa-b2a7-48df197d6fa9	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
253ed92b-51e7-4dc8-ab10-f9dd6d334209	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8bd6fead-d21a-4947-9e77-384dc9b2db45	a29acdd2-e748-4989-88ef-53d5280d664f
d751a181-a69c-4168-83c1-67a08cf77315	a29acdd2-e748-4989-88ef-53d5280d664f
d88f0387-7041-4251-b2a4-3505c71e0145	a29acdd2-e748-4989-88ef-53d5280d664f
fae35cea-412d-4e9a-811a-9496a6fbd663	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
97877fcd-5162-4cb8-a810-ffb9e273b3db	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5cfa28ac-41cf-4072-840b-f1437ae4087e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
18b5f174-70fb-41c9-98c2-e92829150139	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8c383dbf-7ba0-42d2-a048-430a04c866e7	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
93eda126-7711-4029-be8f-82e04d9f41f7	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b2622786-8c32-4971-bb0a-0a56b72df3ec	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
77becf3c-686e-4378-a750-0cc9365facc3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
2b7ffa8c-5e12-4627-9465-93d2ccb7d187	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
1f1ba0dc-9c41-4e33-a891-8ed99eab961d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6a93f815-2bec-47d2-a159-ac376174559c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
c3afe823-fc30-478a-bfb7-ab60739aeca6	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
210eb72b-b6db-4f86-9969-12e56da66cbe	a29acdd2-e748-4989-88ef-53d5280d664f
8fc8908f-b782-41c8-98fc-b46746f7bfba	a29acdd2-e748-4989-88ef-53d5280d664f
9826691b-794a-4aec-ad2f-aca0d1066873	a29acdd2-e748-4989-88ef-53d5280d664f
a238a18e-512b-4aa5-bd8a-b26213de6739	a29acdd2-e748-4989-88ef-53d5280d664f
24b5087c-57d1-4dec-af85-b4418ab71ea3	a29acdd2-e748-4989-88ef-53d5280d664f
37ccc457-85b1-4192-bad0-83bba00950b2	a29acdd2-e748-4989-88ef-53d5280d664f
2383aca2-bafb-40df-a4ed-a73c11cd33a5	a29acdd2-e748-4989-88ef-53d5280d664f
65a29a73-9ff3-4423-9583-38df67506e97	a29acdd2-e748-4989-88ef-53d5280d664f
118ba66e-bb47-4de0-b0cc-34170d92e915	a29acdd2-e748-4989-88ef-53d5280d664f
a1e98df4-f516-45b7-9515-da380ee8bb42	a29acdd2-e748-4989-88ef-53d5280d664f
08fd3bb1-bcb0-4458-bdab-bf9904fd9ecf	a29acdd2-e748-4989-88ef-53d5280d664f
5975d1f2-c365-4a2c-ac7f-c55dd7a5f9e1	a29acdd2-e748-4989-88ef-53d5280d664f
1649b8bb-aafc-49cc-97b5-8fccadad8703	a29acdd2-e748-4989-88ef-53d5280d664f
072f8500-842b-4bce-be47-eaf278261675	a29acdd2-e748-4989-88ef-53d5280d664f
85a36c92-cc5c-447b-848a-3ee52b7fc419	a29acdd2-e748-4989-88ef-53d5280d664f
6cf3311a-c0e7-445c-9728-9138d3e573b4	a29acdd2-e748-4989-88ef-53d5280d664f
08cfea6b-acef-4f81-ad01-f9025cbbbd03	a29acdd2-e748-4989-88ef-53d5280d664f
ea22c6d6-fc3b-4a40-bc89-343d312ee339	a29acdd2-e748-4989-88ef-53d5280d664f
522c6384-9e71-4e1e-b303-2a3e2e67ea10	a29acdd2-e748-4989-88ef-53d5280d664f
69cb5066-a268-4dca-a216-37a1767908bc	a29acdd2-e748-4989-88ef-53d5280d664f
97877fcd-5162-4cb8-a810-ffb9e273b3db	a29acdd2-e748-4989-88ef-53d5280d664f
93eda126-7711-4029-be8f-82e04d9f41f7	a29acdd2-e748-4989-88ef-53d5280d664f
9a35e10d-42af-48b3-9a10-cad37f018dab	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
84f00d8e-2576-497f-8401-5dd68506f502	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
44fd3a81-1dcb-4070-9dee-57437b90ff80	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5efbba82-03b2-40f9-a909-2423099cfd65	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
96d9118e-2b2f-4bc1-8813-47bf99ef578a	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8fc8908f-b782-41c8-98fc-b46746f7bfba	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
c098d34e-a341-4d3b-b4dd-eb3551b96ebd	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6819ef1e-0478-4a68-b0b9-0bab0723819f	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
7117f962-24c7-463d-8255-cf2ccb881dc8	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b78c5bd2-c526-430b-8ed4-4fedf2858cc5	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a238a18e-512b-4aa5-bd8a-b26213de6739	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9b94cb3a-52f5-4167-9db0-805bf8003cf1	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9cd88c81-9bad-41e2-9cf5-b7faba2e1d76	a29acdd2-e748-4989-88ef-53d5280d664f
6cdbe9b1-2bd3-4069-8379-01a4d3ff1fe0	a29acdd2-e748-4989-88ef-53d5280d664f
5c3b1f91-c37f-45f5-9a12-ee6dfdfd2879	a29acdd2-e748-4989-88ef-53d5280d664f
2ce28b99-a3d9-41a1-834b-ad09c808b12d	a29acdd2-e748-4989-88ef-53d5280d664f
d5176ee5-ace3-4939-9c92-f6e28f4a1154	a29acdd2-e748-4989-88ef-53d5280d664f
9a380bfb-edab-405b-add9-4e7cec35ef73	a29acdd2-e748-4989-88ef-53d5280d664f
d7575538-d923-4a71-95ab-a73d5ba019e5	a29acdd2-e748-4989-88ef-53d5280d664f
8830549f-2a56-449b-972a-99f330ff6799	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
1649b8bb-aafc-49cc-97b5-8fccadad8703	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b716fd24-bc6a-4cd8-a59c-f62ac0e2adb6	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
08cfea6b-acef-4f81-ad01-f9025cbbbd03	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
34541214-0d98-4fcd-b432-1d812544dc93	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ae655968-7c21-4d81-be06-2a0df0ed6b28	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
ea22c6d6-fc3b-4a40-bc89-343d312ee339	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
69cb5066-a268-4dca-a216-37a1767908bc	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f77a49ae-cc2a-44a9-8f4b-01508b95b2e2	a29acdd2-e748-4989-88ef-53d5280d664f
612bd607-87b6-4f7e-ad81-eafbb45ad5f5	a29acdd2-e748-4989-88ef-53d5280d664f
be1746e1-2e16-4bbb-95b5-dedeeee7d0a4	a29acdd2-e748-4989-88ef-53d5280d664f
0ac01b61-8af5-4f77-9d2d-4591321157e3	a29acdd2-e748-4989-88ef-53d5280d664f
7b489fe6-48b2-4a10-ac59-806d7b32b2f9	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b458b85f-6f29-4158-bad3-d9b89a337da4	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
8634c4ab-4c4d-4d93-92eb-06ad76d6e4dd	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
acab7624-6acc-4a09-ba9f-54781922f9ce	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
39713fcb-1774-430b-972c-c712969b4aaa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
86e01732-079f-4793-9f5b-72f69da8590b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b9894b0a-a062-4da7-b18b-8c827620c309	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
612bd607-87b6-4f7e-ad81-eafbb45ad5f5	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0f995a1e-25dd-4359-8a0d-ffba517654db	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b82a2ace-49e8-43d3-b163-29df0c81b296	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f10febe0-07fa-43d1-8f03-4662c55f9e2c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
be1746e1-2e16-4bbb-95b5-dedeeee7d0a4	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5203668a-5842-4186-a1eb-753ac32c207b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5d2f2e15-0f4a-456c-9260-e0abd9390c5c	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
0ac01b61-8af5-4f77-9d2d-4591321157e3	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9f29d26f-fe3e-42c5-a5c9-2a74eb436dbb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
5975d1f2-c365-4a2c-ac7f-c55dd7a5f9e1	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9542b213-74ae-4de2-bf9b-5fcc546cfcb9	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d3050429-e99e-46d1-9ebd-400e222d5134	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
86de09e2-9d5b-4cfe-92fa-34810c975fa2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
14dd04c3-fda2-42ac-b7da-e46bc97f9f0e	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
118ba66e-bb47-4de0-b0cc-34170d92e915	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
9a380bfb-edab-405b-add9-4e7cec35ef73	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
bad56af4-15da-4f42-8f15-9b0464e0d333	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a17bc8e8-f215-4e18-b96a-61070db32d7b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
a1e98df4-f516-45b7-9515-da380ee8bb42	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f77a49ae-cc2a-44a9-8f4b-01508b95b2e2	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
57b22cca-04fc-447f-ad5d-0d1eff401b5f	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
08fd3bb1-bcb0-4458-bdab-bf9904fd9ecf	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d2bfc926-63eb-498c-b59e-43763d4cef7b	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
d11e8639-90ac-49fc-9304-62a91b0c264d	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6538235a-0c96-4490-99ee-6c02bd461efa	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
be6e29d9-8353-46c7-8f6e-6f063101fe11	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
701819ca-dc87-4932-9ef4-eb74900b3962	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
393bf858-8373-4b9c-9fcb-79adef17b823	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f35462c3-94e6-480f-9aad-de440723e210	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
f0358778-456e-49eb-9c46-5694a41f0186	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
54ed816e-0a55-4540-bfbf-ec16ec884957	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
b4aff203-ccf3-476b-af94-b6970ff46130	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
c8d09ce1-456f-4dc8-b092-b717f0b4b5ab	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
70b86c9f-030e-42c6-8fc4-647ad2b1dfeb	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
522c6384-9e71-4e1e-b303-2a3e2e67ea10	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
072f8500-842b-4bce-be47-eaf278261675	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
85a36c92-cc5c-447b-848a-3ee52b7fc419	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
6cf3311a-c0e7-445c-9728-9138d3e573b4	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
18fd272b-c4b7-4d22-b870-c81768c0bffc	35525fd7-3ec7-41c0-9ad4-af6fa1c7243c
\.


--
-- Data for Name: user_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_attribute (name, value, user_id, id) FROM stdin;
\.


--
-- Data for Name: user_consent; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_consent (id, client_id, user_id, created_date, last_updated_date, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: user_consent_client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_consent_client_scope (user_consent_id, scope_id) FROM stdin;
\.


--
-- Data for Name: user_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_entity (id, email, email_constraint, email_verified, enabled, federation_link, first_name, last_name, realm_id, username, created_timestamp, service_account_client_link, not_before) FROM stdin;
ddf2637a-e7d1-4396-93c2-514135e73261	\N	8004afb0-a72b-4959-8db9-a82cb713d371	f	t	\N	\N	\N	master	admin	1565685875145	\N	0
78181ea0-a785-4fd2-8273-e66901be11a1	service-account-francoralite@placeholder.org	service-account-francoralite@placeholder.org	f	t	\N	\N	\N	francoralite	service-account-francoralite	1567415962237	6ca8b749-cba1-4453-8a20-0c189d9b9447	0
0914bbc4-0b4f-4768-93a3-a69d14d13114	contributeur@francoralite.org	contributeur@francoralite.org	t	t	\N	Contributeur	Francoralite	francoralite	contributeur	1622987852505	\N	0
fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955	utilisateur@francoralite.org	utilisateur@francoralite.org	t	t	\N	Utilisateur	Francoralite	francoralite	utilisateur	1622987922129	\N	0
25d39c71-cebd-4828-b750-3b8daad7778e	administrateur@francoralite.org	administrateur@francoralite.org	t	t	\N	Administrateur	Francoralite	francoralite	administrateur	1622987776553	\N	1634914374
\.


--
-- Data for Name: user_federation_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_config (user_federation_provider_id, value, name) FROM stdin;
\.


--
-- Data for Name: user_federation_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_mapper (id, name, federation_provider_id, federation_mapper_type, realm_id) FROM stdin;
\.


--
-- Data for Name: user_federation_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_mapper_config (user_federation_mapper_id, value, name) FROM stdin;
\.


--
-- Data for Name: user_federation_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_provider (id, changed_sync_period, display_name, full_sync_period, last_sync, priority, provider_name, realm_id) FROM stdin;
\.


--
-- Data for Name: user_group_membership; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_group_membership (group_id, user_id) FROM stdin;
8baef50e-741a-41d8-bbff-0e5cc18b7211	0914bbc4-0b4f-4768-93a3-a69d14d13114
8d6d3d77-1c07-48fc-b5fa-83b2a6b4dee2	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
81f3b075-bc53-42ec-870a-67153ce10b51	25d39c71-cebd-4828-b750-3b8daad7778e
\.


--
-- Data for Name: user_required_action; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_required_action (user_id, required_action) FROM stdin;
\.


--
-- Data for Name: user_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_role_mapping (role_id, user_id) FROM stdin;
8f8f910c-2f7c-4bec-b66f-d7058b53e4c5	ddf2637a-e7d1-4396-93c2-514135e73261
59163355-f8e4-43f5-9064-c34167799f8f	ddf2637a-e7d1-4396-93c2-514135e73261
b9c894e7-60c9-47ff-bbb4-db20b880c2d9	ddf2637a-e7d1-4396-93c2-514135e73261
d5447076-ea4f-4493-b0f9-dbea011ad108	ddf2637a-e7d1-4396-93c2-514135e73261
398b3395-34b8-4668-9296-05ba7eb64bbb	ddf2637a-e7d1-4396-93c2-514135e73261
5531c621-ad97-4da9-8896-bed73d09c285	78181ea0-a785-4fd2-8273-e66901be11a1
b684e64f-9250-42e0-a055-2a18ffa4df88	78181ea0-a785-4fd2-8273-e66901be11a1
818c584b-976b-40ee-a442-403c98bb668c	78181ea0-a785-4fd2-8273-e66901be11a1
850b0803-fc35-445d-a23e-d6479241bb60	78181ea0-a785-4fd2-8273-e66901be11a1
3d8b9944-d052-4e94-aba8-36358a0b5638	78181ea0-a785-4fd2-8273-e66901be11a1
5531c621-ad97-4da9-8896-bed73d09c285	25d39c71-cebd-4828-b750-3b8daad7778e
b684e64f-9250-42e0-a055-2a18ffa4df88	25d39c71-cebd-4828-b750-3b8daad7778e
818c584b-976b-40ee-a442-403c98bb668c	25d39c71-cebd-4828-b750-3b8daad7778e
850b0803-fc35-445d-a23e-d6479241bb60	25d39c71-cebd-4828-b750-3b8daad7778e
5531c621-ad97-4da9-8896-bed73d09c285	0914bbc4-0b4f-4768-93a3-a69d14d13114
b684e64f-9250-42e0-a055-2a18ffa4df88	0914bbc4-0b4f-4768-93a3-a69d14d13114
818c584b-976b-40ee-a442-403c98bb668c	0914bbc4-0b4f-4768-93a3-a69d14d13114
850b0803-fc35-445d-a23e-d6479241bb60	0914bbc4-0b4f-4768-93a3-a69d14d13114
5531c621-ad97-4da9-8896-bed73d09c285	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
b684e64f-9250-42e0-a055-2a18ffa4df88	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
818c584b-976b-40ee-a442-403c98bb668c	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
850b0803-fc35-445d-a23e-d6479241bb60	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
7f2da254-71c1-452b-b1e7-ab89ef429d94	fae07fa4-0bf4-4d14-a5b0-ef2e7a68d955
afb187be-f83f-4122-a9d9-d609d1b85251	0914bbc4-0b4f-4768-93a3-a69d14d13114
\.


--
-- Data for Name: user_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_session (id, auth_method, ip_address, last_session_refresh, login_username, realm_id, remember_me, started, user_id, user_session_state, broker_session_id, broker_user_id) FROM stdin;
\.


--
-- Data for Name: user_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_session_note (user_session, name, value) FROM stdin;
\.


--
-- Data for Name: username_login_failure; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.username_login_failure (realm_id, username, failed_login_not_before, last_failure, last_ip_failure, num_failures) FROM stdin;
\.


--
-- Data for Name: web_origins; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.web_origins (client_id, value) FROM stdin;
6ca8b749-cba1-4453-8a20-0c189d9b9447	nginx.francoralite.localhost:8080
6ca8b749-cba1-4453-8a20-0c189d9b9447	http://francoralite-api
6ca8b749-cba1-4453-8a20-0c189d9b9447	*
5def7547-cfd3-4473-946c-35f796c52df4	+
96e0973a-a61d-46a8-b1eb-ecd9e3953c25	+
\.


--
-- Name: username_login_failure CONSTRAINT_17-2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.username_login_failure
    ADD CONSTRAINT "CONSTRAINT_17-2" PRIMARY KEY (realm_id, username);


--
-- Name: keycloak_role UK_J3RWUVD56ONTGSUHOGM184WW2-2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT "UK_J3RWUVD56ONTGSUHOGM184WW2-2" UNIQUE (name, client_realm_constraint);


--
-- Name: client_auth_flow_bindings c_cli_flow_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_auth_flow_bindings
    ADD CONSTRAINT c_cli_flow_bind PRIMARY KEY (client_id, binding_name);


--
-- Name: client_scope_client c_cli_scope_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_client
    ADD CONSTRAINT c_cli_scope_bind PRIMARY KEY (client_id, scope_id);


--
-- Name: client_initial_access cnstr_client_init_acc_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_initial_access
    ADD CONSTRAINT cnstr_client_init_acc_pk PRIMARY KEY (id);


--
-- Name: realm_default_groups con_group_id_def_groups; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT con_group_id_def_groups UNIQUE (group_id);


--
-- Name: broker_link constr_broker_link_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.broker_link
    ADD CONSTRAINT constr_broker_link_pk PRIMARY KEY (identity_provider, user_id);


--
-- Name: client_user_session_note constr_cl_usr_ses_note; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_user_session_note
    ADD CONSTRAINT constr_cl_usr_ses_note PRIMARY KEY (client_session, name);


--
-- Name: component_config constr_component_config_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component_config
    ADD CONSTRAINT constr_component_config_pk PRIMARY KEY (id);


--
-- Name: component constr_component_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT constr_component_pk PRIMARY KEY (id);


--
-- Name: fed_user_required_action constr_fed_required_action; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_required_action
    ADD CONSTRAINT constr_fed_required_action PRIMARY KEY (required_action, user_id);


--
-- Name: fed_user_attribute constr_fed_user_attr_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_attribute
    ADD CONSTRAINT constr_fed_user_attr_pk PRIMARY KEY (id);


--
-- Name: fed_user_consent constr_fed_user_consent_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_consent
    ADD CONSTRAINT constr_fed_user_consent_pk PRIMARY KEY (id);


--
-- Name: fed_user_credential constr_fed_user_cred_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_credential
    ADD CONSTRAINT constr_fed_user_cred_pk PRIMARY KEY (id);


--
-- Name: fed_user_group_membership constr_fed_user_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_group_membership
    ADD CONSTRAINT constr_fed_user_group PRIMARY KEY (group_id, user_id);


--
-- Name: fed_user_role_mapping constr_fed_user_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_role_mapping
    ADD CONSTRAINT constr_fed_user_role PRIMARY KEY (role_id, user_id);


--
-- Name: federated_user constr_federated_user; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_user
    ADD CONSTRAINT constr_federated_user PRIMARY KEY (id);


--
-- Name: realm_default_groups constr_realm_default_groups; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT constr_realm_default_groups PRIMARY KEY (realm_id, group_id);


--
-- Name: realm_enabled_event_types constr_realm_enabl_event_types; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_enabled_event_types
    ADD CONSTRAINT constr_realm_enabl_event_types PRIMARY KEY (realm_id, value);


--
-- Name: realm_events_listeners constr_realm_events_listeners; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_events_listeners
    ADD CONSTRAINT constr_realm_events_listeners PRIMARY KEY (realm_id, value);


--
-- Name: realm_supported_locales constr_realm_supported_locales; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_supported_locales
    ADD CONSTRAINT constr_realm_supported_locales PRIMARY KEY (realm_id, value);


--
-- Name: identity_provider constraint_2b; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT constraint_2b PRIMARY KEY (internal_id);


--
-- Name: client_attributes constraint_3c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_attributes
    ADD CONSTRAINT constraint_3c PRIMARY KEY (client_id, name);


--
-- Name: event_entity constraint_4; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.event_entity
    ADD CONSTRAINT constraint_4 PRIMARY KEY (id);


--
-- Name: federated_identity constraint_40; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_identity
    ADD CONSTRAINT constraint_40 PRIMARY KEY (identity_provider, user_id);


--
-- Name: realm constraint_4a; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm
    ADD CONSTRAINT constraint_4a PRIMARY KEY (id);


--
-- Name: client_session_role constraint_5; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_role
    ADD CONSTRAINT constraint_5 PRIMARY KEY (client_session, role_id);


--
-- Name: user_session constraint_57; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session
    ADD CONSTRAINT constraint_57 PRIMARY KEY (id);


--
-- Name: user_federation_provider constraint_5c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_provider
    ADD CONSTRAINT constraint_5c PRIMARY KEY (id);


--
-- Name: client_session_note constraint_5e; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_note
    ADD CONSTRAINT constraint_5e PRIMARY KEY (client_session, name);


--
-- Name: client constraint_7; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT constraint_7 PRIMARY KEY (id);


--
-- Name: client_session constraint_8; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session
    ADD CONSTRAINT constraint_8 PRIMARY KEY (id);


--
-- Name: scope_mapping constraint_81; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_mapping
    ADD CONSTRAINT constraint_81 PRIMARY KEY (client_id, role_id);


--
-- Name: client_node_registrations constraint_84; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_node_registrations
    ADD CONSTRAINT constraint_84 PRIMARY KEY (client_id, name);


--
-- Name: realm_attribute constraint_9; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_attribute
    ADD CONSTRAINT constraint_9 PRIMARY KEY (name, realm_id);


--
-- Name: realm_required_credential constraint_92; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_required_credential
    ADD CONSTRAINT constraint_92 PRIMARY KEY (realm_id, type);


--
-- Name: keycloak_role constraint_a; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT constraint_a PRIMARY KEY (id);


--
-- Name: admin_event_entity constraint_admin_event_entity; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.admin_event_entity
    ADD CONSTRAINT constraint_admin_event_entity PRIMARY KEY (id);


--
-- Name: authenticator_config_entry constraint_auth_cfg_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config_entry
    ADD CONSTRAINT constraint_auth_cfg_pk PRIMARY KEY (authenticator_id, name);


--
-- Name: authentication_execution constraint_auth_exec_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT constraint_auth_exec_pk PRIMARY KEY (id);


--
-- Name: authentication_flow constraint_auth_flow_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_flow
    ADD CONSTRAINT constraint_auth_flow_pk PRIMARY KEY (id);


--
-- Name: authenticator_config constraint_auth_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config
    ADD CONSTRAINT constraint_auth_pk PRIMARY KEY (id);


--
-- Name: client_session_auth_status constraint_auth_status_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_auth_status
    ADD CONSTRAINT constraint_auth_status_pk PRIMARY KEY (client_session, authenticator);


--
-- Name: user_role_mapping constraint_c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_role_mapping
    ADD CONSTRAINT constraint_c PRIMARY KEY (role_id, user_id);


--
-- Name: composite_role constraint_composite_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT constraint_composite_role PRIMARY KEY (composite, child_role);


--
-- Name: client_session_prot_mapper constraint_cs_pmp_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_prot_mapper
    ADD CONSTRAINT constraint_cs_pmp_pk PRIMARY KEY (client_session, protocol_mapper_id);


--
-- Name: identity_provider_config constraint_d; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_config
    ADD CONSTRAINT constraint_d PRIMARY KEY (identity_provider_id, name);


--
-- Name: policy_config constraint_dpc; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.policy_config
    ADD CONSTRAINT constraint_dpc PRIMARY KEY (policy_id, name);


--
-- Name: realm_smtp_config constraint_e; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_smtp_config
    ADD CONSTRAINT constraint_e PRIMARY KEY (realm_id, name);


--
-- Name: credential constraint_f; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.credential
    ADD CONSTRAINT constraint_f PRIMARY KEY (id);


--
-- Name: user_federation_config constraint_f9; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_config
    ADD CONSTRAINT constraint_f9 PRIMARY KEY (user_federation_provider_id, name);


--
-- Name: resource_server_perm_ticket constraint_fapmt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT constraint_fapmt PRIMARY KEY (id);


--
-- Name: resource_server_resource constraint_farsr; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT constraint_farsr PRIMARY KEY (id);


--
-- Name: resource_server_policy constraint_farsrp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT constraint_farsrp PRIMARY KEY (id);


--
-- Name: associated_policy constraint_farsrpap; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT constraint_farsrpap PRIMARY KEY (policy_id, associated_policy_id);


--
-- Name: resource_policy constraint_farsrpp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT constraint_farsrpp PRIMARY KEY (resource_id, policy_id);


--
-- Name: resource_server_scope constraint_farsrs; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT constraint_farsrs PRIMARY KEY (id);


--
-- Name: resource_scope constraint_farsrsp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT constraint_farsrsp PRIMARY KEY (resource_id, scope_id);


--
-- Name: scope_policy constraint_farsrsps; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT constraint_farsrsps PRIMARY KEY (scope_id, policy_id);


--
-- Name: user_entity constraint_fb; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT constraint_fb PRIMARY KEY (id);


--
-- Name: user_federation_mapper_config constraint_fedmapper_cfg_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper_config
    ADD CONSTRAINT constraint_fedmapper_cfg_pm PRIMARY KEY (user_federation_mapper_id, name);


--
-- Name: user_federation_mapper constraint_fedmapperpm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT constraint_fedmapperpm PRIMARY KEY (id);


--
-- Name: fed_user_consent_cl_scope constraint_fgrntcsnt_clsc_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_consent_cl_scope
    ADD CONSTRAINT constraint_fgrntcsnt_clsc_pm PRIMARY KEY (user_consent_id, scope_id);


--
-- Name: user_consent_client_scope constraint_grntcsnt_clsc_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent_client_scope
    ADD CONSTRAINT constraint_grntcsnt_clsc_pm PRIMARY KEY (user_consent_id, scope_id);


--
-- Name: user_consent constraint_grntcsnt_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT constraint_grntcsnt_pm PRIMARY KEY (id);


--
-- Name: keycloak_group constraint_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_group
    ADD CONSTRAINT constraint_group PRIMARY KEY (id);


--
-- Name: group_attribute constraint_group_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_attribute
    ADD CONSTRAINT constraint_group_attribute_pk PRIMARY KEY (id);


--
-- Name: group_role_mapping constraint_group_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_role_mapping
    ADD CONSTRAINT constraint_group_role PRIMARY KEY (role_id, group_id);


--
-- Name: identity_provider_mapper constraint_idpm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_mapper
    ADD CONSTRAINT constraint_idpm PRIMARY KEY (id);


--
-- Name: idp_mapper_config constraint_idpmconfig; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.idp_mapper_config
    ADD CONSTRAINT constraint_idpmconfig PRIMARY KEY (idp_mapper_id, name);


--
-- Name: migration_model constraint_migmod; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.migration_model
    ADD CONSTRAINT constraint_migmod PRIMARY KEY (id);


--
-- Name: offline_client_session constraint_offl_cl_ses_pk3; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.offline_client_session
    ADD CONSTRAINT constraint_offl_cl_ses_pk3 PRIMARY KEY (user_session_id, client_id, client_storage_provider, external_client_id, offline_flag);


--
-- Name: offline_user_session constraint_offl_us_ses_pk2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.offline_user_session
    ADD CONSTRAINT constraint_offl_us_ses_pk2 PRIMARY KEY (user_session_id, offline_flag);


--
-- Name: protocol_mapper constraint_pcm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT constraint_pcm PRIMARY KEY (id);


--
-- Name: protocol_mapper_config constraint_pmconfig; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper_config
    ADD CONSTRAINT constraint_pmconfig PRIMARY KEY (protocol_mapper_id, name);


--
-- Name: redirect_uris constraint_redirect_uris; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.redirect_uris
    ADD CONSTRAINT constraint_redirect_uris PRIMARY KEY (client_id, value);


--
-- Name: required_action_config constraint_req_act_cfg_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_config
    ADD CONSTRAINT constraint_req_act_cfg_pk PRIMARY KEY (required_action_id, name);


--
-- Name: required_action_provider constraint_req_act_prv_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_provider
    ADD CONSTRAINT constraint_req_act_prv_pk PRIMARY KEY (id);


--
-- Name: user_required_action constraint_required_action; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_required_action
    ADD CONSTRAINT constraint_required_action PRIMARY KEY (required_action, user_id);


--
-- Name: resource_uris constraint_resour_uris_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_uris
    ADD CONSTRAINT constraint_resour_uris_pk PRIMARY KEY (resource_id, value);


--
-- Name: role_attribute constraint_role_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.role_attribute
    ADD CONSTRAINT constraint_role_attribute_pk PRIMARY KEY (id);


--
-- Name: user_attribute constraint_user_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_attribute
    ADD CONSTRAINT constraint_user_attribute_pk PRIMARY KEY (id);


--
-- Name: user_group_membership constraint_user_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_group_membership
    ADD CONSTRAINT constraint_user_group PRIMARY KEY (group_id, user_id);


--
-- Name: user_session_note constraint_usn_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session_note
    ADD CONSTRAINT constraint_usn_pk PRIMARY KEY (user_session, name);


--
-- Name: web_origins constraint_web_origins; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.web_origins
    ADD CONSTRAINT constraint_web_origins PRIMARY KEY (client_id, value);


--
-- Name: client_scope_attributes pk_cl_tmpl_attr; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_attributes
    ADD CONSTRAINT pk_cl_tmpl_attr PRIMARY KEY (scope_id, name);


--
-- Name: client_scope pk_cli_template; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope
    ADD CONSTRAINT pk_cli_template PRIMARY KEY (id);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: resource_server pk_resource_server; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server
    ADD CONSTRAINT pk_resource_server PRIMARY KEY (id);


--
-- Name: client_scope_role_mapping pk_template_scope; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_role_mapping
    ADD CONSTRAINT pk_template_scope PRIMARY KEY (scope_id, role_id);


--
-- Name: default_client_scope r_def_cli_scope_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.default_client_scope
    ADD CONSTRAINT r_def_cli_scope_bind PRIMARY KEY (realm_id, scope_id);


--
-- Name: realm_localizations realm_localizations_pkey; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_localizations
    ADD CONSTRAINT realm_localizations_pkey PRIMARY KEY (realm_id, locale);


--
-- Name: resource_attribute res_attr_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_attribute
    ADD CONSTRAINT res_attr_pk PRIMARY KEY (id);


--
-- Name: keycloak_group sibling_names; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_group
    ADD CONSTRAINT sibling_names UNIQUE (realm_id, parent_group, name);


--
-- Name: identity_provider uk_2daelwnibji49avxsrtuf6xj33; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT uk_2daelwnibji49avxsrtuf6xj33 UNIQUE (provider_alias, realm_id);


--
-- Name: client uk_b71cjlbenv945rb6gcon438at; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT uk_b71cjlbenv945rb6gcon438at UNIQUE (realm_id, client_id);


--
-- Name: client_scope uk_cli_scope; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope
    ADD CONSTRAINT uk_cli_scope UNIQUE (realm_id, name);


--
-- Name: user_entity uk_dykn684sl8up1crfei6eckhd7; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT uk_dykn684sl8up1crfei6eckhd7 UNIQUE (realm_id, email_constraint);


--
-- Name: resource_server_resource uk_frsr6t700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT uk_frsr6t700s9v50bu18ws5ha6 UNIQUE (name, owner, resource_server_id);


--
-- Name: resource_server_perm_ticket uk_frsr6t700s9v50bu18ws5pmt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT uk_frsr6t700s9v50bu18ws5pmt UNIQUE (owner, requester, resource_server_id, resource_id, scope_id);


--
-- Name: resource_server_policy uk_frsrpt700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT uk_frsrpt700s9v50bu18ws5ha6 UNIQUE (name, resource_server_id);


--
-- Name: resource_server_scope uk_frsrst700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT uk_frsrst700s9v50bu18ws5ha6 UNIQUE (name, resource_server_id);


--
-- Name: user_consent uk_jkuwuvd56ontgsuhogm8uewrt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT uk_jkuwuvd56ontgsuhogm8uewrt UNIQUE (client_id, client_storage_provider, external_client_id, user_id);


--
-- Name: realm uk_orvsdmla56612eaefiq6wl5oi; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm
    ADD CONSTRAINT uk_orvsdmla56612eaefiq6wl5oi UNIQUE (name);


--
-- Name: user_entity uk_ru8tt6t700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT uk_ru8tt6t700s9v50bu18ws5ha6 UNIQUE (realm_id, username);


--
-- Name: idx_assoc_pol_assoc_pol_id; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_assoc_pol_assoc_pol_id ON public.associated_policy USING btree (associated_policy_id);


--
-- Name: idx_auth_config_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_config_realm ON public.authenticator_config USING btree (realm_id);


--
-- Name: idx_auth_exec_flow; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_exec_flow ON public.authentication_execution USING btree (flow_id);


--
-- Name: idx_auth_exec_realm_flow; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_exec_realm_flow ON public.authentication_execution USING btree (realm_id, flow_id);


--
-- Name: idx_auth_flow_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_flow_realm ON public.authentication_flow USING btree (realm_id);


--
-- Name: idx_cl_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_cl_clscope ON public.client_scope_client USING btree (scope_id);


--
-- Name: idx_client_att_by_name_value; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_att_by_name_value ON public.client_attributes USING btree (name, value);


--
-- Name: idx_client_id; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_id ON public.client USING btree (client_id);


--
-- Name: idx_client_init_acc_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_init_acc_realm ON public.client_initial_access USING btree (realm_id);


--
-- Name: idx_client_session_session; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_session_session ON public.client_session USING btree (session_id);


--
-- Name: idx_clscope_attrs; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_attrs ON public.client_scope_attributes USING btree (scope_id);


--
-- Name: idx_clscope_cl; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_cl ON public.client_scope_client USING btree (client_id);


--
-- Name: idx_clscope_protmap; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_protmap ON public.protocol_mapper USING btree (client_scope_id);


--
-- Name: idx_clscope_role; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_role ON public.client_scope_role_mapping USING btree (scope_id);


--
-- Name: idx_compo_config_compo; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_compo_config_compo ON public.component_config USING btree (component_id);


--
-- Name: idx_component_provider_type; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_component_provider_type ON public.component USING btree (provider_type);


--
-- Name: idx_component_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_component_realm ON public.component USING btree (realm_id);


--
-- Name: idx_composite; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_composite ON public.composite_role USING btree (composite);


--
-- Name: idx_composite_child; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_composite_child ON public.composite_role USING btree (child_role);


--
-- Name: idx_defcls_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_defcls_realm ON public.default_client_scope USING btree (realm_id);


--
-- Name: idx_defcls_scope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_defcls_scope ON public.default_client_scope USING btree (scope_id);


--
-- Name: idx_event_time; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_event_time ON public.event_entity USING btree (realm_id, event_time);


--
-- Name: idx_fedidentity_feduser; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fedidentity_feduser ON public.federated_identity USING btree (federated_user_id);


--
-- Name: idx_fedidentity_user; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fedidentity_user ON public.federated_identity USING btree (user_id);


--
-- Name: idx_fu_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_attribute ON public.fed_user_attribute USING btree (user_id, realm_id, name);


--
-- Name: idx_fu_cnsnt_ext; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_cnsnt_ext ON public.fed_user_consent USING btree (user_id, client_storage_provider, external_client_id);


--
-- Name: idx_fu_consent; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_consent ON public.fed_user_consent USING btree (user_id, client_id);


--
-- Name: idx_fu_consent_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_consent_ru ON public.fed_user_consent USING btree (realm_id, user_id);


--
-- Name: idx_fu_credential; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_credential ON public.fed_user_credential USING btree (user_id, type);


--
-- Name: idx_fu_credential_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_credential_ru ON public.fed_user_credential USING btree (realm_id, user_id);


--
-- Name: idx_fu_group_membership; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_group_membership ON public.fed_user_group_membership USING btree (user_id, group_id);


--
-- Name: idx_fu_group_membership_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_group_membership_ru ON public.fed_user_group_membership USING btree (realm_id, user_id);


--
-- Name: idx_fu_required_action; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_required_action ON public.fed_user_required_action USING btree (user_id, required_action);


--
-- Name: idx_fu_required_action_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_required_action_ru ON public.fed_user_required_action USING btree (realm_id, user_id);


--
-- Name: idx_fu_role_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_role_mapping ON public.fed_user_role_mapping USING btree (user_id, role_id);


--
-- Name: idx_fu_role_mapping_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_role_mapping_ru ON public.fed_user_role_mapping USING btree (realm_id, user_id);


--
-- Name: idx_group_attr_group; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_group_attr_group ON public.group_attribute USING btree (group_id);


--
-- Name: idx_group_role_mapp_group; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_group_role_mapp_group ON public.group_role_mapping USING btree (group_id);


--
-- Name: idx_id_prov_mapp_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_id_prov_mapp_realm ON public.identity_provider_mapper USING btree (realm_id);


--
-- Name: idx_ident_prov_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_ident_prov_realm ON public.identity_provider USING btree (realm_id);


--
-- Name: idx_keycloak_role_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_keycloak_role_client ON public.keycloak_role USING btree (client);


--
-- Name: idx_keycloak_role_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_keycloak_role_realm ON public.keycloak_role USING btree (realm);


--
-- Name: idx_offline_css_preload; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_css_preload ON public.offline_client_session USING btree (client_id, offline_flag);


--
-- Name: idx_offline_uss_by_user; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_uss_by_user ON public.offline_user_session USING btree (user_id, realm_id, offline_flag);


--
-- Name: idx_offline_uss_by_usersess; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_uss_by_usersess ON public.offline_user_session USING btree (realm_id, offline_flag, user_session_id);


--
-- Name: idx_offline_uss_createdon; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_uss_createdon ON public.offline_user_session USING btree (created_on);


--
-- Name: idx_offline_uss_preload; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_uss_preload ON public.offline_user_session USING btree (offline_flag, created_on, user_session_id);


--
-- Name: idx_protocol_mapper_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_protocol_mapper_client ON public.protocol_mapper USING btree (client_id);


--
-- Name: idx_realm_attr_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_attr_realm ON public.realm_attribute USING btree (realm_id);


--
-- Name: idx_realm_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_clscope ON public.client_scope USING btree (realm_id);


--
-- Name: idx_realm_def_grp_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_def_grp_realm ON public.realm_default_groups USING btree (realm_id);


--
-- Name: idx_realm_evt_list_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_evt_list_realm ON public.realm_events_listeners USING btree (realm_id);


--
-- Name: idx_realm_evt_types_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_evt_types_realm ON public.realm_enabled_event_types USING btree (realm_id);


--
-- Name: idx_realm_master_adm_cli; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_master_adm_cli ON public.realm USING btree (master_admin_client);


--
-- Name: idx_realm_supp_local_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_supp_local_realm ON public.realm_supported_locales USING btree (realm_id);


--
-- Name: idx_redir_uri_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_redir_uri_client ON public.redirect_uris USING btree (client_id);


--
-- Name: idx_req_act_prov_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_req_act_prov_realm ON public.required_action_provider USING btree (realm_id);


--
-- Name: idx_res_policy_policy; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_policy_policy ON public.resource_policy USING btree (policy_id);


--
-- Name: idx_res_scope_scope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_scope_scope ON public.resource_scope USING btree (scope_id);


--
-- Name: idx_res_serv_pol_res_serv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_serv_pol_res_serv ON public.resource_server_policy USING btree (resource_server_id);


--
-- Name: idx_res_srv_res_res_srv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_srv_res_res_srv ON public.resource_server_resource USING btree (resource_server_id);


--
-- Name: idx_res_srv_scope_res_srv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_srv_scope_res_srv ON public.resource_server_scope USING btree (resource_server_id);


--
-- Name: idx_role_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_role_attribute ON public.role_attribute USING btree (role_id);


--
-- Name: idx_role_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_role_clscope ON public.client_scope_role_mapping USING btree (role_id);


--
-- Name: idx_scope_mapping_role; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_scope_mapping_role ON public.scope_mapping USING btree (role_id);


--
-- Name: idx_scope_policy_policy; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_scope_policy_policy ON public.scope_policy USING btree (policy_id);


--
-- Name: idx_update_time; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_update_time ON public.migration_model USING btree (update_time);


--
-- Name: idx_us_sess_id_on_cl_sess; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_us_sess_id_on_cl_sess ON public.offline_client_session USING btree (user_session_id);


--
-- Name: idx_usconsent_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usconsent_clscope ON public.user_consent_client_scope USING btree (user_consent_id);


--
-- Name: idx_user_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_attribute ON public.user_attribute USING btree (user_id);


--
-- Name: idx_user_attribute_name; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_attribute_name ON public.user_attribute USING btree (name, value);


--
-- Name: idx_user_consent; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_consent ON public.user_consent USING btree (user_id);


--
-- Name: idx_user_credential; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_credential ON public.credential USING btree (user_id);


--
-- Name: idx_user_email; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_email ON public.user_entity USING btree (email);


--
-- Name: idx_user_group_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_group_mapping ON public.user_group_membership USING btree (user_id);


--
-- Name: idx_user_reqactions; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_reqactions ON public.user_required_action USING btree (user_id);


--
-- Name: idx_user_role_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_role_mapping ON public.user_role_mapping USING btree (user_id);


--
-- Name: idx_usr_fed_map_fed_prv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_map_fed_prv ON public.user_federation_mapper USING btree (federation_provider_id);


--
-- Name: idx_usr_fed_map_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_map_realm ON public.user_federation_mapper USING btree (realm_id);


--
-- Name: idx_usr_fed_prv_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_prv_realm ON public.user_federation_provider USING btree (realm_id);


--
-- Name: idx_web_orig_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_web_orig_client ON public.web_origins USING btree (client_id);


--
-- Name: client_session_auth_status auth_status_constraint; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_auth_status
    ADD CONSTRAINT auth_status_constraint FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: identity_provider fk2b4ebc52ae5c3b34; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT fk2b4ebc52ae5c3b34 FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_attributes fk3c47c64beacca966; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_attributes
    ADD CONSTRAINT fk3c47c64beacca966 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: federated_identity fk404288b92ef007a6; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_identity
    ADD CONSTRAINT fk404288b92ef007a6 FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: client_node_registrations fk4129723ba992f594; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_node_registrations
    ADD CONSTRAINT fk4129723ba992f594 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: client_session_note fk5edfb00ff51c2736; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_note
    ADD CONSTRAINT fk5edfb00ff51c2736 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: user_session_note fk5edfb00ff51d3472; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session_note
    ADD CONSTRAINT fk5edfb00ff51d3472 FOREIGN KEY (user_session) REFERENCES public.user_session(id);


--
-- Name: client_session_role fk_11b7sgqw18i532811v7o2dv76; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_role
    ADD CONSTRAINT fk_11b7sgqw18i532811v7o2dv76 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: redirect_uris fk_1burs8pb4ouj97h5wuppahv9f; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.redirect_uris
    ADD CONSTRAINT fk_1burs8pb4ouj97h5wuppahv9f FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: user_federation_provider fk_1fj32f6ptolw2qy60cd8n01e8; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_provider
    ADD CONSTRAINT fk_1fj32f6ptolw2qy60cd8n01e8 FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_session_prot_mapper fk_33a8sgqw18i532811v7o2dk89; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_prot_mapper
    ADD CONSTRAINT fk_33a8sgqw18i532811v7o2dk89 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: realm_required_credential fk_5hg65lybevavkqfki3kponh9v; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_required_credential
    ADD CONSTRAINT fk_5hg65lybevavkqfki3kponh9v FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: resource_attribute fk_5hrm2vlf9ql5fu022kqepovbr; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_attribute
    ADD CONSTRAINT fk_5hrm2vlf9ql5fu022kqepovbr FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: user_attribute fk_5hrm2vlf9ql5fu043kqepovbr; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_attribute
    ADD CONSTRAINT fk_5hrm2vlf9ql5fu043kqepovbr FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: user_required_action fk_6qj3w1jw9cvafhe19bwsiuvmd; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_required_action
    ADD CONSTRAINT fk_6qj3w1jw9cvafhe19bwsiuvmd FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: keycloak_role fk_6vyqfe4cn4wlq8r6kt5vdsj5c; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT fk_6vyqfe4cn4wlq8r6kt5vdsj5c FOREIGN KEY (realm) REFERENCES public.realm(id);


--
-- Name: realm_smtp_config fk_70ej8xdxgxd0b9hh6180irr0o; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_smtp_config
    ADD CONSTRAINT fk_70ej8xdxgxd0b9hh6180irr0o FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_attribute fk_8shxd6l3e9atqukacxgpffptw; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_attribute
    ADD CONSTRAINT fk_8shxd6l3e9atqukacxgpffptw FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: composite_role fk_a63wvekftu8jo1pnj81e7mce2; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT fk_a63wvekftu8jo1pnj81e7mce2 FOREIGN KEY (composite) REFERENCES public.keycloak_role(id);


--
-- Name: authentication_execution fk_auth_exec_flow; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT fk_auth_exec_flow FOREIGN KEY (flow_id) REFERENCES public.authentication_flow(id);


--
-- Name: authentication_execution fk_auth_exec_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT fk_auth_exec_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: authentication_flow fk_auth_flow_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_flow
    ADD CONSTRAINT fk_auth_flow_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: authenticator_config fk_auth_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config
    ADD CONSTRAINT fk_auth_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_session fk_b4ao2vcvat6ukau74wbwtfqo1; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session
    ADD CONSTRAINT fk_b4ao2vcvat6ukau74wbwtfqo1 FOREIGN KEY (session_id) REFERENCES public.user_session(id);


--
-- Name: user_role_mapping fk_c4fqv34p1mbylloxang7b1q3l; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_role_mapping
    ADD CONSTRAINT fk_c4fqv34p1mbylloxang7b1q3l FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: client_scope_attributes fk_cl_scope_attr_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_attributes
    ADD CONSTRAINT fk_cl_scope_attr_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_scope_role_mapping fk_cl_scope_rm_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_role_mapping
    ADD CONSTRAINT fk_cl_scope_rm_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_user_session_note fk_cl_usr_ses_note; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_user_session_note
    ADD CONSTRAINT fk_cl_usr_ses_note FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: protocol_mapper fk_cli_scope_mapper; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT fk_cli_scope_mapper FOREIGN KEY (client_scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_initial_access fk_client_init_acc_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_initial_access
    ADD CONSTRAINT fk_client_init_acc_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: component_config fk_component_config; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component_config
    ADD CONSTRAINT fk_component_config FOREIGN KEY (component_id) REFERENCES public.component(id);


--
-- Name: component fk_component_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT fk_component_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_default_groups fk_def_groups_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT fk_def_groups_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: user_federation_mapper_config fk_fedmapper_cfg; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper_config
    ADD CONSTRAINT fk_fedmapper_cfg FOREIGN KEY (user_federation_mapper_id) REFERENCES public.user_federation_mapper(id);


--
-- Name: user_federation_mapper fk_fedmapperpm_fedprv; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT fk_fedmapperpm_fedprv FOREIGN KEY (federation_provider_id) REFERENCES public.user_federation_provider(id);


--
-- Name: user_federation_mapper fk_fedmapperpm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT fk_fedmapperpm_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: associated_policy fk_frsr5s213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT fk_frsr5s213xcx4wnkog82ssrfy FOREIGN KEY (associated_policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: scope_policy fk_frsrasp13xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT fk_frsrasp13xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog82sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog82sspmt FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_server_resource fk_frsrho213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT fk_frsrho213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog83sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog83sspmt FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog84sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog84sspmt FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: associated_policy fk_frsrpas14xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT fk_frsrpas14xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: scope_policy fk_frsrpass3xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT fk_frsrpass3xcx4wnkog82ssrfy FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: resource_server_perm_ticket fk_frsrpo2128cx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrpo2128cx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_server_policy fk_frsrpo213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT fk_frsrpo213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_scope fk_frsrpos13xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT fk_frsrpos13xcx4wnkog82ssrfy FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_policy fk_frsrpos53xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT fk_frsrpos53xcx4wnkog82ssrfy FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_policy fk_frsrpp213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT fk_frsrpp213xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_scope fk_frsrps213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT fk_frsrps213xcx4wnkog82ssrfy FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: resource_server_scope fk_frsrso213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT fk_frsrso213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: composite_role fk_gr7thllb9lu8q4vqa4524jjy8; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT fk_gr7thllb9lu8q4vqa4524jjy8 FOREIGN KEY (child_role) REFERENCES public.keycloak_role(id);


--
-- Name: user_consent_client_scope fk_grntcsnt_clsc_usc; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent_client_scope
    ADD CONSTRAINT fk_grntcsnt_clsc_usc FOREIGN KEY (user_consent_id) REFERENCES public.user_consent(id);


--
-- Name: user_consent fk_grntcsnt_user; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT fk_grntcsnt_user FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: group_attribute fk_group_attribute_group; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_attribute
    ADD CONSTRAINT fk_group_attribute_group FOREIGN KEY (group_id) REFERENCES public.keycloak_group(id);


--
-- Name: group_role_mapping fk_group_role_group; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_role_mapping
    ADD CONSTRAINT fk_group_role_group FOREIGN KEY (group_id) REFERENCES public.keycloak_group(id);


--
-- Name: realm_enabled_event_types fk_h846o4h0w8epx5nwedrf5y69j; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_enabled_event_types
    ADD CONSTRAINT fk_h846o4h0w8epx5nwedrf5y69j FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_events_listeners fk_h846o4h0w8epx5nxev9f5y69j; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_events_listeners
    ADD CONSTRAINT fk_h846o4h0w8epx5nxev9f5y69j FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: identity_provider_mapper fk_idpm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_mapper
    ADD CONSTRAINT fk_idpm_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: idp_mapper_config fk_idpmconfig; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.idp_mapper_config
    ADD CONSTRAINT fk_idpmconfig FOREIGN KEY (idp_mapper_id) REFERENCES public.identity_provider_mapper(id);


--
-- Name: web_origins fk_lojpho213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.web_origins
    ADD CONSTRAINT fk_lojpho213xcx4wnkog82ssrfy FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: scope_mapping fk_ouse064plmlr732lxjcn1q5f1; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_mapping
    ADD CONSTRAINT fk_ouse064plmlr732lxjcn1q5f1 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: protocol_mapper fk_pcm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT fk_pcm_realm FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: credential fk_pfyr0glasqyl0dei3kl69r6v0; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.credential
    ADD CONSTRAINT fk_pfyr0glasqyl0dei3kl69r6v0 FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: protocol_mapper_config fk_pmconfig; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper_config
    ADD CONSTRAINT fk_pmconfig FOREIGN KEY (protocol_mapper_id) REFERENCES public.protocol_mapper(id);


--
-- Name: default_client_scope fk_r_def_cli_scope_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.default_client_scope
    ADD CONSTRAINT fk_r_def_cli_scope_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: required_action_provider fk_req_act_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_provider
    ADD CONSTRAINT fk_req_act_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: resource_uris fk_resource_server_uris; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_uris
    ADD CONSTRAINT fk_resource_server_uris FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: role_attribute fk_role_attribute_id; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.role_attribute
    ADD CONSTRAINT fk_role_attribute_id FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: realm_supported_locales fk_supported_locales_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_supported_locales
    ADD CONSTRAINT fk_supported_locales_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: user_federation_config fk_t13hpu1j94r2ebpekr39x5eu5; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_config
    ADD CONSTRAINT fk_t13hpu1j94r2ebpekr39x5eu5 FOREIGN KEY (user_federation_provider_id) REFERENCES public.user_federation_provider(id);


--
-- Name: user_group_membership fk_user_group_user; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_group_membership
    ADD CONSTRAINT fk_user_group_user FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: policy_config fkdc34197cf864c4e43; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.policy_config
    ADD CONSTRAINT fkdc34197cf864c4e43 FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: identity_provider_config fkdc4897cf864c4e43; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_config
    ADD CONSTRAINT fkdc4897cf864c4e43 FOREIGN KEY (identity_provider_id) REFERENCES public.identity_provider(internal_id);


--
-- PostgreSQL database dump complete
--

