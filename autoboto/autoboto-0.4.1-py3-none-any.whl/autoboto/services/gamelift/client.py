import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("gamelift", *args, **kwargs)

    def accept_match(
        self,
        _request: shapes.AcceptMatchInput = None,
        *,
        ticket_id: str,
        player_ids: typing.List[str],
        acceptance_type: typing.Union[str, shapes.AcceptanceType],
    ) -> shapes.AcceptMatchOutput:
        """
        Registers a player's acceptance or rejection of a proposed FlexMatch match. A
        matchmaking configuration may require player acceptance; if so, then matches
        built with that configuration cannot be completed unless all players accept the
        proposed match within a specified time limit.

        When FlexMatch builds a match, all the matchmaking tickets involved in the
        proposed match are placed into status `REQUIRES_ACCEPTANCE`. This is a trigger
        for your game to get acceptance from all players in the ticket. Acceptances are
        only valid for tickets when they are in this status; all other acceptances
        result in an error.

        To register acceptance, specify the ticket ID, a response, and one or more
        players. Once all players have registered acceptance, the matchmaking tickets
        advance to status `PLACING`, where a new game session is created for the match.

        If any player rejects the match, or if acceptances are not received before a
        specified timeout, the proposed match is dropped. The matchmaking tickets are
        then handled in one of two ways: For tickets where all players accepted the
        match, the ticket status is returned to `SEARCHING` to find a new match. For
        tickets where one or more players failed to accept the match, the ticket status
        is set to `FAILED`, and processing is terminated. A new matchmaking request for
        these players can be submitted as needed.

        Matchmaking-related operations include:

          * StartMatchmaking

          * DescribeMatchmaking

          * StopMatchmaking

          * AcceptMatch

          * StartMatchBackfill
        """
        if _request is None:
            _params = {}
            if ticket_id is not ShapeBase.NOT_SET:
                _params['ticket_id'] = ticket_id
            if player_ids is not ShapeBase.NOT_SET:
                _params['player_ids'] = player_ids
            if acceptance_type is not ShapeBase.NOT_SET:
                _params['acceptance_type'] = acceptance_type
            _request = shapes.AcceptMatchInput(**_params)
        response = self._boto_client.accept_match(**_request.to_boto())

        return shapes.AcceptMatchOutput.from_boto(response)

    def create_alias(
        self,
        _request: shapes.CreateAliasInput = None,
        *,
        name: str,
        routing_strategy: shapes.RoutingStrategy,
        description: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateAliasOutput:
        """
        Creates an alias for a fleet. In most situations, you can use an alias ID in
        place of a fleet ID. By using a fleet alias instead of a specific fleet ID, you
        can switch gameplay and players to a new fleet without changing your game client
        or other game components. For example, for games in production, using an alias
        allows you to seamlessly redirect your player base to a new game server update.

        Amazon GameLift supports two types of routing strategies for aliases: simple and
        terminal. A simple alias points to an active fleet. A terminal alias is used to
        display messaging or link to a URL instead of routing players to an active
        fleet. For example, you might use a terminal alias when a game version is no
        longer supported and you want to direct players to an upgrade site.

        To create a fleet alias, specify an alias name, routing strategy, and optional
        description. Each simple alias can point to only one fleet, but a fleet can have
        multiple aliases. If successful, a new alias record is returned, including an
        alias ID, which you can reference when creating a game session. You can reassign
        an alias to another fleet by calling `UpdateAlias`.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if routing_strategy is not ShapeBase.NOT_SET:
                _params['routing_strategy'] = routing_strategy
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            _request = shapes.CreateAliasInput(**_params)
        response = self._boto_client.create_alias(**_request.to_boto())

        return shapes.CreateAliasOutput.from_boto(response)

    def create_build(
        self,
        _request: shapes.CreateBuildInput = None,
        *,
        name: str = ShapeBase.NOT_SET,
        version: str = ShapeBase.NOT_SET,
        storage_location: shapes.S3Location = ShapeBase.NOT_SET,
        operating_system: typing.Union[str, shapes.OperatingSystem] = ShapeBase.
        NOT_SET,
    ) -> shapes.CreateBuildOutput:
        """
        Creates a new Amazon GameLift build record for your game server binary files and
        points to the location of your game server build files in an Amazon Simple
        Storage Service (Amazon S3) location.

        Game server binaries must be combined into a `.zip` file for use with Amazon
        GameLift. See [Uploading Your
        Game](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-
        intro.html) for more information.

        To create new builds quickly and easily, use the AWS CLI command **[upload-
        build](http://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-
        build.html) **. This helper command uploads your build and creates a new build
        record in one step, and automatically handles the necessary permissions. See [
        Upload Build Files to Amazon
        GameLift](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-
        build-cli-uploading.html) for more help.

        The `CreateBuild` operation should be used only when you need to manually upload
        your build files, as in the following scenarios:

          * Store a build file in an Amazon S3 bucket under your own AWS account. To use this option, you must first give Amazon GameLift access to that Amazon S3 bucket. See [ Create a Build with Files in Amazon S3](http://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build) for detailed help. To create a new build record using files in your Amazon S3 bucket, call `CreateBuild` and specify a build name, operating system, and the storage location of your game build.

          * Upload a build file directly to Amazon GameLift's Amazon S3 account. To use this option, you first call `CreateBuild` with a build name and operating system. This action creates a new build record and returns an Amazon S3 storage location (bucket and key only) and temporary access credentials. Use the credentials to manually upload your build file to the storage location (see the Amazon S3 topic [Uploading Objects](http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html)). You can upload files to a location only once. 

        If successful, this operation creates a new build record with a unique build ID
        and places it in `INITIALIZED` status. You can use DescribeBuild to check the
        status of your build. A build must be in `READY` status before it can be used to
        create fleets.

        Build-related operations include:

          * CreateBuild

          * ListBuilds

          * DescribeBuild

          * UpdateBuild

          * DeleteBuild
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            if storage_location is not ShapeBase.NOT_SET:
                _params['storage_location'] = storage_location
            if operating_system is not ShapeBase.NOT_SET:
                _params['operating_system'] = operating_system
            _request = shapes.CreateBuildInput(**_params)
        response = self._boto_client.create_build(**_request.to_boto())

        return shapes.CreateBuildOutput.from_boto(response)

    def create_fleet(
        self,
        _request: shapes.CreateFleetInput = None,
        *,
        name: str,
        build_id: str,
        ec2_instance_type: typing.Union[str, shapes.EC2InstanceType],
        description: str = ShapeBase.NOT_SET,
        server_launch_path: str = ShapeBase.NOT_SET,
        server_launch_parameters: str = ShapeBase.NOT_SET,
        log_paths: typing.List[str] = ShapeBase.NOT_SET,
        ec2_inbound_permissions: typing.List[shapes.IpPermission
                                            ] = ShapeBase.NOT_SET,
        new_game_session_protection_policy: typing.
        Union[str, shapes.ProtectionPolicy] = ShapeBase.NOT_SET,
        runtime_configuration: shapes.RuntimeConfiguration = ShapeBase.NOT_SET,
        resource_creation_limit_policy: shapes.
        ResourceCreationLimitPolicy = ShapeBase.NOT_SET,
        metric_groups: typing.List[str] = ShapeBase.NOT_SET,
        peer_vpc_aws_account_id: str = ShapeBase.NOT_SET,
        peer_vpc_id: str = ShapeBase.NOT_SET,
        fleet_type: typing.Union[str, shapes.FleetType] = ShapeBase.NOT_SET,
    ) -> shapes.CreateFleetOutput:
        """
        Creates a new fleet to run your game servers. A fleet is a set of Amazon Elastic
        Compute Cloud (Amazon EC2) instances, each of which can run multiple server
        processes to host game sessions. You set up a fleet to use instances with
        certain hardware specifications (see [Amazon EC2 Instance
        Types](http://aws.amazon.com/ec2/instance-types/) for more information), and
        deploy your game build to run on each instance.

        To create a new fleet, you must specify the following: (1) a fleet name, (2) the
        build ID of a successfully uploaded game build, (3) an EC2 instance type, and
        (4) a run-time configuration, which describes the server processes to run on
        each instance in the fleet. If you don't specify a fleet type (on-demand or
        spot), the new fleet uses on-demand instances by default.

        You can also configure the new fleet with the following settings:

          * Fleet description

          * Access permissions for inbound traffic

          * Fleet-wide game session protection

          * Resource usage limits

          * VPC peering connection (see [VPC Peering with Amazon GameLift Fleets](http://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html))

        If you use Amazon CloudWatch for metrics, you can add the new fleet to a metric
        group. By adding multiple fleets to a metric group, you can view aggregated
        metrics for all the fleets in the group.

        If the `CreateFleet` call is successful, Amazon GameLift performs the following
        tasks. You can track the process of a fleet by checking the fleet status or by
        monitoring fleet creation events:

          * Creates a fleet record. Status: `NEW`.

          * Begins writing events to the fleet event log, which can be accessed in the Amazon GameLift console.

        Sets the fleet's target capacity to 1 (desired instances), which triggers Amazon
        GameLift to start one new EC2 instance.

          * Downloads the game build to the new instance and installs it. Statuses: `DOWNLOADING`, `VALIDATING`, `BUILDING`. 

          * Starts launching server processes on the instance. If the fleet is configured to run multiple server processes per instance, Amazon GameLift staggers each launch by a few seconds. Status: `ACTIVATING`.

          * Sets the fleet's status to `ACTIVE` as soon as one server process is ready to host a game session.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            if ec2_instance_type is not ShapeBase.NOT_SET:
                _params['ec2_instance_type'] = ec2_instance_type
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if server_launch_path is not ShapeBase.NOT_SET:
                _params['server_launch_path'] = server_launch_path
            if server_launch_parameters is not ShapeBase.NOT_SET:
                _params['server_launch_parameters'] = server_launch_parameters
            if log_paths is not ShapeBase.NOT_SET:
                _params['log_paths'] = log_paths
            if ec2_inbound_permissions is not ShapeBase.NOT_SET:
                _params['ec2_inbound_permissions'] = ec2_inbound_permissions
            if new_game_session_protection_policy is not ShapeBase.NOT_SET:
                _params['new_game_session_protection_policy'
                       ] = new_game_session_protection_policy
            if runtime_configuration is not ShapeBase.NOT_SET:
                _params['runtime_configuration'] = runtime_configuration
            if resource_creation_limit_policy is not ShapeBase.NOT_SET:
                _params['resource_creation_limit_policy'
                       ] = resource_creation_limit_policy
            if metric_groups is not ShapeBase.NOT_SET:
                _params['metric_groups'] = metric_groups
            if peer_vpc_aws_account_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_aws_account_id'] = peer_vpc_aws_account_id
            if peer_vpc_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_id'] = peer_vpc_id
            if fleet_type is not ShapeBase.NOT_SET:
                _params['fleet_type'] = fleet_type
            _request = shapes.CreateFleetInput(**_params)
        response = self._boto_client.create_fleet(**_request.to_boto())

        return shapes.CreateFleetOutput.from_boto(response)

    def create_game_session(
        self,
        _request: shapes.CreateGameSessionInput = None,
        *,
        maximum_player_session_count: int,
        fleet_id: str = ShapeBase.NOT_SET,
        alias_id: str = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        game_properties: typing.List[shapes.GameProperty] = ShapeBase.NOT_SET,
        creator_id: str = ShapeBase.NOT_SET,
        game_session_id: str = ShapeBase.NOT_SET,
        idempotency_token: str = ShapeBase.NOT_SET,
        game_session_data: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateGameSessionOutput:
        """
        Creates a multiplayer game session for players. This action creates a game
        session record and assigns an available server process in the specified fleet to
        host the game session. A fleet must have an `ACTIVE` status before a game
        session can be created in it.

        To create a game session, specify either fleet ID or alias ID and indicate a
        maximum number of players to allow in the game session. You can also provide a
        name and game-specific properties for this game session. If successful, a
        GameSession object is returned containing the game session properties and other
        settings you specified.

        **Idempotency tokens.** You can add a token that uniquely identifies game
        session requests. This is useful for ensuring that game session requests are
        idempotent. Multiple requests with the same idempotency token are processed only
        once; subsequent requests return the original result. All response values are
        the same with the exception of game session status, which may change.

        **Resource creation limits.** If you are creating a game session on a fleet with
        a resource creation limit policy in force, then you must specify a creator ID.
        Without this ID, Amazon GameLift has no way to evaluate the policy for this new
        game session request.

        **Player acceptance policy.** By default, newly created game sessions are open
        to new players. You can restrict new player access by using UpdateGameSession to
        change the game session's player session creation policy.

        **Game session logs.** Logs are retained for all active game sessions for 14
        days. To access the logs, call GetGameSessionLogUrl to download the log files.

        _Available in Amazon GameLift Local._

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if maximum_player_session_count is not ShapeBase.NOT_SET:
                _params['maximum_player_session_count'
                       ] = maximum_player_session_count
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if game_properties is not ShapeBase.NOT_SET:
                _params['game_properties'] = game_properties
            if creator_id is not ShapeBase.NOT_SET:
                _params['creator_id'] = creator_id
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if idempotency_token is not ShapeBase.NOT_SET:
                _params['idempotency_token'] = idempotency_token
            if game_session_data is not ShapeBase.NOT_SET:
                _params['game_session_data'] = game_session_data
            _request = shapes.CreateGameSessionInput(**_params)
        response = self._boto_client.create_game_session(**_request.to_boto())

        return shapes.CreateGameSessionOutput.from_boto(response)

    def create_game_session_queue(
        self,
        _request: shapes.CreateGameSessionQueueInput = None,
        *,
        name: str,
        timeout_in_seconds: int = ShapeBase.NOT_SET,
        player_latency_policies: typing.List[shapes.PlayerLatencyPolicy
                                            ] = ShapeBase.NOT_SET,
        destinations: typing.List[shapes.GameSessionQueueDestination
                                 ] = ShapeBase.NOT_SET,
    ) -> shapes.CreateGameSessionQueueOutput:
        """
        Establishes a new queue for processing requests to place new game sessions. A
        queue identifies where new game sessions can be hosted -- by specifying a list
        of destinations (fleets or aliases) -- and how long requests can wait in the
        queue before timing out. You can set up a queue to try to place game sessions on
        fleets in multiple regions. To add placement requests to a queue, call
        StartGameSessionPlacement and reference the queue name.

        **Destination order.** When processing a request for a game session, Amazon
        GameLift tries each destination in order until it finds one with available
        resources to host the new game session. A queue's default order is determined by
        how destinations are listed. The default order is overridden when a game session
        placement request provides player latency information. Player latency
        information enables Amazon GameLift to prioritize destinations where players
        report the lowest average latency, as a result placing the new game session
        where the majority of players will have the best possible gameplay experience.

        **Player latency policies.** For placement requests containing player latency
        information, use player latency policies to protect individual players from very
        high latencies. With a latency cap, even when a destination can deliver a low
        latency for most players, the game is not placed where any individual player is
        reporting latency higher than a policy's maximum. A queue can have multiple
        latency policies, which are enforced consecutively starting with the policy with
        the lowest latency cap. Use multiple policies to gradually relax latency
        controls; for example, you might set a policy with a low latency cap for the
        first 60 seconds, a second policy with a higher cap for the next 60 seconds,
        etc.

        To create a new queue, provide a name, timeout value, a list of destinations
        and, if desired, a set of latency policies. If successful, a new queue object is
        returned.

        Queue-related operations include:

          * CreateGameSessionQueue

          * DescribeGameSessionQueues

          * UpdateGameSessionQueue

          * DeleteGameSessionQueue
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if timeout_in_seconds is not ShapeBase.NOT_SET:
                _params['timeout_in_seconds'] = timeout_in_seconds
            if player_latency_policies is not ShapeBase.NOT_SET:
                _params['player_latency_policies'] = player_latency_policies
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            _request = shapes.CreateGameSessionQueueInput(**_params)
        response = self._boto_client.create_game_session_queue(
            **_request.to_boto()
        )

        return shapes.CreateGameSessionQueueOutput.from_boto(response)

    def create_matchmaking_configuration(
        self,
        _request: shapes.CreateMatchmakingConfigurationInput = None,
        *,
        name: str,
        game_session_queue_arns: typing.List[str],
        request_timeout_seconds: int,
        acceptance_required: bool,
        rule_set_name: str,
        description: str = ShapeBase.NOT_SET,
        acceptance_timeout_seconds: int = ShapeBase.NOT_SET,
        notification_target: str = ShapeBase.NOT_SET,
        additional_player_count: int = ShapeBase.NOT_SET,
        custom_event_data: str = ShapeBase.NOT_SET,
        game_properties: typing.List[shapes.GameProperty] = ShapeBase.NOT_SET,
        game_session_data: str = ShapeBase.NOT_SET,
    ) -> shapes.CreateMatchmakingConfigurationOutput:
        """
        Defines a new matchmaking configuration for use with FlexMatch. A matchmaking
        configuration sets out guidelines for matching players and getting the matches
        into games. You can set up multiple matchmaking configurations to handle the
        scenarios needed for your game. Each matchmaking ticket (StartMatchmaking or
        StartMatchBackfill) specifies a configuration for the match and provides player
        attributes to support the configuration being used.

        To create a matchmaking configuration, at a minimum you must specify the
        following: configuration name; a rule set that governs how to evaluate players
        and find acceptable matches; a game session queue to use when placing a new game
        session for the match; and the maximum time allowed for a matchmaking attempt.

        **Player acceptance** \-- In each configuration, you have the option to require
        that all players accept participation in a proposed match. To enable this
        feature, set _AcceptanceRequired_ to true and specify a time limit for player
        acceptance. Players have the option to accept or reject a proposed match, and a
        match does not move ahead to game session placement unless all matched players
        accept.

        **Matchmaking status notification** \-- There are two ways to track the progress
        of matchmaking tickets: (1) polling ticket status with DescribeMatchmaking; or
        (2) receiving notifications with Amazon Simple Notification Service (SNS). To
        use notifications, you first need to set up an SNS topic to receive the
        notifications, and provide the topic ARN in the matchmaking configuration (see [
        Setting up Notifications for
        Matchmaking](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
        notification.html)). Since notifications promise only "best effort" delivery, we
        recommend calling `DescribeMatchmaking` if no notifications are received within
        30 seconds.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if game_session_queue_arns is not ShapeBase.NOT_SET:
                _params['game_session_queue_arns'] = game_session_queue_arns
            if request_timeout_seconds is not ShapeBase.NOT_SET:
                _params['request_timeout_seconds'] = request_timeout_seconds
            if acceptance_required is not ShapeBase.NOT_SET:
                _params['acceptance_required'] = acceptance_required
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if acceptance_timeout_seconds is not ShapeBase.NOT_SET:
                _params['acceptance_timeout_seconds'
                       ] = acceptance_timeout_seconds
            if notification_target is not ShapeBase.NOT_SET:
                _params['notification_target'] = notification_target
            if additional_player_count is not ShapeBase.NOT_SET:
                _params['additional_player_count'] = additional_player_count
            if custom_event_data is not ShapeBase.NOT_SET:
                _params['custom_event_data'] = custom_event_data
            if game_properties is not ShapeBase.NOT_SET:
                _params['game_properties'] = game_properties
            if game_session_data is not ShapeBase.NOT_SET:
                _params['game_session_data'] = game_session_data
            _request = shapes.CreateMatchmakingConfigurationInput(**_params)
        response = self._boto_client.create_matchmaking_configuration(
            **_request.to_boto()
        )

        return shapes.CreateMatchmakingConfigurationOutput.from_boto(response)

    def create_matchmaking_rule_set(
        self,
        _request: shapes.CreateMatchmakingRuleSetInput = None,
        *,
        name: str,
        rule_set_body: str,
    ) -> shapes.CreateMatchmakingRuleSetOutput:
        """
        Creates a new rule set for FlexMatch matchmaking. A rule set describes the type
        of match to create, such as the number and size of teams, and sets the
        parameters for acceptable player matches, such as minimum skill level or
        character type. Rule sets are used in matchmaking configurations, which define
        how matchmaking requests are handled. Each MatchmakingConfiguration uses one
        rule set; you can set up multiple rule sets to handle the scenarios that suit
        your game (such as for different game modes), and create a separate matchmaking
        configuration for each rule set. See additional information on rule set content
        in the MatchmakingRuleSet structure. For help creating rule sets, including
        useful examples, see the topic [ Adding FlexMatch to Your
        Game](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
        intro.html).

        Once created, matchmaking rule sets cannot be changed or deleted, so we
        recommend checking the rule set syntax using ValidateMatchmakingRuleSet before
        creating the rule set.

        To create a matchmaking rule set, provide the set of rules and a unique name.
        Rule sets must be defined in the same region as the matchmaking configuration
        they will be used with. Rule sets cannot be edited or deleted. If you need to
        change a rule set, create a new one with the necessary edits and then update
        matchmaking configurations to use the new rule set.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if rule_set_body is not ShapeBase.NOT_SET:
                _params['rule_set_body'] = rule_set_body
            _request = shapes.CreateMatchmakingRuleSetInput(**_params)
        response = self._boto_client.create_matchmaking_rule_set(
            **_request.to_boto()
        )

        return shapes.CreateMatchmakingRuleSetOutput.from_boto(response)

    def create_player_session(
        self,
        _request: shapes.CreatePlayerSessionInput = None,
        *,
        game_session_id: str,
        player_id: str,
        player_data: str = ShapeBase.NOT_SET,
    ) -> shapes.CreatePlayerSessionOutput:
        """
        Adds a player to a game session and creates a player session record. Before a
        player can be added, a game session must have an `ACTIVE` status, have a
        creation policy of `ALLOW_ALL`, and have an open player slot. To add a group of
        players to a game session, use CreatePlayerSessions.

        To create a player session, specify a game session ID, player ID, and optionally
        a string of player data. If successful, the player is added to the game session
        and a new PlayerSession object is returned. Player sessions cannot be updated.

        _Available in Amazon GameLift Local._

        Player-session-related operations include:

          * CreatePlayerSession

          * CreatePlayerSessions

          * DescribePlayerSessions

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if player_id is not ShapeBase.NOT_SET:
                _params['player_id'] = player_id
            if player_data is not ShapeBase.NOT_SET:
                _params['player_data'] = player_data
            _request = shapes.CreatePlayerSessionInput(**_params)
        response = self._boto_client.create_player_session(**_request.to_boto())

        return shapes.CreatePlayerSessionOutput.from_boto(response)

    def create_player_sessions(
        self,
        _request: shapes.CreatePlayerSessionsInput = None,
        *,
        game_session_id: str,
        player_ids: typing.List[str],
        player_data_map: typing.Dict[str, str] = ShapeBase.NOT_SET,
    ) -> shapes.CreatePlayerSessionsOutput:
        """
        Adds a group of players to a game session. This action is useful with a team
        matching feature. Before players can be added, a game session must have an
        `ACTIVE` status, have a creation policy of `ALLOW_ALL`, and have an open player
        slot. To add a single player to a game session, use CreatePlayerSession.

        To create player sessions, specify a game session ID, a list of player IDs, and
        optionally a set of player data strings. If successful, the players are added to
        the game session and a set of new PlayerSession objects is returned. Player
        sessions cannot be updated.

        _Available in Amazon GameLift Local._

        Player-session-related operations include:

          * CreatePlayerSession

          * CreatePlayerSessions

          * DescribePlayerSessions

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if player_ids is not ShapeBase.NOT_SET:
                _params['player_ids'] = player_ids
            if player_data_map is not ShapeBase.NOT_SET:
                _params['player_data_map'] = player_data_map
            _request = shapes.CreatePlayerSessionsInput(**_params)
        response = self._boto_client.create_player_sessions(
            **_request.to_boto()
        )

        return shapes.CreatePlayerSessionsOutput.from_boto(response)

    def create_vpc_peering_authorization(
        self,
        _request: shapes.CreateVpcPeeringAuthorizationInput = None,
        *,
        game_lift_aws_account_id: str,
        peer_vpc_id: str,
    ) -> shapes.CreateVpcPeeringAuthorizationOutput:
        """
        Requests authorization to create or delete a peer connection between the VPC for
        your Amazon GameLift fleet and a virtual private cloud (VPC) in your AWS
        account. VPC peering enables the game servers on your fleet to communicate
        directly with other AWS resources. Once you've received authorization, call
        CreateVpcPeeringConnection to establish the peering connection. For more
        information, see [VPC Peering with Amazon GameLift
        Fleets](http://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-
        peering.html).

        You can peer with VPCs that are owned by any AWS account you have access to,
        including the account that you use to manage your Amazon GameLift fleets. You
        cannot peer with VPCs that are in different regions.

        To request authorization to create a connection, call this operation from the
        AWS account with the VPC that you want to peer to your Amazon GameLift fleet.
        For example, to enable your game servers to retrieve data from a DynamoDB table,
        use the account that manages that DynamoDB resource. Identify the following
        values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the
        AWS account that you use to manage Amazon GameLift. If successful, VPC peering
        is authorized for the specified VPC.

        To request authorization to delete a connection, call this operation from the
        AWS account with the VPC that is peered with your Amazon GameLift fleet.
        Identify the following values: (1) VPC ID that you want to delete the peering
        connection for, and (2) ID of the AWS account that you use to manage Amazon
        GameLift.

        The authorization remains valid for 24 hours unless it is canceled by a call to
        DeleteVpcPeeringAuthorization. You must create or delete the peering connection
        while the authorization is valid.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            if game_lift_aws_account_id is not ShapeBase.NOT_SET:
                _params['game_lift_aws_account_id'] = game_lift_aws_account_id
            if peer_vpc_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_id'] = peer_vpc_id
            _request = shapes.CreateVpcPeeringAuthorizationInput(**_params)
        response = self._boto_client.create_vpc_peering_authorization(
            **_request.to_boto()
        )

        return shapes.CreateVpcPeeringAuthorizationOutput.from_boto(response)

    def create_vpc_peering_connection(
        self,
        _request: shapes.CreateVpcPeeringConnectionInput = None,
        *,
        fleet_id: str,
        peer_vpc_aws_account_id: str,
        peer_vpc_id: str,
    ) -> shapes.CreateVpcPeeringConnectionOutput:
        """
        Establishes a VPC peering connection between a virtual private cloud (VPC) in an
        AWS account with the VPC for your Amazon GameLift fleet. VPC peering enables the
        game servers on your fleet to communicate directly with other AWS resources. You
        can peer with VPCs in any AWS account that you have access to, including the
        account that you use to manage your Amazon GameLift fleets. You cannot peer with
        VPCs that are in different regions. For more information, see [VPC Peering with
        Amazon GameLift
        Fleets](http://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-
        peering.html).

        Before calling this operation to establish the peering connection, you first
        need to call CreateVpcPeeringAuthorization and identify the VPC you want to peer
        with. Once the authorization for the specified VPC is issued, you have 24 hours
        to establish the connection. These two operations handle all tasks necessary to
        peer the two VPCs, including acceptance, updating routing tables, etc.

        To establish the connection, call this operation from the AWS account that is
        used to manage the Amazon GameLift fleets. Identify the following values: (1)
        The ID of the fleet you want to be enable a VPC peering connection for; (2) The
        AWS account with the VPC that you want to peer with; and (3) The ID of the VPC
        you want to peer with. This operation is asynchronous. If successful, a
        VpcPeeringConnection request is created. You can use continuous polling to track
        the request's status using DescribeVpcPeeringConnections, or by monitoring fleet
        events for success or failure using DescribeFleetEvents.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if peer_vpc_aws_account_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_aws_account_id'] = peer_vpc_aws_account_id
            if peer_vpc_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_id'] = peer_vpc_id
            _request = shapes.CreateVpcPeeringConnectionInput(**_params)
        response = self._boto_client.create_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.CreateVpcPeeringConnectionOutput.from_boto(response)

    def delete_alias(
        self,
        _request: shapes.DeleteAliasInput = None,
        *,
        alias_id: str,
    ) -> None:
        """
        Deletes an alias. This action removes all record of the alias. Game clients
        attempting to access a server process using the deleted alias receive an error.
        To delete an alias, specify the alias ID to be deleted.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            _request = shapes.DeleteAliasInput(**_params)
        response = self._boto_client.delete_alias(**_request.to_boto())

    def delete_build(
        self,
        _request: shapes.DeleteBuildInput = None,
        *,
        build_id: str,
    ) -> None:
        """
        Deletes a build. This action permanently deletes the build record and any
        uploaded build files.

        To delete a build, specify its ID. Deleting a build does not affect the status
        of any active fleets using the build, but you can no longer create new fleets
        with the deleted build.

        Build-related operations include:

          * CreateBuild

          * ListBuilds

          * DescribeBuild

          * UpdateBuild

          * DeleteBuild
        """
        if _request is None:
            _params = {}
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            _request = shapes.DeleteBuildInput(**_params)
        response = self._boto_client.delete_build(**_request.to_boto())

    def delete_fleet(
        self,
        _request: shapes.DeleteFleetInput = None,
        *,
        fleet_id: str,
    ) -> None:
        """
        Deletes everything related to a fleet. Before deleting a fleet, you must set the
        fleet's desired capacity to zero. See UpdateFleetCapacity.

        This action removes the fleet's resources and the fleet record. Once a fleet is
        deleted, you can no longer use that fleet.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            _request = shapes.DeleteFleetInput(**_params)
        response = self._boto_client.delete_fleet(**_request.to_boto())

    def delete_game_session_queue(
        self,
        _request: shapes.DeleteGameSessionQueueInput = None,
        *,
        name: str,
    ) -> shapes.DeleteGameSessionQueueOutput:
        """
        Deletes a game session queue. This action means that any
        StartGameSessionPlacement requests that reference this queue will fail. To
        delete a queue, specify the queue name.

        Queue-related operations include:

          * CreateGameSessionQueue

          * DescribeGameSessionQueues

          * UpdateGameSessionQueue

          * DeleteGameSessionQueue
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteGameSessionQueueInput(**_params)
        response = self._boto_client.delete_game_session_queue(
            **_request.to_boto()
        )

        return shapes.DeleteGameSessionQueueOutput.from_boto(response)

    def delete_matchmaking_configuration(
        self,
        _request: shapes.DeleteMatchmakingConfigurationInput = None,
        *,
        name: str,
    ) -> shapes.DeleteMatchmakingConfigurationOutput:
        """
        Permanently removes a FlexMatch matchmaking configuration. To delete, specify
        the configuration name. A matchmaking configuration cannot be deleted if it is
        being used in any active matchmaking tickets.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteMatchmakingConfigurationInput(**_params)
        response = self._boto_client.delete_matchmaking_configuration(
            **_request.to_boto()
        )

        return shapes.DeleteMatchmakingConfigurationOutput.from_boto(response)

    def delete_scaling_policy(
        self,
        _request: shapes.DeleteScalingPolicyInput = None,
        *,
        name: str,
        fleet_id: str,
    ) -> None:
        """
        Deletes a fleet scaling policy. This action means that the policy is no longer
        in force and removes all record of it. To delete a scaling policy, specify both
        the scaling policy name and the fleet ID it is associated with.

        To temporarily suspend scaling policies, call StopFleetActions. This operation
        suspends all policies for the fleet.

        Operations related to fleet capacity scaling include:

          * DescribeFleetCapacity

          * UpdateFleetCapacity

          * DescribeEC2InstanceLimits

          * Manage scaling policies:

            * PutScalingPolicy (auto-scaling)

            * DescribeScalingPolicies (auto-scaling)

            * DeleteScalingPolicy (auto-scaling)

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            _request = shapes.DeleteScalingPolicyInput(**_params)
        response = self._boto_client.delete_scaling_policy(**_request.to_boto())

    def delete_vpc_peering_authorization(
        self,
        _request: shapes.DeleteVpcPeeringAuthorizationInput = None,
        *,
        game_lift_aws_account_id: str,
        peer_vpc_id: str,
    ) -> shapes.DeleteVpcPeeringAuthorizationOutput:
        """
        Cancels a pending VPC peering authorization for the specified VPC. If the
        authorization has already been used to create a peering connection, call
        DeleteVpcPeeringConnection to remove the connection.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            if game_lift_aws_account_id is not ShapeBase.NOT_SET:
                _params['game_lift_aws_account_id'] = game_lift_aws_account_id
            if peer_vpc_id is not ShapeBase.NOT_SET:
                _params['peer_vpc_id'] = peer_vpc_id
            _request = shapes.DeleteVpcPeeringAuthorizationInput(**_params)
        response = self._boto_client.delete_vpc_peering_authorization(
            **_request.to_boto()
        )

        return shapes.DeleteVpcPeeringAuthorizationOutput.from_boto(response)

    def delete_vpc_peering_connection(
        self,
        _request: shapes.DeleteVpcPeeringConnectionInput = None,
        *,
        fleet_id: str,
        vpc_peering_connection_id: str,
    ) -> shapes.DeleteVpcPeeringConnectionOutput:
        """
        Removes a VPC peering connection. To delete the connection, you must have a
        valid authorization for the VPC peering connection that you want to delete. You
        can check for an authorization by calling DescribeVpcPeeringAuthorizations or
        request a new one using CreateVpcPeeringAuthorization.

        Once a valid authorization exists, call this operation from the AWS account that
        is used to manage the Amazon GameLift fleets. Identify the connection to delete
        by the connection ID and fleet ID. If successful, the connection is removed.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if vpc_peering_connection_id is not ShapeBase.NOT_SET:
                _params['vpc_peering_connection_id'] = vpc_peering_connection_id
            _request = shapes.DeleteVpcPeeringConnectionInput(**_params)
        response = self._boto_client.delete_vpc_peering_connection(
            **_request.to_boto()
        )

        return shapes.DeleteVpcPeeringConnectionOutput.from_boto(response)

    def describe_alias(
        self,
        _request: shapes.DescribeAliasInput = None,
        *,
        alias_id: str,
    ) -> shapes.DescribeAliasOutput:
        """
        Retrieves properties for an alias. This operation returns all alias metadata and
        settings. To get an alias's target fleet ID only, use `ResolveAlias`.

        To get alias properties, specify the alias ID. If successful, the requested
        alias record is returned.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            _request = shapes.DescribeAliasInput(**_params)
        response = self._boto_client.describe_alias(**_request.to_boto())

        return shapes.DescribeAliasOutput.from_boto(response)

    def describe_build(
        self,
        _request: shapes.DescribeBuildInput = None,
        *,
        build_id: str,
    ) -> shapes.DescribeBuildOutput:
        """
        Retrieves properties for a build. To request a build record, specify a build ID.
        If successful, an object containing the build properties is returned.

        Build-related operations include:

          * CreateBuild

          * ListBuilds

          * DescribeBuild

          * UpdateBuild

          * DeleteBuild
        """
        if _request is None:
            _params = {}
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            _request = shapes.DescribeBuildInput(**_params)
        response = self._boto_client.describe_build(**_request.to_boto())

        return shapes.DescribeBuildOutput.from_boto(response)

    def describe_ec2_instance_limits(
        self,
        _request: shapes.DescribeEC2InstanceLimitsInput = None,
        *,
        ec2_instance_type: typing.Union[str, shapes.
                                        EC2InstanceType] = ShapeBase.NOT_SET,
    ) -> shapes.DescribeEC2InstanceLimitsOutput:
        """
        Retrieves the following information for the specified EC2 instance type:

          * maximum number of instances allowed per AWS account (service limit)

          * current usage level for the AWS account

        Service limits vary depending on region. Available regions for Amazon GameLift
        can be found in the AWS Management Console for Amazon GameLift (see the drop-
        down list in the upper right corner).

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if ec2_instance_type is not ShapeBase.NOT_SET:
                _params['ec2_instance_type'] = ec2_instance_type
            _request = shapes.DescribeEC2InstanceLimitsInput(**_params)
        response = self._boto_client.describe_ec2_instance_limits(
            **_request.to_boto()
        )

        return shapes.DescribeEC2InstanceLimitsOutput.from_boto(response)

    def describe_fleet_attributes(
        self,
        _request: shapes.DescribeFleetAttributesInput = None,
        *,
        fleet_ids: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetAttributesOutput:
        """
        Retrieves fleet properties, including metadata, status, and configuration, for
        one or more fleets. You can request attributes for all fleets, or specify a list
        of one or more fleet IDs. When requesting multiple fleets, use the pagination
        parameters to retrieve results as a set of sequential pages. If successful, a
        FleetAttributes object is returned for each requested fleet ID. When specifying
        a list of fleet IDs, attribute objects are returned only for fleets that
        currently exist.

        Some API actions may limit the number of fleet IDs allowed in one request. If a
        request exceeds this limit, the request fails and the error message includes the
        maximum allowed.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_ids is not ShapeBase.NOT_SET:
                _params['fleet_ids'] = fleet_ids
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetAttributesInput(**_params)
        response = self._boto_client.describe_fleet_attributes(
            **_request.to_boto()
        )

        return shapes.DescribeFleetAttributesOutput.from_boto(response)

    def describe_fleet_capacity(
        self,
        _request: shapes.DescribeFleetCapacityInput = None,
        *,
        fleet_ids: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetCapacityOutput:
        """
        Retrieves the current status of fleet capacity for one or more fleets. This
        information includes the number of instances that have been requested for the
        fleet and the number currently active. You can request capacity for all fleets,
        or specify a list of one or more fleet IDs. When requesting multiple fleets, use
        the pagination parameters to retrieve results as a set of sequential pages. If
        successful, a FleetCapacity object is returned for each requested fleet ID. When
        specifying a list of fleet IDs, attribute objects are returned only for fleets
        that currently exist.

        Some API actions may limit the number of fleet IDs allowed in one request. If a
        request exceeds this limit, the request fails and the error message includes the
        maximum allowed.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_ids is not ShapeBase.NOT_SET:
                _params['fleet_ids'] = fleet_ids
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetCapacityInput(**_params)
        response = self._boto_client.describe_fleet_capacity(
            **_request.to_boto()
        )

        return shapes.DescribeFleetCapacityOutput.from_boto(response)

    def describe_fleet_events(
        self,
        _request: shapes.DescribeFleetEventsInput = None,
        *,
        fleet_id: str,
        start_time: datetime.datetime = ShapeBase.NOT_SET,
        end_time: datetime.datetime = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetEventsOutput:
        """
        Retrieves entries from the specified fleet's event log. You can specify a time
        range to limit the result set. Use the pagination parameters to retrieve results
        as a set of sequential pages. If successful, a collection of event log entries
        matching the request are returned.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if start_time is not ShapeBase.NOT_SET:
                _params['start_time'] = start_time
            if end_time is not ShapeBase.NOT_SET:
                _params['end_time'] = end_time
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetEventsInput(**_params)
        response = self._boto_client.describe_fleet_events(**_request.to_boto())

        return shapes.DescribeFleetEventsOutput.from_boto(response)

    def describe_fleet_port_settings(
        self,
        _request: shapes.DescribeFleetPortSettingsInput = None,
        *,
        fleet_id: str,
    ) -> shapes.DescribeFleetPortSettingsOutput:
        """
        Retrieves the inbound connection permissions for a fleet. Connection permissions
        include a range of IP addresses and port settings that incoming traffic can use
        to access server processes in the fleet. To get a fleet's inbound connection
        permissions, specify a fleet ID. If successful, a collection of IpPermission
        objects is returned for the requested fleet ID. If the requested fleet has been
        deleted, the result set is empty.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            _request = shapes.DescribeFleetPortSettingsInput(**_params)
        response = self._boto_client.describe_fleet_port_settings(
            **_request.to_boto()
        )

        return shapes.DescribeFleetPortSettingsOutput.from_boto(response)

    def describe_fleet_utilization(
        self,
        _request: shapes.DescribeFleetUtilizationInput = None,
        *,
        fleet_ids: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeFleetUtilizationOutput:
        """
        Retrieves utilization statistics for one or more fleets. You can request
        utilization data for all fleets, or specify a list of one or more fleet IDs.
        When requesting multiple fleets, use the pagination parameters to retrieve
        results as a set of sequential pages. If successful, a FleetUtilization object
        is returned for each requested fleet ID. When specifying a list of fleet IDs,
        utilization objects are returned only for fleets that currently exist.

        Some API actions may limit the number of fleet IDs allowed in one request. If a
        request exceeds this limit, the request fails and the error message includes the
        maximum allowed.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_ids is not ShapeBase.NOT_SET:
                _params['fleet_ids'] = fleet_ids
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeFleetUtilizationInput(**_params)
        response = self._boto_client.describe_fleet_utilization(
            **_request.to_boto()
        )

        return shapes.DescribeFleetUtilizationOutput.from_boto(response)

    def describe_game_session_details(
        self,
        _request: shapes.DescribeGameSessionDetailsInput = None,
        *,
        fleet_id: str = ShapeBase.NOT_SET,
        game_session_id: str = ShapeBase.NOT_SET,
        alias_id: str = ShapeBase.NOT_SET,
        status_filter: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeGameSessionDetailsOutput:
        """
        Retrieves properties, including the protection policy in force, for one or more
        game sessions. This action can be used in several ways: (1) provide a
        `GameSessionId` or `GameSessionArn` to request details for a specific game
        session; (2) provide either a `FleetId` or an `AliasId` to request properties
        for all game sessions running on a fleet.

        To get game session record(s), specify just one of the following: game session
        ID, fleet ID, or alias ID. You can filter this request by game session status.
        Use the pagination parameters to retrieve results as a set of sequential pages.
        If successful, a GameSessionDetail object is returned for each session matching
        the request.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            if status_filter is not ShapeBase.NOT_SET:
                _params['status_filter'] = status_filter
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeGameSessionDetailsInput(**_params)
        response = self._boto_client.describe_game_session_details(
            **_request.to_boto()
        )

        return shapes.DescribeGameSessionDetailsOutput.from_boto(response)

    def describe_game_session_placement(
        self,
        _request: shapes.DescribeGameSessionPlacementInput = None,
        *,
        placement_id: str,
    ) -> shapes.DescribeGameSessionPlacementOutput:
        """
        Retrieves properties and current status of a game session placement request. To
        get game session placement details, specify the placement ID. If successful, a
        GameSessionPlacement object is returned.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if placement_id is not ShapeBase.NOT_SET:
                _params['placement_id'] = placement_id
            _request = shapes.DescribeGameSessionPlacementInput(**_params)
        response = self._boto_client.describe_game_session_placement(
            **_request.to_boto()
        )

        return shapes.DescribeGameSessionPlacementOutput.from_boto(response)

    def describe_game_session_queues(
        self,
        _request: shapes.DescribeGameSessionQueuesInput = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeGameSessionQueuesOutput:
        """
        Retrieves the properties for one or more game session queues. When requesting
        multiple queues, use the pagination parameters to retrieve results as a set of
        sequential pages. If successful, a GameSessionQueue object is returned for each
        requested queue. When specifying a list of queues, objects are returned only for
        queues that currently exist in the region.

        Queue-related operations include:

          * CreateGameSessionQueue

          * DescribeGameSessionQueues

          * UpdateGameSessionQueue

          * DeleteGameSessionQueue
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeGameSessionQueuesInput(**_params)
        response = self._boto_client.describe_game_session_queues(
            **_request.to_boto()
        )

        return shapes.DescribeGameSessionQueuesOutput.from_boto(response)

    def describe_game_sessions(
        self,
        _request: shapes.DescribeGameSessionsInput = None,
        *,
        fleet_id: str = ShapeBase.NOT_SET,
        game_session_id: str = ShapeBase.NOT_SET,
        alias_id: str = ShapeBase.NOT_SET,
        status_filter: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeGameSessionsOutput:
        """
        Retrieves a set of one or more game sessions. Request a specific game session or
        request all game sessions on a fleet. Alternatively, use SearchGameSessions to
        request a set of active game sessions that are filtered by certain criteria. To
        retrieve protection policy settings for game sessions, use
        DescribeGameSessionDetails.

        To get game sessions, specify one of the following: game session ID, fleet ID,
        or alias ID. You can filter this request by game session status. Use the
        pagination parameters to retrieve results as a set of sequential pages. If
        successful, a GameSession object is returned for each game session matching the
        request.

        _Available in Amazon GameLift Local._

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            if status_filter is not ShapeBase.NOT_SET:
                _params['status_filter'] = status_filter
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeGameSessionsInput(**_params)
        response = self._boto_client.describe_game_sessions(
            **_request.to_boto()
        )

        return shapes.DescribeGameSessionsOutput.from_boto(response)

    def describe_instances(
        self,
        _request: shapes.DescribeInstancesInput = None,
        *,
        fleet_id: str,
        instance_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeInstancesOutput:
        """
        Retrieves information about a fleet's instances, including instance IDs. Use
        this action to get details on all instances in the fleet or get details on one
        specific instance.

        To get a specific instance, specify fleet ID and instance ID. To get all
        instances in a fleet, specify a fleet ID only. Use the pagination parameters to
        retrieve results as a set of sequential pages. If successful, an Instance object
        is returned for each result.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeInstancesInput(**_params)
        response = self._boto_client.describe_instances(**_request.to_boto())

        return shapes.DescribeInstancesOutput.from_boto(response)

    def describe_matchmaking(
        self,
        _request: shapes.DescribeMatchmakingInput = None,
        *,
        ticket_ids: typing.List[str],
    ) -> shapes.DescribeMatchmakingOutput:
        """
        Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket
        information, including status and--once a successful match is made--acquire
        connection information for the resulting new game session.

        You can use this operation to track the progress of matchmaking requests
        (through polling) as an alternative to using event notifications. See more
        details on tracking matchmaking requests through polling or notifications in
        StartMatchmaking.

        To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the
        request is successful, a ticket object is returned for each requested ID that
        currently exists.

        Matchmaking-related operations include:

          * StartMatchmaking

          * DescribeMatchmaking

          * StopMatchmaking

          * AcceptMatch

          * StartMatchBackfill
        """
        if _request is None:
            _params = {}
            if ticket_ids is not ShapeBase.NOT_SET:
                _params['ticket_ids'] = ticket_ids
            _request = shapes.DescribeMatchmakingInput(**_params)
        response = self._boto_client.describe_matchmaking(**_request.to_boto())

        return shapes.DescribeMatchmakingOutput.from_boto(response)

    def describe_matchmaking_configurations(
        self,
        _request: shapes.DescribeMatchmakingConfigurationsInput = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        rule_set_name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMatchmakingConfigurationsOutput:
        """
        Retrieves the details of FlexMatch matchmaking configurations. with this
        operation, you have the following options: (1) retrieve all existing
        configurations, (2) provide the names of one or more configurations to retrieve,
        or (3) retrieve all configurations that use a specified rule set name. When
        requesting multiple items, use the pagination parameters to retrieve results as
        a set of sequential pages. If successful, a configuration is returned for each
        requested name. When specifying a list of names, only configurations that
        currently exist are returned.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMatchmakingConfigurationsInput(**_params)
        response = self._boto_client.describe_matchmaking_configurations(
            **_request.to_boto()
        )

        return shapes.DescribeMatchmakingConfigurationsOutput.from_boto(
            response
        )

    def describe_matchmaking_rule_sets(
        self,
        _request: shapes.DescribeMatchmakingRuleSetsInput = None,
        *,
        names: typing.List[str] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeMatchmakingRuleSetsOutput:
        """
        Retrieves the details for FlexMatch matchmaking rule sets. You can request all
        existing rule sets for the region, or provide a list of one or more rule set
        names. When requesting multiple items, use the pagination parameters to retrieve
        results as a set of sequential pages. If successful, a rule set is returned for
        each requested name.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if names is not ShapeBase.NOT_SET:
                _params['names'] = names
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeMatchmakingRuleSetsInput(**_params)
        response = self._boto_client.describe_matchmaking_rule_sets(
            **_request.to_boto()
        )

        return shapes.DescribeMatchmakingRuleSetsOutput.from_boto(response)

    def describe_player_sessions(
        self,
        _request: shapes.DescribePlayerSessionsInput = None,
        *,
        game_session_id: str = ShapeBase.NOT_SET,
        player_id: str = ShapeBase.NOT_SET,
        player_session_id: str = ShapeBase.NOT_SET,
        player_session_status_filter: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribePlayerSessionsOutput:
        """
        Retrieves properties for one or more player sessions. This action can be used in
        several ways: (1) provide a `PlayerSessionId` to request properties for a
        specific player session; (2) provide a `GameSessionId` to request properties for
        all player sessions in the specified game session; (3) provide a `PlayerId` to
        request properties for all player sessions of a specified player.

        To get game session record(s), specify only one of the following: a player
        session ID, a game session ID, or a player ID. You can filter this request by
        player session status. Use the pagination parameters to retrieve results as a
        set of sequential pages. If successful, a PlayerSession object is returned for
        each session matching the request.

        _Available in Amazon GameLift Local._

        Player-session-related operations include:

          * CreatePlayerSession

          * CreatePlayerSessions

          * DescribePlayerSessions

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if player_id is not ShapeBase.NOT_SET:
                _params['player_id'] = player_id
            if player_session_id is not ShapeBase.NOT_SET:
                _params['player_session_id'] = player_session_id
            if player_session_status_filter is not ShapeBase.NOT_SET:
                _params['player_session_status_filter'
                       ] = player_session_status_filter
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribePlayerSessionsInput(**_params)
        response = self._boto_client.describe_player_sessions(
            **_request.to_boto()
        )

        return shapes.DescribePlayerSessionsOutput.from_boto(response)

    def describe_runtime_configuration(
        self,
        _request: shapes.DescribeRuntimeConfigurationInput = None,
        *,
        fleet_id: str,
    ) -> shapes.DescribeRuntimeConfigurationOutput:
        """
        Retrieves the current run-time configuration for the specified fleet. The run-
        time configuration tells Amazon GameLift how to launch server processes on
        instances in the fleet.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            _request = shapes.DescribeRuntimeConfigurationInput(**_params)
        response = self._boto_client.describe_runtime_configuration(
            **_request.to_boto()
        )

        return shapes.DescribeRuntimeConfigurationOutput.from_boto(response)

    def describe_scaling_policies(
        self,
        _request: shapes.DescribeScalingPoliciesInput = None,
        *,
        fleet_id: str,
        status_filter: typing.Union[str, shapes.ScalingStatusType] = ShapeBase.
        NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeScalingPoliciesOutput:
        """
        Retrieves all scaling policies applied to a fleet.

        To get a fleet's scaling policies, specify the fleet ID. You can filter this
        request by policy status, such as to retrieve only active scaling policies. Use
        the pagination parameters to retrieve results as a set of sequential pages. If
        successful, set of ScalingPolicy objects is returned for the fleet.

        A fleet may have all of its scaling policies suspended (StopFleetActions). This
        action does not affect the status of the scaling policies, which remains ACTIVE.
        To see whether a fleet's scaling policies are in force or suspended, call
        DescribeFleetAttributes and check the stopped actions.

        Operations related to fleet capacity scaling include:

          * DescribeFleetCapacity

          * UpdateFleetCapacity

          * DescribeEC2InstanceLimits

          * Manage scaling policies:

            * PutScalingPolicy (auto-scaling)

            * DescribeScalingPolicies (auto-scaling)

            * DeleteScalingPolicy (auto-scaling)

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if status_filter is not ShapeBase.NOT_SET:
                _params['status_filter'] = status_filter
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeScalingPoliciesInput(**_params)
        response = self._boto_client.describe_scaling_policies(
            **_request.to_boto()
        )

        return shapes.DescribeScalingPoliciesOutput.from_boto(response)

    def describe_vpc_peering_authorizations(
        self,
        _request: shapes.DescribeVpcPeeringAuthorizationsInput = None,
    ) -> shapes.DescribeVpcPeeringAuthorizationsOutput:
        """
        Retrieves valid VPC peering authorizations that are pending for the AWS account.
        This operation returns all VPC peering authorizations and requests for peering.
        This includes those initiated and received by this account.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            _request = shapes.DescribeVpcPeeringAuthorizationsInput(**_params)
        response = self._boto_client.describe_vpc_peering_authorizations(
            **_request.to_boto()
        )

        return shapes.DescribeVpcPeeringAuthorizationsOutput.from_boto(response)

    def describe_vpc_peering_connections(
        self,
        _request: shapes.DescribeVpcPeeringConnectionsInput = None,
        *,
        fleet_id: str = ShapeBase.NOT_SET,
    ) -> shapes.DescribeVpcPeeringConnectionsOutput:
        """
        Retrieves information on VPC peering connections. Use this operation to get
        peering information for all fleets or for one specific fleet ID.

        To retrieve connection information, call this operation from the AWS account
        that is used to manage the Amazon GameLift fleets. Specify a fleet ID or leave
        the parameter empty to retrieve all connection records. If successful, the
        retrieved information includes both active and pending connections. Active
        connections identify the IpV4 CIDR block that the VPC uses to connect.

        VPC peering connection operations include:

          * CreateVpcPeeringAuthorization

          * DescribeVpcPeeringAuthorizations

          * DeleteVpcPeeringAuthorization

          * CreateVpcPeeringConnection

          * DescribeVpcPeeringConnections

          * DeleteVpcPeeringConnection
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            _request = shapes.DescribeVpcPeeringConnectionsInput(**_params)
        response = self._boto_client.describe_vpc_peering_connections(
            **_request.to_boto()
        )

        return shapes.DescribeVpcPeeringConnectionsOutput.from_boto(response)

    def get_game_session_log_url(
        self,
        _request: shapes.GetGameSessionLogUrlInput = None,
        *,
        game_session_id: str,
    ) -> shapes.GetGameSessionLogUrlOutput:
        """
        Retrieves the location of stored game session logs for a specified game session.
        When a game session is terminated, Amazon GameLift automatically stores the logs
        in Amazon S3 and retains them for 14 days. Use this URL to download the logs.

        See the [AWS Service
        Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_gamelift)
        page for maximum log file sizes. Log files that exceed this limit are not saved.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            _request = shapes.GetGameSessionLogUrlInput(**_params)
        response = self._boto_client.get_game_session_log_url(
            **_request.to_boto()
        )

        return shapes.GetGameSessionLogUrlOutput.from_boto(response)

    def get_instance_access(
        self,
        _request: shapes.GetInstanceAccessInput = None,
        *,
        fleet_id: str,
        instance_id: str,
    ) -> shapes.GetInstanceAccessOutput:
        """
        Requests remote access to a fleet instance. Remote access is useful for
        debugging, gathering benchmarking data, or watching activity in real time.

        Access requires credentials that match the operating system of the instance. For
        a Windows instance, Amazon GameLift returns a user name and password as strings
        for use with a Windows Remote Desktop client. For a Linux instance, Amazon
        GameLift returns a user name and RSA private key, also as strings, for use with
        an SSH client. The private key must be saved in the proper format to a `.pem`
        file before using. If you're making this request using the AWS CLI, saving the
        secret can be handled as part of the GetInstanceAccess request. (See the example
        later in this topic). For more information on remote access, see [Remotely
        Accessing an
        Instance](http://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-
        remote-access.html).

        To request access to a specific instance, specify the IDs of the instance and
        the fleet it belongs to. If successful, an InstanceAccess object is returned
        containing the instance's IP address and a set of credentials.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if instance_id is not ShapeBase.NOT_SET:
                _params['instance_id'] = instance_id
            _request = shapes.GetInstanceAccessInput(**_params)
        response = self._boto_client.get_instance_access(**_request.to_boto())

        return shapes.GetInstanceAccessOutput.from_boto(response)

    def list_aliases(
        self,
        _request: shapes.ListAliasesInput = None,
        *,
        routing_strategy_type: typing.
        Union[str, shapes.RoutingStrategyType] = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListAliasesOutput:
        """
        Retrieves all aliases for this AWS account. You can filter the result set by
        alias name and/or routing strategy type. Use the pagination parameters to
        retrieve results in sequential pages.

        Returned aliases are not listed in any particular order.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if routing_strategy_type is not ShapeBase.NOT_SET:
                _params['routing_strategy_type'] = routing_strategy_type
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListAliasesInput(**_params)
        response = self._boto_client.list_aliases(**_request.to_boto())

        return shapes.ListAliasesOutput.from_boto(response)

    def list_builds(
        self,
        _request: shapes.ListBuildsInput = None,
        *,
        status: typing.Union[str, shapes.BuildStatus] = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListBuildsOutput:
        """
        Retrieves build records for all builds associated with the AWS account in use.
        You can limit results to builds that are in a specific status by using the
        `Status` parameter. Use the pagination parameters to retrieve results in a set
        of sequential pages.

        Build records are not listed in any particular order.

        Build-related operations include:

          * CreateBuild

          * ListBuilds

          * DescribeBuild

          * UpdateBuild

          * DeleteBuild
        """
        if _request is None:
            _params = {}
            if status is not ShapeBase.NOT_SET:
                _params['status'] = status
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListBuildsInput(**_params)
        response = self._boto_client.list_builds(**_request.to_boto())

        return shapes.ListBuildsOutput.from_boto(response)

    def list_fleets(
        self,
        _request: shapes.ListFleetsInput = None,
        *,
        build_id: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.ListFleetsOutput:
        """
        Retrieves a collection of fleet records for this AWS account. You can filter the
        result set by build ID. Use the pagination parameters to retrieve results in
        sequential pages.

        Fleet records are not listed in any particular order.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.ListFleetsInput(**_params)
        response = self._boto_client.list_fleets(**_request.to_boto())

        return shapes.ListFleetsOutput.from_boto(response)

    def put_scaling_policy(
        self,
        _request: shapes.PutScalingPolicyInput = None,
        *,
        name: str,
        fleet_id: str,
        metric_name: typing.Union[str, shapes.MetricName],
        scaling_adjustment: int = ShapeBase.NOT_SET,
        scaling_adjustment_type: typing.
        Union[str, shapes.ScalingAdjustmentType] = ShapeBase.NOT_SET,
        threshold: float = ShapeBase.NOT_SET,
        comparison_operator: typing.
        Union[str, shapes.ComparisonOperatorType] = ShapeBase.NOT_SET,
        evaluation_periods: int = ShapeBase.NOT_SET,
        policy_type: typing.Union[str, shapes.PolicyType] = ShapeBase.NOT_SET,
        target_configuration: shapes.TargetConfiguration = ShapeBase.NOT_SET,
    ) -> shapes.PutScalingPolicyOutput:
        """
        Creates or updates a scaling policy for a fleet. Scaling policies are used to
        automatically scale a fleet's hosting capacity to meet player demand. An active
        scaling policy instructs Amazon GameLift to track a fleet metric and
        automatically change the fleet's capacity when a certain threshold is reached.
        There are two types of scaling policies: target-based and rule-based. Use a
        target-based policy to quickly and efficiently manage fleet scaling; this option
        is the most commonly used. Use rule-based policies when you need to exert fine-
        grained control over auto-scaling.

        Fleets can have multiple scaling policies of each type in force at the same
        time; you can have one target-based policy, one or multiple rule-based scaling
        policies, or both. We recommend caution, however, because multiple auto-scaling
        policies can have unintended consequences.

        You can temporarily suspend all scaling policies for a fleet by calling
        StopFleetActions with the fleet action AUTO_SCALING. To resume scaling policies,
        call StartFleetActions with the same fleet action. To stop just one scaling
        policy--or to permanently remove it, you must delete the policy with
        DeleteScalingPolicy.

        Learn more about how to work with auto-scaling in [Set Up Fleet Automatic
        Scaling](http://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-
        autoscaling.html).

        **Target-based policy**

        A target-based policy tracks a single metric: PercentAvailableGameSessions. This
        metric tells us how much of a fleet's hosting capacity is ready to host game
        sessions but is not currently in use. This is the fleet's buffer; it measures
        the additional player demand that the fleet could handle at current capacity.
        With a target-based policy, you set your ideal buffer size and leave it to
        Amazon GameLift to take whatever action is needed to maintain that target.

        For example, you might choose to maintain a 10% buffer for a fleet that has the
        capacity to host 100 simultaneous game sessions. This policy tells Amazon
        GameLift to take action whenever the fleet's available capacity falls below or
        rises above 10 game sessions. Amazon GameLift will start new instances or stop
        unused instances in order to return to the 10% buffer.

        To create or update a target-based policy, specify a fleet ID and name, and set
        the policy type to "TargetBased". Specify the metric to track
        (PercentAvailableGameSessions) and reference a TargetConfiguration object with
        your desired buffer value. Exclude all other parameters. On a successful
        request, the policy name is returned. The scaling policy is automatically in
        force as soon as it's successfully created. If the fleet's auto-scaling actions
        are temporarily suspended, the new policy will be in force once the fleet
        actions are restarted.

        **Rule-based policy**

        A rule-based policy tracks specified fleet metric, sets a threshold value, and
        specifies the type of action to initiate when triggered. With a rule-based
        policy, you can select from several available fleet metrics. Each policy
        specifies whether to scale up or scale down (and by how much), so you need one
        policy for each type of action.

        For example, a policy may make the following statement: "If the percentage of
        idle instances is greater than 20% for more than 15 minutes, then reduce the
        fleet capacity by 10%."

        A policy's rule statement has the following structure:

        If `[MetricName]` is `[ComparisonOperator]` `[Threshold]` for
        `[EvaluationPeriods]` minutes, then `[ScalingAdjustmentType]` to/by
        `[ScalingAdjustment]`.

        To implement the example, the rule statement would look like this:

        If `[PercentIdleInstances]` is `[GreaterThanThreshold]` `[20]` for `[15]`
        minutes, then `[PercentChangeInCapacity]` to/by `[10]`.

        To create or update a scaling policy, specify a unique combination of name and
        fleet ID, and set the policy type to "RuleBased". Specify the parameter values
        for a policy rule statement. On a successful request, the policy name is
        returned. Scaling policies are automatically in force as soon as they're
        successfully created. If the fleet's auto-scaling actions are temporarily
        suspended, the new policy will be in force once the fleet actions are restarted.

        Operations related to fleet capacity scaling include:

          * DescribeFleetCapacity

          * UpdateFleetCapacity

          * DescribeEC2InstanceLimits

          * Manage scaling policies:

            * PutScalingPolicy (auto-scaling)

            * DescribeScalingPolicies (auto-scaling)

            * DeleteScalingPolicy (auto-scaling)

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if metric_name is not ShapeBase.NOT_SET:
                _params['metric_name'] = metric_name
            if scaling_adjustment is not ShapeBase.NOT_SET:
                _params['scaling_adjustment'] = scaling_adjustment
            if scaling_adjustment_type is not ShapeBase.NOT_SET:
                _params['scaling_adjustment_type'] = scaling_adjustment_type
            if threshold is not ShapeBase.NOT_SET:
                _params['threshold'] = threshold
            if comparison_operator is not ShapeBase.NOT_SET:
                _params['comparison_operator'] = comparison_operator
            if evaluation_periods is not ShapeBase.NOT_SET:
                _params['evaluation_periods'] = evaluation_periods
            if policy_type is not ShapeBase.NOT_SET:
                _params['policy_type'] = policy_type
            if target_configuration is not ShapeBase.NOT_SET:
                _params['target_configuration'] = target_configuration
            _request = shapes.PutScalingPolicyInput(**_params)
        response = self._boto_client.put_scaling_policy(**_request.to_boto())

        return shapes.PutScalingPolicyOutput.from_boto(response)

    def request_upload_credentials(
        self,
        _request: shapes.RequestUploadCredentialsInput = None,
        *,
        build_id: str,
    ) -> shapes.RequestUploadCredentialsOutput:
        """
        Retrieves a fresh set of credentials for use when uploading a new set of game
        build files to Amazon GameLift's Amazon S3. This is done as part of the build
        creation process; see CreateBuild.

        To request new credentials, specify the build ID as returned with an initial
        `CreateBuild` request. If successful, a new set of credentials are returned,
        along with the S3 storage location associated with the build ID.
        """
        if _request is None:
            _params = {}
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            _request = shapes.RequestUploadCredentialsInput(**_params)
        response = self._boto_client.request_upload_credentials(
            **_request.to_boto()
        )

        return shapes.RequestUploadCredentialsOutput.from_boto(response)

    def resolve_alias(
        self,
        _request: shapes.ResolveAliasInput = None,
        *,
        alias_id: str,
    ) -> shapes.ResolveAliasOutput:
        """
        Retrieves the fleet ID that a specified alias is currently pointing to.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            _request = shapes.ResolveAliasInput(**_params)
        response = self._boto_client.resolve_alias(**_request.to_boto())

        return shapes.ResolveAliasOutput.from_boto(response)

    def search_game_sessions(
        self,
        _request: shapes.SearchGameSessionsInput = None,
        *,
        fleet_id: str = ShapeBase.NOT_SET,
        alias_id: str = ShapeBase.NOT_SET,
        filter_expression: str = ShapeBase.NOT_SET,
        sort_expression: str = ShapeBase.NOT_SET,
        limit: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.SearchGameSessionsOutput:
        """
        Retrieves all active game sessions that match a set of search criteria and sorts
        them in a specified order. You can search or sort by the following game session
        attributes:

          * **gameSessionId** \-- Unique identifier for the game session. You can use either a `GameSessionId` or `GameSessionArn` value. 

          * **gameSessionName** \-- Name assigned to a game session. This value is set when requesting a new game session with CreateGameSession or updating with UpdateGameSession. Game session names do not need to be unique to a game session.

          * **gameSessionProperties** \-- Custom data defined in a game session's `GameProperty` parameter. `GameProperty` values are stored as key:value pairs; the filter expression must indicate the key and a string to search the data values for. For example, to search for game sessions with custom data containing the key:value pair "gameMode:brawl", specify the following: `gameSessionProperties.gameMode = "brawl"`. All custom data values are searched as strings.

          * **maximumSessions** \-- Maximum number of player sessions allowed for a game session. This value is set when requesting a new game session with CreateGameSession or updating with UpdateGameSession.

          * **creationTimeMillis** \-- Value indicating when a game session was created. It is expressed in Unix time as milliseconds.

          * **playerSessionCount** \-- Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out.

          * **hasAvailablePlayerSessions** \-- Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join. 

        Returned values for `playerSessionCount` and `hasAvailablePlayerSessions` change
        quickly as players join sessions and others drop out. Results should be
        considered a snapshot in time. Be sure to refresh search results often, and
        handle sessions that fill up before a player can join.

        To search or sort, specify either a fleet ID or an alias ID, and provide a
        search filter expression, a sort expression, or both. If successful, a
        collection of GameSession objects matching the request is returned. Use the
        pagination parameters to retrieve results as a set of sequential pages.

        You can search for game sessions one fleet at a time only. To find game sessions
        across multiple fleets, you must search each fleet separately and combine the
        results. This search feature finds only game sessions that are in `ACTIVE`
        status. To locate games in statuses other than active, use
        DescribeGameSessionDetails.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            if filter_expression is not ShapeBase.NOT_SET:
                _params['filter_expression'] = filter_expression
            if sort_expression is not ShapeBase.NOT_SET:
                _params['sort_expression'] = sort_expression
            if limit is not ShapeBase.NOT_SET:
                _params['limit'] = limit
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.SearchGameSessionsInput(**_params)
        response = self._boto_client.search_game_sessions(**_request.to_boto())

        return shapes.SearchGameSessionsOutput.from_boto(response)

    def start_fleet_actions(
        self,
        _request: shapes.StartFleetActionsInput = None,
        *,
        fleet_id: str,
        actions: typing.List[typing.Union[str, shapes.FleetAction]],
    ) -> shapes.StartFleetActionsOutput:
        """
        Resumes activity on a fleet that was suspended with StopFleetActions. Currently,
        this operation is used to restart a fleet's auto-scaling activity.

        To start fleet actions, specify the fleet ID and the type of actions to restart.
        When auto-scaling fleet actions are restarted, Amazon GameLift once again
        initiates scaling events as triggered by the fleet's scaling policies. If
        actions on the fleet were never stopped, this operation will have no effect. You
        can view a fleet's stopped actions using DescribeFleetAttributes.

        Operations related to fleet capacity scaling include:

          * DescribeFleetCapacity

          * UpdateFleetCapacity

          * DescribeEC2InstanceLimits

          * Manage scaling policies:

            * PutScalingPolicy (auto-scaling)

            * DescribeScalingPolicies (auto-scaling)

            * DeleteScalingPolicy (auto-scaling)

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            _request = shapes.StartFleetActionsInput(**_params)
        response = self._boto_client.start_fleet_actions(**_request.to_boto())

        return shapes.StartFleetActionsOutput.from_boto(response)

    def start_game_session_placement(
        self,
        _request: shapes.StartGameSessionPlacementInput = None,
        *,
        placement_id: str,
        game_session_queue_name: str,
        maximum_player_session_count: int,
        game_properties: typing.List[shapes.GameProperty] = ShapeBase.NOT_SET,
        game_session_name: str = ShapeBase.NOT_SET,
        player_latencies: typing.List[shapes.PlayerLatency] = ShapeBase.NOT_SET,
        desired_player_sessions: typing.List[shapes.DesiredPlayerSession
                                            ] = ShapeBase.NOT_SET,
        game_session_data: str = ShapeBase.NOT_SET,
    ) -> shapes.StartGameSessionPlacementOutput:
        """
        Places a request for a new game session in a queue (see CreateGameSessionQueue).
        When processing a placement request, Amazon GameLift searches for available
        resources on the queue's destinations, scanning each until it finds resources or
        the placement request times out.

        A game session placement request can also request player sessions. When a new
        game session is successfully created, Amazon GameLift creates a player session
        for each player included in the request.

        When placing a game session, by default Amazon GameLift tries each fleet in the
        order they are listed in the queue configuration. Ideally, a queue's
        destinations are listed in preference order.

        Alternatively, when requesting a game session with players, you can also provide
        latency data for each player in relevant regions. Latency data indicates the
        performance lag a player experiences when connected to a fleet in the region.
        Amazon GameLift uses latency data to reorder the list of destinations to place
        the game session in a region with minimal lag. If latency data is provided for
        multiple players, Amazon GameLift calculates each region's average lag for all
        players and reorders to get the best game play across all players.

        To place a new game session request, specify the following:

          * The queue name and a set of game session properties and settings

          * A unique ID (such as a UUID) for the placement. You use this ID to track the status of the placement request

          * (Optional) A set of IDs and player data for each player you want to join to the new game session

          * Latency data for all players (if you want to optimize game play for the players)

        If successful, a new game session placement is created.

        To track the status of a placement request, call DescribeGameSessionPlacement
        and check the request's status. If the status is `FULFILLED`, a new game session
        has been created and a game session ARN and region are referenced. If the
        placement request times out, you can resubmit the request or retry it with a
        different queue.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if placement_id is not ShapeBase.NOT_SET:
                _params['placement_id'] = placement_id
            if game_session_queue_name is not ShapeBase.NOT_SET:
                _params['game_session_queue_name'] = game_session_queue_name
            if maximum_player_session_count is not ShapeBase.NOT_SET:
                _params['maximum_player_session_count'
                       ] = maximum_player_session_count
            if game_properties is not ShapeBase.NOT_SET:
                _params['game_properties'] = game_properties
            if game_session_name is not ShapeBase.NOT_SET:
                _params['game_session_name'] = game_session_name
            if player_latencies is not ShapeBase.NOT_SET:
                _params['player_latencies'] = player_latencies
            if desired_player_sessions is not ShapeBase.NOT_SET:
                _params['desired_player_sessions'] = desired_player_sessions
            if game_session_data is not ShapeBase.NOT_SET:
                _params['game_session_data'] = game_session_data
            _request = shapes.StartGameSessionPlacementInput(**_params)
        response = self._boto_client.start_game_session_placement(
            **_request.to_boto()
        )

        return shapes.StartGameSessionPlacementOutput.from_boto(response)

    def start_match_backfill(
        self,
        _request: shapes.StartMatchBackfillInput = None,
        *,
        configuration_name: str,
        game_session_arn: str,
        players: typing.List[shapes.Player],
        ticket_id: str = ShapeBase.NOT_SET,
    ) -> shapes.StartMatchBackfillOutput:
        """
        Finds new players to fill open slots in an existing game session. This operation
        can be used to add players to matched games that start with fewer than the
        maximum number of players or to replace players when they drop out. By
        backfilling with the same matchmaker used to create the original match, you
        ensure that new players meet the match criteria and maintain a consistent
        experience throughout the game session. You can backfill a match anytime after a
        game session has been created.

        To request a match backfill, specify a unique ticket ID, the existing game
        session's ARN, a matchmaking configuration, and a set of data that describes all
        current players in the game session. If successful, a match backfill ticket is
        created and returned with status set to QUEUED. The ticket is placed in the
        matchmaker's ticket pool and processed. Track the status of the ticket to
        respond as needed. For more detail how to set up backfilling, see [ Backfill
        Existing Games with
        FlexMatch](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
        backfill.html).

        The process of finding backfill matches is essentially identical to the initial
        matchmaking process. The matchmaker searches the pool and groups tickets
        together to form potential matches, allowing only one backfill ticket per
        potential match. Once the a match is formed, the matchmaker creates player
        sessions for the new players. All tickets in the match are updated with the game
        session's connection information, and the GameSession object is updated to
        include matchmaker data on the new players. For more detail on how match
        backfill requests are processed, see [ How Amazon GameLift FlexMatch
        Works](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
        intro.html).

        Matchmaking-related operations include:

          * StartMatchmaking

          * DescribeMatchmaking

          * StopMatchmaking

          * AcceptMatch

          * StartMatchBackfill
        """
        if _request is None:
            _params = {}
            if configuration_name is not ShapeBase.NOT_SET:
                _params['configuration_name'] = configuration_name
            if game_session_arn is not ShapeBase.NOT_SET:
                _params['game_session_arn'] = game_session_arn
            if players is not ShapeBase.NOT_SET:
                _params['players'] = players
            if ticket_id is not ShapeBase.NOT_SET:
                _params['ticket_id'] = ticket_id
            _request = shapes.StartMatchBackfillInput(**_params)
        response = self._boto_client.start_match_backfill(**_request.to_boto())

        return shapes.StartMatchBackfillOutput.from_boto(response)

    def start_matchmaking(
        self,
        _request: shapes.StartMatchmakingInput = None,
        *,
        configuration_name: str,
        players: typing.List[shapes.Player],
        ticket_id: str = ShapeBase.NOT_SET,
    ) -> shapes.StartMatchmakingOutput:
        """
        Uses FlexMatch to create a game match for a group of players based on custom
        matchmaking rules, and starts a new game for the matched players. Each
        matchmaking request specifies the type of match to build (team configuration,
        rules for an acceptable match, etc.). The request also specifies the players to
        find a match for and where to host the new game session for optimal performance.
        A matchmaking request might start with a single player or a group of players who
        want to play together. FlexMatch finds additional players as needed to fill the
        match. Match type, rules, and the queue used to place a new game session are
        defined in a `MatchmakingConfiguration`. For complete information on setting up
        and using FlexMatch, see the topic [ Adding FlexMatch to Your
        Game](http://docs.aws.amazon.com/gamelift/latest/developerguide/match-
        intro.html).

        To start matchmaking, provide a unique ticket ID, specify a matchmaking
        configuration, and include the players to be matched. You must also include a
        set of player attributes relevant for the matchmaking configuration. If
        successful, a matchmaking ticket is returned with status set to `QUEUED`. Track
        the status of the ticket to respond as needed and acquire game session
        connection information for successfully completed matches.

        **Tracking ticket status** \-- A couple of options are available for tracking
        the status of matchmaking requests:

          * Polling -- Call `DescribeMatchmaking`. This operation returns the full ticket object, including current status and (for completed tickets) game session connection info. We recommend polling no more than once every 10 seconds.

          * Notifications -- Get event notifications for changes in ticket status using Amazon Simple Notification Service (SNS). Notifications are easy to set up (see CreateMatchmakingConfiguration) and typically deliver match status changes faster and more efficiently than polling. We recommend that you use polling to back up to notifications (since delivery is not guaranteed) and call `DescribeMatchmaking` only when notifications are not received within 30 seconds.

        **Processing a matchmaking request** \-- FlexMatch handles a matchmaking request
        as follows:

          1. Your client code submits a `StartMatchmaking` request for one or more players and tracks the status of the request ticket. 

          2. FlexMatch uses this ticket and others in process to build an acceptable match. When a potential match is identified, all tickets in the proposed match are advanced to the next status. 

          3. If the match requires player acceptance (set in the matchmaking configuration), the tickets move into status `REQUIRES_ACCEPTANCE`. This status triggers your client code to solicit acceptance from all players in every ticket involved in the match, and then call AcceptMatch for each player. If any player rejects or fails to accept the match before a specified timeout, the proposed match is dropped (see `AcceptMatch` for more details).

          4. Once a match is proposed and accepted, the matchmaking tickets move into status `PLACING`. FlexMatch locates resources for a new game session using the game session queue (set in the matchmaking configuration) and creates the game session based on the match data. 

          5. When the match is successfully placed, the matchmaking tickets move into `COMPLETED` status. Connection information (including game session endpoint and player session) is added to the matchmaking tickets. Matched players can use the connection information to join the game. 

        Matchmaking-related operations include:

          * StartMatchmaking

          * DescribeMatchmaking

          * StopMatchmaking

          * AcceptMatch

          * StartMatchBackfill
        """
        if _request is None:
            _params = {}
            if configuration_name is not ShapeBase.NOT_SET:
                _params['configuration_name'] = configuration_name
            if players is not ShapeBase.NOT_SET:
                _params['players'] = players
            if ticket_id is not ShapeBase.NOT_SET:
                _params['ticket_id'] = ticket_id
            _request = shapes.StartMatchmakingInput(**_params)
        response = self._boto_client.start_matchmaking(**_request.to_boto())

        return shapes.StartMatchmakingOutput.from_boto(response)

    def stop_fleet_actions(
        self,
        _request: shapes.StopFleetActionsInput = None,
        *,
        fleet_id: str,
        actions: typing.List[typing.Union[str, shapes.FleetAction]],
    ) -> shapes.StopFleetActionsOutput:
        """
        Suspends activity on a fleet. Currently, this operation is used to stop a
        fleet's auto-scaling activity. It is used to temporarily stop scaling events
        triggered by the fleet's scaling policies. The policies can be retained and
        auto-scaling activity can be restarted using StartFleetActions. You can view a
        fleet's stopped actions using DescribeFleetAttributes.

        To stop fleet actions, specify the fleet ID and the type of actions to suspend.
        When auto-scaling fleet actions are stopped, Amazon GameLift no longer initiates
        scaling events except to maintain the fleet's desired instances setting
        (FleetCapacity. Changes to the fleet's capacity must be done manually using
        UpdateFleetCapacity.
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if actions is not ShapeBase.NOT_SET:
                _params['actions'] = actions
            _request = shapes.StopFleetActionsInput(**_params)
        response = self._boto_client.stop_fleet_actions(**_request.to_boto())

        return shapes.StopFleetActionsOutput.from_boto(response)

    def stop_game_session_placement(
        self,
        _request: shapes.StopGameSessionPlacementInput = None,
        *,
        placement_id: str,
    ) -> shapes.StopGameSessionPlacementOutput:
        """
        Cancels a game session placement that is in `PENDING` status. To stop a
        placement, provide the placement ID values. If successful, the placement is
        moved to `CANCELLED` status.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if placement_id is not ShapeBase.NOT_SET:
                _params['placement_id'] = placement_id
            _request = shapes.StopGameSessionPlacementInput(**_params)
        response = self._boto_client.stop_game_session_placement(
            **_request.to_boto()
        )

        return shapes.StopGameSessionPlacementOutput.from_boto(response)

    def stop_matchmaking(
        self,
        _request: shapes.StopMatchmakingInput = None,
        *,
        ticket_id: str,
    ) -> shapes.StopMatchmakingOutput:
        """
        Cancels a matchmaking ticket that is currently being processed. To stop the
        matchmaking operation, specify the ticket ID. If successful, work on the ticket
        is stopped, and the ticket status is changed to `CANCELLED`.

        Matchmaking-related operations include:

          * StartMatchmaking

          * DescribeMatchmaking

          * StopMatchmaking

          * AcceptMatch

          * StartMatchBackfill
        """
        if _request is None:
            _params = {}
            if ticket_id is not ShapeBase.NOT_SET:
                _params['ticket_id'] = ticket_id
            _request = shapes.StopMatchmakingInput(**_params)
        response = self._boto_client.stop_matchmaking(**_request.to_boto())

        return shapes.StopMatchmakingOutput.from_boto(response)

    def update_alias(
        self,
        _request: shapes.UpdateAliasInput = None,
        *,
        alias_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        routing_strategy: shapes.RoutingStrategy = ShapeBase.NOT_SET,
    ) -> shapes.UpdateAliasOutput:
        """
        Updates properties for an alias. To update properties, specify the alias ID to
        be updated and provide the information to be changed. To reassign an alias to
        another fleet, provide an updated routing strategy. If successful, the updated
        alias record is returned.

        Alias-related operations include:

          * CreateAlias

          * ListAliases

          * DescribeAlias

          * UpdateAlias

          * DeleteAlias

          * ResolveAlias
        """
        if _request is None:
            _params = {}
            if alias_id is not ShapeBase.NOT_SET:
                _params['alias_id'] = alias_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if routing_strategy is not ShapeBase.NOT_SET:
                _params['routing_strategy'] = routing_strategy
            _request = shapes.UpdateAliasInput(**_params)
        response = self._boto_client.update_alias(**_request.to_boto())

        return shapes.UpdateAliasOutput.from_boto(response)

    def update_build(
        self,
        _request: shapes.UpdateBuildInput = None,
        *,
        build_id: str,
        name: str = ShapeBase.NOT_SET,
        version: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateBuildOutput:
        """
        Updates metadata in a build record, including the build name and version. To
        update the metadata, specify the build ID to update and provide the new values.
        If successful, a build object containing the updated metadata is returned.

        Build-related operations include:

          * CreateBuild

          * ListBuilds

          * DescribeBuild

          * UpdateBuild

          * DeleteBuild
        """
        if _request is None:
            _params = {}
            if build_id is not ShapeBase.NOT_SET:
                _params['build_id'] = build_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if version is not ShapeBase.NOT_SET:
                _params['version'] = version
            _request = shapes.UpdateBuildInput(**_params)
        response = self._boto_client.update_build(**_request.to_boto())

        return shapes.UpdateBuildOutput.from_boto(response)

    def update_fleet_attributes(
        self,
        _request: shapes.UpdateFleetAttributesInput = None,
        *,
        fleet_id: str,
        name: str = ShapeBase.NOT_SET,
        description: str = ShapeBase.NOT_SET,
        new_game_session_protection_policy: typing.
        Union[str, shapes.ProtectionPolicy] = ShapeBase.NOT_SET,
        resource_creation_limit_policy: shapes.
        ResourceCreationLimitPolicy = ShapeBase.NOT_SET,
        metric_groups: typing.List[str] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFleetAttributesOutput:
        """
        Updates fleet properties, including name and description, for a fleet. To update
        metadata, specify the fleet ID and the property values that you want to change.
        If successful, the fleet ID for the updated fleet is returned.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if new_game_session_protection_policy is not ShapeBase.NOT_SET:
                _params['new_game_session_protection_policy'
                       ] = new_game_session_protection_policy
            if resource_creation_limit_policy is not ShapeBase.NOT_SET:
                _params['resource_creation_limit_policy'
                       ] = resource_creation_limit_policy
            if metric_groups is not ShapeBase.NOT_SET:
                _params['metric_groups'] = metric_groups
            _request = shapes.UpdateFleetAttributesInput(**_params)
        response = self._boto_client.update_fleet_attributes(
            **_request.to_boto()
        )

        return shapes.UpdateFleetAttributesOutput.from_boto(response)

    def update_fleet_capacity(
        self,
        _request: shapes.UpdateFleetCapacityInput = None,
        *,
        fleet_id: str,
        desired_instances: int = ShapeBase.NOT_SET,
        min_size: int = ShapeBase.NOT_SET,
        max_size: int = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFleetCapacityOutput:
        """
        Updates capacity settings for a fleet. Use this action to specify the number of
        EC2 instances (hosts) that you want this fleet to contain. Before calling this
        action, you may want to call DescribeEC2InstanceLimits to get the maximum
        capacity based on the fleet's EC2 instance type.

        Specify minimum and maximum number of instances. Amazon GameLift will not change
        fleet capacity to values fall outside of this range. This is particularly
        important when using auto-scaling (see PutScalingPolicy) to allow capacity to
        adjust based on player demand while imposing limits on automatic adjustments.

        To update fleet capacity, specify the fleet ID and the number of instances you
        want the fleet to host. If successful, Amazon GameLift starts or terminates
        instances so that the fleet's active instance count matches the desired instance
        count. You can view a fleet's current capacity information by calling
        DescribeFleetCapacity. If the desired instance count is higher than the instance
        type's limit, the "Limit Exceeded" exception occurs.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if desired_instances is not ShapeBase.NOT_SET:
                _params['desired_instances'] = desired_instances
            if min_size is not ShapeBase.NOT_SET:
                _params['min_size'] = min_size
            if max_size is not ShapeBase.NOT_SET:
                _params['max_size'] = max_size
            _request = shapes.UpdateFleetCapacityInput(**_params)
        response = self._boto_client.update_fleet_capacity(**_request.to_boto())

        return shapes.UpdateFleetCapacityOutput.from_boto(response)

    def update_fleet_port_settings(
        self,
        _request: shapes.UpdateFleetPortSettingsInput = None,
        *,
        fleet_id: str,
        inbound_permission_authorizations: typing.List[shapes.IpPermission
                                                      ] = ShapeBase.NOT_SET,
        inbound_permission_revocations: typing.List[shapes.IpPermission
                                                   ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateFleetPortSettingsOutput:
        """
        Updates port settings for a fleet. To update settings, specify the fleet ID to
        be updated and list the permissions you want to update. List the permissions you
        want to add in `InboundPermissionAuthorizations`, and permissions you want to
        remove in `InboundPermissionRevocations`. Permissions to be removed must match
        existing fleet permissions. If successful, the fleet ID for the updated fleet is
        returned.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if inbound_permission_authorizations is not ShapeBase.NOT_SET:
                _params['inbound_permission_authorizations'
                       ] = inbound_permission_authorizations
            if inbound_permission_revocations is not ShapeBase.NOT_SET:
                _params['inbound_permission_revocations'
                       ] = inbound_permission_revocations
            _request = shapes.UpdateFleetPortSettingsInput(**_params)
        response = self._boto_client.update_fleet_port_settings(
            **_request.to_boto()
        )

        return shapes.UpdateFleetPortSettingsOutput.from_boto(response)

    def update_game_session(
        self,
        _request: shapes.UpdateGameSessionInput = None,
        *,
        game_session_id: str,
        maximum_player_session_count: int = ShapeBase.NOT_SET,
        name: str = ShapeBase.NOT_SET,
        player_session_creation_policy: typing.
        Union[str, shapes.PlayerSessionCreationPolicy] = ShapeBase.NOT_SET,
        protection_policy: typing.Union[str, shapes.
                                        ProtectionPolicy] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGameSessionOutput:
        """
        Updates game session properties. This includes the session name, maximum player
        count, protection policy, which controls whether or not an active game session
        can be terminated during a scale-down event, and the player session creation
        policy, which controls whether or not new players can join the session. To
        update a game session, specify the game session ID and the values you want to
        change. If successful, an updated GameSession object is returned.

        Game-session-related operations include:

          * CreateGameSession

          * DescribeGameSessions

          * DescribeGameSessionDetails

          * SearchGameSessions

          * UpdateGameSession

          * GetGameSessionLogUrl

          * Game session placements

            * StartGameSessionPlacement

            * DescribeGameSessionPlacement

            * StopGameSessionPlacement
        """
        if _request is None:
            _params = {}
            if game_session_id is not ShapeBase.NOT_SET:
                _params['game_session_id'] = game_session_id
            if maximum_player_session_count is not ShapeBase.NOT_SET:
                _params['maximum_player_session_count'
                       ] = maximum_player_session_count
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if player_session_creation_policy is not ShapeBase.NOT_SET:
                _params['player_session_creation_policy'
                       ] = player_session_creation_policy
            if protection_policy is not ShapeBase.NOT_SET:
                _params['protection_policy'] = protection_policy
            _request = shapes.UpdateGameSessionInput(**_params)
        response = self._boto_client.update_game_session(**_request.to_boto())

        return shapes.UpdateGameSessionOutput.from_boto(response)

    def update_game_session_queue(
        self,
        _request: shapes.UpdateGameSessionQueueInput = None,
        *,
        name: str,
        timeout_in_seconds: int = ShapeBase.NOT_SET,
        player_latency_policies: typing.List[shapes.PlayerLatencyPolicy
                                            ] = ShapeBase.NOT_SET,
        destinations: typing.List[shapes.GameSessionQueueDestination
                                 ] = ShapeBase.NOT_SET,
    ) -> shapes.UpdateGameSessionQueueOutput:
        """
        Updates settings for a game session queue, which determines how new game session
        requests in the queue are processed. To update settings, specify the queue name
        to be updated and provide the new settings. When updating destinations, provide
        a complete list of destinations.

        Queue-related operations include:

          * CreateGameSessionQueue

          * DescribeGameSessionQueues

          * UpdateGameSessionQueue

          * DeleteGameSessionQueue
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if timeout_in_seconds is not ShapeBase.NOT_SET:
                _params['timeout_in_seconds'] = timeout_in_seconds
            if player_latency_policies is not ShapeBase.NOT_SET:
                _params['player_latency_policies'] = player_latency_policies
            if destinations is not ShapeBase.NOT_SET:
                _params['destinations'] = destinations
            _request = shapes.UpdateGameSessionQueueInput(**_params)
        response = self._boto_client.update_game_session_queue(
            **_request.to_boto()
        )

        return shapes.UpdateGameSessionQueueOutput.from_boto(response)

    def update_matchmaking_configuration(
        self,
        _request: shapes.UpdateMatchmakingConfigurationInput = None,
        *,
        name: str,
        description: str = ShapeBase.NOT_SET,
        game_session_queue_arns: typing.List[str] = ShapeBase.NOT_SET,
        request_timeout_seconds: int = ShapeBase.NOT_SET,
        acceptance_timeout_seconds: int = ShapeBase.NOT_SET,
        acceptance_required: bool = ShapeBase.NOT_SET,
        rule_set_name: str = ShapeBase.NOT_SET,
        notification_target: str = ShapeBase.NOT_SET,
        additional_player_count: int = ShapeBase.NOT_SET,
        custom_event_data: str = ShapeBase.NOT_SET,
        game_properties: typing.List[shapes.GameProperty] = ShapeBase.NOT_SET,
        game_session_data: str = ShapeBase.NOT_SET,
    ) -> shapes.UpdateMatchmakingConfigurationOutput:
        """
        Updates settings for a FlexMatch matchmaking configuration. To update settings,
        specify the configuration name to be updated and provide the new settings.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if description is not ShapeBase.NOT_SET:
                _params['description'] = description
            if game_session_queue_arns is not ShapeBase.NOT_SET:
                _params['game_session_queue_arns'] = game_session_queue_arns
            if request_timeout_seconds is not ShapeBase.NOT_SET:
                _params['request_timeout_seconds'] = request_timeout_seconds
            if acceptance_timeout_seconds is not ShapeBase.NOT_SET:
                _params['acceptance_timeout_seconds'
                       ] = acceptance_timeout_seconds
            if acceptance_required is not ShapeBase.NOT_SET:
                _params['acceptance_required'] = acceptance_required
            if rule_set_name is not ShapeBase.NOT_SET:
                _params['rule_set_name'] = rule_set_name
            if notification_target is not ShapeBase.NOT_SET:
                _params['notification_target'] = notification_target
            if additional_player_count is not ShapeBase.NOT_SET:
                _params['additional_player_count'] = additional_player_count
            if custom_event_data is not ShapeBase.NOT_SET:
                _params['custom_event_data'] = custom_event_data
            if game_properties is not ShapeBase.NOT_SET:
                _params['game_properties'] = game_properties
            if game_session_data is not ShapeBase.NOT_SET:
                _params['game_session_data'] = game_session_data
            _request = shapes.UpdateMatchmakingConfigurationInput(**_params)
        response = self._boto_client.update_matchmaking_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateMatchmakingConfigurationOutput.from_boto(response)

    def update_runtime_configuration(
        self,
        _request: shapes.UpdateRuntimeConfigurationInput = None,
        *,
        fleet_id: str,
        runtime_configuration: shapes.RuntimeConfiguration,
    ) -> shapes.UpdateRuntimeConfigurationOutput:
        """
        Updates the current run-time configuration for the specified fleet, which tells
        Amazon GameLift how to launch server processes on instances in the fleet. You
        can update a fleet's run-time configuration at any time after the fleet is
        created; it does not need to be in an `ACTIVE` status.

        To update run-time configuration, specify the fleet ID and provide a
        `RuntimeConfiguration` object with the updated collection of server process
        configurations.

        Each instance in a Amazon GameLift fleet checks regularly for an updated run-
        time configuration and changes how it launches server processes to comply with
        the latest version. Existing server processes are not affected by the update;
        they continue to run until they end, while Amazon GameLift simply adds new
        server processes to fit the current run-time configuration. As a result, the
        run-time configuration changes are applied gradually as existing processes shut
        down and new processes are launched in Amazon GameLift's normal process
        recycling activity.

        Fleet-related operations include:

          * CreateFleet

          * ListFleets

          * DeleteFleet

          * Describe fleets:

            * DescribeFleetAttributes

            * DescribeFleetCapacity

            * DescribeFleetPortSettings

            * DescribeFleetUtilization

            * DescribeRuntimeConfiguration

            * DescribeEC2InstanceLimits

            * DescribeFleetEvents

          * Update fleets:

            * UpdateFleetAttributes

            * UpdateFleetCapacity

            * UpdateFleetPortSettings

            * UpdateRuntimeConfiguration

          * Manage fleet actions:

            * StartFleetActions

            * StopFleetActions
        """
        if _request is None:
            _params = {}
            if fleet_id is not ShapeBase.NOT_SET:
                _params['fleet_id'] = fleet_id
            if runtime_configuration is not ShapeBase.NOT_SET:
                _params['runtime_configuration'] = runtime_configuration
            _request = shapes.UpdateRuntimeConfigurationInput(**_params)
        response = self._boto_client.update_runtime_configuration(
            **_request.to_boto()
        )

        return shapes.UpdateRuntimeConfigurationOutput.from_boto(response)

    def validate_matchmaking_rule_set(
        self,
        _request: shapes.ValidateMatchmakingRuleSetInput = None,
        *,
        rule_set_body: str,
    ) -> shapes.ValidateMatchmakingRuleSetOutput:
        """
        Validates the syntax of a matchmaking rule or rule set. This operation checks
        that the rule set uses syntactically correct JSON and that it conforms to
        allowed property expressions. To validate syntax, provide a rule set string.

        Operations related to match configurations and rule sets include:

          * CreateMatchmakingConfiguration

          * DescribeMatchmakingConfigurations

          * UpdateMatchmakingConfiguration

          * DeleteMatchmakingConfiguration

          * CreateMatchmakingRuleSet

          * DescribeMatchmakingRuleSets

          * ValidateMatchmakingRuleSet
        """
        if _request is None:
            _params = {}
            if rule_set_body is not ShapeBase.NOT_SET:
                _params['rule_set_body'] = rule_set_body
            _request = shapes.ValidateMatchmakingRuleSetInput(**_params)
        response = self._boto_client.validate_matchmaking_rule_set(
            **_request.to_boto()
        )

        return shapes.ValidateMatchmakingRuleSetOutput.from_boto(response)
