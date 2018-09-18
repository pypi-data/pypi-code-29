import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import dataclasses


@dataclasses.dataclass
class AccessDenied(ShapeBase):
    """
    Access denied.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ActiveTrustedSigners(ShapeBase):
    """
    A complex type that lists the AWS accounts, if any, that you included in the
    `TrustedSigners` complex type for this distribution. These are the accounts that
    you want to allow to create signed URLs for private content.

    The `Signer` complex type lists the AWS account number of the trusted signer or
    `self` if the signer is the AWS account that created the distribution. The
    `Signer` element also includes the IDs of any active CloudFront key pairs that
    are associated with the trusted signer's AWS account. If no `KeyPairId` element
    appears for a `Signer`, that signer can't create signed URLs.

    For more information, see [Serving Private Content through
    CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[Signer]),
            ),
        ]

    # Enabled is `true` if any of the AWS accounts listed in the `TrustedSigners`
    # complex type for this RTMP distribution have active CloudFront key pairs.
    # If not, `Enabled` is `false`.

    # For more information, see ActiveTrustedSigners.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `Signer` complex type for each trusted
    # signer specified in the `TrustedSigners` complex type.

    # For more information, see ActiveTrustedSigners.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `Signer` complex type for each trusted
    # signer that is specified in the `TrustedSigners` complex type.

    # For more information, see ActiveTrustedSigners.
    items: typing.List["Signer"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Aliases(ShapeBase):
    """
    A complex type that contains information about CNAMEs (alternate domain names),
    if any, for this distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of CNAME aliases, if any, that you want to associate with this
    # distribution.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains the CNAME aliases, if any, that you want to
    # associate with this distribution.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllowedMethods(ShapeBase):
    """
    A complex type that controls which HTTP methods CloudFront processes and
    forwards to your Amazon S3 bucket or your custom origin. There are three
    choices:

      * CloudFront forwards only `GET` and `HEAD` requests.

      * CloudFront forwards only `GET`, `HEAD`, and `OPTIONS` requests.

      * CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests.

    If you pick the third choice, you may need to restrict access to your Amazon S3
    bucket or to your custom origin so users can't perform operations that you don't
    want them to. For example, you might not want users to have permissions to
    delete objects from your origin.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[typing.Union[str, Method]]),
            ),
            (
                "cached_methods",
                "CachedMethods",
                TypeInfo(CachedMethods),
            ),
        ]

    # The number of HTTP methods that you want CloudFront to forward to your
    # origin. Valid values are 2 (for `GET` and `HEAD` requests), 3 (for `GET`,
    # `HEAD`, and `OPTIONS` requests) and 7 (for `GET, HEAD, OPTIONS, PUT, PATCH,
    # POST`, and `DELETE` requests).
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains the HTTP methods that you want CloudFront to
    # process and forward to your origin.
    items: typing.List[typing.Union[str, "Method"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that controls whether CloudFront caches the response to
    # requests using the specified HTTP methods. There are two choices:

    #   * CloudFront caches responses to `GET` and `HEAD` requests.

    #   * CloudFront caches responses to `GET`, `HEAD`, and `OPTIONS` requests.

    # If you pick the second choice for your Amazon S3 Origin, you may need to
    # forward Access-Control-Request-Method, Access-Control-Request-Headers, and
    # Origin headers for the responses to be cached correctly.
    cached_methods: "CachedMethods" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchTooLarge(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CNAMEAlreadyExists(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CacheBehavior(ShapeBase):
    """
    A complex type that describes how CloudFront processes requests.

    You must create at least as many cache behaviors (including the default cache
    behavior) as you have origins if you want CloudFront to distribute objects from
    all of the origins. Each cache behavior specifies the one origin from which you
    want CloudFront to get objects. If you have two origins and only the default
    cache behavior, the default cache behavior will cause CloudFront to get objects
    from one of the origins, but the other origin is never used.

    For the current limit on the number of cache behaviors that you can add to a
    distribution, see [Amazon CloudFront
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront)
    in the _AWS General Reference_.

    If you don't want to specify any cache behaviors, include only an empty
    `CacheBehaviors` element. Don't include an empty `CacheBehavior` element, or
    CloudFront returns a `MalformedXML` error.

    To delete all cache behaviors in an existing distribution, update the
    distribution configuration and include only an empty `CacheBehaviors` element.

    To add, change, or remove one or more cache behaviors, update the distribution
    configuration and specify all of the cache behaviors that you want to include in
    the updated distribution.

    For more information about cache behaviors, see [Cache
    Behaviors](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-
    web-values-specify.html#DownloadDistValuesCacheBehavior) in the _Amazon
    CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "path_pattern",
                "PathPattern",
                TypeInfo(str),
            ),
            (
                "target_origin_id",
                "TargetOriginId",
                TypeInfo(str),
            ),
            (
                "forwarded_values",
                "ForwardedValues",
                TypeInfo(ForwardedValues),
            ),
            (
                "trusted_signers",
                "TrustedSigners",
                TypeInfo(TrustedSigners),
            ),
            (
                "viewer_protocol_policy",
                "ViewerProtocolPolicy",
                TypeInfo(typing.Union[str, ViewerProtocolPolicy]),
            ),
            (
                "min_ttl",
                "MinTTL",
                TypeInfo(int),
            ),
            (
                "allowed_methods",
                "AllowedMethods",
                TypeInfo(AllowedMethods),
            ),
            (
                "smooth_streaming",
                "SmoothStreaming",
                TypeInfo(bool),
            ),
            (
                "default_ttl",
                "DefaultTTL",
                TypeInfo(int),
            ),
            (
                "max_ttl",
                "MaxTTL",
                TypeInfo(int),
            ),
            (
                "compress",
                "Compress",
                TypeInfo(bool),
            ),
            (
                "lambda_function_associations",
                "LambdaFunctionAssociations",
                TypeInfo(LambdaFunctionAssociations),
            ),
            (
                "field_level_encryption_id",
                "FieldLevelEncryptionId",
                TypeInfo(str),
            ),
        ]

    # The pattern (for example, `images/*.jpg`) that specifies which requests to
    # apply the behavior to. When CloudFront receives a viewer request, the
    # requested path is compared with path patterns in the order in which cache
    # behaviors are listed in the distribution.

    # You can optionally include a slash (`/`) at the beginning of the path
    # pattern. For example, `/images/*.jpg`. CloudFront behavior is the same with
    # or without the leading `/`.

    # The path pattern for the default cache behavior is `*` and cannot be
    # changed. If the request for an object does not match the path pattern for
    # any cache behaviors, CloudFront applies the behavior in the default cache
    # behavior.

    # For more information, see [Path
    # Pattern](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-
    # web-values-specify.html#DownloadDistValuesPathPattern) in the _Amazon
    # CloudFront Developer Guide_.
    path_pattern: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of `ID` for the origin that you want CloudFront to route requests
    # to when a request matches the path pattern either for a cache behavior or
    # for the default cache behavior in your distribution.
    target_origin_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies how CloudFront handles query strings and
    # cookies.
    forwarded_values: "ForwardedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that specifies the AWS accounts, if any, that you want to
    # allow to create signed URLs for private content.

    # If you want to require signed URLs in requests for objects in the target
    # origin that match the `PathPattern` for this cache behavior, specify `true`
    # for `Enabled`, and specify the applicable values for `Quantity` and
    # `Items`. For more information, see [Serving Private Content through
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    # in the _Amazon Amazon CloudFront Developer Guide_.

    # If you don't want to require signed URLs in requests for objects that match
    # `PathPattern`, specify `false` for `Enabled` and `0` for `Quantity`. Omit
    # `Items`.

    # To add, change, or remove one or more trusted signers, change `Enabled` to
    # `true` (if it's currently `false`), change `Quantity` as applicable, and
    # specify all of the trusted signers that you want to include in the updated
    # distribution.
    trusted_signers: "TrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The protocol that viewers can use to access the files in the origin
    # specified by `TargetOriginId` when a request matches the path pattern in
    # `PathPattern`. You can specify the following options:

    #   * `allow-all`: Viewers can use HTTP or HTTPS.

    #   * `redirect-to-https`: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.

    #   * `https-only`: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

    # For more information about requiring the HTTPS protocol, see [Using an
    # HTTPS Connection to Access Your
    # Objects](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html)
    # in the _Amazon CloudFront Developer Guide_.

    # The only way to guarantee that viewers retrieve an object that was fetched
    # from the origin using HTTPS is never to use any other protocol to fetch the
    # object. If you have recently changed from HTTP to HTTPS, we recommend that
    # you clear your objects' cache because cached objects are protocol agnostic.
    # That means that an edge location will return an object from the cache
    # regardless of whether the current request protocol matches the protocol
    # used previously. For more information, see [Specifying How Long Objects and
    # Errors Stay in a CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon CloudFront Developer Guide_.
    viewer_protocol_policy: typing.Union[str, "ViewerProtocolPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The minimum amount of time that you want objects to stay in CloudFront
    # caches before CloudFront forwards another request to your origin to
    # determine whether the object has been updated. For more information, see
    # [Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon Amazon CloudFront Developer Guide_.

    # You must specify `0` for `MinTTL` if you configure CloudFront to forward
    # all headers to your origin (under `Headers`, if you specify `1` for
    # `Quantity` and `*` for `Name`).
    min_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that controls which HTTP methods CloudFront processes and
    # forwards to your Amazon S3 bucket or your custom origin. There are three
    # choices:

    #   * CloudFront forwards only `GET` and `HEAD` requests.

    #   * CloudFront forwards only `GET`, `HEAD`, and `OPTIONS` requests.

    #   * CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests.

    # If you pick the third choice, you may need to restrict access to your
    # Amazon S3 bucket or to your custom origin so users can't perform operations
    # that you don't want them to. For example, you might not want users to have
    # permissions to delete objects from your origin.
    allowed_methods: "AllowedMethods" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether you want to distribute media files in the Microsoft
    # Smooth Streaming format using the origin that is associated with this cache
    # behavior. If so, specify `true`; if not, specify `false`. If you specify
    # `true` for `SmoothStreaming`, you can still distribute other content using
    # this cache behavior if the content matches the value of `PathPattern`.
    smooth_streaming: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default amount of time that you want objects to stay in CloudFront
    # caches before CloudFront forwards another request to your origin to
    # determine whether the object has been updated. The value that you specify
    # applies only when your origin does not add HTTP headers such as `Cache-
    # Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects. For
    # more information, see [Specifying How Long Objects and Errors Stay in a
    # CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon CloudFront Developer Guide_.
    default_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum amount of time that you want objects to stay in CloudFront
    # caches before CloudFront forwards another request to your origin to
    # determine whether the object has been updated. The value that you specify
    # applies only when your origin adds HTTP headers such as `Cache-Control max-
    # age`, `Cache-Control s-maxage`, and `Expires` to objects. For more
    # information, see [Specifying How Long Objects and Errors Stay in a
    # CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon CloudFront Developer Guide_.
    max_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want CloudFront to automatically compress certain files for
    # this cache behavior. If so, specify true; if not, specify false. For more
    # information, see [Serving Compressed
    # Files](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)
    # in the _Amazon CloudFront Developer Guide_.
    compress: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains zero or more Lambda function associations for
    # a cache behavior.
    lambda_function_associations: "LambdaFunctionAssociations" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of `ID` for the field-level encryption configuration that you
    # want CloudFront to use for encrypting specific fields of data for a cache
    # behavior or for the default cache behavior in your distribution.
    field_level_encryption_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CacheBehaviors(ShapeBase):
    """
    A complex type that contains zero or more `CacheBehavior` elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[CacheBehavior]),
            ),
        ]

    # The number of cache behaviors for this distribution.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Optional: A complex type that contains cache behaviors for this
    # distribution. If `Quantity` is `0`, you can omit `Items`.
    items: typing.List["CacheBehavior"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CachedMethods(ShapeBase):
    """
    A complex type that controls whether CloudFront caches the response to requests
    using the specified HTTP methods. There are two choices:

      * CloudFront caches responses to `GET` and `HEAD` requests.

      * CloudFront caches responses to `GET`, `HEAD`, and `OPTIONS` requests.

    If you pick the second choice for your Amazon S3 Origin, you may need to forward
    Access-Control-Request-Method, Access-Control-Request-Headers, and Origin
    headers for the responses to be cached correctly.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[typing.Union[str, Method]]),
            ),
        ]

    # The number of HTTP methods for which you want CloudFront to cache
    # responses. Valid values are `2` (for caching responses to `GET` and `HEAD`
    # requests) and `3` (for caching responses to `GET`, `HEAD`, and `OPTIONS`
    # requests).
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains the HTTP methods that you want CloudFront to
    # cache responses to.
    items: typing.List[typing.Union[str, "Method"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CannotChangeImmutablePublicKeyFields(ShapeBase):
    """
    You can't change the value of a public key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class CertificateSource(str):
    cloudfront = "cloudfront"
    iam = "iam"
    acm = "acm"


@dataclasses.dataclass
class CloudFrontOriginAccessIdentity(ShapeBase):
    """
    CloudFront origin access identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "s3_canonical_user_id",
                "S3CanonicalUserId",
                TypeInfo(str),
            ),
            (
                "cloud_front_origin_access_identity_config",
                "CloudFrontOriginAccessIdentityConfig",
                TypeInfo(CloudFrontOriginAccessIdentityConfig),
            ),
        ]

    # The ID for the origin access identity, for example, `E74FTE3AJFJ256A`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 canonical user ID for the origin access identity, used when
    # giving the origin access identity read permission to an object in Amazon
    # S3.
    s3_canonical_user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current configuration information for the identity.
    cloud_front_origin_access_identity_config: "CloudFrontOriginAccessIdentityConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CloudFrontOriginAccessIdentityAlreadyExists(ShapeBase):
    """
    If the `CallerReference` is a value you already sent in a previous request to
    create an identity but the content of the `CloudFrontOriginAccessIdentityConfig`
    is different from the original request, CloudFront returns a
    `CloudFrontOriginAccessIdentityAlreadyExists` error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudFrontOriginAccessIdentityConfig(ShapeBase):
    """
    Origin access identity configuration. Send a `GET` request to the `/ _CloudFront
    API version_ /CloudFront/identity ID/config` resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # A unique number that ensures the request can't be replayed.

    # If the `CallerReference` is new (no matter the content of the
    # `CloudFrontOriginAccessIdentityConfig` object), a new origin access
    # identity is created.

    # If the `CallerReference` is a value already sent in a previous identity
    # request, and the content of the `CloudFrontOriginAccessIdentityConfig` is
    # identical to the original request (ignoring white space), the response
    # includes the same information returned to the original request.

    # If the `CallerReference` is a value you already sent in a previous request
    # to create an identity, but the content of the
    # `CloudFrontOriginAccessIdentityConfig` is different from the original
    # request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists`
    # error.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any comments you want to include about the origin access identity.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudFrontOriginAccessIdentityInUse(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloudFrontOriginAccessIdentityList(ShapeBase):
    """
    Lists the origin access identities for CloudFront.Send a `GET` request to the `/
    _CloudFront API version_ /origin-access-identity/cloudfront` resource. The
    response includes a `CloudFrontOriginAccessIdentityList` element with zero or
    more `CloudFrontOriginAccessIdentitySummary` child elements. By default, your
    entire list of origin access identities is returned in one single page. If the
    list is long, you can paginate it using the `MaxItems` and `Marker` parameters.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[CloudFrontOriginAccessIdentitySummary]),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # origin access identities. The results include identities in the list that
    # occur after the marker. To get the next page of results, set the `Marker`
    # to the value of the `NextMarker` from the current page's response (which is
    # also the ID of the last identity on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of origin access identities you want in the response
    # body.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether more origin access identities remain to be
    # listed. If your results were truncated, you can make a follow-up pagination
    # request using the `Marker` request parameter to retrieve more items in the
    # list.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of CloudFront origin access identities that were created by the
    # current AWS account.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `IsTruncated` is `true`, this element is present and contains the value
    # you can use for the `Marker` request parameter to continue listing your
    # origin access identities where they left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `CloudFrontOriginAccessIdentitySummary`
    # element for each origin access identity that was created by the current AWS
    # account.
    items: typing.List["CloudFrontOriginAccessIdentitySummary"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )


@dataclasses.dataclass
class CloudFrontOriginAccessIdentitySummary(ShapeBase):
    """
    Summary of the information about a CloudFront origin access identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "s3_canonical_user_id",
                "S3CanonicalUserId",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # The ID for the origin access identity. For example: `E74FTE3AJFJ256A`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 canonical user ID for the origin access identity, which you
    # use when giving the origin access identity read permission to an object in
    # Amazon S3.
    s3_canonical_user_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The comment for this origin access identity, as originally specified when
    # created.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContentTypeProfile(ShapeBase):
    """
    A field-level encryption content type profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "format",
                "Format",
                TypeInfo(typing.Union[str, Format]),
            ),
            (
                "content_type",
                "ContentType",
                TypeInfo(str),
            ),
            (
                "profile_id",
                "ProfileId",
                TypeInfo(str),
            ),
        ]

    # The format for a field-level encryption content type-profile mapping.
    format: typing.Union[str, "Format"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The content type for a field-level encryption content type-profile mapping.
    content_type: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The profile ID for a field-level encryption content type-profile mapping.
    profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ContentTypeProfileConfig(ShapeBase):
    """
    The configuration for a field-level encryption content type-profile mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "forward_when_content_type_is_unknown",
                "ForwardWhenContentTypeIsUnknown",
                TypeInfo(bool),
            ),
            (
                "content_type_profiles",
                "ContentTypeProfiles",
                TypeInfo(ContentTypeProfiles),
            ),
        ]

    # The setting in a field-level encryption content type-profile mapping that
    # specifies what to do when an unknown content type is provided for the
    # profile. If true, content is forwarded without being encrypted when the
    # content type is unknown. If false (the default), an error is returned when
    # the content type is unknown.
    forward_when_content_type_is_unknown: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The configuration for a field-level encryption content type-profile.
    content_type_profiles: "ContentTypeProfiles" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContentTypeProfiles(ShapeBase):
    """
    Field-level encryption content type-profile.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[ContentTypeProfile]),
            ),
        ]

    # The number of field-level encryption content type-profile mappings.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Items in a field-level encryption content type-profile mapping.
    items: typing.List["ContentTypeProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CookieNames(ShapeBase):
    """
    A complex type that specifies whether you want CloudFront to forward cookies to
    the origin and, if so, which ones. For more information about forwarding cookies
    to the origin, see [How CloudFront Forwards, Caches, and Logs
    Cookies](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of different cookies that you want CloudFront to forward to the
    # origin for this cache behavior.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `Name` element for each cookie that you
    # want CloudFront to forward to the origin for this cache behavior.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CookiePreference(ShapeBase):
    """
    A complex type that specifies whether you want CloudFront to forward cookies to
    the origin and, if so, which ones. For more information about forwarding cookies
    to the origin, see [How CloudFront Forwards, Caches, and Logs
    Cookies](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "forward",
                "Forward",
                TypeInfo(typing.Union[str, ItemSelection]),
            ),
            (
                "whitelisted_names",
                "WhitelistedNames",
                TypeInfo(CookieNames),
            ),
        ]

    # Specifies which cookies to forward to the origin for this cache behavior:
    # all, none, or the list of cookies specified in the `WhitelistedNames`
    # complex type.

    # Amazon S3 doesn't process cookies. When the cache behavior is forwarding
    # requests to an Amazon S3 origin, specify none for the `Forward` element.
    forward: typing.Union[str, "ItemSelection"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Required if you specify `whitelist` for the value of `Forward:`. A complex
    # type that specifies how many different cookies you want CloudFront to
    # forward to the origin for this cache behavior and, if you want to forward
    # selected cookies, the names of those cookies.

    # If you specify `all` or none for the value of `Forward`, omit
    # `WhitelistedNames`. If you change the value of `Forward` from `whitelist`
    # to all or none and you don't delete the `WhitelistedNames` element and its
    # child elements, CloudFront deletes them automatically.

    # For the current limit on the number of cookie names that you can whitelist
    # for each cache behavior, see [Amazon CloudFront
    # Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront)
    # in the _AWS General Reference_.
    whitelisted_names: "CookieNames" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCloudFrontOriginAccessIdentityRequest(ShapeBase):
    """
    The request to create a new origin access identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_front_origin_access_identity_config",
                "CloudFrontOriginAccessIdentityConfig",
                TypeInfo(CloudFrontOriginAccessIdentityConfig),
            ),
        ]

    # The current configuration information for the identity.
    cloud_front_origin_access_identity_config: "CloudFrontOriginAccessIdentityConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateCloudFrontOriginAccessIdentityResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cloud_front_origin_access_identity",
                "CloudFrontOriginAccessIdentity",
                TypeInfo(CloudFrontOriginAccessIdentity),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The origin access identity's information.
    cloud_front_origin_access_identity: "CloudFrontOriginAccessIdentity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new origin access identity just created. For
    # example: `https://cloudfront.amazonaws.com/2010-11-01/origin-access-
    # identity/cloudfront/E74FTE3AJFJ256A`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the origin access identity created.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDistributionRequest(ShapeBase):
    """
    The request to create a new distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_config",
                "DistributionConfig",
                TypeInfo(DistributionConfig),
            ),
        ]

    # The distribution's configuration information.
    distribution_config: "DistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution",
                "Distribution",
                TypeInfo(Distribution),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's information.
    distribution: "Distribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new distribution resource just created. For
    # example:
    # `https://cloudfront.amazonaws.com/2010-11-01/distribution/EDFDVBD632BHDS5`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the distribution created.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDistributionWithTagsRequest(ShapeBase):
    """
    The request to create a new distribution with tags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_config_with_tags",
                "DistributionConfigWithTags",
                TypeInfo(DistributionConfigWithTags),
            ),
        ]

    # The distribution's configuration information.
    distribution_config_with_tags: "DistributionConfigWithTags" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDistributionWithTagsResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution",
                "Distribution",
                TypeInfo(Distribution),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's information.
    distribution: "Distribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new distribution resource just created. For
    # example:
    # `https://cloudfront.amazonaws.com/2010-11-01/distribution/EDFDVBD632BHDS5`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the distribution created.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFieldLevelEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_level_encryption_config",
                "FieldLevelEncryptionConfig",
                TypeInfo(FieldLevelEncryptionConfig),
            ),
        ]

    # The request to create a new field-level encryption configuration.
    field_level_encryption_config: "FieldLevelEncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFieldLevelEncryptionConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption",
                "FieldLevelEncryption",
                TypeInfo(FieldLevelEncryption),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returned when you create a new field-level encryption configuration.
    field_level_encryption: "FieldLevelEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new configuration resource just created. For
    # example: `https://cloudfront.amazonaws.com/2010-11-01/field-level-
    # encryption-config/EDFDVBD632BHDS5`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the field level encryption configuration. For
    # example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateFieldLevelEncryptionProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_level_encryption_profile_config",
                "FieldLevelEncryptionProfileConfig",
                TypeInfo(FieldLevelEncryptionProfileConfig),
            ),
        ]

    # The request to create a field-level encryption profile.
    field_level_encryption_profile_config: "FieldLevelEncryptionProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateFieldLevelEncryptionProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_profile",
                "FieldLevelEncryptionProfile",
                TypeInfo(FieldLevelEncryptionProfile),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returned when you create a new field-level encryption profile.
    field_level_encryption_profile: "FieldLevelEncryptionProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new profile resource just created. For
    # example: `https://cloudfront.amazonaws.com/2010-11-01/field-level-
    # encryption-profile/EDFDVBD632BHDS5`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the field level encryption profile. For example:
    # `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInvalidationRequest(ShapeBase):
    """
    The request to create an invalidation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_id",
                "DistributionId",
                TypeInfo(str),
            ),
            (
                "invalidation_batch",
                "InvalidationBatch",
                TypeInfo(InvalidationBatch),
            ),
        ]

    # The distribution's id.
    distribution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The batch information for the invalidation.
    invalidation_batch: "InvalidationBatch" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateInvalidationResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "invalidation",
                "Invalidation",
                TypeInfo(Invalidation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the distribution and invalidation batch request,
    # including the `Invalidation ID`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The invalidation's information.
    invalidation: "Invalidation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "public_key_config",
                "PublicKeyConfig",
                TypeInfo(PublicKeyConfig),
            ),
        ]

    # The request to add a public key to CloudFront.
    public_key_config: "PublicKeyConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreatePublicKeyResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(PublicKey),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returned when you add a public key.
    public_key: "PublicKey" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The fully qualified URI of the new public key resource just created. For
    # example: `https://cloudfront.amazonaws.com/2010-11-01/cloudfront-public-
    # key/EDFDVBD632BHDS5`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the public key. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamingDistributionRequest(ShapeBase):
    """
    The request to create a new streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_distribution_config",
                "StreamingDistributionConfig",
                TypeInfo(StreamingDistributionConfig),
            ),
        ]

    # The streaming distribution's configuration information.
    streaming_distribution_config: "StreamingDistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStreamingDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution",
                "StreamingDistribution",
                TypeInfo(StreamingDistribution),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's information.
    streaming_distribution: "StreamingDistribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new streaming distribution resource just
    # created. For example:
    # `https://cloudfront.amazonaws.com/2010-11-01/streaming-
    # distribution/EGTXBD79H29TRA8`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the streaming distribution created.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateStreamingDistributionWithTagsRequest(ShapeBase):
    """
    The request to create a new streaming distribution with tags.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_distribution_config_with_tags",
                "StreamingDistributionConfigWithTags",
                TypeInfo(StreamingDistributionConfigWithTags),
            ),
        ]

    # The streaming distribution's configuration information.
    streaming_distribution_config_with_tags: "StreamingDistributionConfigWithTags" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateStreamingDistributionWithTagsResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution",
                "StreamingDistribution",
                TypeInfo(StreamingDistribution),
            ),
            (
                "location",
                "Location",
                TypeInfo(str),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's information.
    streaming_distribution: "StreamingDistribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The fully qualified URI of the new streaming distribution resource just
    # created. For example:`
    # https://cloudfront.amazonaws.com/2010-11-01/streaming-
    # distribution/EGTXBD79H29TRA8`.
    location: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomErrorResponse(ShapeBase):
    """
    A complex type that controls:

      * Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer. 

      * How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

    For more information about custom error pages, see [Customizing Error
    Responses](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-
    error-pages.html) in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "error_code",
                "ErrorCode",
                TypeInfo(int),
            ),
            (
                "response_page_path",
                "ResponsePagePath",
                TypeInfo(str),
            ),
            (
                "response_code",
                "ResponseCode",
                TypeInfo(str),
            ),
            (
                "error_caching_min_ttl",
                "ErrorCachingMinTTL",
                TypeInfo(int),
            ),
        ]

    # The HTTP status code for which you want to specify a custom error page
    # and/or a caching duration.
    error_code: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The path to the custom error page that you want CloudFront to return to a
    # viewer when your origin returns the HTTP status code specified by
    # `ErrorCode`, for example, `/4xx-errors/403-forbidden.html`. If you want to
    # store your objects and your custom error pages in different locations, your
    # distribution must include a cache behavior for which the following is true:

    #   * The value of `PathPattern` matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named `/4xx-errors`. Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, `/4xx-errors/*`.

    #   * The value of `TargetOriginId` specifies the value of the `ID` element for the origin that contains your custom error pages.

    # If you specify a value for `ResponsePagePath`, you must also specify a
    # value for `ResponseCode`. If you don't want to specify a value, include an
    # empty element, `<ResponsePagePath>`, in the XML document.

    # We recommend that you store custom error pages in an Amazon S3 bucket. If
    # you store custom error pages on an HTTP server and the server starts to
    # return 5xx errors, CloudFront can't get the files that you want to return
    # to viewers because the origin server is unavailable.
    response_page_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTP status code that you want CloudFront to return to the viewer along
    # with the custom error page. There are a variety of reasons that you might
    # want CloudFront to return a status code different from the status code that
    # your origin returned to CloudFront, for example:

    #   * Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute `200`, the response typically won't be intercepted.

    #   * If you don't care about distinguishing among different client errors or server errors, you can specify `400` or `500` as the `ResponseCode` for all 4xx or 5xx errors.

    #   * You might want to return a `200` status code (OK) and static website so your customers don't know that your website is down.

    # If you specify a value for `ResponseCode`, you must also specify a value
    # for `ResponsePagePath`. If you don't want to specify a value, include an
    # empty element, `<ResponseCode>`, in the XML document.
    response_code: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The minimum amount of time, in seconds, that you want CloudFront to cache
    # the HTTP status code specified in `ErrorCode`. When this time period has
    # elapsed, CloudFront queries your origin to see whether the problem that
    # caused the error has been resolved and the requested object is now
    # available.

    # If you don't want to specify a value, include an empty element,
    # `<ErrorCachingMinTTL>`, in the XML document.

    # For more information, see [Customizing Error
    # Responses](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-
    # error-pages.html) in the _Amazon CloudFront Developer Guide_.
    error_caching_min_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CustomErrorResponses(ShapeBase):
    """
    A complex type that controls:

      * Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.

      * How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

    For more information about custom error pages, see [Customizing Error
    Responses](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-
    error-pages.html) in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[CustomErrorResponse]),
            ),
        ]

    # The number of HTTP status codes for which you want to specify a custom
    # error page and/or a caching duration. If `Quantity` is `0`, you can omit
    # `Items`.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains a `CustomErrorResponse` element for each HTTP
    # status code for which you want to specify a custom error page and/or a
    # caching duration.
    items: typing.List["CustomErrorResponse"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CustomHeaders(ShapeBase):
    """
    A complex type that contains the list of Custom Headers for each origin.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[OriginCustomHeader]),
            ),
        ]

    # The number of custom headers, if any, for this distribution.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Optional** : A list that contains one `OriginCustomHeader` element for
    # each custom header that you want CloudFront to forward to the origin. If
    # Quantity is `0`, omit `Items`.
    items: typing.List["OriginCustomHeader"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CustomOriginConfig(ShapeBase):
    """
    A customer origin or an Amazon S3 bucket configured as a website endpoint.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "http_port",
                "HTTPPort",
                TypeInfo(int),
            ),
            (
                "https_port",
                "HTTPSPort",
                TypeInfo(int),
            ),
            (
                "origin_protocol_policy",
                "OriginProtocolPolicy",
                TypeInfo(typing.Union[str, OriginProtocolPolicy]),
            ),
            (
                "origin_ssl_protocols",
                "OriginSslProtocols",
                TypeInfo(OriginSslProtocols),
            ),
            (
                "origin_read_timeout",
                "OriginReadTimeout",
                TypeInfo(int),
            ),
            (
                "origin_keepalive_timeout",
                "OriginKeepaliveTimeout",
                TypeInfo(int),
            ),
        ]

    # The HTTP port the custom origin listens on.
    http_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The HTTPS port the custom origin listens on.
    https_port: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The origin protocol policy to apply to your origin.
    origin_protocol_policy: typing.Union[str, "OriginProtocolPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The SSL/TLS protocols that you want CloudFront to use when communicating
    # with your origin over HTTPS.
    origin_ssl_protocols: "OriginSslProtocols" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # You can create a custom origin read timeout. All timeout units are in
    # seconds. The default origin read timeout is 30 seconds, but you can
    # configure custom timeout lengths using the CloudFront API. The minimum
    # timeout length is 4 seconds; the maximum is 60 seconds.

    # If you need to increase the maximum time limit, contact the [AWS Support
    # Center](https://console.aws.amazon.com/support/home#/).
    origin_read_timeout: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # You can create a custom keep-alive timeout. All timeout units are in
    # seconds. The default keep-alive timeout is 5 seconds, but you can configure
    # custom timeout lengths using the CloudFront API. The minimum timeout length
    # is 1 second; the maximum is 60 seconds.

    # If you need to increase the maximum time limit, contact the [AWS Support
    # Center](https://console.aws.amazon.com/support/home#/).
    origin_keepalive_timeout: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DefaultCacheBehavior(ShapeBase):
    """
    A complex type that describes the default cache behavior if you don't specify a
    `CacheBehavior` element or if files don't match any of the values of
    `PathPattern` in `CacheBehavior` elements. You must create exactly one default
    cache behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_origin_id",
                "TargetOriginId",
                TypeInfo(str),
            ),
            (
                "forwarded_values",
                "ForwardedValues",
                TypeInfo(ForwardedValues),
            ),
            (
                "trusted_signers",
                "TrustedSigners",
                TypeInfo(TrustedSigners),
            ),
            (
                "viewer_protocol_policy",
                "ViewerProtocolPolicy",
                TypeInfo(typing.Union[str, ViewerProtocolPolicy]),
            ),
            (
                "min_ttl",
                "MinTTL",
                TypeInfo(int),
            ),
            (
                "allowed_methods",
                "AllowedMethods",
                TypeInfo(AllowedMethods),
            ),
            (
                "smooth_streaming",
                "SmoothStreaming",
                TypeInfo(bool),
            ),
            (
                "default_ttl",
                "DefaultTTL",
                TypeInfo(int),
            ),
            (
                "max_ttl",
                "MaxTTL",
                TypeInfo(int),
            ),
            (
                "compress",
                "Compress",
                TypeInfo(bool),
            ),
            (
                "lambda_function_associations",
                "LambdaFunctionAssociations",
                TypeInfo(LambdaFunctionAssociations),
            ),
            (
                "field_level_encryption_id",
                "FieldLevelEncryptionId",
                TypeInfo(str),
            ),
        ]

    # The value of `ID` for the origin that you want CloudFront to route requests
    # to when a request matches the path pattern either for a cache behavior or
    # for the default cache behavior in your distribution.
    target_origin_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies how CloudFront handles query strings and
    # cookies.
    forwarded_values: "ForwardedValues" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that specifies the AWS accounts, if any, that you want to
    # allow to create signed URLs for private content.

    # If you want to require signed URLs in requests for objects in the target
    # origin that match the `PathPattern` for this cache behavior, specify `true`
    # for `Enabled`, and specify the applicable values for `Quantity` and
    # `Items`. For more information, see [Serving Private Content through
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    # in the _Amazon Amazon CloudFront Developer Guide_.

    # If you don't want to require signed URLs in requests for objects that match
    # `PathPattern`, specify `false` for `Enabled` and `0` for `Quantity`. Omit
    # `Items`.

    # To add, change, or remove one or more trusted signers, change `Enabled` to
    # `true` (if it's currently `false`), change `Quantity` as applicable, and
    # specify all of the trusted signers that you want to include in the updated
    # distribution.
    trusted_signers: "TrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The protocol that viewers can use to access the files in the origin
    # specified by `TargetOriginId` when a request matches the path pattern in
    # `PathPattern`. You can specify the following options:

    #   * `allow-all`: Viewers can use HTTP or HTTPS.

    #   * `redirect-to-https`: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.

    #   * `https-only`: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

    # For more information about requiring the HTTPS protocol, see [Using an
    # HTTPS Connection to Access Your
    # Objects](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html)
    # in the _Amazon CloudFront Developer Guide_.

    # The only way to guarantee that viewers retrieve an object that was fetched
    # from the origin using HTTPS is never to use any other protocol to fetch the
    # object. If you have recently changed from HTTP to HTTPS, we recommend that
    # you clear your objects' cache because cached objects are protocol agnostic.
    # That means that an edge location will return an object from the cache
    # regardless of whether the current request protocol matches the protocol
    # used previously. For more information, see [Specifying How Long Objects and
    # Errors Stay in a CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon CloudFront Developer Guide_.
    viewer_protocol_policy: typing.Union[str, "ViewerProtocolPolicy"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The minimum amount of time that you want objects to stay in CloudFront
    # caches before CloudFront forwards another request to your origin to
    # determine whether the object has been updated. For more information, see
    # [Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon Amazon CloudFront Developer Guide_.

    # You must specify `0` for `MinTTL` if you configure CloudFront to forward
    # all headers to your origin (under `Headers`, if you specify `1` for
    # `Quantity` and `*` for `Name`).
    min_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that controls which HTTP methods CloudFront processes and
    # forwards to your Amazon S3 bucket or your custom origin. There are three
    # choices:

    #   * CloudFront forwards only `GET` and `HEAD` requests.

    #   * CloudFront forwards only `GET`, `HEAD`, and `OPTIONS` requests.

    #   * CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST`, and `DELETE` requests.

    # If you pick the third choice, you may need to restrict access to your
    # Amazon S3 bucket or to your custom origin so users can't perform operations
    # that you don't want them to. For example, you might not want users to have
    # permissions to delete objects from your origin.
    allowed_methods: "AllowedMethods" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether you want to distribute media files in the Microsoft
    # Smooth Streaming format using the origin that is associated with this cache
    # behavior. If so, specify `true`; if not, specify `false`. If you specify
    # `true` for `SmoothStreaming`, you can still distribute other content using
    # this cache behavior if the content matches the value of `PathPattern`.
    smooth_streaming: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The default amount of time that you want objects to stay in CloudFront
    # caches before CloudFront forwards another request to your origin to
    # determine whether the object has been updated. The value that you specify
    # applies only when your origin does not add HTTP headers such as `Cache-
    # Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects. For
    # more information, see [Specifying How Long Objects and Errors Stay in a
    # CloudFront Edge Cache
    # (Expiration)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
    # in the _Amazon CloudFront Developer Guide_.
    default_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )
    max_ttl: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Whether you want CloudFront to automatically compress certain files for
    # this cache behavior. If so, specify `true`; if not, specify `false`. For
    # more information, see [Serving Compressed
    # Files](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)
    # in the _Amazon CloudFront Developer Guide_.
    compress: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains zero or more Lambda function associations for
    # a cache behavior.
    lambda_function_associations: "LambdaFunctionAssociations" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of `ID` for the field-level encryption configuration that you
    # want CloudFront to use for encrypting specific fields of data for a cache
    # behavior or for the default cache behavior in your distribution.
    field_level_encryption_id: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteCloudFrontOriginAccessIdentityRequest(ShapeBase):
    """
    Deletes a origin access identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The origin access identity's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header you received from a previous `GET` or `PUT`
    # request. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDistributionRequest(ShapeBase):
    """
    This action deletes a web distribution. To delete a web distribution using the
    CloudFront API, perform the following steps.

    **To delete a web distribution using the CloudFront API:**

      1. Disable the web distribution 

      2. Submit a `GET Distribution Config` request to get the current configuration and the `Etag` header for the distribution.

      3. Update the XML document that was returned in the response to your `GET Distribution Config` request to change the value of `Enabled` to `false`.

      4. Submit a `PUT Distribution Config` request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Distribution Config` request in Step 2.

      5. Review the response to the `PUT Distribution Config` request to confirm that the distribution was successfully disabled.

      6. Submit a `GET Distribution` request to confirm that your changes have propagated. When propagation is complete, the value of `Status` is `Deployed`.

      7. Submit a `DELETE Distribution` request. Set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Distribution Config` request in Step 6.

      8. Review the response to your `DELETE Distribution` request to confirm that the distribution was successfully deleted.

    For information about deleting a distribution using the CloudFront console, see
    [Deleting a
    Distribution](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The distribution ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when you disabled the
    # distribution. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFieldLevelEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The ID of the configuration you want to delete from CloudFront.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # configuration identity to delete. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteFieldLevelEncryptionProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # Request the ID of the profile you want to delete from CloudFront.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # profile to delete. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeletePublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The ID of the public key you want to remove from CloudFront.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the public
    # key identity to delete. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteStreamingDistributionRequest(ShapeBase):
    """
    The request to delete a streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The distribution ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when you disabled the
    # streaming distribution. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Distribution(ShapeBase):
    """
    The distribution's information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "in_progress_invalidation_batches",
                "InProgressInvalidationBatches",
                TypeInfo(int),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "active_trusted_signers",
                "ActiveTrustedSigners",
                TypeInfo(ActiveTrustedSigners),
            ),
            (
                "distribution_config",
                "DistributionConfig",
                TypeInfo(DistributionConfig),
            ),
        ]

    # The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) for the distribution. For example:
    # `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where
    # `123456789012` is your AWS account ID.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This response element indicates the current status of the distribution.
    # When the status is `Deployed`, the distribution's information is fully
    # propagated to all CloudFront edge locations.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the distribution was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of invalidation batches currently in progress.
    in_progress_invalidation_batches: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name corresponding to the distribution, for example,
    # `d111111abcdef8.cloudfront.net`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # CloudFront automatically adds this element to the response only if you've
    # set up the distribution to serve private content with signed URLs. The
    # element lists the key pair IDs that CloudFront is aware of for each trusted
    # signer. The `Signer` child element lists the AWS account number of the
    # trusted signer (or an empty `Self` element if the signer is you). The
    # `Signer` element also includes the IDs of any active key pairs associated
    # with the trusted signer's AWS account. If no `KeyPairId` element appears
    # for a `Signer`, that signer can't create working signed URLs.
    active_trusted_signers: "ActiveTrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current configuration information for the distribution. Send a `GET`
    # request to the `/ _CloudFront API version_ /distribution ID/config`
    # resource.
    distribution_config: "DistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DistributionAlreadyExists(ShapeBase):
    """
    The caller reference you attempted to create the distribution with is associated
    with another distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DistributionConfig(ShapeBase):
    """
    A distribution configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "origins",
                "Origins",
                TypeInfo(Origins),
            ),
            (
                "default_cache_behavior",
                "DefaultCacheBehavior",
                TypeInfo(DefaultCacheBehavior),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(Aliases),
            ),
            (
                "default_root_object",
                "DefaultRootObject",
                TypeInfo(str),
            ),
            (
                "cache_behaviors",
                "CacheBehaviors",
                TypeInfo(CacheBehaviors),
            ),
            (
                "custom_error_responses",
                "CustomErrorResponses",
                TypeInfo(CustomErrorResponses),
            ),
            (
                "logging",
                "Logging",
                TypeInfo(LoggingConfig),
            ),
            (
                "price_class",
                "PriceClass",
                TypeInfo(typing.Union[str, PriceClass]),
            ),
            (
                "viewer_certificate",
                "ViewerCertificate",
                TypeInfo(ViewerCertificate),
            ),
            (
                "restrictions",
                "Restrictions",
                TypeInfo(Restrictions),
            ),
            (
                "web_acl_id",
                "WebACLId",
                TypeInfo(str),
            ),
            (
                "http_version",
                "HttpVersion",
                TypeInfo(typing.Union[str, HttpVersion]),
            ),
            (
                "is_ipv6_enabled",
                "IsIPV6Enabled",
                TypeInfo(bool),
            ),
        ]

    # A unique value (for example, a date-time stamp) that ensures that the
    # request can't be replayed.

    # If the value of `CallerReference` is new (regardless of the content of the
    # `DistributionConfig` object), CloudFront creates a new distribution.

    # If `CallerReference` is a value you already sent in a previous request to
    # create a distribution, and if the content of the `DistributionConfig` is
    # identical to the original request (ignoring white space), CloudFront
    # returns the same the response that it returned to the original request.

    # If `CallerReference` is a value you already sent in a previous request to
    # create a distribution but the content of the `DistributionConfig` is
    # different from the original request, CloudFront returns a
    # `DistributionAlreadyExists` error.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about origins for this
    # distribution.
    origins: "Origins" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that describes the default cache behavior if you don't
    # specify a `CacheBehavior` element or if files don't match any of the values
    # of `PathPattern` in `CacheBehavior` elements. You must create exactly one
    # default cache behavior.
    default_cache_behavior: "DefaultCacheBehavior" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Any comments you want to include about the distribution.

    # If you don't want to specify a comment, include an empty `Comment` element.

    # To delete an existing comment, update the distribution configuration and
    # include an empty `Comment` element.

    # To add or change a comment, update the distribution configuration and
    # specify the new comment.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # From this field, you can enable or disable the selected distribution.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about CNAMEs (alternate domain
    # names), if any, for this distribution.
    aliases: "Aliases" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The object that you want CloudFront to request from your origin (for
    # example, `index.html`) when a viewer requests the root URL for your
    # distribution (`http://www.example.com`) instead of an object in your
    # distribution (`http://www.example.com/product-description.html`).
    # Specifying a default root object avoids exposing the contents of your
    # distribution.

    # Specify only the object name, for example, `index.html`. Don't add a `/`
    # before the object name.

    # If you don't want to specify a default root object when you create a
    # distribution, include an empty `DefaultRootObject` element.

    # To delete the default root object from an existing distribution, update the
    # distribution configuration and include an empty `DefaultRootObject`
    # element.

    # To replace the default root object, update the distribution configuration
    # and specify the new object.

    # For more information about the default root object, see [Creating a Default
    # Root
    # Object](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html)
    # in the _Amazon CloudFront Developer Guide_.
    default_root_object: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains zero or more `CacheBehavior` elements.
    cache_behaviors: "CacheBehaviors" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that controls the following:

    #   * Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.

    #   * How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

    # For more information about custom error pages, see [Customizing Error
    # Responses](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-
    # error-pages.html) in the _Amazon CloudFront Developer Guide_.
    custom_error_responses: "CustomErrorResponses" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that controls whether access logs are written for the
    # distribution.

    # For more information about logging, see [Access
    # Logs](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)
    # in the _Amazon CloudFront Developer Guide_.
    logging: "LoggingConfig" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The price class that corresponds with the maximum price that you want to
    # pay for CloudFront service. If you specify `PriceClass_All`, CloudFront
    # responds to requests for your objects from all CloudFront edge locations.

    # If you specify a price class other than `PriceClass_All`, CloudFront serves
    # your objects from the CloudFront edge location that has the lowest latency
    # among the edge locations in your price class. Viewers who are in or near
    # regions that are excluded from your specified price class may encounter
    # slower performance.

    # For more information about price classes, see [Choosing the Price Class for
    # a CloudFront
    # Distribution](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html)
    # in the _Amazon CloudFront Developer Guide_. For information about
    # CloudFront pricing, including how price classes (such as Price Class 100)
    # map to CloudFront regions, see [Amazon CloudFront
    # Pricing](https://aws.amazon.com/cloudfront/pricing/). For price class
    # information, scroll down to see the table at the bottom of the page.
    price_class: typing.Union[str, "PriceClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that specifies the following:

    #   * Whether you want viewers to use HTTP or HTTPS to request your objects.

    #   * If you want viewers to use HTTPS, whether you're using an alternate domain name such as `example.com` or the CloudFront domain name for your distribution, such as `d111111abcdef8.cloudfront.net`.

    #   * If you're using an alternate domain name, whether AWS Certificate Manager (ACM) provided the certificate, or you purchased a certificate from a third-party certificate authority and imported it into ACM or uploaded it to the IAM certificate store.

    # You must specify only one of the following values:

    #   * ViewerCertificate$ACMCertificateArn

    #   * ViewerCertificate$IAMCertificateId

    #   * ViewerCertificate$CloudFrontDefaultCertificate

    # Don't specify `false` for `CloudFrontDefaultCertificate`.

    # **If you want viewers to use HTTP instead of HTTPS to request your
    # objects** : Specify the following value:

    # `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>`

    # In addition, specify `allow-all` for `ViewerProtocolPolicy` for all of your
    # cache behaviors.

    # **If you want viewers to use HTTPS to request your objects** : Choose the
    # type of certificate that you want to use based on whether you're using an
    # alternate domain name for your objects or the CloudFront domain name:

    #   * **If you're using an alternate domain name, such as example.com** : Specify one of the following values, depending on whether ACM provided your certificate or you purchased your certificate from third-party certificate authority:

    #     * `<ACMCertificateArn> _ARN for ACM SSL/TLS certificate_ <ACMCertificateArn>` where ` _ARN for ACM SSL/TLS certificate_ ` is the ARN for the ACM SSL/TLS certificate that you want to use for this distribution.

    #     * `<IAMCertificateId> _IAM certificate ID_ <IAMCertificateId>` where ` _IAM certificate ID_ ` is the ID that IAM returned when you added the certificate to the IAM certificate store.

    # If you specify `ACMCertificateArn` or `IAMCertificateId`, you must also
    # specify a value for `SSLSupportMethod`.

    # If you choose to use an ACM certificate or a certificate in the IAM
    # certificate store, we recommend that you use only an alternate domain name
    # in your object URLs (`https://example.com/logo.jpg`). If you use the domain
    # name that is associated with your CloudFront distribution (such as
    # `https://d111111abcdef8.cloudfront.net/logo.jpg`) and the viewer supports
    # `SNI`, then CloudFront behaves normally. However, if the browser does not
    # support SNI, the user's experience depends on the value that you choose for
    # `SSLSupportMethod`:

    #     * `vip`: The viewer displays a warning because there is a mismatch between the CloudFront domain name and the domain name in your SSL/TLS certificate.

    #     * `sni-only`: CloudFront drops the connection with the browser without returning the object.

    #   * **If you're using the CloudFront domain name for your distribution, such as`d111111abcdef8.cloudfront.net` ** : Specify the following value:

    # `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> `

    # If you want viewers to use HTTPS, you must also specify one of the
    # following values in your cache behaviors:

    #   * ` <ViewerProtocolPolicy>https-only<ViewerProtocolPolicy>`

    #   * `<ViewerProtocolPolicy>redirect-to-https<ViewerProtocolPolicy>`

    # You can also optionally require that CloudFront use HTTPS to communicate
    # with your origin by specifying one of the following values for the
    # applicable origins:

    #   * `<OriginProtocolPolicy>https-only<OriginProtocolPolicy> `

    #   * `<OriginProtocolPolicy>match-viewer<OriginProtocolPolicy> `

    # For more information, see [Using Alternate Domain Names and
    # HTTPS](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS)
    # in the _Amazon CloudFront Developer Guide_.
    viewer_certificate: "ViewerCertificate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that identifies ways in which you want to restrict
    # distribution of your content.
    restrictions: "Restrictions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A unique identifier that specifies the AWS WAF web ACL, if any, to
    # associate with this distribution.

    # AWS WAF is a web application firewall that lets you monitor the HTTP and
    # HTTPS requests that are forwarded to CloudFront, and lets you control
    # access to your content. Based on conditions that you specify, such as the
    # IP addresses that requests originate from or the values of query strings,
    # CloudFront responds to requests either with the requested content or with
    # an HTTP 403 status code (Forbidden). You can also configure CloudFront to
    # return a custom error page when a request is blocked. For more information
    # about AWS WAF, see the [AWS WAF Developer
    # Guide](http://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-
    # waf.html).
    web_acl_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) Specify the maximum HTTP version that you want viewers to use to
    # communicate with CloudFront. The default value for new web distributions is
    # http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP
    # version.

    # For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or
    # later, and must support Server Name Identification (SNI).

    # In general, configuring CloudFront to communicate with viewers using HTTP/2
    # reduces latency. You can improve performance by optimizing for HTTP/2. For
    # more information, do an Internet search for "http/2 optimization."
    http_version: typing.Union[str, "HttpVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address
    # for your distribution, specify `true`. If you specify `false`, CloudFront
    # responds to IPv6 DNS requests with the DNS response code `NOERROR` and with
    # no IP addresses. This allows viewers to submit a second request, for an
    # IPv4 address for your distribution.

    # In general, you should enable IPv6 if you have users on IPv6 networks who
    # want to access your content. However, if you're using signed URLs or signed
    # cookies to restrict access to your content, and if you're using a custom
    # policy that includes the `IpAddress` parameter to restrict the IP addresses
    # that can access your content, don't enable IPv6. If you want to restrict
    # access to some content by IP address and not restrict access to other
    # content (or restrict access but not by IP address), you can create two
    # distributions. For more information, see [Creating a Signed URL Using a
    # Custom
    # Policy](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-
    # content-creating-signed-url-custom-policy.html) in the _Amazon CloudFront
    # Developer Guide_.

    # If you're using an Amazon Route 53 alias resource record set to route
    # traffic to your CloudFront distribution, you need to create a second alias
    # resource record set when both of the following are true:

    #   * You enable IPv6 for the distribution

    #   * You're using alternate domain names in the URLs for your objects

    # For more information, see [Routing Traffic to an Amazon CloudFront Web
    # Distribution by Using Your Domain
    # Name](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-
    # cloudfront-distribution.html) in the _Amazon Route 53 Developer Guide_.

    # If you created a CNAME resource record set, either with Amazon Route 53 or
    # with another DNS service, you don't need to make any changes. A CNAME
    # record will route traffic to your distribution regardless of the IP address
    # format of the viewer request.
    is_ipv6_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DistributionConfigWithTags(ShapeBase):
    """
    A distribution Configuration and a list of tags to be associated with the
    distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_config",
                "DistributionConfig",
                TypeInfo(DistributionConfig),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(Tags),
            ),
        ]

    # A distribution configuration.
    distribution_config: "DistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains zero or more `Tag` elements.
    tags: "Tags" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DistributionList(ShapeBase):
    """
    A distribution list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[DistributionSummary]),
            ),
        ]

    # The value you provided for the `Marker` request parameter.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value you provided for the `MaxItems` request parameter.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether more distributions remain to be listed. If
    # your results were truncated, you can make a follow-up pagination request
    # using the `Marker` request parameter to retrieve more distributions in the
    # list.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of distributions that were created by the current AWS account.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `IsTruncated` is `true`, this element is present and contains the value
    # you can use for the `Marker` request parameter to continue listing your
    # distributions where they left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `DistributionSummary` element for each
    # distribution that was created by the current AWS account.
    items: typing.List["DistributionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DistributionNotDisabled(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DistributionSummary(ShapeBase):
    """
    A summary of the information about a CloudFront distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(Aliases),
            ),
            (
                "origins",
                "Origins",
                TypeInfo(Origins),
            ),
            (
                "default_cache_behavior",
                "DefaultCacheBehavior",
                TypeInfo(DefaultCacheBehavior),
            ),
            (
                "cache_behaviors",
                "CacheBehaviors",
                TypeInfo(CacheBehaviors),
            ),
            (
                "custom_error_responses",
                "CustomErrorResponses",
                TypeInfo(CustomErrorResponses),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "price_class",
                "PriceClass",
                TypeInfo(typing.Union[str, PriceClass]),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "viewer_certificate",
                "ViewerCertificate",
                TypeInfo(ViewerCertificate),
            ),
            (
                "restrictions",
                "Restrictions",
                TypeInfo(Restrictions),
            ),
            (
                "web_acl_id",
                "WebACLId",
                TypeInfo(str),
            ),
            (
                "http_version",
                "HttpVersion",
                TypeInfo(typing.Union[str, HttpVersion]),
            ),
            (
                "is_ipv6_enabled",
                "IsIPV6Enabled",
                TypeInfo(bool),
            ),
        ]

    # The identifier for the distribution. For example: `EDFDVBD632BHDS5`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) for the distribution. For example:
    # `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`, where
    # `123456789012` is your AWS account ID.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the distribution. When the status is `Deployed`, the
    # distribution's information is propagated to all CloudFront edge locations.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the distribution was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name that corresponds to the distribution, for example,
    # `d111111abcdef8.cloudfront.net`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about CNAMEs (alternate domain
    # names), if any, for this distribution.
    aliases: "Aliases" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about origins for this
    # distribution.
    origins: "Origins" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that describes the default cache behavior if you don't
    # specify a `CacheBehavior` element or if files don't match any of the values
    # of `PathPattern` in `CacheBehavior` elements. You must create exactly one
    # default cache behavior.
    default_cache_behavior: "DefaultCacheBehavior" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains zero or more `CacheBehavior` elements.
    cache_behaviors: "CacheBehaviors" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains zero or more `CustomErrorResponses` elements.
    custom_error_responses: "CustomErrorResponses" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The comment originally specified when this distribution was created.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    price_class: typing.Union[str, "PriceClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the distribution is enabled to accept user requests for content.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies the following:

    #   * Whether you want viewers to use HTTP or HTTPS to request your objects.

    #   * If you want viewers to use HTTPS, whether you're using an alternate domain name such as `example.com` or the CloudFront domain name for your distribution, such as `d111111abcdef8.cloudfront.net`.

    #   * If you're using an alternate domain name, whether AWS Certificate Manager (ACM) provided the certificate, or you purchased a certificate from a third-party certificate authority and imported it into ACM or uploaded it to the IAM certificate store.

    # You must specify only one of the following values:

    #   * ViewerCertificate$ACMCertificateArn

    #   * ViewerCertificate$IAMCertificateId

    #   * ViewerCertificate$CloudFrontDefaultCertificate

    # Don't specify `false` for `CloudFrontDefaultCertificate`.

    # **If you want viewers to use HTTP instead of HTTPS to request your
    # objects** : Specify the following value:

    # `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>`

    # In addition, specify `allow-all` for `ViewerProtocolPolicy` for all of your
    # cache behaviors.

    # **If you want viewers to use HTTPS to request your objects** : Choose the
    # type of certificate that you want to use based on whether you're using an
    # alternate domain name for your objects or the CloudFront domain name:

    #   * **If you're using an alternate domain name, such as example.com** : Specify one of the following values, depending on whether ACM provided your certificate or you purchased your certificate from third-party certificate authority:

    #     * `<ACMCertificateArn> _ARN for ACM SSL/TLS certificate_ <ACMCertificateArn>` where ` _ARN for ACM SSL/TLS certificate_ ` is the ARN for the ACM SSL/TLS certificate that you want to use for this distribution.

    #     * `<IAMCertificateId> _IAM certificate ID_ <IAMCertificateId>` where ` _IAM certificate ID_ ` is the ID that IAM returned when you added the certificate to the IAM certificate store.

    # If you specify `ACMCertificateArn` or `IAMCertificateId`, you must also
    # specify a value for `SSLSupportMethod`.

    # If you choose to use an ACM certificate or a certificate in the IAM
    # certificate store, we recommend that you use only an alternate domain name
    # in your object URLs (`https://example.com/logo.jpg`). If you use the domain
    # name that is associated with your CloudFront distribution (such as
    # `https://d111111abcdef8.cloudfront.net/logo.jpg`) and the viewer supports
    # `SNI`, then CloudFront behaves normally. However, if the browser does not
    # support SNI, the user's experience depends on the value that you choose for
    # `SSLSupportMethod`:

    #     * `vip`: The viewer displays a warning because there is a mismatch between the CloudFront domain name and the domain name in your SSL/TLS certificate.

    #     * `sni-only`: CloudFront drops the connection with the browser without returning the object.

    #   * **If you're using the CloudFront domain name for your distribution, such as`d111111abcdef8.cloudfront.net` ** : Specify the following value:

    # `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> `

    # If you want viewers to use HTTPS, you must also specify one of the
    # following values in your cache behaviors:

    #   * ` <ViewerProtocolPolicy>https-only<ViewerProtocolPolicy>`

    #   * `<ViewerProtocolPolicy>redirect-to-https<ViewerProtocolPolicy>`

    # You can also optionally require that CloudFront use HTTPS to communicate
    # with your origin by specifying one of the following values for the
    # applicable origins:

    #   * `<OriginProtocolPolicy>https-only<OriginProtocolPolicy> `

    #   * `<OriginProtocolPolicy>match-viewer<OriginProtocolPolicy> `

    # For more information, see [Using Alternate Domain Names and
    # HTTPS](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS)
    # in the _Amazon CloudFront Developer Guide_.
    viewer_certificate: "ViewerCertificate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that identifies ways in which you want to restrict
    # distribution of your content.
    restrictions: "Restrictions" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The Web ACL Id (if any) associated with the distribution.
    web_acl_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specify the maximum HTTP version that you want viewers to use to
    # communicate with CloudFront. The default value for new web distributions is
    # `http2`. Viewers that don't support `HTTP/2` will automatically use an
    # earlier version.
    http_version: typing.Union[str, "HttpVersion"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for
    # your distribution.
    is_ipv6_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class EncryptionEntities(ShapeBase):
    """
    Complex data type for field-level encryption profiles that includes all of the
    encryption entities.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[EncryptionEntity]),
            ),
        ]

    # Number of field pattern items in a field-level encryption content type-
    # profile mapping.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of field patterns in a field-level encryption content type-profile
    # mapping.
    items: typing.List["EncryptionEntity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class EncryptionEntity(ShapeBase):
    """
    Complex data type for field-level encryption profiles that includes the
    encryption key and field pattern specifications.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "public_key_id",
                "PublicKeyId",
                TypeInfo(str),
            ),
            (
                "provider_id",
                "ProviderId",
                TypeInfo(str),
            ),
            (
                "field_patterns",
                "FieldPatterns",
                TypeInfo(FieldPatterns),
            ),
        ]

    # The public key associated with a set of field-level encryption patterns, to
    # be used when encrypting the fields that match the patterns.
    public_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The provider associated with the public key being used for encryption. This
    # value must also be provided with the private key for applications to be
    # able to decrypt data.
    provider_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Field patterns in a field-level encryption content type profile specify the
    # fields that you want to be encrypted. You can provide the full field name,
    # or any beginning characters followed by a wildcard (*). You can't overlap
    # field patterns. For example, you can't have both ABC* and AB*. Note that
    # field patterns are case-sensitive.
    field_patterns: "FieldPatterns" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class EventType(str):
    viewer_request = "viewer-request"
    viewer_response = "viewer-response"
    origin_request = "origin-request"
    origin_response = "origin-response"


@dataclasses.dataclass
class FieldLevelEncryption(ShapeBase):
    """
    A complex data type that includes the profile configurations and other options
    specified for field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "field_level_encryption_config",
                "FieldLevelEncryptionConfig",
                TypeInfo(FieldLevelEncryptionConfig),
            ),
        ]

    # The configuration ID for a field-level encryption configuration which
    # includes a set of profiles that specify certain selected data fields to be
    # encrypted by specific public keys.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time the field-level encryption configuration was changed.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex data type that includes the profile configurations specified for
    # field-level encryption.
    field_level_encryption_config: "FieldLevelEncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FieldLevelEncryptionConfig(ShapeBase):
    """
    A complex data type that includes the profile configurations specified for
    field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "query_arg_profile_config",
                "QueryArgProfileConfig",
                TypeInfo(QueryArgProfileConfig),
            ),
            (
                "content_type_profile_config",
                "ContentTypeProfileConfig",
                TypeInfo(ContentTypeProfileConfig),
            ),
        ]

    # A unique number that ensures the request can't be replayed.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional comment about the configuration.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex data type that specifies when to forward content if a profile
    # isn't found and the profile that can be provided as a query argument in a
    # request.
    query_arg_profile_config: "QueryArgProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex data type that specifies when to forward content if a content
    # type isn't recognized and profiles to use as by default in a request if a
    # query argument doesn't specify a profile to use.
    content_type_profile_config: "ContentTypeProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FieldLevelEncryptionConfigAlreadyExists(ShapeBase):
    """
    The specified configuration for field-level encryption already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionConfigInUse(ShapeBase):
    """
    The specified configuration for field-level encryption is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionList(ShapeBase):
    """
    List of field-level encrpytion configurations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[FieldLevelEncryptionSummary]),
            ),
        ]

    # The maximum number of elements you want in the response body.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of field-level encryption items.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there are more elements to be listed, this element is present and
    # contains the value that you can use for the `Marker` request parameter to
    # continue listing your configurations where you left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of field-level encryption items.
    items: typing.List["FieldLevelEncryptionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FieldLevelEncryptionProfile(ShapeBase):
    """
    A complex data type for field-level encryption profiles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "field_level_encryption_profile_config",
                "FieldLevelEncryptionProfileConfig",
                TypeInfo(FieldLevelEncryptionProfileConfig),
            ),
        ]

    # The ID for a field-level encryption profile configuration which includes a
    # set of profiles that specify certain selected data fields to be encrypted
    # by specific public keys.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time the field-level encryption profile was updated.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex data type that includes the profile name and the encryption
    # entities for the field-level encryption profile.
    field_level_encryption_profile_config: "FieldLevelEncryptionProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FieldLevelEncryptionProfileAlreadyExists(ShapeBase):
    """
    The specified profile for field-level encryption already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionProfileConfig(ShapeBase):
    """
    A complex data type of profiles for the field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "encryption_entities",
                "EncryptionEntities",
                TypeInfo(EncryptionEntities),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # Profile name for the field-level encryption profile.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A unique number that ensures the request can't be replayed.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex data type of encryption entities for the field-level encryption
    # profile that include the public key ID, provider, and field patterns for
    # specifying which fields to encrypt with this key.
    encryption_entities: "EncryptionEntities" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional comment for the field-level encryption profile.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionProfileInUse(ShapeBase):
    """
    The specified profile for field-level encryption is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionProfileList(ShapeBase):
    """
    List of field-level encryption profiles.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[FieldLevelEncryptionProfileSummary]),
            ),
        ]

    # The maximum number of field-level encryption profiles you want in the
    # response body.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of field-level encryption profiles.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there are more elements to be listed, this element is present and
    # contains the value that you can use for the `Marker` request parameter to
    # continue listing your profiles where you left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The field-level encryption profile items.
    items: typing.List["FieldLevelEncryptionProfileSummary"
                      ] = dataclasses.field(
                          default=ShapeBase.NOT_SET,
                      )


@dataclasses.dataclass
class FieldLevelEncryptionProfileSizeExceeded(ShapeBase):
    """
    The maximum size of a profile for field-level encryption was exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionProfileSummary(ShapeBase):
    """
    The field-level encryption profile summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "encryption_entities",
                "EncryptionEntities",
                TypeInfo(EncryptionEntities),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # ID for the field-level encryption profile summary.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The time when the the field-level encryption profile summary was last
    # updated.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Name for the field-level encryption profile summary.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex data type of encryption entities for the field-level encryption
    # profile that include the public key ID, provider, and field patterns for
    # specifying which fields to encrypt with this key.
    encryption_entities: "EncryptionEntities" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional comment for the field-level encryption profile summary.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class FieldLevelEncryptionSummary(ShapeBase):
    """
    A summary of a field-level encryption item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "query_arg_profile_config",
                "QueryArgProfileConfig",
                TypeInfo(QueryArgProfileConfig),
            ),
            (
                "content_type_profile_config",
                "ContentTypeProfileConfig",
                TypeInfo(ContentTypeProfileConfig),
            ),
        ]

    # The unique ID of a field-level encryption item.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The last time that the summary of field-level encryption items was
    # modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An optional comment about the field-level encryption item.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A summary of a query argument-profile mapping.
    query_arg_profile_config: "QueryArgProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A summary of a content type-profile mapping.
    content_type_profile_config: "ContentTypeProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class FieldPatterns(ShapeBase):
    """
    A complex data type that includes the field patterns to match for field-level
    encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of field-level encryption field patterns.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of the field-level encryption field patterns.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class Format(str):
    URLEncoded = "URLEncoded"


@dataclasses.dataclass
class ForwardedValues(ShapeBase):
    """
    A complex type that specifies how CloudFront handles query strings and cookies.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_string",
                "QueryString",
                TypeInfo(bool),
            ),
            (
                "cookies",
                "Cookies",
                TypeInfo(CookiePreference),
            ),
            (
                "headers",
                "Headers",
                TypeInfo(Headers),
            ),
            (
                "query_string_cache_keys",
                "QueryStringCacheKeys",
                TypeInfo(QueryStringCacheKeys),
            ),
        ]

    # Indicates whether you want CloudFront to forward query strings to the
    # origin that is associated with this cache behavior and cache based on the
    # query string parameters. CloudFront behavior depends on the value of
    # `QueryString` and on the values that you specify for
    # `QueryStringCacheKeys`, if any:

    # If you specify true for `QueryString` and you don't specify any values for
    # `QueryStringCacheKeys`, CloudFront forwards all query string parameters to
    # the origin and caches based on all query string parameters. Depending on
    # how many query string parameters and values you have, this can adversely
    # affect performance because CloudFront must forward more requests to the
    # origin.

    # If you specify true for `QueryString` and you specify one or more values
    # for `QueryStringCacheKeys`, CloudFront forwards all query string parameters
    # to the origin, but it only caches based on the query string parameters that
    # you specify.

    # If you specify false for `QueryString`, CloudFront doesn't forward any
    # query string parameters to the origin, and doesn't cache based on query
    # string parameters.

    # For more information, see [Configuring CloudFront to Cache Based on Query
    # String
    # Parameters](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html)
    # in the _Amazon CloudFront Developer Guide_.
    query_string: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies whether you want CloudFront to forward
    # cookies to the origin and, if so, which ones. For more information about
    # forwarding cookies to the origin, see [How CloudFront Forwards, Caches, and
    # Logs
    # Cookies](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html)
    # in the _Amazon CloudFront Developer Guide_.
    cookies: "CookiePreference" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies the `Headers`, if any, that you want
    # CloudFront to base caching on for this cache behavior.
    headers: "Headers" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about the query string parameters
    # that you want CloudFront to use for caching for this cache behavior.
    query_string_cache_keys: "QueryStringCacheKeys" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GeoRestriction(ShapeBase):
    """
    A complex type that controls the countries in which your content is distributed.
    CloudFront determines the location of your users using `MaxMind` GeoIP
    databases.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "restriction_type",
                "RestrictionType",
                TypeInfo(typing.Union[str, GeoRestrictionType]),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The method that you want to use to restrict distribution of your content by
    # country:

    #   * `none`: No geo restriction is enabled, meaning access to content is not restricted by client geo location.

    #   * `blacklist`: The `Location` elements specify the countries in which you don't want CloudFront to distribute your content.

    #   * `whitelist`: The `Location` elements specify the countries in which you want CloudFront to distribute your content.
    restriction_type: typing.Union[str, "GeoRestrictionType"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # When geo restriction is `enabled`, this is the number of countries in your
    # `whitelist` or `blacklist`. Otherwise, when it is not enabled, `Quantity`
    # is `0`, and you can omit `Items`.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains a `Location` element for each country in which
    # you want CloudFront either to distribute your content (`whitelist`) or not
    # distribute your content (`blacklist`).

    # The `Location` element is a two-letter, uppercase country code for a
    # country that you want to include in your `blacklist` or `whitelist`.
    # Include one `Location` element for each country.

    # CloudFront and `MaxMind` both use `ISO 3166` country codes. For the current
    # list of countries and the corresponding codes, see `ISO 3166-1-alpha-2`
    # code on the _International Organization for Standardization_ website. You
    # can also refer to the country list on the CloudFront console, which
    # includes both country names and codes.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class GeoRestrictionType(str):
    blacklist = "blacklist"
    whitelist = "whitelist"
    none = "none"


@dataclasses.dataclass
class GetCloudFrontOriginAccessIdentityConfigRequest(ShapeBase):
    """
    The origin access identity's configuration information. For more information,
    see CloudFrontOriginAccessIdentityConfigComplexType.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The identity's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCloudFrontOriginAccessIdentityConfigResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cloud_front_origin_access_identity_config",
                "CloudFrontOriginAccessIdentityConfig",
                TypeInfo(CloudFrontOriginAccessIdentityConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The origin access identity's configuration information.
    cloud_front_origin_access_identity_config: "CloudFrontOriginAccessIdentityConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCloudFrontOriginAccessIdentityRequest(ShapeBase):
    """
    The request to get an origin access identity's information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The identity's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetCloudFrontOriginAccessIdentityResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cloud_front_origin_access_identity",
                "CloudFrontOriginAccessIdentity",
                TypeInfo(CloudFrontOriginAccessIdentity),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The origin access identity's information.
    cloud_front_origin_access_identity: "CloudFrontOriginAccessIdentity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the origin access identity's information. For
    # example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDistributionConfigRequest(ShapeBase):
    """
    The request to get a distribution configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The distribution's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDistributionConfigResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution_config",
                "DistributionConfig",
                TypeInfo(DistributionConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's configuration information.
    distribution_config: "DistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDistributionRequest(ShapeBase):
    """
    The request to get a distribution's information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The distribution's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution",
                "Distribution",
                TypeInfo(Distribution),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's information.
    distribution: "Distribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the distribution's information. For example:
    # `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Request the ID for the field-level encryption configuration information.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_config",
                "FieldLevelEncryptionConfig",
                TypeInfo(FieldLevelEncryptionConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the field-level encryption configuration information.
    field_level_encryption_config: "FieldLevelEncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the field level encryption configuration. For
    # example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionProfileConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Get the ID for the field-level encryption profile configuration
    # information.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionProfileConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_profile_config",
                "FieldLevelEncryptionProfileConfig",
                TypeInfo(FieldLevelEncryptionProfileConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the field-level encryption profile configuration information.
    field_level_encryption_profile_config: "FieldLevelEncryptionProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the field-level encryption profile configuration
    # result. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Get the ID for the field-level encryption profile information.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_profile",
                "FieldLevelEncryptionProfile",
                TypeInfo(FieldLevelEncryptionProfile),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the field-level encryption profile information.
    field_level_encryption_profile: "FieldLevelEncryptionProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the field level encryption profile. For example:
    # `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Request the ID for the field-level encryption configuration information.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetFieldLevelEncryptionResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption",
                "FieldLevelEncryption",
                TypeInfo(FieldLevelEncryption),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the field-level encryption configuration information.
    field_level_encryption: "FieldLevelEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the field level encryption configuration. For
    # example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInvalidationRequest(ShapeBase):
    """
    The request to get an invalidation's information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_id",
                "DistributionId",
                TypeInfo(str),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The distribution's ID.
    distribution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The identifier for the invalidation request, for example,
    # `IDFDVBD632BHDS5`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInvalidationResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invalidation",
                "Invalidation",
                TypeInfo(Invalidation),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The invalidation's information. For more information, see [Invalidation
    # Complex
    # Type](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html).
    invalidation: "Invalidation" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetPublicKeyConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Request the ID for the public key configuration.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPublicKeyConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key_config",
                "PublicKeyConfig",
                TypeInfo(PublicKeyConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the result for the public key configuration.
    public_key_config: "PublicKeyConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the public key configuration. For example:
    # `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # Request the ID for the public key.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetPublicKeyResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(PublicKey),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the public key.
    public_key: "PublicKey" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the public key. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStreamingDistributionConfigRequest(ShapeBase):
    """
    To request to get a streaming distribution configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The streaming distribution's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStreamingDistributionConfigResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution_config",
                "StreamingDistributionConfig",
                TypeInfo(StreamingDistributionConfig),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's configuration information.
    streaming_distribution_config: "StreamingDistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStreamingDistributionRequest(ShapeBase):
    """
    The request to get a streaming distribution's information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
        ]

    # The streaming distribution's ID.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStreamingDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution",
                "StreamingDistribution",
                TypeInfo(StreamingDistribution),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's information.
    streaming_distribution: "StreamingDistribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the streaming distribution's information. For
    # example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Headers(ShapeBase):
    """
    A complex type that specifies the request headers, if any, that you want
    CloudFront to base caching on for this cache behavior.

    For the headers that you specify, CloudFront caches separate versions of a
    specified object based on the header values in viewer requests. For example,
    suppose viewer requests for `logo.jpg` contain a custom `product` header that
    has a value of either `acme` or `apex`, and you configure CloudFront to cache
    your content based on values in the `product` header. CloudFront forwards the
    `product` header to the origin and caches the response from the origin once for
    each header value. For more information about caching based on header values,
    see [How CloudFront Forwards and Caches
    Headers](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-
    caching.html) in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of different headers that you want CloudFront to base caching on
    # for this cache behavior. You can configure each cache behavior in a web
    # distribution to do one of the following:

    #   * **Forward all headers to your origin** : Specify `1` for `Quantity` and `*` for `Name`.

    # CloudFront doesn't cache the objects that are associated with this cache
    # behavior. Instead, CloudFront sends every request to the origin.

    #   * **Forward a whitelist of headers you specify** : Specify the number of headers that you want CloudFront to base caching on. Then specify the header names in `Name` elements. CloudFront caches your objects based on the values in the specified headers.

    #   * **Forward only the default headers** : Specify `0` for `Quantity` and omit `Items`. In this configuration, CloudFront doesn't cache based on the values in the request headers.

    # Regardless of which option you choose, CloudFront forwards headers to your
    # origin based on whether the origin is an S3 bucket or a custom origin. See
    # the following documentation:

    #   * **S3 bucket** : See [HTTP Request Headers That CloudFront Removes or Updates](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers)

    #   * **Custom origin** : See [HTTP Request Headers and CloudFront Behavior](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-headers-behavior)
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list that contains one `Name` element for each header that you want
    # CloudFront to use for caching in this cache behavior. If `Quantity` is `0`,
    # omit `Items`.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


class HttpVersion(str):
    http1_1 = "http1.1"
    http2 = "http2"


@dataclasses.dataclass
class IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior(ShapeBase):
    """
    The specified configuration for field-level encryption can't be associated with
    the specified cache behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IllegalUpdate(ShapeBase):
    """
    Origin and `CallerReference` cannot be updated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InconsistentQuantities(ShapeBase):
    """
    The value of `Quantity` and the size of `Items` don't match.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidArgument(ShapeBase):
    """
    The argument is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidDefaultRootObject(ShapeBase):
    """
    The default root object file name is too big or contains an invalid character.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidErrorCode(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidForwardCookies(ShapeBase):
    """
    Your request contains forward cookies option which doesn't match with the
    expectation for the `whitelisted` list of cookie names. Either list of cookie
    names has been specified when not allowed or list of cookie names is missing
    when expected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidGeoRestrictionParameter(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidHeadersForS3Origin(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidIfMatchVersion(ShapeBase):
    """
    The `If-Match` version is missing or not valid for the distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLambdaFunctionAssociation(ShapeBase):
    """
    The specified Lambda function association is invalid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidLocationCode(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidMinimumProtocolVersion(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOrigin(ShapeBase):
    """
    The Amazon S3 origin server specified does not refer to a valid Amazon S3
    bucket.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOriginAccessIdentity(ShapeBase):
    """
    The origin access identity is not valid or doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOriginKeepaliveTimeout(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidOriginReadTimeout(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidProtocolSettings(ShapeBase):
    """
    You cannot specify SSLv3 as the minimum protocol version if you only want to
    support only clients that support Server Name Indication (SNI).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidQueryStringParameters(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRelativePath(ShapeBase):
    """
    The relative path is too big, is not URL-encoded, or does not begin with a slash
    (/).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRequiredProtocol(ShapeBase):
    """
    This operation requires the HTTPS protocol. Ensure that you specify the HTTPS
    protocol in your request, or omit the `RequiredProtocols` element from your
    distribution configuration.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidResponseCode(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTTLOrder(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidTagging(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidViewerCertificate(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidWebACLId(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Invalidation(ShapeBase):
    """
    An invalidation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "create_time",
                "CreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "invalidation_batch",
                "InvalidationBatch",
                TypeInfo(InvalidationBatch),
            ),
        ]

    # The identifier for the invalidation request. For example:
    # `IDFDVBD632BHDS5`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The status of the invalidation request. When the invalidation batch is
    # finished, the status is `Completed`.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the invalidation request was first made.
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current invalidation information for the batch request.
    invalidation_batch: "InvalidationBatch" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidationBatch(ShapeBase):
    """
    An invalidation batch.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "paths",
                "Paths",
                TypeInfo(Paths),
            ),
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
        ]

    # A complex type that contains information about the objects that you want to
    # invalidate. For more information, see [Specifying the Objects to
    # Invalidate](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-
    # specifying-objects) in the _Amazon CloudFront Developer Guide_.
    paths: "Paths" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A value that you specify to uniquely identify an invalidation request.
    # CloudFront uses the value to prevent you from accidentally resubmitting an
    # identical request. Whenever you create a new invalidation request, you must
    # specify a new value for `CallerReference` and change other values in the
    # request as applicable. One way to ensure that the value of
    # `CallerReference` is unique is to use a `timestamp`, for example,
    # `20120301090000`.

    # If you make a second invalidation request with the same value for
    # `CallerReference`, and if the rest of the request is the same, CloudFront
    # doesn't create a new invalidation request. Instead, CloudFront returns
    # information about the invalidation request that you previously created with
    # the same `CallerReference`.

    # If `CallerReference` is a value you already sent in a previous invalidation
    # batch request but the content of any `Path` is different from the original
    # request, CloudFront returns an `InvalidationBatchAlreadyExists` error.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidationList(ShapeBase):
    """
    The `InvalidationList` complex type describes the list of invalidation objects.
    For more information about invalidation, see [Invalidating Objects (Web
    Distributions
    Only)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[InvalidationSummary]),
            ),
        ]

    # The value that you provided for the `Marker` request parameter.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that you provided for the `MaxItems` request parameter.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether more invalidation batch requests remain to be
    # listed. If your results were truncated, you can make a follow-up pagination
    # request using the `Marker` request parameter to retrieve more invalidation
    # batches in the list.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of invalidation batches that were created by the current AWS
    # account.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `IsTruncated` is `true`, this element is present and contains the value
    # that you can use for the `Marker` request parameter to continue listing
    # your invalidation batches where they left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `InvalidationSummary` element for each
    # invalidation batch created by the current AWS account.
    items: typing.List["InvalidationSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InvalidationSummary(ShapeBase):
    """
    A summary of an invalidation request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "create_time",
                "CreateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
        ]

    # The unique ID for an invalidation request.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    create_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The status of an invalidation request.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ItemSelection(str):
    none = "none"
    whitelist = "whitelist"
    all = "all"


@dataclasses.dataclass
class KeyPairIds(ShapeBase):
    """
    A complex type that lists the active CloudFront key pairs, if any, that are
    associated with `AwsAccountNumber`.

    For more information, see ActiveTrustedSigners.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of active CloudFront key pairs for `AwsAccountNumber`.

    # For more information, see ActiveTrustedSigners.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that lists the active CloudFront key pairs, if any, that are
    # associated with `AwsAccountNumber`.

    # For more information, see ActiveTrustedSigners.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionAssociation(ShapeBase):
    """
    A complex type that contains a Lambda function association.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "lambda_function_arn",
                "LambdaFunctionARN",
                TypeInfo(str),
            ),
            (
                "event_type",
                "EventType",
                TypeInfo(typing.Union[str, EventType]),
            ),
            (
                "include_body",
                "IncludeBody",
                TypeInfo(bool),
            ),
        ]

    # The ARN of the Lambda function. You must specify the ARN of a function
    # version; you can't specify a Lambda alias or $LATEST.
    lambda_function_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the event type that triggers a Lambda function invocation. You
    # can specify the following values:

    #   * `viewer-request`: The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.

    #   * `origin-request`: The function executes only when CloudFront forwards a request to your origin. When the requested object is in the edge cache, the function doesn't execute.

    #   * `origin-response`: The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesn't execute.

    # If the origin returns an HTTP status code other than HTTP 200 (OK), the
    # function doesn't execute.

    #   * `viewer-response`: The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache.

    # If the origin returns an HTTP status code other than HTTP 200 (OK), the
    # function doesn't execute.
    event_type: typing.Union[str, "EventType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A flag that allows a Lambda function to have read access to the body
    # content. For more information, see [Accessing Body
    # Content](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)
    # in the Amazon CloudFront Developer Guide.
    include_body: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LambdaFunctionAssociations(ShapeBase):
    """
    A complex type that specifies a list of Lambda functions associations for a
    cache behavior.

    If you want to invoke one or more Lambda functions triggered by requests that
    match the `PathPattern` of the cache behavior, specify the applicable values for
    `Quantity` and `Items`. Note that there can be up to 4
    `LambdaFunctionAssociation` items in this list (one for each possible value of
    `EventType`) and each `EventType` can be associated with the Lambda function
    only once.

    If you don't want to invoke any Lambda functions for the requests that match
    `PathPattern`, specify `0` for `Quantity` and omit `Items`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[LambdaFunctionAssociation]),
            ),
        ]

    # The number of Lambda function associations for this cache behavior.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Optional** : A complex type that contains `LambdaFunctionAssociation`
    # items for this cache behavior. If `Quantity` is `0`, you can omit `Items`.
    items: typing.List["LambdaFunctionAssociation"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListCloudFrontOriginAccessIdentitiesRequest(ShapeBase):
    """
    The request to list origin access identities.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # origin access identities. The results include identities in the list that
    # occur after the marker. To get the next page of results, set the `Marker`
    # to the value of the `NextMarker` from the current page's response (which is
    # also the ID of the last identity on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of origin access identities you want in the response
    # body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListCloudFrontOriginAccessIdentitiesResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cloud_front_origin_access_identity_list",
                "CloudFrontOriginAccessIdentityList",
                TypeInfo(CloudFrontOriginAccessIdentityList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `CloudFrontOriginAccessIdentityList` type.
    cloud_front_origin_access_identity_list: "CloudFrontOriginAccessIdentityList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator[
        "ListCloudFrontOriginAccessIdentitiesResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListDistributionsByWebACLIdRequest(ShapeBase):
    """
    The request to list distributions that are associated with a specified AWS WAF
    web ACL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "web_acl_id",
                "WebACLId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # The ID of the AWS WAF web ACL that you want to list the associated
    # distributions. If you specify "null" for the ID, the request returns a list
    # of the distributions that aren't associated with a web ACL.
    web_acl_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use `Marker` and `MaxItems` to control pagination of results. If you have
    # more than `MaxItems` distributions that satisfy the request, the response
    # includes a `NextMarker` element. To get the next page of results, submit
    # another request. For the value of `Marker`, specify the value of
    # `NextMarker` from the last response. (For the first request, omit
    # `Marker`.)
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of distributions that you want CloudFront to return in
    # the response body. The maximum and default values are both 100.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDistributionsByWebACLIdResult(OutputShapeBase):
    """
    The response to a request to list the distributions that are associated with a
    specified AWS WAF web ACL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution_list",
                "DistributionList",
                TypeInfo(DistributionList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `DistributionList` type.
    distribution_list: "DistributionList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListDistributionsRequest(ShapeBase):
    """
    The request to list your distributions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # distributions. The results include distributions in the list that occur
    # after the marker. To get the next page of results, set the `Marker` to the
    # value of the `NextMarker` from the current page's response (which is also
    # the ID of the last distribution on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of distributions you want in the response body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListDistributionsResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution_list",
                "DistributionList",
                TypeInfo(DistributionList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `DistributionList` type.
    distribution_list: "DistributionList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListDistributionsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListFieldLevelEncryptionConfigsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # configurations. The results include configurations in the list that occur
    # after the marker. To get the next page of results, set the `Marker` to the
    # value of the `NextMarker` from the current page's response (which is also
    # the ID of the last configuration on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of field-level encryption configurations you want in the
    # response body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFieldLevelEncryptionConfigsResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_list",
                "FieldLevelEncryptionList",
                TypeInfo(FieldLevelEncryptionList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a list of all field-level encryption configurations that have been
    # created in CloudFront for this account.
    field_level_encryption_list: "FieldLevelEncryptionList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListFieldLevelEncryptionProfilesRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # profiles. The results include profiles in the list that occur after the
    # marker. To get the next page of results, set the `Marker` to the value of
    # the `NextMarker` from the current page's response (which is also the ID of
    # the last profile on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of field-level encryption profiles you want in the
    # response body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListFieldLevelEncryptionProfilesResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_profile_list",
                "FieldLevelEncryptionProfileList",
                TypeInfo(FieldLevelEncryptionProfileList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a list of the field-level encryption profiles that have been
    # created in CloudFront for this account.
    field_level_encryption_profile_list: "FieldLevelEncryptionProfileList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListInvalidationsRequest(ShapeBase):
    """
    The request to list invalidations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_id",
                "DistributionId",
                TypeInfo(str),
            ),
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # The distribution's ID.
    distribution_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Use this parameter when paginating results to indicate where to begin in
    # your list of invalidation batches. Because the results are returned in
    # decreasing order from most recent to oldest, the most recent results are on
    # the first page, the second page will contain earlier results, and so on. To
    # get the next page of results, set `Marker` to the value of the `NextMarker`
    # from the current page's response. This value is the same as the ID of the
    # last invalidation batch on that page.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of invalidation batches that you want in the response
    # body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListInvalidationsResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "invalidation_list",
                "InvalidationList",
                TypeInfo(InvalidationList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about invalidation batches.
    invalidation_list: "InvalidationList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self,
                ) -> typing.Generator["ListInvalidationsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListPublicKeysRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # Use this when paginating results to indicate where to begin in your list of
    # public keys. The results include public keys in the list that occur after
    # the marker. To get the next page of results, set the `Marker` to the value
    # of the `NextMarker` from the current page's response (which is also the ID
    # of the last public key on that page).
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of public keys you want in the response body.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListPublicKeysResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key_list",
                "PublicKeyList",
                TypeInfo(PublicKeyList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Returns a list of all public keys that have been added to CloudFront for
    # this account.
    public_key_list: "PublicKeyList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListStreamingDistributionsRequest(ShapeBase):
    """
    The request to list your streaming distributions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(str),
            ),
        ]

    # The value that you provided for the `Marker` request parameter.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value that you provided for the `MaxItems` request parameter.
    max_items: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListStreamingDistributionsResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution_list",
                "StreamingDistributionList",
                TypeInfo(StreamingDistributionList),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The `StreamingDistributionList` type.
    streaming_distribution_list: "StreamingDistributionList" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(
        self,
    ) -> typing.Generator["ListStreamingDistributionsResult", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsForResourceRequest(ShapeBase):
    """
    The request to list tags for a CloudFront resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
        ]

    # An ARN of a CloudFront resource.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsForResourceResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(Tags),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains zero or more `Tag` elements.
    tags: "Tags" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoggingConfig(ShapeBase):
    """
    A complex type that controls whether access logs are written for the
    distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "include_cookies",
                "IncludeCookies",
                TypeInfo(bool),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    # Specifies whether you want CloudFront to save access logs to an Amazon S3
    # bucket. If you don't want to enable logging when you create a distribution
    # or if you want to disable logging for an existing distribution, specify
    # `false` for `Enabled`, and specify empty `Bucket` and `Prefix` elements. If
    # you specify `false` for `Enabled` but you specify values for `Bucket`,
    # `prefix`, and `IncludeCookies`, the values are automatically deleted.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies whether you want CloudFront to include cookies in access logs,
    # specify `true` for `IncludeCookies`. If you choose to include cookies in
    # logs, CloudFront logs all cookies regardless of how you configure the cache
    # behaviors for this distribution. If you don't want to include cookies when
    # you create a distribution or if you want to disable include cookies for an
    # existing distribution, specify `false` for `IncludeCookies`.
    include_cookies: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 bucket to store the access logs in, for example,
    # `myawslogbucket.s3.amazonaws.com`.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional string that you want CloudFront to prefix to the access log
    # `filenames` for this distribution, for example, `myprefix/`. If you want to
    # enable logging, but you don't want to specify a prefix, you still must
    # include an empty `Prefix` element in the `Logging` element.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class Method(str):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    DELETE = "DELETE"


class MinimumProtocolVersion(str):
    SSLv3 = "SSLv3"
    TLSv1 = "TLSv1"
    TLSv1_2016 = "TLSv1_2016"
    TLSv1_1_2016 = "TLSv1.1_2016"
    TLSv1_2_2018 = "TLSv1.2_2018"


@dataclasses.dataclass
class MissingBody(ShapeBase):
    """
    This operation requires a body. Ensure that the body is present and the
    `Content-Type` header is set.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchCloudFrontOriginAccessIdentity(ShapeBase):
    """
    The specified origin access identity does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchDistribution(ShapeBase):
    """
    The specified distribution does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchFieldLevelEncryptionConfig(ShapeBase):
    """
    The specified configuration for field-level encryption doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchFieldLevelEncryptionProfile(ShapeBase):
    """
    The specified profile for field-level encryption doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchInvalidation(ShapeBase):
    """
    The specified invalidation does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchOrigin(ShapeBase):
    """
    No origin exists with the specified `Origin Id`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchPublicKey(ShapeBase):
    """
    The specified public key doesn't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchResource(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class NoSuchStreamingDistribution(ShapeBase):
    """
    The specified streaming distribution does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Origin(ShapeBase):
    """
    A complex type that describes the Amazon S3 bucket or the HTTP server (for
    example, a web server) from which CloudFront gets your files. You must create at
    least one origin.

    For the current limit on the number of origins that you can create for a
    distribution, see [Amazon CloudFront
    Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront)
    in the _AWS General Reference_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "origin_path",
                "OriginPath",
                TypeInfo(str),
            ),
            (
                "custom_headers",
                "CustomHeaders",
                TypeInfo(CustomHeaders),
            ),
            (
                "s3_origin_config",
                "S3OriginConfig",
                TypeInfo(S3OriginConfig),
            ),
            (
                "custom_origin_config",
                "CustomOriginConfig",
                TypeInfo(CustomOriginConfig),
            ),
        ]

    # A unique identifier for the origin. The value of `Id` must be unique within
    # the distribution.

    # When you specify the value of `TargetOriginId` for the default cache
    # behavior or for another cache behavior, you indicate the origin to which
    # you want the cache behavior to route requests by specifying the value of
    # the `Id` element for that origin. When a request matches the path pattern
    # for that cache behavior, CloudFront routes the request to the specified
    # origin. For more information, see [Cache Behavior
    # Settings](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-
    # web-values-specify.html#DownloadDistValuesCacheBehavior) in the _Amazon
    # CloudFront Developer Guide_.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you
    # want CloudFront to get objects for this origin, for example,
    # `myawsbucket.s3.amazonaws.com`. If you set up your bucket to be configured
    # as a website endpoint, enter the Amazon S3 static website hosting endpoint
    # for the bucket.

    # Constraints for Amazon S3 origins:

    #   * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the `s3-accelerate` endpoint for `DomainName`.

    #   * The bucket name must be between 3 and 63 characters long (inclusive).

    #   * The bucket name must contain only lowercase characters, numbers, periods, underscores, and dashes.

    #   * The bucket name must not contain adjacent periods.

    # **Custom Origins** : The DNS domain name for the HTTP server from which you
    # want CloudFront to get objects for this origin, for example,
    # `www.example.com`.

    # Constraints for custom origins:

    #   * `DomainName` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.), hyphen (-), or underscore (_) characters.

    #   * The name cannot exceed 128 characters.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional element that causes CloudFront to request your content from a
    # directory in your Amazon S3 bucket or your custom origin. When you include
    # the `OriginPath` element, specify the directory name, beginning with a `/`.
    # CloudFront appends the directory name to the value of `DomainName`, for
    # example, `example.com/production`. Do not include a `/` at the end of the
    # directory name.

    # For example, suppose you've specified the following values for your
    # distribution:

    #   * `DomainName`: An Amazon S3 bucket named `myawsbucket`.

    #   * `OriginPath`: `/production`

    #   * `CNAME`: `example.com`

    # When a user enters `example.com/index.html` in a browser, CloudFront sends
    # a request to Amazon S3 for `myawsbucket/production/index.html`.

    # When a user enters `example.com/acme/index.html` in a browser, CloudFront
    # sends a request to Amazon S3 for `myawsbucket/production/acme/index.html`.
    origin_path: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains names and values for the custom headers that
    # you want.
    custom_headers: "CustomHeaders" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about the Amazon S3 origin. If the
    # origin is a custom origin, use the `CustomOriginConfig` element instead.
    s3_origin_config: "S3OriginConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about a custom origin. If the
    # origin is an Amazon S3 bucket, use the `S3OriginConfig` element instead.
    custom_origin_config: "CustomOriginConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class OriginCustomHeader(ShapeBase):
    """
    A complex type that contains `HeaderName` and `HeaderValue` elements, if any,
    for this distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "header_name",
                "HeaderName",
                TypeInfo(str),
            ),
            (
                "header_value",
                "HeaderValue",
                TypeInfo(str),
            ),
        ]

    # The name of a header that you want CloudFront to forward to your origin.
    # For more information, see [Forwarding Custom Headers to Your Origin (Web
    # Distributions
    # Only)](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-
    # custom-headers.html) in the _Amazon Amazon CloudFront Developer Guide_.
    header_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value for the header that you specified in the `HeaderName` field.
    header_value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class OriginProtocolPolicy(str):
    http_only = "http-only"
    match_viewer = "match-viewer"
    https_only = "https-only"


@dataclasses.dataclass
class OriginSslProtocols(ShapeBase):
    """
    A complex type that contains information about the SSL/TLS protocols that
    CloudFront can use when establishing an HTTPS connection with your origin.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[typing.Union[str, SslProtocol]]),
            ),
        ]

    # The number of SSL/TLS protocols that you want to allow CloudFront to use
    # when establishing an HTTPS connection with this origin.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list that contains allowed SSL/TLS protocols for this distribution.
    items: typing.List[typing.Union[str, "SslProtocol"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Origins(ShapeBase):
    """
    A complex type that contains information about origins for this distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[Origin]),
            ),
        ]

    # The number of origins for this distribution.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains origins for this distribution.
    items: typing.List["Origin"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Paths(ShapeBase):
    """
    A complex type that contains information about the objects that you want to
    invalidate. For more information, see [Specifying the Objects to
    Invalidate](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-
    specifying-objects) in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of objects that you want to invalidate.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains a list of the paths that you want to
    # invalidate.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PreconditionFailed(ShapeBase):
    """
    The precondition given in one or more of the request-header fields evaluated to
    `false`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class PriceClass(str):
    PriceClass_100 = "PriceClass_100"
    PriceClass_200 = "PriceClass_200"
    PriceClass_All = "PriceClass_All"


@dataclasses.dataclass
class PublicKey(ShapeBase):
    """
    A complex data type of public keys you add to CloudFront to use with features
    like field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "public_key_config",
                "PublicKeyConfig",
                TypeInfo(PublicKeyConfig),
            ),
        ]

    # A unique ID assigned to a public key you've added to CloudFront.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A time you added a public key to CloudFront.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex data type for a public key you add to CloudFront to use with
    # features like field-level encryption.
    public_key_config: "PublicKeyConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PublicKeyAlreadyExists(ShapeBase):
    """
    The specified public key already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublicKeyConfig(ShapeBase):
    """
    Information about a public key you add to CloudFront to use with features like
    field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "encoded_key",
                "EncodedKey",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # A unique number that ensures the request can't be replayed.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name for a public key you add to CloudFront to use with features like
    # field-level encryption.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The encoded public key that you want to add to CloudFront to use with
    # features like field-level encryption.
    encoded_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional comment about a public key.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublicKeyInUse(ShapeBase):
    """
    The specified public key is in use.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PublicKeyList(ShapeBase):
    """
    A list of public keys you've added to CloudFront to use with features like
    field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[PublicKeySummary]),
            ),
        ]

    # The maximum number of public keys you want in the response body.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of public keys you added to CloudFront to use with features like
    # field-level encryption.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If there are more elements to be listed, this element is present and
    # contains the value that you can use for the `Marker` request parameter to
    # continue listing your public keys where you left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of information about a public key you add to CloudFront to use
    # with features like field-level encryption.
    items: typing.List["PublicKeySummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PublicKeySummary(ShapeBase):
    """
    Public key information summary.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "name",
                "Name",
                TypeInfo(str),
            ),
            (
                "created_time",
                "CreatedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "encoded_key",
                "EncodedKey",
                TypeInfo(str),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
        ]

    # ID for public key information summary.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name for public key information summary.
    name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Creation time for public key information summary.
    created_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Encoded key for public key information summary.
    encoded_key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Comment for public key information summary.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryArgProfile(ShapeBase):
    """
    Query argument-profile mapping for field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "query_arg",
                "QueryArg",
                TypeInfo(str),
            ),
            (
                "profile_id",
                "ProfileId",
                TypeInfo(str),
            ),
        ]

    # Query argument for field-level encryption query argument-profile mapping.
    query_arg: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ID of profile to use for field-level encryption query argument-profile
    # mapping
    profile_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryArgProfileConfig(ShapeBase):
    """
    Configuration for query argument-profile mapping for field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "forward_when_query_arg_profile_is_unknown",
                "ForwardWhenQueryArgProfileIsUnknown",
                TypeInfo(bool),
            ),
            (
                "query_arg_profiles",
                "QueryArgProfiles",
                TypeInfo(QueryArgProfiles),
            ),
        ]

    # Flag to set if you want a request to be forwarded to the origin even if the
    # profile specified by the field-level encryption query argument, fle-
    # profile, is unknown.
    forward_when_query_arg_profile_is_unknown: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Profiles specified for query argument-profile mapping for field-level
    # encryption.
    query_arg_profiles: "QueryArgProfiles" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueryArgProfileEmpty(ShapeBase):
    """
    No profile specified for the field-level encryption query argument.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class QueryArgProfiles(ShapeBase):
    """
    Query argument-profile mapping for field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[QueryArgProfile]),
            ),
        ]

    # Number of profiles for query argument-profile mapping for field-level
    # encryption.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of items for query argument-profile mapping for field-level
    # encryption.
    items: typing.List["QueryArgProfile"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueryStringCacheKeys(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The number of `whitelisted` query string parameters for this cache
    # behavior.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # (Optional) A list that contains the query string parameters that you want
    # CloudFront to use as a basis for caching for this cache behavior. If
    # `Quantity` is 0, you can omit `Items`.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Restrictions(ShapeBase):
    """
    A complex type that identifies ways in which you want to restrict distribution
    of your content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "geo_restriction",
                "GeoRestriction",
                TypeInfo(GeoRestriction),
            ),
        ]

    # A complex type that controls the countries in which your content is
    # distributed. CloudFront determines the location of your users using
    # `MaxMind` GeoIP databases.
    geo_restriction: "GeoRestriction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class S3Origin(ShapeBase):
    """
    A complex type that contains information about the Amazon S3 bucket from which
    you want CloudFront to get your media files for distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "origin_access_identity",
                "OriginAccessIdentity",
                TypeInfo(str),
            ),
        ]

    # The DNS name of the Amazon S3 origin.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The CloudFront origin access identity to associate with the RTMP
    # distribution. Use an origin access identity to configure the distribution
    # so that end users can only access objects in an Amazon S3 bucket through
    # CloudFront.

    # If you want end users to be able to access objects using either the
    # CloudFront URL or the Amazon S3 URL, specify an empty
    # `OriginAccessIdentity` element.

    # To delete the origin access identity from an existing distribution, update
    # the distribution configuration and include an empty `OriginAccessIdentity`
    # element.

    # To replace the origin access identity, update the distribution
    # configuration and specify the new origin access identity.

    # For more information, see [Using an Origin Access Identity to Restrict
    # Access to Your Amazon S3
    # Content](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-
    # content-restricting-access-to-s3.html) in the _Amazon Amazon CloudFront
    # Developer Guide_.
    origin_access_identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class S3OriginConfig(ShapeBase):
    """
    A complex type that contains information about the Amazon S3 origin. If the
    origin is a custom origin, use the `CustomOriginConfig` element instead.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "origin_access_identity",
                "OriginAccessIdentity",
                TypeInfo(str),
            ),
        ]

    # The CloudFront origin access identity to associate with the origin. Use an
    # origin access identity to configure the origin so that viewers can _only_
    # access objects in an Amazon S3 bucket through CloudFront. The format of the
    # value is:

    # origin-access-identity/cloudfront/ _ID-of-origin-access-identity_

    # where ` _ID-of-origin-access-identity_ ` is the value that CloudFront
    # returned in the `ID` element when you created the origin access identity.

    # If you want viewers to be able to access objects using either the
    # CloudFront URL or the Amazon S3 URL, specify an empty
    # `OriginAccessIdentity` element.

    # To delete the origin access identity from an existing distribution, update
    # the distribution configuration and include an empty `OriginAccessIdentity`
    # element.

    # To replace the origin access identity, update the distribution
    # configuration and specify the new origin access identity.

    # For more information about the origin access identity, see [Serving Private
    # Content through
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    # in the _Amazon CloudFront Developer Guide_.
    origin_access_identity: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SSLSupportMethod(str):
    sni_only = "sni-only"
    vip = "vip"


@dataclasses.dataclass
class Signer(ShapeBase):
    """
    A complex type that lists the AWS accounts that were included in the
    `TrustedSigners` complex type, as well as their active CloudFront key pair IDs,
    if any.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aws_account_number",
                "AwsAccountNumber",
                TypeInfo(str),
            ),
            (
                "key_pair_ids",
                "KeyPairIds",
                TypeInfo(KeyPairIds),
            ),
        ]

    # An AWS account that is included in the `TrustedSigners` complex type for
    # this RTMP distribution. Valid values include:

    #   * `self`, which is the AWS account used to create the distribution.

    #   * An AWS account number.
    aws_account_number: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that lists the active CloudFront key pairs, if any, that are
    # associated with `AwsAccountNumber`.
    key_pair_ids: "KeyPairIds" = dataclasses.field(default=ShapeBase.NOT_SET, )


class SslProtocol(str):
    SSLv3 = "SSLv3"
    TLSv1 = "TLSv1"
    TLSv1_1 = "TLSv1.1"
    TLSv1_2 = "TLSv1.2"


@dataclasses.dataclass
class StreamingDistribution(ShapeBase):
    """
    A streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "active_trusted_signers",
                "ActiveTrustedSigners",
                TypeInfo(ActiveTrustedSigners),
            ),
            (
                "streaming_distribution_config",
                "StreamingDistributionConfig",
                TypeInfo(StreamingDistributionConfig),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The identifier for the RTMP distribution. For example: `EGTXBD79EXAMPLE`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the RTMP distribution. When the status is `Deployed`,
    # the distribution's information is propagated to all CloudFront edge
    # locations.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The domain name that corresponds to the streaming distribution, for
    # example, `s5c39gqb8ow64r.cloudfront.net`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that lists the AWS accounts, if any, that you included in
    # the `TrustedSigners` complex type for this distribution. These are the
    # accounts that you want to allow to create signed URLs for private content.

    # The `Signer` complex type lists the AWS account number of the trusted
    # signer or `self` if the signer is the AWS account that created the
    # distribution. The `Signer` element also includes the IDs of any active
    # CloudFront key pairs that are associated with the trusted signer's AWS
    # account. If no `KeyPairId` element appears for a `Signer`, that signer
    # can't create signed URLs.

    # For more information, see [Serving Private Content through
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    # in the _Amazon CloudFront Developer Guide_.
    active_trusted_signers: "ActiveTrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current configuration information for the RTMP distribution.
    streaming_distribution_config: "StreamingDistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time that the distribution was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamingDistributionAlreadyExists(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamingDistributionConfig(ShapeBase):
    """
    The RTMP distribution's configuration information.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "caller_reference",
                "CallerReference",
                TypeInfo(str),
            ),
            (
                "s3_origin",
                "S3Origin",
                TypeInfo(S3Origin),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "trusted_signers",
                "TrustedSigners",
                TypeInfo(TrustedSigners),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(Aliases),
            ),
            (
                "logging",
                "Logging",
                TypeInfo(StreamingLoggingConfig),
            ),
            (
                "price_class",
                "PriceClass",
                TypeInfo(typing.Union[str, PriceClass]),
            ),
        ]

    # A unique number that ensures that the request can't be replayed. If the
    # `CallerReference` is new (no matter the content of the
    # `StreamingDistributionConfig` object), a new streaming distribution is
    # created. If the `CallerReference` is a value that you already sent in a
    # previous request to create a streaming distribution, and the content of the
    # `StreamingDistributionConfig` is identical to the original request
    # (ignoring white space), the response includes the same information returned
    # to the original request. If the `CallerReference` is a value that you
    # already sent in a previous request to create a streaming distribution but
    # the content of the `StreamingDistributionConfig` is different from the
    # original request, CloudFront returns a `DistributionAlreadyExists` error.
    caller_reference: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about the Amazon S3 bucket from
    # which you want CloudFront to get your media files for distribution.
    s3_origin: "S3Origin" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Any comments you want to include about the streaming distribution.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies any AWS accounts that you want to permit to
    # create signed URLs for private content. If you want the distribution to use
    # signed URLs, include this element; if you want the distribution to use
    # public URLs, remove this element. For more information, see [Serving
    # Private Content through
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    # in the _Amazon CloudFront Developer Guide_.
    trusted_signers: "TrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the streaming distribution is enabled to accept user requests for
    # content.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about CNAMEs (alternate domain
    # names), if any, for this streaming distribution.
    aliases: "Aliases" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that controls whether access logs are written for the
    # streaming distribution.
    logging: "StreamingLoggingConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains information about price class for this
    # streaming distribution.
    price_class: typing.Union[str, "PriceClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamingDistributionConfigWithTags(ShapeBase):
    """
    A streaming distribution Configuration and a list of tags to be associated with
    the streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_distribution_config",
                "StreamingDistributionConfig",
                TypeInfo(StreamingDistributionConfig),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(Tags),
            ),
        ]

    # A streaming distribution Configuration.
    streaming_distribution_config: "StreamingDistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A complex type that contains zero or more `Tag` elements.
    tags: "Tags" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamingDistributionList(ShapeBase):
    """
    A streaming distribution list.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "marker",
                "Marker",
                TypeInfo(str),
            ),
            (
                "max_items",
                "MaxItems",
                TypeInfo(int),
            ),
            (
                "is_truncated",
                "IsTruncated",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "next_marker",
                "NextMarker",
                TypeInfo(str),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[StreamingDistributionSummary]),
            ),
        ]

    # The value you provided for the `Marker` request parameter.
    marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value you provided for the `MaxItems` request parameter.
    max_items: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A flag that indicates whether more streaming distributions remain to be
    # listed. If your results were truncated, you can make a follow-up pagination
    # request using the `Marker` request parameter to retrieve more distributions
    # in the list.
    is_truncated: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of streaming distributions that were created by the current AWS
    # account.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If `IsTruncated` is `true`, this element is present and contains the value
    # you can use for the `Marker` request parameter to continue listing your
    # RTMP distributions where they left off.
    next_marker: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains one `StreamingDistributionSummary` element for
    # each distribution that was created by the current AWS account.
    items: typing.List["StreamingDistributionSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamingDistributionNotDisabled(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamingDistributionSummary(ShapeBase):
    """
    A summary of the information for an Amazon CloudFront streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "arn",
                "ARN",
                TypeInfo(str),
            ),
            (
                "status",
                "Status",
                TypeInfo(str),
            ),
            (
                "last_modified_time",
                "LastModifiedTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "domain_name",
                "DomainName",
                TypeInfo(str),
            ),
            (
                "s3_origin",
                "S3Origin",
                TypeInfo(S3Origin),
            ),
            (
                "aliases",
                "Aliases",
                TypeInfo(Aliases),
            ),
            (
                "trusted_signers",
                "TrustedSigners",
                TypeInfo(TrustedSigners),
            ),
            (
                "comment",
                "Comment",
                TypeInfo(str),
            ),
            (
                "price_class",
                "PriceClass",
                TypeInfo(typing.Union[str, PriceClass]),
            ),
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
        ]

    # The identifier for the distribution, for example, `EDFDVBD632BHDS5`.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN (Amazon Resource Name) for the streaming distribution. For example:
    # `arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`,
    # where `123456789012` is your AWS account ID.
    arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates the current status of the distribution. When the status is
    # `Deployed`, the distribution's information is fully propagated throughout
    # the Amazon CloudFront system.
    status: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The date and time the distribution was last modified.
    last_modified_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The domain name corresponding to the distribution, for example,
    # `d111111abcdef8.cloudfront.net`.
    domain_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about the Amazon S3 bucket from
    # which you want CloudFront to get your media files for distribution.
    s3_origin: "S3Origin" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains information about CNAMEs (alternate domain
    # names), if any, for this streaming distribution.
    aliases: "Aliases" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that specifies the AWS accounts, if any, that you want to
    # allow to create signed URLs for private content. If you want to require
    # signed URLs in requests for objects in the target origin that match the
    # `PathPattern` for this cache behavior, specify `true` for `Enabled`, and
    # specify the applicable values for `Quantity` and `Items`.If you don't want
    # to require signed URLs in requests for objects that match `PathPattern`,
    # specify `false` for `Enabled` and `0` for `Quantity`. Omit `Items`. To add,
    # change, or remove one or more trusted signers, change `Enabled` to `true`
    # (if it's currently `false`), change `Quantity` as applicable, and specify
    # all of the trusted signers that you want to include in the updated
    # distribution.
    trusted_signers: "TrustedSigners" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The comment originally specified when this distribution was created.
    comment: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    price_class: typing.Union[str, "PriceClass"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Whether the distribution is enabled to accept end user requests for
    # content.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StreamingLoggingConfig(ShapeBase):
    """
    A complex type that controls whether access logs are written for this streaming
    distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "bucket",
                "Bucket",
                TypeInfo(str),
            ),
            (
                "prefix",
                "Prefix",
                TypeInfo(str),
            ),
        ]

    # Specifies whether you want CloudFront to save access logs to an Amazon S3
    # bucket. If you don't want to enable logging when you create a streaming
    # distribution or if you want to disable logging for an existing streaming
    # distribution, specify `false` for `Enabled`, and specify `empty Bucket` and
    # `Prefix` elements. If you specify `false` for `Enabled` but you specify
    # values for `Bucket` and `Prefix`, the values are automatically deleted.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon S3 bucket to store the access logs in, for example,
    # `myawslogbucket.s3.amazonaws.com`.
    bucket: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional string that you want CloudFront to prefix to the access log
    # filenames for this streaming distribution, for example, `myprefix/`. If you
    # want to enable logging, but you don't want to specify a prefix, you still
    # must include an empty `Prefix` element in the `Logging` element.
    prefix: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    A complex type that contains `Tag` key and `Tag` value.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(str),
            ),
            (
                "value",
                "Value",
                TypeInfo(str),
            ),
        ]

    # A string that contains `Tag` key.

    # The string length should be between 1 and 128 characters. Valid characters
    # include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / =
    # + @`.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that contains an optional `Tag` value.

    # The string length should be between 0 and 256 characters. Valid characters
    # include `a-z`, `A-Z`, `0-9`, space, and the special characters `_ - . : / =
    # + @`.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagKeys(ShapeBase):
    """
    A complex type that contains zero or more `Tag` elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # A complex type that contains `Tag` key elements.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceRequest(ShapeBase):
    """
    The request to add tags to a CloudFront resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(Tags),
            ),
        ]

    # An ARN of a CloudFront resource.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains zero or more `Tag` elements.
    tags: "Tags" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Tags(ShapeBase):
    """
    A complex type that contains zero or more `Tag` elements.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "items",
                "Items",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # A complex type that contains `Tag` elements.
    items: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyCacheBehaviors(ShapeBase):
    """
    You cannot create more cache behaviors for the distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyCertificates(ShapeBase):
    """
    You cannot create anymore custom SSL/TLS certificates.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyCloudFrontOriginAccessIdentities(ShapeBase):
    """
    Processing your request would cause you to exceed the maximum number of origin
    access identities allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyCookieNamesInWhiteList(ShapeBase):
    """
    Your request contains more cookie names in the whitelist than are allowed per
    cache behavior.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyDistributionCNAMEs(ShapeBase):
    """
    Your request contains more CNAMEs than are allowed per distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyDistributions(ShapeBase):
    """
    Processing your request would cause you to exceed the maximum number of
    distributions allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyDistributionsAssociatedToFieldLevelEncryptionConfig(ShapeBase):
    """
    The maximum number of distributions have been associated with the specified
    configuration for field-level encryption.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyDistributionsWithLambdaAssociations(ShapeBase):
    """
    Processing your request would cause the maximum number of distributions with
    Lambda function associations per owner to be exceeded.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionConfigs(ShapeBase):
    """
    The maximum number of configurations for field-level encryption have been
    created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionContentTypeProfiles(ShapeBase):
    """
    The maximum number of content type profiles for field-level encryption have been
    created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionEncryptionEntities(ShapeBase):
    """
    The maximum number of encryption entities for field-level encryption have been
    created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionFieldPatterns(ShapeBase):
    """
    The maximum number of field patterns for field-level encryption have been
    created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionProfiles(ShapeBase):
    """
    The maximum number of profiles for field-level encryption have been created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyFieldLevelEncryptionQueryArgProfiles(ShapeBase):
    """
    The maximum number of query arg profiles for field-level encryption have been
    created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyHeadersInForwardedValues(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyInvalidationsInProgress(ShapeBase):
    """
    You have exceeded the maximum number of allowable InProgress invalidation batch
    requests, or invalidation objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyLambdaFunctionAssociations(ShapeBase):
    """
    Your request contains more Lambda function associations than are allowed per
    distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyOriginCustomHeaders(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyOrigins(ShapeBase):
    """
    You cannot create more origins for the distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyPublicKeys(ShapeBase):
    """
    The maximum number of public keys for field-level encryption have been created.
    To create a new public key, delete one of the existing keys.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyQueryStringParameters(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyStreamingDistributionCNAMEs(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyStreamingDistributions(ShapeBase):
    """
    Processing your request would cause you to exceed the maximum number of
    streaming distributions allowed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TooManyTrustedSigners(ShapeBase):
    """
    Your request contains more trusted signers than are allowed per distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedSignerDoesNotExist(ShapeBase):
    """
    One or more of your trusted signers don't exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TrustedSigners(ShapeBase):
    """
    A complex type that specifies the AWS accounts, if any, that you want to allow
    to create signed URLs for private content.

    If you want to require signed URLs in requests for objects in the target origin
    that match the `PathPattern` for this cache behavior, specify `true` for
    `Enabled`, and specify the applicable values for `Quantity` and `Items`. For
    more information, see [Serving Private Content through
    CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)
    in the _Amazon Amazon CloudFront Developer Guide_.

    If you don't want to require signed URLs in requests for objects that match
    `PathPattern`, specify `false` for `Enabled` and `0` for `Quantity`. Omit
    `Items`.

    To add, change, or remove one or more trusted signers, change `Enabled` to
    `true` (if it's currently `false`), change `Quantity` as applicable, and specify
    all of the trusted signers that you want to include in the updated distribution.

    For more information about updating the distribution configuration, see
    DistributionConfig .
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "enabled",
                "Enabled",
                TypeInfo(bool),
            ),
            (
                "quantity",
                "Quantity",
                TypeInfo(int),
            ),
            (
                "items",
                "Items",
                TypeInfo(typing.List[str]),
            ),
        ]

    # Specifies whether you want to require viewers to use signed URLs to access
    # the files specified by `PathPattern` and `TargetOriginId`.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of trusted signers for this cache behavior.
    quantity: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # **Optional** : A complex type that contains trusted signers for this cache
    # behavior. If `Quantity` is `0`, you can omit `Items`.
    items: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UntagResourceRequest(ShapeBase):
    """
    The request to remove tags from a CloudFront resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource",
                "Resource",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(TagKeys),
            ),
        ]

    # An ARN of a CloudFront resource.
    resource: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A complex type that contains zero or more `Tag` key elements.
    tag_keys: "TagKeys" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCloudFrontOriginAccessIdentityRequest(ShapeBase):
    """
    The request to update an origin access identity.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_front_origin_access_identity_config",
                "CloudFrontOriginAccessIdentityConfig",
                TypeInfo(CloudFrontOriginAccessIdentityConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The identity's configuration information.
    cloud_front_origin_access_identity_config: "CloudFrontOriginAccessIdentityConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The identity's id.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # identity's configuration. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateCloudFrontOriginAccessIdentityResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "cloud_front_origin_access_identity",
                "CloudFrontOriginAccessIdentity",
                TypeInfo(CloudFrontOriginAccessIdentity),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The origin access identity's information.
    cloud_front_origin_access_identity: "CloudFrontOriginAccessIdentity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDistributionRequest(ShapeBase):
    """
    The request to update a distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "distribution_config",
                "DistributionConfig",
                TypeInfo(DistributionConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The distribution's configuration information.
    distribution_config: "DistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's id.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # distribution's configuration. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "distribution",
                "Distribution",
                TypeInfo(Distribution),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The distribution's information.
    distribution: "Distribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFieldLevelEncryptionConfigRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_level_encryption_config",
                "FieldLevelEncryptionConfig",
                TypeInfo(FieldLevelEncryptionConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # Request to update a field-level encryption configuration.
    field_level_encryption_config: "FieldLevelEncryptionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the configuration you want to update.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # configuration identity to update. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFieldLevelEncryptionConfigResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption",
                "FieldLevelEncryption",
                TypeInfo(FieldLevelEncryption),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the results of updating the configuration.
    field_level_encryption: "FieldLevelEncryption" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The value of the `ETag` header that you received when updating the
    # configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFieldLevelEncryptionProfileRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "field_level_encryption_profile_config",
                "FieldLevelEncryptionProfileConfig",
                TypeInfo(FieldLevelEncryptionProfileConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # Request to update a field-level encryption profile.
    field_level_encryption_profile_config: "FieldLevelEncryptionProfileConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ID of the field-level encryption profile request.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # profile identity to update. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateFieldLevelEncryptionProfileResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "field_level_encryption_profile",
                "FieldLevelEncryptionProfile",
                TypeInfo(FieldLevelEncryptionProfile),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the results of updating the profile.
    field_level_encryption_profile: "FieldLevelEncryptionProfile" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The result of the field-level encryption profile request.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePublicKeyRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "public_key_config",
                "PublicKeyConfig",
                TypeInfo(PublicKeyConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # Request to update public key information.
    public_key_config: "PublicKeyConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ID of the public key to be updated.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the public
    # key to update. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdatePublicKeyResult(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "public_key",
                "PublicKey",
                TypeInfo(PublicKey),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Return the results of updating the public key.
    public_key: "PublicKey" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current version of the update public key result. For example:
    # `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStreamingDistributionRequest(ShapeBase):
    """
    The request to update a streaming distribution.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "streaming_distribution_config",
                "StreamingDistributionConfig",
                TypeInfo(StreamingDistributionConfig),
            ),
            (
                "id",
                "Id",
                TypeInfo(str),
            ),
            (
                "if_match",
                "IfMatch",
                TypeInfo(str),
            ),
        ]

    # The streaming distribution's configuration information.
    streaming_distribution_config: "StreamingDistributionConfig" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's id.
    id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the `ETag` header that you received when retrieving the
    # streaming distribution's configuration. For example: `E2QWRUHAPOMQZL`.
    if_match: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateStreamingDistributionResult(OutputShapeBase):
    """
    The returned result of the corresponding request.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "streaming_distribution",
                "StreamingDistribution",
                TypeInfo(StreamingDistribution),
            ),
            (
                "e_tag",
                "ETag",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The streaming distribution's information.
    streaming_distribution: "StreamingDistribution" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current version of the configuration. For example: `E2QWRUHAPOMQZL`.
    e_tag: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ViewerCertificate(ShapeBase):
    """
    A complex type that specifies the following:

      * Whether you want viewers to use HTTP or HTTPS to request your objects.

      * If you want viewers to use HTTPS, whether you're using an alternate domain name such as `example.com` or the CloudFront domain name for your distribution, such as `d111111abcdef8.cloudfront.net`.

      * If you're using an alternate domain name, whether AWS Certificate Manager (ACM) provided the certificate, or you purchased a certificate from a third-party certificate authority and imported it into ACM or uploaded it to the IAM certificate store.

    You must specify only one of the following values:

      * ViewerCertificate$ACMCertificateArn

      * ViewerCertificate$IAMCertificateId

      * ViewerCertificate$CloudFrontDefaultCertificate

    Don't specify `false` for `CloudFrontDefaultCertificate`.

    **If you want viewers to use HTTP instead of HTTPS to request your objects** :
    Specify the following value:

    `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>`

    In addition, specify `allow-all` for `ViewerProtocolPolicy` for all of your
    cache behaviors.

    **If you want viewers to use HTTPS to request your objects** : Choose the type
    of certificate that you want to use based on whether you're using an alternate
    domain name for your objects or the CloudFront domain name:

      * **If you're using an alternate domain name, such as example.com** : Specify one of the following values, depending on whether ACM provided your certificate or you purchased your certificate from third-party certificate authority:

        * `<ACMCertificateArn> _ARN for ACM SSL/TLS certificate_ <ACMCertificateArn>` where ` _ARN for ACM SSL/TLS certificate_ ` is the ARN for the ACM SSL/TLS certificate that you want to use for this distribution.

        * `<IAMCertificateId> _IAM certificate ID_ <IAMCertificateId>` where ` _IAM certificate ID_ ` is the ID that IAM returned when you added the certificate to the IAM certificate store.

    If you specify `ACMCertificateArn` or `IAMCertificateId`, you must also specify
    a value for `SSLSupportMethod`.

    If you choose to use an ACM certificate or a certificate in the IAM certificate
    store, we recommend that you use only an alternate domain name in your object
    URLs (`https://example.com/logo.jpg`). If you use the domain name that is
    associated with your CloudFront distribution (such as
    `https://d111111abcdef8.cloudfront.net/logo.jpg`) and the viewer supports `SNI`,
    then CloudFront behaves normally. However, if the browser does not support SNI,
    the user's experience depends on the value that you choose for
    `SSLSupportMethod`:

        * `vip`: The viewer displays a warning because there is a mismatch between the CloudFront domain name and the domain name in your SSL/TLS certificate.

        * `sni-only`: CloudFront drops the connection with the browser without returning the object.

      * **If you're using the CloudFront domain name for your distribution, such as`d111111abcdef8.cloudfront.net` ** : Specify the following value:

    `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate> `

    If you want viewers to use HTTPS, you must also specify one of the following
    values in your cache behaviors:

      * ` <ViewerProtocolPolicy>https-only<ViewerProtocolPolicy>`

      * `<ViewerProtocolPolicy>redirect-to-https<ViewerProtocolPolicy>`

    You can also optionally require that CloudFront use HTTPS to communicate with
    your origin by specifying one of the following values for the applicable
    origins:

      * `<OriginProtocolPolicy>https-only<OriginProtocolPolicy> `

      * `<OriginProtocolPolicy>match-viewer<OriginProtocolPolicy> `

    For more information, see [Using Alternate Domain Names and
    HTTPS](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS)
    in the _Amazon CloudFront Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cloud_front_default_certificate",
                "CloudFrontDefaultCertificate",
                TypeInfo(bool),
            ),
            (
                "iam_certificate_id",
                "IAMCertificateId",
                TypeInfo(str),
            ),
            (
                "acm_certificate_arn",
                "ACMCertificateArn",
                TypeInfo(str),
            ),
            (
                "ssl_support_method",
                "SSLSupportMethod",
                TypeInfo(typing.Union[str, SSLSupportMethod]),
            ),
            (
                "minimum_protocol_version",
                "MinimumProtocolVersion",
                TypeInfo(typing.Union[str, MinimumProtocolVersion]),
            ),
            (
                "certificate",
                "Certificate",
                TypeInfo(str),
            ),
            (
                "certificate_source",
                "CertificateSource",
                TypeInfo(typing.Union[str, CertificateSource]),
            ),
        ]

    # For information about how and when to use `CloudFrontDefaultCertificate`,
    # see ViewerCertificate.
    cloud_front_default_certificate: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # For information about how and when to use `IAMCertificateId`, see
    # ViewerCertificate.
    iam_certificate_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For information about how and when to use `ACMCertificateArn`, see
    # ViewerCertificate.
    acm_certificate_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If you specify a value for ViewerCertificate$ACMCertificateArn or for
    # ViewerCertificate$IAMCertificateId, you must also specify how you want
    # CloudFront to serve HTTPS requests: using a method that works for all
    # clients or one that works for most clients:

    #   * `vip`: CloudFront uses dedicated IP addresses for your content and can respond to HTTPS requests from any viewer. However, you will incur additional monthly charges.

    #   * `sni-only`: CloudFront can respond to HTTPS requests from viewers that support Server Name Indication (SNI). All modern browsers support SNI, but some browsers still in use don't support SNI. If some of your users' browsers don't support SNI, we recommend that you do one of the following:

    #     * Use the `vip` option (dedicated IP addresses) instead of `sni-only`.

    #     * Use the CloudFront SSL/TLS certificate instead of a custom certificate. This requires that you use the CloudFront domain name of your distribution in the URLs for your objects, for example, `https://d111111abcdef8.cloudfront.net/logo.png`.

    #     * If you can control which browser your users use, upgrade the browser to one that supports SNI.

    #     * Use HTTP instead of HTTPS.

    # Don't specify a value for `SSLSupportMethod` if you specified
    # `<CloudFrontDefaultCertificate>true<CloudFrontDefaultCertificate>`.

    # For more information, see [Using Alternate Domain Names and
    # HTTPS](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html#CNAMEsAndHTTPS.html)
    # in the _Amazon CloudFront Developer Guide_.
    ssl_support_method: typing.Union[str, "SSLSupportMethod"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )

    # Specify the security policy that you want CloudFront to use for HTTPS
    # connections. A security policy determines two settings:

    #   * The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers

    #   * The cipher that CloudFront uses to encrypt the content that it returns to viewers

    # On the CloudFront console, this setting is called **Security policy**.

    # We recommend that you specify `TLSv1.1_2016` unless your users are using
    # browsers or devices that do not support TLSv1.1 or later.

    # When both of the following are true, you must specify `TLSv1` or later for
    # the security policy:

    #   * You're using a custom certificate: you specified a value for `ACMCertificateArn` or for `IAMCertificateId`

    #   * You're using SNI: you specified `sni-only` for `SSLSupportMethod`

    # If you specify `true` for `CloudFrontDefaultCertificate`, CloudFront
    # automatically sets the security policy to `TLSv1` regardless of the value
    # that you specify for `MinimumProtocolVersion`.

    # For information about the relationship between the security policy that you
    # choose and the protocols and ciphers that CloudFront uses to communicate
    # with viewers, see [ Supported SSL/TLS Protocols and Ciphers for
    # Communication Between Viewers and
    # CloudFront](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-
    # connections-supported-viewer-protocols-ciphers.html#secure-connections-
    # supported-ciphers) in the _Amazon CloudFront Developer Guide_.
    minimum_protocol_version: typing.Union[str, "MinimumProtocolVersion"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # This field has been deprecated. Use one of the following fields instead:

    #   * ViewerCertificate$ACMCertificateArn

    #   * ViewerCertificate$IAMCertificateId

    #   * ViewerCertificate$CloudFrontDefaultCertificate
    certificate: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This field has been deprecated. Use one of the following fields instead:

    #   * ViewerCertificate$ACMCertificateArn

    #   * ViewerCertificate$IAMCertificateId

    #   * ViewerCertificate$CloudFrontDefaultCertificate
    certificate_source: typing.Union[str, "CertificateSource"
                                    ] = dataclasses.field(
                                        default=ShapeBase.NOT_SET,
                                    )


class ViewerProtocolPolicy(str):
    allow_all = "allow-all"
    https_only = "https-only"
    redirect_to_https = "redirect-to-https"
