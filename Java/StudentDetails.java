import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class StudentDetails extends JFrame
{
	public static void main (String s[])
	{
		String course[] = {"B.Sc(IT)","B.Sc(CS)","BCA"};
		JFrame frame = new JFrame ("Student Details");
		frame.setLayout(new GridLayout(6,2));
		JLabel l1 = new JLabel ("Enter Your Name");
		JTextField t1 = new JTextField();
		JLabel l2 = new JLabel ("Enter Your Roll NO");
		JTextField t2 = new JTextField();
		JLabel l3 = new JLabel ("Select Your Course");
		JComboBox cb = new JComboBox(course);
		JLabel l4 = new JLabel ("Enter Your Subject");
		JTextField t3 = new JTextField();
		JLabel l5 = new JLabel ("Marks / Percentage");
		JTextField t4 = new JTextField();
		JButton b1= new JButton();
		b1.setText("Save");
		b1.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
				b1.setText("Saved Successfully!");
			}
		});
		JButton b2= new JButton();
		b2.setText("Exit");
		b2.addActionListener(new ActionListener()
		{
			public void actionPerformed(ActionEvent e)
			{
					System.exit(0);
			}
		});
		frame.add(l1);
		frame.add(t1);
		frame.add(l2);
		frame.add(t2);
		frame.add(l3);
		frame.add(cb);
		frame.add(l4);
		frame.add(t3);
		frame.add(l5);
		frame.add(t4);
		frame.add(b1);
		frame.add(b2);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(500,450);
		frame.setVisible(true);
	}
}