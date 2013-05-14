class DatapointsController < ApplicationController
  # GET /datapoints
  # GET /datapoints.json
  def index
    @datapoints = Datapoint.all
    @json = @datapoints.to_gmaps4rails

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @datapoints }
    end
  end

  # GET /datapoints/1
  # GET /datapoints/1.json
  def show
    @datapoint = Datapoint.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @datapoint }
    end
  end

  # GET /datapoints/new
  # GET /datapoints/new.json
  def new
    @datapoint = Datapoint.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @datapoint }
    end
  end

  # GET /datapoints/1/edit
  def edit
    @datapoint = Datapoint.find(params[:id])
  end

  # POST /datapoints
  # POST /datapoints.json
  def create
    @datapoint = Datapoint.new(params[:datapoint])

    respond_to do |format|
      if @datapoint.save
        format.html { redirect_to @datapoint, notice: 'Datapoint was successfully created.' }
        format.json { render json: @datapoint, status: :created, location: @datapoint }
      else
        format.html { render action: "new" }
        format.json { render json: @datapoint.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /datapoints/1
  # PUT /datapoints/1.json
  def update
    @datapoint = Datapoint.find(params[:id])

    respond_to do |format|
      if @datapoint.update_attributes(params[:datapoint])
        format.html { redirect_to @datapoint, notice: 'Datapoint was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @datapoint.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /datapoints/1
  # DELETE /datapoints/1.json
  def destroy
    @datapoint = Datapoint.find(params[:id])
    @datapoint.destroy

    respond_to do |format|
      format.html { redirect_to datapoints_url }
      format.json { head :no_content }
    end
  end

  def remove_all
    Datapoint.delete_all
    flash[:notice] = "You have removed all results!"
    redirect_to datapoints_path
  end

end
