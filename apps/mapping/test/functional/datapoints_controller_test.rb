require 'test_helper'

class DatapointsControllerTest < ActionController::TestCase
  setup do
    @datapoint = datapoints(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:datapoints)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create datapoint" do
    assert_difference('Datapoint.count') do
      post :create, datapoint: { gmaps: @datapoint.gmaps, latitude: @datapoint.latitude, longitude: @datapoint.longitude, name: @datapoint.name }
    end

    assert_redirected_to datapoint_path(assigns(:datapoint))
  end

  test "should show datapoint" do
    get :show, id: @datapoint
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @datapoint
    assert_response :success
  end

  test "should update datapoint" do
    put :update, id: @datapoint, datapoint: { gmaps: @datapoint.gmaps, latitude: @datapoint.latitude, longitude: @datapoint.longitude, name: @datapoint.name }
    assert_redirected_to datapoint_path(assigns(:datapoint))
  end

  test "should destroy datapoint" do
    assert_difference('Datapoint.count', -1) do
      delete :destroy, id: @datapoint
    end

    assert_redirected_to datapoints_path
  end
end
