from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .permissions import IsOwnerOrIsAdmin
from .models import Tracker
from .serializers import TrackerSerializer, TrackerDetailSerializer, TrackerCreateSerializer, TrackerUpdateSerializer


class TrackerView(APIView):
    permission_classes = [IsOwnerOrIsAdmin]    

    def get(self, request): # 해당 유저 트래커 모두 불러오기
        trackers=Tracker.objects.filter(user_id=request.user.id)
        serializer=TrackerSerializer(trackers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request): # 트래커 작성
        serializer = TrackerCreateSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, tracker_id): 
        tracker=get_object_or_404(Tracker, id=tracker_id)
        if request.user==tracker.user:
            serializer = TrackerUpdateSerializer(tracker, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('본인의 가계부만 수정이 가능합니다.', status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, tracker_id):
        tracker=get_object_or_404(Tracker, id=tracker_id)
        if request.user==tracker.user:
            tracker.delete()
            return Response('가계부가 삭제되었습니다',status=status.HTTP_403_FORBIDDEN)
            

class TrackerDetailView(APIView):
    permission_classes = [IsOwnerOrIsAdmin]  

    def get(self, request, tracker_id):
        tracker=get_object_or_404(Tracker, id=tracker_id)
        serializer=TrackerDetailSerializer(tracker)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, tracker_id):
        tracker=get_object_or_404(Tracker, id=tracker_id)
        if request.user==tracker.user:
            serializer = TrackerUpdateSerializer(tracker, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('본인의 가계부만 수정이 가능합니다.', status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, tracker_id):
        tracker=get_object_or_404(Tracker, id=tracker_id)
        if request.user==tracker.user:
            tracker.delete()
            return Response('가계부가 삭제되었습니다.',status=status.HTTP_204_NO_CONTENT)
        return Response('본인의 가계부만 삭제가 가능합니다.',status=status.HTTP_403_FORBIDDEN)