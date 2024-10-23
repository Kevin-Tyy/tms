from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm, DriverAssignForm;
from drivers.models import Driver
from django.db.models import Q

def vehicles_list(request):
  vehicles = Vehicle.objects.all()
  return render(request, 'vehicles-list.html', {'vehicles': vehicles })

    
def create_vehicle(request):
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('vehicle-list')
  else:
    form = VehicleForm()
      
  return render(request, 'create-vehicle.html', {'form': form})


def update_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  if request.method == 'POST':
    form = VehicleForm(request.POST, instance=vehicle)
    if form.is_valid():
      form.save() 
      return redirect('vehicle-list')            
  else:
      form = VehicleForm(instance=vehicle)

  return render(request, 'update-vehicle.html', {'form': form})


def delete_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    vehicle.delete()
    return redirect('vehicle-list')
  
  return render(request, 'delete-vehicle.html', {'vehicle': vehicle})


def assign_driver_to_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    form = DriverAssignForm(request.POST)
    if form.is_valid():
      driver = form.cleaned_data['driver']
      driver.vehicle = vehicle
      driver.save()
      return redirect('vehicle-list')
  else:
      form = DriverAssignForm()

  return render(request, 'assign-driver.html', {'vehicle': vehicle, 'form': form })

def view_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  driver = Driver.objects.filter(vehicle=vehicle).first()
  return render(request, 'view-vehicle.html', {'vehicle': vehicle, 'driver': driver})