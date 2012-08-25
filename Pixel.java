import java.awt.Color;

public class Pixel{
    public final Vec2 position;
    public final Color color;

    private final Window window;

    public Pixel(Vec2 position, Color color,Window window){
        this.position = position;
        this.color    = color;
        this.window   = window;
    }

    public void setColor(Color c){
        window.setColor(this.position,c);
    }

    public String toString(){
        return position.toString() + " " + color.toString();
    }
}
