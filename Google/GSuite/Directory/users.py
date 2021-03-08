from types import MethodType
from ...base import Base
from ...utilities import request_parameter


class Users(Base):

    def delete(self, user_key: str) -> dict:
        """
        Deletes a user.
        Args:
            user_key str: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def get(
        self, user_key: str, custom_field_mask: str = None,
        projection: str = None, view_type: str = None
    ) -> dict:
        """
        Retrieves a user.
        Args:
            user_key str: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
            custom_field_mask str: A comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when projection=custom.
            projection str: What subset of fields to fetch for this user.
                PROJECTION_UNDEFINED
                BASIC               Do not include any custom fields for the user.
                CUSTOM              Include custom fields from schemas requested in customFieldMask.
                FULL                Include all fields associated with this user.
            view_type str: Whether to fetch the administrator-only or domain-wide public view of the user. For more information, see Retrieve a user as a non-administrator.
                VIEW_TYPE_UNDEFINED
                ADMIN_VIEW          Results include both administrator-only and domain-public fields for the user.
                DOMAIN_PUBLIC       Results only include fields for the user that are publicly visible to other users in the domain.
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def insert(
        self,
        primary_email: str, password: str, family_name: str, given_name: str,
        id: str = None, hash_function: str = None, suspended: bool = None,
        change_password_at_next_login: bool = None,
        ip_whitelisted: bool = None, emails: str = None,
        external_ids: str = None, relations: str = None, addresses: str = None,
        organizations: str = None, last_login_time: str = None,
        phones: str = None, languages: str = None, posix_accounts: str = None,
        creation_time: str = None, ssh_public_keys: str = None,
        notes: str = None, websites: str = None, locations: str = None,
        include_in_global_address_list: bool = None, keywords: str = None,
        deletion_time: str = None, gender: str = None, ims: str = None,
        custom_schemas: str = None, archived: bool = None,
        org_unit_path: str = None, recovery_email: str = None,
        recovery_phone: str = None
    ) -> dict:
        """
        Creates a user.
        Args:
            id str: The unique ID for the user. A user?id?can be used as a user request URI's?userKey.
            primary_email str: The user's primary email address. This property is required in a request to create a user account. The?primaryEmail?must be unique and cannot be an alias of another user.
            password str: "Stores the password for the user account. The user's password value is required when creating a user account. It is optional when updating a user and should only be provided if the user is updating their account password.
            A password can contain any combination of ASCII characters. A minimum of 8 characters is required. The maximum length is 100 characters.
            We recommend sending the?password?property value as a base 16 bit, hexadecimal-encoded hash value. If a?hashFunction?is specified, the password must be a valid hash key.
            The password value is never returned in the API's response body."
            hash_function str: Stores the hash format of the password property. We recommend sending the?password?property value as a base 16 bit hexadecimal-encoded hash value. Set the?hashFunction?values as either the?SHA-1,?MD5, or [crypt](https://en.wikipedia.org/wiki/Crypt_(C)) hash format.
            suspended bool: Indicates if user is suspended.
            change_password_at_next_login bool: Indicates if the user is forced to change their password at next login. This setting doesn't apply when?the user signs in via a third-party identity provider.
            ip_whitelisted bool: If?true, the user's IP address is?white listed.
            family_name str: The user's last name. Required when creating a user account.
            given_name str: The user's first name. Required when creating a user account.
            emails str: A list of the user's email addresses. The maximum allowed data size for this field is 10Kb.
            external_ids str: A list of external IDs for the user, such as an employee or network ID. The maximum allowed data size for this field is 2Kb.
            relations str: A list of the user's relationships to other users. The maximum allowed data size for this field is 2Kb.
            addresses str: A list of the user's addresses. The maximum allowed data size for this field is 10Kb.
            organizations str: A list of organizations the user belongs to. The maximum allowed data size for this field is 10Kb.
            phones str: A list of the user's phone numbers. The maximum allowed data size for this field is 1Kb.
            languages str: The user's languages. The maximum allowed data size for this field is 1Kb.
            posix_accounts str: A list of?POSIX?account information for the user.
            ssh_public_keys str: A list of SSH public keys.
            notes str: Notes for the user.
            websites str: The user's websites. The maximum allowed data size for this field is 2Kb.
            locations str: The user's locations. The maximum allowed data size for this field is 10Kb.
            include_in_global_address_list bool: Indicates if the user's profile is visible in the G Suite global address list when the contact sharing feature is enabled for the domain. For more information about excluding user profiles, see the?administration help center.
            keywords str: The user's keywords. The maximum allowed data size for this field is 1Kb.
            gender str: The user's gender. The maximum allowed data size for this field is 1Kb.
            ims str: The user's Instant Messenger (IM) accounts. A user account can have multiple ims properties. But, only one of these ims properties can be the primary IM contact. The maximum allowed data size for this field is 2Kb.
            custom_schemas str: Custom fields of the user.
            archived bool: Indicates if user is archived.
            org_unit_path str: The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (/).
            recovery_email str: Recovery email of the user.
            recovery_phone str: Recovery phone of the user. The phone number must be in the E.164 format, starting with the plus sign (+). Example:?+16506661212.
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def list(
        self,
        custom_field_mask: str = None, customer: str = None,
        domain: str = None, max_results: int = None, order_by: str = None,
        page_token: str = None, projection: str = None, query: str = None,
        show_deleted: str = None, sort_order: str = None, view_type: str = None
    ) -> dict:
        """
        Retrieves a paginated list of either deleted users or all users in a domain.
        Args:
            custom_field_mask str: A comma-separated list of schema names. All fields from these schemas are fetched. This should only be set when?projection=custom.
            customer str: The unique ID for the customer's G Suite account. In case of a multi-domain account, to fetch all groups for a customer, fill this field instead of domain. You can also use the?my_customer?alias to represent your account's?customerId. The?customerId?is also returned as part of the?Users resource. Either the?customer?or the?domain?parameter must be provided.
            domain str: The domain name. Use this field to get fields from only one domain. To return all domains for a customer account, use the?customer?query parameter instead. Either the?customer?or the?domain?parameter must be provided.
            max_results int: Maximum number of results to return.
            order_by str: Property to use for sorting results.
            page_token str: Token to specify next page in the list
            projection str: What subset of fields to fetch for this user.
            query str: Query string for searching user fields. For more information on constructing user queries, see?Search for Users.
            show_deleted str: If set to?true, retrieves the list of deleted users. (Default:?false)
            sort_order str: Whether to return results in ascending or descending order.
            view_type str: Whether to fetch the administrator-only or domain-wide public view of the user. For more information, see?Retrieve a user as a non-administrator.
        """
        request = request_parameter(locals())
        return self.http_request(**request)

    def make_admin(
        self, user_key: str, status: bool
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def patch(
        self, user_key: str,
        primary_email: str = None, password: str = None,
        family_name: str = None, given_name: str = None,
        id: str = None, hash_function: str = None, suspended: bool = None,
        change_password_at_next_login: bool = None,
        ip_whitelisted: bool = None, emails: str = None,
        external_ids: str = None, relations: str = None, addresses: str = None,
        organizations: str = None, last_login_time: str = None,
        phones: str = None, languages: str = None, posix_accounts: str = None,
        creation_time: str = None, ssh_public_keys: str = None,
        notes: str = None, websites: str = None, locations: str = None,
        include_in_global_address_list: bool = None, keywords: str = None,
        deletion_time: str = None, gender: str = None, ims: str = None,
        custom_schemas: str = None, archived: bool = None,
        org_unit_path: str = None, recovery_email: str = None,
        recovery_phone: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def sign_out(self, user_key: str) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def undelete(self, user_key: str, org_unit_path: str) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def update(
        self, user_key: str,
        primary_email: str = None, password: str = None,
        family_name: str = None, given_name: str = None,
        id: str = None, hash_function: str = None, suspended: bool = None,
        change_password_at_next_login: bool = None,
        ip_whitelisted: bool = None, emails: str = None,
        external_ids: str = None, relations: str = None, addresses: str = None,
        organizations: str = None, last_login_time: str = None,
        phones: str = None, languages: str = None, posix_accounts: str = None,
        creation_time: str = None, ssh_public_keys: str = None,
        notes: str = None, websites: str = None, locations: str = None,
        include_in_global_address_list: bool = None, keywords: str = None,
        deletion_time: str = None, gender: str = None, ims: str = None,
        custom_schemas: str = None, archived: bool = None,
        org_unit_path: str = None, recovery_email: str = None,
        recovery_phone: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)

    def watch(
        self, domain: str = None, customer: str = None, event: str = None,
        custom_field_mask: str = None, max_results: int = None,
        order_by: str = None, page_token: str = None, projection: str = None,
        query: str = None, show_deleted: str = None, sort_order: str = None,
        view_type: str = None
    ) -> dict:
        request = request_parameter(locals())
        return self.http_request(**request)
