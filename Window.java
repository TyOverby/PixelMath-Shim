import java.awt.Color;
import java.util.Iterator;

public class Window{
    private static PixelMathAbstractionInterface pm;

    public static void init(PixelMathAbstractionInterface pm){
        Window.pm = pm;
    }

    public final int id;

    private Window(String filename, String title, Vec2 dimensions, Color color){
        this.id = pm.newImage(0, title, (int) dimensions.x, (int) dimensions.y,
                                color.getRed(), color.getGreen(), color.getBlue());
        if(filename != null){
            pm.openImage(this.id,filename);
        }
    }

    public Window(String filename, Vec2 dimensions){
        this(filename, "Title", dimensions, Color.BLACK);
    }
    public Window(Vec2 dimensions){
        this(null,dimensions);
    }

    public Window(int id){
        this.id = id;
    }

    public static Window newBlank(Vec2 dimensions){
        return new Window(null,"Blank Window",dimensions,Color.BLACK);
    }

    public Color getColor(Vec2 position){
        return new Color(pm.getPixelQuickly(this.id,(int) position.x, (int)position.y));
    }

    public void setColor(Vec2 position, Color color){
        pm.setPixelQuickly(this.id, position.x, position.y, color.getRGB());
    }

    public Vec2 getSize(){
        return new Vec2(pm.getImageWidth(this.id),pm.getImageHeight(this.id));
    }

    public int getWidth(){
        return pm.getImageWidth(this.id);
    }

    public int getHeight(){
        return pm.getImageHeight(this.id);
    }

    public void refresh(){
        pm.refresh(this.id);
    }

    public Iterator<Vec2> positions(){
        return new Iterator<Vec2>(){
            Vec2 size = Window.this.getSize();
            int length = (int) ((size.x+1)*(size.y));
            int i = 0;

            int x = 0;
            int y = 0;

            public boolean hasNext(){
                //System.out.println("w: "+size.x+" h: "+size.y);
                System.out.println("x: "+x+" y: "+y+" i: "+i+" len "+length);
                return i<length;
            }
            public Vec2 next(){
                i++;
                if(x<size.x){
                    return new Vec2(x++,y);
                }
                else{
                    return new Vec2(x=0,y++);
                }

            }
            public void remove(){
                return;
            }

        };
    }

    public Iterator<Color> colors(){
        final Iterator<Vec2> posIterator = Window.this.positions();
        return new Iterator<Color>(){
            public boolean hasNext(){
                return posIterator.hasNext();
            }
            public Color next(){
                return Window.this.getColor(posIterator.next());
            }
            public void remove(){
                return;
            }

        };
    }

    public Iterator<Pixel> pixels(){
        final Iterator<Vec2> posIterator = Window.this.positions();
        return new Iterator<Pixel>(){
            public boolean hasNext(){
                return posIterator.hasNext();
            }
            public Pixel next(){
                Vec2 nextPos = posIterator.next();
                return new Pixel(nextPos,Window.this.getColor(nextPos), Window.this);
            }
            public void remove(){
                return;
            }
        };
    }
}
