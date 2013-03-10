import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextPane;
import javax.swing.UIManager;
import javax.swing.JList;
import javax.swing.JSlider;
import javax.swing.JButton;
import java.awt.Panel;
import javax.swing.event.ChangeListener;
import javax.swing.event.ChangeEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.ArrayList;
import java.util.List;


public class SetupFrame extends JFrame {
	private static final long serialVersionUID = 1302748744894761036L;
	
	private JPanel contentPane;
	private Panel previewPanel;
	
	private Color currentColor;
	private List<Color> teamColors = new ArrayList<Color>();
	private JList colorDisplayList;
	private JButton addButton;
	private JButton finishedButton;
	
	public boolean isFinished = false;

	
	/**
	 * Create the frame.
	 */
	private SetupFrame(int team) {
		super("Setup For Team "+team);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 323, 192);
		contentPane = new JPanel();
		contentPane.setBackground(UIManager.getColor("Button.background"));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextPane infoTextPane = new JTextPane();
		infoTextPane.setBackground(UIManager.getColor("Button.background"));
		infoTextPane.setEditable(false);
		infoTextPane.setText("Please select your team of colors.\n* Each color is a hue value from 0 to 1.\n* You have 6 colors per team");
		infoTextPane.setBounds(12, 0, 424, 51);
		contentPane.add(infoTextPane);
		
		colorDisplayList = new JList();
		colorDisplayList.setBounds(12, 50, 80, 95);
		colorDisplayList.setLayoutOrientation(JList.VERTICAL);
		contentPane.add(colorDisplayList);		
		
		addButton = new JButton("Add");
		addButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				teamColors.add(currentColor);
				Panel p = new Panel();
				p.setBounds(0, (teamColors.size()-1)*colorDisplayList.getHeight()/6, 100, colorDisplayList.getHeight()/6);
				p.setBackground(currentColor);
				
				colorDisplayList.add(p);
				
				if(teamColors.size()>=6){
					addButton.setEnabled(false);
					finishedButton.setEnabled(true);
				}
			}
		});
		addButton.setBounds(114, 85, 87, 25);
		contentPane.add(addButton);
		
		previewPanel = new Panel();
		previewPanel.setBackground(new Color(255, 0, 0));
		previewPanel.setBounds(207, 80, 92, 64);
		contentPane.add(previewPanel);
		
		finishedButton = new JButton("Done");
		finishedButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				SetupFrame.this.setVisible(false);
				isFinished = true;
				
			}
		});
		finishedButton.setBounds(114, 85+40, 87, 25);
		finishedButton.setEnabled(false);
		contentPane.add(finishedButton);
		
		final JSlider colorSlider = new JSlider();
		colorSlider.addChangeListener(new ChangeListener() {
			public void stateChanged(ChangeEvent e) {
				float hue = ((float) colorSlider.getValue())/colorSlider.getMaximum();
				SetupFrame.this.currentColor = Color.getHSBColor(hue, 1, 1);
				SetupFrame.this.previewPanel.setBackground(SetupFrame.this.currentColor);
			}
		});
		colorSlider.setValue(0);
		colorSlider.setBounds(104, 58, 200, 16);
		contentPane.add(colorSlider);
		
	}
	
	private Color[] getColors(){
		return (Color[]) this.teamColors.toArray(new Color[6]);
	}

	public static Color[] getTeamColors(int teamNumber){
		SetupFrame frame = new SetupFrame(teamNumber);
		frame.setVisible(true);
		while(!frame.isFinished){
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		frame.dispose();
		return frame.getColors();
	}
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		for(Color c:getTeamColors(0)){
			System.out.println(c);
		}
		
//		EventQueue.invokeLater(new Runnable() {
//			public void run() {
//				try {
//					SetupFrame frame = new SetupFrame(1);
//					frame.setVisible(true);
//				} catch (Exception e) {
//					e.printStackTrace();
//				}
//			}
//		});
	}
}
