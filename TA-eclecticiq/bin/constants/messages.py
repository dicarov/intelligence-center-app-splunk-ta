"""MESSAGES."""
# API request success and failure messages
SUCCESS_MSG = "SUCCESS"
ERROR_MSG = "ERROR"

# Retry Messages
MAX_RETRY_WARNING = "{input}Reached to max retry attempts"
RETRY_ERROR_MSG = "{input}  trying again"


SETUP_CALLED = "Setup called !"
TEST_CONNECTION = "Test Connection !"
SAVE_CONFIGURATION = "Save configuration!"
TEST_CONNECTION_SUCCESSFULL = "Test Connection Successful."
USER_UNAUTHORIZED = "Error! 500 not authorised ."
USER_UNAUTHORIZED_MSG = (
    "Error! 500 not authorised . Please check URL, API key and Certificate of the url."
)
GET_CONFIGURATION = "Get configuration!"
CONFIGURATION_SAVED_SUCCESSFULLY = "Configuration saved Successfully ."
GET_OUTGOING_FEEDS = "Get Outgoing feeds!"

#
FETCH_OUTGOING_FEEDS = "Fetching outgoing feeds data!"
DATA_RECEIVED = "Data received {0}."
FETCH_ENTITIES = "Get entities status code: {0} ."
JSON_EXCEPTION = "Data is not a valid JSON : {0} ."
EXCEPTION = "Exception occured : {0} ."
COUNT_RECEIVED = "Count received {0} ."
OBSERVABLE_TYPE_RECEIVED = "Observable type received : {0} ."
OBSERVABLE_TYPE_MODIFIED = "Modified Observable type: {0} ."

ENTITY_ID_AND_OBSERVABLE_IDS = "Collector:Entity id and Observable ids : {} and {}"
ENTITY_ID_RECEIVED = "Collector: Entity Id received {}"
ENTITY_ID_MODIFIED = "Collector: Entity Id modified {}"
NOT_LOADING_OBSERVABLE = "Not loading this observable as it is of type : {}"

FORMATTED_DATA_TO_LOAD = "Formatted data to load: {0} ."
COLLECTING_DATA = "Collector: Getting entities and observables for ingestion."
OUTGOING_FEED_ID = "Collector: In Fetch outgoing-feed id {}"
GET_OBSERVABLE = "Collector:Getting observable by id!"

GET_OBSERVABLE_DATA = (
    "Collector:Getting data for observable id: {0} and outgoing_feed_id: {1} ."
)
ENDPOINT_CALLED = "Collector:Endpoint called {0}"

OBSERVABLE_DATA_DICT = "Collector:Found observable data to load in reference table."
NO_DATA_FOUND = "Collector:No data to load for {0} {1} ."
DATA_FOUND_FOR_FEED_ID_AND_TYPE = (
    "Collector:Data found to load for outgoing_feed_id: {0} ,observable_type {1}."
)
SEND_REQUEST = "Collector:Sending request with params {0}"
RESPONSE_RECEIVED = "Response Received! {0}"
OBSERVABLES_FOUND = "Collector:Observables found {0}"

IN_GET_ENTITIES = "Collector:In get entities counter : {}"

ADD_OBSERVABLES = "Collector:Added observables in long list. Total observables: {0} ."
BREAK_LOOP = "Collector:Breaking from the loop! ."
FETCH_OUTGOING_FEED_ID = "Collector:Fetching data for outgoing_feed_id: {0}"
CHECKPOINT_FOUND = "Collector:Checkpoint found for feed id {}"
OBSERVABLES_AND_CHECKPOINT_RECEIVED = (
    "Collector:Observables received: {0} and checkpoint received  {1}"
)
PENDING_OBSERVABLES = "Collector:Pending Observables to collect: {}"
COLLECTING_OBSERVABLE = "Collector:Currently collecting {} observable"

WRITING_CHECKPOINT = "Writing checkpoint with {0}"
CHECKPOINT_SUCCESSFULLY_WRITTEN = "Checkpoint successfully written."

CHECK_QRADAR_REFERENCE_TABLES = "Creating or checking qradar reference tables!"
TABLE_NAME = "Collector:Got Table : {0} "
CHECK_QRADAR_REFERENCE_TABLE = (
    "Collector:Creating or checking qradar reference table: {0}"
)
URL_MSG = " Url {0} "
DATA_FOUND = (
    "Collector:Found Observable key: {0} and last updated date for observable: {1} "
)
REQUEST_PARAM_NOT_VALID = "A request parameter is not valid for table creation: {0}."
TABLE_ALREADY_EXISTS = "The reference table with the name {0} already exist."
INTERNAL_ERROR = "Error occured in table creation! Status code: {0} and Content {1}"
TABLE_CREATED = "Reference table created ! Table Name: {0} and Status Code {1}"

BULK_LOAD_ERROR_PARSING = "An error occurred parsing the JSON-formatted message body. Bulk upload to Table: {0}"
REFERENCE_TABLE_DOES_NOT_EXIST = "The reference table {0} does not exist ."

BULK_LOAD_REQUEST_PARAM_NOT_VALID = (
    "A request parameter is not valid. Bulk upload to Table: {0} ."
)
BULK_LOAD_UPDATE_ERROR = "An error occurred during the attempt to add or update data in the reference table {0} ."

BULK_LOAD_INTERNAL_ERROR = "Table name {0} Error. Code: {1} Text: {2}"
BULK_LOAD_SUCCESSFULL = "Collector:Bulk upload to Reference Table {0} was successful ."

GET_REFERENCE_TABLE = "Getting reference table to check QRadar connection ."
GET_REFERENCE_TABLES_PARAM_NOT_VALID = (
    "A request parameter is not valid for fetching reference tables"
)
GET_REFERENCE_TABLES_NOT_FOUND = "Reference tables not found"
GET_REFERENCE_TABLES_ERROR = "Interval server error in fetching reference tables"
GET_REFERENCE_TABLES_INTERNAL_ERROR = (
    "Error occured in fetching reference table names Code: {0} Text: {1}"
)
SUCCESSFULLY_FETCHED_REFERENCE_TABLES = "Successfully fetched reference tables"

MISSING_PERMISSIONS = "User missing required permissions : {}"
GETTING_PLATFORM_PERMISSIONS = "Getting platform Permissions !"
REQUEST_UNAUTHORIZED = "Unauthrized request !"
USER_MISSING_PERMISSIONS = "Missing Permissions !"
ERROR_OCCURED_IN_PLATFORM_PERMISSIONS = (
    "Error occured in fetching platform permissions , Status Code :{} and content : {}"
)
SUCCESSFULLY_FETCHED_PLATFORM_PERMISSIONS = (
    "Successfully fetched platform permissions !"
)

GETTING_USER_PERMISSIONS = "Getting User Permissions !"
REQUEST_DOES_NOT_EXIST = "Request does not exist !"
ERROR_IN_USER_PERMISSIONS = (
    "Error occured in fetching user permissions , Status Code :{} and content : {}"
)
SUCCESSFULLY_FETCHED_USER_PERMISSIONS = "Successfully fetched user permissions !"

MISSING_READ_PERMISSIONS = "Missing permission for user: read permissions"
ALL_PERMISSIONS_GRANTED_TO_USER = (
    "All permissions granted to user. Permissions missing is: {}"
)
RECEIVED_TABLES = "Delete Observables:Received all tables :{}"
DELETE_EVENTS = "Delete Observables: In Delete Events."
REFERENCE_DATA_TABLES = "Delete Observables: Getting reference data tables."
DELETE_ERROR_IN_FETCHING_TABLES = "Delete Observables: Error occured in fetching reference tables ! Status code received :{0} and Text :{1}"
ERROR_IN_FETCHING_TABLES = "Error occured in fetching reference tables ! Status code received :{0} and Text :{1}"
DELETE_REQUEST_PARAM_INVALID = "Delete Observables:Request param is invalid! "
DELETE_SUCCESSFULLY_FETCHED_REFERENCE_TABLES = (
    "Delete Observables:Successfully fetched reference tables"
)
REQUEST_PARAM_INVALID = "Request param is invalid! "

DELETE_REFERENCE_TABLE_DOES_NOT_EXIST = (
    "Delete Observables:The reference table {0} does not exist ."
)
RECORD_DOES_NOT_EXIST = (
    "The reference table does not exist {} or the record does not exist"
)
ERROR_IN_DELETE_OBSERVABLES = "Error occured in deleteing observable value ! Status code received :{0} and Text :{1}"

VALUE_REMOVED = "The reference table had a value removed !"
SUCCESSFULLY_REMOVED_OBSERVABLE = "Successfully removed the observable !"


DELETE_DATA_FOUND = "Delete Observables:Found Observable key: {0} and last updated date for observable: {1} "
DELETE_OBSERVABLE_DATA_IS_OLDER = "Delete Observables:Last updated date for observable is {} older than formatted date {}"
DELETE_FETCH_DATA = "Delete Observables:Fetching observable data for tables."
FETCH_DATA_FOR_TABLE = "Delete Observables:Fetching observable data for table : {}"
OBSERVABLE_DELETED = "Delete Observables:Observable value deleted for table name {0}"
NO_DATA_TO_DELETE = "Delete Observables:No observable data to delete! {0}"


GET_TABLES = "Getting all Reference tables ! "
IN_DELETE = "In Delete Qradar reference tables !"
DELETING_TABLE = "Deleting Qradar reference table: {}"
REQUEST_PARAM_INVALID_TO_DELETE = "Request param is not valid {}"

ERROR_OCCURED_WHILE_DELETING_TABLE = "An error occurred during the attempt to remove or purge values from the reference table. Status code {} and Text {}"
REFERENCE_TABLE_REQUEST_ACCEPTED = "The reference data table: {0} deletion or purge request was accepted and is in progress.Status code {1}"
DATA_NOT_FOUND_FOR_SELECTED_OUTGOING_FEED = (
    "No data to delete for selected outgoing feed."
)
RETREIVE_TASK_STATUS = (
    "Retrieve the delete Reference Data Tables task status for task_id: {}"
)
TASK_DOES_NOT_EXIST = "The Delete Task Status does not exist. {}"
ERROR_OCCURED_WHILE_RETREVING_TASK_STATUS = "An error occurred while attempting to retrieve the Delete Task Status. Status code {} and Text {}"
TASK_STATUS_RETREIVED = (
    "The Delete Task Status: {0} has been retrieved with status code {1}"
)

# Sighting
NO_OBSERVABLES_FOUND = (
    "Create_sighting. Can not find the observables related to type:{}, value{}"
)

LOOKUP_OBS_CALLED = "Lookup Observables called"
SIGHTING_CREATED = "Sighting created successfully."
VIEW_CREATED_SIGHTING = "Sighting created! View: {}/api/beta/entities/{}"
SIGHTING_NOT_CREATED = "Sighting could not be created. {}"

DATA_OF_OUTGOING_FEED_DELETED_SUCCESSFULLY = (
    "Data of outgoing feed {} deleted successfully!"
)
TABLE_DELETED_SUCCESSFULLY = "Table deleted successfully :"
DELETE_REFERNCE_TABLES = "Delete refence tables called ."

REMOVING_CHECKPOINT = "Removing checkpoint!"
CHECKPOINT_REMOVED = "Checkpoint removed successfully."

OBSERVABLE_TIME_TO_LIVE_IS = "Observable time to live is : {} ."


#


CURRENT_INPUT_STANZA = "Current stanza : {}"
OUTGOING_FEED_IDS_SELECTED = "Outgoing-feed ids selected : {} "

LAST_UPDATED_VALUE_NOT_FOUND = (
    "Delete Observables:Last updated value for the observable not found for: {}"
)

OBSERVABLE_TIME_TO_LIVE = "Delete Observables: Observable time to live is : {}."
DELETE_OBSERVABLES = "Delete Observables: Deletion of observables in progress."
ENTITY_ID_RECEIVED_FOR_DELETE_OBSERVABLES = (
    "Delete Observables: Entity ID received : {}"
)
LENGTH_ENTITY_ID_LESS_THAN_2 = (
    "Delete Observables: Length of entity ID is less than 2 : {}"
)
UNABLE_TO_DELETE_OBSERVABLES = "Delete Observables:Unable to delete the observables."
ALL_OBSERVABLES_SUCCESSFULLY_DELETED = (
    "Delete Observables:All observables successfully deleted."
)

DELETE_OBSERVABLES_DATA_NOT_OLDER = "Delete observable data is not older {} {}"

API_ERROR = "Input: {input} Error: {err}"
EVENTS_RESPONSE_ERROR_CODE = "input {input} API responded with error {code}: {error}"

# Create Sighting Right Click

SIGHTING_CREATED = "Sighting Created Successfully. Link: {}/entity/{}"
REQUEST_FAILED = "Request failed!Please try again!!"
COULD_NOT_CREATE_SIGHTING = "Could not create sighting. Please try again!"
CREDS_NOT_FOUND = "Please store the credentials first from the configuration screen."

# Validator messages.
PROXY_FETCHING_ERROR_LOG_MESSAGE = (
    "Error while fetching proxy information.\n Error: {msg}"
)

SUCCESS_MSG = "Connection successful."
ERROR_MSG = "Connection unsuccessful."

API_ERROR = "Error: {err}"
API_KEY_REQUIRED_MSG = "API Key is required."
SSL_ERROR_MSG = "{error_msg_prefix} Error: Please check the SSL Cretificate of the URL."
INVALID_CREDS_ERROR_MSG = "{error_msg_prefix} Please enter valid URL, API Key or Proxy."
INVALID_CREDS_LOG_ERROR_MSG = (
    "{msg} Please enter valid URL, API Key or Proxy. Error: {err}"
)
INVALID_URL_ERROR_MSG = "URL must start with https."


CREDENTIALS_GIVEN_ARE_CORRECT = "Credentials entered are correct."
START_DATE_NOT_VALID_FORMAT = "Start date is not of valid format."

BACKFILL_TIME_OLDER = "Start date is older than 90 days."
SELECT_ATLEAST_ONE_OBSERVABLE_TYPE = "Atleast one observable type must be selected."
SELECT_ATLEAST_ONE_OBSERVABLE_TYPE_TO_BE_INGESTED = (
    "Select atleast one observable type to be ingested."
)

MIN_AND_MAX_INTERVAL = "Interval must be between 60s and 90 days."
INTERVAL_IS_BETWEEN_MIN_AND_MAX_INTERVAL = "Interval is between 60s and 7776000s"
INTERVAL_MUST_BE_BETWEEN_MIN_AND_MAX_INTERVAL = (
    "Interval must be between 60s and 7776000s"
)

UNIQUE_VALUES_FOR_OUTGOING_FEEDS_ALLOWED = (
    "Only unique values for outgoing-feeds are allowed."
)

MAXIMUM_FIVE_OUTGOING_FEEDS = "Maximum 5 outgoing-feeds allowed."
START_DATE_INCORRECT = "Start date is incorrect."
FUTURE_DATE_IS_NOT_ACCEPTABLE = "Future date is not acceptable."
