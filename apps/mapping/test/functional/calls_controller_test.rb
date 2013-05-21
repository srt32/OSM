require 'test_helper'

class CallsControllerTest < ActionController::TestCase
  setup do
    @call = calls(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:calls)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create call" do
    assert_difference('Call.count') do
      post :create, call: { API_response_filename: @call.API_response_filename, DP_DB_filename: @call.DP_DB_filename, DP_rails_filename: @call.DP_rails_filename, school_data_filename: @call.school_data_filename, school_name: @call.school_name, script_name: @call.script_name }
    end

    assert_redirected_to call_path(assigns(:call))
  end

  test "should show call" do
    get :show, id: @call
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @call
    assert_response :success
  end

  test "should update call" do
    put :update, id: @call, call: { API_response_filename: @call.API_response_filename, DP_DB_filename: @call.DP_DB_filename, DP_rails_filename: @call.DP_rails_filename, school_data_filename: @call.school_data_filename, school_name: @call.school_name, script_name: @call.script_name }
    assert_redirected_to call_path(assigns(:call))
  end

  test "should destroy call" do
    assert_difference('Call.count', -1) do
      delete :destroy, id: @call
    end

    assert_redirected_to calls_path
  end
end
