## StreetView Sampler

This project is still under construction and in an early state.

The objective is to allow for easy random sampling of googles streetview api to return a series of images from a one location or multiple locations. Ultimately this will enable users to apply image recognition techniques to generate comparisons between cities or other geographic sites.

### Getting Started

First install package:

```
pip install streetviewsampler
```

Once package is installed need to setup a project and acquire a google maps api key https://developers.google.com/maps/documentation/streetview/cloud-setup , at time of writing google offers 12 months and $300 free credit for api calls.

### Using Package

Once we have a google api key and the streetviewsampler package is installed we can create a streetviewsampler class by passing our api key as shown below:

```
mysampler = StreetViewSampler(api_key)
```

Next if we want to pull a random image next to a given location we can call

```
mysampler.query_location_random((50.000, 50.000))
```

To pull a random image within a radius of the provided coordinates. If we want to sample a series of images we can use the below command

```
data = [['Portland', 50.00, 50.00], ['Seattle', 60.00, 50.00]]
cities = pd.DataFrame(data, columns = ['City', 'Latitude', 'Longitude])
query_multiple_locations( cities, return_count)
```
