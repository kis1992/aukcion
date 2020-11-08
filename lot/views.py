from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from lot import serializers, models

class LotViews(APIView):

    class_serializer = serializers.LotSerializers
    image =  models.Lot.objects.get(id=2).lot_image

    def get(self, request):
        lots = models.Lot.objects.all()
        serializer_elem=self.class_serializer(lots,many=True)
        return Response(serializer_elem.data)

    def post(self, request):
        request.data['lot_image'] = self.image
        lot = request.data
        serializer_elem = self.class_serializer(data=lot)

        if serializer_elem.is_valid():
            serializer_elem.save()
            return Response(serializer_elem.data)

        return Response({"status": "faild", "message": serializer_elem.errors})

class LotPutDelete(APIView):

    class_serializer = serializers.LotSerializers
    image =  models.Lot.objects.get(id=2).lot_image

    def query_get_lot_by_id(self,id):
        lot = None
        try:
            lot = models.Lot.objects.get(id=id)
        except models.Lot.DoesNotExist:
            return 'Model not exist!'
        return lot

    def get(self, request, id):
        lot = self.query_get_lot_by_id(id)

        if not lot:
            return Response({"message":"NOT FOUND"})
        
        serializer = self.class_serializer(lot)

        return Response(serializer.data)

    def put(self, request, id):

        lot = self.query_get_lot_by_id(id)

        if not lot:
            return Response({"message":"NOT FOUND"})

        request.data["lot_image"] = self.image
                
        serializer = self.class_serializer(lot, data = request.data)
        print('serialaizer are created')

        if serializer.is_valid():
            serializer.save()
            print('serialaizer are saved')
            return Response({"success": "Article updated successfully"})
        else:
            return Response({"message": serializer.errors})
        

    def delete(self, request, id):
        lot = self.query_get_lot_by_id(id)

        if not lot:
            return Response({"message":"NOT FOUND"})

        lot.delete()
        return Response({
            "message": "DELETE"
        })