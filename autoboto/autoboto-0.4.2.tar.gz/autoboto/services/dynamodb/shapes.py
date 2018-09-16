import datetime
import typing
from autoboto import ShapeBase, OutputShapeBase, TypeInfo
import botocore.response
import dataclasses


class AttributeAction(str):
    ADD = "ADD"
    PUT = "PUT"
    DELETE = "DELETE"


@dataclasses.dataclass
class AttributeDefinition(ShapeBase):
    """
    Represents an attribute for describing the key schema for the table and indexes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "attribute_type",
                "AttributeType",
                TypeInfo(typing.Union[str, ScalarAttributeType]),
            ),
        ]

    # A name for the attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The data type for the attribute, where:

    #   * `S` \- the attribute is of type String

    #   * `N` \- the attribute is of type Number

    #   * `B` \- the attribute is of type Binary
    attribute_type: typing.Union[str, "ScalarAttributeType"
                                ] = dataclasses.field(
                                    default=ShapeBase.NOT_SET,
                                )


@dataclasses.dataclass
class AttributeValue(ShapeBase):
    """
    Represents the data for an attribute.

    Each attribute value is described as a name-value pair. The name is the data
    type, and the value is the data itself.

    For more information, see [Data
    Types](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes)
    in the _Amazon DynamoDB Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "s",
                "S",
                TypeInfo(str),
            ),
            (
                "n",
                "N",
                TypeInfo(str),
            ),
            (
                "b",
                "B",
                TypeInfo(typing.Any),
            ),
            (
                "ss",
                "SS",
                TypeInfo(typing.List[str]),
            ),
            (
                "ns",
                "NS",
                TypeInfo(typing.List[str]),
            ),
            (
                "bs",
                "BS",
                TypeInfo(typing.List[typing.Any]),
            ),
            (
                "m",
                "M",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "l",
                "L",
                TypeInfo(typing.List[AttributeValue]),
            ),
            (
                "null",
                "NULL",
                TypeInfo(bool),
            ),
            (
                "bool",
                "BOOL",
                TypeInfo(bool),
            ),
        ]

    # An attribute of type String. For example:

    # `"S": "Hello"`
    s: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Number. For example:

    # `"N": "123.45"`

    # Numbers are sent across the network to DynamoDB as strings, to maximize
    # compatibility across languages and libraries. However, DynamoDB treats them
    # as number type attributes for mathematical operations.
    n: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Binary. For example:

    # `"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`
    b: typing.Any = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type String Set. For example:

    # `"SS": ["Giraffe", "Hippo" ,"Zebra"]`
    ss: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Number Set. For example:

    # `"NS": ["42.2", "-19", "7.5", "3.14"]`

    # Numbers are sent across the network to DynamoDB as strings, to maximize
    # compatibility across languages and libraries. However, DynamoDB treats them
    # as number type attributes for mathematical operations.
    ns: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Binary Set. For example:

    # `"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]`
    bs: typing.List[typing.Any] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Map. For example:

    # `"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}`
    m: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An attribute of type List. For example:

    # `"L": ["Cookies", "Coffee", 3.14159]`
    l: typing.List["AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An attribute of type Null. For example:

    # `"NULL": true`
    null: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An attribute of type Boolean. For example:

    # `"BOOL": true`
    bool: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttributeValueUpdate(ShapeBase):
    """
    For the `UpdateItem` operation, represents the attributes to be modified, the
    action to perform on each, and the new value for each.

    You cannot use `UpdateItem` to update any primary key attributes. Instead, you
    will need to delete the item, and then use `PutItem` to create a new item with
    new attributes.

    Attribute values cannot be null; string and binary type attributes must have
    lengths greater than zero; and set type attributes must not be empty. Requests
    with empty values will be rejected with a `ValidationException` exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(AttributeValue),
            ),
            (
                "action",
                "Action",
                TypeInfo(typing.Union[str, AttributeAction]),
            ),
        ]

    # Represents the data for an attribute.

    # Each attribute value is described as a name-value pair. The name is the
    # data type, and the value is the data itself.

    # For more information, see [Data
    # Types](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes)
    # in the _Amazon DynamoDB Developer Guide_.
    value: "AttributeValue" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies how to perform the update. Valid values are `PUT` (default),
    # `DELETE`, and `ADD`. The behavior depends on whether the specified primary
    # key already exists in the table.

    # **If an item with the specified _Key_ is found in the table:**

    #   * `PUT` \- Adds the specified attribute to the item. If the attribute already exists, it is replaced by the new value.

    #   * `DELETE` \- If no value is specified, the attribute and its value are removed from the item. The data type of the specified value must match the existing value's data type.

    # If a _set_ of values is specified, then those values are subtracted from
    # the old set. For example, if the attribute value was the set `[a,b,c]` and
    # the `DELETE` action specified `[a,c]`, then the final attribute value would
    # be `[b]`. Specifying an empty set is an error.

    #   * `ADD` \- If the attribute does not already exist, then the attribute and its values are added to the item. If the attribute does exist, then the behavior of `ADD` depends on the data type of the attribute:

    #     * If the existing attribute is a number, and if `Value` is also a number, then the `Value` is mathematically added to the existing attribute. If `Value` is a negative number, then it is subtracted from the existing attribute.

    # If you use `ADD` to increment or decrement a number value for an item that
    # doesn't exist before the update, DynamoDB uses 0 as the initial value.

    # In addition, if you use `ADD` to update an existing item, and intend to
    # increment or decrement an attribute value which does not yet exist,
    # DynamoDB uses `0` as the initial value. For example, suppose that the item
    # you want to update does not yet have an attribute named _itemcount_ , but
    # you decide to `ADD` the number `3` to this attribute anyway, even though it
    # currently does not exist. DynamoDB will create the _itemcount_ attribute,
    # set its initial value to `0`, and finally add `3` to it. The result will be
    # a new _itemcount_ attribute in the item, with a value of `3`.

    #     * If the existing data type is a set, and if the `Value` is also a set, then the `Value` is added to the existing set. (This is a _set_ operation, not mathematical addition.) For example, if the attribute value was the set `[1,2]`, and the `ADD` action specified `[3]`, then the final attribute value would be `[1,2,3]`. An error occurs if an Add action is specified for a set attribute and the attribute type specified does not match the existing set type.

    # Both sets must have the same primitive data type. For example, if the
    # existing data type is a set of strings, the `Value` must also be a set of
    # strings. The same holds true for number sets and binary sets.

    # This action is only valid for an existing attribute whose data type is
    # number or is a set. Do not use `ADD` for any other data types.

    # **If no item with the specified _Key_ is found:**

    #   * `PUT` \- DynamoDB creates a new item with the specified primary key, and then adds the attribute.

    #   * `DELETE` \- Nothing happens; there is no attribute to delete.

    #   * `ADD` \- DynamoDB creates an item with the supplied primary key and number (or set of numbers) for the attribute value. The only data types allowed are number and number set; no other data types can be specified.
    action: typing.Union[str, "AttributeAction"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingPolicyDescription(ShapeBase):
    """
    Represents the properties of the scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
            (
                "target_tracking_scaling_policy_configuration",
                "TargetTrackingScalingPolicyConfiguration",
                TypeInfo(
                    AutoScalingTargetTrackingScalingPolicyConfigurationDescription
                ),
            ),
        ]

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents a target tracking scaling policy configuration.
    target_tracking_scaling_policy_configuration: "AutoScalingTargetTrackingScalingPolicyConfigurationDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingPolicyUpdate(ShapeBase):
    """
    Represents the autoscaling policy to be modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_tracking_scaling_policy_configuration",
                "TargetTrackingScalingPolicyConfiguration",
                TypeInfo(
                    AutoScalingTargetTrackingScalingPolicyConfigurationUpdate
                ),
            ),
            (
                "policy_name",
                "PolicyName",
                TypeInfo(str),
            ),
        ]

    # Represents a target tracking scaling policy configuration.
    target_tracking_scaling_policy_configuration: "AutoScalingTargetTrackingScalingPolicyConfigurationUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the scaling policy.
    policy_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutoScalingSettingsDescription(ShapeBase):
    """
    Represents the autoscaling settings for a global table or global secondary
    index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_units",
                "MinimumUnits",
                TypeInfo(int),
            ),
            (
                "maximum_units",
                "MaximumUnits",
                TypeInfo(int),
            ),
            (
                "auto_scaling_disabled",
                "AutoScalingDisabled",
                TypeInfo(bool),
            ),
            (
                "auto_scaling_role_arn",
                "AutoScalingRoleArn",
                TypeInfo(str),
            ),
            (
                "scaling_policies",
                "ScalingPolicies",
                TypeInfo(typing.List[AutoScalingPolicyDescription]),
            ),
        ]

    # The minimum capacity units that a global table or global secondary index
    # should be scaled down to.
    minimum_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum capacity units that a global table or global secondary index
    # should be scaled up to.
    maximum_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Disabled autoscaling for this global table or global secondary index.
    auto_scaling_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Role ARN used for configuring autoScaling policy.
    auto_scaling_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Information about the scaling policies.
    scaling_policies: typing.List["AutoScalingPolicyDescription"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class AutoScalingSettingsUpdate(ShapeBase):
    """
    Represents the autoscaling settings to be modified for a global table or global
    secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "minimum_units",
                "MinimumUnits",
                TypeInfo(int),
            ),
            (
                "maximum_units",
                "MaximumUnits",
                TypeInfo(int),
            ),
            (
                "auto_scaling_disabled",
                "AutoScalingDisabled",
                TypeInfo(bool),
            ),
            (
                "auto_scaling_role_arn",
                "AutoScalingRoleArn",
                TypeInfo(str),
            ),
            (
                "scaling_policy_update",
                "ScalingPolicyUpdate",
                TypeInfo(AutoScalingPolicyUpdate),
            ),
        ]

    # The minimum capacity units that a global table or global secondary index
    # should be scaled down to.
    minimum_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum capacity units that a global table or global secondary index
    # should be scaled up to.
    maximum_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Disabled autoscaling for this global table or global secondary index.
    auto_scaling_disabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Role ARN used for configuring autoscaling policy.
    auto_scaling_role_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The scaling policy to apply for scaling target global table or global
    # secondary index capacity units.
    scaling_policy_update: "AutoScalingPolicyUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AutoScalingTargetTrackingScalingPolicyConfigurationDescription(ShapeBase):
    """
    Represents the properties of a target tracking scaling policy.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_value",
                "TargetValue",
                TypeInfo(float),
            ),
            (
                "disable_scale_in",
                "DisableScaleIn",
                TypeInfo(bool),
            ),
            (
                "scale_in_cooldown",
                "ScaleInCooldown",
                TypeInfo(int),
            ),
            (
                "scale_out_cooldown",
                "ScaleOutCooldown",
                TypeInfo(int),
            ),
        ]

    # The target value for the metric. The range is 8.515920e-109 to
    # 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether scale in by the target tracking policy is disabled. If
    # the value is true, scale in is disabled and the target tracking policy
    # won't remove capacity from the scalable resource. Otherwise, scale in is
    # enabled and the target tracking policy can remove capacity from the
    # scalable resource. The default value is false.
    disable_scale_in: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale in activity completes before
    # another scale in activity can start. The cooldown period is used to block
    # subsequent scale in requests until it has expired. You should scale in
    # conservatively to protect your application's availability. However, if
    # another alarm triggers a scale out policy during the cooldown period after
    # a scale-in, application autoscaling scales out your scalable target
    # immediately.
    scale_in_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale out activity completes before
    # another scale out activity can start. While the cooldown period is in
    # effect, the capacity that has been added by the previous scale out event
    # that initiated the cooldown is calculated as part of the desired capacity
    # for the next scale out. You should continuously (but not excessively) scale
    # out.
    scale_out_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(ShapeBase):
    """
    Represents the settings of a target tracking scaling policy that will be
    modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_value",
                "TargetValue",
                TypeInfo(float),
            ),
            (
                "disable_scale_in",
                "DisableScaleIn",
                TypeInfo(bool),
            ),
            (
                "scale_in_cooldown",
                "ScaleInCooldown",
                TypeInfo(int),
            ),
            (
                "scale_out_cooldown",
                "ScaleOutCooldown",
                TypeInfo(int),
            ),
        ]

    # The target value for the metric. The range is 8.515920e-109 to
    # 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
    target_value: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Indicates whether scale in by the target tracking policy is disabled. If
    # the value is true, scale in is disabled and the target tracking policy
    # won't remove capacity from the scalable resource. Otherwise, scale in is
    # enabled and the target tracking policy can remove capacity from the
    # scalable resource. The default value is false.
    disable_scale_in: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale in activity completes before
    # another scale in activity can start. The cooldown period is used to block
    # subsequent scale in requests until it has expired. You should scale in
    # conservatively to protect your application's availability. However, if
    # another alarm triggers a scale out policy during the cooldown period after
    # a scale-in, application autoscaling scales out your scalable target
    # immediately.
    scale_in_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of time, in seconds, after a scale out activity completes before
    # another scale out activity can start. While the cooldown period is in
    # effect, the capacity that has been added by the previous scale out event
    # that initiated the cooldown is calculated as part of the desired capacity
    # for the next scale out. You should continuously (but not excessively) scale
    # out.
    scale_out_cooldown: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BackupDescription(ShapeBase):
    """
    Contains the description of the backup created for the table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_details",
                "BackupDetails",
                TypeInfo(BackupDetails),
            ),
            (
                "source_table_details",
                "SourceTableDetails",
                TypeInfo(SourceTableDetails),
            ),
            (
                "source_table_feature_details",
                "SourceTableFeatureDetails",
                TypeInfo(SourceTableFeatureDetails),
            ),
        ]

    # Contains the details of the backup created for the table.
    backup_details: "BackupDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the table when the backup was created.
    source_table_details: "SourceTableDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the features enabled on the table when the backup
    # was created. For example, LSIs, GSIs, streams, TTL.
    source_table_feature_details: "SourceTableFeatureDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BackupDetails(ShapeBase):
    """
    Contains the details of the backup created for the table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
            (
                "backup_name",
                "BackupName",
                TypeInfo(str),
            ),
            (
                "backup_status",
                "BackupStatus",
                TypeInfo(typing.Union[str, BackupStatus]),
            ),
            (
                "backup_type",
                "BackupType",
                TypeInfo(typing.Union[str, BackupType]),
            ),
            (
                "backup_creation_date_time",
                "BackupCreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "backup_size_bytes",
                "BackupSizeBytes",
                TypeInfo(int),
            ),
            (
                "backup_expiry_date_time",
                "BackupExpiryDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # ARN associated with the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the requested backup.
    backup_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Backup can be in one of the following states: CREATING, ACTIVE, DELETED.
    backup_status: typing.Union[str, "BackupStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # BackupType:

    #   * `USER` \- On-demand backup created by you.

    #   * `SYSTEM` \- On-demand backup automatically created by DynamoDB.
    backup_type: typing.Union[str, "BackupType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time at which the backup was created. This is the request time of the
    # backup.
    backup_creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of the backup in bytes.
    backup_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time at which the automatic on-demand backup created by DynamoDB will
    # expire. This `SYSTEM` on-demand backup expires automatically 35 days after
    # its creation.
    backup_expiry_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BackupInUseException(ShapeBase):
    """
    There is another ongoing conflicting backup control plane operation on the
    table. The backups is either being created, deleted or restored to a table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class BackupNotFoundException(ShapeBase):
    """
    Backup not found for the given BackupARN.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class BackupStatus(str):
    CREATING = "CREATING"
    DELETED = "DELETED"
    AVAILABLE = "AVAILABLE"


@dataclasses.dataclass
class BackupSummary(ShapeBase):
    """
    Contains details for the backup.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "table_id",
                "TableId",
                TypeInfo(str),
            ),
            (
                "table_arn",
                "TableArn",
                TypeInfo(str),
            ),
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
            (
                "backup_name",
                "BackupName",
                TypeInfo(str),
            ),
            (
                "backup_creation_date_time",
                "BackupCreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "backup_expiry_date_time",
                "BackupExpiryDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "backup_status",
                "BackupStatus",
                TypeInfo(typing.Union[str, BackupStatus]),
            ),
            (
                "backup_type",
                "BackupType",
                TypeInfo(typing.Union[str, BackupType]),
            ),
            (
                "backup_size_bytes",
                "BackupSizeBytes",
                TypeInfo(int),
            ),
        ]

    # Name of the table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the table.
    table_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN associated with the table.
    table_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN associated with the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Name of the specified backup.
    backup_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Time at which the backup was created.
    backup_creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time at which the automatic on-demand backup created by DynamoDB will
    # expire. This `SYSTEM` on-demand backup expires automatically 35 days after
    # its creation.
    backup_expiry_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Backup can be in one of the following states: CREATING, ACTIVE, DELETED.
    backup_status: typing.Union[str, "BackupStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # BackupType:

    #   * `USER` \- On-demand backup created by you.

    #   * `SYSTEM` \- On-demand backup automatically created by DynamoDB.
    backup_type: typing.Union[str, "BackupType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Size of the backup in bytes.
    backup_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )


class BackupType(str):
    USER = "USER"
    SYSTEM = "SYSTEM"


class BackupTypeFilter(str):
    USER = "USER"
    SYSTEM = "SYSTEM"
    ALL = "ALL"


@dataclasses.dataclass
class BatchGetItemInput(ShapeBase):
    """
    Represents the input of a `BatchGetItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "request_items",
                "RequestItems",
                TypeInfo(typing.Dict[str, KeysAndAttributes]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
        ]

    # A map of one or more table names and, for each table, a map that describes
    # one or more items to retrieve from that table. Each table name can be used
    # only once per `BatchGetItem` request.

    # Each element in the map of items to retrieve consists of the following:

    #   * `ConsistentRead` \- If `true`, a strongly consistent read is used; if `false` (the default), an eventually consistent read is used.

    #   * `ExpressionAttributeNames` \- One or more substitution tokens for attribute names in the `ProjectionExpression` parameter. The following are some use cases for using `ExpressionAttributeNames`:

    #     * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #     * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #     * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #     * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #     * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #     * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.

    #   * `Keys` \- An array of primary key attribute values that define specific items in the table. For each primary key, you must provide _all_ of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide _both_ the partition key value and the sort key value.

    #   * `ProjectionExpression` \- A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.

    # If no attribute names are specified, then all attributes will be returned.
    # If any of the requested attributes are not found, they will not appear in
    # the result.

    # For more information, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.

    #   * `AttributesToGet` \- This is a legacy parameter. Use `ProjectionExpression` instead. For more information, see [AttributesToGet](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html) in the _Amazon DynamoDB Developer Guide_.
    request_items: typing.Dict[str, "KeysAndAttributes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )


@dataclasses.dataclass
class BatchGetItemOutput(OutputShapeBase):
    """
    Represents the output of a `BatchGetItem` operation.
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
                "responses",
                "Responses",
                TypeInfo(
                    typing.Dict[str, typing.List[typing.
                                                 Dict[str, AttributeValue]]]
                ),
            ),
            (
                "unprocessed_keys",
                "UnprocessedKeys",
                TypeInfo(typing.Dict[str, KeysAndAttributes]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(typing.List[ConsumedCapacity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of table name to a list of items. Each object in `Responses` consists
    # of a table name, along with a map of attribute data consisting of the data
    # type and attribute value.
    responses: typing.Dict[str, typing.List[typing.Dict[str, "AttributeValue"]]
                          ] = dataclasses.field(
                              default=ShapeBase.NOT_SET,
                          )

    # A map of tables and their respective keys that were not processed with the
    # current response. The `UnprocessedKeys` value is in the same form as
    # `RequestItems`, so the value can be provided directly to a subsequent
    # `BatchGetItem` operation. For more information, see `RequestItems` in the
    # Request Parameters section.

    # Each element consists of:

    #   * `Keys` \- An array of primary key attribute values that define specific items in the table.

    #   * `ProjectionExpression` \- One or more attributes to be retrieved from the table or index. By default, all attributes are returned. If a requested attribute is not found, it does not appear in the result.

    #   * `ConsistentRead` \- The consistency of a read operation. If set to `true`, then a strongly consistent read is used; otherwise, an eventually consistent read is used.

    # If there are no unprocessed keys remaining, the response contains an empty
    # `UnprocessedKeys` map.
    unprocessed_keys: typing.Dict[str, "KeysAndAttributes"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The read capacity units consumed by the entire `BatchGetItem` operation.

    # Each element consists of:

    #   * `TableName` \- The table that consumed the provisioned throughput.

    #   * `CapacityUnits` \- The total number of capacity units consumed.
    consumed_capacity: typing.List["ConsumedCapacity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class BatchWriteItemInput(ShapeBase):
    """
    Represents the input of a `BatchWriteItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "request_items",
                "RequestItems",
                TypeInfo(typing.Dict[str, typing.List[WriteRequest]]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "return_item_collection_metrics",
                "ReturnItemCollectionMetrics",
                TypeInfo(typing.Union[str, ReturnItemCollectionMetrics]),
            ),
        ]

    # A map of one or more table names and, for each table, a list of operations
    # to be performed (`DeleteRequest` or `PutRequest`). Each element in the map
    # consists of the following:

    #   * `DeleteRequest` \- Perform a `DeleteItem` operation on the specified item. The item to be deleted is identified by a `Key` subelement:

    #     * `Key` \- A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide _all_ of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for _both_ the partition key and the sort key.

    #   * `PutRequest` \- Perform a `PutItem` operation on the specified item. The item to be put is identified by an `Item` subelement:

    #     * `Item` \- A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a `ValidationException` exception.

    # If you specify any attributes that are part of an index key, then the data
    # types for those attributes must match those of the schema in the table's
    # attribute definition.
    request_items: typing.Dict[str, typing.
                               List["WriteRequest"]] = dataclasses.field(
                                   default=ShapeBase.NOT_SET,
                               )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Determines whether item collection metrics are returned. If set to `SIZE`,
    # the response includes statistics about item collections, if any, that were
    # modified during the operation are returned in the response. If set to
    # `NONE` (the default), no statistics are returned.
    return_item_collection_metrics: typing.Union[
        str, "ReturnItemCollectionMetrics"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class BatchWriteItemOutput(OutputShapeBase):
    """
    Represents the output of a `BatchWriteItem` operation.
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
                "unprocessed_items",
                "UnprocessedItems",
                TypeInfo(typing.Dict[str, typing.List[WriteRequest]]),
            ),
            (
                "item_collection_metrics",
                "ItemCollectionMetrics",
                TypeInfo(typing.Dict[str, typing.List[ItemCollectionMetrics]]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(typing.List[ConsumedCapacity]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of tables and requests against those tables that were not processed.
    # The `UnprocessedItems` value is in the same form as `RequestItems`, so you
    # can provide this value directly to a subsequent `BatchGetItem` operation.
    # For more information, see `RequestItems` in the Request Parameters section.

    # Each `UnprocessedItems` entry consists of a table name and, for that table,
    # a list of operations to perform (`DeleteRequest` or `PutRequest`).

    #   * `DeleteRequest` \- Perform a `DeleteItem` operation on the specified item. The item to be deleted is identified by a `Key` subelement:

    #     * `Key` \- A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value.

    #   * `PutRequest` \- Perform a `PutItem` operation on the specified item. The item to be put is identified by an `Item` subelement:

    #     * `Item` \- A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a `ValidationException` exception.

    # If you specify any attributes that are part of an index key, then the data
    # types for those attributes must match those of the schema in the table's
    # attribute definition.

    # If there are no unprocessed items remaining, the response contains an empty
    # `UnprocessedItems` map.
    unprocessed_items: typing.Dict[str, typing.
                                   List["WriteRequest"]] = dataclasses.field(
                                       default=ShapeBase.NOT_SET,
                                   )

    # A list of tables that were processed by `BatchWriteItem` and, for each
    # table, information about any item collections that were affected by
    # individual `DeleteItem` or `PutItem` operations.

    # Each entry consists of the following subelements:

    #   * `ItemCollectionKey` \- The partition key value of the item collection. This is the same as the partition key value of the item.

    #   * `SizeEstimateRangeGB` \- An estimate of item collection size, expressed in GB. This is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on the table. Use this estimate to measure whether a local secondary index is approaching its size limit.

    # The estimate is subject to change over time; therefore, do not rely on the
    # precision or accuracy of the estimate.
    item_collection_metrics: typing.Dict[
        str, typing.List["ItemCollectionMetrics"]] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # The capacity units consumed by the entire `BatchWriteItem` operation.

    # Each element consists of:

    #   * `TableName` \- The table that consumed the provisioned throughput.

    #   * `CapacityUnits` \- The total number of capacity units consumed.
    consumed_capacity: typing.List["ConsumedCapacity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class BinaryAttributeValue(botocore.response.StreamingBody):
    pass


@dataclasses.dataclass
class Capacity(ShapeBase):
    """
    Represents the amount of provisioned throughput capacity consumed on a table or
    an index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "capacity_units",
                "CapacityUnits",
                TypeInfo(float),
            ),
        ]

    # The total number of capacity units consumed on a table or an index.
    capacity_units: float = dataclasses.field(default=ShapeBase.NOT_SET, )


class ComparisonOperator(str):
    EQ = "EQ"
    NE = "NE"
    IN = "IN"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"
    BETWEEN = "BETWEEN"
    NOT_NULL = "NOT_NULL"
    NULL = "NULL"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    BEGINS_WITH = "BEGINS_WITH"


@dataclasses.dataclass
class Condition(ShapeBase):
    """
    Represents the selection criteria for a `Query` or `Scan` operation:

      * For a `Query` operation, `Condition` is used for specifying the `KeyConditions` to use when querying a table or an index. For `KeyConditions`, only the following comparison operators are supported:

    `EQ | LE | LT | GE | GT | BEGINS_WITH | BETWEEN`

    `Condition` is also used in a `QueryFilter`, which evaluates the query results
    and returns only the desired values.

      * For a `Scan` operation, `Condition` is used in a `ScanFilter`, which evaluates the scan results and returns only the desired values.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "attribute_value_list",
                "AttributeValueList",
                TypeInfo(typing.List[AttributeValue]),
            ),
        ]

    # A comparator for evaluating attributes. For example, equals, greater than,
    # less than, etc.

    # The following comparison operators are available:

    # `EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS |
    # BEGINS_WITH | IN | BETWEEN`

    # The following are descriptions of each comparison operator.

    #   * `EQ` : Equal. `EQ` is supported for all data types, including lists and maps.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, Binary, String Set, Number Set, or Binary Set. If an item
    # contains an `AttributeValue` element of a different type than the one
    # provided in the request, the value does not match. For example, `{"S":"6"}`
    # does not equal `{"N":"6"}`. Also, `{"N":"6"}` does not equal `{"NS":["6",
    # "2", "1"]}`.

    #   * `NE` : Not equal. `NE` is supported for all data types, including lists and maps.

    # `AttributeValueList` can contain only one `AttributeValue` of type String,
    # Number, Binary, String Set, Number Set, or Binary Set. If an item contains
    # an `AttributeValue` of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}`.

    #   * `LE` : Less than or equal.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `LT` : Less than.

    # `AttributeValueList` can contain only one `AttributeValue` of type String,
    # Number, or Binary (not a set type). If an item contains an `AttributeValue`
    # element of a different type than the one provided in the request, the value
    # does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}`. Also,
    # `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}`.

    #   * `GE` : Greater than or equal.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `GT` : Greater than.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `NOT_NULL` : The attribute exists. `NOT_NULL` is supported for all data types, including lists and maps.

    # This operator tests for the existence of an attribute, not its data type.
    # If the data type of attribute "`a`" is null, and you evaluate it using
    # `NOT_NULL`, the result is a Boolean `true`. This result is because the
    # attribute "`a`" exists; its data type is not relevant to the `NOT_NULL`
    # comparison operator.

    #   * `NULL` : The attribute does not exist. `NULL` is supported for all data types, including lists and maps.

    # This operator tests for the nonexistence of an attribute, not its data
    # type. If the data type of attribute "`a`" is null, and you evaluate it
    # using `NULL`, the result is a Boolean `false`. This is because the
    # attribute "`a`" exists; its data type is not relevant to the `NULL`
    # comparison operator.

    #   * `CONTAINS` : Checks for a subsequence, or value in a set.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If the target attribute of the
    # comparison is of type String, then the operator checks for a substring
    # match. If the target attribute of the comparison is of type Binary, then
    # the operator looks for a subsequence of the target that matches the input.
    # If the target attribute of the comparison is a set ("`SS`", "`NS`", or
    # "`BS`"), then the operator evaluates to true if it finds an exact match
    # with any member of the set.

    # CONTAINS is supported for lists: When evaluating "`a CONTAINS b`", "`a`"
    # can be a list; however, "`b`" cannot be a set, a map, or a list.

    #   * `NOT_CONTAINS` : Checks for absence of a subsequence, or absence of a value in a set.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If the target attribute of the
    # comparison is a String, then the operator checks for the absence of a
    # substring match. If the target attribute of the comparison is Binary, then
    # the operator checks for the absence of a subsequence of the target that
    # matches the input. If the target attribute of the comparison is a set
    # ("`SS`", "`NS`", or "`BS`"), then the operator evaluates to true if it
    # _does not_ find an exact match with any member of the set.

    # NOT_CONTAINS is supported for lists: When evaluating "`a NOT CONTAINS b`",
    # "`a`" can be a list; however, "`b`" cannot be a set, a map, or a list.

    #   * `BEGINS_WITH` : Checks for a prefix.

    # `AttributeValueList` can contain only one `AttributeValue` of type String
    # or Binary (not a Number or a set type). The target attribute of the
    # comparison must be of type String or Binary (not a Number or a set type).

    #   * `IN` : Checks for matching elements in a list.

    # `AttributeValueList` can contain one or more `AttributeValue` elements of
    # type String, Number, or Binary. These attributes are compared against an
    # existing attribute of an item. If any elements of the input are equal to
    # the item attribute, the expression evaluates to true.

    #   * `BETWEEN` : Greater than or equal to the first value, and less than or equal to the second value.

    # `AttributeValueList` must contain two `AttributeValue` elements of the same
    # type, either String, Number, or Binary (not a set type). A target attribute
    # matches if the target value is greater than, or equal to, the first element
    # and less than, or equal to, the second element. If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not
    # compare to `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6",
    # "2", "1"]}`

    # For usage examples of `AttributeValueList` and `ComparisonOperator`, see
    # [Legacy Conditional
    # Parameters](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html)
    # in the _Amazon DynamoDB Developer Guide_.
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # One or more values to evaluate against the supplied attribute. The number
    # of values in the list depends on the `ComparisonOperator` being used.

    # For type Number, value comparisons are numeric.

    # String value comparisons for greater than, equals, or less than are based
    # on ASCII character code values. For example, `a` is greater than `A`, and
    # `a` is greater than `B`. For a list of code values, see
    # <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>.

    # For Binary, DynamoDB treats each byte of the binary data as unsigned when
    # it compares binary values.
    attribute_value_list: typing.List["AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ConditionalCheckFailedException(ShapeBase):
    """
    A condition specified in the operation could not be evaluated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The conditional request failed.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class ConditionalOperator(str):
    AND = "AND"
    OR = "OR"


@dataclasses.dataclass
class ConsumedCapacity(ShapeBase):
    """
    The capacity units consumed by an operation. The data returned includes the
    total provisioned throughput consumed, along with statistics for the table and
    any indexes involved in the operation. `ConsumedCapacity` is only returned if
    the request asked for it. For more information, see [Provisioned
    Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    in the _Amazon DynamoDB Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "capacity_units",
                "CapacityUnits",
                TypeInfo(float),
            ),
            (
                "table",
                "Table",
                TypeInfo(Capacity),
            ),
            (
                "local_secondary_indexes",
                "LocalSecondaryIndexes",
                TypeInfo(typing.Dict[str, Capacity]),
            ),
            (
                "global_secondary_indexes",
                "GlobalSecondaryIndexes",
                TypeInfo(typing.Dict[str, Capacity]),
            ),
        ]

    # The name of the table that was affected by the operation.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total number of capacity units consumed by the operation.
    capacity_units: float = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of throughput consumed on the table affected by the operation.
    table: "Capacity" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The amount of throughput consumed on each local index affected by the
    # operation.
    local_secondary_indexes: typing.Dict[str, "Capacity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The amount of throughput consumed on each global index affected by the
    # operation.
    global_secondary_indexes: typing.Dict[str, "Capacity"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ContinuousBackupsDescription(ShapeBase):
    """
    Represents the continuous backups and point in time recovery settings on the
    table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "continuous_backups_status",
                "ContinuousBackupsStatus",
                TypeInfo(typing.Union[str, ContinuousBackupsStatus]),
            ),
            (
                "point_in_time_recovery_description",
                "PointInTimeRecoveryDescription",
                TypeInfo(PointInTimeRecoveryDescription),
            ),
        ]

    # `ContinuousBackupsStatus` can be one of the following states: ENABLED,
    # DISABLED
    continuous_backups_status: typing.Union[str, "ContinuousBackupsStatus"
                                           ] = dataclasses.field(
                                               default=ShapeBase.NOT_SET,
                                           )

    # The description of the point in time recovery settings applied to the
    # table.
    point_in_time_recovery_description: "PointInTimeRecoveryDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ContinuousBackupsStatus(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class ContinuousBackupsUnavailableException(ShapeBase):
    """
    Backups have not yet been enabled for this table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBackupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "backup_name",
                "BackupName",
                TypeInfo(str),
            ),
        ]

    # The name of the table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specified name for the backup.
    backup_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateBackupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backup_details",
                "BackupDetails",
                TypeInfo(BackupDetails),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the backup created for the table.
    backup_details: "BackupDetails" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGlobalSecondaryIndexAction(ShapeBase):
    """
    Represents a new global secondary index to be added to an existing table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
        ]

    # The name of the global secondary index to be created.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The key schema for the global secondary index.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into an
    # index. These are in addition to the primary key attributes and index key
    # attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the provisioned throughput settings for the specified global
    # secondary index.

    # For current minimum and maximum provisioned throughput values, see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGlobalTableInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(typing.List[Replica]),
            ),
        ]

    # The global table name.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The regions where the global table needs to be created.
    replication_group: typing.List["Replica"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateGlobalTableOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_table_description",
                "GlobalTableDescription",
                TypeInfo(GlobalTableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the global table.
    global_table_description: "GlobalTableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateReplicaAction(ShapeBase):
    """
    Represents a replica to be added.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
        ]

    # The region of the replica to be added.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateTableInput(ShapeBase):
    """
    Represents the input of a `CreateTable` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_definitions",
                "AttributeDefinitions",
                TypeInfo(typing.List[AttributeDefinition]),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
            (
                "local_secondary_indexes",
                "LocalSecondaryIndexes",
                TypeInfo(typing.List[LocalSecondaryIndex]),
            ),
            (
                "global_secondary_indexes",
                "GlobalSecondaryIndexes",
                TypeInfo(typing.List[GlobalSecondaryIndex]),
            ),
            (
                "stream_specification",
                "StreamSpecification",
                TypeInfo(StreamSpecification),
            ),
            (
                "sse_specification",
                "SSESpecification",
                TypeInfo(SSESpecification),
            ),
        ]

    # An array of attributes that describe the key schema for the table and
    # indexes.
    attribute_definitions: typing.List["AttributeDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The name of the table to create.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Specifies the attributes that make up the primary key for a table or an
    # index. The attributes in `KeySchema` must also be defined in the
    # `AttributeDefinitions` array. For more information, see [Data
    # Model](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html)
    # in the _Amazon DynamoDB Developer Guide_.

    # Each `KeySchemaElement` in the array is composed of:

    #   * `AttributeName` \- The name of this key attribute.

    #   * `KeyType` \- The role that the key attribute will assume:

    #     * `HASH` \- partition key

    #     * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.

    # For a simple primary key (partition key), you must provide exactly one
    # element with a `KeyType` of `HASH`.

    # For a composite primary key (partition key and sort key), you must provide
    # exactly two elements, in this order: The first element must have a
    # `KeyType` of `HASH`, and the second element must have a `KeyType` of
    # `RANGE`.

    # For more information, see [Specifying the Primary
    # Key](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#WorkingWithTables.primary.key)
    # in the _Amazon DynamoDB Developer Guide_.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the provisioned throughput settings for a specified table or
    # index. The settings can be modified using the `UpdateTable` operation.

    # For current minimum and maximum provisioned throughput values, see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more local secondary indexes (the maximum is five) to be created on
    # the table. Each index is scoped to a given partition key value. There is a
    # 10 GB size limit per partition key value; otherwise, the size of a local
    # secondary index is unconstrained.

    # Each local secondary index in the array includes the following:

    #   * `IndexName` \- The name of the local secondary index. Must be unique only for this table.

    #   * `KeySchema` \- Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table.

    #   * `Projection` \- Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:

    #     * `ProjectionType` \- One of the following:

    #       * `KEYS_ONLY` \- Only the index and primary keys are projected into the index.

    #       * `INCLUDE` \- Only the specified table attributes are projected into the index. The list of projected attributes are in `NonKeyAttributes`.

    #       * `ALL` \- All of the table attributes are projected into the index.

    #     * `NonKeyAttributes` \- A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.
    local_secondary_indexes: typing.List["LocalSecondaryIndex"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # One or more global secondary indexes (the maximum is five) to be created on
    # the table. Each global secondary index in the array includes the following:

    #   * `IndexName` \- The name of the global secondary index. Must be unique only for this table.

    #   * `KeySchema` \- Specifies the key schema for the global secondary index.

    #   * `Projection` \- Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:

    #     * `ProjectionType` \- One of the following:

    #       * `KEYS_ONLY` \- Only the index and primary keys are projected into the index.

    #       * `INCLUDE` \- Only the specified table attributes are projected into the index. The list of projected attributes are in `NonKeyAttributes`.

    #       * `ALL` \- All of the table attributes are projected into the index.

    #     * `NonKeyAttributes` \- A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

    #   * `ProvisionedThroughput` \- The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.
    global_secondary_indexes: typing.List["GlobalSecondaryIndex"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The settings for DynamoDB Streams on the table. These settings consist of:

    #   * `StreamEnabled` \- Indicates whether Streams is to be enabled (true) or disabled (false).

    #   * `StreamViewType` \- When an item in the table is modified, `StreamViewType` determines what information is written to the table's stream. Valid values for `StreamViewType` are:

    #     * `KEYS_ONLY` \- Only the key attributes of the modified item are written to the stream.

    #     * `NEW_IMAGE` \- The entire item, as it appears after it was modified, is written to the stream.

    #     * `OLD_IMAGE` \- The entire item, as it appeared before it was modified, is written to the stream.

    #     * `NEW_AND_OLD_IMAGES` \- Both the new and the old item images of the item are written to the stream.
    stream_specification: "StreamSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the settings used to enable server-side encryption.
    sse_specification: "SSESpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateTableOutput(OutputShapeBase):
    """
    Represents the output of a `CreateTable` operation.
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
                "table_description",
                "TableDescription",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the properties of the table.
    table_description: "TableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteBackupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN associated with the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteBackupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backup_description",
                "BackupDescription",
                TypeInfo(BackupDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the description of the backup created for the table.
    backup_description: "BackupDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteGlobalSecondaryIndexAction(ShapeBase):
    """
    Represents a global secondary index to be deleted from an existing table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
        ]

    # The name of the global secondary index to be deleted.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteItemInput(ShapeBase):
    """
    Represents the input of a `DeleteItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "expected",
                "Expected",
                TypeInfo(typing.Dict[str, ExpectedAttributeValue]),
            ),
            (
                "conditional_operator",
                "ConditionalOperator",
                TypeInfo(typing.Union[str, ConditionalOperator]),
            ),
            (
                "return_values",
                "ReturnValues",
                TypeInfo(typing.Union[str, ReturnValue]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "return_item_collection_metrics",
                "ReturnItemCollectionMetrics",
                TypeInfo(typing.Union[str, ReturnItemCollectionMetrics]),
            ),
            (
                "condition_expression",
                "ConditionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expression_attribute_values",
                "ExpressionAttributeValues",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # The name of the table from which to delete the item.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of attribute names to `AttributeValue` objects, representing the
    # primary key of the item to delete.

    # For the primary key, you must provide all of the attributes. For example,
    # with a simple primary key, you only need to provide a value for the
    # partition key. For a composite primary key, you must provide values for
    # both the partition key and the sort key.
    key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [Expected](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expected: typing.Dict[str, "ExpectedAttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [ConditionalOperator](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html)
    # in the _Amazon DynamoDB Developer Guide_.
    conditional_operator: typing.Union[str, "ConditionalOperator"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use `ReturnValues` if you want to get the item attributes as they appeared
    # before they were deleted. For `DeleteItem`, the valid values are:

    #   * `NONE` \- If `ReturnValues` is not specified, or if its value is `NONE`, then nothing is returned. (This setting is the default for `ReturnValues`.)

    #   * `ALL_OLD` \- The content of the old item is returned.

    # The `ReturnValues` parameter is used by several DynamoDB operations;
    # however, `DeleteItem` does not recognize any values other than `NONE` or
    # `ALL_OLD`.
    return_values: typing.Union[str, "ReturnValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Determines whether item collection metrics are returned. If set to `SIZE`,
    # the response includes statistics about item collections, if any, that were
    # modified during the operation are returned in the response. If set to
    # `NONE` (the default), no statistics are returned.
    return_item_collection_metrics: typing.Union[
        str, "ReturnItemCollectionMetrics"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # A condition that must be satisfied in order for a conditional `DeleteItem`
    # to succeed.

    # An expression can contain any of the following:

    #   * Functions: `attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size`

    # These function names are case-sensitive.

    #   * Comparison operators: `= | <> | < | > | <= | >= | BETWEEN | IN `

    #   * Logical operators: `AND | OR | NOT`

    # For more information on condition expressions, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    condition_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more values that can be substituted in an expression.

    # Use the **:** (colon) character in an expression to dereference an
    # attribute value. For example, suppose that you wanted to check whether the
    # value of the _ProductStatus_ attribute was one of the following:

    # `Available | Backordered | Discontinued`

    # You would first need to specify `ExpressionAttributeValues` as follows:

    # `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"},
    # ":disc":{"S":"Discontinued"} }`

    # You could then use these values in an expression, such as this:

    # `ProductStatus IN (:avail, :back, :disc)`

    # For more information on expression attribute values, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_values: typing.Dict[str, "AttributeValue"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class DeleteItemOutput(OutputShapeBase):
    """
    Represents the output of a `DeleteItem` operation.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
            (
                "item_collection_metrics",
                "ItemCollectionMetrics",
                TypeInfo(ItemCollectionMetrics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of attribute names to `AttributeValue` objects, representing the item
    # as it appeared before the `DeleteItem` operation. This map appears in the
    # response only if `ReturnValues` was specified as `ALL_OLD` in the request.
    attributes: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `DeleteItem` operation. The data
    # returned includes the total provisioned throughput consumed, along with
    # statistics for the table and any indexes involved in the operation.
    # `ConsumedCapacity` is only returned if the `ReturnConsumedCapacity`
    # parameter was specified. For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about item collections, if any, that were affected by the
    # `DeleteItem` operation. `ItemCollectionMetrics` is only returned if the
    # `ReturnItemCollectionMetrics` parameter was specified. If the table does
    # not have any local secondary indexes, this information is not returned in
    # the response.

    # Each `ItemCollectionMetrics` element consists of:

    #   * `ItemCollectionKey` \- The partition key value of the item collection. This is the same as the partition key value of the item itself.

    #   * `SizeEstimateRangeGB` \- An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.

    # The estimate is subject to change over time; therefore, do not rely on the
    # precision or accuracy of the estimate.
    item_collection_metrics: "ItemCollectionMetrics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteReplicaAction(ShapeBase):
    """
    Represents a replica to be removed.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
        ]

    # The region of the replica to be removed.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteRequest(ShapeBase):
    """
    Represents a request to perform a `DeleteItem` operation on an item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key",
                "Key",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # A map of attribute name to attribute values, representing the primary key
    # of the item to delete. All of the table's primary key attributes must be
    # specified, and their data types must match those of the table's key schema.
    key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteTableInput(ShapeBase):
    """
    Represents the input of a `DeleteTable` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # The name of the table to delete.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteTableOutput(OutputShapeBase):
    """
    Represents the output of a `DeleteTable` operation.
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
                "table_description",
                "TableDescription",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the properties of a table.
    table_description: "TableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeBackupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
        ]

    # The ARN associated with the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeBackupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backup_description",
                "BackupDescription",
                TypeInfo(BackupDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the description of the backup created for the table.
    backup_description: "BackupDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeContinuousBackupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # Name of the table for which the customer wants to check the continuous
    # backups and point in time recovery settings.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeContinuousBackupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "continuous_backups_description",
                "ContinuousBackupsDescription",
                TypeInfo(ContinuousBackupsDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the continuous backups and point in time recovery settings on
    # the table.
    continuous_backups_description: "ContinuousBackupsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeEndpointsRequest(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeEndpointsResponse(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "endpoints",
                "Endpoints",
                TypeInfo(typing.List[Endpoint]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
    endpoints: typing.List["Endpoint"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeGlobalTableInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
        ]

    # The name of the global table.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGlobalTableOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_table_description",
                "GlobalTableDescription",
                TypeInfo(GlobalTableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the global table.
    global_table_description: "GlobalTableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeGlobalTableSettingsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
        ]

    # The name of the global table to describe.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeGlobalTableSettingsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "replica_settings",
                "ReplicaSettings",
                TypeInfo(typing.List[ReplicaSettingsDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the global table.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region specific settings for the global table.
    replica_settings: typing.List["ReplicaSettingsDescription"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class DescribeLimitsInput(ShapeBase):
    """
    Represents the input of a `DescribeLimits` operation. Has no content.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeLimitsOutput(OutputShapeBase):
    """
    Represents the output of a `DescribeLimits` operation.
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
                "account_max_read_capacity_units",
                "AccountMaxReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "account_max_write_capacity_units",
                "AccountMaxWriteCapacityUnits",
                TypeInfo(int),
            ),
            (
                "table_max_read_capacity_units",
                "TableMaxReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "table_max_write_capacity_units",
                "TableMaxWriteCapacityUnits",
                TypeInfo(int),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum total read capacity units that your account allows you to
    # provision across all of your tables in this region.
    account_max_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum total write capacity units that your account allows you to
    # provision across all of your tables in this region.
    account_max_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum read capacity units that your account allows you to provision
    # for a new table that you are creating in this region, including the read
    # capacity units provisioned for its global secondary indexes (GSIs).
    table_max_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum write capacity units that your account allows you to provision
    # for a new table that you are creating in this region, including the write
    # capacity units provisioned for its global secondary indexes (GSIs).
    table_max_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeTableInput(ShapeBase):
    """
    Represents the input of a `DescribeTable` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # The name of the table to describe.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTableOutput(OutputShapeBase):
    """
    Represents the output of a `DescribeTable` operation.
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
                "table",
                "Table",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The properties of the table.
    table: "TableDescription" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTimeToLiveInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
        ]

    # The name of the table to be described.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeTimeToLiveOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "time_to_live_description",
                "TimeToLiveDescription",
                TypeInfo(TimeToLiveDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    time_to_live_description: "TimeToLiveDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class Endpoint(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "address",
                "Address",
                TypeInfo(str),
            ),
            (
                "cache_period_in_minutes",
                "CachePeriodInMinutes",
                TypeInfo(int),
            ),
        ]

    address: str = dataclasses.field(default=ShapeBase.NOT_SET, )
    cache_period_in_minutes: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ExpectedAttributeValue(ShapeBase):
    """
    Represents a condition to be compared with an attribute value. This condition
    can be used with `DeleteItem`, `PutItem` or `UpdateItem` operations; if the
    comparison evaluates to true, the operation succeeds; if not, the operation
    fails. You can use `ExpectedAttributeValue` in one of two different ways:

      * Use `AttributeValueList` to specify one or more values to compare against an attribute. Use `ComparisonOperator` to specify how you want to perform the comparison. If the comparison evaluates to true, then the conditional operation succeeds.

      * Use `Value` to specify a value that DynamoDB will compare against an attribute. If the values match, then `ExpectedAttributeValue` evaluates to true and the conditional operation succeeds. Optionally, you can also set `Exists` to false, indicating that you _do not_ expect to find the attribute value in the table. In this case, the conditional operation succeeds only if the comparison evaluates to false.

    `Value` and `Exists` are incompatible with `AttributeValueList` and
    `ComparisonOperator`. Note that if you use both sets of parameters at once,
    DynamoDB will return a `ValidationException` exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "value",
                "Value",
                TypeInfo(AttributeValue),
            ),
            (
                "exists",
                "Exists",
                TypeInfo(bool),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                TypeInfo(typing.Union[str, ComparisonOperator]),
            ),
            (
                "attribute_value_list",
                "AttributeValueList",
                TypeInfo(typing.List[AttributeValue]),
            ),
        ]

    # Represents the data for the expected attribute.

    # Each attribute value is described as a name-value pair. The name is the
    # data type, and the value is the data itself.

    # For more information, see [Data
    # Types](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes)
    # in the _Amazon DynamoDB Developer Guide_.
    value: "AttributeValue" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Causes DynamoDB to evaluate the value before attempting a conditional
    # operation:

    #   * If `Exists` is `true`, DynamoDB will check to see if that attribute value already exists in the table. If it is found, then the operation succeeds. If it is not found, the operation fails with a `ConditionalCheckFailedException`.

    #   * If `Exists` is `false`, DynamoDB assumes that the attribute value does not exist in the table. If in fact the value does not exist, then the assumption is valid and the operation succeeds. If the value is found, despite the assumption that it does not exist, the operation fails with a `ConditionalCheckFailedException`.

    # The default setting for `Exists` is `true`. If you supply a `Value` all by
    # itself, DynamoDB assumes the attribute exists: You don't have to set
    # `Exists` to `true`, because it is implied.

    # DynamoDB returns a `ValidationException` if:

    #   * `Exists` is `true` but there is no `Value` to check. (You expect a value to exist, but don't specify what that value is.)

    #   * `Exists` is `false` but you also provide a `Value`. (You cannot expect an attribute to have a value, while also expecting it not to exist.)
    exists: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A comparator for evaluating attributes in the `AttributeValueList`. For
    # example, equals, greater than, less than, etc.

    # The following comparison operators are available:

    # `EQ | NE | LE | LT | GE | GT | NOT_NULL | NULL | CONTAINS | NOT_CONTAINS |
    # BEGINS_WITH | IN | BETWEEN`

    # The following are descriptions of each comparison operator.

    #   * `EQ` : Equal. `EQ` is supported for all data types, including lists and maps.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, Binary, String Set, Number Set, or Binary Set. If an item
    # contains an `AttributeValue` element of a different type than the one
    # provided in the request, the value does not match. For example, `{"S":"6"}`
    # does not equal `{"N":"6"}`. Also, `{"N":"6"}` does not equal `{"NS":["6",
    # "2", "1"]}`.

    #   * `NE` : Not equal. `NE` is supported for all data types, including lists and maps.

    # `AttributeValueList` can contain only one `AttributeValue` of type String,
    # Number, Binary, String Set, Number Set, or Binary Set. If an item contains
    # an `AttributeValue` of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not equal `{"NS":["6", "2", "1"]}`.

    #   * `LE` : Less than or equal.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `LT` : Less than.

    # `AttributeValueList` can contain only one `AttributeValue` of type String,
    # Number, or Binary (not a set type). If an item contains an `AttributeValue`
    # element of a different type than the one provided in the request, the value
    # does not match. For example, `{"S":"6"}` does not equal `{"N":"6"}`. Also,
    # `{"N":"6"}` does not compare to `{"NS":["6", "2", "1"]}`.

    #   * `GE` : Greater than or equal.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `GT` : Greater than.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not equal
    # `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6", "2",
    # "1"]}`.

    #   * `NOT_NULL` : The attribute exists. `NOT_NULL` is supported for all data types, including lists and maps.

    # This operator tests for the existence of an attribute, not its data type.
    # If the data type of attribute "`a`" is null, and you evaluate it using
    # `NOT_NULL`, the result is a Boolean `true`. This result is because the
    # attribute "`a`" exists; its data type is not relevant to the `NOT_NULL`
    # comparison operator.

    #   * `NULL` : The attribute does not exist. `NULL` is supported for all data types, including lists and maps.

    # This operator tests for the nonexistence of an attribute, not its data
    # type. If the data type of attribute "`a`" is null, and you evaluate it
    # using `NULL`, the result is a Boolean `false`. This is because the
    # attribute "`a`" exists; its data type is not relevant to the `NULL`
    # comparison operator.

    #   * `CONTAINS` : Checks for a subsequence, or value in a set.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If the target attribute of the
    # comparison is of type String, then the operator checks for a substring
    # match. If the target attribute of the comparison is of type Binary, then
    # the operator looks for a subsequence of the target that matches the input.
    # If the target attribute of the comparison is a set ("`SS`", "`NS`", or
    # "`BS`"), then the operator evaluates to true if it finds an exact match
    # with any member of the set.

    # CONTAINS is supported for lists: When evaluating "`a CONTAINS b`", "`a`"
    # can be a list; however, "`b`" cannot be a set, a map, or a list.

    #   * `NOT_CONTAINS` : Checks for absence of a subsequence, or absence of a value in a set.

    # `AttributeValueList` can contain only one `AttributeValue` element of type
    # String, Number, or Binary (not a set type). If the target attribute of the
    # comparison is a String, then the operator checks for the absence of a
    # substring match. If the target attribute of the comparison is Binary, then
    # the operator checks for the absence of a subsequence of the target that
    # matches the input. If the target attribute of the comparison is a set
    # ("`SS`", "`NS`", or "`BS`"), then the operator evaluates to true if it
    # _does not_ find an exact match with any member of the set.

    # NOT_CONTAINS is supported for lists: When evaluating "`a NOT CONTAINS b`",
    # "`a`" can be a list; however, "`b`" cannot be a set, a map, or a list.

    #   * `BEGINS_WITH` : Checks for a prefix.

    # `AttributeValueList` can contain only one `AttributeValue` of type String
    # or Binary (not a Number or a set type). The target attribute of the
    # comparison must be of type String or Binary (not a Number or a set type).

    #   * `IN` : Checks for matching elements in a list.

    # `AttributeValueList` can contain one or more `AttributeValue` elements of
    # type String, Number, or Binary. These attributes are compared against an
    # existing attribute of an item. If any elements of the input are equal to
    # the item attribute, the expression evaluates to true.

    #   * `BETWEEN` : Greater than or equal to the first value, and less than or equal to the second value.

    # `AttributeValueList` must contain two `AttributeValue` elements of the same
    # type, either String, Number, or Binary (not a set type). A target attribute
    # matches if the target value is greater than, or equal to, the first element
    # and less than, or equal to, the second element. If an item contains an
    # `AttributeValue` element of a different type than the one provided in the
    # request, the value does not match. For example, `{"S":"6"}` does not
    # compare to `{"N":"6"}`. Also, `{"N":"6"}` does not compare to `{"NS":["6",
    # "2", "1"]}`
    comparison_operator: typing.Union[str, "ComparisonOperator"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # One or more values to evaluate against the supplied attribute. The number
    # of values in the list depends on the `ComparisonOperator` being used.

    # For type Number, value comparisons are numeric.

    # String value comparisons for greater than, equals, or less than are based
    # on ASCII character code values. For example, `a` is greater than `A`, and
    # `a` is greater than `B`. For a list of code values, see
    # <http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>.

    # For Binary, DynamoDB treats each byte of the binary data as unsigned when
    # it compares binary values.

    # For information on specifying data types in JSON, see [JSON Data
    # Format](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataFormat.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attribute_value_list: typing.List["AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetItemInput(ShapeBase):
    """
    Represents the input of a `GetItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "attributes_to_get",
                "AttributesToGet",
                TypeInfo(typing.List[str]),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                TypeInfo(bool),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "projection_expression",
                "ProjectionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The name of the table containing the requested item.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of attribute names to `AttributeValue` objects, representing the
    # primary key of the item to retrieve.

    # For the primary key, you must provide all of the attributes. For example,
    # with a simple primary key, you only need to provide a value for the
    # partition key. For a composite primary key, you must provide values for
    # both the partition key and the sort key.
    key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ProjectionExpression` instead. For more
    # information, see
    # [AttributesToGet](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attributes_to_get: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the read consistency model: If set to `true`, then the operation
    # uses strongly consistent reads; otherwise, the operation uses eventually
    # consistent reads.
    consistent_read: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # A string that identifies one or more attributes to retrieve from the table.
    # These attributes can include scalars, sets, or elements of a JSON document.
    # The attributes in the expression must be separated by commas.

    # If no attribute names are specified, then all attributes will be returned.
    # If any of the requested attributes are not found, they will not appear in
    # the result.

    # For more information, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    projection_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetItemOutput(OutputShapeBase):
    """
    Represents the output of a `GetItem` operation.
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
                "item",
                "Item",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of attribute names to `AttributeValue` objects, as specified by
    # `ProjectionExpression`.
    item: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `GetItem` operation. The data returned
    # includes the total provisioned throughput consumed, along with statistics
    # for the table and any indexes involved in the operation. `ConsumedCapacity`
    # is only returned if the `ReturnConsumedCapacity` parameter was specified.
    # For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalSecondaryIndex(ShapeBase):
    """
    Represents the properties of a global secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
        ]

    # The name of the global secondary index. The name must be unique among all
    # other indexes on this table.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for a global secondary index, which consists of one
    # or more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # global secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the provisioned throughput settings for the specified global
    # secondary index.

    # For current minimum and maximum provisioned throughput values, see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalSecondaryIndexDescription(ShapeBase):
    """
    Represents the properties of a global secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
            (
                "index_status",
                "IndexStatus",
                TypeInfo(typing.Union[str, IndexStatus]),
            ),
            (
                "backfilling",
                "Backfilling",
                TypeInfo(bool),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughputDescription),
            ),
            (
                "index_size_bytes",
                "IndexSizeBytes",
                TypeInfo(int),
            ),
            (
                "item_count",
                "ItemCount",
                TypeInfo(int),
            ),
            (
                "index_arn",
                "IndexArn",
                TypeInfo(str),
            ),
        ]

    # The name of the global secondary index.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for a global secondary index, which consists of one
    # or more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # global secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the global secondary index:

    #   * `CREATING` \- The index is being created.

    #   * `UPDATING` \- The index is being updated.

    #   * `DELETING` \- The index is being deleted.

    #   * `ACTIVE` \- The index is ready for use.
    index_status: typing.Union[str, "IndexStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates whether the index is currently backfilling. _Backfilling_ is the
    # process of reading items from the table and determining whether they can be
    # added to the index. (Not all items will qualify: For example, a partition
    # key cannot have any duplicate values.) If an item can be added to the
    # index, DynamoDB will do so. After all items have been processed, the
    # backfilling operation is complete and `Backfilling` is false.

    # For indexes that were created during a `CreateTable` operation, the
    # `Backfilling` attribute does not appear in the `DescribeTable` output.
    backfilling: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the provisioned throughput settings for the specified global
    # secondary index.

    # For current minimum and maximum provisioned throughput values, see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    provisioned_throughput: "ProvisionedThroughputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total size of the specified index, in bytes. DynamoDB updates this
    # value approximately every six hours. Recent changes might not be reflected
    # in this value.
    index_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of items in the specified index. DynamoDB updates this value
    # approximately every six hours. Recent changes might not be reflected in
    # this value.
    item_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that uniquely identifies the index.
    index_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GlobalSecondaryIndexInfo(ShapeBase):
    """
    Represents the properties of a global secondary index for the table when the
    backup was created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
        ]

    # The name of the global secondary index.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for a global secondary index, which consists of one
    # or more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # global secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the provisioned throughput settings for the specified global
    # secondary index.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalSecondaryIndexUpdate(ShapeBase):
    """
    Represents one of the following:

      * A new global secondary index to be added to an existing table.

      * New provisioned throughput parameters for an existing global secondary index.

      * An existing global secondary index to be removed from an existing table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "update",
                "Update",
                TypeInfo(UpdateGlobalSecondaryIndexAction),
            ),
            (
                "create",
                "Create",
                TypeInfo(CreateGlobalSecondaryIndexAction),
            ),
            (
                "delete",
                "Delete",
                TypeInfo(DeleteGlobalSecondaryIndexAction),
            ),
        ]

    # The name of an existing global secondary index, along with new provisioned
    # throughput settings to be applied to that index.
    update: "UpdateGlobalSecondaryIndexAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The parameters required for creating a global secondary index on an
    # existing table:

    #   * `IndexName `

    #   * `KeySchema `

    #   * `AttributeDefinitions `

    #   * `Projection `

    #   * `ProvisionedThroughput `
    create: "CreateGlobalSecondaryIndexAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of an existing global secondary index to be removed.
    delete: "DeleteGlobalSecondaryIndexAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalTable(ShapeBase):
    """
    Represents the properties of a global table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(typing.List[Replica]),
            ),
        ]

    # The global table name.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The regions where the global table has replicas.
    replication_group: typing.List["Replica"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalTableAlreadyExistsException(ShapeBase):
    """
    The specified global table already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GlobalTableDescription(ShapeBase):
    """
    Contains details about the global table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "replication_group",
                "ReplicationGroup",
                TypeInfo(typing.List[ReplicaDescription]),
            ),
            (
                "global_table_arn",
                "GlobalTableArn",
                TypeInfo(str),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "global_table_status",
                "GlobalTableStatus",
                TypeInfo(typing.Union[str, GlobalTableStatus]),
            ),
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
        ]

    # The regions where the global table has replicas.
    replication_group: typing.List["ReplicaDescription"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The unique identifier of the global table.
    global_table_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The creation time of the global table.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the global table:

    #   * `CREATING` \- The global table is being created.

    #   * `UPDATING` \- The global table is being updated.

    #   * `DELETING` \- The global table is being deleted.

    #   * `ACTIVE` \- The global table is ready for use.
    global_table_status: typing.Union[str, "GlobalTableStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The global table name.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GlobalTableGlobalSecondaryIndexSettingsUpdate(ShapeBase):
    """
    Represents the settings of a global secondary index for a global table that will
    be modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "provisioned_write_capacity_units",
                "ProvisionedWriteCapacityUnits",
                TypeInfo(int),
            ),
            (
                "provisioned_write_capacity_auto_scaling_settings_update",
                "ProvisionedWriteCapacityAutoScalingSettingsUpdate",
                TypeInfo(AutoScalingSettingsUpdate),
            ),
        ]

    # The name of the global secondary index. The name must be unique among all
    # other indexes on this table.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException.`
    provisioned_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AutoScaling settings for managing a global secondary index's write capacity
    # units.
    provisioned_write_capacity_auto_scaling_settings_update: "AutoScalingSettingsUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GlobalTableNotFoundException(ShapeBase):
    """
    The specified global table does not exist.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class GlobalTableStatus(str):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"


@dataclasses.dataclass
class IndexNotFoundException(ShapeBase):
    """
    The operation tried to access a nonexistent index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class IndexStatus(str):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class InternalServerError(ShapeBase):
    """
    An error occurred on the server side.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The server encountered an internal error trying to fulfill the request.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidRestoreTimeException(ShapeBase):
    """
    An invalid restore time was specified. RestoreDateTime must be between
    EarliestRestorableDateTime and LatestRestorableDateTime.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ItemCollectionMetrics(ShapeBase):
    """
    Information about item collections, if any, that were affected by the operation.
    `ItemCollectionMetrics` is only returned if the request asked for it. If the
    table does not have any local secondary indexes, this information is not
    returned in the response.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item_collection_key",
                "ItemCollectionKey",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "size_estimate_range_gb",
                "SizeEstimateRangeGB",
                TypeInfo(typing.List[float]),
            ),
        ]

    # The partition key value of the item collection. This value is the same as
    # the partition key value of the item.
    item_collection_key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An estimate of item collection size, in gigabytes. This value is a two-
    # element array containing a lower bound and an upper bound for the estimate.
    # The estimate includes the size of all the items in the table, plus the size
    # of all attributes projected into all of the local secondary indexes on that
    # table. Use this estimate to measure whether a local secondary index is
    # approaching its size limit.

    # The estimate is subject to change over time; therefore, do not rely on the
    # precision or accuracy of the estimate.
    size_estimate_range_gb: typing.List[float] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ItemCollectionSizeLimitExceededException(ShapeBase):
    """
    An item collection is too large. This exception is only returned for tables that
    have one or more local secondary indexes.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The total size of an item collection has exceeded the maximum limit of 10
    # gigabytes.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeySchemaElement(ShapeBase):
    """
    Represents _a single element_ of a key schema. A key schema specifies the
    attributes that make up the primary key of a table, or the key attributes of an
    index.

    A `KeySchemaElement` represents exactly one attribute of the primary key. For
    example, a simple primary key would be represented by one `KeySchemaElement`
    (for the partition key). A composite primary key would require one
    `KeySchemaElement` for the partition key, and another `KeySchemaElement` for the
    sort key.

    A `KeySchemaElement` must be a scalar, top-level attribute (not a nested
    attribute). The data type must be one of String, Number, or Binary. The
    attribute cannot be nested within a List or a Map.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
            (
                "key_type",
                "KeyType",
                TypeInfo(typing.Union[str, KeyType]),
            ),
        ]

    # The name of a key attribute.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The role that this key attribute will assume:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_type: typing.Union[str, "KeyType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class KeyType(str):
    HASH = "HASH"
    RANGE = "RANGE"


@dataclasses.dataclass
class KeysAndAttributes(ShapeBase):
    """
    Represents a set of primary keys and, for each key, the attributes to retrieve
    from the table.

    For each primary key, you must provide _all_ of the key attributes. For example,
    with a simple primary key, you only need to provide the partition key. For a
    composite primary key, you must provide _both_ the partition key and the sort
    key.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "keys",
                "Keys",
                TypeInfo(typing.List[typing.Dict[str, AttributeValue]]),
            ),
            (
                "attributes_to_get",
                "AttributesToGet",
                TypeInfo(typing.List[str]),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                TypeInfo(bool),
            ),
            (
                "projection_expression",
                "ProjectionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The primary key attribute values that define the items and the attributes
    # associated with the items.
    keys: typing.List[typing.Dict[str, "AttributeValue"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ProjectionExpression` instead. For more
    # information, see [Legacy Conditional
    # Parameters](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attributes_to_get: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The consistency of a read operation. If set to `true`, then a strongly
    # consistent read is used; otherwise, an eventually consistent read is used.
    consistent_read: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies one or more attributes to retrieve from the table.
    # These attributes can include scalars, sets, or elements of a JSON document.
    # The attributes in the `ProjectionExpression` must be separated by commas.

    # If no attribute names are specified, then all attributes will be returned.
    # If any of the requested attributes are not found, they will not appear in
    # the result.

    # For more information, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    projection_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LimitExceededException(ShapeBase):
    """
    There is no limit to the number of daily on-demand backups that can be taken.

    Up to 10 simultaneous table operations are allowed per account. These operations
    include `CreateTable`, `UpdateTable`, `DeleteTable`,`UpdateTimeToLive`,
    `RestoreTableFromBackup`, and `RestoreTableToPointInTime`.

    For tables with secondary indexes, only one of those tables can be in the
    `CREATING` state at any point in time. Do not attempt to create more than one
    such table simultaneously.

    The total limit of tables in the `ACTIVE` state is 250.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # Too many operations for a given subscriber.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListBackupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "time_range_lower_bound",
                "TimeRangeLowerBound",
                TypeInfo(datetime.datetime),
            ),
            (
                "time_range_upper_bound",
                "TimeRangeUpperBound",
                TypeInfo(datetime.datetime),
            ),
            (
                "exclusive_start_backup_arn",
                "ExclusiveStartBackupArn",
                TypeInfo(str),
            ),
            (
                "backup_type",
                "BackupType",
                TypeInfo(typing.Union[str, BackupTypeFilter]),
            ),
        ]

    # The backups from the table specified by `TableName` are listed.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Maximum number of backups to return at once.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Only backups created after this time are listed. `TimeRangeLowerBound` is
    # inclusive.
    time_range_lower_bound: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Only backups created before this time are listed. `TimeRangeUpperBound` is
    # exclusive.
    time_range_upper_bound: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # `LastEvaluatedBackupArn` is the ARN of the backup last evaluated when the
    # current page of results was returned, inclusive of the current page of
    # results. This value may be specified as the `ExclusiveStartBackupArn` of a
    # new `ListBackups` operation in order to fetch the next page of results.
    exclusive_start_backup_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The backups from the table specified by `BackupType` are listed.

    # Where `BackupType` can be:

    #   * `USER` \- On-demand backup created by you.

    #   * `SYSTEM` \- On-demand backup automatically created by DynamoDB.

    #   * `ALL` \- All types of on-demand backups (USER and SYSTEM).
    backup_type: typing.Union[str, "BackupTypeFilter"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListBackupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "backup_summaries",
                "BackupSummaries",
                TypeInfo(typing.List[BackupSummary]),
            ),
            (
                "last_evaluated_backup_arn",
                "LastEvaluatedBackupArn",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of `BackupSummary` objects.
    backup_summaries: typing.List["BackupSummary"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The ARN of the backup last evaluated when the current page of results was
    # returned, inclusive of the current page of results. This value may be
    # specified as the `ExclusiveStartBackupArn` of a new `ListBackups` operation
    # in order to fetch the next page of results.

    # If `LastEvaluatedBackupArn` is empty, then the last page of results has
    # been processed and there are no more results to be retrieved.

    # If `LastEvaluatedBackupArn` is not empty, this may or may not indicate
    # there is more data to be returned. All results are guaranteed to have been
    # returned if and only if no value for `LastEvaluatedBackupArn` is returned.
    last_evaluated_backup_arn: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListBackupsOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListGlobalTablesInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exclusive_start_global_table_name",
                "ExclusiveStartGlobalTableName",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
        ]

    # The first global table name that this operation will evaluate.
    exclusive_start_global_table_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of table names to return.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Lists the global tables in a specific region.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListGlobalTablesOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_tables",
                "GlobalTables",
                TypeInfo(typing.List[GlobalTable]),
            ),
            (
                "last_evaluated_global_table_name",
                "LastEvaluatedGlobalTableName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # List of global table names.
    global_tables: typing.List["GlobalTable"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Last evaluated global table name.
    last_evaluated_global_table_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ListTablesInput(ShapeBase):
    """
    Represents the input of a `ListTables` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "exclusive_start_table_name",
                "ExclusiveStartTableName",
                TypeInfo(str),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
        ]

    # The first table name that this operation will evaluate. Use the value that
    # was returned for `LastEvaluatedTableName` in a previous operation, so that
    # you can obtain the next page of results.
    exclusive_start_table_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A maximum number of table names to return. If this parameter is not
    # specified, the limit is 100.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTablesOutput(OutputShapeBase):
    """
    Represents the output of a `ListTables` operation.
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
                "table_names",
                "TableNames",
                TypeInfo(typing.List[str]),
            ),
            (
                "last_evaluated_table_name",
                "LastEvaluatedTableName",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The names of the tables associated with the current account at the current
    # endpoint. The maximum size of this array is 100.

    # If `LastEvaluatedTableName` also appears in the output, you can use this
    # value as the `ExclusiveStartTableName` parameter in a subsequent
    # `ListTables` request and obtain the next page of results.
    table_names: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the last table in the current page of results. Use this value
    # as the `ExclusiveStartTableName` in a new request to obtain the next page
    # of results, until all the table names are returned.

    # If you do not receive a `LastEvaluatedTableName` value in the response,
    # this means that there are no more table names to be retrieved.
    last_evaluated_table_name: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ListTablesOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class ListTagsOfResourceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    # The Amazon DynamoDB resource with tags to be listed. This value is an
    # Amazon Resource Name (ARN).
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An optional string that, if supplied, must be copied from the output of a
    # previous call to ListTagOfResource. When provided in this manner, this API
    # fetches the next page of results.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ListTagsOfResourceOutput(OutputShapeBase):
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
                TypeInfo(typing.List[Tag]),
            ),
            (
                "next_token",
                "NextToken",
                TypeInfo(str),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The tags currently associated with the Amazon DynamoDB resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )

    # If this value is returned, there are additional results to be displayed. To
    # retrieve them, call ListTagsOfResource again, with NextToken set to this
    # value.
    next_token: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LocalSecondaryIndex(ShapeBase):
    """
    Represents the properties of a local secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
        ]

    # The name of the local secondary index. The name must be unique among all
    # other indexes on this table.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for the local secondary index, consisting of one or
    # more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # local secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LocalSecondaryIndexDescription(ShapeBase):
    """
    Represents the properties of a local secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
            (
                "index_size_bytes",
                "IndexSizeBytes",
                TypeInfo(int),
            ),
            (
                "item_count",
                "ItemCount",
                TypeInfo(int),
            ),
            (
                "index_arn",
                "IndexArn",
                TypeInfo(str),
            ),
        ]

    # Represents the name of the local secondary index.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for the local secondary index, consisting of one or
    # more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # global secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The total size of the specified index, in bytes. DynamoDB updates this
    # value approximately every six hours. Recent changes might not be reflected
    # in this value.
    index_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of items in the specified index. DynamoDB updates this value
    # approximately every six hours. Recent changes might not be reflected in
    # this value.
    item_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that uniquely identifies the index.
    index_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LocalSecondaryIndexInfo(ShapeBase):
    """
    Represents the properties of a local secondary index for the table when the
    backup was created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "projection",
                "Projection",
                TypeInfo(Projection),
            ),
        ]

    # Represents the name of the local secondary index.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The complete key schema for a local secondary index, which consists of one
    # or more pairs of attribute names and key types:

    #   * `HASH` \- partition key

    #   * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents attributes that are copied (projected) from the table into the
    # global secondary index. These are in addition to the primary key attributes
    # and index key attributes, which are automatically projected.
    projection: "Projection" = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PointInTimeRecoveryDescription(ShapeBase):
    """
    The description of the point in time settings applied to the table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "point_in_time_recovery_status",
                "PointInTimeRecoveryStatus",
                TypeInfo(typing.Union[str, PointInTimeRecoveryStatus]),
            ),
            (
                "earliest_restorable_date_time",
                "EarliestRestorableDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "latest_restorable_date_time",
                "LatestRestorableDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # The current state of point in time recovery:

    #   * `ENABLING` \- Point in time recovery is being enabled.

    #   * `ENABLED` \- Point in time recovery is enabled.

    #   * `DISABLED` \- Point in time recovery is disabled.
    point_in_time_recovery_status: typing.Union[str, "PointInTimeRecoveryStatus"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # Specifies the earliest point in time you can restore your table to. It You
    # can restore your table to any point in time during the last 35 days.
    earliest_restorable_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # `LatestRestorableDateTime` is typically 5 minutes before the current time.
    latest_restorable_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PointInTimeRecoverySpecification(ShapeBase):
    """
    Represents the settings used to enable point in time recovery.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "point_in_time_recovery_enabled",
                "PointInTimeRecoveryEnabled",
                TypeInfo(bool),
            ),
        ]

    # Indicates whether point in time recovery is enabled (true) or disabled
    # (false) on the table.
    point_in_time_recovery_enabled: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class PointInTimeRecoveryStatus(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class PointInTimeRecoveryUnavailableException(ShapeBase):
    """
    Point in time recovery has not yet been enabled for this source table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Projection(ShapeBase):
    """
    Represents attributes that are copied (projected) from the table into an index.
    These are in addition to the primary key attributes and index key attributes,
    which are automatically projected.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "projection_type",
                "ProjectionType",
                TypeInfo(typing.Union[str, ProjectionType]),
            ),
            (
                "non_key_attributes",
                "NonKeyAttributes",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The set of attributes that are projected into the index:

    #   * `KEYS_ONLY` \- Only the index and primary keys are projected into the index.

    #   * `INCLUDE` \- Only the specified table attributes are projected into the index. The list of projected attributes are in `NonKeyAttributes`.

    #   * `ALL` \- All of the table attributes are projected into the index.
    projection_type: typing.Union[str, "ProjectionType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the non-key attribute names which will be projected into the
    # index.

    # For local secondary indexes, the total count of `NonKeyAttributes` summed
    # across all of the local secondary indexes, must not exceed 20. If you
    # project the same attribute into two different indexes, this counts as two
    # distinct attributes when determining the total.
    non_key_attributes: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ProjectionType(str):
    ALL = "ALL"
    KEYS_ONLY = "KEYS_ONLY"
    INCLUDE = "INCLUDE"


@dataclasses.dataclass
class ProvisionedThroughput(ShapeBase):
    """
    Represents the provisioned throughput settings for a specified table or index.
    The settings can be modified using the `UpdateTable` operation.

    For current minimum and maximum provisioned throughput values, see
    [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    in the _Amazon DynamoDB Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "read_capacity_units",
                "ReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "write_capacity_units",
                "WriteCapacityUnits",
                TypeInfo(int),
            ),
        ]

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`. For more information, see
    # [Specifying Read and Write
    # Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput)
    # in the _Amazon DynamoDB Developer Guide_.
    read_capacity_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException`. For more information, see [Specifying Read and Write
    # Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput)
    # in the _Amazon DynamoDB Developer Guide_.
    write_capacity_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedThroughputDescription(ShapeBase):
    """
    Represents the provisioned throughput settings for the table, consisting of read
    and write capacity units, along with data about increases and decreases.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "last_increase_date_time",
                "LastIncreaseDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "last_decrease_date_time",
                "LastDecreaseDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "number_of_decreases_today",
                "NumberOfDecreasesToday",
                TypeInfo(int),
            ),
            (
                "read_capacity_units",
                "ReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "write_capacity_units",
                "WriteCapacityUnits",
                TypeInfo(int),
            ),
        ]

    # The date and time of the last provisioned throughput increase for this
    # table.
    last_increase_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time of the last provisioned throughput decrease for this
    # table.
    last_decrease_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of provisioned throughput decreases for this table during this
    # UTC calendar day. For current maximums on provisioned throughput decreases,
    # see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    number_of_decreases_today: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`. Eventually consistent reads
    # require less effort than strongly consistent reads, so a setting of 50
    # `ReadCapacityUnits` per second provides 100 eventually consistent
    # `ReadCapacityUnits` per second.
    read_capacity_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException`.
    write_capacity_units: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ProvisionedThroughputExceededException(ShapeBase):
    """
    Your request rate is too high. The AWS SDKs for DynamoDB automatically retry
    requests that receive this exception. Your request is eventually successful,
    unless your retry queue is too large to finish. Reduce the frequency of requests
    and use exponential backoff. For more information, go to [Error Retries and
    Exponential
    Backoff](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff)
    in the _Amazon DynamoDB Developer Guide_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # You exceeded your maximum allowed provisioned throughput.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutItemInput(ShapeBase):
    """
    Represents the input of a `PutItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "item",
                "Item",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "expected",
                "Expected",
                TypeInfo(typing.Dict[str, ExpectedAttributeValue]),
            ),
            (
                "return_values",
                "ReturnValues",
                TypeInfo(typing.Union[str, ReturnValue]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "return_item_collection_metrics",
                "ReturnItemCollectionMetrics",
                TypeInfo(typing.Union[str, ReturnItemCollectionMetrics]),
            ),
            (
                "conditional_operator",
                "ConditionalOperator",
                TypeInfo(typing.Union[str, ConditionalOperator]),
            ),
            (
                "condition_expression",
                "ConditionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expression_attribute_values",
                "ExpressionAttributeValues",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # The name of the table to contain the item.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A map of attribute name/value pairs, one for each attribute. Only the
    # primary key attributes are required; you can optionally provide other
    # attribute name-value pairs for the item.

    # You must provide all of the attributes for the primary key. For example,
    # with a simple primary key, you only need to provide a value for the
    # partition key. For a composite primary key, you must provide both values
    # for both the partition key and the sort key.

    # If you specify any attributes that are part of an index key, then the data
    # types for those attributes must match those of the schema in the table's
    # attribute definition.

    # For more information about primary keys, see [Primary
    # Key](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModelPrimaryKey)
    # in the _Amazon DynamoDB Developer Guide_.

    # Each element in the `Item` map is an `AttributeValue` object.
    item: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [Expected](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expected: typing.Dict[str, "ExpectedAttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Use `ReturnValues` if you want to get the item attributes as they appeared
    # before they were updated with the `PutItem` request. For `PutItem`, the
    # valid values are:

    #   * `NONE` \- If `ReturnValues` is not specified, or if its value is `NONE`, then nothing is returned. (This setting is the default for `ReturnValues`.)

    #   * `ALL_OLD` \- If `PutItem` overwrote an attribute name-value pair, then the content of the old item is returned.

    # The `ReturnValues` parameter is used by several DynamoDB operations;
    # however, `PutItem` does not recognize any values other than `NONE` or
    # `ALL_OLD`.
    return_values: typing.Union[str, "ReturnValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Determines whether item collection metrics are returned. If set to `SIZE`,
    # the response includes statistics about item collections, if any, that were
    # modified during the operation are returned in the response. If set to
    # `NONE` (the default), no statistics are returned.
    return_item_collection_metrics: typing.Union[
        str, "ReturnItemCollectionMetrics"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [ConditionalOperator](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html)
    # in the _Amazon DynamoDB Developer Guide_.
    conditional_operator: typing.Union[str, "ConditionalOperator"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # A condition that must be satisfied in order for a conditional `PutItem`
    # operation to succeed.

    # An expression can contain any of the following:

    #   * Functions: `attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size`

    # These function names are case-sensitive.

    #   * Comparison operators: `= | <> | < | > | <= | >= | BETWEEN | IN `

    #   * Logical operators: `AND | OR | NOT`

    # For more information on condition expressions, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    condition_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more values that can be substituted in an expression.

    # Use the **:** (colon) character in an expression to dereference an
    # attribute value. For example, suppose that you wanted to check whether the
    # value of the _ProductStatus_ attribute was one of the following:

    # `Available | Backordered | Discontinued`

    # You would first need to specify `ExpressionAttributeValues` as follows:

    # `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"},
    # ":disc":{"S":"Discontinued"} }`

    # You could then use these values in an expression, such as this:

    # `ProductStatus IN (:avail, :back, :disc)`

    # For more information on expression attribute values, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_values: typing.Dict[str, "AttributeValue"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class PutItemOutput(OutputShapeBase):
    """
    Represents the output of a `PutItem` operation.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
            (
                "item_collection_metrics",
                "ItemCollectionMetrics",
                TypeInfo(ItemCollectionMetrics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The attribute values as they appeared before the `PutItem` operation, but
    # only if `ReturnValues` is specified as `ALL_OLD` in the request. Each
    # element consists of an attribute name and an attribute value.
    attributes: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `PutItem` operation. The data returned
    # includes the total provisioned throughput consumed, along with statistics
    # for the table and any indexes involved in the operation. `ConsumedCapacity`
    # is only returned if the `ReturnConsumedCapacity` parameter was specified.
    # For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about item collections, if any, that were affected by the
    # `PutItem` operation. `ItemCollectionMetrics` is only returned if the
    # `ReturnItemCollectionMetrics` parameter was specified. If the table does
    # not have any local secondary indexes, this information is not returned in
    # the response.

    # Each `ItemCollectionMetrics` element consists of:

    #   * `ItemCollectionKey` \- The partition key value of the item collection. This is the same as the partition key value of the item itself.

    #   * `SizeEstimateRangeGB` \- An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.

    # The estimate is subject to change over time; therefore, do not rely on the
    # precision or accuracy of the estimate.
    item_collection_metrics: "ItemCollectionMetrics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class PutRequest(ShapeBase):
    """
    Represents a request to perform a `PutItem` operation on an item.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "item",
                "Item",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # A map of attribute name to attribute values, representing the primary key
    # of an item to be processed by `PutItem`. All of the table's primary key
    # attributes must be specified, and their data types must match those of the
    # table's key schema. If any attributes are present in the item which are
    # part of an index key schema for the table, their types must match the index
    # key schema.
    item: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class QueryInput(ShapeBase):
    """
    Represents the input of a `Query` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "select",
                "Select",
                TypeInfo(typing.Union[str, Select]),
            ),
            (
                "attributes_to_get",
                "AttributesToGet",
                TypeInfo(typing.List[str]),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                TypeInfo(bool),
            ),
            (
                "key_conditions",
                "KeyConditions",
                TypeInfo(typing.Dict[str, Condition]),
            ),
            (
                "query_filter",
                "QueryFilter",
                TypeInfo(typing.Dict[str, Condition]),
            ),
            (
                "conditional_operator",
                "ConditionalOperator",
                TypeInfo(typing.Union[str, ConditionalOperator]),
            ),
            (
                "scan_index_forward",
                "ScanIndexForward",
                TypeInfo(bool),
            ),
            (
                "exclusive_start_key",
                "ExclusiveStartKey",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "projection_expression",
                "ProjectionExpression",
                TypeInfo(str),
            ),
            (
                "filter_expression",
                "FilterExpression",
                TypeInfo(str),
            ),
            (
                "key_condition_expression",
                "KeyConditionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expression_attribute_values",
                "ExpressionAttributeValues",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # The name of the table containing the requested items.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of an index to query. This index can be any local secondary index
    # or global secondary index on the table. Note that if you use the
    # `IndexName` parameter, you must also provide `TableName.`
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes to be returned in the result. You can retrieve all item
    # attributes, specific item attributes, the count of matching items, or in
    # the case of an index, some or all of the attributes projected into the
    # index.

    #   * `ALL_ATTRIBUTES` \- Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.

    #   * `ALL_PROJECTED_ATTRIBUTES` \- Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES`.

    #   * `COUNT` \- Returns the number of matching items, rather than the matching items themselves.

    #   * `SPECIFIC_ATTRIBUTES` \- Returns only the attributes listed in `AttributesToGet`. This return value is equivalent to specifying `AttributesToGet` without specifying any value for `Select`.

    # If you query or scan a local secondary index and request only attributes
    # that are projected into that index, the operation will read only the index
    # and not the table. If any of the requested attributes are not projected
    # into the local secondary index, DynamoDB will fetch each of these
    # attributes from the parent table. This extra fetching incurs additional
    # throughput cost and latency.

    # If you query or scan a global secondary index, you can only request
    # attributes that are projected into the index. Global secondary index
    # queries cannot fetch attributes from the parent table.

    # If neither `Select` nor `AttributesToGet` are specified, DynamoDB defaults
    # to `ALL_ATTRIBUTES` when accessing a table, and `ALL_PROJECTED_ATTRIBUTES`
    # when accessing an index. You cannot use both `Select` and `AttributesToGet`
    # together in a single request, unless the value for `Select` is
    # `SPECIFIC_ATTRIBUTES`. (This usage is equivalent to specifying
    # `AttributesToGet` without any value for `Select`.)

    # If you use the `ProjectionExpression` parameter, then the value for
    # `Select` can only be `SPECIFIC_ATTRIBUTES`. Any other value for `Select`
    # will return an error.
    select: typing.Union[str, "Select"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ProjectionExpression` instead. For more
    # information, see
    # [AttributesToGet](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attributes_to_get: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to evaluate (not necessarily the number of
    # matching items). If DynamoDB processes the number of items up to the limit
    # while processing the results, it stops the operation and returns the
    # matching values up to that point, and a key in `LastEvaluatedKey` to apply
    # in a subsequent operation, so that you can pick up where you left off.
    # Also, if the processed data set size exceeds 1 MB before DynamoDB reaches
    # this limit, it stops the operation and returns the matching values up to
    # the limit, and a key in `LastEvaluatedKey` to apply in a subsequent
    # operation to continue the operation. For more information, see [Query and
    # Scan](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html)
    # in the _Amazon DynamoDB Developer Guide_.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Determines the read consistency model: If set to `true`, then the operation
    # uses strongly consistent reads; otherwise, the operation uses eventually
    # consistent reads.

    # Strongly consistent reads are not supported on global secondary indexes. If
    # you query a global secondary index with `ConsistentRead` set to `true`, you
    # will receive a `ValidationException`.
    consistent_read: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is a legacy parameter. Use `KeyConditionExpression` instead. For more
    # information, see
    # [KeyConditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    key_conditions: typing.Dict[str, "Condition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `FilterExpression` instead. For more
    # information, see
    # [QueryFilter](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html)
    # in the _Amazon DynamoDB Developer Guide_.
    query_filter: typing.Dict[str, "Condition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `FilterExpression` instead. For more
    # information, see
    # [ConditionalOperator](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html)
    # in the _Amazon DynamoDB Developer Guide_.
    conditional_operator: typing.Union[str, "ConditionalOperator"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Specifies the order for index traversal: If `true` (default), the traversal
    # is performed in ascending order; if `false`, the traversal is performed in
    # descending order.

    # Items with the same partition key value are stored in sorted order by sort
    # key. If the sort key data type is Number, the results are stored in numeric
    # order. For type String, the results are stored in order of UTF-8 bytes. For
    # type Binary, DynamoDB treats each byte of the binary data as unsigned.

    # If `ScanIndexForward` is `true`, DynamoDB returns the results in the order
    # in which they are stored (by sort key value). This is the default behavior.
    # If `ScanIndexForward` is `false`, DynamoDB reads the results in reverse
    # order by sort key value, and then returns the results to the client.
    scan_index_forward: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The primary key of the first item that this operation will evaluate. Use
    # the value that was returned for `LastEvaluatedKey` in the previous
    # operation.

    # The data type for `ExclusiveStartKey` must be String, Number or Binary. No
    # set data types are allowed.
    exclusive_start_key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # A string that identifies one or more attributes to retrieve from the table.
    # These attributes can include scalars, sets, or elements of a JSON document.
    # The attributes in the expression must be separated by commas.

    # If no attribute names are specified, then all attributes will be returned.
    # If any of the requested attributes are not found, they will not appear in
    # the result.

    # For more information, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    projection_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that contains conditions that DynamoDB applies after the `Query`
    # operation, but before the data is returned to you. Items that do not
    # satisfy the `FilterExpression` criteria are not returned.

    # A `FilterExpression` does not allow key attributes. You cannot define a
    # filter expression based on a partition key or a sort key.

    # A `FilterExpression` is applied after the items have already been read; the
    # process of filtering does not consume any additional read capacity units.

    # For more information, see [Filter
    # Expressions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#FilteringResults)
    # in the _Amazon DynamoDB Developer Guide_.
    filter_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The condition that specifies the key value(s) for items to be retrieved by
    # the `Query` action.

    # The condition must perform an equality test on a single partition key
    # value.

    # The condition can optionally perform one of several comparison tests on a
    # single sort key value. This allows `Query` to retrieve one item with a
    # given partition key value and sort key value, or several items that have
    # the same partition key value but different sort key values.

    # The partition key equality test is required, and must be specified in the
    # following format:

    # `partitionKeyName` _=_ `:partitionkeyval`

    # If you also want to provide a condition for the sort key, it must be
    # combined using `AND` with the condition for the sort key. Following is an
    # example, using the **=** comparison operator for the sort key:

    # `partitionKeyName` `=` `:partitionkeyval` `AND` `sortKeyName` `=`
    # `:sortkeyval`

    # Valid comparisons for the sort key condition are as follows:

    #   * `sortKeyName` `=` `:sortkeyval` \- true if the sort key value is equal to `:sortkeyval`.

    #   * `sortKeyName` `<` `:sortkeyval` \- true if the sort key value is less than `:sortkeyval`.

    #   * `sortKeyName` `<=` `:sortkeyval` \- true if the sort key value is less than or equal to `:sortkeyval`.

    #   * `sortKeyName` `>` `:sortkeyval` \- true if the sort key value is greater than `:sortkeyval`.

    #   * `sortKeyName` `>= ` `:sortkeyval` \- true if the sort key value is greater than or equal to `:sortkeyval`.

    #   * `sortKeyName` `BETWEEN` `:sortkeyval1` `AND` `:sortkeyval2` \- true if the sort key value is greater than or equal to `:sortkeyval1`, and less than or equal to `:sortkeyval2`.

    #   * `begins_with (` `sortKeyName`, `:sortkeyval` `)` \- true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name `begins_with` is case-sensitive.

    # Use the `ExpressionAttributeValues` parameter to replace tokens such as
    # `:partitionval` and `:sortval` with actual values at runtime.

    # You can optionally use the `ExpressionAttributeNames` parameter to replace
    # the names of the partition key and sort key with placeholder tokens. This
    # option might be necessary if an attribute name conflicts with a DynamoDB
    # reserved word. For example, the following `KeyConditionExpression`
    # parameter causes an error because _Size_ is a reserved word:

    #   * `Size = :myval`

    # To work around this, define a placeholder (such a `#S`) to represent the
    # attribute name _Size_. `KeyConditionExpression` then is as follows:

    #   * `#S = :myval`

    # For a list of reserved words, see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_.

    # For more information on `ExpressionAttributeNames` and
    # `ExpressionAttributeValues`, see [Using Placeholders for Attribute Names
    # and
    # Values](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html)
    # in the _Amazon DynamoDB Developer Guide_.
    key_condition_expression: str = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more values that can be substituted in an expression.

    # Use the **:** (colon) character in an expression to dereference an
    # attribute value. For example, suppose that you wanted to check whether the
    # value of the _ProductStatus_ attribute was one of the following:

    # `Available | Backordered | Discontinued`

    # You would first need to specify `ExpressionAttributeValues` as follows:

    # `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"},
    # ":disc":{"S":"Discontinued"} }`

    # You could then use these values in an expression, such as this:

    # `ProductStatus IN (:avail, :back, :disc)`

    # For more information on expression attribute values, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_values: typing.Dict[str, "AttributeValue"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class QueryOutput(OutputShapeBase):
    """
    Represents the output of a `Query` operation.
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
                "items",
                "Items",
                TypeInfo(typing.List[typing.Dict[str, AttributeValue]]),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "scanned_count",
                "ScannedCount",
                TypeInfo(int),
            ),
            (
                "last_evaluated_key",
                "LastEvaluatedKey",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of item attributes that match the query criteria. Each element in
    # this array consists of an attribute name and the value for that attribute.
    items: typing.List[typing.Dict[str, "AttributeValue"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of items in the response.

    # If you used a `QueryFilter` in the request, then `Count` is the number of
    # items returned after the filter was applied, and `ScannedCount` is the
    # number of matching items before the filter was applied.

    # If you did not use a filter in the request, then `Count` and `ScannedCount`
    # are the same.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of items evaluated, before any `QueryFilter` is applied. A high
    # `ScannedCount` value with few, or no, `Count` results indicates an
    # inefficient `Query` operation. For more information, see [Count and
    # ScannedCount](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#Count)
    # in the _Amazon DynamoDB Developer Guide_.

    # If you did not use a filter in the request, then `ScannedCount` is the same
    # as `Count`.
    scanned_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The primary key of the item where the operation stopped, inclusive of the
    # previous result set. Use this value to start a new operation, excluding
    # this value in the new request.

    # If `LastEvaluatedKey` is empty, then the "last page" of results has been
    # processed and there is no more data to be retrieved.

    # If `LastEvaluatedKey` is not empty, it does not necessarily mean that there
    # is more data in the result set. The only way to know when you have reached
    # the end of the result set is when `LastEvaluatedKey` is empty.
    last_evaluated_key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `Query` operation. The data returned
    # includes the total provisioned throughput consumed, along with statistics
    # for the table and any indexes involved in the operation. `ConsumedCapacity`
    # is only returned if the `ReturnConsumedCapacity` parameter was specified
    # For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["QueryOutput", None, None]:
        yield from super()._paginate()


@dataclasses.dataclass
class Replica(ShapeBase):
    """
    Represents the properties of a replica.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
        ]

    # The region where the replica needs to be created.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicaAlreadyExistsException(ShapeBase):
    """
    The specified replica is already part of the global table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicaDescription(ShapeBase):
    """
    Contains the details of the replica.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
        ]

    # The name of the region.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicaGlobalSecondaryIndexSettingsDescription(ShapeBase):
    """
    Represents the properties of a global secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "index_status",
                "IndexStatus",
                TypeInfo(typing.Union[str, IndexStatus]),
            ),
            (
                "provisioned_read_capacity_units",
                "ProvisionedReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "provisioned_read_capacity_auto_scaling_settings",
                "ProvisionedReadCapacityAutoScalingSettings",
                TypeInfo(AutoScalingSettingsDescription),
            ),
            (
                "provisioned_write_capacity_units",
                "ProvisionedWriteCapacityUnits",
                TypeInfo(int),
            ),
            (
                "provisioned_write_capacity_auto_scaling_settings",
                "ProvisionedWriteCapacityAutoScalingSettings",
                TypeInfo(AutoScalingSettingsDescription),
            ),
        ]

    # The name of the global secondary index. The name must be unique among all
    # other indexes on this table.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current status of the global secondary index:

    #   * `CREATING` \- The global secondary index is being created.

    #   * `UPDATING` \- The global secondary index is being updated.

    #   * `DELETING` \- The global secondary index is being deleted.

    #   * `ACTIVE` \- The global secondary index is ready for use.
    index_status: typing.Union[str, "IndexStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`.
    provisioned_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Autoscaling settings for a global secondary index replica's read capacity
    # units.
    provisioned_read_capacity_auto_scaling_settings: "AutoScalingSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException`.
    provisioned_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AutoScaling settings for a global secondary index replica's write capacity
    # units.
    provisioned_write_capacity_auto_scaling_settings: "AutoScalingSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicaGlobalSecondaryIndexSettingsUpdate(ShapeBase):
    """
    Represents the settings of a global secondary index for a global table that will
    be modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "provisioned_read_capacity_units",
                "ProvisionedReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "provisioned_read_capacity_auto_scaling_settings_update",
                "ProvisionedReadCapacityAutoScalingSettingsUpdate",
                TypeInfo(AutoScalingSettingsUpdate),
            ),
        ]

    # The name of the global secondary index. The name must be unique among all
    # other indexes on this table.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`.
    provisioned_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Autoscaling settings for managing a global secondary index replica's read
    # capacity units.
    provisioned_read_capacity_auto_scaling_settings_update: "AutoScalingSettingsUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReplicaNotFoundException(ShapeBase):
    """
    The specified replica is no longer part of the global table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ReplicaSettingsDescription(ShapeBase):
    """
    Represents the properties of a replica.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
            (
                "replica_status",
                "ReplicaStatus",
                TypeInfo(typing.Union[str, ReplicaStatus]),
            ),
            (
                "replica_provisioned_read_capacity_units",
                "ReplicaProvisionedReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "replica_provisioned_read_capacity_auto_scaling_settings",
                "ReplicaProvisionedReadCapacityAutoScalingSettings",
                TypeInfo(AutoScalingSettingsDescription),
            ),
            (
                "replica_provisioned_write_capacity_units",
                "ReplicaProvisionedWriteCapacityUnits",
                TypeInfo(int),
            ),
            (
                "replica_provisioned_write_capacity_auto_scaling_settings",
                "ReplicaProvisionedWriteCapacityAutoScalingSettings",
                TypeInfo(AutoScalingSettingsDescription),
            ),
            (
                "replica_global_secondary_index_settings",
                "ReplicaGlobalSecondaryIndexSettings",
                TypeInfo(
                    typing.List[ReplicaGlobalSecondaryIndexSettingsDescription]
                ),
            ),
        ]

    # The region name of the replica.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The current state of the region:

    #   * `CREATING` \- The region is being created.

    #   * `UPDATING` \- The region is being updated.

    #   * `DELETING` \- The region is being deleted.

    #   * `ACTIVE` \- The region is ready for use.
    replica_status: typing.Union[str, "ReplicaStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`. For more information, see
    # [Specifying Read and Write
    # Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput)
    # in the _Amazon DynamoDB Developer Guide_.
    replica_provisioned_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Autoscaling settings for a global table replica's read capacity units.
    replica_provisioned_read_capacity_auto_scaling_settings: "AutoScalingSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException`. For more information, see [Specifying Read and Write
    # Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput)
    # in the _Amazon DynamoDB Developer Guide_.
    replica_provisioned_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AutoScaling settings for a global table replica's write capacity units.
    replica_provisioned_write_capacity_auto_scaling_settings: "AutoScalingSettingsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Replica global secondary index settings for the global table.
    replica_global_secondary_index_settings: typing.List[
        "ReplicaGlobalSecondaryIndexSettingsDescription"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


@dataclasses.dataclass
class ReplicaSettingsUpdate(ShapeBase):
    """
    Represents the settings for a global table in a region that will be modified.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "region_name",
                "RegionName",
                TypeInfo(str),
            ),
            (
                "replica_provisioned_read_capacity_units",
                "ReplicaProvisionedReadCapacityUnits",
                TypeInfo(int),
            ),
            (
                "replica_provisioned_read_capacity_auto_scaling_settings_update",
                "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate",
                TypeInfo(AutoScalingSettingsUpdate),
            ),
            (
                "replica_global_secondary_index_settings_update",
                "ReplicaGlobalSecondaryIndexSettingsUpdate",
                TypeInfo(
                    typing.List[ReplicaGlobalSecondaryIndexSettingsUpdate]
                ),
            ),
        ]

    # The region of the replica to be added.
    region_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of strongly consistent reads consumed per second before
    # DynamoDB returns a `ThrottlingException`. For more information, see
    # [Specifying Read and Write
    # Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput)
    # in the _Amazon DynamoDB Developer Guide_.
    replica_provisioned_read_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Autoscaling settings for managing a global table replica's read capacity
    # units.
    replica_provisioned_read_capacity_auto_scaling_settings_update: "AutoScalingSettingsUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the settings of a global secondary index for a global table that
    # will be modified.
    replica_global_secondary_index_settings_update: typing.List[
        "ReplicaGlobalSecondaryIndexSettingsUpdate"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )


class ReplicaStatus(str):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class ReplicaUpdate(ShapeBase):
    """
    Represents one of the following:

      * A new replica to be added to an existing global table.

      * New parameters for an existing replica.

      * An existing replica to be removed from an existing global table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "create",
                "Create",
                TypeInfo(CreateReplicaAction),
            ),
            (
                "delete",
                "Delete",
                TypeInfo(DeleteReplicaAction),
            ),
        ]

    # The parameters required for creating a replica on an existing global table.
    create: "CreateReplicaAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the existing replica to be removed.
    delete: "DeleteReplicaAction" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ResourceInUseException(ShapeBase):
    """
    The operation conflicts with the resource's availability. For example, you
    attempted to recreate an existing table, or tried to delete a table currently in
    the `CREATING` state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The resource which is being attempted to be changed is in use.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ResourceNotFoundException(ShapeBase):
    """
    The operation tried to access a nonexistent table or index. The resource might
    not be specified correctly, or its status might not be `ACTIVE`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    # The resource which is being requested does not exist.
    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreSummary(ShapeBase):
    """
    Contains details for the restore.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "restore_date_time",
                "RestoreDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "restore_in_progress",
                "RestoreInProgress",
                TypeInfo(bool),
            ),
            (
                "source_backup_arn",
                "SourceBackupArn",
                TypeInfo(str),
            ),
            (
                "source_table_arn",
                "SourceTableArn",
                TypeInfo(str),
            ),
        ]

    # Point in time or source backup time.
    restore_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Indicates if a restore is in progress or not.
    restore_in_progress: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the backup from which the table was restored.
    source_backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # ARN of the source table of the backup that is being restored.
    source_table_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreTableFromBackupInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "target_table_name",
                "TargetTableName",
                TypeInfo(str),
            ),
            (
                "backup_arn",
                "BackupArn",
                TypeInfo(str),
            ),
        ]

    # The name of the new table to which the backup must be restored.
    target_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The ARN associated with the backup.
    backup_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RestoreTableFromBackupOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_description",
                "TableDescription",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the table created from an existing backup.
    table_description: "TableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreTableToPointInTimeInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "source_table_name",
                "SourceTableName",
                TypeInfo(str),
            ),
            (
                "target_table_name",
                "TargetTableName",
                TypeInfo(str),
            ),
            (
                "use_latest_restorable_time",
                "UseLatestRestorableTime",
                TypeInfo(bool),
            ),
            (
                "restore_date_time",
                "RestoreDateTime",
                TypeInfo(datetime.datetime),
            ),
        ]

    # Name of the source table that is being restored.
    source_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the new table to which it must be restored to.
    target_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Restore the table to the latest possible time. `LatestRestorableDateTime`
    # is typically 5 minutes before the current time.
    use_latest_restorable_time: bool = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time in the past to restore the table to.
    restore_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class RestoreTableToPointInTimeOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "table_description",
                "TableDescription",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the properties of a table.
    table_description: "TableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class ReturnConsumedCapacity(str):
    """
    Determines the level of detail about provisioned throughput consumption that is
    returned in the response:

      * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    Note that some operations, such as `GetItem` and `BatchGetItem`, do not access
    any indexes at all. In these cases, specifying `INDEXES` will only return
    `ConsumedCapacity` information for table(s).

      * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

      * `NONE` \- No `ConsumedCapacity` details are included in the response.
    """
    INDEXES = "INDEXES"
    TOTAL = "TOTAL"
    NONE = "NONE"


class ReturnItemCollectionMetrics(str):
    SIZE = "SIZE"
    NONE = "NONE"


class ReturnValue(str):
    NONE = "NONE"
    ALL_OLD = "ALL_OLD"
    UPDATED_OLD = "UPDATED_OLD"
    ALL_NEW = "ALL_NEW"
    UPDATED_NEW = "UPDATED_NEW"


@dataclasses.dataclass
class SSEDescription(ShapeBase):
    """
    The description of the server-side encryption status on the specified table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "status",
                "Status",
                TypeInfo(typing.Union[str, SSEStatus]),
            ),
            (
                "sse_type",
                "SSEType",
                TypeInfo(typing.Union[str, SSEType]),
            ),
            (
                "kms_master_key_arn",
                "KMSMasterKeyArn",
                TypeInfo(str),
            ),
        ]

    # The current state of server-side encryption:

    #   * `ENABLING` \- Server-side encryption is being enabled.

    #   * `ENABLED` \- Server-side encryption is enabled.

    #   * `DISABLING` \- Server-side encryption is being disabled.

    #   * `DISABLED` \- Server-side encryption is disabled.

    #   * `UPDATING` \- Server-side encryption is being updated.
    status: typing.Union[str, "SSEStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Server-side encryption type:

    #   * `AES256` \- Server-side encryption which uses the AES256 algorithm.

    #   * `KMS` \- Server-side encryption which uses AWS Key Management Service.
    sse_type: typing.Union[str, "SSEType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The KMS master key ARN used for the KMS encryption.
    kms_master_key_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SSESpecification(ShapeBase):
    """
    Represents the settings used to enable server-side encryption.
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
                "sse_type",
                "SSEType",
                TypeInfo(typing.Union[str, SSEType]),
            ),
            (
                "kms_master_key_id",
                "KMSMasterKeyId",
                TypeInfo(str),
            ),
        ]

    # Indicates whether server-side encryption is enabled (true) or disabled
    # (false) on the table.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Server-side encryption type:

    #   * `AES256` \- Server-side encryption which uses the AES256 algorithm.

    #   * `KMS` \- Server-side encryption which uses AWS Key Management Service. (default)
    sse_type: typing.Union[str, "SSEType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The KMS Master Key (CMK) which should be used for the KMS encryption. To
    # specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or
    # alias ARN. Note that you should only provide this parameter if the key is
    # different from the default DynamoDB KMS Master Key alias/aws/dynamodb.
    kms_master_key_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class SSEStatus(str):
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"
    UPDATING = "UPDATING"


class SSEType(str):
    AES256 = "AES256"
    KMS = "KMS"


class ScalarAttributeType(str):
    S = "S"
    N = "N"
    B = "B"


@dataclasses.dataclass
class ScanInput(ShapeBase):
    """
    Represents the input of a `Scan` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "attributes_to_get",
                "AttributesToGet",
                TypeInfo(typing.List[str]),
            ),
            (
                "limit",
                "Limit",
                TypeInfo(int),
            ),
            (
                "select",
                "Select",
                TypeInfo(typing.Union[str, Select]),
            ),
            (
                "scan_filter",
                "ScanFilter",
                TypeInfo(typing.Dict[str, Condition]),
            ),
            (
                "conditional_operator",
                "ConditionalOperator",
                TypeInfo(typing.Union[str, ConditionalOperator]),
            ),
            (
                "exclusive_start_key",
                "ExclusiveStartKey",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "total_segments",
                "TotalSegments",
                TypeInfo(int),
            ),
            (
                "segment",
                "Segment",
                TypeInfo(int),
            ),
            (
                "projection_expression",
                "ProjectionExpression",
                TypeInfo(str),
            ),
            (
                "filter_expression",
                "FilterExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expression_attribute_values",
                "ExpressionAttributeValues",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consistent_read",
                "ConsistentRead",
                TypeInfo(bool),
            ),
        ]

    # The name of the table containing the requested items; or, if you provide
    # `IndexName`, the name of the table to which that index belongs.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of a secondary index to scan. This index can be any local
    # secondary index or global secondary index. Note that if you use the
    # `IndexName` parameter, you must also provide `TableName`.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # This is a legacy parameter. Use `ProjectionExpression` instead. For more
    # information, see
    # [AttributesToGet](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attributes_to_get: typing.List[str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The maximum number of items to evaluate (not necessarily the number of
    # matching items). If DynamoDB processes the number of items up to the limit
    # while processing the results, it stops the operation and returns the
    # matching values up to that point, and a key in `LastEvaluatedKey` to apply
    # in a subsequent operation, so that you can pick up where you left off.
    # Also, if the processed data set size exceeds 1 MB before DynamoDB reaches
    # this limit, it stops the operation and returns the matching values up to
    # the limit, and a key in `LastEvaluatedKey` to apply in a subsequent
    # operation to continue the operation. For more information, see [Query and
    # Scan](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html)
    # in the _Amazon DynamoDB Developer Guide_.
    limit: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The attributes to be returned in the result. You can retrieve all item
    # attributes, specific item attributes, the count of matching items, or in
    # the case of an index, some or all of the attributes projected into the
    # index.

    #   * `ALL_ATTRIBUTES` \- Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.

    #   * `ALL_PROJECTED_ATTRIBUTES` \- Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL_ATTRIBUTES`.

    #   * `COUNT` \- Returns the number of matching items, rather than the matching items themselves.

    #   * `SPECIFIC_ATTRIBUTES` \- Returns only the attributes listed in `AttributesToGet`. This return value is equivalent to specifying `AttributesToGet` without specifying any value for `Select`.

    # If you query or scan a local secondary index and request only attributes
    # that are projected into that index, the operation will read only the index
    # and not the table. If any of the requested attributes are not projected
    # into the local secondary index, DynamoDB will fetch each of these
    # attributes from the parent table. This extra fetching incurs additional
    # throughput cost and latency.

    # If you query or scan a global secondary index, you can only request
    # attributes that are projected into the index. Global secondary index
    # queries cannot fetch attributes from the parent table.

    # If neither `Select` nor `AttributesToGet` are specified, DynamoDB defaults
    # to `ALL_ATTRIBUTES` when accessing a table, and `ALL_PROJECTED_ATTRIBUTES`
    # when accessing an index. You cannot use both `Select` and `AttributesToGet`
    # together in a single request, unless the value for `Select` is
    # `SPECIFIC_ATTRIBUTES`. (This usage is equivalent to specifying
    # `AttributesToGet` without any value for `Select`.)

    # If you use the `ProjectionExpression` parameter, then the value for
    # `Select` can only be `SPECIFIC_ATTRIBUTES`. Any other value for `Select`
    # will return an error.
    select: typing.Union[str, "Select"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `FilterExpression` instead. For more
    # information, see
    # [ScanFilter](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html)
    # in the _Amazon DynamoDB Developer Guide_.
    scan_filter: typing.Dict[str, "Condition"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `FilterExpression` instead. For more
    # information, see
    # [ConditionalOperator](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html)
    # in the _Amazon DynamoDB Developer Guide_.
    conditional_operator: typing.Union[str, "ConditionalOperator"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The primary key of the first item that this operation will evaluate. Use
    # the value that was returned for `LastEvaluatedKey` in the previous
    # operation.

    # The data type for `ExclusiveStartKey` must be String, Number or Binary. No
    # set data types are allowed.

    # In a parallel scan, a `Scan` request that includes `ExclusiveStartKey` must
    # specify the same segment whose previous `Scan` returned the corresponding
    # value of `LastEvaluatedKey`.
    exclusive_start_key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # For a parallel `Scan` request, `TotalSegments` represents the total number
    # of segments into which the `Scan` operation will be divided. The value of
    # `TotalSegments` corresponds to the number of application workers that will
    # perform the parallel scan. For example, if you want to use four application
    # threads to scan a table or an index, specify a `TotalSegments` value of 4.

    # The value for `TotalSegments` must be greater than or equal to 1, and less
    # than or equal to 1000000. If you specify a `TotalSegments` value of 1, the
    # `Scan` operation will be sequential rather than parallel.

    # If you specify `TotalSegments`, you must also specify `Segment`.
    total_segments: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # For a parallel `Scan` request, `Segment` identifies an individual segment
    # to be scanned by an application worker.

    # Segment IDs are zero-based, so the first segment is always 0. For example,
    # if you want to use four application threads to scan a table or an index,
    # then the first thread specifies a `Segment` value of 0, the second thread
    # specifies 1, and so on.

    # The value of `LastEvaluatedKey` returned from a parallel `Scan` request
    # must be used as `ExclusiveStartKey` with the same segment ID in a
    # subsequent `Scan` operation.

    # The value for `Segment` must be greater than or equal to 0, and less than
    # the value provided for `TotalSegments`.

    # If you provide `Segment`, you must also provide `TotalSegments`.
    segment: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that identifies one or more attributes to retrieve from the
    # specified table or index. These attributes can include scalars, sets, or
    # elements of a JSON document. The attributes in the expression must be
    # separated by commas.

    # If no attribute names are specified, then all attributes will be returned.
    # If any of the requested attributes are not found, they will not appear in
    # the result.

    # For more information, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    projection_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A string that contains conditions that DynamoDB applies after the `Scan`
    # operation, but before the data is returned to you. Items that do not
    # satisfy the `FilterExpression` criteria are not returned.

    # A `FilterExpression` is applied after the items have already been read; the
    # process of filtering does not consume any additional read capacity units.

    # For more information, see [Filter
    # Expressions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#FilteringResults)
    # in the _Amazon DynamoDB Developer Guide_.
    filter_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more values that can be substituted in an expression.

    # Use the **:** (colon) character in an expression to dereference an
    # attribute value. For example, suppose that you wanted to check whether the
    # value of the _ProductStatus_ attribute was one of the following:

    # `Available | Backordered | Discontinued`

    # You would first need to specify `ExpressionAttributeValues` as follows:

    # `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"},
    # ":disc":{"S":"Discontinued"} }`

    # You could then use these values in an expression, such as this:

    # `ProductStatus IN (:avail, :back, :disc)`

    # For more information on expression attribute values, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_values: typing.Dict[str, "AttributeValue"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )

    # A Boolean value that determines the read consistency model during the scan:

    #   * If `ConsistentRead` is `false`, then the data returned from `Scan` might not contain the results from other recently completed write operations (PutItem, UpdateItem or DeleteItem).

    #   * If `ConsistentRead` is `true`, then all of the write operations that completed before the `Scan` began are guaranteed to be contained in the `Scan` response.

    # The default setting for `ConsistentRead` is `false`.

    # The `ConsistentRead` parameter is not supported on global secondary
    # indexes. If you scan a global secondary index with `ConsistentRead` set to
    # true, you will receive a `ValidationException`.
    consistent_read: bool = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class ScanOutput(OutputShapeBase):
    """
    Represents the output of a `Scan` operation.
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
                "items",
                "Items",
                TypeInfo(typing.List[typing.Dict[str, AttributeValue]]),
            ),
            (
                "count",
                "Count",
                TypeInfo(int),
            ),
            (
                "scanned_count",
                "ScannedCount",
                TypeInfo(int),
            ),
            (
                "last_evaluated_key",
                "LastEvaluatedKey",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of item attributes that match the scan criteria. Each element in
    # this array consists of an attribute name and the value for that attribute.
    items: typing.List[typing.Dict[str, "AttributeValue"]] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The number of items in the response.

    # If you set `ScanFilter` in the request, then `Count` is the number of items
    # returned after the filter was applied, and `ScannedCount` is the number of
    # matching items before the filter was applied.

    # If you did not use a filter in the request, then `Count` is the same as
    # `ScannedCount`.
    count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of items evaluated, before any `ScanFilter` is applied. A high
    # `ScannedCount` value with few, or no, `Count` results indicates an
    # inefficient `Scan` operation. For more information, see [Count and
    # ScannedCount](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#Count)
    # in the _Amazon DynamoDB Developer Guide_.

    # If you did not use a filter in the request, then `ScannedCount` is the same
    # as `Count`.
    scanned_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The primary key of the item where the operation stopped, inclusive of the
    # previous result set. Use this value to start a new operation, excluding
    # this value in the new request.

    # If `LastEvaluatedKey` is empty, then the "last page" of results has been
    # processed and there is no more data to be retrieved.

    # If `LastEvaluatedKey` is not empty, it does not necessarily mean that there
    # is more data in the result set. The only way to know when you have reached
    # the end of the result set is when `LastEvaluatedKey` is empty.
    last_evaluated_key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `Scan` operation. The data returned
    # includes the total provisioned throughput consumed, along with statistics
    # for the table and any indexes involved in the operation. `ConsumedCapacity`
    # is only returned if the `ReturnConsumedCapacity` parameter was specified.
    # For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    def paginate(self, ) -> typing.Generator["ScanOutput", None, None]:
        yield from super()._paginate()


class Select(str):
    ALL_ATTRIBUTES = "ALL_ATTRIBUTES"
    ALL_PROJECTED_ATTRIBUTES = "ALL_PROJECTED_ATTRIBUTES"
    SPECIFIC_ATTRIBUTES = "SPECIFIC_ATTRIBUTES"
    COUNT = "COUNT"


@dataclasses.dataclass
class SourceTableDetails(ShapeBase):
    """
    Contains the details of the table when the backup was created.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "table_id",
                "TableId",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "table_creation_date_time",
                "TableCreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
            (
                "table_arn",
                "TableArn",
                TypeInfo(str),
            ),
            (
                "table_size_bytes",
                "TableSizeBytes",
                TypeInfo(int),
            ),
            (
                "item_count",
                "ItemCount",
                TypeInfo(int),
            ),
        ]

    # The name of the table for which the backup was created.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the table for which the backup was created.
    table_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Schema of the table.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time when the source table was created.
    table_creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Read IOPs and Write IOPS on the table when the backup was created.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # ARN of the table for which backup was created.
    table_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Size of the table in bytes. Please note this is an approximate value.
    table_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Number of items in the table. Please note this is an approximate value.
    item_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class SourceTableFeatureDetails(ShapeBase):
    """
    Contains the details of the features enabled on the table when the backup was
    created. For example, LSIs, GSIs, streams, TTL.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "local_secondary_indexes",
                "LocalSecondaryIndexes",
                TypeInfo(typing.List[LocalSecondaryIndexInfo]),
            ),
            (
                "global_secondary_indexes",
                "GlobalSecondaryIndexes",
                TypeInfo(typing.List[GlobalSecondaryIndexInfo]),
            ),
            (
                "stream_description",
                "StreamDescription",
                TypeInfo(StreamSpecification),
            ),
            (
                "time_to_live_description",
                "TimeToLiveDescription",
                TypeInfo(TimeToLiveDescription),
            ),
            (
                "sse_description",
                "SSEDescription",
                TypeInfo(SSEDescription),
            ),
        ]

    # Represents the LSI properties for the table when the backup was created. It
    # includes the IndexName, KeySchema and Projection for the LSIs on the table
    # at the time of backup.
    local_secondary_indexes: typing.List["LocalSecondaryIndexInfo"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # Represents the GSI properties for the table when the backup was created. It
    # includes the IndexName, KeySchema, Projection and ProvisionedThroughput for
    # the GSIs on the table at the time of backup.
    global_secondary_indexes: typing.List["GlobalSecondaryIndexInfo"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # Stream settings on the table when the backup was created.
    stream_description: "StreamSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Time to Live settings on the table when the backup was created.
    time_to_live_description: "TimeToLiveDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the server-side encryption status on the table when the
    # backup was created.
    sse_description: "SSEDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class StreamSpecification(ShapeBase):
    """
    Represents the DynamoDB Streams configuration for a table in DynamoDB.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "stream_enabled",
                "StreamEnabled",
                TypeInfo(bool),
            ),
            (
                "stream_view_type",
                "StreamViewType",
                TypeInfo(typing.Union[str, StreamViewType]),
            ),
        ]

    # Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on
    # the table.
    stream_enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # When an item in the table is modified, `StreamViewType` determines what
    # information is written to the stream for this table. Valid values for
    # `StreamViewType` are:

    #   * `KEYS_ONLY` \- Only the key attributes of the modified item are written to the stream.

    #   * `NEW_IMAGE` \- The entire item, as it appears after it was modified, is written to the stream.

    #   * `OLD_IMAGE` \- The entire item, as it appeared before it was modified, is written to the stream.

    #   * `NEW_AND_OLD_IMAGES` \- Both the new and the old item images of the item are written to the stream.
    stream_view_type: typing.Union[str, "StreamViewType"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


class StreamViewType(str):
    NEW_IMAGE = "NEW_IMAGE"
    OLD_IMAGE = "OLD_IMAGE"
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"
    KEYS_ONLY = "KEYS_ONLY"


@dataclasses.dataclass
class TableAlreadyExistsException(ShapeBase):
    """
    A target table with the specified name already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableDescription(ShapeBase):
    """
    Represents the properties of a table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "attribute_definitions",
                "AttributeDefinitions",
                TypeInfo(typing.List[AttributeDefinition]),
            ),
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key_schema",
                "KeySchema",
                TypeInfo(typing.List[KeySchemaElement]),
            ),
            (
                "table_status",
                "TableStatus",
                TypeInfo(typing.Union[str, TableStatus]),
            ),
            (
                "creation_date_time",
                "CreationDateTime",
                TypeInfo(datetime.datetime),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughputDescription),
            ),
            (
                "table_size_bytes",
                "TableSizeBytes",
                TypeInfo(int),
            ),
            (
                "item_count",
                "ItemCount",
                TypeInfo(int),
            ),
            (
                "table_arn",
                "TableArn",
                TypeInfo(str),
            ),
            (
                "table_id",
                "TableId",
                TypeInfo(str),
            ),
            (
                "local_secondary_indexes",
                "LocalSecondaryIndexes",
                TypeInfo(typing.List[LocalSecondaryIndexDescription]),
            ),
            (
                "global_secondary_indexes",
                "GlobalSecondaryIndexes",
                TypeInfo(typing.List[GlobalSecondaryIndexDescription]),
            ),
            (
                "stream_specification",
                "StreamSpecification",
                TypeInfo(StreamSpecification),
            ),
            (
                "latest_stream_label",
                "LatestStreamLabel",
                TypeInfo(str),
            ),
            (
                "latest_stream_arn",
                "LatestStreamArn",
                TypeInfo(str),
            ),
            (
                "restore_summary",
                "RestoreSummary",
                TypeInfo(RestoreSummary),
            ),
            (
                "sse_description",
                "SSEDescription",
                TypeInfo(SSEDescription),
            ),
        ]

    # An array of `AttributeDefinition` objects. Each of these objects describes
    # one attribute in the table and index key schema.

    # Each `AttributeDefinition` object in this array is composed of:

    #   * `AttributeName` \- The name of the attribute.

    #   * `AttributeType` \- The data type for the attribute.
    attribute_definitions: typing.List["AttributeDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The name of the table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The primary key structure for the table. Each `KeySchemaElement` consists
    # of:

    #   * `AttributeName` \- The name of the attribute.

    #   * `KeyType` \- The role of the attribute:

    #     * `HASH` \- partition key

    #     * `RANGE` \- sort key

    # The partition key of an item is also known as its _hash attribute_. The
    # term "hash attribute" derives from DynamoDB' usage of an internal hash
    # function to evenly distribute data items across partitions, based on their
    # partition key values.

    # The sort key of an item is also known as its _range attribute_. The term
    # "range attribute" derives from the way DynamoDB stores items with the same
    # partition key physically close together, in sorted order by the sort key
    # value.

    # For more information about primary keys, see [Primary
    # Key](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModelPrimaryKey)
    # in the _Amazon DynamoDB Developer Guide_.
    key_schema: typing.List["KeySchemaElement"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The current state of the table:

    #   * `CREATING` \- The table is being created.

    #   * `UPDATING` \- The table is being updated.

    #   * `DELETING` \- The table is being deleted.

    #   * `ACTIVE` \- The table is ready for use.
    table_status: typing.Union[str, "TableStatus"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The date and time when the table was created, in [UNIX epoch
    # time](http://www.epochconverter.com/) format.
    creation_date_time: datetime.datetime = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The provisioned throughput settings for the table, consisting of read and
    # write capacity units, along with data about increases and decreases.
    provisioned_throughput: "ProvisionedThroughputDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The total size of the specified table, in bytes. DynamoDB updates this
    # value approximately every six hours. Recent changes might not be reflected
    # in this value.
    table_size_bytes: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The number of items in the specified table. DynamoDB updates this value
    # approximately every six hours. Recent changes might not be reflected in
    # this value.
    item_count: int = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that uniquely identifies the table.
    table_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Unique identifier for the table for which the backup was created.
    table_id: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents one or more local secondary indexes on the table. Each index is
    # scoped to a given partition key value. Tables with one or more local
    # secondary indexes are subject to an item collection size limit, where the
    # amount of data within a given item collection cannot exceed 10 GB. Each
    # element is composed of:

    #   * `IndexName` \- The name of the local secondary index.

    #   * `KeySchema` \- Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.

    #   * `Projection` \- Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:

    #     * `ProjectionType` \- One of the following:

    #       * `KEYS_ONLY` \- Only the index and primary keys are projected into the index.

    #       * `INCLUDE` \- Only the specified table attributes are projected into the index. The list of projected attributes are in `NonKeyAttributes`.

    #       * `ALL` \- All of the table attributes are projected into the index.

    #     * `NonKeyAttributes` \- A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

    #   * `IndexSizeBytes` \- Represents the total size of the index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

    #   * `ItemCount` \- Represents the number of items in the index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

    # If the table is in the `DELETING` state, no information about indexes will
    # be returned.
    local_secondary_indexes: typing.List["LocalSecondaryIndexDescription"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )

    # The global secondary indexes, if any, on the table. Each index is scoped to
    # a given partition key value. Each element is composed of:

    #   * `Backfilling` \- If true, then the index is currently in the backfilling phase. Backfilling occurs only when a new global secondary index is added to the table; it is the process by which DynamoDB populates the new index with data from the table. (This attribute does not appear for indexes that were created during a `CreateTable` operation.)

    #   * `IndexName` \- The name of the global secondary index.

    #   * `IndexSizeBytes` \- The total size of the global secondary index, in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

    #   * `IndexStatus` \- The current status of the global secondary index:

    #     * `CREATING` \- The index is being created.

    #     * `UPDATING` \- The index is being updated.

    #     * `DELETING` \- The index is being deleted.

    #     * `ACTIVE` \- The index is ready for use.

    #   * `ItemCount` \- The number of items in the global secondary index. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.

    #   * `KeySchema` \- Specifies the complete index key schema. The attribute names in the key schema must be between 1 and 255 characters (inclusive). The key schema must begin with the same partition key as the table.

    #   * `Projection` \- Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:

    #     * `ProjectionType` \- One of the following:

    #       * `KEYS_ONLY` \- Only the index and primary keys are projected into the index.

    #       * `INCLUDE` \- Only the specified table attributes are projected into the index. The list of projected attributes are in `NonKeyAttributes`.

    #       * `ALL` \- All of the table attributes are projected into the index.

    #     * `NonKeyAttributes` \- A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in `NonKeyAttributes`, summed across all of the secondary indexes, must not exceed 20. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

    #   * `ProvisionedThroughput` \- The provisioned throughput settings for the global secondary index, consisting of read and write capacity units, along with data about increases and decreases.

    # If the table is in the `DELETING` state, no information about indexes will
    # be returned.
    global_secondary_indexes: typing.List["GlobalSecondaryIndexDescription"
                                         ] = dataclasses.field(
                                             default=ShapeBase.NOT_SET,
                                         )

    # The current DynamoDB Streams configuration for the table.
    stream_specification: "StreamSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A timestamp, in ISO 8601 format, for this stream.

    # Note that `LatestStreamLabel` is not a unique identifier for the stream,
    # because it is possible that a stream from another table might have the same
    # timestamp. However, the combination of the following three elements is
    # guaranteed to be unique:

    #   * the AWS customer ID.

    #   * the table name.

    #   * the `StreamLabel`.
    latest_stream_label: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) that uniquely identifies the latest stream
    # for this table.
    latest_stream_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Contains details for the restore.
    restore_summary: "RestoreSummary" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The description of the server-side encryption status on the specified
    # table.
    sse_description: "SSEDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class TableInUseException(ShapeBase):
    """
    A target table with the specified name is either being created or deleted.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TableNotFoundException(ShapeBase):
    """
    A source table with the name `TableName` does not currently exist within the
    subscriber's account.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TableStatus(str):
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    ACTIVE = "ACTIVE"


@dataclasses.dataclass
class Tag(ShapeBase):
    """
    Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a
    single DynamoDB table.

    AWS-assigned tag names and values are automatically assigned the aws: prefix,
    which the user cannot assign. AWS-assigned tag names do not count towards the
    tag limit of 50. User-assigned tag names have the prefix user: in the Cost
    Allocation Report. You cannot backdate the application of a tag.

    For an overview on tagging DynamoDB resources, see [Tagging for
    DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html)
    in the _Amazon DynamoDB Developer Guide_.
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

    # The key of the tag.Tag keys are case sensitive. Each DynamoDB table can
    # only have up to one tag with the same key. If you try to add an existing
    # tag (same key), the existing tag value will be updated to the new value.
    key: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The value of the tag. Tag values are case-sensitive and can be null.
    value: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TagResourceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tags",
                "Tags",
                TypeInfo(typing.List[Tag]),
            ),
        ]

    # Identifies the Amazon DynamoDB resource to which tags should be added. This
    # value is an Amazon Resource Name (ARN).
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The tags to be assigned to the Amazon DynamoDB resource.
    tags: typing.List["Tag"] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeToLiveDescription(ShapeBase):
    """
    The description of the Time to Live (TTL) status on the specified table.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "time_to_live_status",
                "TimeToLiveStatus",
                TypeInfo(typing.Union[str, TimeToLiveStatus]),
            ),
            (
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
        ]

    # The Time to Live status for the table.
    time_to_live_status: typing.Union[str, "TimeToLiveStatus"
                                     ] = dataclasses.field(
                                         default=ShapeBase.NOT_SET,
                                     )

    # The name of the Time to Live attribute for items in the table.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class TimeToLiveSpecification(ShapeBase):
    """
    Represents the settings used to enable or disable Time to Live for the specified
    table.
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
                "attribute_name",
                "AttributeName",
                TypeInfo(str),
            ),
        ]

    # Indicates whether Time To Live is to be enabled (true) or disabled (false)
    # on the table.
    enabled: bool = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The name of the Time to Live attribute used to store the expiration time
    # for items in the table.
    attribute_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )


class TimeToLiveStatus(str):
    ENABLING = "ENABLING"
    DISABLING = "DISABLING"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


@dataclasses.dataclass
class UntagResourceInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_arn",
                "ResourceArn",
                TypeInfo(str),
            ),
            (
                "tag_keys",
                "TagKeys",
                TypeInfo(typing.List[str]),
            ),
        ]

    # The Amazon DyanamoDB resource the tags will be removed from. This value is
    # an Amazon Resource Name (ARN).
    resource_arn: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of tag keys. Existing tags of the resource whose keys are members of
    # this list will be removed from the Amazon DynamoDB resource.
    tag_keys: typing.List[str] = dataclasses.field(default=ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UpdateContinuousBackupsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "point_in_time_recovery_specification",
                "PointInTimeRecoverySpecification",
                TypeInfo(PointInTimeRecoverySpecification),
            ),
        ]

    # The name of the table.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the settings used to enable point in time recovery.
    point_in_time_recovery_specification: "PointInTimeRecoverySpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateContinuousBackupsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "continuous_backups_description",
                "ContinuousBackupsDescription",
                TypeInfo(ContinuousBackupsDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the continuous backups and point in time recovery settings on
    # the table.
    continuous_backups_description: "ContinuousBackupsDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGlobalSecondaryIndexAction(ShapeBase):
    """
    Represents the new provisioned throughput settings to be applied to a global
    secondary index.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "index_name",
                "IndexName",
                TypeInfo(str),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
        ]

    # The name of the global secondary index to be updated.
    index_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the provisioned throughput settings for the specified global
    # secondary index.

    # For current minimum and maximum provisioned throughput values, see
    # [Limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)
    # in the _Amazon DynamoDB Developer Guide_.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGlobalTableInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "replica_updates",
                "ReplicaUpdates",
                TypeInfo(typing.List[ReplicaUpdate]),
            ),
        ]

    # The global table name.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A list of regions that should be added or removed from the global table.
    replica_updates: typing.List["ReplicaUpdate"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGlobalTableOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_table_description",
                "GlobalTableDescription",
                TypeInfo(GlobalTableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Contains the details of the global table.
    global_table_description: "GlobalTableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateGlobalTableSettingsInput(ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "global_table_provisioned_write_capacity_units",
                "GlobalTableProvisionedWriteCapacityUnits",
                TypeInfo(int),
            ),
            (
                "global_table_provisioned_write_capacity_auto_scaling_settings_update",
                "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate",
                TypeInfo(AutoScalingSettingsUpdate),
            ),
            (
                "global_table_global_secondary_index_settings_update",
                "GlobalTableGlobalSecondaryIndexSettingsUpdate",
                TypeInfo(
                    typing.List[GlobalTableGlobalSecondaryIndexSettingsUpdate]
                ),
            ),
            (
                "replica_settings_update",
                "ReplicaSettingsUpdate",
                TypeInfo(typing.List[ReplicaSettingsUpdate]),
            ),
        ]

    # The name of the global table
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The maximum number of writes consumed per second before DynamoDB returns a
    # `ThrottlingException.`
    global_table_provisioned_write_capacity_units: int = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # AutoScaling settings for managing provisioned write capacity for the global
    # table.
    global_table_provisioned_write_capacity_auto_scaling_settings_update: "AutoScalingSettingsUpdate" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the settings of a global secondary index for a global table that
    # will be modified.
    global_table_global_secondary_index_settings_update: typing.List[
        "GlobalTableGlobalSecondaryIndexSettingsUpdate"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # Represents the settings for a global table in a region that will be
    # modified.
    replica_settings_update: typing.List["ReplicaSettingsUpdate"
                                        ] = dataclasses.field(
                                            default=ShapeBase.NOT_SET,
                                        )


@dataclasses.dataclass
class UpdateGlobalTableSettingsOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "global_table_name",
                "GlobalTableName",
                TypeInfo(str),
            ),
            (
                "replica_settings",
                "ReplicaSettings",
                TypeInfo(typing.List[ReplicaSettingsDescription]),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The name of the global table.
    global_table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The region specific settings for the global table.
    replica_settings: typing.List["ReplicaSettingsDescription"
                                 ] = dataclasses.field(
                                     default=ShapeBase.NOT_SET,
                                 )


@dataclasses.dataclass
class UpdateItemInput(ShapeBase):
    """
    Represents the input of an `UpdateItem` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "key",
                "Key",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "attribute_updates",
                "AttributeUpdates",
                TypeInfo(typing.Dict[str, AttributeValueUpdate]),
            ),
            (
                "expected",
                "Expected",
                TypeInfo(typing.Dict[str, ExpectedAttributeValue]),
            ),
            (
                "conditional_operator",
                "ConditionalOperator",
                TypeInfo(typing.Union[str, ConditionalOperator]),
            ),
            (
                "return_values",
                "ReturnValues",
                TypeInfo(typing.Union[str, ReturnValue]),
            ),
            (
                "return_consumed_capacity",
                "ReturnConsumedCapacity",
                TypeInfo(typing.Union[str, ReturnConsumedCapacity]),
            ),
            (
                "return_item_collection_metrics",
                "ReturnItemCollectionMetrics",
                TypeInfo(typing.Union[str, ReturnItemCollectionMetrics]),
            ),
            (
                "update_expression",
                "UpdateExpression",
                TypeInfo(str),
            ),
            (
                "condition_expression",
                "ConditionExpression",
                TypeInfo(str),
            ),
            (
                "expression_attribute_names",
                "ExpressionAttributeNames",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "expression_attribute_values",
                "ExpressionAttributeValues",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
        ]

    # The name of the table containing the item to update.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # The primary key of the item to be updated. Each element consists of an
    # attribute name and a value for that attribute.

    # For the primary key, you must provide all of the attributes. For example,
    # with a simple primary key, you only need to provide a value for the
    # partition key. For a composite primary key, you must provide values for
    # both the partition key and the sort key.
    key: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `UpdateExpression` instead. For more
    # information, see
    # [AttributeUpdates](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributeUpdates.html)
    # in the _Amazon DynamoDB Developer Guide_.
    attribute_updates: typing.Dict[str, "AttributeValueUpdate"
                                  ] = dataclasses.field(
                                      default=ShapeBase.NOT_SET,
                                  )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [Expected](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expected: typing.Dict[str, "ExpectedAttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # This is a legacy parameter. Use `ConditionExpression` instead. For more
    # information, see
    # [ConditionalOperator](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html)
    # in the _Amazon DynamoDB Developer Guide_.
    conditional_operator: typing.Union[str, "ConditionalOperator"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # Use `ReturnValues` if you want to get the item attributes as they appear
    # before or after they are updated. For `UpdateItem`, the valid values are:

    #   * `NONE` \- If `ReturnValues` is not specified, or if its value is `NONE`, then nothing is returned. (This setting is the default for `ReturnValues`.)

    #   * `ALL_OLD` \- Returns all of the attributes of the item, as they appeared before the UpdateItem operation.

    #   * `UPDATED_OLD` \- Returns only the updated attributes, as they appeared before the UpdateItem operation.

    #   * `ALL_NEW` \- Returns all of the attributes of the item, as they appear after the UpdateItem operation.

    #   * `UPDATED_NEW` \- Returns only the updated attributes, as they appear after the UpdateItem operation.

    # There is no additional cost associated with requesting a return value aside
    # from the small network and processing overhead of receiving a larger
    # response. No read capacity units are consumed.

    # The values returned are strongly consistent.
    return_values: typing.Union[str, "ReturnValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Determines the level of detail about provisioned throughput consumption
    # that is returned in the response:

    #   * `INDEXES` \- The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

    # Note that some operations, such as `GetItem` and `BatchGetItem`, do not
    # access any indexes at all. In these cases, specifying `INDEXES` will only
    # return `ConsumedCapacity` information for table(s).

    #   * `TOTAL` \- The response includes only the aggregate `ConsumedCapacity` for the operation.

    #   * `NONE` \- No `ConsumedCapacity` details are included in the response.
    return_consumed_capacity: typing.Union[str, "ReturnConsumedCapacity"
                                          ] = dataclasses.field(
                                              default=ShapeBase.NOT_SET,
                                          )

    # Determines whether item collection metrics are returned. If set to `SIZE`,
    # the response includes statistics about item collections, if any, that were
    # modified during the operation are returned in the response. If set to
    # `NONE` (the default), no statistics are returned.
    return_item_collection_metrics: typing.Union[
        str, "ReturnItemCollectionMetrics"] = dataclasses.field(
            default=ShapeBase.NOT_SET,
        )

    # An expression that defines one or more attributes to be updated, the action
    # to be performed on them, and new value(s) for them.

    # The following action values are available for `UpdateExpression`.

    #   * `SET` \- Adds one or more attributes and values to an item. If any of these attribute already exist, they are replaced by the new values. You can also use `SET` to add or subtract from an attribute that is of type Number. For example: `SET myNum = myNum + :val`

    # `SET` supports the following functions:

    #     * `if_not_exists (path, operand)` \- if the item does not contain an attribute at the specified path, then `if_not_exists` evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item.

    #     * `list_append (operand, operand)` \- evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands.

    # These function names are case-sensitive.

    #   * `REMOVE` \- Removes one or more attributes from an item.

    #   * `ADD` \- Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of `ADD` depends on the data type of the attribute:

    #     * If the existing attribute is a number, and if `Value` is also a number, then `Value` is mathematically added to the existing attribute. If `Value` is a negative number, then it is subtracted from the existing attribute.

    # If you use `ADD` to increment or decrement a number value for an item that
    # doesn't exist before the update, DynamoDB uses `0` as the initial value.

    # Similarly, if you use `ADD` for an existing item to increment or decrement
    # an attribute value that doesn't exist before the update, DynamoDB uses `0`
    # as the initial value. For example, suppose that the item you want to update
    # doesn't have an attribute named _itemcount_ , but you decide to `ADD` the
    # number `3` to this attribute anyway. DynamoDB will create the _itemcount_
    # attribute, set its initial value to `0`, and finally add `3` to it. The
    # result will be a new _itemcount_ attribute in the item, with a value of
    # `3`.

    #     * If the existing data type is a set and if `Value` is also a set, then `Value` is added to the existing set. For example, if the attribute value is the set `[1,2]`, and the `ADD` action specified `[3]`, then the final attribute value is `[1,2,3]`. An error occurs if an `ADD` action is specified for a set attribute and the attribute type specified does not match the existing set type.

    # Both sets must have the same primitive data type. For example, if the
    # existing data type is a set of strings, the `Value` must also be a set of
    # strings.

    # The `ADD` action only supports Number and set data types. In addition,
    # `ADD` can only be used on top-level attributes, not nested attributes.

    #   * `DELETE` \- Deletes an element from a set.

    # If a set of values is specified, then those values are subtracted from the
    # old set. For example, if the attribute value was the set `[a,b,c]` and the
    # `DELETE` action specifies `[a,c]`, then the final attribute value is `[b]`.
    # Specifying an empty set is an error.

    # The `DELETE` action only supports set data types. In addition, `DELETE` can
    # only be used on top-level attributes, not nested attributes.

    # You can have many actions in a single expression, such as the following:
    # `SET a=:value1, b=:value2 DELETE :value3, :value4, :value5`

    # For more information on update expressions, see [Modifying Items and
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.Modifying.html)
    # in the _Amazon DynamoDB Developer Guide_.
    update_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A condition that must be satisfied in order for a conditional update to
    # succeed.

    # An expression can contain any of the following:

    #   * Functions: `attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size`

    # These function names are case-sensitive.

    #   * Comparison operators: `= | <> | < | > | <= | >= | BETWEEN | IN `

    #   * Logical operators: `AND | OR | NOT`

    # For more information on condition expressions, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    condition_expression: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # One or more substitution tokens for attribute names in an expression. The
    # following are some use cases for using `ExpressionAttributeNames`:

    #   * To access an attribute whose name conflicts with a DynamoDB reserved word.

    #   * To create a placeholder for repeating occurrences of an attribute name in an expression.

    #   * To prevent special characters in an attribute name from being misinterpreted in an expression.

    # Use the **#** character in an expression to dereference an attribute name.
    # For example, consider the following attribute name:

    #   * `Percentile`

    # The name of this attribute conflicts with a reserved word, so it cannot be
    # used directly in an expression. (For the complete list of reserved words,
    # see [Reserved
    # Words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)
    # in the _Amazon DynamoDB Developer Guide_ ). To work around this, you could
    # specify the following for `ExpressionAttributeNames`:

    #   * `{"#P":"Percentile"}`

    # You could then use this substitution in an expression, as in this example:

    #   * `#P = :val`

    # Tokens that begin with the **:** character are _expression attribute
    # values_ , which are placeholders for the actual value at runtime.

    # For more information on expression attribute names, see [Accessing Item
    # Attributes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_names: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # One or more values that can be substituted in an expression.

    # Use the **:** (colon) character in an expression to dereference an
    # attribute value. For example, suppose that you wanted to check whether the
    # value of the _ProductStatus_ attribute was one of the following:

    # `Available | Backordered | Discontinued`

    # You would first need to specify `ExpressionAttributeValues` as follows:

    # `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"},
    # ":disc":{"S":"Discontinued"} }`

    # You could then use these values in an expression, such as this:

    # `ProductStatus IN (:avail, :back, :disc)`

    # For more information on expression attribute values, see [Specifying
    # Conditions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
    # in the _Amazon DynamoDB Developer Guide_.
    expression_attribute_values: typing.Dict[str, "AttributeValue"
                                            ] = dataclasses.field(
                                                default=ShapeBase.NOT_SET,
                                            )


@dataclasses.dataclass
class UpdateItemOutput(OutputShapeBase):
    """
    Represents the output of an `UpdateItem` operation.
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
                "attributes",
                "Attributes",
                TypeInfo(typing.Dict[str, AttributeValue]),
            ),
            (
                "consumed_capacity",
                "ConsumedCapacity",
                TypeInfo(ConsumedCapacity),
            ),
            (
                "item_collection_metrics",
                "ItemCollectionMetrics",
                TypeInfo(ItemCollectionMetrics),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # A map of attribute values as they appear before or after the `UpdateItem`
    # operation, as determined by the `ReturnValues` parameter.

    # The `Attributes` map is only present if `ReturnValues` was specified as
    # something other than `NONE` in the request. Each element represents one
    # attribute.
    attributes: typing.Dict[str, "AttributeValue"] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The capacity units consumed by the `UpdateItem` operation. The data
    # returned includes the total provisioned throughput consumed, along with
    # statistics for the table and any indexes involved in the operation.
    # `ConsumedCapacity` is only returned if the `ReturnConsumedCapacity`
    # parameter was specified. For more information, see [Provisioned
    # Throughput](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html)
    # in the _Amazon DynamoDB Developer Guide_.
    consumed_capacity: "ConsumedCapacity" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Information about item collections, if any, that were affected by the
    # `UpdateItem` operation. `ItemCollectionMetrics` is only returned if the
    # `ReturnItemCollectionMetrics` parameter was specified. If the table does
    # not have any local secondary indexes, this information is not returned in
    # the response.

    # Each `ItemCollectionMetrics` element consists of:

    #   * `ItemCollectionKey` \- The partition key value of the item collection. This is the same as the partition key value of the item itself.

    #   * `SizeEstimateRangeGB` \- An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.

    # The estimate is subject to change over time; therefore, do not rely on the
    # precision or accuracy of the estimate.
    item_collection_metrics: "ItemCollectionMetrics" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTableInput(ShapeBase):
    """
    Represents the input of an `UpdateTable` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "attribute_definitions",
                "AttributeDefinitions",
                TypeInfo(typing.List[AttributeDefinition]),
            ),
            (
                "provisioned_throughput",
                "ProvisionedThroughput",
                TypeInfo(ProvisionedThroughput),
            ),
            (
                "global_secondary_index_updates",
                "GlobalSecondaryIndexUpdates",
                TypeInfo(typing.List[GlobalSecondaryIndexUpdate]),
            ),
            (
                "stream_specification",
                "StreamSpecification",
                TypeInfo(StreamSpecification),
            ),
            (
                "sse_specification",
                "SSESpecification",
                TypeInfo(SSESpecification),
            ),
        ]

    # The name of the table to be updated.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # An array of attributes that describe the key schema for the table and
    # indexes. If you are adding a new global secondary index to the table,
    # `AttributeDefinitions` must include the key element(s) of the new index.
    attribute_definitions: typing.List["AttributeDefinition"
                                      ] = dataclasses.field(
                                          default=ShapeBase.NOT_SET,
                                      )

    # The new provisioned throughput settings for the specified table or index.
    provisioned_throughput: "ProvisionedThroughput" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # An array of one or more global secondary indexes for the table. For each
    # index in the array, you can request one action:

    #   * `Create` \- add a new global secondary index to the table.

    #   * `Update` \- modify the provisioned throughput settings of an existing global secondary index.

    #   * `Delete` \- remove a global secondary index from the table.

    # For more information, see [Managing Global Secondary
    # Indexes](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html)
    # in the _Amazon DynamoDB Developer Guide_.
    global_secondary_index_updates: typing.List["GlobalSecondaryIndexUpdate"
                                               ] = dataclasses.field(
                                                   default=ShapeBase.NOT_SET,
                                               )

    # Represents the DynamoDB Streams configuration for the table.

    # You will receive a `ResourceInUseException` if you attempt to enable a
    # stream on a table that already has a stream, or if you attempt to disable a
    # stream on a table which does not have a stream.
    stream_specification: "StreamSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # The new server-side encryption settings for the specified table.
    sse_specification: "SSESpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTableOutput(OutputShapeBase):
    """
    Represents the output of an `UpdateTable` operation.
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
                "table_description",
                "TableDescription",
                TypeInfo(TableDescription),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the properties of the table.
    table_description: "TableDescription" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTimeToLiveInput(ShapeBase):
    """
    Represents the input of an `UpdateTimeToLive` operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "table_name",
                "TableName",
                TypeInfo(str),
            ),
            (
                "time_to_live_specification",
                "TimeToLiveSpecification",
                TypeInfo(TimeToLiveSpecification),
            ),
        ]

    # The name of the table to be configured.
    table_name: str = dataclasses.field(default=ShapeBase.NOT_SET, )

    # Represents the settings used to enable or disable Time to Live for the
    # specified table.
    time_to_live_specification: "TimeToLiveSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateTimeToLiveOutput(OutputShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_metadata",
                "ResponseMetadata",
                TypeInfo(typing.Dict[str, str]),
            ),
            (
                "time_to_live_specification",
                "TimeToLiveSpecification",
                TypeInfo(TimeToLiveSpecification),
            ),
        ]

    response_metadata: typing.Dict[str, str] = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )

    # Represents the output of an `UpdateTimeToLive` operation.
    time_to_live_specification: "TimeToLiveSpecification" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class WriteRequest(ShapeBase):
    """
    Represents an operation to perform - either `DeleteItem` or `PutItem`. You can
    only request one of these operations, not both, in a single `WriteRequest`. If
    you do need to perform both of these operations, you will need to provide two
    separate `WriteRequest` objects.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "put_request",
                "PutRequest",
                TypeInfo(PutRequest),
            ),
            (
                "delete_request",
                "DeleteRequest",
                TypeInfo(DeleteRequest),
            ),
        ]

    # A request to perform a `PutItem` operation.
    put_request: "PutRequest" = dataclasses.field(default=ShapeBase.NOT_SET, )

    # A request to perform a `DeleteItem` operation.
    delete_request: "DeleteRequest" = dataclasses.field(
        default=ShapeBase.NOT_SET,
    )
