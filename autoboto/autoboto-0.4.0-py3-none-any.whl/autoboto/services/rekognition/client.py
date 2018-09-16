import datetime
import typing
import boto3
from autoboto import ClientBase, ShapeBase, OutputShapeBase
from . import shapes


class Client(ClientBase):
    def __init__(self, *args, **kwargs):
        super().__init__("rekognition", *args, **kwargs)

    def compare_faces(
        self,
        _request: shapes.CompareFacesRequest = None,
        *,
        source_image: shapes.Image,
        target_image: shapes.Image,
        similarity_threshold: float = ShapeBase.NOT_SET,
    ) -> shapes.CompareFacesResponse:
        """
        Compares a face in the _source_ input image with each of the 100 largest faces
        detected in the _target_ input image.

        If the source image contains multiple faces, the service detects the largest
        face and compares it with each face detected in the target image.

        You pass the input and target images either as base64-encoded image bytes or as
        a references to images in an Amazon S3 bucket. If you use the Amazon CLI to call
        Amazon Rekognition operations, passing image bytes is not supported. The image
        must be either a PNG or JPEG formatted file.

        In response, the operation returns an array of face matches ordered by
        similarity score in descending order. For each face match, the response provides
        a bounding box of the face, facial landmarks, pose details (pitch, role, and
        yaw), quality (brightness and sharpness), and confidence value (indicating the
        level of confidence that the bounding box contains a face). The response also
        provides a similarity score, which indicates how closely the faces match.

        By default, only faces with a similarity score of greater than or equal to 80%
        are returned in the response. You can change this value by specifying the
        `SimilarityThreshold` parameter.

        `CompareFaces` also returns an array of faces that don't match the source image.
        For each face, it returns a bounding box, confidence value, landmarks, pose
        details, and quality. The response also returns information about the face in
        the source image, including the bounding box of the face and confidence value.

        If the image doesn't contain Exif metadata, `CompareFaces` returns orientation
        information for the source and target images. Use these values to display the
        images with the correct image orientation.

        If no faces are detected in the source or target images, `CompareFaces` returns
        an `InvalidParameterException` error.

        This is a stateless API operation. That is, data returned by this operation
        doesn't persist.

        For an example, see Comparing Faces in Images in the Amazon Rekognition
        Developer Guide.

        This operation requires permissions to perform the `rekognition:CompareFaces`
        action.
        """
        if _request is None:
            _params = {}
            if source_image is not ShapeBase.NOT_SET:
                _params['source_image'] = source_image
            if target_image is not ShapeBase.NOT_SET:
                _params['target_image'] = target_image
            if similarity_threshold is not ShapeBase.NOT_SET:
                _params['similarity_threshold'] = similarity_threshold
            _request = shapes.CompareFacesRequest(**_params)
        response = self._boto_client.compare_faces(**_request.to_boto())

        return shapes.CompareFacesResponse.from_boto(response)

    def create_collection(
        self,
        _request: shapes.CreateCollectionRequest = None,
        *,
        collection_id: str,
    ) -> shapes.CreateCollectionResponse:
        """
        Creates a collection in an AWS Region. You can add faces to the collection using
        the operation.

        For example, you might create collections, one for each of your application
        users. A user can then index faces using the `IndexFaces` operation and persist
        results in a specific collection. Then, a user can search the collection for
        faces in the user-specific container.

        Collection names are case-sensitive.

        This operation requires permissions to perform the
        `rekognition:CreateCollection` action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            _request = shapes.CreateCollectionRequest(**_params)
        response = self._boto_client.create_collection(**_request.to_boto())

        return shapes.CreateCollectionResponse.from_boto(response)

    def create_stream_processor(
        self,
        _request: shapes.CreateStreamProcessorRequest = None,
        *,
        input: shapes.StreamProcessorInput,
        output: shapes.StreamProcessorOutput,
        name: str,
        settings: shapes.StreamProcessorSettings,
        role_arn: str,
    ) -> shapes.CreateStreamProcessorResponse:
        """
        Creates an Amazon Rekognition stream processor that you can use to detect and
        recognize faces in a streaming video.

        Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video
        Streams. Amazon Rekognition Video sends analysis results to Amazon Kinesis Data
        Streams.

        You provide as input a Kinesis video stream (`Input`) and a Kinesis data stream
        (`Output`) stream. You also specify the face recognition criteria in `Settings`.
        For example, the collection containing faces that you want to recognize. Use
        `Name` to assign an identifier for the stream processor. You use `Name` to
        manage the stream processor. For example, you can start processing the source
        video by calling with the `Name` field.

        After you have finished analyzing a streaming video, use to stop processing. You
        can delete the stream processor by calling .
        """
        if _request is None:
            _params = {}
            if input is not ShapeBase.NOT_SET:
                _params['input'] = input
            if output is not ShapeBase.NOT_SET:
                _params['output'] = output
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            if settings is not ShapeBase.NOT_SET:
                _params['settings'] = settings
            if role_arn is not ShapeBase.NOT_SET:
                _params['role_arn'] = role_arn
            _request = shapes.CreateStreamProcessorRequest(**_params)
        response = self._boto_client.create_stream_processor(
            **_request.to_boto()
        )

        return shapes.CreateStreamProcessorResponse.from_boto(response)

    def delete_collection(
        self,
        _request: shapes.DeleteCollectionRequest = None,
        *,
        collection_id: str,
    ) -> shapes.DeleteCollectionResponse:
        """
        Deletes the specified collection. Note that this operation removes all faces in
        the collection. For an example, see delete-collection-procedure.

        This operation requires permissions to perform the
        `rekognition:DeleteCollection` action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            _request = shapes.DeleteCollectionRequest(**_params)
        response = self._boto_client.delete_collection(**_request.to_boto())

        return shapes.DeleteCollectionResponse.from_boto(response)

    def delete_faces(
        self,
        _request: shapes.DeleteFacesRequest = None,
        *,
        collection_id: str,
        face_ids: typing.List[str],
    ) -> shapes.DeleteFacesResponse:
        """
        Deletes faces from a collection. You specify a collection ID and an array of
        face IDs to remove from the collection.

        This operation requires permissions to perform the `rekognition:DeleteFaces`
        action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if face_ids is not ShapeBase.NOT_SET:
                _params['face_ids'] = face_ids
            _request = shapes.DeleteFacesRequest(**_params)
        response = self._boto_client.delete_faces(**_request.to_boto())

        return shapes.DeleteFacesResponse.from_boto(response)

    def delete_stream_processor(
        self,
        _request: shapes.DeleteStreamProcessorRequest = None,
        *,
        name: str,
    ) -> shapes.DeleteStreamProcessorResponse:
        """
        Deletes the stream processor identified by `Name`. You assign the value for
        `Name` when you create the stream processor with . You might not be able to use
        the same name for a stream processor for a few seconds after calling
        `DeleteStreamProcessor`.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DeleteStreamProcessorRequest(**_params)
        response = self._boto_client.delete_stream_processor(
            **_request.to_boto()
        )

        return shapes.DeleteStreamProcessorResponse.from_boto(response)

    def describe_collection(
        self,
        _request: shapes.DescribeCollectionRequest = None,
        *,
        collection_id: str,
    ) -> shapes.DescribeCollectionResponse:
        """
        Describes the specified collection. You can use `DescribeCollection` to get
        information, such as the number of faces indexed into a collection and the
        version of the model used by the collection for face detection.

        For more information, see Describing a Collection in the Amazon Rekognition
        Developer Guide.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            _request = shapes.DescribeCollectionRequest(**_params)
        response = self._boto_client.describe_collection(**_request.to_boto())

        return shapes.DescribeCollectionResponse.from_boto(response)

    def describe_stream_processor(
        self,
        _request: shapes.DescribeStreamProcessorRequest = None,
        *,
        name: str,
    ) -> shapes.DescribeStreamProcessorResponse:
        """
        Provides information about a stream processor created by . You can get
        information about the input and output streams, the input parameters for the
        face recognition being performed, and the current status of the stream
        processor.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.DescribeStreamProcessorRequest(**_params)
        response = self._boto_client.describe_stream_processor(
            **_request.to_boto()
        )

        return shapes.DescribeStreamProcessorResponse.from_boto(response)

    def detect_faces(
        self,
        _request: shapes.DetectFacesRequest = None,
        *,
        image: shapes.Image,
        attributes: typing.List[typing.Union[str, shapes.Attribute]
                               ] = ShapeBase.NOT_SET,
    ) -> shapes.DetectFacesResponse:
        """
        Detects faces within an image that is provided as input.

        `DetectFaces` detects the 100 largest faces in the image. For each face
        detected, the operation returns face details including a bounding box of the
        face, a confidence value (that the bounding box contains a face), and a fixed
        set of attributes such as facial landmarks (for example, coordinates of eye and
        mouth), gender, presence of beard, sunglasses, etc.

        The face-detection algorithm is most effective on frontal faces. For non-frontal
        or obscured faces, the algorithm may not detect the faces or might detect faces
        with lower confidence.

        You pass the input image either as base64-encoded image bytes or as a reference
        to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.

        This is a stateless API operation. That is, the operation does not persist any
        data.

        This operation requires permissions to perform the `rekognition:DetectFaces`
        action.
        """
        if _request is None:
            _params = {}
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if attributes is not ShapeBase.NOT_SET:
                _params['attributes'] = attributes
            _request = shapes.DetectFacesRequest(**_params)
        response = self._boto_client.detect_faces(**_request.to_boto())

        return shapes.DetectFacesResponse.from_boto(response)

    def detect_labels(
        self,
        _request: shapes.DetectLabelsRequest = None,
        *,
        image: shapes.Image,
        max_labels: int = ShapeBase.NOT_SET,
        min_confidence: float = ShapeBase.NOT_SET,
    ) -> shapes.DetectLabelsResponse:
        """
        Detects instances of real-world entities within an image (JPEG or PNG) provided
        as input. This includes objects like flower, tree, and table; events like
        wedding, graduation, and birthday party; and concepts like landscape, evening,
        and nature.

        For an example, see Analyzing Images Stored in an Amazon S3 Bucket in the Amazon
        Rekognition Developer Guide.

        `DetectLabels` does not support the detection of activities. However, activity
        detection is supported for label detection in videos. For more information, see
        StartLabelDetection in the Amazon Rekognition Developer Guide.

        You pass the input image as base64-encoded image bytes or as a reference to an
        image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.

        For each object, scene, and concept the API returns one or more labels. Each
        label provides the object name, and the level of confidence that the image
        contains the object. For example, suppose the input image has a lighthouse, the
        sea, and a rock. The response will include all three labels, one for each
        object.

        `{Name: lighthouse, Confidence: 98.4629}`

        `{Name: rock,Confidence: 79.2097}`

        ` {Name: sea,Confidence: 75.061}`

        In the preceding example, the operation returns one label for each of the three
        objects. The operation can also return multiple labels for the same object in
        the image. For example, if the input image shows a flower (for example, a
        tulip), the operation might return the following three labels.

        `{Name: flower,Confidence: 99.0562}`

        `{Name: plant,Confidence: 99.0562}`

        `{Name: tulip,Confidence: 99.0562}`

        In this example, the detection algorithm more precisely identifies the flower as
        a tulip.

        In response, the API returns an array of labels. In addition, the response also
        includes the orientation correction. Optionally, you can specify `MinConfidence`
        to control the confidence threshold for the labels returned. The default is 50%.
        You can also add the `MaxLabels` parameter to limit the number of labels
        returned.

        If the object detected is a person, the operation doesn't provide the same
        facial details that the DetectFaces operation provides.

        This is a stateless API operation. That is, the operation does not persist any
        data.

        This operation requires permissions to perform the `rekognition:DetectLabels`
        action.
        """
        if _request is None:
            _params = {}
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if max_labels is not ShapeBase.NOT_SET:
                _params['max_labels'] = max_labels
            if min_confidence is not ShapeBase.NOT_SET:
                _params['min_confidence'] = min_confidence
            _request = shapes.DetectLabelsRequest(**_params)
        response = self._boto_client.detect_labels(**_request.to_boto())

        return shapes.DetectLabelsResponse.from_boto(response)

    def detect_moderation_labels(
        self,
        _request: shapes.DetectModerationLabelsRequest = None,
        *,
        image: shapes.Image,
        min_confidence: float = ShapeBase.NOT_SET,
    ) -> shapes.DetectModerationLabelsResponse:
        """
        Detects explicit or suggestive adult content in a specified JPEG or PNG format
        image. Use `DetectModerationLabels` to moderate images depending on your
        requirements. For example, you might want to filter images that contain nudity,
        but not images containing suggestive content.

        To filter images, use the labels returned by `DetectModerationLabels` to
        determine which types of content are appropriate.

        For information about moderation labels, see Detecting Unsafe Content in the
        Amazon Rekognition Developer Guide.

        You pass the input image either as base64-encoded image bytes or as a reference
        to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.
        """
        if _request is None:
            _params = {}
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if min_confidence is not ShapeBase.NOT_SET:
                _params['min_confidence'] = min_confidence
            _request = shapes.DetectModerationLabelsRequest(**_params)
        response = self._boto_client.detect_moderation_labels(
            **_request.to_boto()
        )

        return shapes.DetectModerationLabelsResponse.from_boto(response)

    def detect_text(
        self,
        _request: shapes.DetectTextRequest = None,
        *,
        image: shapes.Image,
    ) -> shapes.DetectTextResponse:
        """
        Detects text in the input image and converts it into machine-readable text.

        Pass the input image as base64-encoded image bytes or as a reference to an image
        in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition
        operations, you must pass it as a reference to an image in an Amazon S3 bucket.
        For the AWS CLI, passing image bytes is not supported. The image must be either
        a .png or .jpeg formatted file.

        The `DetectText` operation returns text in an array of elements,
        `TextDetections`. Each `TextDetection` element provides information about a
        single word or line of text that was detected in the image.

        A word is one or more ISO basic latin script characters that are not separated
        by spaces. `DetectText` can detect up to 50 words in an image.

        A line is a string of equally spaced words. A line isn't necessarily a complete
        sentence. For example, a driver's license number is detected as a line. A line
        ends when there is no aligned text after it. Also, a line ends when there is a
        large gap between words, relative to the length of the words. This means,
        depending on the gap between words, Amazon Rekognition may detect multiple lines
        in text aligned in the same direction. Periods don't represent the end of a
        line. If a sentence spans multiple lines, the `DetectText` operation returns
        multiple lines.

        To determine whether a `TextDetection` element is a line of text or a word, use
        the `TextDetection` object `Type` field.

        To be detected, text must be within +/- 90 degrees orientation of the horizontal
        axis.

        For more information, see DetectText in the Amazon Rekognition Developer Guide.
        """
        if _request is None:
            _params = {}
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            _request = shapes.DetectTextRequest(**_params)
        response = self._boto_client.detect_text(**_request.to_boto())

        return shapes.DetectTextResponse.from_boto(response)

    def get_celebrity_info(
        self,
        _request: shapes.GetCelebrityInfoRequest = None,
        *,
        id: str,
    ) -> shapes.GetCelebrityInfoResponse:
        """
        Gets the name and additional information about a celebrity based on his or her
        Rekognition ID. The additional information is returned as an array of URLs. If
        there is no additional information about the celebrity, this list is empty.

        For more information, see Recognizing Celebrities in an Image in the Amazon
        Rekognition Developer Guide.

        This operation requires permissions to perform the
        `rekognition:GetCelebrityInfo` action.
        """
        if _request is None:
            _params = {}
            if id is not ShapeBase.NOT_SET:
                _params['id'] = id
            _request = shapes.GetCelebrityInfoRequest(**_params)
        response = self._boto_client.get_celebrity_info(**_request.to_boto())

        return shapes.GetCelebrityInfoResponse.from_boto(response)

    def get_celebrity_recognition(
        self,
        _request: shapes.GetCelebrityRecognitionRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.
                              CelebrityRecognitionSortBy] = ShapeBase.NOT_SET,
    ) -> shapes.GetCelebrityRecognitionResponse:
        """
        Gets the celebrity recognition results for a Amazon Rekognition Video analysis
        started by .

        Celebrity recognition in a video is an asynchronous operation. Analysis is
        started by a call to which returns a job identifier (`JobId`). When the
        celebrity recognition operation finishes, Amazon Rekognition Video publishes a
        completion status to the Amazon Simple Notification Service topic registered in
        the initial call to `StartCelebrityRecognition`. To get the results of the
        celebrity recognition analysis, first check that the status value published to
        the Amazon SNS topic is `SUCCEEDED`. If so, call `GetCelebrityDetection` and
        pass the job identifier (`JobId`) from the initial call to
        `StartCelebrityDetection`.

        For more information, see Working With Stored Videos in the Amazon Rekognition
        Developer Guide.

        `GetCelebrityRecognition` returns detected celebrities and the time(s) they are
        detected in an array (`Celebrities`) of objects. Each `CelebrityRecognition`
        contains information about the celebrity in a object and the time, `Timestamp`,
        the celebrity was detected.

        `GetCelebrityRecognition` only returns the default facial attributes
        (`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`). The other
        facial attributes listed in the `Face` object of the following response syntax
        are not returned. For more information, see FaceDetail in the Amazon Rekognition
        Developer Guide.

        By default, the `Celebrities` array is sorted by time (milliseconds from the
        start of the video). You can also sort the array by celebrity by specifying the
        value `ID` in the `SortBy` input parameter.

        The `CelebrityDetail` object includes the celebrity identifer and additional
        information urls. If you don't store the additional information urls, you can
        get them later by calling with the celebrity identifer.

        No information is returned for faces not recognized as celebrities.

        Use MaxResults parameter to limit the number of labels returned. If there are
        more results than specified in `MaxResults`, the value of `NextToken` in the
        operation response contains a pagination token for getting the next set of
        results. To get the next page of results, call `GetCelebrityDetection` and
        populate the `NextToken` request parameter with the token value returned from
        the previous call to `GetCelebrityRecognition`.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            _request = shapes.GetCelebrityRecognitionRequest(**_params)
        response = self._boto_client.get_celebrity_recognition(
            **_request.to_boto()
        )

        return shapes.GetCelebrityRecognitionResponse.from_boto(response)

    def get_content_moderation(
        self,
        _request: shapes.GetContentModerationRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.ContentModerationSortBy] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetContentModerationResponse:
        """
        Gets the content moderation analysis results for a Amazon Rekognition Video
        analysis started by .

        Content moderation analysis of a video is an asynchronous operation. You start
        analysis by calling . which returns a job identifier (`JobId`). When analysis
        finishes, Amazon Rekognition Video publishes a completion status to the Amazon
        Simple Notification Service topic registered in the initial call to
        `StartContentModeration`. To get the results of the content moderation analysis,
        first check that the status value published to the Amazon SNS topic is
        `SUCCEEDED`. If so, call `GetCelebrityDetection` and pass the job identifier
        (`JobId`) from the initial call to `StartCelebrityDetection`.

        For more information, see Working with Stored Videos in the Amazon Rekognition
        Devlopers Guide.

        `GetContentModeration` returns detected content moderation labels, and the time
        they are detected, in an array, `ModerationLabels`, of objects.

        By default, the moderated labels are returned sorted by time, in milliseconds
        from the start of the video. You can also sort them by moderated label by
        specifying `NAME` for the `SortBy` input parameter.

        Since video analysis can return a large number of results, use the `MaxResults`
        parameter to limit the number of labels returned in a single call to
        `GetContentModeration`. If there are more results than specified in
        `MaxResults`, the value of `NextToken` in the operation response contains a
        pagination token for getting the next set of results. To get the next page of
        results, call `GetContentModeration` and populate the `NextToken` request
        parameter with the value of `NextToken` returned from the previous call to
        `GetContentModeration`.

        For more information, see Detecting Unsafe Content in the Amazon Rekognition
        Developer Guide.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            _request = shapes.GetContentModerationRequest(**_params)
        response = self._boto_client.get_content_moderation(
            **_request.to_boto()
        )

        return shapes.GetContentModerationResponse.from_boto(response)

    def get_face_detection(
        self,
        _request: shapes.GetFaceDetectionRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
    ) -> shapes.GetFaceDetectionResponse:
        """
        Gets face detection results for a Amazon Rekognition Video analysis started by .

        Face detection with Amazon Rekognition Video is an asynchronous operation. You
        start face detection by calling which returns a job identifier (`JobId`). When
        the face detection operation finishes, Amazon Rekognition Video publishes a
        completion status to the Amazon Simple Notification Service topic registered in
        the initial call to `StartFaceDetection`. To get the results of the face
        detection operation, first check that the status value published to the Amazon
        SNS topic is `SUCCEEDED`. If so, call and pass the job identifier (`JobId`) from
        the initial call to `StartFaceDetection`.

        `GetFaceDetection` returns an array of detected faces (`Faces`) sorted by the
        time the faces were detected.

        Use MaxResults parameter to limit the number of labels returned. If there are
        more results than specified in `MaxResults`, the value of `NextToken` in the
        operation response contains a pagination token for getting the next set of
        results. To get the next page of results, call `GetFaceDetection` and populate
        the `NextToken` request parameter with the token value returned from the
        previous call to `GetFaceDetection`.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.GetFaceDetectionRequest(**_params)
        response = self._boto_client.get_face_detection(**_request.to_boto())

        return shapes.GetFaceDetectionResponse.from_boto(response)

    def get_face_search(
        self,
        _request: shapes.GetFaceSearchRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.FaceSearchSortBy] = ShapeBase.NOT_SET,
    ) -> shapes.GetFaceSearchResponse:
        """
        Gets the face search results for Amazon Rekognition Video face search started by
        . The search returns faces in a collection that match the faces of persons
        detected in a video. It also includes the time(s) that faces are matched in the
        video.

        Face search in a video is an asynchronous operation. You start face search by
        calling to which returns a job identifier (`JobId`). When the search operation
        finishes, Amazon Rekognition Video publishes a completion status to the Amazon
        Simple Notification Service topic registered in the initial call to
        `StartFaceSearch`. To get the search results, first check that the status value
        published to the Amazon SNS topic is `SUCCEEDED`. If so, call `GetFaceSearch`
        and pass the job identifier (`JobId`) from the initial call to
        `StartFaceSearch`.

        For more information, see Searching Faces in a Collection in the Amazon
        Rekognition Developer Guide.

        The search results are retured in an array, `Persons`, of objects.
        Each`PersonMatch` element contains details about the matching faces in the input
        collection, person information (facial attributes, bounding boxes, and person
        identifer) for the matched person, and the time the person was matched in the
        video.

        `GetFaceSearch` only returns the default facial attributes (`BoundingBox`,
        `Confidence`, `Landmarks`, `Pose`, and `Quality`). The other facial attributes
        listed in the `Face` object of the following response syntax are not returned.
        For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

        By default, the `Persons` array is sorted by the time, in milliseconds from the
        start of the video, persons are matched. You can also sort by persons by
        specifying `INDEX` for the `SORTBY` input parameter.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            _request = shapes.GetFaceSearchRequest(**_params)
        response = self._boto_client.get_face_search(**_request.to_boto())

        return shapes.GetFaceSearchResponse.from_boto(response)

    def get_label_detection(
        self,
        _request: shapes.GetLabelDetectionRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.LabelDetectionSortBy] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetLabelDetectionResponse:
        """
        Gets the label detection results of a Amazon Rekognition Video analysis started
        by .

        The label detection operation is started by a call to which returns a job
        identifier (`JobId`). When the label detection operation finishes, Amazon
        Rekognition publishes a completion status to the Amazon Simple Notification
        Service topic registered in the initial call to `StartlabelDetection`. To get
        the results of the label detection operation, first check that the status value
        published to the Amazon SNS topic is `SUCCEEDED`. If so, call and pass the job
        identifier (`JobId`) from the initial call to `StartLabelDetection`.

        `GetLabelDetection` returns an array of detected labels (`Labels`) sorted by the
        time the labels were detected. You can also sort by the label name by specifying
        `NAME` for the `SortBy` input parameter.

        The labels returned include the label name, the percentage confidence in the
        accuracy of the detected label, and the time the label was detected in the
        video.

        Use MaxResults parameter to limit the number of labels returned. If there are
        more results than specified in `MaxResults`, the value of `NextToken` in the
        operation response contains a pagination token for getting the next set of
        results. To get the next page of results, call `GetlabelDetection` and populate
        the `NextToken` request parameter with the token value returned from the
        previous call to `GetLabelDetection`.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            _request = shapes.GetLabelDetectionRequest(**_params)
        response = self._boto_client.get_label_detection(**_request.to_boto())

        return shapes.GetLabelDetectionResponse.from_boto(response)

    def get_person_tracking(
        self,
        _request: shapes.GetPersonTrackingRequest = None,
        *,
        job_id: str,
        max_results: int = ShapeBase.NOT_SET,
        next_token: str = ShapeBase.NOT_SET,
        sort_by: typing.Union[str, shapes.PersonTrackingSortBy] = ShapeBase.
        NOT_SET,
    ) -> shapes.GetPersonTrackingResponse:
        """
        Gets the person tracking results of a Amazon Rekognition Video analysis started
        by .

        The person detection operation is started by a call to `StartPersonTracking`
        which returns a job identifier (`JobId`). When the person detection operation
        finishes, Amazon Rekognition Video publishes a completion status to the Amazon
        Simple Notification Service topic registered in the initial call to
        `StartPersonTracking`.

        To get the results of the person tracking operation, first check that the status
        value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and pass the
        job identifier (`JobId`) from the initial call to `StartPersonTracking`.

        `GetPersonTracking` returns an array, `Persons`, of tracked persons and the
        time(s) they were tracked in the video.

        `GetPersonTracking` only returns the default facial attributes (`BoundingBox`,
        `Confidence`, `Landmarks`, `Pose`, and `Quality`). The other facial attributes
        listed in the `Face` object of the following response syntax are not returned.

        For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

        By default, the array is sorted by the time(s) a person is tracked in the video.
        You can sort by tracked persons by specifying `INDEX` for the `SortBy` input
        parameter.

        Use the `MaxResults` parameter to limit the number of items returned. If there
        are more results than specified in `MaxResults`, the value of `NextToken` in the
        operation response contains a pagination token for getting the next set of
        results. To get the next page of results, call `GetPersonTracking` and populate
        the `NextToken` request parameter with the token value returned from the
        previous call to `GetPersonTracking`.
        """
        if _request is None:
            _params = {}
            if job_id is not ShapeBase.NOT_SET:
                _params['job_id'] = job_id
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if sort_by is not ShapeBase.NOT_SET:
                _params['sort_by'] = sort_by
            _request = shapes.GetPersonTrackingRequest(**_params)
        response = self._boto_client.get_person_tracking(**_request.to_boto())

        return shapes.GetPersonTrackingResponse.from_boto(response)

    def index_faces(
        self,
        _request: shapes.IndexFacesRequest = None,
        *,
        collection_id: str,
        image: shapes.Image,
        external_image_id: str = ShapeBase.NOT_SET,
        detection_attributes: typing.List[typing.Union[str, shapes.Attribute]
                                         ] = ShapeBase.NOT_SET,
    ) -> shapes.IndexFacesResponse:
        """
        Detects faces in the input image and adds them to the specified collection.

        Amazon Rekognition does not save the actual faces detected. Instead, the
        underlying detection algorithm first detects the faces in the input image, and
        for each face extracts facial features into a feature vector, and stores it in
        the back-end database. Amazon Rekognition uses feature vectors when performing
        face match and search operations using the and operations.

        To get the number of faces in a collection, call .

        If you are using version 1.0 of the face detection model, `IndexFaces` indexes
        the 15 largest faces in the input image. Later versions of the face detection
        model index the 100 largest faces in the input image. To determine which version
        of the model you are using, call and supply the collection ID. You also get the
        model version from the value of `FaceModelVersion` in the response from
        `IndexFaces`.

        For more information, see Model Versioning in the Amazon Rekognition Developer
        Guide.

        If you provide the optional `ExternalImageID` for the input image you provided,
        Amazon Rekognition associates this ID with all faces that it detects. When you
        call the operation, the response returns the external ID. You can use this
        external image ID to create a client-side index to associate the faces with each
        image. You can then use the index to find all faces in an image.

        In response, the operation returns an array of metadata for all detected faces.
        This includes, the bounding box of the detected face, confidence value
        (indicating the bounding box contains a face), a face ID assigned by the service
        for each face that is detected and stored, and an image ID assigned by the
        service for the input image. If you request all facial attributes (using the
        `detectionAttributes` parameter, Amazon Rekognition returns detailed facial
        attributes such as facial landmarks (for example, location of eye and mouth) and
        other facial attributes such gender. If you provide the same image, specify the
        same collection, and use the same external ID in the `IndexFaces` operation,
        Amazon Rekognition doesn't save duplicate face metadata.

        For more information, see Adding Faces to a Collection in the Amazon Rekognition
        Developer Guide.

        The input image is passed either as base64-encoded image bytes or as a reference
        to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.

        This operation requires permissions to perform the `rekognition:IndexFaces`
        action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if external_image_id is not ShapeBase.NOT_SET:
                _params['external_image_id'] = external_image_id
            if detection_attributes is not ShapeBase.NOT_SET:
                _params['detection_attributes'] = detection_attributes
            _request = shapes.IndexFacesRequest(**_params)
        response = self._boto_client.index_faces(**_request.to_boto())

        return shapes.IndexFacesResponse.from_boto(response)

    def list_collections(
        self,
        _request: shapes.ListCollectionsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListCollectionsResponse:
        """
        Returns list of collection IDs in your account. If the result is truncated, the
        response also provides a `NextToken` that you can use in the subsequent request
        to fetch the next set of collection IDs.

        For an example, see Listing Collections in the Amazon Rekognition Developer
        Guide.

        This operation requires permissions to perform the `rekognition:ListCollections`
        action.
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListCollectionsRequest(**_params)
        paginator = self.get_paginator("list_collections").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListCollectionsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListCollectionsResponse.from_boto(response)

    def list_faces(
        self,
        _request: shapes.ListFacesRequest = None,
        *,
        collection_id: str,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListFacesResponse:
        """
        Returns metadata for faces in the specified collection. This metadata includes
        information such as the bounding box coordinates, the confidence (that the
        bounding box contains a face), and face ID. For an example, see Listing Faces in
        a Collection in the Amazon Rekognition Developer Guide.

        This operation requires permissions to perform the `rekognition:ListFaces`
        action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListFacesRequest(**_params)
        paginator = self.get_paginator("list_faces").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListFacesResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListFacesResponse.from_boto(response)

    def list_stream_processors(
        self,
        _request: shapes.ListStreamProcessorsRequest = None,
        *,
        next_token: str = ShapeBase.NOT_SET,
        max_results: int = ShapeBase.NOT_SET,
    ) -> shapes.ListStreamProcessorsResponse:
        """
        Gets a list of stream processors that you have created with .
        """
        if _request is None:
            _params = {}
            if next_token is not ShapeBase.NOT_SET:
                _params['next_token'] = next_token
            if max_results is not ShapeBase.NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.ListStreamProcessorsRequest(**_params)
        paginator = self.get_paginator("list_stream_processors").paginate(
            **_request.to_boto()
        )
        page_generator = (page for page in paginator)
        first_page = next(page_generator)
        result = shapes.ListStreamProcessorsResponse.from_boto(first_page)
        result._page_iterator = page_generator
        return result

        return shapes.ListStreamProcessorsResponse.from_boto(response)

    def recognize_celebrities(
        self,
        _request: shapes.RecognizeCelebritiesRequest = None,
        *,
        image: shapes.Image,
    ) -> shapes.RecognizeCelebritiesResponse:
        """
        Returns an array of celebrities recognized in the input image. For more
        information, see Recognizing Celebrities in the Amazon Rekognition Developer
        Guide.

        `RecognizeCelebrities` returns the 100 largest faces in the image. It lists
        recognized celebrities in the `CelebrityFaces` array and unrecognized faces in
        the `UnrecognizedFaces` array. `RecognizeCelebrities` doesn't return celebrities
        whose faces are not amongst the largest 100 faces in the image.

        For each celebrity recognized, the `RecognizeCelebrities` returns a `Celebrity`
        object. The `Celebrity` object contains the celebrity name, ID, URL links to
        additional information, match confidence, and a `ComparedFace` object that you
        can use to locate the celebrity's face on the image.

        Rekognition does not retain information about which images a celebrity has been
        recognized in. Your application must store this information and use the
        `Celebrity` ID property as a unique identifier for the celebrity. If you don't
        store the celebrity name or additional information URLs returned by
        `RecognizeCelebrities`, you will need the ID to identify the celebrity in a call
        to the operation.

        You pass the imput image either as base64-encoded image bytes or as a reference
        to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.

        For an example, see Recognizing Celebrities in an Image in the Amazon
        Rekognition Developer Guide.

        This operation requires permissions to perform the
        `rekognition:RecognizeCelebrities` operation.
        """
        if _request is None:
            _params = {}
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            _request = shapes.RecognizeCelebritiesRequest(**_params)
        response = self._boto_client.recognize_celebrities(**_request.to_boto())

        return shapes.RecognizeCelebritiesResponse.from_boto(response)

    def search_faces(
        self,
        _request: shapes.SearchFacesRequest = None,
        *,
        collection_id: str,
        face_id: str,
        max_faces: int = ShapeBase.NOT_SET,
        face_match_threshold: float = ShapeBase.NOT_SET,
    ) -> shapes.SearchFacesResponse:
        """
        For a given input face ID, searches for matching faces in the collection the
        face belongs to. You get a face ID when you add a face to the collection using
        the IndexFaces operation. The operation compares the features of the input face
        with faces in the specified collection.

        You can also search faces without indexing faces by using the
        `SearchFacesByImage` operation.

        The operation response returns an array of faces that match, ordered by
        similarity score with the highest similarity first. More specifically, it is an
        array of metadata for each face match that is found. Along with the metadata,
        the response also includes a `confidence` value for each face match, indicating
        the confidence that the specific face matches the input face.

        For an example, see Searching for a Face Using Its Face ID in the Amazon
        Rekognition Developer Guide.

        This operation requires permissions to perform the `rekognition:SearchFaces`
        action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if face_id is not ShapeBase.NOT_SET:
                _params['face_id'] = face_id
            if max_faces is not ShapeBase.NOT_SET:
                _params['max_faces'] = max_faces
            if face_match_threshold is not ShapeBase.NOT_SET:
                _params['face_match_threshold'] = face_match_threshold
            _request = shapes.SearchFacesRequest(**_params)
        response = self._boto_client.search_faces(**_request.to_boto())

        return shapes.SearchFacesResponse.from_boto(response)

    def search_faces_by_image(
        self,
        _request: shapes.SearchFacesByImageRequest = None,
        *,
        collection_id: str,
        image: shapes.Image,
        max_faces: int = ShapeBase.NOT_SET,
        face_match_threshold: float = ShapeBase.NOT_SET,
    ) -> shapes.SearchFacesByImageResponse:
        """
        For a given input image, first detects the largest face in the image, and then
        searches the specified collection for matching faces. The operation compares the
        features of the input face with faces in the specified collection.

        To search for all faces in an input image, you might first call the operation,
        and then use the face IDs returned in subsequent calls to the operation.

        You can also call the `DetectFaces` operation and use the bounding boxes in the
        response to make face crops, which then you can pass in to the
        `SearchFacesByImage` operation.

        You pass the input image either as base64-encoded image bytes or as a reference
        to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon
        Rekognition operations, passing image bytes is not supported. The image must be
        either a PNG or JPEG formatted file.

        The response returns an array of faces that match, ordered by similarity score
        with the highest similarity first. More specifically, it is an array of metadata
        for each face match found. Along with the metadata, the response also includes a
        `similarity` indicating how similar the face is to the input face. In the
        response, the operation also returns the bounding box (and a confidence level
        that the bounding box contains a face) of the face that Amazon Rekognition used
        for the input image.

        For an example, Searching for a Face Using an Image in the Amazon Rekognition
        Developer Guide.

        This operation requires permissions to perform the
        `rekognition:SearchFacesByImage` action.
        """
        if _request is None:
            _params = {}
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if image is not ShapeBase.NOT_SET:
                _params['image'] = image
            if max_faces is not ShapeBase.NOT_SET:
                _params['max_faces'] = max_faces
            if face_match_threshold is not ShapeBase.NOT_SET:
                _params['face_match_threshold'] = face_match_threshold
            _request = shapes.SearchFacesByImageRequest(**_params)
        response = self._boto_client.search_faces_by_image(**_request.to_boto())

        return shapes.SearchFacesByImageResponse.from_boto(response)

    def start_celebrity_recognition(
        self,
        _request: shapes.StartCelebrityRecognitionRequest = None,
        *,
        video: shapes.Video,
        client_request_token: str = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartCelebrityRecognitionResponse:
        """
        Starts asynchronous recognition of celebrities in a stored video.

        Amazon Rekognition Video can detect celebrities in a video must be stored in an
        Amazon S3 bucket. Use Video to specify the bucket name and the filename of the
        video. `StartCelebrityRecognition` returns a job identifier (`JobId`) which you
        use to get the results of the analysis. When celebrity recognition analysis is
        finished, Amazon Rekognition Video publishes a completion status to the Amazon
        Simple Notification Service topic that you specify in `NotificationChannel`. To
        get the results of the celebrity recognition analysis, first check that the
        status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and
        pass the job identifier (`JobId`) from the initial call to
        `StartCelebrityRecognition`.

        For more information, see Recognizing Celebrities in the Amazon Rekognition
        Developer Guide.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartCelebrityRecognitionRequest(**_params)
        response = self._boto_client.start_celebrity_recognition(
            **_request.to_boto()
        )

        return shapes.StartCelebrityRecognitionResponse.from_boto(response)

    def start_content_moderation(
        self,
        _request: shapes.StartContentModerationRequest = None,
        *,
        video: shapes.Video,
        min_confidence: float = ShapeBase.NOT_SET,
        client_request_token: str = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartContentModerationResponse:
        """
        Starts asynchronous detection of explicit or suggestive adult content in a
        stored video.

        Amazon Rekognition Video can moderate content in a video stored in an Amazon S3
        bucket. Use Video to specify the bucket name and the filename of the video.
        `StartContentModeration` returns a job identifier (`JobId`) which you use to get
        the results of the analysis. When content moderation analysis is finished,
        Amazon Rekognition Video publishes a completion status to the Amazon Simple
        Notification Service topic that you specify in `NotificationChannel`.

        To get the results of the content moderation analysis, first check that the
        status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and
        pass the job identifier (`JobId`) from the initial call to
        `StartContentModeration`.

        For more information, see Detecting Unsafe Content in the Amazon Rekognition
        Developer Guide.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if min_confidence is not ShapeBase.NOT_SET:
                _params['min_confidence'] = min_confidence
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartContentModerationRequest(**_params)
        response = self._boto_client.start_content_moderation(
            **_request.to_boto()
        )

        return shapes.StartContentModerationResponse.from_boto(response)

    def start_face_detection(
        self,
        _request: shapes.StartFaceDetectionRequest = None,
        *,
        video: shapes.Video,
        client_request_token: str = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        face_attributes: typing.Union[str, shapes.FaceAttributes] = ShapeBase.
        NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartFaceDetectionResponse:
        """
        Starts asynchronous detection of faces in a stored video.

        Amazon Rekognition Video can detect faces in a video stored in an Amazon S3
        bucket. Use Video to specify the bucket name and the filename of the video.
        `StartFaceDetection` returns a job identifier (`JobId`) that you use to get the
        results of the operation. When face detection is finished, Amazon Rekognition
        Video publishes a completion status to the Amazon Simple Notification Service
        topic that you specify in `NotificationChannel`. To get the results of the label
        detection operation, first check that the status value published to the Amazon
        SNS topic is `SUCCEEDED`. If so, call and pass the job identifier (`JobId`) from
        the initial call to `StartFaceDetection`.

        For more information, see Detecting Faces in a Stored Video in the Amazon
        Rekognition Developer Guide.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if face_attributes is not ShapeBase.NOT_SET:
                _params['face_attributes'] = face_attributes
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartFaceDetectionRequest(**_params)
        response = self._boto_client.start_face_detection(**_request.to_boto())

        return shapes.StartFaceDetectionResponse.from_boto(response)

    def start_face_search(
        self,
        _request: shapes.StartFaceSearchRequest = None,
        *,
        video: shapes.Video,
        collection_id: str,
        client_request_token: str = ShapeBase.NOT_SET,
        face_match_threshold: float = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartFaceSearchResponse:
        """
        Starts the asynchronous search for faces in a collection that match the faces of
        persons detected in a stored video.

        The video must be stored in an Amazon S3 bucket. Use Video to specify the bucket
        name and the filename of the video. `StartFaceSearch` returns a job identifier
        (`JobId`) which you use to get the search results once the search has completed.
        When searching is finished, Amazon Rekognition Video publishes a completion
        status to the Amazon Simple Notification Service topic that you specify in
        `NotificationChannel`. To get the search results, first check that the status
        value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and pass the
        job identifier (`JobId`) from the initial call to `StartFaceSearch`. For more
        information, see procedure-person-search-videos.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if collection_id is not ShapeBase.NOT_SET:
                _params['collection_id'] = collection_id
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if face_match_threshold is not ShapeBase.NOT_SET:
                _params['face_match_threshold'] = face_match_threshold
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartFaceSearchRequest(**_params)
        response = self._boto_client.start_face_search(**_request.to_boto())

        return shapes.StartFaceSearchResponse.from_boto(response)

    def start_label_detection(
        self,
        _request: shapes.StartLabelDetectionRequest = None,
        *,
        video: shapes.Video,
        client_request_token: str = ShapeBase.NOT_SET,
        min_confidence: float = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartLabelDetectionResponse:
        """
        Starts asynchronous detection of labels in a stored video.

        Amazon Rekognition Video can detect labels in a video. Labels are instances of
        real-world entities. This includes objects like flower, tree, and table; events
        like wedding, graduation, and birthday party; concepts like landscape, evening,
        and nature; and activities like a person getting out of a car or a person
        skiing.

        The video must be stored in an Amazon S3 bucket. Use Video to specify the bucket
        name and the filename of the video. `StartLabelDetection` returns a job
        identifier (`JobId`) which you use to get the results of the operation. When
        label detection is finished, Amazon Rekognition Video publishes a completion
        status to the Amazon Simple Notification Service topic that you specify in
        `NotificationChannel`.

        To get the results of the label detection operation, first check that the status
        value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and pass the
        job identifier (`JobId`) from the initial call to `StartLabelDetection`.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if min_confidence is not ShapeBase.NOT_SET:
                _params['min_confidence'] = min_confidence
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartLabelDetectionRequest(**_params)
        response = self._boto_client.start_label_detection(**_request.to_boto())

        return shapes.StartLabelDetectionResponse.from_boto(response)

    def start_person_tracking(
        self,
        _request: shapes.StartPersonTrackingRequest = None,
        *,
        video: shapes.Video,
        client_request_token: str = ShapeBase.NOT_SET,
        notification_channel: shapes.NotificationChannel = ShapeBase.NOT_SET,
        job_tag: str = ShapeBase.NOT_SET,
    ) -> shapes.StartPersonTrackingResponse:
        """
        Starts the asynchronous tracking of persons in a stored video.

        Amazon Rekognition Video can track persons in a video stored in an Amazon S3
        bucket. Use Video to specify the bucket name and the filename of the video.
        `StartPersonTracking` returns a job identifier (`JobId`) which you use to get
        the results of the operation. When label detection is finished, Amazon
        Rekognition publishes a completion status to the Amazon Simple Notification
        Service topic that you specify in `NotificationChannel`.

        To get the results of the person detection operation, first check that the
        status value published to the Amazon SNS topic is `SUCCEEDED`. If so, call and
        pass the job identifier (`JobId`) from the initial call to
        `StartPersonTracking`.
        """
        if _request is None:
            _params = {}
            if video is not ShapeBase.NOT_SET:
                _params['video'] = video
            if client_request_token is not ShapeBase.NOT_SET:
                _params['client_request_token'] = client_request_token
            if notification_channel is not ShapeBase.NOT_SET:
                _params['notification_channel'] = notification_channel
            if job_tag is not ShapeBase.NOT_SET:
                _params['job_tag'] = job_tag
            _request = shapes.StartPersonTrackingRequest(**_params)
        response = self._boto_client.start_person_tracking(**_request.to_boto())

        return shapes.StartPersonTrackingResponse.from_boto(response)

    def start_stream_processor(
        self,
        _request: shapes.StartStreamProcessorRequest = None,
        *,
        name: str,
    ) -> shapes.StartStreamProcessorResponse:
        """
        Starts processing a stream processor. You create a stream processor by calling .
        To tell `StartStreamProcessor` which stream processor to start, use the value of
        the `Name` field specified in the call to `CreateStreamProcessor`.
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StartStreamProcessorRequest(**_params)
        response = self._boto_client.start_stream_processor(
            **_request.to_boto()
        )

        return shapes.StartStreamProcessorResponse.from_boto(response)

    def stop_stream_processor(
        self,
        _request: shapes.StopStreamProcessorRequest = None,
        *,
        name: str,
    ) -> shapes.StopStreamProcessorResponse:
        """
        Stops a running stream processor that was created by .
        """
        if _request is None:
            _params = {}
            if name is not ShapeBase.NOT_SET:
                _params['name'] = name
            _request = shapes.StopStreamProcessorRequest(**_params)
        response = self._boto_client.stop_stream_processor(**_request.to_boto())

        return shapes.StopStreamProcessorResponse.from_boto(response)
