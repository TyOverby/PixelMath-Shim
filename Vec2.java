public class Vec2{
    public float x;
    public float y;

    public Vec2(float x, float y){
        this.x = x;
        this.y = y;
    }
    public Vec2(Vec2 other){
        this.x = other.x;
        this.y = other.y;
    }

    public Vec2 clone(){
        return new Vec2(this.x, this.y);
    }

    public Vec2 plus(float x, float y){
        return new Vec2(this.x+x, this.y+y);
    }
    public Vec2 plus(Vec2 other){
        return this.plus(other.x, other.y);
    }

    public Vec2 plusEquals(float x, float y){
        this.x += x;
        this.y += y;
        return this;
    }
    public Vec2 PlusEquals(Vec2 other){
        return this.plusEquals(other.x, other.y);
    }

    public Vec2 minus(float x, float y){
        return new Vec2(this.x - x, this.y - y);
    }
    public Vec2 minus(Vec2 other){
        return this.minus(other.x, other.y);
    }

    public Vec2 minusEquals(float x, float y){
        this.x -= x;
        this.y -= y;
        return this;
    }
    public Vec2 minusEquals(Vec2 other){
        return this.minusEquals(other.x, other.y);
    }

    public Vec2 scaled(float scalar){
        return new Vec2(this.x * scalar, this.y * scalar);
    }
    public Vec2 scale(float scalar){
        this.x *= scalar;
        this.y *= scalar;
        return this;
    }

    public Vec2 normalise(){
        float l = this.getLength();

        if(l == 0){
            return this;
        }

        x/=l;
        y/=l;
        return this;

    }
    public Vec2 normalized(){
        return this.clone().normalise();
    }

    public float getLength(){
        return (float) Math.sqrt(this.x * this.x + this.y * this.y);
    }

    public float getRotation(){
        double theta = Math.toDegrees(Math.atan2(y, x));
        if ((theta < -360) || (theta > 360)) {
            theta = theta % 360;
        }
        if (theta < 0) {
            theta = 360 + theta;
        }

        return (float) theta;
    }
}
